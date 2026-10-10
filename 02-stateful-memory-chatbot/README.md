# 02 - Stateful In-Memory Chatbot

A multi-turn conversational chatbot built with **LangChain** and **Groq Cloud API** demonstrating how to maintain conversational state and context across multiple turns.

---

## 📌 Architectural Concept: Stateful In-Memory Context

Unlike a stateless system, a **stateful** chatbot remembers previous messages within an active session:
- Every user input is converted into a `HumanMessage` and appended to an in-memory `conversation_history` list.
- The model's response is converted into an `AIMessage` and appended to the same list.
- On each subsequent turn, the entire history is unpacked into the prompt payload alongside the `SystemMessage`.

```
                  +----------------------------------------------+
                  |             conversation_history             |
                  | [HumanMessage(1), AIMessage(1), ...]        |
                  +----------------------------------------------+
                                         |
                                         v
User Message ---> [ SystemMessage + Unpacked History + New Message ] ---> Groq LLM
                                                                              |
                                         +------------------------------------+
                                         v
                       Appends new AIMessage to history
```

---

## 📂 Included Implementations

1. **`memory_bot_basic.py`**:
   - Monolithic procedural script.
   - Ideal for understanding the raw mechanics of appending messages and list unpacking.
2. **`memory_bot_modular.py`**:
   - Refactored with clean separation of concerns.
   - Encapsulates logic into `get_ai_response(user_input, conversation_history)`.
   - Directly bridges into web frameworks (such as Streamlit or FastAPI).

---

## 🚀 Getting Started

### 1. Configure Environment Variables
Copy `.env.example` to `.env` and insert your Groq API key:

```bash
# On Windows PowerShell
Copy-Item .env.example .env

# On Linux / macOS
cp .env.example .env
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Either Script

Run the basic procedural version:
```bash
python memory_bot_basic.py
```

Or run the refactored modular version:
```bash
python memory_bot_modular.py
```

---

## 💬 Multi-Turn Conversation Demonstration

```text
========================================================
  Stateful Chatbot with In-Memory History (Modular)
  Persona: Snoop Dogg (Chill & Slang)
========================================================

You: Yo! My favorite food is homemade tacos.
AI: Fo shizzle! Tacos are legendary, nephew. Season that beef right and keep that salsa poppin'!

You: What did I just say my favorite food was?
AI: You already know, homie—you said homemade tacos! Can't go wrong with that flavor.
```

Notice how the bot retains conversational memory and answers the follow-up question accurately.
