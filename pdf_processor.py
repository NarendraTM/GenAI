import fitz
from typing import List, Dict

def extract_pdf_pages(pdf_bytes: bytes, filename: str) -> List[Dict]:
    """Extract text page-by-page, retaining filename and page number metadata."""
    pages = []
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for index, page in enumerate(doc, start=1):
            text = page.get_text("text").strip()
            if text:
                pages.append({"file": filename, "page": index, "text": text})
    return pages

def chunk_pages(pages: List[Dict], chunk_size: int = 1000, overlap: int = 150) -> List[Dict]:
    """Split page text into overlapping character chunks, preserving page metadata."""
    chunks = []
    chunk_size = max(1, chunk_size)
    overlap = min(max(0, overlap), chunk_size - 1)
    step = chunk_size - overlap
    for page in pages:
        text = page["text"]
        for start in range(0, len(text), step):
            piece = text[start:start + chunk_size].strip()
            if piece:
                chunks.append({"file": page["file"], "page": page["page"], "text": piece, "chunk_id": len(chunks)})
            if start + chunk_size >= len(text):
                break
    return chunks
