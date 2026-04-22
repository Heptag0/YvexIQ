import streamlit as st
from main import consultar

st.title("Consulta de Ventas")
pregunta =st.text_input("Ingrese su pregunta sobre tus ventas")
if st.button("Consultar"):
    respuesta = consultar(pregunta)
    if isinstance(respuesta, str):
     st.write(respuesta)
    else:
     st.dataframe(respuesta)
else:
    st.write("Ingrese una pregunta y presione el boton para obtener una respuesta")

