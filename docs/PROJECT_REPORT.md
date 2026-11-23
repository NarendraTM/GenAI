# Project Report: Intelligent Academic Assistant for Document-Based Question Answering

> **Submission draft:** Replace bracketed placeholders and add screenshots, actual experiment results, and supervisor/institution details before submission. This report describes the repository implementation and does not claim unmeasured performance.

## Cover details
- Project title: Intelligent Academic Assistant for Document-Based Question Answering
- Student: [Student name / ID]
- Institution / department: [Institution]
- Guide: [Faculty guide]
- Academic year: [Year]

## Abstract
Students and researchers often need to search lengthy academic PDFs to locate specific concepts, definitions, and explanations. This project implements a local document-question-answering prototype that combines PDF text extraction, semantic retrieval, and a locally hosted language model. Users upload PDF documents through a Streamlit interface. Text is extracted page-by-page, split into overlapping chunks, embedded using Sentence Transformers, and ranked against a question by vector similarity. The highest-ranked passages are provided to an Ollama-served language model, which is instructed to answer from the supplied context and acknowledge when the context is insufficient. The interface displays retrieved source filenames and page numbers. This prototype demonstrates a retrieval-augmented generation workflow; evaluation and limitations are discussed without inventing benchmark results.

## Chapter 1 — Introduction
Academic materials may contain hundreds of pages. Keyword searches can miss relevant passages when the wording differs from a question, and manually locating evidence can be time-consuming. A document-focused assistant can reduce navigation effort by retrieving passages semantically and presenting a natural-language answer along with the location of retrieved evidence.

### Problem statement
Develop a simple, locally runnable application that accepts academic PDFs, retrieves text passages relevant to user questions, and generates concise answers grounded in those passages.

### Objectives
1. Extract text from PDF files and retain page metadata.
2. Divide extracted text into manageable overlapping chunks.
3. Generate vector embeddings locally.
4. Retrieve the most semantically relevant chunks for a query.
5. Generate a context-grounded response using a local LLM.
6. Present answers and source filenames/page numbers in a web UI.

### Scope
Text-based PDFs are supported. OCR for scanned documents, external database ingestion, multi-user accounts, and production-scale indexing are outside this prototype scope.

## Chapter 2 — Background and Related Concepts
- **PDF extraction:** Text extraction libraries can read embedded text and page structure.
- **Chunking:** Dividing long text helps fit context windows and gives retrieval smaller units.
- **Embeddings:** Sentence embeddings encode text into vectors to represent semantic similarity.
- **Vector retrieval:** Similarity scoring ranks chunks by closeness to a query vector.
- **RAG:** Retrieved text is supplied to a language model at answer time to improve grounding and reduce reliance on model memory.

## Chapter 3 — System Design
### Architecture
PDF upload → page text extraction → overlapping chunk creation → chunk embedding → query embedding → similarity ranking → Top-K passage selection → local LLM prompt → answer and source display.

### Components
- **Frontend:** Streamlit upload, settings, chat, and source display.
- **PDF processor:** PyMuPDF extraction and character-based chunking.
- **Embedding module:** Sentence Transformers model `all-MiniLM-L6-v2`.
- **Retriever:** Dot-product ranking on normalized embeddings (equivalent to cosine similarity for normalized vectors).
- **Generator:** Ollama HTTP API with configurable model (default `llama3.2`).
- **Runtime:** Local Python process and local model server.

### Data flow
1. User selects PDF file(s).
2. Each page's text is extracted and tagged with filename/page number.
3. Page text is chunked with configurable size and overlap.
4. Embeddings are computed for chunks.
5. User asks a question; its embedding is computed.
6. Chunk scores are computed and Top-K chunks are selected.
7. Selected chunk text and source metadata are sent to the Ollama chat API.
8. The response is displayed; retrieved source page metadata is available in the interface.

## Chapter 4 — Implementation
### Technology stack
Python, Streamlit, PyMuPDF, Sentence Transformers, NumPy, Requests, Ollama.

### File responsibilities
- `app.py`: Streamlit UI, upload flow, session state, chat, settings, and indexing.
- `pdf_processor.py`: `extract_pdf_pages` and `chunk_pages`.
- `retrieval.py`: cached embedding-model load, chunk embeddings, semantic retrieval.
- `ollama_client.py`: endpoint health check and chat API call.
- `requirements.txt`: Python dependencies.

### Chunking
Chunk size and overlap are configurable. For each page, chunks are created by advancing the start position by `chunk_size - overlap`. Each chunk retains its source file, page, and chunk identifier. This implementation uses character-based chunking rather than token-aware or sentence-aware chunking.

### Retrieval
The model `sentence-transformers/all-MiniLM-L6-v2` encodes chunks and questions. Embeddings are normalized, and dot product scores rank chunks. The UI exposes Top-K selection.

### Generation
The application builds a context string containing source labels and retrieved text. The system instruction asks the LLM to use only that context, avoid inventing facts, and report when the context does not answer the question. Requests are sent to Ollama's local `/api/chat` endpoint with temperature 0.2.

## Chapter 5 — Setup and Execution
1. Install Python 3.10+.
2. Install Ollama and start its service.
3. Pull a model, for example `ollama pull llama3.2`.
4. Create a virtual environment.
5. Install dependencies with `pip install -r requirements.txt`.
6. Start the application with `streamlit run app.py`.
7. Open the local Streamlit page, upload PDFs, and ask questions.

See the root README for commands for Windows, Linux, and macOS.

## Chapter 6 — Testing and Evaluation
### Proposed test cases
| Test | Input | Expected observation |
|---|---|---|
| Text PDF upload | PDF with selectable text | Text chunks are indexed |
| Multiple PDFs | Two or more text PDFs | Chunks include each filename |
| Answerable query | Question whose answer appears in source | Relevant passages are retrieved; answer should reflect context |
| Unanswerable query | Question absent from source | Model should state insufficient document evidence |
| Source metadata | Query with useful retrieved passage | Source filename/page shown |
| Ollama unavailable | Stop model service | UI reports unavailable/error |
| Scanned PDF | Image-only PDF | No text extracted; app reports OCR is not included |

### Results
**Actual measurements to be entered after running the tests.** Record test outcome, relevant retrieval passage, response correctness, latency, and hardware/model details. Do not insert fabricated accuracy or timing values.

Recommended metrics:
- Answer correctness judged against document ground truth
- Retrieval relevance (e.g., relevant chunks among Top-K)
- Unsupported-claim rate / faithfulness review
- Average response latency
- Behavior on unanswerable questions

## Chapter 7 — Discussion
The local workflow can reduce the effort needed to locate passages in academic PDFs. Semantic retrieval is useful when question wording differs from document phrasing. Source metadata improves traceability, but the retrieved list is not a formal citation validation system. LLM output may still contain unsupported statements, so answers should be checked against original pages.

## Chapter 8 — Limitations and Future Work
### Limitations
- OCR is not implemented for scanned PDFs.
- Chunk boundaries are character-based and may split sentences.
- Similarity retrieval is a simple vector ranking approach.
- No reranker, persistent vector database, or token-aware chunking.
- Retrieved source display does not ensure every answer claim is supported.
- Model speed and output quality depend on the chosen local model and hardware.
- No systematic benchmark has been conducted in this draft.

### Future enhancements
OCR integration, sentence/token-aware chunking, persistent vector store, reranking, richer citations, document management, multi-document filtering, answer-quality evaluation, and optional streaming generation.

## Chapter 9 — Conclusion
This project implements an accessible local RAG prototype for academic PDF question answering. It demonstrates extraction, chunking, embedding, retrieval, and generation within a simple interface. The implementation is a foundation for further evaluation and improvements in accuracy, usability, and citation fidelity.

## References
1. Streamlit documentation: https://docs.streamlit.io/
2. PyMuPDF documentation: https://pymupdf.readthedocs.io/
3. Sentence Transformers documentation: https://www.sbert.net/
4. NumPy documentation: https://numpy.org/doc/
5. Ollama documentation: https://ollama.com/
6. Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020), arXiv: https://arxiv.org/abs/2005.11401

## Appendix A — Run checklist
- [ ] Student/institution/faculty details filled in
- [ ] App installed and launched
- [ ] Sample PDFs prepared (use lawful documents)
- [ ] Screenshots captured from actual app
- [ ] Tests run and results recorded
- [ ] Limitations acknowledged
- [ ] Report proofread and formatted for faculty template
