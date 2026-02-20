import streamlit as st

# ──────────────────────────────────────────────
# Reusable Streamlit UI Components
# ──────────────────────────────────────────────

def inject_custom_css():
    """Inject custom CSS for the YouTube dark-mode theme."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap');

        /* ── Global ── */
        .stApp {
            background: #0F0F0F;
        }

        /* ── Header ── */
        .app-header {
            text-align: center;
            padding: 2rem 0 1rem;
        }
        .app-header h1 {
            font-family: 'Roboto', sans-serif;
            font-size: 2.6rem;
            font-weight: 900;
            color: #FFFFFF;
            margin-bottom: 0.3rem;
            letter-spacing: -0.5px;
        }
        .app-header h1 .yt-icon {
            display: inline-block;
            background: #FF0000;
            color: #FFFFFF;
            border-radius: 8px;
            padding: 0.1em 0.35em;
            margin-right: 0.25em;
            font-size: 0.85em;
            vertical-align: middle;
            line-height: 1;
        }
        .app-header p {
            color: #AAAAAA;
            font-size: 1rem;
            font-family: 'Roboto', sans-serif;
        }

        /* ── Card ── */
        .glass-card {
            background: #272727;
            border: 1px solid #3A3A3A;
            border-radius: 12px;
            padding: 1.5rem 1.8rem;
            margin: 1rem 0;
        }
        .glass-card h3 {
            font-family: 'Roboto', sans-serif;
            font-weight: 700;
            color: #FFFFFF;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }

        /* ── Summary Box ── */
        .summary-box {
            background: #1A1A1A;
            border: 1px solid #3A3A3A;
            border-left: 4px solid #FF0000;
            border-radius: 0 12px 12px 0;
            padding: 1.2rem 1.5rem;
            margin-top: 1rem;
            color: #E0E0E0;
            font-size: 0.95rem;
            line-height: 1.75;
            font-family: 'Roboto', sans-serif;
        }

        /* ── Status Badge ── */
        .status-badge {
            display: inline-block;
            font-family: 'Roboto', sans-serif;
            font-size: 0.75rem;
            font-weight: 600;
            padding: 0.3rem 0.9rem;
            border-radius: 20px;
            margin: 0.3rem 0.3rem 0.3rem 0;
        }
        .badge-green {
            background: rgba(46, 204, 113, 0.15);
            color: #2ecc71;
            border: 1px solid rgba(46, 204, 113, 0.3);
        }
        .badge-blue {
            background: rgba(255, 0, 0, 0.10);
            color: #FF4E45;
            border: 1px solid rgba(255, 0, 0, 0.25);
        }
        .badge-yellow {
            background: rgba(255, 255, 255, 0.08);
            color: #FFFFFF;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        /* ── Answer Box ── */
        .answer-box {
            background: #1A1A1A;
            border: 1px solid #3A3A3A;
            border-left: 4px solid #CC0000;
            border-radius: 0 12px 12px 0;
            padding: 1.2rem 1.5rem;
            margin-top: 0.8rem;
            color: #E0E0E0;
            font-size: 0.95rem;
            line-height: 1.75;
            font-family: 'Roboto', sans-serif;
        }

        /* ── Divider ── */
        .divider {
            border: none;
            border-top: 1px solid #3A3A3A;
            margin: 1.5rem 0;
        }

        /* ── Streamlit Overrides ── */
        .stTextInput > div > div > input {
            background: #181818 !important;
            border: 1px solid #3A3A3A !important;
            border-radius: 10px !important;
            color: #FFFFFF !important;
            font-family: 'Roboto', sans-serif !important;
            padding: 0.6rem 1rem !important;
        }
        .stTextInput > div > div > input::placeholder {
            color: #717171 !important;
        }
        .stTextInput > div > div > input:focus {
            border-color: #FF0000 !important;
            box-shadow: 0 0 0 2px rgba(255, 0, 0, 0.15) !important;
        }

        .stButton > button {
            background: #FF0000 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 10px !important;
            font-family: 'Roboto', sans-serif !important;
            font-weight: 600 !important;
            padding: 0.55rem 1.8rem !important;
            font-size: 0.9rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(255, 0, 0, 0.25) !important;
        }
        .stButton > button:hover {
            background: #CC0000 !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 6px 20px rgba(255, 0, 0, 0.40) !important;
        }

        .stSpinner > div > div {
            border-top-color: #FF0000 !important;
        }
    </style>
    """, unsafe_allow_html=True)


def render_header():
    """Render the app title and subtitle."""
    st.markdown("""
    <div class="app-header">
        <h1><span class="yt-icon">▶</span> YouTube ChatBot</h1>
        <p>Paste a video ID → Get instant summaries & answers powered by RAG</p>
    </div>
    """, unsafe_allow_html=True)


def render_status_badges():
    """Render success status badges after index is built."""
    st.markdown("""
    <span class="status-badge badge-green">✓ Transcript loaded</span>
    <span class="status-badge badge-blue">✓ Vector store built</span>
    <span class="status-badge badge-yellow">✓ RAG chain ready</span>
    """, unsafe_allow_html=True)
