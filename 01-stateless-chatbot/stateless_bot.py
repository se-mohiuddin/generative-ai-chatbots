"""
Stateless Console Chatbot
-------------------------
A simple CLI chatbot built using LangChain and Groq LLM.

In this architecture, each turn is independent (stateless): the model receives
only the system prompt and the latest user prompt, with no memory of prior turns.
"""

import os
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

# 1. Load environment variables from .env
load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    print("Error: GROQ_API_KEY is not set. Please configure it in your .env file.")
    sys.exit(1)

# 2. Instantiate the Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",  # Groq high-speed model
    temperature=0.7,             # Controls randomness (0.0 = deterministic, 1.0 = creative)
)

# 3. Define AI persona via SystemMessage
system_message = SystemMessage(
    content=(
        "Return responses like an old man, that has lived long enough to see "
        "the world, creating business from zero and will guide you on making wealth. "
        "Keep your answers concise, not too long or short."
    )
)

print("\n========================================================")
print("  Stateless Groq Chatbot: Wealth Advisor Persona")
print("  (Type 'exit' or 'quit' to end the session)")
print("========================================================\n")

# 4. Interactive chat loop
while True:
    try:
        user_input = input("You: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        break

    if not user_input:
        continue

    if user_input.lower() in ("exit", "quit"):
        print("Old Man: Thanks for visiting! You can always come back for more advice. Goodbye!")
        break

    # 5. Build turn message list (stateless: no prior conversation history)
    messages = [
        system_message,
        HumanMessage(content=user_input),
    ]

    # 6. Invoke model and display response
    try:
        response = llm.invoke(messages)
        print(f"Old Man: {response.content}\n")
    except Exception as e:
        print(f"Error invoking Groq LLM: {e}\n")
