from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever

from config import RETRIEVER_SEARCH_TYPE, RETRIEVER_K

# ──────────────────────────────────────────────
# Stage 1d — Vector Store & Retriever
# ──────────────────────────────────────────────

def build_vector_store(documents: list[Document], embeddings) -> FAISS:
    """
    Build a FAISS vector store from document chunks and embeddings.

    Args:
        documents: List of chunked Document objects.
        embeddings: The embedding model instance.

    Returns:
        FAISS vector store with indexed documents.
    """
    return FAISS.from_documents(documents, embeddings)


def get_retriever(vector_store: FAISS) -> VectorStoreRetriever:
    """
    Convert a FAISS vector store into a LangChain retriever.

    Args:
        vector_store: The FAISS vector store.

    Returns:
        VectorStoreRetriever configured for similarity search.
    """
    return vector_store.as_retriever(
        search_type=RETRIEVER_SEARCH_TYPE,
        search_kwargs={"k": RETRIEVER_K},
    )
