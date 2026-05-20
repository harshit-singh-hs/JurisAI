import os
import pickle
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever
from database.chroma_setup import get_vectorstore

BM25_INDEX_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "bm25_index.pkl")

def get_bm25_retriever():
    if os.path.exists(BM25_INDEX_PATH):
        with open(BM25_INDEX_PATH, "rb") as f:
            return pickle.load(f)
    return None

def get_ensemble_retriever():
    vectorstore = get_vectorstore()
    chroma_retriever = vectorstore.as_retriever(search_kwargs={"k": 6})
    
    bm25_retriever = get_bm25_retriever()
    
    if bm25_retriever:
        bm25_retriever.k = 6
        print("Using Hybrid Search (BM25 + Vector)")
        return EnsembleRetriever(
            retrievers=[bm25_retriever, chroma_retriever],
            weights=[0.5, 0.5]
        )
    else:
        print("Warning: BM25 index not found. Using Vector Search only.")
        return chroma_retriever
