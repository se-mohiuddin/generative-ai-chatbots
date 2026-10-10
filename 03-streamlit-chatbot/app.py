"""
Streamlit Web Chatbot Application
---------------------------------
An interactive web user interface built with Streamlit, LangChain, and Groq.
Persists multi-turn conversation memory using Streamlit Session State.
"""

import os
import streamlit as st
from dotenv import load_dotenv
from chatbot import get_ai_response

# 1. Page Configuration
st.set_page_config(
    page_title="Conversational AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 2. Sidebar Configuration & Controls
with st.sidebar:
    st.title("⚙️ Configuration")
    st.markdown("### Architecture")
    st.markdown(
        "- **Framework**: Streamlit\n"
        "- **Orchestration**: LangChain\n"
        "- **Inference**: Groq LPU\n"
        "- **Model**: `openai/gpt-oss-20b`\n"
        "- **Persona**: Snoop Dogg (Chill & Slang)"
    )

    st.markdown("---")

    # API Key status check
    api_key_set = bool(os.getenv("GROQ_API_KEY"))
    if api_key_set:
        st.success("API Key detected in environment", icon="🔑")
    else:
        st.error("GROQ_API_KEY is not set. Please update your .env file.", icon="⚠️")

    st.markdown("---")

    # Clear chat button
    if st.button("🧹 Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("Built by **Mohiuddin Siddiqui**")

# 3. Main Header
st.title("🤖 Conversational AI Chatbot")
st.caption("A responsive multi-turn AI chatbot powered by Streamlit, LangChain, and Groq.")

# 4. Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Render Message History
for message in st.session_state.messages:
    role = "user" if message.type == "human" else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# 6. User Input Handling
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display the user's message immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response from Groq via LangChain
    with st.chat_message("assistant"):
        # with st.spinner("Thinking..."):
            try:
                response = get_ai_response(
                    user_input=user_input,
                    conversation_history=st.session_state.messages,
                )
                st.markdown(response)
            except Exception as error:
                st.error(f"Error generating response: {error}")
