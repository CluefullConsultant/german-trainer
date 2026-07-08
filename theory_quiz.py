# theory_quiz.py
import re
import json
import streamlit as st
import anthropic


def _client():
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    return anthropic.Anthropic(api_key=api_key)


def _parse_json_array(raw: str) -> list:
    match = re.search(r'\[.*\]', raw, re.DOTALL)
    if not match:
        return []
    return json.loads(match.group())


def generate_more_examples(title: str, explanation: str, level: str) -> list[dict]:
    """4 fresh example sentences for this exact rule, different vocabulary/context each call."""
    prompt = f"""Grammatikregel: "{title}" (Niveau {level})

Regelerklärung:
{explanation}

Erstelle 4 NEUE Beispielsätze, die genau diese Regel zeigen - jeder Satz mit anderem Wortschatz/Kontext (beruflich, alltäglich, gemischt), damit das Muster durch Wiederholung mit Variation sitzt. Nicht die Beispiele aus der Erklärung wiederholen.

Antworte NUR mit JSON:
[{{"label": "Kurzer Kontext-Titel", "sentence": "Beispielsatz mit **fettgedrucktem** Zielelement", "note": "Ein Satz Erklärung, warum das Beispiel die Regel zeigt"}}]"""

    response = _client().messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return _parse_json_array(response.content[0].text)


def generate_quiz(title: str, explanation: str, level: str) -> list[dict]:
    """5 fresh multiple-choice questions testing exactly this rule."""
    prompt = f"""Grammatikregel: "{title}" (Niveau {level})

Regelerklärung:
{explanation}

Erstelle einen kurzen Test mit 5 Multiple-Choice-Fragen, die GENAU diese Regel prüfen. Jede Frage ist entweder ein Lückensatz ("Ergänzen Sie: Er dankte ___ für die Hilfe.") oder eine direkte Auswahlfrage. Genau 4 Antwortoptionen pro Frage, nur eine richtig. Falsche Optionen sollen plausible Fehler zeigen (typische Verwechslungen bei dieser Regel), keine offensichtlich falschen.

Mische den Schwierigkeitsgrad bewusst - nicht alle 5 Fragen gleich schwer:
- 2 leichte Fragen: die Grundregel direkt und eindeutig angewendet
- 2 mittelschwere Fragen: etwas komplexerer Satzkontext oder eine häufige Verwechslung
- 1 schwere Frage: ein Grenzfall, eine Ausnahme, oder eine Stelle, wo die Regel mit einer ähnlichen Regel kollidiert

Antworte NUR mit JSON:
[{{"frage": "Fragetext oder Lückensatz", "optionen": ["Option A", "Option B", "Option C", "Option D"], "richtig_index": 0, "erklaerung": "Kurze Begründung, warum diese Antwort richtig ist", "schwierigkeit": "leicht|mittel|schwer"}}]"""

    response = _client().messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return _parse_json_array(response.content[0].text)
