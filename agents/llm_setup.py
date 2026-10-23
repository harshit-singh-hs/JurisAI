import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# llama-3.3-70b-versatile was retired by Groq; override with GROQ_MODEL if this one is too
DEFAULT_MODEL = "openai/gpt-oss-120b"

# Without an explicit limit Groq caps output at 3072 tokens, and gpt-oss spends part of that on
# hidden reasoning, so long answers (e.g. drafted contracts) were cut off mid-sentence
MAX_OUTPUT_TOKENS = 8192

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if api_key:
        return ChatGroq(
            model=os.getenv("GROQ_MODEL", DEFAULT_MODEL),
            temperature=0.0,
            max_tokens=MAX_OUTPUT_TOKENS,
            # Fail instead of leaving the user's request (and a worker thread) hanging forever
            timeout=120,
            max_retries=2,
            api_key=api_key
        )
    else:
        raise ValueError("GROQ_API_KEY is not set. Cannot initialize LLM.")
