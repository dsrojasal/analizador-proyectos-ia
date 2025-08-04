import streamlit as st
from explorer import analizar_proyecto
from assistant import responder_pregunta_stream
import os
from dotenv import load_dotenv

# Cargar .env
load_dotenv()

st.set_page_config(page_title="Analizador de Proyectos", layout="wide")
st.title("🧠 Analizador de Proyectos")

# Ruta del proyecto
ruta_proyecto = st.text_input("📁 Ruta del proyecto:", value=os.getcwd())

# Botón para analizar
if st.button("🔍 Analizar proyecto"):
    with st.spinner("Analizando proyecto..."):
        resumen, arbol = analizar_proyecto(ruta_proyecto)
        st.session_state["resumen_proyecto"] = resumen
        st.session_state["arbol_proyecto"] = arbol
        st.success("✅ Análisis completado")

# Mostrar resultados
if "resumen_proyecto" in st.session_state:
    st.subheader("📄 Archivos clave del proyecto")
    st.code(st.session_state["arbol_proyecto"], language="text")

    st.subheader("📝 Resumen del proyecto")
    st.write(st.session_state["resumen_proyecto"])

st.divider()

# Pregunta a la IA
st.subheader("🤖 Pregúntale a la IA sobre el proyecto")
pregunta = st.text_input("Escribe tu pregunta...")

if st.button("💬 Consultar IA"):
    if "resumen_proyecto" not in st.session_state:
        st.warning("⚠️ Primero debes analizar el proyecto para generar un resumen.")
    elif not pregunta.strip():
        st.warning("⚠️ Escribe una pregunta para consultar a la IA.")
    else:
        with st.spinner("Consultando a la IA..."):
            contexto = st.session_state["resumen_proyecto"]
            respuesta_completa = ""
            for chunk in responder_pregunta_stream(pregunta, contexto):
                respuesta_completa += chunk
            st.markdown(respuesta_completa)

            # Créditos del autor (plegable)
with st.expander("👤 Créditos del autor"):
    st.markdown("""
    **Daniel Rojas**  
    Estudiante de Ingeniería de Sistemas  
    [🔗 Mi LinkedIn](https://www.linkedin.com/in/danielrojas123/)  
    Proyecto creado con Python, Streamlit y APIs de IA.  
    Agosto 2025
    """)

    st.caption("🛠️ Proyecto creado por Daniel Rojas — Código abierto bajo licencia MIT")

