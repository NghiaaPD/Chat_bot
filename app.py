from dotenv import load_dotenv
import streamlit as st
import os

from functions.gemini import gemini

load_dotenv()

st.set_page_config(
    page_title="Chat app",
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

st.sidebar.markdown("## Select :green[**Models**]")

models = st.sidebar.selectbox(
    "**Choose your Models:**",
    ("Gemini", "Llama3", "Phi-2")
)

st.title("🤖 Chat app")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response_text = ""
    response_generator = gemini(prompt, os.getenv('GEMINI_API_KEY'))

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        try:
            if response_generator is None:
                response_text = "An error occurred: gemini function returned None"
                response_placeholder.markdown(response_text)
            else:
                # print("Generator created successfully")
                for word in response_generator:
                    response_text += word
                    response_placeholder.markdown(response_text)
        except Exception as e:
            print(f"Exception in Streamlit app: {str(e)}")
            response_text = f"An error occurred: {str(e)}"
            response_placeholder.markdown(response_text)

    st.session_state.messages.append({"role": "assistant", "content": response_text})
