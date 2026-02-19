import streamlit as st
from datetime import datetime

# 1. Consultamos la hora actual
hora_actual = datetime.now().hour

# 2. Lógica de decisión (Esto es lo que hace un programador)
if 6 <= hora_actual < 12:
    saludo = "¡Buenos días! ☀️"
    fondo = "¡Qué temprano! ¿Ya desayunaste? ☕"
elif 12 <= hora_actual < 19:
    saludo = "¡Buenas tardes! 🌤️"
    fondo = "Espero que tu tarde vaya excelente. 😎"
else:
    saludo = "¡Buenas noches! 🌙"
    fondo = "Ya es hora de descansar un poco. 🛌"

# 3. Mostramos el resultado en la Web
st.title(f"{saludo} Hannya")
st.write(fondo)

# Agregamos un contador de clics (Memoria del sistema)
if 'contador' not in st.session_state:
    st.session_state.counter = 0

if st.button("Pícale aquí para subir tu nivel de programadora"):
    st.session_state.counter += 1
    st.balloons()

st.metric(label="Nivel de experiencia", value=f"{st.session_state.counter} XP")
st.divider() # Pone una línea divisoria
st.subheader("💰 Calculadora de Propinas Pro")

cuenta = st.number_input("¿Cuánto fue de la cuenta?", value=100)
porcentaje = st.slider("¿Qué porcentaje quieres dejar?", 0, 30, 10)

# Aquí está la matemática:
propina = cuenta * (porcentaje / 100)
total = cuenta + propina

st.write(f"Debes dejar **${propina}** de propina.")
st.success(f"El total a pagar es: **${total}**")
st.divider()
st.subheader("🎯 Mis Metas de Programadora")

mis_metas = ["Aprender Python", "Hacer mi propia Web", "Crear un juego", "Trabajar en Google"]

for meta in mis_metas:
    st.checkbox(meta) # Esto crea una lista con cuadritos para marcar
st.divider()
st.subheader("❤️ Mis metas de Programadora")

mis_metas = ["Aprender Python", "Hacer mi propia Web", "Crear un juego", "Trabajar en Google"]

for meta in mis_metas:
    st.checkbox(meta, key=f"check_{meta}") # Esto crea una lista con cuadritos para marcar
st.divider()
st.subheader("🚀 Panel de Control")

# Creamos 3 columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.info("Estado: Activo ✅")

with col2:
    if st.button("Activar Modo Fiesta"):
        st.snow()
        st.toast('¡Fiesta activada!', icon='🎉')

with col3:
    st.warning("Nivel: Aprendiz ⭐")

st.divider()
st.subheader("🎧 Tu DJ Personal de IA")

# 1. Creamos la base de datos de canciones (esto es un Diccionario)
biblioteca = {
    "Feliz ☀️": ["https://open.spotify.com/track/60SdxuYpZpYvYf9P9S0pbu", "Happy - Pharrell"],
    "Triste 🌧️": ["https://open.spotify.com/track/1Z1lsTbsS479m9vCAsDaeY", "Someone Like You - Adele"],
    "Productiva/Estudiando 💻": ["https://open.spotify.com/track/5uCax9HTlsidG46vMv3vdf", "Lofi Hip Hop - Chill Beats"],
    "Modo Fiesta 🔥": ["https://www.youtube.com/watch?v=7zp1TbLFPp8", "Danza Kuduro - Don Omar"]

# 2. Le preguntamos al usuario cómo se siente
estado = st.selectbox("¿Cómo va tu mood hoy?", list(biblioteca.keys()))

# 3. La lógica mágica
if st.button("Recomiéndame una rola"):
    cancion_info = biblioteca[estado]
    st.success(f"Te recomiendo escuchar: **{cancion_info[1]}**")
    st.video(cancion_info[0]) # Esto intentará mostrar el reproductor 