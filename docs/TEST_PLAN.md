# Test Plan

| ID | Test | Procedure | Expected result | Actual result |
|---|---|---|---|---|
| T01 | Text extraction | Upload selectable-text PDF | Page text is extracted | To be filled |
| T02 | Multiple PDFs | Upload two PDFs | Both filenames appear in indexed details | To be filled |
| T03 | Answerable QA | Ask a question answered by source | Relevant context retrieved and answer generated | To be filled |
| T04 | Unanswerable QA | Ask question absent from source | Assistant should acknowledge missing context; inspect for hallucination | To be filled |
| T05 | Page metadata | Inspect sources panel | Filename and page number shown | To be filled |
| T06 | Service offline | Stop Ollama and ask question | UI reports service unavailable/error | To be filled |
| T07 | Scanned PDF | Upload image-only PDF | Empty extraction handled with OCR limitation message | To be filled |

Record computer specifications, model, PDF dataset (with permission), latency, correctness judgments, and retrieval relevance. This table is intentionally unfilled until tests are performed.
