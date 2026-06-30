import re
import json
import streamlit as st
import anthropic

_SYSTEM_PROMPT = """Du bist ein strenger, prasizer Deutschlehrer.
Beurteile die Antwort des Lernenden und gib direktes, konkretes Feedback auf Deutsch.
Erklare jeden Fehler mit der genauen Grammatikregel die verletzt wurde.
Sei direkt - keine Lobhudelei fur falsche Antworten.
Antworte NUR mit einem JSON-Objekt: {"feedback": "Dein Feedback-Text", "error_tags": ["Themenname"]}
error_tags: Liste der Grammatikthemen bei denen Fehler gemacht wurden (leer wenn alles korrekt)."""


def _parse_feedback_response(raw: str) -> tuple[str, list[str]]:
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    if not match:
        return raw, []
    data = json.loads(match.group())
    return data.get("feedback", raw), data.get("error_tags", [])


def generate_feedback(exercise_content: dict, exercise_type: str, answer: dict) -> tuple[str, list[str]]:
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)

    user_prompt = f"""Aufgabentyp: {exercise_type}
Aufgabe:
{json.dumps(exercise_content, ensure_ascii=False, indent=2)}

Antwort des Lernenden:
{json.dumps(answer, ensure_ascii=False, indent=2)}

Beurteile die Antwort. Gib item-weises Feedback und benenne jeden Grammatikfehler genau."""

    raw = ""
    with client.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    ) as stream:
        for text in stream.text_stream:
            raw += text

    return _parse_feedback_response(raw)
