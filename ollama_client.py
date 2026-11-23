import requests

def ollama_available(base_url: str) -> bool:
    try:
        response = requests.get(base_url.rstrip("/") + "/api/tags", timeout=2)
        return response.ok
    except requests.RequestException:
        return False

def generate_answer(question, retrieved_chunks, base_url, model):
    context_parts = []
    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_parts.append(f"[Source {i}: {chunk['file']}, page {chunk['page']}]\n{chunk['text']}")
    context = "\n\n".join(context_parts)
    system_prompt = (
        "You are an academic document assistant. Answer using only the supplied context. "
        "If the context does not contain the answer, say you cannot find the answer in the uploaded documents. "
        "Do not invent facts. Explain clearly and concisely. When useful, mention source filename and page."
    )
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"DOCUMENT CONTEXT:\n{context}\n\nQUESTION:\n{question}"}
        ],
        "stream": False,
        "options": {"temperature": 0.2}
    }
    try:
        response = requests.post(base_url.rstrip("/") + "/api/chat", json=payload, timeout=180)
        response.raise_for_status()
        data = response.json()
        return data.get("message", {}).get("content", "The model returned an empty response.")
    except requests.RequestException as exc:
        return f"Error contacting Ollama: {exc}. Confirm Ollama is running and the model is downloaded."
