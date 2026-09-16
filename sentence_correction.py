import streamlit as st
import anthropic


_PROMPT = """Der folgende Text wurde von einem Deutschlernenden auf C1-Zielniveau geschrieben. Er darf informell sein, unvollstaendige Saetze oder Umgangssprache enthalten - das ist so gewollt und ist KEIN Fehler. Korrigiere NUR echte Fehler: Grammatik, Kasus, Wortstellung (z.B. weil/dass mit Verb am Satzende), Verbkonjugation, Genus, Praepositionen, Rechtschreibung.

Text: "{text}"

Antworte in GENAU diesem Format, ohne JSON, ohne Markdown-Codeblock, ohne Einleitung:
KORRIGIERT:
<der vollstaendige korrigierte Text, gleicher Ton und gleiche Umgangssprachlichkeit wie das Original>
FEHLER:
<fehlerhafte Stelle> ||| <korrigierte Stelle> ||| <kurzer Grund auf Deutsch, nur bei nicht offensichtlichen Fehlern, sonst leer>
(eine Zeile pro Fehler. Wenn der Text schon fehlerfrei ist, schreibe nach FEHLER: nur das Wort KEINE)"""


def stream_correction(text: str):
    """Yields raw text chunks as Claude generates the correction, for a live-typing display.
    Call parse_correction_response() on the fully accumulated chunks once streaming ends."""
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)
    with client.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=1536,
        messages=[{"role": "user", "content": _PROMPT.format(text=text)}],
    ) as stream:
        for chunk in stream.text_stream:
            yield chunk


def parse_correction_response(raw: str, original_text: str) -> dict:
    """Split the plain-text KORRIGIERT:/FEHLER: response into a corrected string and a mistake list."""
    after_marker = raw.split("KORRIGIERT:", 1)[-1]
    if "FEHLER:" in after_marker:
        corrected_part, fehler_part = after_marker.split("FEHLER:", 1)
    else:
        corrected_part, fehler_part = after_marker, ""

    corrected = corrected_part.strip() or original_text

    mistakes = []
    for line in fehler_part.strip().splitlines():
        line = line.strip()
        if not line or line.upper() == "KEINE":
            continue
        parts = [p.strip() for p in line.split("|||")]
        if len(parts) >= 2 and parts[0] != parts[1]:
            mistakes.append({
                "original": parts[0],
                "correction": parts[1],
                "reason": parts[2] if len(parts) > 2 else "",
            })

    return {"corrected": corrected, "mistakes": mistakes}
