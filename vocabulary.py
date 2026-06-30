import re
import json
import streamlit as st
import anthropic

_SYSTEM_PROMPT = """Du bist ein Deutschlehrer. Extrahiere 3-5 wichtige Vokabeln aus dem gegebenen Ubungstext.
Gib nur Vokabeln zuruck, die fur B2/C1-Niveau relevant sind.
Antworte NUR mit einem JSON-Array:
[{"word": "Wort", "definition": "Deutsche Definition/Erklarung", "example": "Beispielsatz aus dem Text"}]"""


def _parse_vocab_response(raw: str) -> list[dict]:
    match = re.search(r'\[.*\]', raw, re.DOTALL)
    if not match:
        return []
    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return []


def extract_vocabulary(exercise_content: dict, exercise_type: str) -> list[dict]:
    # Skip types with no meaningful text to extract vocabulary from
    if exercise_type in ("Sprechaufgabe", "Brief schreiben", "Kategoriensortierung"):
        return []

    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)

    content_text = json.dumps(exercise_content, ensure_ascii=False)

    raw = ""
    with client.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=512,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"Ubungsinhalt:\n{content_text}"}]
    ) as stream:
        for text in stream.text_stream:
            raw += text

    return _parse_vocab_response(raw)
