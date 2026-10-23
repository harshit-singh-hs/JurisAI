FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Bake the ONNX embedding model into the image so the first request doesn't download it
# (Chroma only needs the extracted files, so drop the 80MB archive)
RUN python -c "from chromadb.utils.embedding_functions import ONNXMiniLM_L6_V2; ONNXMiniLM_L6_V2()(['warmup'])" \
    && rm -f /root/.cache/chroma/onnx_models/all-MiniLM-L6-v2/onnx.tar.gz

# Copy application code
COPY . .

# Create data directory
RUN mkdir -p /app/data

# Expose port
EXPOSE 8000

# Render (and most hosts) assign the port via $PORT
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
