import requests
import xml.etree.ElementTree as ET
import streamlit as st
import anthropic
import re
import json


LESEN_SOURCES = {
    "Zeit": {
        "Schlagzeilen": "https://newsfeed.zeit.de/index",
    },
    "Spiegel": {
        "Schlagzeilen": "https://www.spiegel.de/schlagzeilen/index.rss",
    },
    "Handelsblatt": {
        "Schlagzeilen": "https://feeds.cms.handelsblatt.com/schlagzeilen",
        "Politik": "https://feeds.cms.handelsblatt.com/politik",
        "Unternehmen": "https://feeds.cms.handelsblatt.com/unternehmen",
        "Finanzen": "https://feeds.cms.handelsblatt.com/finanzen",
        "Technologie": "https://feeds.cms.handelsblatt.com/technologie",
        "Marktberichte": "https://feeds.cms.handelsblatt.com/marktberichte",
    },
    "WirtschaftsWoche": {
        "Schlagzeilen": "https://feeds.cms.wiwo.de/rss/schlagzeilen",
        "Erfolg": "https://feeds.cms.wiwo.de/rss/erfolg",
        "Finanzen": "https://feeds.cms.wiwo.de/rss/finanzen",
        "Politik": "https://feeds.cms.wiwo.de/rss/politik",
        "Technologie": "https://feeds.cms.wiwo.de/rss/technologie",
        "Unternehmen": "https://feeds.cms.wiwo.de/rss/unternehmen",
    },
}


def fetch_lesen_articles(url: str, max_items: int = 8) -> list[dict]:
    """Fetch current articles from a real (non-learner-simplified) German news RSS feed."""
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code != 200:
            return []
        root = ET.fromstring(resp.content)
        items = []
        for item in root.findall(".//item"):
            title = item.findtext("title", "").strip()
            link = item.findtext("link", "").strip()
            desc = item.findtext("description", "").strip()
            desc = re.sub(r"<[^>]+>", "", desc).strip()
            if title:
                items.append({"title": title, "link": link, "description": desc or title})
            if len(items) >= max_items:
                break
        return items
    except Exception:
        return []


HOEREN_SOURCES = {
    "Deutschlandfunk – Der Tag": "https://www.deutschlandfunk.de/podcast-104.xml",
    "Lage der Nation": "https://feeds.lagedernation.org/feeds/ldn-mp3.xml",
    "Easy German Podcast": "https://podcast.easygerman.org/rss",
    "Handelsblatt Audio": "https://feeds.cms.handelsblatt.com/podcast",
}

_ITUNES_NS = "http://www.itunes.com/dtds/podcast-1.0.dtd"
_PODCAST_NS = "https://podcastindex.org/namespace/1.0"


def fetch_hoeren_episodes(url: str, max_items: int = 8) -> list[dict]:
    """Fetch current episodes from a real German-language podcast RSS feed.

    Not every feed exposes a playable audio enclosure (Handelsblatt's only links out
    to its own player), so audio_url can be None - the UI falls back to an external link.
    """
    try:
        resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code != 200:
            return []
        root = ET.fromstring(resp.content)
        episodes = []
        for item in root.findall(".//item"):
            title = item.findtext("title", "").strip()
            link = item.findtext("link", "").strip()
            desc = item.findtext("description", "").strip()
            desc = re.sub(r"<[^>]+>", "", desc).strip()

            enclosure = item.find("enclosure")
            audio_url = None
            if enclosure is not None and enclosure.get("type", "").startswith("audio"):
                audio_url = enclosure.get("url")

            duration = item.findtext(f"{{{_ITUNES_NS}}}duration", "").strip()
            transcript_el = item.find(f"{{{_PODCAST_NS}}}transcript")
            transcript_url = transcript_el.get("url") if transcript_el is not None else None

            if title:
                episodes.append({
                    "title": title,
                    "link": link,
                    "description": desc or title,
                    "audio_url": audio_url,
                    "duration": duration,
                    "transcript_url": transcript_url,
                })
            if len(episodes) >= max_items:
                break
        return episodes
    except Exception:
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
