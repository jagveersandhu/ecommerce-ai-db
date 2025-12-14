import requests

API_BASE = "http://127.0.0.1:8000"

def ai_query(question: str):
    try:
        resp = requests.post(
            f"{API_BASE}/ai/query",
            json={"question": question},
            timeout=1000
        )
        resp.raise_for_status()
        return resp.json()["answer"]
    except requests.exceptions.RequestException as e:
        return f"API Error: {str(e)}"
