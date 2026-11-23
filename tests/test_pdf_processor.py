from pdf_processor import chunk_pages

def test_chunking_preserves_page_metadata():
    pages = [{"file": "paper.pdf", "page": 3, "text": "abcdefghij"}]
    chunks = chunk_pages(pages, chunk_size=5, overlap=2)
    assert [c["text"] for c in chunks] == ["abcde", "defgh", "ij"]
    assert all(c["file"] == "paper.pdf" and c["page"] == 3 for c in chunks)

def test_chunking_empty_text():
    assert chunk_pages([], chunk_size=10, overlap=2) == []
