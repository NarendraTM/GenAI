# Video Presentation Script (target 8–9 minutes; under 10-minute maximum)

> Use the live app or screen recording for the demo. Add actual screenshots and avoid narrating results that have not been verified.

## 0:00–0:25 — Opening
Hello. My project is titled **Intelligent Academic Assistant for Document-Based Question Answering**. The goal is to make it easier to query academic PDF documents using natural language and retrieve supporting passages.

## 0:25–1:15 — Problem
Academic papers and study material can be lengthy. Searching page-by-page takes time, and keyword search may not locate relevant information when the wording of a question differs from the text. This project explores semantic retrieval combined with a local language model to make document exploration more conversational.

## 1:15–1:55 — Objectives
The objectives are to extract PDF text while retaining page metadata, divide text into chunks, embed those chunks, retrieve relevant passages for a question, generate a concise answer based on retrieved context, and display source filenames and pages.

## 1:55–2:50 — Architecture
The system starts with PDF uploads in a Streamlit interface. PyMuPDF extracts text page-by-page. The text is split into overlapping character chunks. Sentence Transformers converts each chunk into a vector embedding. When the user asks a question, the same model encodes the question and ranks chunks by similarity. The selected passages are sent to Ollama, which runs a language model locally. The generated answer and source-page information are shown in the interface.

## 2:50–3:45 — Technologies
The implementation uses Python and Streamlit for the user interface, PyMuPDF for PDF text extraction, Sentence Transformers for semantic embeddings, NumPy for similarity calculations, Requests for HTTP communication, and Ollama for local generation. The default model configuration is llama3.2, but the UI allows model name and server URL to be changed.

## 3:45–6:15 — Demonstration
[SCREEN: open the app]
First, I open the Academic Assistant. I upload a text-based PDF and wait while the application extracts pages, creates chunks, and computes embeddings.
[SCREEN: upload actual PDF and show indexing]
Now I ask a question whose answer is present in the document.
[SCREEN: enter real answerable question]
The system retrieves relevant passages and generates a response. I can expand the sources section to see the filename and page numbers associated with retrieved passages.
[SCREEN: expand sources, compare to actual PDF page]
Next, I ask a question that is not answered in the uploaded document.
[SCREEN: enter unanswerable question]
The system is instructed to say when the retrieved context does not contain the answer. Show the actual behavior; if it generates unsupported text, note this as a limitation rather than claiming a perfect refusal.
[OPTIONAL SCREEN: Ollama unavailable error after stopping service, only if safe and practical]

## 6:15–7:10 — Testing
I tested or will document the following cases: text extraction, multiple PDFs, an answerable question, an unanswerable question, source metadata, and an unavailable Ollama service. [Replace this with actual test outcomes.] Evaluation should include answer correctness, retrieval relevance, response time, and unsupported claims. No accuracy figure is claimed without a measured test set.

## 7:10–8:00 — Limitations and Future Work
This version supports text-based PDFs but does not include OCR for scanned files. Chunking is character-based and may split sentences. It uses basic similarity retrieval without reranking or persistent vector storage. Future work includes OCR, improved chunking, a vector database, reranking, and formal evaluation.

## 8:00–8:30 — Conclusion
The project demonstrates a local retrieval-augmented document assistant that connects PDF extraction, semantic retrieval, and language-model generation. It provides a base for building more accurate and thoroughly evaluated academic assistants. Thank you.

## Recording checklist
- [ ] App and Ollama running before recording
- [ ] PDFs selected and demo questions prepared
- [ ] Hide personal files and notifications
- [ ] Show answer and source pages clearly
- [ ] Record at 1080p if available
- [ ] Keep narration concise and total video under 10 minutes
- [ ] Add actual screenshots / screen recording, not mock results
