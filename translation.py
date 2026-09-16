import re
import json
import streamlit as st
import anthropic


_PROMPT = """Übersetze das folgende Wort oder die folgende Phrase zwischen Deutsch und Englisch. Erkenne automatisch die Ausgangssprache (Deutsch oder Englisch).

Text: "{text}"

Antworte NUR mit JSON in diesem Format:
{{
  "source_language": "Deutsch" oder "Englisch",
  "translation": "die Übersetzung",
  "word_type": "z.B. 'Nomen (die Herausforderung)' mit Artikel, 'Verb', 'Adjektiv' - nur bei Einzelwörtern, sonst leerer String",
  "example_source": "ein natürlicher Beispielsatz in der Ausgangssprache mit dem Wort/der Phrase",
  "example_target": "derselbe Satz in der Zielsprache"
}}"""


def translate(text: str) -> dict:
    """Translate a word or short phrase between German and English, auto-detecting direction."""
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=512,
        messages=[{"role": "user", "content": _PROMPT.format(text=text)}]
    )
    raw = response.content[0].text
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    if match:
        data = json.loads(match.group())
        return {
            "source_language": data.get("source_language", ""),
            "translation": data.get("translation", ""),
            "word_type": data.get("word_type", ""),
            "example_source": data.get("example_source", ""),
            "example_target": data.get("example_target", ""),
        }
    return {"source_language": "", "translation": raw.strip(), "word_type": "", "example_source": "", "example_target": ""}
