import pandas as pd
from db_connector import conectar
from sqlalchemy import text
import os

# PALABRAS COLUMNAS BASURA
PALABRAS_BASURA = ["interno", "legacy", "sistema", "hash", "viejo", "antiguo", "backup", "notas", "barras", "modificacion"]
UMBRAL_NULOS = 0.8

def es_columna_basura(df, columna):
    """
    Detecta si una columna es basura basándose en 3 reglas:
    1. Varianza cero — siempre el mismo valor
    2. Más del 80% nulos Y nombre sospechoso
    3. Duplicado exacto de otra columna
    """
    # Regla 1 — varianza cero
    if df[columna].nunique() <= 1:
        return True
    
    # Regla 2 — muchos nulos y nombre sospechoso
    porcentaje_nulos = df[columna].isna().mean()
    nombre_sospechoso = any(palabra in columna.lower() for palabra in PALABRAS_BASURA)
    if porcentaje_nulos > UMBRAL_NULOS and nombre_sospechoso:
        return True
    
    # Regla 3 — duplicado de otra columna
    for otra_columna in df.columns:
        if otra_columna != columna and df[columna].equals(df[otra_columna]):
            return True
    
    return False

def normalizar_fecha(valor):
    """
    Intenta convertir cualquier formato de fecha a YYYY-MM-DD.
    Si no puede, devuelve None.
    """
    if pd.isna(valor):
        return None
    
    formatos = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%Y/%m/%d",
        "%d-%m-%Y",
        "%Y%m%d"
    ]
    
    for formato in formatos:
        try:
            return pd.to_datetime(str(valor), format=formato).strftime("%Y-%m-%d")
        except:
            continue
    
    # Último intento — pandas infiere el formato
    try:
        return pd.to_datetime(str(valor), infer_datetime_format=True).strftime("%Y-%m-%d")
    except:
        return None


def detectar_columnas_fecha(df):
    """
    Detecta qué columnas contienen fechas basándose en el nombre
    y en el contenido de la columna.
    """
    palabras_fecha = ["fecha", "date", "time", "dia", "mes", "año", "created", "updated"]
    columnas_fecha = []
    
    for columna in df.columns:
        if any(palabra in columna.lower() for palabra in palabras_fecha):
            columnas_fecha.append(columna)
    
    return columnas_fecha

def limpiar_tabla(engine, tabla):
    """
    Lee una tabla, la limpia y devuelve un DataFrame limpio.
    """
    print(f"\nLimpiando tabla: {tabla}")
    
    # LEER TABLA
    df = pd.read_sql(f"SELECT * FROM {tabla}", engine)
    print(f"   Filas originales: {len(df)}")
    print(f"   Columnas originales: {len(df.columns)}")
    
    # ELIMINAR COLUMNAS BASURA
    columnas_basura = [col for col in df.columns if es_columna_basura(df, col)]
    if columnas_basura:
        print(f"   Columnas eliminadas: {columnas_basura}")
    df = df.drop(columns=columnas_basura)
    
    # NORMALIZAR FECHAS
    columnas_fecha = detectar_columnas_fecha(df)
    for columna in columnas_fecha:
        df[columna] = df[columna].apply(normalizar_fecha)
    if columnas_fecha:
        print(f"   Fechas normalizadas: {columnas_fecha}")
    
    # ELIMINAR FILAS DUPLICADAS
    duplicados = df.duplicated().sum()
    df = df.drop_duplicates()
    if duplicados:
        print(f"   Duplicados eliminados: {duplicados}")
    
    # ELIMINAR FILAS SIN ID
    if "id" in df.columns:
        df = df.dropna(subset=["id"])
    
    print(f"   Filas finales: {len(df)}")
    print(f"   Columnas finales: {len(df.columns)}")
    
    return df
def guardar_tabla_clean(engine, df, tabla):
    """
    Guarda el DataFrame limpio como tabla _clean en MySQL.
    """
    tabla_clean = f"{tabla}_clean"
    
    try:
        df.to_sql(
            name=tabla_clean,
            con=engine,
            if_exists="replace",
            index=False
        )
        print(f"Tabla {tabla_clean} creada correctamente")
    except Exception as e:
        print(f"Error guardando {tabla_clean}: {e}")

def main():
    print("Iniciando limpieza de base de datos...")
    
    engine = conectar()
    
    # OBTENER TODAS LAS TABLAS
    with engine.connect() as conn:
        tablas = pd.read_sql("SHOW TABLES", conn)
        tablas = tablas.iloc[:, 0].tolist()
        tablas = [t for t in tablas if not t.endswith("_clean")]
    
    print(f"Tablas encontradas: {tablas}")
    
    # LIMPIAR Y GUARDAR CADA TABLA
    for tabla in tablas:
        df_limpio = limpiar_tabla(engine, tabla)
        guardar_tabla_clean(engine, df_limpio, tabla)
    
    # GENERAR SCHEMA
    from generar_schema import generar_schema
    generar_schema(engine)
    
    print("\nLimpieza completada")
    print("schema.py actualizado automáticamente")

if __name__ == "__main__":
    main()
