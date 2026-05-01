import pandas as pd
from db_connector import conectar

# PALABRAS CLAVE PARA COMENTARIOS AUTOMÁTICOS
COMENTARIOS = {
    # Fechas específicas
    "fecha_registro": "fecha en que se registró el cliente",
    "fecha_ultima_compra": "fecha de la última compra del cliente",
    "fecha_creado": "fecha de creación del producto",
    "fecha_movimiento": "fecha del movimiento de inventario",
    # Fechas genéricas
    "fecha": "fecha del registro",
    "date": "fecha del registro",
    "created": "fecha de creación",
    "updated": "fecha de última actualización",
    # Identificadores
    "nombre": "nombre del registro",
    "descripcion": "nombre o descripción del registro",
    "titulo": "título del registro",
    # Monetarias
    "total": "valor monetario total",
    "precio_costo": "precio de compra al proveedor",
    "precio_venta": "precio de venta al cliente",
    "precio": "precio del producto",
    "ganancia": "beneficio económico",
    "importe": "valor monetario",
    "descuento": "porcentaje de descuento aplicado",
    "costo": "costo del producto",
    # Cantidades
    "stock_actual": "unidades disponibles actualmente en inventario",
    "cantidad_movimiento": "unidades añadidas o retiradas del inventario",
    "cantidad_anterior": "unidades en inventario antes del movimiento",
    "cantidad": "cantidad de unidades",
    # Contacto
    "email": "correo electrónico",
    "telefono": "número de teléfono",
    "ciudad": "ciudad del registro",
    "pais": "país del registro",
    # Otros
    "motivo": "razón o motivo del registro",
    "canal": "canal de venta — tienda física, online o teléfono",
    "metodo_pago": "método de pago usado — efectivo, tarjeta o transferencia",
    "temporada": "temporada de la colección del producto",
    "talla": "talla del producto",
    "color": "color del producto",
    "activo": "indica si el registro está activo",
    "operador": "código del operador que realizó la venta"
}

def obtener_comentario(columna):
    """
    Devuelve un comentario automático basándose en el nombre de la columna.
    """
    for palabra, comentario in COMENTARIOS.items():
        if columna in COMENTARIOS:
            return f" -- {COMENTARIOS[columna]}"
        if palabra in columna.lower():
            return f" -- {comentario}"
    return ""

def obtener_tipo_dato(dtype, columna):
    """
    Convierte el tipo de dato de pandas a un tipo legible.
    """
    monetarias = ["total", "precio", "ganancia", "importe", "descuento", "costo"]
    fechas = ["fecha", "date", "created", "updated"]
    if "int" in str(dtype):
        return "int"
    elif "float" in str(dtype):
        if columna.endswith("_id") or columna == "id":
            return "int"
        return "decimal"
    elif "datetime" in str(dtype):
        return "date"
    elif "object" in str(dtype):
        if any(palabra in columna.lower() for palabra in monetarias):
            return "decimal"
        if any(palabra in columna.lower() for palabra in fechas):
            return "date"
        return "varchar"
    elif "str" in str(dtype):
        if any(palabra in columna.lower() for palabra in fechas):
            return "date"
        return "varchar"
    else:
        return str(dtype)

def detectar_relaciones(tablas, engine):
    """
    Detecta relaciones entre tablas buscando columnas que terminan en _id
    y verificando si existe una tabla correspondiente.
    """
    relaciones = []
    nombres_tablas = [t.replace("_clean", "") for t in tablas]
    
    for tabla in tablas:
        df = pd.read_sql(f"SELECT * FROM {tabla} LIMIT 1", engine)
        for columna in df.columns:
            if columna.endswith("_id") and columna != "id":
                tabla_referenciada = columna.replace("_id", "")
                if tabla_referenciada in nombres_tablas:
                    relaciones.append(
                        f"- {tabla}.{columna} = {tabla_referenciada}_clean.id"
                    )
    return relaciones

def generar_schema(engine):
    """
    Lee todas las tablas _clean y genera schema.py automáticamente.
    """
    print("\nGenerando schema.py...")
    
    # OBTENER TABLAS CLEAN
    with engine.connect() as conn:
        tablas = pd.read_sql("SHOW TABLES", conn)
        tablas = tablas.iloc[:, 0].tolist()
        tablas = [t for t in tablas if t.endswith("_clean")]
    
    schema_texto = 'def obtener_schema():\n    return """\n'
    
    # GENERAR DESCRIPCIÓN DE CADA TABLA
    for tabla in tablas:
        df = pd.read_sql(f"SELECT * FROM {tabla} LIMIT 5", engine)
        
        schema_texto += f"Tabla: {tabla}\n"
        schema_texto += "Columnas: "
        
        columnas = []
        for columna in df.columns:
            tipo = obtener_tipo_dato(df[columna].dtype, columna)
            comentario = obtener_comentario(columna)
            columnas.append(f"{columna} ({tipo}){comentario}")
        
        schema_texto += ", ".join(columnas)
        schema_texto += "\n\n"
    
    # GENERAR RELACIONES
    relaciones = detectar_relaciones(tablas, engine)
    if relaciones:
        schema_texto += "Relaciones:\n"
        schema_texto += "\n".join(relaciones)
        schema_texto += "\n"
    
    schema_texto += '"""\n'
    
    # GUARDAR schema.py
    with open("schema.py", "w", encoding="utf-8") as f:
        f.write(schema_texto)
    
    print("schema.py generado correctamente")
engine = conectar()
df = pd.read_sql("SELECT * FROM clientes_clean LIMIT 1", engine)
print(df.dtypes)

if __name__ == "__main__":
    engine = conectar()
    generar_schema(engine)