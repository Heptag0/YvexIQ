import streamlit as st
from main import consultar
from graficos import detectar_grafico, generar_grafico

st.title("Consulta de Ventas")
pregunta =st.text_input("Ingrese su pregunta sobre tus ventas")
if st.button("Consultar"):
    with st.spinner("Analizando tu consulta..."):
        try:
            respuesta_natural, resultado = consultar(pregunta)
            st.write(respuesta_natural)
            if resultado is not None:
                st.dataframe(resultado.reset_index(drop=True), hide_index=True)
                tipo_grafico = detectar_grafico(resultado)
                grafico = generar_grafico(resultado, tipo_grafico)
                st.plotly_chart(grafico)
        except Exception as e:
            st.write(f"No se ha podido realizar la consulta, error: {e}")
else:
    st.write("Ingrese una pregunta y presione el boton para obtener una respuesta")


