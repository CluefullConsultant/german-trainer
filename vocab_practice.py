import streamlit as st
import anthropic
import re
import json


def check_sentence(word: str, definition: str, user_sentence: str) -> dict:
    """Claude checks if user sentence uses the word correctly. Returns {correct: bool, feedback: str}"""
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""Das Wort: "{word}"
Definition: "{definition}"
Satz des Lernenden: "{user_sentence}"

Ist das Wort korrekt und natuerlich im Satz verwendet? Antworte NUR mit JSON:
{{"correct": true/false, "feedback": "Kurzes, direktes Feedback auf Deutsch. Max 2 Saetze. Bei Fehler: zeige die korrekte Version."}}"""

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.content[0].text
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    if match:
        return json.loads(match.group())
    return {"correct": False, "feedback": "Fehler beim Auswerten."}
