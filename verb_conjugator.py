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
    "perfekt": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."},
    "futur1": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."},
    "futur2": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."}
  },
  "konjunktiv2": {
    "praeteritum": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."},
    "plusquamperfekt": {"ich": "...", "du": "...", "er_sie_es": "...", "wir": "...", "ihr": "...", "sie_Sie": "..."}
  },
  "imperativ": {"du": "...", "ihr": "...", "Sie": "...", "hat_imperativ": true},
  "partizip_praesens": "..."
}"""


def generate_full_conjugation(verb: str) -> dict:
    """Full paradigm for one verb: all persons, across Indikativ (6 Zeiten), Konjunktiv I (Präsens/Perfekt/Futur I+II),
    Konjunktiv II (Präteritum/Plusquamperfekt), Imperativ, Partizip Präsens/Perfekt - mirrors the standard
    Flexionstabelle format (e.g. LEO)."""
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""Gib die vollständige Konjugation des deutschen Verbs "{verb}" an - grammatikalisch exakt korrekt, keine Fantasieformen, im Stil einer klassischen Flexionstabelle (wie bei LEO).

Wichtige Regeln:
- Konjunktiv II (Präteritum/Plusquamperfekt) basiert auf dem Präteritum-Stamm, NICHT auf dem Präsens-Stamm. Benutze die würde-Form nur, wenn die synthetische Form im Neuhochdeutschen ungebräuchlich/veraltet wirkt; bei sein/haben/werden/Modalverben und einigen häufigen starken Verben ist die synthetische Form Standard (z.B. 'wäre', 'hätte', 'könnte', 'käme', 'ginge').
- Konjunktiv I/II Futur I und Futur II: gib die Konjunktiv-I-Form an (werde/werdest/werde/werden/werdet/werden + Infinitiv bzw. + Partizip II + haben/sein); falls Konjunktiv I mit dem Indikativ identisch wäre, ist das in Ordnung, das ist normal (siehe Regel Konjunktiv I in indirekter Rede).
- Imperativ: nicht jedes Verb hat einen Imperativ (z.B. Modalverben wie können/müssen/wollen/dürfen/sollen/mögen, oder sein-Zustandsverben wie 'wissen' nur eingeschränkt). Setze "hat_imperativ": false und lasse du/ihr/Sie leer ("-"), wenn das Verb keinen gebräuchlichen Imperativ hat.
- partizip_praesens: Infinitiv + d (z.B. arbeitend, lachend). Wenn ein Verb (wie manche Modalverben oder Zustandsverben) praktisch nie im Partizip Präsens vorkommt, trotzdem die grammatisch mögliche Form angeben.

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

# Kuratierte Liste der wichtigsten/häufigsten deutschen Verben fuer die Schnellauswahl.
WICHTIGE_VERBEN = [
    "sein", "haben", "werden", "können", "müssen", "wollen", "sollen", "dürfen", "mögen",
    "gehen", "kommen", "machen", "sagen", "geben", "sehen", "wissen", "nehmen", "finden",
    "bleiben", "sprechen", "arbeiten", "denken", "bringen", "fahren",
]
