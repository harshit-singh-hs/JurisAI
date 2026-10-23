import re
from functools import lru_cache
from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document
try:
    # LangChain >= 1.0 moved EnsembleRetriever into langchain-classic
    from langchain_classic.retrievers import EnsembleRetriever
except ImportError:
    from langchain.retrievers import EnsembleRetriever
from database.chroma_setup import get_vectorstore

# Words that appear in nearly every query/document; left in, "what is the ..." matches everything
STOPWORDS = frozenset("""
a an and are as at be been by can could do does did for from had has have how i if in into is it its
me my of on or our so than that the their them then there these they this those to was we were what
when where which who whom why will with would you your
""".split())

def tokenize(text: str):
    """Lowercased word tokens, so "Article 21." matches "article 21" and "FIR?" matches "FIR"."""
    return [token for token in re.findall(r"\w+", text.lower()) if token not in STOPWORDS]

def get_bm25_retriever(vectorstore):
    # Built from the Chroma collection so the keyword and vector indexes always hold the same chunks
    data = vectorstore.get(include=["documents", "metadatas"])
    if not data["documents"]:
        return None
    docs = [
        Document(page_content=text, metadata=metadata or {})
        for text, metadata in zip(data["documents"], data["metadatas"])
    ]
    return BM25Retriever.from_documents(docs, k=6, preprocess_func=tokenize)

@lru_cache(maxsize=1)
def get_ensemble_retriever():
    # Cached: rebuilding this per request reloads the embedding model and BM25 index
    vectorstore = get_vectorstore()
    chroma_retriever = vectorstore.as_retriever(search_kwargs={"k": 6})

    bm25_retriever = get_bm25_retriever(vectorstore)

    if bm25_retriever:
        print("Using Hybrid Search (BM25 + Vector)")
        return EnsembleRetriever(
            retrievers=[bm25_retriever, chroma_retriever],
            weights=[0.5, 0.5]
        )
    else:
        print("Warning: Chroma collection is empty. Run ingestion/document_loader.py first.")
        return chroma_retriever
