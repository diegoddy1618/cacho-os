import streamlit as st
import google.generativeai as genai

# Configuración visual: Aquí le ponemos el nombre a la pestaña
st.set_page_config(page_title="cacho.os", page_icon="💀", layout="centered")

# Título en la pantalla
st.title("cacho.os")
st.caption("Sistema Operativo Personal - v1.0")

# Conexión segura con la IA
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("Falta la API Key. Configúrala en los 'Secrets' de Streamlit.")
    st.stop()

# Memoria del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Casilla para escribir
if prompt := st.chat_input("Ingresa comando o consulta..."):
    # Guardar lo que escribiste
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # La IA piensa
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        message_placeholder.markdown(response.text)
    
    # Guardar respuesta
    st.session_state.messages.append({"role": "assistant", "content": response.text})
