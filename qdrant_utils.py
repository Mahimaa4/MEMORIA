from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance, PointStruct, ScoredPoint
from typing import List

COLLECTION_NAME = "pdf_rag_collection"
client = QdrantClient(":memory:")

# ------------------ CREATE COLLECTION ------------------
def setup_collection(vector_size: int):
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )
    print("🌍 Qdrant in-memory collection created.")


# ------------------ STORE EMBEDDINGS ------------------
def store_vectors(points: List[PointStruct]):
    client.upsert(collection_name=COLLECTION_NAME, points=points)
    print(f"📌 Stored {len(points)} vectors in DB.")


# ------------------ SEARCH EMBEDDINGS ------------------
def search_vectors(query_vector: List[float], limit=5) -> List[ScoredPoint]:
    return client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=limit,
        with_payload=True
    )
