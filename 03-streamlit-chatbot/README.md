# 03 - Streamlit Web AI Chatbot

An interactive, responsive web-based conversational AI interface built with **Streamlit**, **LangChain**, and **Groq Cloud API**.

---

## 📌 Architectural Concept: Web Session State

In web applications, each user interaction triggers a script rerun. To maintain conversational continuity across reruns:
- Chat history is stored in **`st.session_state.messages`**.
- The backend (`chatbot.py`) appends both user inputs and LLM responses to this session state list.
- Streamlit's native `st.chat_message` renders avatars and formatted markdown messages dynamically.

```
[ User Input (st.chat_input) ]
              |
              v
[ st.session_state.messages ] ---> [ LangChain ChatGroq ] ---> [ Groq LPU API ]
              ^                                                     |
              |------------------ Append AIMessage <----------------+
              |
              v
[ Render Chat UI (st.chat_message) ]
```

---

## ✨ Features

- **Intuitive Web UI**: Modern chat bubbles using Streamlit native components.
- **Persistent Multi-Turn Context**: Maintains full chat history across reruns.
- **Sidebar Diagnostics**: Real-time API key status, model architecture specs, and persona details.
- **One-Click Session Reset**: Clear chat history instantly to start a fresh conversation.
- **Modular Codebase**: Clean separation between presentation (`app.py`) and AI orchestration (`chatbot.py`).

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- A free Groq API key from [GroqCloud Console](https://console.groq.com/keys)

### 2. Configure Environment Variables
Copy `.env.example` to `.env` and set your key:

```bash
# On Windows PowerShell
Copy-Item .env.example .env

# On Linux / macOS
cp .env.example .env
```

Set your API key in `.env`:
```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501`.

---

## 🌐 Deploying to Streamlit Community Cloud

This project is ready for one-click deployment:
1. Push this repository to GitHub.
2. Sign in to [share.streamlit.io](https://share.streamlit.io).
3. Select your repository.
4. Set the **Main file path** to `03-streamlit-chatbot/app.py`.
5. Under **Advanced settings**, add your `GROQ_API_KEY` into the **Secrets** section:
   ```toml
   GROQ_API_KEY = "gsk_..."
   ```
6. Click **Deploy!**
