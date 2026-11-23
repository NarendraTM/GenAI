import streamlit as st
from pdf_processor import extract_pdf_pages, chunk_pages
from retrieval import embed_chunks, retrieve
from ollama_client import generate_answer, ollama_available

st.set_page_config(page_title="Academic Document Assistant", page_icon="📚", layout="wide")
st.title("📚 Intelligent Academic Assistant")
st.caption("Ask questions about your academic PDFs. Answers are grounded in the documents you upload.")

with st.sidebar:
    st.header("Settings")
    ollama_url = st.text_input("Ollama URL", value="http://localhost:11434")
    model_name = st.text_input("Chat model", value="llama3.2")
    chunk_size = st.slider("Chunk size (characters)", 500, 2000, 1000, 100)
    overlap = st.slider("Chunk overlap (characters)", 0, 400, 150, 25)
    top_k = st.slider("Retrieved chunks (Top-K)", 1, 8, 4)
    st.divider()
    ollama_ok = ollama_available(ollama_url)
    st.markdown("Ollama status: " + ("🟢 Available" if ollama_ok else "🔴 Not detected"))
    st.caption("Start Ollama and pull the selected model before asking questions.")

uploaded_files = st.file_uploader("Upload academic PDF file(s)", type=["pdf"], accept_multiple_files=True)
for key, default in [("chunks", []), ("vectors", None), ("chat", []), ("indexed_names", [])]:
    if key not in st.session_state:
        st.session_state[key] = default

if uploaded_files:
    names = [f.name for f in uploaded_files]
    if names != st.session_state.indexed_names:
        with st.spinner("Extracting text and creating semantic embeddings..."):
            pages = []
            for file in uploaded_files:
                pages.extend(extract_pdf_pages(file.getvalue(), file.name))
            chunks = chunk_pages(pages, chunk_size=chunk_size, overlap=overlap)
            if chunks:
                vectors = embed_chunks(chunks)
                st.session_state.chunks = chunks
                st.session_state.vectors = vectors
                st.session_state.indexed_names = names
                st.session_state.chat = []
            else:
                st.session_state.chunks = []
                st.session_state.vectors = None
                st.error("No extractable text found. Scanned PDFs require OCR, which is not included.")
        if st.session_state.chunks:
            st.success(f"Indexed {len(uploaded_files)} document(s) into {len(st.session_state.chunks)} text chunks.")

if st.session_state.chunks:
    with st.expander("Indexed document details"):
        st.write("Files:", ", ".join(st.session_state.indexed_names))
        st.write(f"Chunks indexed: {len(st.session_state.chunks)}")
        st.write("Embedding model: sentence-transformers/all-MiniLM-L6-v2")
    for item in st.session_state.chat:
        with st.chat_message(item["role"]):
            st.markdown(item["content"])
            if item.get("sources"):
                with st.expander("Sources used"):
                    for src in item["sources"]:
                        st.markdown(f"- **{src['file']}**, page {src['page']} (similarity: {src['score']:.3f})")
    question = st.chat_input("Ask a question about your uploaded documents…")
    if question:
        st.session_state.chat.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)
        with st.chat_message("assistant"):
            if not ollama_available(ollama_url):
                st.error("Ollama is not running. Start Ollama, then try again.")
                answer, sources = "Ollama is unavailable. Start it and retry.", []
            else:
                with st.spinner("Searching documents and generating answer..."):
                    selected = retrieve(question, st.session_state.chunks, st.session_state.vectors, top_k)
                    answer = generate_answer(question, selected, ollama_url, model_name)
                    sources = [{"file": c["file"], "page": c["page"], "score": float(c["score"])} for c in selected]
                st.markdown(answer)
                if sources:
                    with st.expander("Sources used"):
                        for src in sources:
                            st.markdown(f"- **{src['file']}**, page {src['page']} (similarity: {src['score']:.3f})")
        st.session_state.chat.append({"role": "assistant", "content": answer, "sources": sources})
    if st.button("Clear conversation"):
        st.session_state.chat = []
        st.rerun()
else:
    st.info("Upload one or more PDFs above to begin.")
    st.markdown("**How to use**\n1. Upload PDFs.\n2. Wait for indexing.\n3. Ask a question.\n4. Review answer and source pages.")
