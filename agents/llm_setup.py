import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.chat_models import ChatOllama

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
        # Fallback to local Ollama if no API key is provided
        # Ensure ollama is running locally with `ollama run llama3`
        print("Warning: No GROQ_API_KEY found. Falling back to local Ollama (llama3).")
        return ChatOllama(model="llama3", temperature=0)
