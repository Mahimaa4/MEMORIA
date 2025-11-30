from typing import List  
from google.genai import Client
from google.genai.errors import APIError
import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

client = None
if GEMINI_API_KEY:
    client = Client(api_key=GEMINI_API_KEY)
    print("✅ Gemini API connected")
else:
    raise RuntimeError("❌ No GEMINI_API_KEY found! Set it in your environment variables.")

EMBEDDING_MODEL = "text-embedding-004"
EMBEDDING_DIM = 768
MAX_CHARS = 2000

def get_embedding(text: str) -> List[float]:  # ✅ return type fixed
    """Return embedding vector from Gemini API"""
    if not text.strip():
        raise ValueError("❌ Text is empty. Cannot embed.")

    text = text[:MAX_CHARS]  # optional truncation

    try:
        resp = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=[text]  # ✅ Gemini expects 'contents', not 'content'
        )
        vector = resp.embeddings[0].values  # ✅ correct way to get vector
        return vector

    except APIError as e:
        raise RuntimeError(f"❌ Embedding failed: {e}")
