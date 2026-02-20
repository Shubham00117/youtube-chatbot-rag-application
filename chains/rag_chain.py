from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from prompts.templates import RAG_PROMPT, SUMMARY_PROMPT

# ──────────────────────────────────────────────
# LCEL RAG Chain Assembly
# ──────────────────────────────────────────────

def _format_docs(retrieved_docs) -> str:
    """Join retrieved Document objects into a single context string."""
    return "\n\n".join(doc.page_content for doc in retrieved_docs)


def build_rag_chain(retriever, llm):
    """
    Assemble the full LCEL RAG chain.

    Pipeline: question → (context + question) → prompt → LLM → string

    Args:
        retriever: LangChain retriever (e.g. from FAISS).
        llm: LangChain LLM instance (e.g. ChatGroq).

    Returns:
        An LCEL Runnable chain.
    """
    parallel_chain = RunnableParallel({
        "context": retriever | RunnableLambda(_format_docs),
        "question": RunnablePassthrough(),
    })

    rag_chain = parallel_chain | RAG_PROMPT | llm | StrOutputParser()
    return rag_chain


def generate_summary(rag_chain) -> str:
    """Generate a comprehensive summary of the video via the RAG chain."""
    return rag_chain.invoke(SUMMARY_PROMPT)
