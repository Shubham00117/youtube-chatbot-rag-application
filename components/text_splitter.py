from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_SIZE, CHUNK_OVERLAP

# ──────────────────────────────────────────────
# Stage 1b — Text Splitting
# ──────────────────────────────────────────────

def split_text(text: str) -> list[Document]:
    """
    Split raw transcript text into LangChain Document chunks.

    Args:
        text: The full transcript as a single string.

    Returns:
        List of Document objects, each containing a chunk of text.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    return splitter.create_documents([text])
