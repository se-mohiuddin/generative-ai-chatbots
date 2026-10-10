"""
Chatbot Backend Logic
----------------------
Handles model configuration, prompt structuring, and conversation
state using LangChain and Groq Cloud.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

# 1. Load environment variables from .env
load_dotenv()


def get_llm():
    """
    Instantiate and return the Groq Chat model.
    Raises ValueError if GROQ_API_KEY is not configured.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Please set it in your .env file or environment.")

    return ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.7,
        groq_api_key=api_key,
    )


# System instruction defining personality
SYSTEM_MESSAGE = SystemMessage(
    content="Return responses like an old man, that has lived long enough to see "
            "the world, creating business from zero and will guide you on making wealth. "
            "Keep your answers concise, not too long or short."
)


def get_ai_response(user_input: str, conversation_history: list) -> str:
    """
    Generate an AI response using the user's message and the existing conversation history.

    Args:
        user_input (str): The new prompt typed by the user.
        conversation_history (list): Streamlit session state message list.

    Returns:
        str: Clean text content of the assistant response.
    """
    llm = get_llm()

    # Wrap incoming user text into a LangChain HumanMessage
    user_message = HumanMessage(content=user_input)
    conversation_history.append(user_message)

    # Build the complete message sequence for the LLM
    messages = [
        SYSTEM_MESSAGE,
        *conversation_history,
    ]

    # Invoke Groq LLM
    ai_msg = llm.invoke(messages)

    # Append AI response to persist history across turns
    conversation_history.append(
        AIMessage(content=ai_msg.content)
    )

    return str(ai_msg.content)
