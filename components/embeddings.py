from langchain_huggingface import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL

# ──────────────────────────────────────────────
# Stage 1c — Embedding Model Factory
# ──────────────────────────────────────────────

def get_embeddings() -> HuggingFaceEmbeddings:
    """
    Create and return the embedding model.

    Uses sentence-transformers locally (free, no API key needed).
    Swap this function to change the embedding provider.
    """
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
