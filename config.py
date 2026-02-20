# ──────────────────────────────────────────────
# Centralized Configuration & Constants
# ──────────────────────────────────────────────

# Text Splitter (Stage 1b)
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Embedding Model (Stage 1c) — runs locally via sentence-transformers
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# LLM (Stage 4) — Groq
LLM_MODEL = "llama-3.3-70b-versatile"
LLM_TEMPERATURE = 0.2

# Retriever (Stage 2)
RETRIEVER_SEARCH_TYPE = "similarity"
RETRIEVER_K = 4
