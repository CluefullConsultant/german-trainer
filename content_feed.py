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


def generate_daily_vocab(existing_words: list[str]) -> list[dict]:
    """Pick 8 words from the structured A1-C1 vocab list that the user hasn't seen yet.

    Selection: 1 A1/A2 wildcard + 2 B1 + 3 B2 + 2 C1.
    Falls back to any unseen word if a level is exhausted.
    """
    from vocab_list import VOCAB_LIST
    import random

    seen = set(existing_words)
    unseen = [w for w in VOCAB_LIST if w["word"] not in seen]

    if not unseen:
        return []

    def pick(levels, n):
        pool = [w for w in unseen if w["level"] in levels]
        random.shuffle(pool)
        return pool[:n]

    selected = []
    selected += pick(["A1", "A2"], 1)
    selected += pick(["B1"], 2)
    selected += pick(["B2"], 3)
    selected += pick(["C1"], 2)

    # pad if any level was exhausted
    if len(selected) < 8:
        remaining = [w for w in unseen if w not in selected]
        random.shuffle(remaining)
        selected += remaining[:8 - len(selected)]

    result = []
    for w in selected:
        result.append({
            "word": w["word"],
            "definition": f"[{w['english']}] {w['definition']}",
            "example": w["example"],
            "is_verb": w["is_verb"],
            "context": "beruflich" if w["level"] in ("B2", "C1") else "alltäglich",
            "level": w["level"],
        })
    return result


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
