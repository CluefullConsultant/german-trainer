import re
import json
import streamlit as st
import anthropic

TOPICS = [
    "Konnektoren",
    "Deklination (Nominativ/Akkusativ/Dativ/Genitiv)",
    "Konjunktiv II",
    "Passiv",
    "Relativsätze",
    "Partizipialkonstruktionen",
    "Wortstellung",
    "Trennbare Verben",
    "Wechselpräpositionen",
    "Genitiv-Präpositionen",
    "Schriftlicher Ausdruck (Brief)",
    "Leseverstehen",
    "Hörverstehen",
    "Sprechaufgabe",
    "Wortschatz in Kontext",
]

EXERCISE_TYPES = [
    "Lückentext",
    "Mehrfachauswahl",
    "Satztransformation",
    "Fehlersuche",
    "Übersetzung",
    "Kategoriensortierung",
    "Brief schreiben",
    "Leseverstehen",
    "Hörverstehen",
    "Sprechaufgabe",
]

EXERCISE_TYPES_FOR_TOPIC: dict[str, list[str]] = {
    "Konnektoren": ["Lückentext", "Mehrfachauswahl", "Satztransformation", "Fehlersuche", "Kategoriensortierung", "Übersetzung"],
    "Deklination (Nominativ/Akkusativ/Dativ/Genitiv)": ["Lückentext", "Mehrfachauswahl", "Fehlersuche", "Satztransformation"],
    "Konjunktiv II": ["Lückentext", "Satztransformation", "Fehlersuche", "Übersetzung"],
    "Passiv": ["Satztransformation", "Lückentext", "Fehlersuche", "Übersetzung"],
    "Relativsätze": ["Lückentext", "Satztransformation", "Fehlersuche"],
    "Partizipialkonstruktionen": ["Lückentext", "Satztransformation", "Fehlersuche"],
    "Wortstellung": ["Fehlersuche", "Satztransformation", "Lückentext"],
    "Trennbare Verben": ["Lückentext", "Satztransformation", "Fehlersuche", "Mehrfachauswahl"],
    "Wechselpräpositionen": ["Lückentext", "Mehrfachauswahl", "Fehlersuche", "Satztransformation"],
    "Genitiv-Präpositionen": ["Lückentext", "Mehrfachauswahl", "Fehlersuche"],
    "Schriftlicher Ausdruck (Brief)": ["Brief schreiben"],
    "Leseverstehen": ["Leseverstehen"],
    "Hörverstehen": ["Hörverstehen"],
    "Sprechaufgabe": ["Sprechaufgabe"],
    "Wortschatz in Kontext": ["Lückentext", "Mehrfachauswahl", "Übersetzung"],
}

_SYSTEM_PROMPT = """Du bist ein erfahrener Deutschlehrer, der Ubungsaufgaben fur einen Lernenden auf B2/C1-Niveau erstellt.
Erstelle immer klar strukturierte Aufgaben mit einem Losungsschlussel und einer Erklarung der Grammatikregel.
Antworte NUR mit einem gultig formatierten JSON-Objekt - kein Markdown, kein erklarender Text davor oder danach.
Die Aufgabe muss pedagogisch korrekt und auf C1-Niveau sein, darf aber grundlegende Grammatik (A1-C1) als Thema haben."""

_TYPE_SCHEMAS = {
    "Lückentext": """Ausgabeformat:
{"instruction": "Klare Aufgabenstellung fur den Lernenden, z.B. 'Ergänzen Sie den richtigen Artikel.' oder 'Setzen Sie das Verb in der richtigen Form ein.'", "text_with_blanks": "Satz mit ___ fur jede Lucke", "blanks": [{"position": 0, "answer": "Antwort", "hint": "kurzer Hinweis"}], "explanation": "Grammatikerklarung"}
Erstelle 5-8 Lucken im Text. Das Feld 'instruction' muss immer ausgefullt sein.""",

    "Mehrfachauswahl": """Ausgabeformat:
{"question": "Frage", "options": ["Option A", "Option B", "Option C", "Option D"], "correct_index": 0, "explanation": "Grammatikerklarung"}
Erstelle 5 Fragen als Array unter dem Schlussel "items": [...]""",

    "Satztransformation": """Ausgabeformat:
{"items": [{"instruction": "Anweisung", "sentences": ["Satz 1.", "Satz 2."], "answer": "Kombinierter Satz", "explanation": "Erklarung"}]}
Erstelle 5 Transformationsaufgaben.""",

    "Fehlersuche": """Ausgabeformat:
{"sentences": [{"text": "Satz mit oder ohne Fehler", "has_error": true, "correction": "Korrektur oder null", "rule": "Regelname oder null"}]}
Erstelle 8 Satze, davon 5 mit Fehlern und 3 ohne Fehler (gemischt).""",

    "Übersetzung": """Ausgabeformat:
{"direction": "EN-DE", "items": [{"source": "Englischer Satz", "answer": "Deutscher Satz", "explanation": "Grammatikhinweis"}]}
Erstelle 5 Ubersetzungsaufgaben.""",

    "Kategoriensortierung": """Ausgabeformat:
{"instruction": "Sortieranweisung", "words": ["Wort1", "Wort2"], "categories": {"Kategoriename": ["Wort1"]}, "explanation": "Erklarung des Systems"}
Verwende mindestens 10 Worter auf mindestens 3 Kategorien verteilt.""",

    "Brief schreiben": """Ausgabeformat:
{"prompt": "Aufgabenstellung", "reihenpunkte": ["Punkt 1", "Punkt 2", "Punkt 3"], "time_limit_minutes": 30, "register": "formell"}
Erstelle einen realistischen Telc-Stil Briefschreibauftrag.""",

    "Leseverstehen": """Ausgabeformat:
{"text": "...vollstandiger deutscher Text...", "is_hoerverstehen": false, "questions": [{"question": "Frage", "answer": "Antwort"}]}
Der Text muss mindestens 300 Worter haben. Erstelle 5 Verstandnisfragen auf C1-Niveau. Falls der Mentor einen Text bereitgestellt hat, verwende diesen.""",

    "Hörverstehen": """Ausgabeformat:
{"text": "...Text der laut vorgelesen wird...", "is_hoerverstehen": true, "questions": [{"question": "Frage", "answer": "Antwort"}]}
Der Text muss 150-250 Worter haben (ca. 1-2 Minuten Lesezeit). Erstelle 5 Fragen. Falls der Mentor einen Text bereitgestellt hat, verwende diesen.""",

    "Sprechaufgabe": """Ausgabeformat:
{"prompt": "Sprechanlass", "hints": ["Hinweis 1", "Hinweis 2", "Hinweis 3"]}
Der Sprechanlass soll eine realistische Diskussionssituation beschreiben.""",
}


def _parse_json(raw: str) -> dict:
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    if not match:
        raise ValueError(f"Keine JSON-Struktur gefunden in: {raw[:200]}")
    return json.loads(match.group())


def generate_exercise(topic: str, exercise_type: str, mentor_notes: str = "", pasted_text: str = "") -> dict:
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)

    schema = _TYPE_SCHEMAS.get(exercise_type, "")
    notes_section = f"\nZusatzliche Hinweise des Mentors: {mentor_notes}" if mentor_notes.strip() else ""
    text_section = f"\nBereitgestellter Text:\n{pasted_text}" if pasted_text.strip() else ""

    user_prompt = f"""Erstelle eine {exercise_type}-Aufgabe zum Thema: {topic}{notes_section}{text_section}

{schema}"""

    raw = ""
    with client.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    ) as stream:
        for text in stream.text_stream:
            raw += text

    return _parse_json(raw)
