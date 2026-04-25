import pandas as pd
import plotly.express as px


palabras_fecha = ["fecha", "mes", "año", "dia", "semana", "trimestre", "periodo"]

def detectar_grafico(df):
    tiene_fecha = False
    tiene_texto = False
    tiene_numerico = False
    for col in df.columns:
        if df[col].dtype == 'datetime64' or any(palabra in col.lower() for palabra in palabras_fecha):
            tiene_fecha = True
        elif df[col].dtype == 'int64' or df[col].dtype == 'float64':
            tiene_numerico = True
        elif df[col].dtype == 'object':
            tiene_texto = True
    if tiene_fecha:
        return "linea"
    elif tiene_texto and tiene_numerico and len(df) <= 6:
     return "pastel"
    elif tiene_texto and tiene_numerico:
        return "barras"
    else: 
        return "barras"
    

def generar_grafico(df, tipo):
    if tipo == "barras":
        fig = px.bar(df, x=df.columns[0], y=df.columns[1], text_auto=True)
    elif tipo == "linea":
        orden_meses = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
        col_x = df.columns[0]
        if any(mes in df[col_x].values for mes in orden_meses):
            df[col_x] = pd.Categorical(df[col_x], categories=orden_meses, ordered=True)
            df = df.sort_values(col_x)
        fig = px.line(df, x=df.columns[0], y=df.columns[1], markers=True)
    elif tipo == "pastel":
        fig = px.pie(df, names=df.columns[0], values=df.columns[1], hole=0.4)
    return fig