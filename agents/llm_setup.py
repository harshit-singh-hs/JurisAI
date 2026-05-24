import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    
    if api_key:
        return ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=api_key
        )
    else:
        raise ValueError("GROQ_API_KEY is not set. Cannot initialize LLM.")
