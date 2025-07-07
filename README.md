

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
## 📸 Screenshots

### 🔍 Homepage

![home page](https://github.com/user-attachments/assets/13e9c213-9354-4e14-802a-5634f009fe40)

### 📝 Summary Output
![summary](https://github.com/user-attachments/assets/b0508e18-38d9-4d11-a8d2-c166b57c0b23)

### ❓ Q&A with Sources
![result 1](https://github.com/user-attachments/assets/39332941-05bd-4082-887c-2c8c5d313e2c)
![result 2](https://github.com/user-attachments/assets/28caca23-9af8-4da3-915b-07d360992c73)
![result 3](https://github.com/user-attachments/assets/ef968f1a-9697-4d4c-9423-15c2027755e0)
![result 4](https://github.com/user-attachments/assets/934e0ea9-6306-4bfd-ad06-8ab4aec1c3a7)
![result 5](https://github.com/user-attachments/assets/f436c2de-f045-4360-994b-72e3109795ff)




## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Mmeetttt/eqisage-ai.git
cd eqisage-ai
