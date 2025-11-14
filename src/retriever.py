import os, numpy as np
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer, CrossEncoder
from src.config import CHROMA_PATH, EMBED_MODEL, TOP_K, RERANK_TOP


client = PersistentClient(path=CHROMA_PATH)
collection = client.get_collection("football_kb")
encoder = SentenceTransformer(EMBED_MODEL)
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def retrieve(query: str) -> str:
    qemb = encoder.encode(query).tolist()
    res = collection.query(query_embeddings=[qemb], n_results=TOP_K)
    docs = res["documents"][0]
    pairs = [(query, d) for d in docs]
    scores = reranker.predict(pairs)
    top = np.argsort(scores)[::-1][:RERANK_TOP]
    return "\n\n".join([docs[i] for i in top])

