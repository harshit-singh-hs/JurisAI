import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "chroma_db")

def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def get_vectorstore():
    return Chroma(
        collection_name="legal_documents",
        embedding_function=get_embedding_model(),
        persist_directory=DB_DIR
    )

def get_retriever():
    vectorstore = get_vectorstore()
    return vectorstore.as_retriever(search_kwargs={"k": 3})
