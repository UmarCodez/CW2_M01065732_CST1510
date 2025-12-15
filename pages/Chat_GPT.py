import streamlit as st
from groq import Groq
from groq import BadRequestError

client = Groq(api_key="Groq_API_KEY")

st.title("Chat with GPT")

@st.cache_data(ttl=300)
def list_models():
    ms = client.models.list()
    names = [m.id for m in ms.data]
    chat_like = [n for n in names if any(k in n.lower() for k in ["llama", "mixtral", "gemma", "qwen", "gpt", "k2"])]
    return chat_like or names

models = list_models()
if not models:
    st.error("No models available on Groq right now.")
    st.stop()

model = st.selectbox("Model", models)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("Enter your message:")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        completion = client.chat.completions.create(
            model=model,
            messages=st.session_state.messages,
        )
        reply = completion.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)
    except BadRequestError as e:
        st.error(f"Model error: {e}")