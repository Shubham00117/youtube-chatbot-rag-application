import streamlit as st

# ──────────────────────────────────────────────
# Reusable Streamlit UI Components
# ──────────────────────────────────────────────

def inject_custom_css():
    """Inject custom CSS for the dark glassmorphism theme."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        /* Global */
        .stApp {
            background: linear-gradient(160deg, #0f0c29 0%, #1a1a3e 40%, #24243e 100%);
        }

        /* Header */
        .app-header {
            text-align: center;
            padding: 2rem 0 1rem;
        }
        .app-header h1 {
            font-family: 'Inter', sans-serif;
            font-size: 2.6rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ff416c, #ff4b2b, #f7971e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.3rem;
            letter-spacing: -0.5px;
        }
        .app-header p {
            color: #8b8fa3;
            font-size: 1rem;
            font-family: 'Inter', sans-serif;
        }

        /* Glass Card */
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 1.5rem 1.8rem;
            margin: 1rem 0;
            backdrop-filter: blur(12px);
        }
        .glass-card h3 {
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            color: #e0e0e0;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }

        /* Summary Box */
        .summary-box {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-left: 4px solid #ff416c;
            border-radius: 0 12px 12px 0;
            padding: 1.2rem 1.5rem;
            margin-top: 1rem;
            color: #d0d0d0;
            font-size: 0.95rem;
            line-height: 1.75;
            font-family: 'Inter', sans-serif;
        }

        /* Status Badge */
        .status-badge {
            display: inline-block;
            font-family: 'Inter', sans-serif;
            font-size: 0.75rem;
            font-weight: 600;
            padding: 0.3rem 0.9rem;
            border-radius: 20px;
            margin: 0.3rem 0.3rem 0.3rem 0;
        }
        .badge-green {
            background: rgba(72, 199, 142, 0.15);
            color: #48c78e;
            border: 1px solid rgba(72, 199, 142, 0.3);
        }
        .badge-blue {
            background: rgba(66, 133, 244, 0.15);
            color: #4285f4;
            border: 1px solid rgba(66, 133, 244, 0.3);
        }
        .badge-yellow {
            background: rgba(255, 193, 7, 0.15);
            color: #ffc107;
            border: 1px solid rgba(255, 193, 7, 0.3);
        }

        /* Chat answer box */
        .answer-box {
            background: rgba(66, 133, 244, 0.06);
            border: 1px solid rgba(66, 133, 244, 0.15);
            border-left: 4px solid #4285f4;
            border-radius: 0 12px 12px 0;
            padding: 1.2rem 1.5rem;
            margin-top: 0.8rem;
            color: #d0d0d0;
            font-size: 0.95rem;
            line-height: 1.75;
            font-family: 'Inter', sans-serif;
        }

        /* Divider */
        .divider {
            border: none;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
            margin: 1.5rem 0;
        }

        /* Override Streamlit defaults */
        .stTextInput > div > div > input {
            background: rgba(255, 255, 255, 0.06) !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 10px !important;
            color: #e0e0e0 !important;
            font-family: 'Inter', sans-serif !important;
            padding: 0.6rem 1rem !important;
        }
        .stTextInput > div > div > input::placeholder {
            color: #6b6b8d !important;
        }
        .stTextInput > div > div > input:focus {
            border-color: #ff416c !important;
            box-shadow: 0 0 0 2px rgba(255, 65, 108, 0.15) !important;
        }

        .stButton > button {
            background: linear-gradient(135deg, #ff416c, #ff4b2b) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            padding: 0.55rem 1.8rem !important;
            font-size: 0.9rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(255, 65, 108, 0.3) !important;
        }
        .stButton > button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 6px 20px rgba(255, 65, 108, 0.45) !important;
        }

        .stSpinner > div > div {
            border-top-color: #ff416c !important;
        }
    </style>
    """, unsafe_allow_html=True)


def render_header():
    """Render the app title and subtitle."""
    st.markdown("""
    <div class="app-header">
        <h1>▶ YouTube ChatBot</h1>
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
