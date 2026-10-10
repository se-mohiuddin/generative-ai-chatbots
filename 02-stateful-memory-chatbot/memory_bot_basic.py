"""
Stateful In-Memory Chatbot (Procedural)
--------------------------------------
A CLI chatbot built with LangChain and Groq LLM featuring conversation memory.

Unlike a stateless bot, this script retains conversation history across turns
by storing HumanMessage and AIMessage objects in an in-memory list and passing
them with each subsequent LLM call.
"""

import os
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

# 1. Load environment variables from .env
load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    print("Error: GROQ_API_KEY is not set. Please configure it in your .env file.")
    sys.exit(1)

# 2. Instantiate Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
)

# 3. Define AI persona via SystemMessage
system_message = SystemMessage(
    content="Return responses like an old man, that has lived long enough to see "
            "the world, creating business from zero and will guide you on making wealth. "
            "Keep your answers concise, not too long or short."
)

# 4. Initialize in-memory conversation history list
conversation_history: list = []

print("\n========================================================")
print("  Stateful Chatbot with In-Memory History (Basic)")
print("  Persona: Snoop Dogg (Chill & Slang)")
print("  (Type 'exit' or 'quit' to quit)")
print("========================================================\n")

# 5. Interactive loop
while True:
    try:
        user_input = input("You: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nSee ya later!")
        break

    if not user_input:
        continue

    if user_input.lower() in ("exit", "quit"):
        print("AI: See ya later, stay smooth!")
        break

    # Wrap input as HumanMessage and store in history
    user_message = HumanMessage(content=user_input)
    conversation_history.append(user_message)

    # Construct complete payload: SystemMessage + all past conversation turns
    messages = [
        system_message,
        *conversation_history,
    ]

    try:
        ai_msg = llm.invoke(messages)
        print(f"AI: {ai_msg.content}\n")

        # Store AI response in history to retain multi-turn context
        conversation_history.append(
            AIMessage(content=ai_msg.content)
        )
    except Exception as e:
        print(f"Error invoking Groq LLM: {e}\n")
