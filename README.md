# Intelligent Academic Assistant for Document-Based Question Answering

A local Retrieval-Augmented Generation (RAG) prototype that lets users upload academic PDF documents, ask questions in natural language, retrieve semantically relevant passages, and generate grounded answers using a local Ollama model.

## Features
- Upload multiple PDFs
- Extract text page-by-page and preserve page metadata
- Overlapping text chunking
- Local semantic embeddings with Sentence Transformers
- Similarity-based Top-K retrieval
- Local LLM answer generation with Ollama
- Retrieved filename/page references displayed in the UI
- Streamlit chat interface

## Architecture
PDF upload → PyMuPDF text extraction → overlapping chunks → Sentence Transformers embeddings → query embedding → similarity ranking → Top-K context → Ollama generation → answer with retrieved source references.

## Requirements
- Python 3.10+
- Ollama installed
- Local model (example: `llama3.2`)

## Quick start (Windows PowerShell)
```powershell
ollama pull llama3.2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Linux/macOS
```bash
ollama pull llama3.2
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open the Streamlit page, upload PDF(s), wait for indexing, and ask questions.

## Project files
- `app.py`: Streamlit interface and session state
- `pdf_processor.py`: PDF extraction and text chunking
- `retrieval.py`: embeddings and similarity retrieval
- `ollama_client.py`: Ollama availability and chat request
- `requirements.txt`: dependencies
- `docs/`: report, presentation outline, and video script
- `tests/`: basic processing tests

## Important limitations
- Scanned PDFs/image-only pages are not OCR processed.
- Retrieved passages are shown as evidence, but citation display does not guarantee every answer claim is supported.
- First embedding-model run may download model files.
- Performance depends on local CPU/GPU and selected Ollama model.
- Evaluation results should be measured by the project team; no benchmark numbers are claimed here.

## Academic deliverable status
The documentation is a reproducible implementation description and draft submission package. Replace the placeholders in the report and presentation with student/faculty details and actual screenshots, testing observations, and measured results before final submission.
