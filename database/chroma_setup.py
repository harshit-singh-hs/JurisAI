import os
import shutil
from functools import lru_cache
from chromadb.utils.embedding_functions import ONNXMiniLM_L6_V2
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DB_DIR = os.path.join(DATA_DIR, "chroma_db")

if os.environ.get("VERCEL"):
    # Vercel's filesystem is read-only outside /tmp
    ONNXMiniLM_L6_V2.DOWNLOAD_PATH = "/tmp/onnx_models/all-MiniLM-L6-v2"
    RUNTIME_DB_DIR = "/tmp/chroma_db"
else:
    RUNTIME_DB_DIR = os.path.join(DATA_DIR, "chroma_runtime")


class MiniLMEmbeddings(Embeddings):
    """all-MiniLM-L6-v2 run through Chroma's bundled ONNX runtime.

    Produces the same vectors as sentence-transformers' all-MiniLM-L6-v2, but without
    PyTorch, which cost ~1GB of image size and several hundred MB of RAM.
    """

    def __init__(self):
        self._embed = ONNXMiniLM_L6_V2()

    def embed_documents(self, texts):
        return [vector.tolist() for vector in self._embed(texts)]

    def embed_query(self, text):
        return self.embed_documents([text])[0]


@lru_cache(maxsize=1)
def get_embedding_model():
    # Loading the model takes seconds, so load it once per process
    return MiniLMEmbeddings()

@lru_cache(maxsize=1)
def get_runtime_db_dir():
    # Chroma writes a lock row to its SQLite file on every open, which dirtied the tracked index
    # and fails on read-only filesystems (e.g. Vercel), so the app queries a copy that is
    # refreshed whenever the tracked index changes
    source = os.path.join(DB_DIR, "chroma.sqlite3")
    stamp_path = os.path.join(RUNTIME_DB_DIR, ".source_stamp")
    stamp = f"{os.path.getsize(source)}:{os.path.getmtime(source)}"
    try:
        with open(stamp_path) as f:
            if f.read() == stamp:
                return RUNTIME_DB_DIR
    except OSError:
        pass

    shutil.rmtree(RUNTIME_DB_DIR, ignore_errors=True)
    shutil.copytree(DB_DIR, RUNTIME_DB_DIR, dirs_exist_ok=True)
    with open(stamp_path, "w") as f:
        f.write(stamp)
    return RUNTIME_DB_DIR

def get_vectorstore(persist_directory=None):
    """Open the legal documents collection; pass DB_DIR to write to the tracked index itself."""
    return Chroma(
        collection_name="legal_documents",
        embedding_function=get_embedding_model(),
        persist_directory=persist_directory or get_runtime_db_dir()
    )

def get_retriever():
    vectorstore = get_vectorstore()
    return vectorstore.as_retriever(search_kwargs={"k": 3})
