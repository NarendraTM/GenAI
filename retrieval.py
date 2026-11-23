import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

@st.cache_resource(show_spinner="Loading embedding model (first run may download it)...")
def get_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL)

def embed_chunks(chunks):
    model = get_embedding_model()
    texts = [c["text"] for c in chunks]
    vectors = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
    return np.asarray(vectors, dtype=np.float32)

def retrieve(question, chunks, vectors, top_k=4):
    model = get_embedding_model()
    query_vector = model.encode([question], normalize_embeddings=True, show_progress_bar=False)[0]
    scores = np.dot(vectors, query_vector)
    indices = np.argsort(scores)[::-1][:top_k]
    results = []
    for idx in indices:
        item = dict(chunks[int(idx)])
        item["score"] = float(scores[int(idx)])
        results.append(item)
    return results
