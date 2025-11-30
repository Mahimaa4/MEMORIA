
from modules.qdrant_utils import search_vectors
from embeddings import get_embedding
from google import genai
import os

GEN_MODEL = "models/text-bison-001"   # works with your SDK version

def get_answer_from_pdf(query, top_k=5):

    qv = get_embedding(query)
    if not qv:
        return {"answer":"Embedding failed","sources":[]}

    results = search_vectors(qv, limit=top_k)

    chunks = [hit.payload["text"] for hit in results if "text" in hit.payload]
    context = "\n---\n".join(chunks)

    if not context.strip():
        return {"answer":"⚠ No relevant content from PDF","sources":[]}

    prompt = f"""You are an academic assistant.
Read the data below and answer based only on it.

PDF CONTENT:
{context}

QUESTION: {query}

Respond clearly from only the PDF.
"""

    response = genai.generate_text(
        model=GEN_MODEL,
        prompt=prompt,
        temperature=0.4,
        max_output_tokens=300
    )

    return {
        "answer": response.result,
        "sources": chunks[:3]
    }
