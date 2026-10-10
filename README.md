# 🤖 Generative AI Chatbots: From Stateless CLI to Interactive Web Apps

> A progressive, production-ready portfolio collection of conversational AI systems built with **LangChain**, **Groq Cloud LLMs**, and **Streamlit**—tracking the evolution from foundational stateless command-line prompts to stateful multi-turn memory and interactive web applications, designed for extension into RAG and AI Agents.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-v0.3%2B-1C3C3C.svg?logo=chainlink)](https://www.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-LPU%20Inference-f55036.svg)](https://groq.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-v1.35%2B-FF4B4B.svg?logo=streamlit)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Repository Overview

This repository documents my structured learning journey in building conversational AI systems. Rather than viewing chatbots as opaque scripts, this project demonstrates their inner architecture layer-by-layer:

1. **Stateless Foundations**: Understanding LLM prompt payloads, message roles (`SystemMessage`, `HumanMessage`), and the stateless nature of raw language models.
2. **Stateful In-Memory History**: Structuring conversation memory by tracking message sequences (`AIMessage`) across dynamic multi-turn interactions.
3. **Modular Software Architecture**: Decoupling LLM invocation logic from user interfaces for reusability, testability, and portability.
4. **Interactive Web Interface**: Bringing stateful conversational AI to the browser using Streamlit's reactive session state.
5. **Future Roadmap**: Scaling progressively into Retrieval-Augmented Generation (RAG) and Autonomous Tool-Using Agents.

---

## 📂 Project Architecture & Roadmap

| Module | Status | Architecture | Tech Stack | Highlights |
| :--- | :---: | :--- | :--- | :--- |
| [**`01-stateless-chatbot`**](./01-stateless-chatbot) | ✅ Completed | Stateless CLI Loop | Python, LangChain, Groq | System persona priming, single-turn prompts |
| [**`02-stateful-memory-chatbot`**](./02-stateful-memory-chatbot) | ✅ Completed | In-Memory Stateful Context | Python, LangChain, Groq | Multi-turn history, modular function design |
| [**`03-streamlit-chatbot`**](./03-streamlit-chatbot) | ✅ Completed | Interactive Web UI | Streamlit, LangChain, Groq | Session state persistence, diagnostics, reset controls |
| **`04-rag-document-chatbot`** | 🚧 Planned | Retrieval-Augmented Generation | LangChain, ChromaDB / FAISS | Querying local documents & vector embeddings |
| **`05-agentic-chatbot`** | 🚧 Planned | Tool-Using Autonomous Agent | LangGraph / LangChain Agents | Web search, calculator, custom API execution |

---

## 🛠️ Tech Stack & Key Libraries

- **Language**: Python 3.10+
- **LLM Orchestration**: [LangChain](https://www.langchain.com/) (`langchain-core`, `langchain-groq`)
- **High-Speed Inference**: [Groq Cloud](https://groq.com/) (`openai/gpt-oss-20b`, LPU inference engine)
- **Web Frontend**: [Streamlit](https://streamlit.io/)
- **Configuration & Security**: `python-dotenv` for secure environment variable management

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/se-mohiuddin/generative-ai-chatbots.git
cd generative-ai-chatbots
```

### 2. Set Up a Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Activate on macOS / Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Copy `.env.example` to `.env` and insert your Groq API key:
```bash
# Windows PowerShell
Copy-Item .env.example .env

# macOS / Linux
cp .env.example .env
```
Inside `.env`:
```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

---

## 🏃 Running the Projects

### Stage 1: Stateless Console Chatbot
```bash
python 01-stateless-chatbot/stateless_bot.py
```

### Stage 2: Stateful In-Memory Chatbot
Run the procedural version:
```bash
python 02-stateful-memory-chatbot/memory_bot_basic.py
```
Or run the modular refactored version:
```bash
python 02-stateful-memory-chatbot/memory_bot_modular.py
```

### Stage 3: Interactive Streamlit Web Chatbot
```bash
streamlit run 03-streamlit-chatbot/app.py
```

---

## 🛡️ Security & Clean Code Practices
- **No Secret Leakage**: The repository strictly enforces `.gitignore` rules preventing `.env` files, `.venv` environments, and bytecode caches from ever being committed.
- **Environment Isolation**: Always use `.env.example` as a template for public documentation and never hardcode API keys.

---

## 👤 Author

**Mohiuddin Siddiqui**
- GitHub: [@se-mohiuddin](https://github.com/se-mohiuddin)

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
