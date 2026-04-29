import streamlit as st
from main import consultar
from graficos import detectar_grafico, generar_grafico
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# MEMORIA DE SESIÓN 
# Inicializar variables que necesitan mantenerse en recargas
if "pregunta" not in st.session_state:
    st.session_state.pregunta = ""
if "ejecutar" not in st.session_state:
    st.session_state.ejecutar = False
if "lista_sugerencias" not in st.session_state:
    st.session_state.lista_sugerencias = None

# MEMORIA DE SESIÓN 
# Inicializar variables que necesitan mantenerse en recargas
if "pregunta" not in st.session_state:
    st.session_state.pregunta = ""
if "ejecutar" not in st.session_state:
    st.session_state.ejecutar = False
if "lista_sugerencias" not in st.session_state:
    st.session_state.lista_sugerencias = None

# INTERFAZ
st.markdown("""
    <div class="brand-header">
        <h1>Yvex<span>IQ</span></h1>
        <p>Pregunta. Analiza. Decide.</p>
    </div>
""", unsafe_allow_html=True)
pregunta = st.text_input("Ingrese su pregunta sobre tus ventas", 
                          value=st.session_state.pregunta)

# EJECUCIÓN AUTOMÁTICA (click en una sugerencia)
if st.session_state.ejecutar:
    st.session_state.ejecutar = False  # resetear para no ejecutar en bucle
    pregunta = st.session_state.pregunta
    with st.spinner("Analizando tu consulta..."):
        try:
            respuesta_texto, resultado, lista_sugerencias = consultar(pregunta, modo="rapido")
            st.session_state.lista_sugerencias = lista_sugerencias
            if respuesta_texto is not None:
                st.write(respuesta_texto)
            if resultado is not None:
                st.dataframe(resultado.reset_index(drop=True), hide_index=True)
                if resultado.shape[0] > 0 and resultado.shape[1] >= 2:
                    tipo_grafico = detectar_grafico(resultado)
                    grafico = generar_grafico(resultado, tipo_grafico)
                    st.plotly_chart(grafico)
        except Exception as e:
            st.write(f"No se ha podido realizar la consulta, error: {e}")

# BOTONES PRINCIPALES
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown('<div class="boton-rapida">', unsafe_allow_html=True)
    rapida = st.button("⚡ Rápida")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="boton-profunda">', unsafe_allow_html=True)
    profunda = st.button("🔍 Profunda")
    st.markdown('</div>', unsafe_allow_html=True)

# BLOQUE RESPUESTA PROFUNDA
if profunda:
    st.session_state.lista_sugerencias = None  # limpiar sugerencias anteriores
    with st.spinner("Analizando tu consulta..."):
        try:
            respuesta_natural, resultado, lista_sugerencias = consultar(pregunta, modo="profundo")
            st.session_state.lista_sugerencias = lista_sugerencias
            if respuesta_natural is not None:
                st.write(respuesta_natural)
            if resultado is not None:
                st.dataframe(resultado.reset_index(drop=True), hide_index=True)
                if resultado.shape[0] > 0 and resultado.shape[1] >= 2:
                    tipo_grafico = detectar_grafico(resultado)
                    grafico = generar_grafico(resultado, tipo_grafico)
                    st.plotly_chart(grafico)
        except Exception as e:
            st.write(f"No se ha podido realizar la consulta, error: {e}")

# BLOQUE RESPUESTA RÁPIDA 
if rapida:
    st.session_state.lista_sugerencias = None  # limpiar sugerencias anteriores
    with st.spinner("Analizando tu consulta..."):
        try:
            respuesta_texto, resultado, lista_sugerencias = consultar(pregunta, modo="rapido")
            st.session_state.lista_sugerencias = lista_sugerencias
            if respuesta_texto is not None:
                st.write(respuesta_texto)
            if resultado is not None:
                st.dataframe(resultado.reset_index(drop=True), hide_index=True)
                if resultado.shape[0] > 0 and resultado.shape[1] >= 2:
                    tipo_grafico = detectar_grafico(resultado)
                    grafico = generar_grafico(resultado, tipo_grafico)
                    st.plotly_chart(grafico)
        except Exception as e:
            st.write(f"No se ha podido realizar la consulta, error: {e}")

# BOTONES DE SUGERENCIAS 
# Siempre visibles si hay sugerencias guardadas en la sesion
if st.session_state.lista_sugerencias:
    st.write("Preguntas recomendadas:")
    for i, sug in enumerate(st.session_state.lista_sugerencias):
        if st.button(sug, key=f"sug_{i}"):
            st.session_state.pregunta = sug
            st.session_state.ejecutar = True
            st.rerun()

# MENSAJE INICIAL 
if not rapida and not profunda and not st.session_state.ejecutar:
    st.write("Ingrese una pregunta y presione el botón para obtener una respuesta")