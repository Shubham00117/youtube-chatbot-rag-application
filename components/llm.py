from langchain_groq import ChatGroq

from config import LLM_MODEL, LLM_TEMPERATURE

# ──────────────────────────────────────────────
# LLM Factory
# ──────────────────────────────────────────────

def get_llm() -> ChatGroq:
    """
    Create and return the LLM instance.

    Uses Groq for ultra-fast inference.
    Swap this function to change the LLM provider.
    """
    return ChatGroq(
        model=LLM_MODEL,
        temperature=LLM_TEMPERATURE,
    )
