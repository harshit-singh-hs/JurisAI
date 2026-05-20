import os
import sys

# Add parent directory to path to allow absolute imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from database.chroma_setup import get_vectorstore

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

def load_documents():
    print(f"Loading documents from {DATA_DIR}...")
    
    # Load Text files
    txt_loader = DirectoryLoader(DATA_DIR, glob="**/*.txt", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
    txt_docs = txt_loader.load()
    
    # Load PDF files
    try:
        import pypdf
        pdf_loader = DirectoryLoader(DATA_DIR, glob="**/*.pdf", loader_cls=PyPDFLoader)
        pdf_docs = pdf_loader.load()
    except ImportError:
        print("pypdf not installed. Skipping PDF files.")
        pdf_docs = []

    documents = txt_docs + pdf_docs
    print(f"Loaded {len(documents)} documents.")
    return documents

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split documents into {len(chunks)} chunks.")
    return chunks

def ingest_data():
    documents = load_documents()
    if not documents:
        print("No documents found to ingest.")
        return
        
    chunks = split_documents(documents)
    
    # Clean old indices to prevent duplication
    import shutil
    from database.chroma_setup import DB_DIR
    from database.hybrid_search import BM25_INDEX_PATH
    
    print("Clearing old Chroma DB directory...")
    shutil.rmtree(DB_DIR, ignore_errors=True)
    
    if os.path.exists(BM25_INDEX_PATH):
        print("Clearing old BM25 index...")
        os.remove(BM25_INDEX_PATH)
        
    vectorstore = get_vectorstore()
    
    print("Adding documents to ChromaDB...")
    # Add in batches of 100 to avoid any database limits
    batch_size = 100
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        print(f"Ingesting batch {i//batch_size + 1} of {(len(chunks)-1)//batch_size + 1}...")
        vectorstore.add_documents(batch)
    
    print("Building BM25 Index for Hybrid Search...")
    import pickle
    from langchain_community.retrievers import BM25Retriever
    
    bm25_retriever = BM25Retriever.from_documents(chunks)
    bm25_retriever.k = 6
    
    with open(BM25_INDEX_PATH, "wb") as f:
        pickle.dump(bm25_retriever, f)
        
    print("Ingestion complete.")

if __name__ == "__main__":
    ingest_data()
