# ▶ YouTube ChatBot — RAG Application

A YouTube Video ChatBot powered by **Retrieval-Augmented Generation (RAG)**. Paste a video ID, get instant summaries, and ask questions about any YouTube video — all through a sleek Streamlit interface.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green?logo=langchain)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎥 **Video Transcript Loading** | Fetches English transcripts from any YouTube video using its video ID |
| 📝 **AI-Powered Summary** | Generates a detailed summary covering main topics and key takeaways |
| 💬 **Q&A Chat** | Ask any question about the video and get contextual answers |
| ⚡ **Ultra-Fast Inference** | Uses Groq's Llama 3.3 70B for lightning-fast responses |
| 🔍 **Semantic Search** | FAISS vector store with similarity retrieval for accurate context |
| 🎨 **Dark Glassmorphism UI** | Modern, premium-looking Streamlit interface |

---

## 🏗️ Architecture — LangChain Modular RAG

Each RAG pipeline stage is an **isolated, swappable module**:

```
├── components/                  # One module per RAG stage
│   ├── document_loader.py       # Stage 1a: YouTube transcript ingestion
│   ├── text_splitter.py         # Stage 1b: Text chunking
│   ├── embeddings.py            # Stage 1c: Embedding model factory
│   ├── vector_store.py          # Stage 1d: FAISS indexing & retriever
│   └── llm.py                   # LLM factory (Groq)
│
├── prompts/templates.py         # All prompt definitions
├── chains/rag_chain.py          # LCEL chain assembly
├── ui/components.py             # Streamlit UI helpers
├── config.py                    # Tunable constants
└── app.py                       # Entry point
```

### RAG Pipeline Flow

```
YouTube Video ID
      │
      ▼
┌─────────────┐    ┌──────────────┐    ┌────────────┐    ┌─────────────┐
│  Transcript  │───▶│  Text Split  │───▶│  Embed     │───▶│  FAISS      │
│  Fetching    │    │  (1000 chars)│    │  (MiniLM)  │    │  Index      │
└─────────────┘    └──────────────┘    └────────────┘    └──────┬──────┘
                                                                │
                   User Question ──────────────────────────────▶│
                                                                ▼
                                                        ┌──────────────┐
                                                        │  Retriever   │
                                                        │  (top 4)     │
                                                        └──────┬───────┘
                                                               │
                                                               ▼
                                                     ┌──────────────────┐
                                                     │  Prompt Template │
                                                     │  (context + Q)   │
                                                     └────────┬─────────┘
                                                              │
                                                              ▼
                                                     ┌──────────────────┐
                                                     │   Groq LLM      │
                                                     │  (Llama 3.3 70B)│
                                                     └────────┬─────────┘
                                                              │
                                                              ▼
                                                          Answer
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A [Groq API key](https://console.groq.com/keys) (free tier available)

### Installation

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd "Youtube ChatBot ( RAG Application)"

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your API key
cp .env.example .env
# Edit .env and paste your Groq API key:
# GROQ_API_KEY=gsk_your_key_here

# 4. Run the app
streamlit run app.py
```

The app will open at **http://localhost:8501**

---

## 📖 How to Use

### Step 1 — Load a Video
1. Go to any YouTube video
2. Copy the **video ID** from the URL (the part after `v=`)
   - Example: `https://www.youtube.com/watch?v=LPZh9BOjkQs` → ID is `LPZh9BOjkQs`
3. Paste the ID into the input field
4. Click **🔗 Load Video & Build Index**
5. Wait for the status badges: ✓ Transcript loaded → ✓ Vector store built → ✓ RAG chain ready

### Step 2 — Generate Summary
1. Click **✨ Generate Summary**
2. The AI will analyze the video transcript and produce a detailed summary

### Step 3 — Ask Questions
1. Type any question about the video in the Q&A section
2. Click **🚀 Get Answer**
3. The RAG pipeline retrieves relevant chunks and generates a contextual answer

---

## ⚙️ Configuration

All settings are in [`config.py`](config.py):

| Setting | Default | Description |
|---------|---------|-------------|
| `CHUNK_SIZE` | 1000 | Characters per text chunk |
| `CHUNK_OVERLAP` | 200 | Overlap between chunks |
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Sentence-transformers model (local, free) |
| `LLM_MODEL` | `llama-3.3-70b-versatile` | Groq model for generation |
| `LLM_TEMPERATURE` | 0.2 | Creativity level (0 = focused, 1 = creative) |
| `RETRIEVER_K` | 4 | Number of chunks to retrieve |

---

## 🔌 Swappability

| Want to change... | Edit only... |
|---|---|
| LLM provider (Groq → OpenAI) | `components/llm.py` |
| Embedding model | `components/embeddings.py` |
| Vector store (FAISS → Pinecone) | `components/vector_store.py` |
| Data source (YouTube → PDF) | `components/document_loader.py` |
| Chunking strategy | `components/text_splitter.py` |
| Prompt template | `prompts/templates.py` |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **LLM** | Groq — Llama 3.3 70B Versatile |
| **Embeddings** | all-MiniLM-L6-v2 (local, free) |
| **Vector Store** | FAISS (in-memory) |
| **Framework** | LangChain (LCEL) |
| **Frontend** | Streamlit |
| **Transcript** | youtube-transcript-api |

---

## 📁 Project Structure

```
Youtube ChatBot ( RAG Application)/
├── .env                         # API keys (gitignored)
├── .env.example                 # Template
├── .gitignore
├── .streamlit/config.toml       # Streamlit dark theme
├── requirements.txt
├── README.md
│
├── config.py                    # All tunable constants
│
├── components/                  # RAG pipeline components
│   ├── __init__.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── llm.py
│
├── prompts/                     # Prompt templates
│   ├── __init__.py
│   └── templates.py
│
├── chains/                      # LCEL chain composition
│   ├── __init__.py
│   └── rag_chain.py
│
├── ui/                          # Streamlit UI layer
│   ├── __init__.py
│   └── components.py
│
└── app.py                       # Entry point
```

---

## 📜 License

This project is for educational purposes.
