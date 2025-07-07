import os
import streamlit as st
import pickle
import time

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    UnstructuredURLLoader,
    PyPDFLoader,
    TextLoader,
    CSVLoader
)
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document

# App Title
st.set_page_config(page_title="EquiSage: AI News Analyst", page_icon="📊")
st.title("📊 EquiSage: AI-Powered News Research Assistant")
st.sidebar.title("📰 Enter News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    if url:
        urls.append(url)

uploaded_files = st.sidebar.file_uploader(
    "📁 Upload PDF, TXT, or CSV files",
    type=["pdf", "txt", "csv"],
    accept_multiple_files=True
)

process_url_clicked = st.sidebar.button("🔍 Process Content")
file_path = "faiss_store.pkl"
main_placeholder = st.empty()

# Initialize Groq LLM
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant"
)

# Process URLs and uploaded files
if process_url_clicked and (urls or uploaded_files):
    documents = []

    # Load from URLs
    if urls:
        loader = UnstructuredURLLoader(urls=urls)
        main_placeholder.text("🔄 Loading data from URLs...")
        url_docs = loader.load()
        for i, doc in enumerate(url_docs):
            doc.metadata["source"] = urls[i]
        documents.extend(url_docs)

    # Load from uploaded files
    for file in uploaded_files:
        file_name = file.name
        file_path_temp = os.path.join("temp", file_name)
        os.makedirs("temp", exist_ok=True)
        with open(file_path_temp, "wb") as f:
            f.write(file.read())

        if file_name.endswith(".pdf"):
            loader = PyPDFLoader(file_path_temp)
        elif file_name.endswith(".txt"):
            loader = TextLoader(file_path_temp)
        elif file_name.endswith(".csv"):
            loader = CSVLoader(file_path_temp)
        else:
            continue

        file_docs = loader.load()
        for doc in file_docs:
            doc.metadata["source"] = file_name
        documents.extend(file_docs)

    # Split and embed
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    main_placeholder.text("✂️ Splitting text into chunks...")
    docs = text_splitter.split_documents(documents)
    for doc in docs:
        doc.metadata["source"] = doc.metadata.get("source", "Unknown")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("🧠 Building vector store with embeddings...")

    with open(file_path, "wb") as f:
        pickle.dump(vectorstore, f)

    main_placeholder.success("✅ Content processed and stored!")

    # Summarize each document
    st.subheader("📝 Summaries")
    summary_chain = load_summarize_chain(llm, chain_type="stuff")
    for doc in documents:
        short_doc = doc.page_content[:3000]
        summary = summary_chain.run([Document(page_content=short_doc)])
        source = doc.metadata.get("source", "Unknown")
        st.markdown(f"**Source:** {source}")
        st.info(summary)

# Question-answering interface
query = main_placeholder.text_input("💬 Ask a question about the content:")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)

        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever()
        )
        result = chain({"question": query}, return_only_outputs=True)

        st.header("🧠 Answer")
        st.write(result["answer"])

        sources = result.get("sources", "")
        if sources:
            st.subheader("🔗 Sources")
            unique_sources = set(sources.split("\n"))
            for source in unique_sources:
                if source.startswith("http"):
                    st.markdown(f"- [🔗 {source}]({source})")
                else:
                    st.write(f"- {source}")