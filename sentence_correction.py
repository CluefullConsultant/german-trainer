import re
import json
import streamlit as st
import anthropic


_PROMPT = """Der folgende Text wurde von einem Deutschlernenden auf C1-Zielniveau geschrieben. Er darf informell sein, unvollstaendige Saetze oder Umgangssprache enthalten - das ist so gewollt und ist KEIN Fehler. Korrigiere NUR echte Fehler: Grammatik, Kasus, Wortstellung (z.B. weil/dass mit Verb am Satzende), Verbkonjugation, Genus, Praepositionen, Rechtschreibung.

Text: "{text}"

Antworte NUR mit JSON in diesem Format:
{{
  "corrected": "der vollstaendige korrigierte Text, gleicher Ton und gleiche Umgangssprachlichkeit wie das Original",
  "mistakes": [
    {{"original": "die fehlerhafte Stelle", "correction": "die korrigierte Stelle", "reason": "kurzer Grund auf Deutsch, nur bei nicht offensichtlichen Fehlern, sonst leerer String"}}
  ]
}}
Wenn der Text schon fehlerfrei ist, setze "corrected" identisch zum Original und "mistakes" als leere Liste."""


def correct_sentences(text: str) -> dict:
    """Correct free-form German text (informal register allowed) and list each mistake made."""
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": _PROMPT.format(text=text)}]
    )
    raw = response.content[0].text
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    if match:
        data = json.loads(match.group())
        return {
            "corrected": data.get("corrected", text),
            "mistakes": data.get("mistakes", []),
        }
    return {"corrected": text, "mistakes": []}
