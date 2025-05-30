import streamlit as st
from personas import PERSONAS
from utils import generate_response
from PIL import Image

st.markdown("<h1 style='text-align: center;'>☕ Coffee Chat with AI Guru</h1>", unsafe_allow_html=True)
st.title("🧠 Persona Chat App")

col1, col2 = st.columns(2)

with col1:
    if st.button("🧑‍🏫 Hitesh Choudhary"):
        st.session_state.persona = "Hitesh Choudhary"
    st.image("assets/hitesh.jpeg", width=200)
    st.write("Tech Educator, YouTuber & Mentor at iNeuron.")

with col2:
    if st.button("👨‍💻 Piyush Garg"):
        st.session_state.persona = "Piyush Garg"
    st.image("assets/piyush.jpeg", width=200)
    st.write("GenAI Expert, Mentor, and Engineer.")

if "persona" in st.session_state:
    st.markdown(f"### 💬 Talking to: {st.session_state.persona}")
else:
    st.stop()

# Chat input
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask a question:")

if user_input:
    # Append user message
    st.session_state.chat_history.append(("You", user_input))

    # Generate response
    response = generate_response(st.session_state.persona, user_input)
    st.session_state.chat_history.append((st.session_state.persona, response))

# Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")