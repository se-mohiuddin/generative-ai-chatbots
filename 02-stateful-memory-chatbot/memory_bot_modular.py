"""
Stateful In-Memory Chatbot (Modular / Refactored)
------------------------------------------------
A refactored CLI chatbot where conversation management is encapsulated into
a reusable function `get_ai_response()`.

This separation of concerns isolates the conversation engine from the I/O interface,
making it easily testable and directly reusable in web frameworks (such as Streamlit).
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

# 1. Load environment variables
load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    print("Error: GROQ_API_KEY is not set. Please configure it in your .env file.")
    sys.exit(1)

# 2. Instantiate Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
)

# 3. Define AI persona
SYSTEM_MESSAGE = SystemMessage(
    content="Return responses like an old man, that has lived long enough to see "
            "the world, creating business from zero and will guide you on making wealth. "
            "Keep your answers concise, not too long or short."
)


def get_ai_response(user_input: str, conversation_history: list) -> str:
    """
    Generate an AI response using the user's message and ongoing conversation history.

    Args:
        user_input (str): The current message typed by the user.
        conversation_history (list): List of HumanMessage and AIMessage objects.

    Returns:
        str: Text content of the AI's response.
    """
    # Wrap and record user message
    user_message = HumanMessage(content=user_input)
    conversation_history.append(user_message)

    # Combine system prompt with full conversation history
    messages = [
        SYSTEM_MESSAGE,
        *conversation_history,
    ]

    # Invoke the model
    ai_msg = llm.invoke(messages)

    # Record AI message in history
    conversation_history.append(
        AIMessage(content=ai_msg.content)
    )

    return ai_msg.content


def main():
    """Main CLI interaction loop."""
    conversation_history: list = []

    print("\n========================================================")
    print("  Stateful Chatbot with In-Memory History (Modular)")
    print("  Persona: Snoop Dogg (Chill & Slang)")
    print("  (Type 'exit' or 'quit' to quit)")
    print("========================================================\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("AI: Peace out! Catch you on the flip side.")
            break

        try:
            response = get_ai_response(user_input, conversation_history)
            print(f"AI: {response}\n")
        except Exception as e:
            print(f"Error invoking Groq LLM: {e}\n")


if __name__ == "__main__":
    main()
