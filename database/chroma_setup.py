import hashlib
import io
import os
import shutil
import tarfile
import urllib.request
from functools import cached_property, lru_cache
from chromadb.utils.embedding_functions import ONNXMiniLM_L6_V2
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DB_DIR = os.path.join(DATA_DIR, "chroma_db")

if os.environ.get("VERCEL"):
    # Vercel's filesystem is read-only outside /tmp
    RUNTIME_DB_DIR = "/tmp/chroma_db"
else:
    RUNTIME_DB_DIR = os.path.join(DATA_DIR, "chroma_runtime")


class InMemoryMiniLM(ONNXMiniLM_L6_V2):
    """Chroma's all-MiniLM-L6-v2 embedder, loaded straight into memory instead of from disk.

    On Vercel the app's packages are installed into /tmp at startup, leaving too little room
    there for the ~170MB model download, and bundling the model would push the function past
    Vercel's 500MB size limit. Only loading is overridden; Chroma's own _forward() still
    computes the vectors, so they match the search index exactly.
    """

    def __init__(self):
        super().__init__()
        with urllib.request.urlopen(self.MODEL_DOWNLOAD_URL, timeout=120) as response:
            archive = response.read()
        if hashlib.sha256(archive).hexdigest() != self._MODEL_SHA256:
            raise RuntimeError("Embedding model download failed its checksum")
        with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as tar:
            self._files = {
                os.path.basename(member.name): tar.extractfile(member).read()
                for member in tar.getmembers() if member.isfile()
            }

    def _download_model_if_not_exists(self):
        pass  # Already in memory

    @cached_property
    def tokenizer(self):
        tokenizer = self.Tokenizer.from_str(self._files.pop("tokenizer.json").decode("utf-8"))
        # Same settings as ONNXMiniLM_L6_V2.tokenizer
        tokenizer.enable_truncation(max_length=256)
        tokenizer.enable_padding(pad_id=0, pad_token="[PAD]", length=256)
        return tokenizer

    @cached_property
    def model(self):
        options = self.ort.SessionOptions()
        options.log_severity_level = 3
        options.graph_optimization_level = self.ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        return self.ort.InferenceSession(
            self._files.pop("model.onnx"), providers=["CPUExecutionProvider"], sess_options=options
        )


class MiniLMEmbeddings(Embeddings):
    """all-MiniLM-L6-v2 run through Chroma's bundled ONNX runtime.

    Produces the same vectors as sentence-transformers' all-MiniLM-L6-v2, but without
    PyTorch, which cost ~1GB of image size and several hundred MB of RAM.
    """

    def __init__(self):
        self._embed = InMemoryMiniLM() if os.environ.get("VERCEL") else ONNXMiniLM_L6_V2()

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
