import fitz  # PyMuPDF
from typing import List
from embeddings import get_embedding  # ✅ importing correct function
from modules.qdrant_utils import store_vectors  # ✅ correct file
from qdrant_client.http.models import PointStruct
import uuid

MAX_CHARS = 2000

def make_chunks(text: str, size=500) -> List[str]:
    return [text[i:i+size] for i in range(0, len(text), size) if text[i:i+size].strip()]

def process_pdf(file_bytes: bytes, chunk_size: int = 500) -> int:
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    texts = ""
    for page in doc:
        texts += page.get_text()
    doc.close()

    chunks = make_chunks(texts, chunk_size)
    points = []

    for ch in chunks:
        ch = ch[:MAX_CHARS]
        emb = get_embedding(ch)
        if emb:  # ✅ no need to check None again
            points.append(PointStruct(
                id=str(uuid.uuid4()),
                vector=emb,
                payload={"chunk": ch}
            ))

    if points:
        store_vectors(points)  # ✅ storing vectors

    print(f"📄 Total chunks embedded: {len(points)}")
    return len(points)
