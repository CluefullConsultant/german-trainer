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
    "Zuordnung",
    "Richtig/Falsch/Nicht im Text",
    "Wortbildung",
]

EXERCISE_TYPES_FOR_TOPIC: dict[str, list[str]] = {
    "Konnektoren": ["Lückentext", "Mehrfachauswahl", "Satztransformation", "Fehlersuche", "Kategoriensortierung", "Übersetzung", "Zuordnung"],
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
    "Leseverstehen": ["Leseverstehen", "Richtig/Falsch/Nicht im Text", "Zuordnung"],
    "Hörverstehen": ["Hörverstehen", "Richtig/Falsch/Nicht im Text"],
    "Sprechaufgabe": ["Sprechaufgabe"],
    "Wortschatz in Kontext": ["Lückentext", "Mehrfachauswahl", "Übersetzung", "Zuordnung", "Wortbildung"],
    "Zweiteilige Konnektoren (nicht nur...sondern auch, sowohl...als auch)": ["Lückentext", "Satztransformation", "Fehlersuche", "Kategoriensortierung"],
    "Verben mit Kasus (Verben + Dativ/Akkusativ/Genitiv)": ["Lückentext", "Mehrfachauswahl", "Fehlersuche", "Satztransformation"],
    "Reflexive Verben (sich-Verben)": ["Lückentext", "Mehrfachauswahl", "Fehlersuche", "Satztransformation"],
    "Modalpartikeln (doch, mal, ja, eigentlich)": ["Lückentext", "Mehrfachauswahl", "Übersetzung", "Fehlersuche"],
    "Indirekte Rede": ["Satztransformation", "Lückentext", "Fehlersuche"],
    "Eigenes Thema": ["Lückentext", "Mehrfachauswahl", "Satztransformation", "Fehlersuche", "Übersetzung", "Sprechaufgabe", "Brief schreiben", "Zuordnung", "Richtig/Falsch/Nicht im Text", "Wortbildung"],
}

_SYSTEM_PROMPT = """Du bist ein erfahrener Deutschlehrer, der Ubungsaufgaben fur einen Lernenden auf C1-Niveau erstellt. Der Lernende ist ein professioneller Unternehmensberater, der Deutsch im Arbeitsalltag braucht: Geschafts-E-Mails, Besprechungen, Berichte, Prasentation von Daten, formelle Anfragen, Feedback geben und nehmen, Verhandlungen.

KONTEXT: Alle Aufgaben sollen in einem professionellen, geschaftlichen Umfeld angesiedelt sein. Typische Szenarien:
- Unternehmensberatung, Projektmanagement, Strategiemeetings
- Formelle und halbformelle Geschaftskorrespondenz (E-Mail, Bericht, Memo)
- Daten prasentieren und kommentieren ("Die Umsatzzahlen zeigen...")
- Feedback geben und annehmen ("Ich schlage vor, dass...", "Es ware sinnvoll, wenn...")
- Besprechungen leiten oder daran teilnehmen
- Kunden- und Kollegenkommunikation auf C1-Niveau

WICHTIG: Jede Aufgabe muss eine glasklare Aufgabenanweisung auf Deutsch enthalten. Beispiele:
- "Ergänzen Sie die Lucken mit dem richtigen Konnektor."
- "Verbinden Sie die Satze zu einem formellen Geschaftssatz."
- "Finden Sie den Grammatikfehler und schreiben Sie den korrekten Satz."
- "Übersetzen Sie die E-Mail-Abschnitte ins Deutsche."
- "Wählen Sie die richtige Antwort."

Schlechte Themen (NICHT verwenden): Urlaub buchen, Einkaufen, Wetter, Freizeit, Kochen.
Gute Themen: Quartalsbericht, Projektabschluss, Kundenprasentation, Teambesprechung, Stellungnahme, Angebotserstellung.

Antworte NUR mit einem gultig formatierten JSON-Objekt - kein Markdown, kein erklarender Text."""

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
Der Sprechanlass soll eine realistische berufliche Diskussionssituation beschreiben (z.B. Prasentieren von Projektergebnissen, Argumentieren fur eine Strategie).""",

    "Zuordnung": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Ordnen Sie jedem Begriff (1-6) die passende Definition (A-F) zu.'", "items": [{"id": "1", "text": "Begriff oder Satzanfang"}], "options": [{"id": "A", "text": "Definition oder Satzende"}], "pairs": {"1": "A"}, "explanation": "Erklarung der richtigen Zuordnungen"}
Erstelle 6 Begriffspaare aus dem beruflichen Kontext (z.B. Fachbegriffe und ihre Definitionen, Satzanfange und passende Fortfuhrungen, Situationen und angemessene Reaktionen).""",

    "Richtig/Falsch/Nicht im Text": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Lesen Sie den Text und entscheiden Sie: Ist die Aussage richtig (R), falsch (F) oder nicht im Text erwahnt (N)?'", "text": "...vollstandiger deutscher Geschaftstext (Bericht, E-Mail, Protokoll, mindestens 200 Worter)...", "statements": [{"statement": "Aussage uber den Text", "answer": "R", "explanation": "Warum richtig/falsch/nicht erwahnt"}]}
Erstelle 6 Aussagen: 2 richtig, 2 falsch, 2 nicht im Text. Der Text soll aus dem beruflichen Umfeld stammen (Bericht, Protokoll, Geschaftsbrief, interne Mitteilung).""",

    "Wortbildung": """Ausgabeformat:
{"instruction": "Glasklare Aufgabenanweisung, z.B. 'Bilden Sie aus dem angegebenen Wort die richtige Form und setzen Sie sie in die Lucke ein.'", "items": [{"sentence": "Satz mit Lucke (___)", "base_word": "Grundwort in Klammern", "answer": "abgeleitetes Wort", "word_class": "Nomen/Verb/Adjektiv/Adverb", "explanation": "Bildungsregel"}]}
Erstelle 6 Wortbildungsaufgaben aus dem beruflichen Wortschatz. Decke verschiedene Typen ab: Nomen aus Verben (die Entscheid___ von entscheiden), Adjektive aus Nomen (verantwort___ von Verantwortung), zusammengesetzte Nomen. Alle Satze sollen im Geschaftskontext stehen.""",
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
