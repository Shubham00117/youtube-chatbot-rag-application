import streamlit as st
from dotenv import load_dotenv

from components import load_transcript, split_text, get_embeddings, build_vector_store, get_retriever, get_llm
from chains import build_rag_chain, generate_summary
from ui import inject_custom_css, render_header, render_status_badges

load_dotenv()

# ──────────────────────────────────────────────
# Page Config
# ──────────────────────────────────────────────

st.set_page_config(page_title="YouTube ChatBot", page_icon="▶️", layout="centered")
inject_custom_css()
render_header()

# ──────────────────────────────────────────────
# Session State
# ──────────────────────────────────────────────

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None
if "video_loaded" not in st.session_state:
    st.session_state.video_loaded = False
if "summary" not in st.session_state:
    st.session_state.summary = None

# ──────────────────────────────────────────────
# 1. Video ID Input + Load
# ──────────────────────────────────────────────

st.markdown('<div class="glass-card"><h3>📺 Enter YouTube Video ID</h3>', unsafe_allow_html=True)
video_id = st.text_input("Video ID", placeholder="e.g. LPZh9BOjkQs", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    load_btn = st.button("🔗 Load Video & Build Index", use_container_width=True)

if load_btn and video_id:
    try:
        # Stage 1a — Document Ingestion
        with st.spinner("📥 Fetching transcript..."):
            transcript = load_transcript(video_id.strip())

        if transcript:
            with st.spinner("⚙️ Building RAG index..."):
                # Stage 1b — Text Splitting
                chunks = split_text(transcript)
                # Stage 1c — Embedding
                embeddings = get_embeddings()
                # Stage 1d — Vector Store
                vector_store = build_vector_store(chunks, embeddings)
                # Retriever + LLM + Chain Assembly
                retriever = get_retriever(vector_store)
                llm = get_llm()
                st.session_state.rag_chain = build_rag_chain(retriever, llm)
                st.session_state.video_loaded = True
                st.session_state.summary = None

            render_status_badges()
        else:
            st.error("❌ Could not fetch transcript. Check the video ID or ensure captions are available.")
    except RuntimeError as e:
        st.error(f"❌ {e}")

elif load_btn and not video_id:
    st.warning("⚠️ Please enter a YouTube video ID first.")

# ──────────────────────────────────────────────
# 2. Summary Section
# ──────────────────────────────────────────────

if st.session_state.video_loaded:
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="glass-card"><h3>📝 Video Summary</h3>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        summary_btn = st.button("✨ Generate Summary", use_container_width=True)

    if summary_btn:
        with st.spinner("🤖 Generating summary..."):
            st.session_state.summary = generate_summary(st.session_state.rag_chain)

    if st.session_state.summary:
        st.markdown(f'<div class="summary-box">{st.session_state.summary}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ──────────────────────────────────────────
    # 3. Q&A Section
    # ──────────────────────────────────────────

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<div class="glass-card"><h3>💬 Ask a Question</h3>', unsafe_allow_html=True)

    question = st.text_input("Your question", placeholder="Ask anything about this video...", label_visibility="collapsed")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        ask_btn = st.button("🚀 Get Answer", use_container_width=True)

    if ask_btn and question:
        with st.spinner("🔍 Searching & generating answer..."):
            answer = st.session_state.rag_chain.invoke(question)
        st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)
    elif ask_btn and not question:
        st.warning("⚠️ Please type a question first.")

    st.markdown('</div>', unsafe_allow_html=True)
