import re
import json
import streamlit as st
import anthropic

TOPICS = [
    "Konnektoren",
    "Zweiteilige Konnektoren (nicht nur...sondern auch, sowohl...als auch)",
    "Deklination (Nominativ/Akkusativ/Dativ/Genitiv)",
    "Verben mit Kasus (Verben + Dativ/Akkusativ/Genitiv)",
    "Reflexive Verben (sich-Verben)",
    "Konjunktiv II",
    "Passiv",
    "Relativsätze",
    "Partizipialkonstruktionen",
    "Wortstellung",
    "Trennbare Verben",
    "Wechselpräpositionen",
    "Genitiv-Präpositionen",
    "Modalpartikeln (doch, mal, ja, eigentlich)",
    "Indirekte Rede",
    "Schriftlicher Ausdruck (Brief)",
    "Leseverstehen",
    "Hörverstehen",
    "Sprechaufgabe",
    "Wortschatz in Kontext",
    "Eigenes Thema",
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
    "Zweiteilige Konnektoren (nicht nur...sondern auch, sowohl...als auch)": ["Lückentext", "Satztransformation", "Fehlersuche", "Kategoriensortierung"],
    "Verben mit Kasus (Verben + Dativ/Akkusativ/Genitiv)": ["Lückentext", "Mehrfachauswahl", "Fehlersuche", "Satztransformation"],
    "Reflexive Verben (sich-Verben)": ["Lückentext", "Mehrfachauswahl", "Fehlersuche", "Satztransformation"],
    "Modalpartikeln (doch, mal, ja, eigentlich)": ["Lückentext", "Mehrfachauswahl", "Übersetzung", "Fehlersuche"],
    "Indirekte Rede": ["Satztransformation", "Lückentext", "Fehlersuche"],
    "Eigenes Thema": ["Lückentext", "Mehrfachauswahl", "Satztransformation", "Fehlersuche", "Übersetzung", "Sprechaufgabe", "Brief schreiben"],
}

_SYSTEM_PROMPT = """Du bist ein erfahrener Deutschlehrer, der Ubungsaufgaben fur einen Lernenden auf B2/C1-Niveau erstellt.

WICHTIG: Jede Aufgabe muss eine glasklare Aufgabenanweisung auf Deutsch enthalten - so formuliert, dass ein Lernender ohne weitere Erklarung sofort weiss, was er tun soll. Beispiele guter Anweisungen:
- "Ergänzen Sie den richtigen Artikel (der/die/das/dem/den/des)."
- "Verbinden Sie die zwei Satze mit dem passenden Konnektor."
- "Finden Sie den Fehler im Satz und schreiben Sie die richtige Version."
- "Übersetzen Sie die Satze ins Deutsche."
- "Wählen Sie die richtige Antwort."

Schlechte Anweisungen (NICHT verwenden):
- Grammatikjargon ohne Erklarung ("Genitiv maskulin temporal")
- Zu kurze Anweisungen ohne konkretes Beispiel was zu tun ist

Antworte NUR mit einem gultig formatierten JSON-Objekt - kein Markdown, kein erklarender Text davor oder danach.
Die Aufgabe muss pedagogisch korrekt und auf C1-Niveau sein."""

_TYPE_SCHEMAS = {
    "Lückentext": """Ausgabeformat:
{"instruction": "Klare Aufgabenstellung fur den Lernenden, z.B. 'Ergänzen Sie den richtigen Artikel.' oder 'Setzen Sie das Verb in der richtigen Form ein.'", "text_with_blanks": "Satz mit ___ fur jede Lucke", "blanks": [{"position": 0, "answer": "Antwort", "hint": "kurzer Hinweis"}], "explanation": "Grammatikerklarung"}
Erstelle 5-8 Lucken im Text. Das Feld 'instruction' muss immer ausgefullt sein.""",

    "Mehrfachauswahl": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Wählen Sie die richtige Antwort (a, b, c oder d).'", "items": [{"question": "Frage", "options": ["Option A", "Option B", "Option C", "Option D"], "correct_index": 0, "explanation": "Grammatikerklarung"}]}
Erstelle 5 Fragen.""",

    "Satztransformation": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Verbinden Sie die zwei Satze zu einem Satz. Benutzen Sie den angegebenen Konnektor.'", "items": [{"instruction": "Konnektor oder Hinweis fur diese Aufgabe", "sentences": ["Satz 1.", "Satz 2."], "answer": "Kombinierter Satz", "explanation": "Erklarung"}]}
Erstelle 5 Transformationsaufgaben.""",

    "Fehlersuche": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Lesen Sie jeden Satz. Enthält er einen Grammatikfehler? Wenn ja, schreiben Sie den korrekten Satz.'", "sentences": [{"text": "Satz mit oder ohne Fehler", "has_error": true, "correction": "Korrektur oder null", "rule": "Regelname oder null"}]}
Erstelle 8 Satze, davon 5 mit Fehlern und 3 ohne Fehler (gemischt).""",

    "Übersetzung": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Übersetzen Sie die folgenden Satze vom Englischen ins Deutsche.'", "direction": "EN-DE", "items": [{"source": "Englischer Satz", "answer": "Deutscher Satz", "explanation": "Grammatikhinweis"}]}
Erstelle 5 Ubersetzungsaufgaben.""",

    "Kategoriensortierung": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Ordnen Sie die Konnektoren in die richtige Kategorie ein (A, B oder C).'", "words": ["Wort1", "Wort2"], "categories": {"Kategoriename": ["Wort1"]}, "explanation": "Erklarung des Systems"}
Verwende mindestens 10 Worter auf mindestens 3 Kategorien verteilt.""",

    "Brief schreiben": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Schreiben Sie einen formellen Brief (ca. 200 Wörter). Gehen Sie auf alle vier Punkte ein.'", "prompt": "Aufgabenstellung mit Kontext", "reihenpunkte": ["Punkt 1", "Punkt 2", "Punkt 3"], "time_limit_minutes": 30, "register": "formell"}
Erstelle einen realistischen Telc-Stil Briefschreibauftrag.""",

    "Leseverstehen": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Lesen Sie den Text und beantworten Sie die Fragen in vollständigen Satzen.'", "text": "...vollstandiger deutscher Text...", "is_hoerverstehen": false, "questions": [{"question": "Frage", "answer": "Antwort"}]}
Der Text muss mindestens 300 Worter haben. Erstelle 5 Verstandnisfragen auf C1-Niveau. Falls der Mentor einen Text bereitgestellt hat, verwende diesen.""",

    "Hörverstehen": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Hören Sie dem Text zu und beantworten Sie die Fragen.'", "text": "...Text der laut vorgelesen wird...", "is_hoerverstehen": true, "questions": [{"question": "Frage", "answer": "Antwort"}]}
Der Text muss 150-250 Worter haben (ca. 1-2 Minuten Lesezeit). Erstelle 5 Fragen. Falls der Mentor einen Text bereitgestellt hat, verwende diesen.""",

    "Sprechaufgabe": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Sprechen Sie 2-3 Minuten über das folgende Thema. Benutzen Sie die Hinweise als Hilfe.'", "prompt": "Sprechanlass", "hints": ["Hinweis 1", "Hinweis 2", "Hinweis 3"]}
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
