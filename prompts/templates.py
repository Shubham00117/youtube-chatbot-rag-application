from langchain_core.prompts import PromptTemplate

# ──────────────────────────────────────────────
# Prompt Templates
# ──────────────────────────────────────────────

RAG_PROMPT = PromptTemplate(
    template="""You are a helpful assistant.
Answer ONLY from the provided transcript context.
If the context is insufficient, just say you don't know.

{context}
Question: {question}""",
    input_variables=["context", "question"],
)

SUMMARY_PROMPT = (
    "Provide a detailed summary of this video. "
    "Cover all the main topics, key points, and important takeaways discussed."
)
