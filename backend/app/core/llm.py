from langchain_openai import ChatOpenAI

from app.core.config import settings


def get_llm():
    return ChatOpenAI(
        model="gpt-4.1",
        api_key=settings.OPENAI_API_KEY,
        temperature=0.2,
    )