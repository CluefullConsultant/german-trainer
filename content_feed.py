import requests
import xml.etree.ElementTree as ET
import streamlit as st
import anthropic
import re
import json


def fetch_dw_articles(max_items: int = 5) -> list[dict]:
    """Fetch today's articles from Deutsche Welle learner RSS."""
    urls = [
        "https://rss.dw.com/xml/rss-de-all",
        "https://rss.dw.com/xml/rss-de-ger",
        "https://www.tagesschau.de/xml/rss2",
        "https://rss.dw.com/rdf/rss-de-all",
    ]
    for url in urls:
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code != 200:
                continue
            root = ET.fromstring(resp.content)
            items = []
            for item in root.findall(".//item"):
                title = item.findtext("title", "").strip()
                link = item.findtext("link", "").strip()
                desc = item.findtext("description", "").strip()
                if title and desc:
                    items.append({"title": title, "link": link, "description": desc})
                if len(items) >= max_items:
                    break
            if items:
                return items
        except Exception:
            continue
    return []


def generate_questions_from_article(title: str, text: str) -> list[dict]:
    """Generate 3 comprehension questions from article text."""
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)
    prompt = f"""Artikel: "{title}"
Text: "{text}"

Erstelle 3 einfache Verstaendnisfragen auf Deutsch zu diesem Artikel. Antworte NUR mit JSON:
[{{"question": "Frage?", "answer": "Antwort"}}]"""
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.content[0].text
    match = re.search(r'\[.*\]', raw, re.DOTALL)
    if match:
        return json.loads(match.group())
    return []


def generate_tandem_prompts(title: str, text: str) -> list[str]:
    """Generate 5 conversation prompts for Tandem speaking practice based on the article."""
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)
    prompt = f"""Artikel: "{title}"
Text: "{text}"

Erstelle 5 Gesprächsanlässe auf Deutsch für ein Tandem-Gespräch über diesen Artikel.
Die Fragen sollen zum Nachdenken anregen und eine echte Diskussion ermöglichen - nicht nur Ja/Nein-Antworten.
Antworte NUR mit JSON: ["Frage 1?", "Frage 2?", "Frage 3?", "Frage 4?", "Frage 5?"]"""

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.content[0].text
    match = re.search(r'\[.*\]', raw, re.DOTALL)
    if match:
        return json.loads(match.group())
    return []


def extract_vocab_from_article(text: str) -> list[dict]:
    """Extract 5 useful vocabulary words from article."""
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)
    prompt = f"""Text: "{text}"

Extrahiere 5 nuetzliche Vokabeln aus diesem Text fuer einen B2/C1 Deutschlernenden.
Antworte NUR mit JSON:
[{{"word": "Wort", "definition": "Deutsche Definition", "example": "Beispielsatz aus dem Text"}}]"""
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.content[0].text
    match = re.search(r'\[.*\]', raw, re.DOTALL)
    if match:
        return json.loads(match.group())
    return []
