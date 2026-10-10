# 01 - Stateless Console Chatbot

A command-line chatbot built with **LangChain** and **Groq Cloud API** demonstrating the fundamentals of LLM prompt structuring and stateless conversational loops.

---

## 📌 Architectural Concept: Statelessness

In a **stateless** chatbot, every interaction is isolated:
- The language model does **not** remember previous turns.
- For each user input, the application constructs a fresh payload containing only:
  1. A **`SystemMessage`**: primes the persona and instructions ("Wealth Advisor").
  2. A **`HumanMessage`**: the latest user input.
- Past questions and responses are discarded after each turn.

```
+------------+       User Message
|    User    | ------------------------+
+------------+                         |
                                       v
                             +-------------------+
                             |  Message Payload  |
                             | - SystemMessage   |
                             | - HumanMessage    |
                             +-------------------+
                                       |
                                       v
+------------+       LLM Response    +-------------------+
|  Console   | <-------------------- |     Groq LLM      |
+------------+                       +-------------------+
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.10+ installed and a Groq API key from [GroqCloud Console](https://console.groq.com/keys).

### 2. Configure Environment Variables
Copy `.env.example` to `.env` and set your Groq API key:

```bash
# On Windows PowerShell
Copy-Item .env.example .env

# On Linux / macOS
cp .env.example .env
```

Open `.env` and paste your key:
```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Chatbot
```bash
python stateless_bot.py
```

---

## 💬 Example Interaction

```text
========================================================
  Stateless Groq Chatbot: Wealth Advisor Persona
  (Type 'exit' or 'quit' to end the session)
========================================================

You: Hi, my name is Alex.
Old Man: Welcome, Alex. Time is the greatest asset you'll ever manage—what financial venture are we building today?

You: What is my name?
Old Man: I don't know your name, but names matter less than your credit and compounding returns. What's on your mind?
```

Notice how the bot does not retain the name "Alex" in the second turn—highlighting the defining characteristic of a stateless system.
