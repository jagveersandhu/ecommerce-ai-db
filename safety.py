FORBIDDEN = [
    "insert",
    "update",
    "delete",
    "drop",
    "truncate",
    "alter",
    "create"
]

def is_safe(question: str) -> bool:
    q = question.lower()
    return not any(word in q for word in FORBIDDEN)
