# verb_conjugator.py
import re
import json
import streamlit as st
import anthropic

_SCHEMA = """Antworte NUR mit JSON in genau diesem Format (alle 6 Personen ausfüllen: ich, du, er_sie_es, wir, ihr, sie_Sie):
{
  "verb": "Infinitiv",
  "stammformen": {"infinitiv": "...", "praeteritum_3": "...", "partizip2": "...", "hilfsverb": "haben oder sein"},
  "indikativ": {
    "praesens": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."},
    "praeteritum": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."},
    "perfekt": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."},
    "plusquamperfekt": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."},
    "futur1": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."},
    "futur2": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."}
  },
  "konjunktiv1": {
    "praesens": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."},
    "perfekt": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."}
  },
  "konjunktiv2": {
    "praesens": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."},
    "perfekt": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."}
  },
  "imperativ": {"du": "...", "ihr": "...", "Sie": "..."}
}"""


def generate_full_conjugation(verb: str) -> dict:
    """Full paradigm for one verb: all persons, across Indikativ (6 Zeiten), Konjunktiv I/II (Präsens+Perfekt), Imperativ."""
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""Gib die vollständige Konjugation des deutschen Verbs "{verb}" an - grammatikalisch exakt korrekt, keine Fantasieformen. Bei Konjunktiv II im Präsens: benutze die würde-Form, außer bei sein/haben/Modalverben und den paar starken Verben, wo die synthetische Form üblich ist (z.B. 'wäre', 'hätte', 'könnte', 'käme', 'ginge').

{_SCHEMA}"""

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.content[0].text
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    if not match:
        return {}
    return json.loads(match.group())


PERSON_ORDER = ["ich", "du", "er_sie_es", "wir", "ihr", "sie_Sie"]
PERSON_LABELS = {"ich": "ich", "du": "du", "er_sie_es": "er/sie/es", "wir": "wir", "ihr": "ihr", "sie_Sie": "sie/Sie"}
