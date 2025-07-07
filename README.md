

**EquiSage** is an AI-powered research assistant that helps you analyze financial news articles and uploaded documents. Built with Streamlit, LangChain, and Groq-hosted LLaMA 3.1, it summarizes content, answers questions, and cites sources—all in one place.

---

## 🚀 Features

- 🔗 Analyze news from URLs
- 📁 Upload and process PDFs, TXTs, and CSVs
- 🧠 Summarize content using LLM
- ❓ Ask questions and get source-backed answers
- 💾 Store embeddings with FAISS for fast retrieval

---

## 🧠 Tech Stack

| Component        | Tool/Library                     |
|------------------|----------------------------------|
| UI               | Streamlit                        |
| LLM              | Groq + LLaMA 3.1 (via langchain-groq) |
| Embeddings       | HuggingFace (MiniLM)             |
| Vector Store     | FAISS                            |
| Document Parsing | LangChain loaders (URL, PDF, TXT, CSV) |
| Summarization    | LangChain summarize chain        |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Mmeetttt/eqisage-ai.git
cd eqisage-ai
