# Presentation Slide Plan — 10-minute cap

> Convert this outline to PowerPoint and add screenshots from the running implementation. Avoid claiming performance results until tests are run.

## Slide 1 — Title (20 sec)
**Intelligent Academic Assistant for Document-Based Question Answering**
Student: [Name / ID] • Guide: [Faculty] • [Institution]

## Slide 2 — Problem & Motivation (45 sec)
- Academic PDFs are lengthy and information-dense.
- Keyword search can be limited when question wording differs.
- Reading/searching page-by-page takes time.
- Goal: ask natural-language questions and find document evidence.

## Slide 3 — Objectives (40 sec)
- Extract text and preserve page metadata.
- Semantic chunking/retrieval workflow.
- Ground generation in retrieved passages.
- Show source file/page details.

## Slide 4 — Proposed Solution (60 sec)
Flow: PDF upload → text extraction → chunking → embeddings → similarity retrieval → local LLM → response with source pages.
Add architecture graphic.

## Slide 5 — Technologies (50 sec)
Python • Streamlit • PyMuPDF • Sentence Transformers (all-MiniLM-L6-v2) • NumPy • Ollama • llama3.2 (configurable)

## Slide 6 — Implementation (60 sec)
- PDF processor and overlapping chunks
- Embedding vectors for chunks and queries
- Top-K similarity retrieval
- Context prompt sent to local Ollama
- UI displays answer and source filename/page

## Slide 7 — Demo (2 min)
Show:
1. Launch app
2. Upload a real text PDF
3. Wait for indexing
4. Ask a question with an answer in the document
5. Expand source panel and open cited page in original PDF
6. Ask a question not covered by the document; show fallback behavior (verify actual behavior live)

## Slide 8 — Testing & Results (60 sec)
Insert actual test outcomes:
- PDF extraction test
- Answerable question
- Unanswerable question
- Source/page metadata
- Service-unavailable behavior
Include a small table or measured latency. Do not invent numbers.

## Slide 9 — Limitations & Future Work (45 sec)
Limitations: scanned PDF OCR absent, character-based chunks, no persistent vector DB or reranker, local hardware/model performance variability.
Future: OCR, token-aware chunking, persistent index, reranker, benchmark evaluation.

## Slide 10 — Conclusion (30 sec)
Prototype demonstrates local document QA using retrieval-augmented generation. Next step is systematic evaluation and usability improvements.

**Timing target:** 7–9 minutes, leaving margin below the 10-minute maximum.
