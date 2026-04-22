import streamlit as st
from main import consultar

st.title("Consulta de Ventas")
pregunta =st.text_input("Ingrese su pregunta sobre tus ventas")
if st.button("Consultar"):
    try:
        respuesta = consultar(pregunta)
        if isinstance(respuesta, str):
            st.write(respuesta)
        else:
            st.dataframe(respuesta)
    except Exception as e:
        st.write(f"No se ha podido realizar la consulta, error: {e}")
else:
    st.write("Ingrese una pregunta y presione el boton para obtener una respuesta")
