# German Trainer App Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a shared Streamlit app where Antony's German mentor creates exercises with Claude's help, Antony solves them, and both track progress toward C1.

**Architecture:** Single Streamlit app with 4 tabs (create, practice, feedback, progress). Claude generates exercises from a guided mentor form and gives instant feedback on submissions. Supabase stores all exercises, submissions, and vocabulary persistently. Entire UI is in German.

**Tech Stack:** Python 3.11+, Streamlit, Anthropic Python SDK, supabase-py, deployed on Streamlit Cloud.

## Global Constraints

- All UI text must be in German - no English strings visible to users
- No Niveau/level selector - all exercises target B2-C1, covering foundations as topics
- No user accounts or login - one shared URL, all tabs visible to both users
- Model: `claude-sonnet-4-5` (consistent with existing tools)
- No em dashes anywhere in code or copy - use plain dash or rewrite
- Follow existing streaming pattern from other tools: `client.messages.stream(...)` with `stream.text_stream`
- Robust JSON parsing: use `re.search(r'\{.*\}', raw, re.DOTALL)` to strip markdown fences

---

## File Structure

```
german-trainer/
├── app.py              # Streamlit UI - 4 tabs, all German
├── db.py               # Supabase client + all DB operations
├── exercises.py        # Claude exercise generation - prompts, parsing, topic/type lists
├── feedback.py         # Claude answer feedback - per-item grading, error tagging
├── vocabulary.py       # Claude vocabulary extraction from exercise content
├── requirements.txt    # Dependencies
├── .streamlit/
│   └── secrets.toml    # Local only - ANTHROPIC_API_KEY, SUPABASE_URL, SUPABASE_KEY
└── docs/
    └── superpowers/
        ├── specs/2026-06-30-german-trainer-design.md
        └── plans/2026-06-30-german-trainer.md
```

---

## Exercise Content Schemas (JSON stored in Supabase `content` column)

Each exercise type uses a fixed JSON schema. Claude must output exactly this shape.

**Luckentext:**
```json
{
  "text_with_blanks": "Obwohl er müde ___ war, ging er zur Arbeit.",
  "blanks": [{"position": 0, "answer": "war", "hint": "Verb: sein"}],
  "explanation": "Obwohl ist eine subordinierende Konjunktion (Kategorie C) - das Verb geht ans Ende."
}
```

**Mehrfachauswahl:**
```json
{
  "question": "Welcher Konnektor passt hier? Er ist müde, ___ er geht zur Arbeit.",
  "options": ["obwohl", "trotzdem", "dennoch", "weil"],
  "correct_index": 0,
  "explanation": "obwohl leitet einen Nebensatz ein (Verb ans Ende). trotzdem/dennoch wären adverbiale Konnektoren."
}
```

**Satztransformation:**
```json
{
  "instruction": "Verbinden Sie die zwei Satze mit 'obwohl':",
  "sentences": ["Er ist müde.", "Er geht zur Arbeit."],
  "answer": "Obwohl er müde ist, geht er zur Arbeit.",
  "explanation": "obwohl (Kategorie C): Verb ans Ende des Nebensatzes."
}
```

**Fehlersuche:**
```json
{
  "sentences": [
    {"text": "Es statt findet morgen statt.", "has_error": true, "correction": "Es findet morgen statt.", "rule": "Trennbare Verben: Prafix geht ans Satzende"},
    {"text": "Obwohl er müde ist, geht er zur Arbeit.", "has_error": false, "correction": null, "rule": null}
  ]
}
```

**Ubersetzung:**
```json
{
  "direction": "EN-DE",
  "source": "Although he is tired, he goes to work.",
  "answer": "Obwohl er müde ist, geht er zur Arbeit.",
  "explanation": "obwohl = subordinierende Konjunktion, Verb ans Ende."
}
```

**Kategoriensortierung:**
```json
{
  "instruction": "Sortieren Sie die Konnektoren in die richtige Kategorie (A, B oder C):",
  "words": ["obwohl", "trotzdem", "und", "weil", "jedoch", "aber"],
  "categories": {
    "A - Koordinierende Konjunktionen": ["und", "aber"],
    "B - Adverbiale Konnektoren": ["trotzdem", "jedoch"],
    "C - Subordinierende Konjunktionen": ["obwohl", "weil"]
  },
  "explanation": "Kategorie bestimmt die Wortstellung, nicht die Bedeutung."
}
```

**Brief schreiben:**
```json
{
  "prompt": "Schreiben Sie einen formellen Beschwerdebrief an einen Vermieter. Ihr Heizsystem funktioniert seit zwei Wochen nicht.",
  "reihenpunkte": ["Schildern Sie das Problem und seit wann es besteht", "Beschreiben Sie die Auswirkungen auf Ihren Alltag", "Fordern Sie eine konkrete Losung innerhalb einer Frist"],
  "time_limit_minutes": 30,
  "register": "formell"
}
```

**Leseverstehen / Horverstehen:**
```json
{
  "text": "...[full German text pasted by mentor]...",
  "is_hoerverstehen": false,
  "questions": [
    {"question": "Was ist das Hauptthema des Textes?", "answer": "..."},
    {"question": "Welche drei Argumente nennt der Autor?", "answer": "..."},
    {"question": "Was bedeutet der Begriff '...' im Kontext des Textes?", "answer": "..."}
  ]
}
```

**Sprechaufgabe:**
```json
{
  "prompt": "Beschreiben Sie eine Situation, in der Sie eine schwierige Entscheidung treffen mussten. Verwenden Sie Konjunktiv II.",
  "hints": ["Mindestens 2 Minuten sprechen", "Konjunktiv II: hatte, ware, wurde...", "Begrunden Sie Ihre Entscheidung"]
}
```

---

### Task 1: Project Setup

**Files:**
- Create: `german-trainer/requirements.txt`
- Create: `german-trainer/.streamlit/secrets.toml` (local only, gitignored)
- Create: `german-trainer/.gitignore`

**Interfaces:**
- Produces: working Python environment, Supabase tables, secrets structure for Tasks 2-9

- [ ] **Step 1: Create the project directory and git repo**

```bash
cd C:\Users\antme\Projects
mkdir german-trainer
cd german-trainer
git init
```

- [ ] **Step 2: Create requirements.txt**

```
streamlit>=1.35.0
anthropic>=0.28.0
supabase>=2.4.0
```

- [ ] **Step 3: Create .gitignore**

```
.streamlit/secrets.toml
__pycache__/
*.pyc
.env
```

- [ ] **Step 4: Create .streamlit/secrets.toml structure (fill in values after Supabase setup)**

```bash
mkdir .streamlit
```

```toml
ANTHROPIC_API_KEY = "sk-ant-..."
SUPABASE_URL = "https://xxxx.supabase.co"
SUPABASE_KEY = "eyJ..."
```

- [ ] **Step 5: Create Supabase project and tables**

Go to https://supabase.com, create a free project called `german-trainer`.

In the Supabase SQL editor, run:

```sql
create table exercises (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz default now(),
  topic text not null,
  exercise_type text not null,
  content jsonb not null,
  mentor_notes text
);

create table submissions (
  id uuid primary key default gen_random_uuid(),
  exercise_id uuid references exercises(id) on delete cascade,
  submitted_at timestamptz default now(),
  answer jsonb not null,
  claude_feedback text,
  mentor_feedback text,
  reviewed_at timestamptz,
  error_tags text[]
);

create table vocabulary (
  id uuid primary key default gen_random_uuid(),
  exercise_id uuid references exercises(id) on delete cascade,
  word text not null,
  definition text not null,
  example text not null,
  added_at timestamptz default now()
);
```

- [ ] **Step 6: Copy Supabase URL and anon key into secrets.toml**

In Supabase: Project Settings > API. Copy "Project URL" and "anon public" key into `.streamlit/secrets.toml`.

- [ ] **Step 7: Install dependencies**

```bash
pip install -r requirements.txt
```

Expected: all packages install without error.

- [ ] **Step 8: Initial commit**

```bash
git add requirements.txt .gitignore .streamlit/
git commit -m "chore: project setup with Supabase schema and dependencies"
```

---

### Task 2: db.py - Database Layer

**Files:**
- Create: `german-trainer/db.py`
- Create: `german-trainer/tests/test_db.py`

**Interfaces:**
- Consumes: Supabase tables from Task 1, `st.secrets` for credentials
- Produces:
  - `get_client() -> Client`
  - `save_exercise(topic: str, exercise_type: str, content: dict, mentor_notes: str) -> str`
  - `get_exercises(topic_filter: str | None, status_filter: str | None) -> list[dict]`
  - `get_exercise(exercise_id: str) -> dict`
  - `save_submission(exercise_id: str, answer: dict) -> str`
  - `save_claude_feedback(submission_id: str, feedback: str, error_tags: list[str]) -> None`
  - `save_mentor_feedback(submission_id: str, feedback: str) -> None`
  - `get_unreviewed_submissions() -> list[dict]`
  - `get_all_reviewed_submissions() -> list[dict]`
  - `save_vocabulary(words: list[dict], exercise_id: str) -> None`
  - `get_vocabulary() -> list[dict]`
  - `get_error_stats() -> dict`

- [ ] **Step 1: Write the test file**

```python
# tests/test_db.py
import json
import pytest
from unittest.mock import MagicMock, patch

# We test the logic around db.py without hitting real Supabase.
# Each function is tested by mocking the supabase client.

@patch("db.get_client")
def test_save_exercise_returns_id(mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.table.return_value.insert.return_value.execute.return_value.data = [
        {"id": "abc-123"}
    ]
    import db
    result = db.save_exercise("Konnektoren", "Luckentext", {"text_with_blanks": "test"}, "")
    assert result == "abc-123"

@patch("db.get_client")
def test_get_exercises_no_filter(mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.table.return_value.select.return_value.order.return_value.execute.return_value.data = [
        {"id": "abc-123", "topic": "Konnektoren", "exercise_type": "Luckentext"}
    ]
    import db
    result = db.get_exercises(None, None)
    assert len(result) == 1
    assert result[0]["topic"] == "Konnektoren"

@patch("db.get_client")
def test_save_submission_returns_id(mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.table.return_value.insert.return_value.execute.return_value.data = [
        {"id": "sub-456"}
    ]
    import db
    result = db.save_submission("abc-123", {"answer": "war"})
    assert result == "sub-456"

@patch("db.get_client")
def test_get_error_stats_returns_dict(mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.table.return_value.select.return_value.execute.return_value.data = [
        {"error_tags": ["Konnektoren", "Trennbare Verben"]},
        {"error_tags": ["Konnektoren"]},
        {"error_tags": None},
    ]
    import db
    result = db.get_error_stats()
    assert result["Konnektoren"] == 2
    assert result["Trennbare Verben"] == 1
```

- [ ] **Step 2: Run tests to confirm they fail**

```bash
cd C:\Users\antme\Projects\german-trainer
python -m pytest tests/test_db.py -v
```

Expected: ImportError or ModuleNotFoundError - `db` does not exist yet.

- [ ] **Step 3: Implement db.py**

```python
# db.py
import streamlit as st
from supabase import create_client, Client
from datetime import datetime, timezone


def get_client() -> Client:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)


def save_exercise(topic: str, exercise_type: str, content: dict, mentor_notes: str) -> str:
    client = get_client()
    result = client.table("exercises").insert({
        "topic": topic,
        "exercise_type": exercise_type,
        "content": content,
        "mentor_notes": mentor_notes,
    }).execute()
    return result.data[0]["id"]


def get_exercises(topic_filter: str | None = None, status_filter: str | None = None) -> list[dict]:
    client = get_client()
    query = client.table("exercises").select(
        "*, submissions(id, reviewed_at)"
    ).order("created_at", desc=True)
    if topic_filter:
        query = query.eq("topic", topic_filter)
    rows = query.execute().data

    result = []
    for row in rows:
        subs = row.get("submissions") or []
        if status_filter == "Neu" and subs:
            continue
        if status_filter == "Bearbeitet" and not subs:
            continue
        if status_filter == "Feedback erhalten" and not any(s.get("reviewed_at") for s in subs):
            continue
        # Attach latest status label
        if not subs:
            row["status"] = "Neu"
        elif any(s.get("reviewed_at") for s in subs):
            row["status"] = "Feedback erhalten"
        else:
            row["status"] = "Beim Mentor"
        result.append(row)
    return result


def get_exercise(exercise_id: str) -> dict:
    client = get_client()
    result = client.table("exercises").select("*").eq("id", exercise_id).single().execute()
    return result.data


def save_submission(exercise_id: str, answer: dict) -> str:
    client = get_client()
    result = client.table("submissions").insert({
        "exercise_id": exercise_id,
        "answer": answer,
    }).execute()
    return result.data[0]["id"]


def save_claude_feedback(submission_id: str, feedback: str, error_tags: list[str]) -> None:
    client = get_client()
    client.table("submissions").update({
        "claude_feedback": feedback,
        "error_tags": error_tags,
    }).eq("id", submission_id).execute()


def save_mentor_feedback(submission_id: str, feedback: str) -> None:
    client = get_client()
    client.table("submissions").update({
        "mentor_feedback": feedback,
        "reviewed_at": datetime.now(timezone.utc).isoformat(),
    }).eq("id", submission_id).execute()


def get_unreviewed_submissions() -> list[dict]:
    client = get_client()
    result = client.table("submissions").select(
        "*, exercises(topic, exercise_type, content)"
    ).is_("reviewed_at", "null").order("submitted_at", desc=True).execute()
    return result.data


def get_all_reviewed_submissions() -> list[dict]:
    client = get_client()
    result = client.table("submissions").select(
        "*, exercises(topic, exercise_type, content)"
    ).not_.is_("reviewed_at", "null").order("reviewed_at", desc=True).execute()
    return result.data


def save_vocabulary(words: list[dict], exercise_id: str) -> None:
    client = get_client()
    rows = [
        {"word": w["word"], "definition": w["definition"], "example": w["example"], "exercise_id": exercise_id}
        for w in words
    ]
    if rows:
        client.table("vocabulary").insert(rows).execute()


def get_vocabulary() -> list[dict]:
    client = get_client()
    result = client.table("vocabulary").select("*").order("added_at", desc=True).execute()
    return result.data


def get_error_stats() -> dict:
    client = get_client()
    result = client.table("submissions").select("error_tags").execute()
    counts: dict[str, int] = {}
    for row in result.data:
        tags = row.get("error_tags") or []
        for tag in tags:
            counts[tag] = counts.get(tag, 0) + 1
    return counts
```

- [ ] **Step 4: Run tests**

```bash
python -m pytest tests/test_db.py -v
```

Expected: 4 tests pass.

- [ ] **Step 5: Commit**

```bash
git add db.py tests/test_db.py
git commit -m "feat: add Supabase database layer"
```

---

### Task 3: exercises.py - Exercise Generation

**Files:**
- Create: `german-trainer/exercises.py`
- Create: `german-trainer/tests/test_exercises.py`

**Interfaces:**
- Consumes: Anthropic API via `st.secrets["ANTHROPIC_API_KEY"]`
- Produces:
  - `TOPICS: list[str]` - ordered list of all topic names in German
  - `EXERCISE_TYPES: list[str]` - ordered list of all exercise type names in German
  - `EXERCISE_TYPES_FOR_TOPIC: dict[str, list[str]]` - which types are valid per topic
  - `generate_exercise(topic: str, exercise_type: str, mentor_notes: str) -> dict` - returns parsed content JSON

- [ ] **Step 1: Write tests**

```python
# tests/test_exercises.py
import json
import pytest
from unittest.mock import MagicMock, patch


def test_topics_list_not_empty():
    import exercises
    assert len(exercises.TOPICS) > 10
    assert "Konnektoren" in exercises.TOPICS
    assert "Deklination" in exercises.TOPICS


def test_exercise_types_not_empty():
    import exercises
    assert "Luckentext" in exercises.EXERCISE_TYPES
    assert "Brief schreiben" in exercises.EXERCISE_TYPES


def test_exercise_types_for_topic_brief_schreiben():
    import exercises
    types = exercises.EXERCISE_TYPES_FOR_TOPIC.get("Schriftlicher Ausdruck (Brief)", [])
    assert "Brief schreiben" in types


def test_parse_exercise_json_strips_fences():
    import exercises
    raw = '```json\n{"text_with_blanks": "test"}\n```'
    result = exercises._parse_json(raw)
    assert result["text_with_blanks"] == "test"


def test_parse_exercise_json_plain():
    import exercises
    raw = '{"text_with_blanks": "test"}'
    result = exercises._parse_json(raw)
    assert result["text_with_blanks"] == "test"


def test_parse_exercise_json_invalid_raises():
    import exercises
    with pytest.raises(ValueError):
        exercises._parse_json("this is not json at all")
```

- [ ] **Step 2: Run tests to confirm they fail**

```bash
python -m pytest tests/test_exercises.py -v
```

Expected: ImportError - `exercises` module does not exist.

- [ ] **Step 3: Implement exercises.py**

```python
# exercises.py
import re
import json
import streamlit as st
import anthropic

TOPICS = [
    "Artikel & Genus",
    "Deklination (Nominativ/Akkusativ/Dativ/Genitiv)",
    "Personalpronomina",
    "Possessivartikel",
    "Konnektoren",
    "Trennbare Verben",
    "Wechselprasitionen",
    "Konjunktiv II",
    "Passiv",
    "Relativsatze",
    "Wortstellung",
    "Temporale Konjunktionen",
    "Genitiv-Prasitionen",
    "Partizipialkonstruktionen",
    "Nominalisierung",
    "Infinitiv mit zu",
    "Schriftlicher Ausdruck (Brief)",
    "Leseverstehen",
    "Horverstehen",
    "Sprechaufgabe",
    "Wortschatz in Kontext",
]

EXERCISE_TYPES = [
    "Luckentext",
    "Mehrfachauswahl",
    "Satztransformation",
    "Fehlersuche",
    "Ubersetzung",
    "Kategoriensortierung",
    "Brief schreiben",
    "Leseverstehen",
    "Horverstehen",
    "Sprechaufgabe",
]

# Which exercise types make sense for each topic
EXERCISE_TYPES_FOR_TOPIC: dict[str, list[str]] = {
    "Artikel & Genus": ["Luckentext", "Mehrfachauswahl", "Fehlersuche"],
    "Deklination (Nominativ/Akkusativ/Dativ/Genitiv)": ["Luckentext", "Mehrfachauswahl", "Fehlersuche", "Satztransformation"],
    "Personalpronomina": ["Luckentext", "Mehrfachauswahl", "Fehlersuche"],
    "Possessivartikel": ["Luckentext", "Mehrfachauswahl", "Fehlersuche"],
    "Konnektoren": ["Luckentext", "Mehrfachauswahl", "Satztransformation", "Fehlersuche", "Kategoriensortierung", "Ubersetzung"],
    "Trennbare Verben": ["Luckentext", "Satztransformation", "Fehlersuche", "Mehrfachauswahl"],
    "Wechselprasitionen": ["Luckentext", "Mehrfachauswahl", "Fehlersuche", "Satztransformation"],
    "Konjunktiv II": ["Luckentext", "Satztransformation", "Fehlersuche", "Ubersetzung"],
    "Passiv": ["Satztransformation", "Luckentext", "Fehlersuche", "Ubersetzung"],
    "Relativsatze": ["Luckentext", "Satztransformation", "Fehlersuche"],
    "Wortstellung": ["Fehlersuche", "Satztransformation", "Luckentext"],
    "Temporale Konjunktionen": ["Luckentext", "Mehrfachauswahl", "Satztransformation", "Kategoriensortierung"],
    "Genitiv-Prasitionen": ["Luckentext", "Mehrfachauswahl", "Fehlersuche"],
    "Partizipialkonstruktionen": ["Luckentext", "Satztransformation", "Fehlersuche"],
    "Nominalisierung": ["Satztransformation", "Luckentext", "Ubersetzung"],
    "Infinitiv mit zu": ["Luckentext", "Satztransformation", "Fehlersuche"],
    "Schriftlicher Ausdruck (Brief)": ["Brief schreiben"],
    "Leseverstehen": ["Leseverstehen"],
    "Horverstehen": ["Horverstehen"],
    "Sprechaufgabe": ["Sprechaufgabe"],
    "Wortschatz in Kontext": ["Luckentext", "Mehrfachauswahl", "Ubersetzung"],
}

_SYSTEM_PROMPT = """Du bist ein erfahrener Deutschlehrer, der Ubungsaufgaben fur einen Lernenden auf B2/C1-Niveau erstellt.
Erstelle immer klar strukturierte Aufgaben mit einem Losungsschlussel und einer Erklarung der Grammatikregel.
Antworte NUR mit einem gultig formatierten JSON-Objekt - kein Markdown, kein erklarender Text davor oder danach.
Die Aufgabe muss pedagogisch korrekt und auf C1-Niveau sein, darf aber grundlegende Grammatik (A1-C1) als Thema haben."""

_TYPE_SCHEMAS = {
    "Luckentext": """Ausgabeformat:
{"text_with_blanks": "Satz mit ___ fur jede Lucke", "blanks": [{"position": 0, "answer": "Antwort", "hint": "kurzer Hinweis"}], "explanation": "Grammatikerklarung"}
Erstelle 5-8 Lucken im Text.""",

    "Mehrfachauswahl": """Ausgabeformat:
{"question": "Frage", "options": ["Option A", "Option B", "Option C", "Option D"], "correct_index": 0, "explanation": "Grammatikerklarung"}
Erstelle 5 Fragen als Array unter dem Schlussel "items": [...]""",

    "Satztransformation": """Ausgabeformat:
{"items": [{"instruction": "Anweisung", "sentences": ["Satz 1.", "Satz 2."], "answer": "Kombinierter Satz", "explanation": "Erklarung"}]}
Erstelle 5 Transformationsaufgaben.""",

    "Fehlersuche": """Ausgabeformat:
{"sentences": [{"text": "Satz mit oder ohne Fehler", "has_error": true, "correction": "Korrektur oder null", "rule": "Regelname oder null"}]}
Erstelle 8 Satze, davon 5 mit Fehlern und 3 ohne Fehler (gemischt).""",

    "Ubersetzung": """Ausgabeformat:
{"direction": "EN-DE", "items": [{"source": "Englischer Satz", "answer": "Deutscher Satz", "explanation": "Grammatikhinweis"}]}
Erstelle 5 Ubersetzungsaufgaben.""",

    "Kategoriensortierung": """Ausgabeformat:
{"instruction": "Sortieranweisung", "words": ["Wort1", "Wort2", ...], "categories": {"Kategoriename": ["Wort1"], ...}, "explanation": "Erklarung des Systems"}
Verwende mindestens 10 Worter auf mindestens 3 Kategorien verteilt.""",

    "Brief schreiben": """Ausgabeformat:
{"prompt": "Aufgabenstellung", "reihenpunkte": ["Punkt 1", "Punkt 2", "Punkt 3"], "time_limit_minutes": 30, "register": "formell"}
Erstelle einen realistischen Telc-Stil Briefschreibauftrag.""",

    "Leseverstehen": """Ausgabeformat:
{"text": "...vollstandiger deutscher Text...", "is_hoerverstehen": false, "questions": [{"question": "Frage", "answer": "Antwort"}]}
Der Text muss mindestens 300 Worter haben. Erstelle 5 Verstandnisfragen auf C1-Niveau. Falls der Mentor einen Text bereitgestellt hat, verwende diesen.""",

    "Horverstehen": """Ausgabeformat:
{"text": "...Text der laut vorgelesen wird...", "is_hoerverstehen": true, "questions": [{"question": "Frage", "answer": "Antwort"}]}
Der Text muss 150-250 Worter haben (ca. 1-2 Minuten Lesezeit). Erstelle 5 Fragen. Falls der Mentor einen Text bereitgestellt hat, verwende diesen.""",

    "Sprechaufgabe": """Ausgabeformat:
{"prompt": "Sprechanlass", "hints": ["Hinweis 1", "Hinweis 2", "Hinweis 3"]}
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
```

- [ ] **Step 4: Run tests**

```bash
python -m pytest tests/test_exercises.py -v
```

Expected: all 6 tests pass.

- [ ] **Step 5: Commit**

```bash
git add exercises.py tests/test_exercises.py
git commit -m "feat: add Claude exercise generation with topic/type system"
```

---

### Task 4: feedback.py - Answer Feedback

**Files:**
- Create: `german-trainer/feedback.py`
- Create: `german-trainer/tests/test_feedback.py`

**Interfaces:**
- Consumes: Anthropic API, exercise content dict (from Task 3 schemas), answer dict
- Produces:
  - `generate_feedback(exercise_content: dict, exercise_type: str, answer: dict) -> tuple[str, list[str]]`
    - Returns `(feedback_text_in_german, error_tags)`
    - `error_tags` are strings from TOPICS list in exercises.py

- [ ] **Step 1: Write tests**

```python
# tests/test_feedback.py
import pytest
from unittest.mock import MagicMock, patch


def test_parse_feedback_response_extracts_text_and_tags():
    import feedback
    raw = '{"feedback": "Sehr gut! Obwohl ist korrekt.", "error_tags": ["Konnektoren"]}'
    text, tags = feedback._parse_feedback_response(raw)
    assert "Sehr gut" in text
    assert "Konnektoren" in tags


def test_parse_feedback_response_empty_tags():
    import feedback
    raw = '{"feedback": "Alles korrekt!", "error_tags": []}'
    text, tags = feedback._parse_feedback_response(raw)
    assert tags == []


def test_parse_feedback_strips_markdown():
    import feedback
    raw = '```json\n{"feedback": "Gut gemacht.", "error_tags": ["Trennbare Verben"]}\n```'
    text, tags = feedback._parse_feedback_response(raw)
    assert "Gut gemacht" in text
    assert "Trennbare Verben" in tags
```

- [ ] **Step 2: Run tests to confirm they fail**

```bash
python -m pytest tests/test_feedback.py -v
```

Expected: ImportError.

- [ ] **Step 3: Implement feedback.py**

```python
# feedback.py
import re
import json
import streamlit as st
import anthropic

_SYSTEM_PROMPT = """Du bist ein strenger, prasizer Deutschlehrer.
Beurteile die Antwort des Lernenden und gib direktes, konkretes Feedback auf Deutsch.
Erklare jeden Fehler mit der genauen Grammatikregel die verletzt wurde.
Sei direkt - keine Lobhudelei fur falsche Antworten.
Antworte NUR mit einem JSON-Objekt: {"feedback": "Dein Feedback-Text", "error_tags": ["Themenname"]}
error_tags: Liste der Grammatikthemen bei denen Fehler gemacht wurden (leer wenn alles korrekt)."""


def _parse_feedback_response(raw: str) -> tuple[str, list[str]]:
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    if not match:
        return raw, []
    data = json.loads(match.group())
    return data.get("feedback", raw), data.get("error_tags", [])


def generate_feedback(exercise_content: dict, exercise_type: str, answer: dict) -> tuple[str, list[str]]:
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)

    user_prompt = f"""Aufgabentyp: {exercise_type}
Aufgabe:
{json.dumps(exercise_content, ensure_ascii=False, indent=2)}

Antwort des Lernenden:
{json.dumps(answer, ensure_ascii=False, indent=2)}

Beurteile die Antwort. Gib item-weises Feedback und benenne jeden Grammatikfehler genau."""

    raw = ""
    with client.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    ) as stream:
        for text in stream.text_stream:
            raw += text

    return _parse_feedback_response(raw)
```

- [ ] **Step 4: Run tests**

```bash
python -m pytest tests/test_feedback.py -v
```

Expected: 3 tests pass.

- [ ] **Step 5: Commit**

```bash
git add feedback.py tests/test_feedback.py
git commit -m "feat: add Claude answer feedback with error tagging"
```

---

### Task 5: vocabulary.py - Vocabulary Extraction

**Files:**
- Create: `german-trainer/vocabulary.py`
- Create: `german-trainer/tests/test_vocabulary.py`

**Interfaces:**
- Consumes: Anthropic API, exercise content dict
- Produces:
  - `extract_vocabulary(exercise_content: dict, exercise_type: str) -> list[dict]`
    - Returns list of `{"word": str, "definition": str, "example": str}`

- [ ] **Step 1: Write tests**

```python
# tests/test_vocabulary.py
import pytest
from unittest.mock import patch


def test_parse_vocabulary_response():
    import vocabulary
    raw = '[{"word": "trotzdem", "definition": "dennoch, aber", "example": "Er war müde, trotzdem ging er."}]'
    result = vocabulary._parse_vocab_response(raw)
    assert len(result) == 1
    assert result[0]["word"] == "trotzdem"


def test_parse_vocabulary_strips_markdown():
    import vocabulary
    raw = '```json\n[{"word": "obwohl", "definition": "auch wenn", "example": "Obwohl er müde war..."}]\n```'
    result = vocabulary._parse_vocab_response(raw)
    assert result[0]["word"] == "obwohl"


def test_parse_vocabulary_invalid_returns_empty():
    import vocabulary
    result = vocabulary._parse_vocab_response("keine json hier")
    assert result == []
```

- [ ] **Step 2: Run tests to confirm they fail**

```bash
python -m pytest tests/test_vocabulary.py -v
```

Expected: ImportError.

- [ ] **Step 3: Implement vocabulary.py**

```python
# vocabulary.py
import re
import json
import streamlit as st
import anthropic

_SYSTEM_PROMPT = """Du bist ein Deutschlehrer. Extrahiere 3-5 wichtige Vokabeln aus dem gegebenen Ubungstext.
Gib nur Vokabeln zuruck, die fur B2/C1-Niveau relevant sind.
Antworte NUR mit einem JSON-Array:
[{"word": "Wort", "definition": "Deutsche Definition/Erklarung", "example": "Beispielsatz aus dem Text"}]"""


def _parse_vocab_response(raw: str) -> list[dict]:
    match = re.search(r'\[.*\]', raw, re.DOTALL)
    if not match:
        return []
    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return []


def extract_vocabulary(exercise_content: dict, exercise_type: str) -> list[dict]:
    # Skip types with no meaningful text to extract vocabulary from
    if exercise_type in ("Sprechaufgabe", "Brief schreiben", "Kategoriensortierung"):
        return []

    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)

    content_text = json.dumps(exercise_content, ensure_ascii=False)

    raw = ""
    with client.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=512,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"Ubungsinhalt:\n{content_text}"}]
    ) as stream:
        for text in stream.text_stream:
            raw += text

    return _parse_vocab_response(raw)
```

- [ ] **Step 4: Run tests**

```bash
python -m pytest tests/test_vocabulary.py -v
```

Expected: 3 tests pass.

- [ ] **Step 5: Commit**

```bash
git add vocabulary.py tests/test_vocabulary.py
git commit -m "feat: add Claude vocabulary extraction"
```

---

### Task 6: Tab 1 - "Aufgaben erstellen" (Mentor creates exercises)

**Files:**
- Create: `german-trainer/app.py` (initial version, Tab 1 only, other tabs are stubs)

**Interfaces:**
- Consumes: `exercises.TOPICS`, `exercises.EXERCISE_TYPES_FOR_TOPIC`, `exercises.generate_exercise()`, `db.save_exercise()`, `vocabulary.extract_vocabulary()`, `db.save_vocabulary()`
- Produces: working Tab 1 in Streamlit

- [ ] **Step 1: Create app.py with Tab 1**

```python
# app.py
import streamlit as st
import exercises
import feedback
import vocabulary
import db
import json

st.set_page_config(page_title="Deutsch Trainer", page_icon="", layout="wide")

st.title("Deutsch Trainer")
st.caption("Ein Lernwerkzeug fur Antony und seinen Mentor")

tab1, tab2, tab3, tab4 = st.tabs([
    "Aufgaben erstellen",
    "Uben",
    "Feedback",
    "Fortschritt",
])

# ─── TAB 1: AUFGABEN ERSTELLEN ───────────────────────────────────────────────
with tab1:
    st.header("Neue Aufgabe erstellen")
    st.info(
        "Wahlen Sie ein Thema und einen Aufgabentyp. "
        "Claude erstellt die Ubung automatisch. "
        "Sie konnen die Aufgabe dann kontrollieren und speichern."
    )

    col1, col2 = st.columns(2)

    with col1:
        selected_topic = st.selectbox(
            "Thema",
            options=exercises.TOPICS,
            help="Welches Grammatikthema soll geübt werden?",
        )

    valid_types = exercises.EXERCISE_TYPES_FOR_TOPIC.get(selected_topic, exercises.EXERCISE_TYPES)

    with col2:
        selected_type = st.selectbox(
            "Aufgabentyp",
            options=valid_types,
            help="Welche Art von Aufgabe soll erstellt werden?",
        )

    # Show extra text input for Leseverstehen / Horverstehen
    pasted_text = ""
    if selected_type in ("Leseverstehen", "Horverstehen"):
        pasted_text = st.text_area(
            "Text einfügen (optional)",
            height=200,
            placeholder="Fugen Sie hier einen deutschen Text ein. Wenn leer, erstellt Claude einen passenden Text.",
            help="Sie konnen einen Zeitungsartikel oder anderen Text einfugen. Claude erstellt dann die Fragen dazu.",
        )

    mentor_notes = st.text_input(
        "Zusatzliche Hinweise (optional)",
        placeholder="z.B. 'obwohl vs trotzdem' oder 'Fokus auf trennbare Verben mit statt-'",
        help="Besondere Schwerpunkte oder Hinweise fur diese Aufgabe.",
    )

    if st.button("Aufgabe generieren", type="primary"):
        with st.spinner("Claude erstellt die Aufgabe..."):
            try:
                content = exercises.generate_exercise(
                    topic=selected_topic,
                    exercise_type=selected_type,
                    mentor_notes=mentor_notes,
                    pasted_text=pasted_text,
                )
                st.session_state["preview_content"] = content
                st.session_state["preview_topic"] = selected_topic
                st.session_state["preview_type"] = selected_type
                st.session_state["preview_notes"] = mentor_notes
            except Exception as e:
                st.error(f"Fehler bei der Generierung: {e}")

    if "preview_content" in st.session_state:
        st.divider()
        st.subheader("Vorschau")
        st.json(st.session_state["preview_content"])

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Neu generieren"):
                with st.spinner("Claude erstellt eine neue Version..."):
                    try:
                        content = exercises.generate_exercise(
                            topic=st.session_state["preview_topic"],
                            exercise_type=st.session_state["preview_type"],
                            mentor_notes=st.session_state["preview_notes"],
                            pasted_text=pasted_text,
                        )
                        st.session_state["preview_content"] = content
                        st.rerun()
                    except Exception as e:
                        st.error(f"Fehler: {e}")
        with col_b:
            if st.button("Speichern", type="primary"):
                with st.spinner("Wird gespeichert..."):
                    exercise_id = db.save_exercise(
                        topic=st.session_state["preview_topic"],
                        exercise_type=st.session_state["preview_type"],
                        content=st.session_state["preview_content"],
                        mentor_notes=st.session_state["preview_notes"],
                    )
                    # Extract and save vocabulary in background
                    try:
                        words = vocabulary.extract_vocabulary(
                            st.session_state["preview_content"],
                            st.session_state["preview_type"],
                        )
                        if words:
                            db.save_vocabulary(words, exercise_id)
                    except Exception:
                        pass  # Vocabulary extraction is best-effort
                    del st.session_state["preview_content"]
                    st.success("Aufgabe gespeichert!")
                    st.rerun()

# ─── TAB 2: UBEN (stub) ──────────────────────────────────────────────────────
with tab2:
    st.info("Ubungsbereich - wird in Schritt 7 implementiert.")

# ─── TAB 3: FEEDBACK (stub) ──────────────────────────────────────────────────
with tab3:
    st.info("Feedback-Bereich - wird in Schritt 8 implementiert.")

# ─── TAB 4: FORTSCHRITT (stub) ───────────────────────────────────────────────
with tab4:
    st.info("Fortschritt - wird in Schritt 9 implementiert.")
```

- [ ] **Step 2: Run the app locally**

```bash
streamlit run app.py
```

Expected: app opens in browser, Tab 1 shows the form. Select a topic, generate an exercise, see the JSON preview, save it. Verify it appears in Supabase `exercises` table.

- [ ] **Step 3: Commit**

```bash
git add app.py
git commit -m "feat: Tab 1 - mentor exercise creation with Claude"
```

---

### Task 7: Tab 2 - "Uben" (Antony solves exercises)

**Files:**
- Modify: `german-trainer/app.py` - replace Tab 2 stub with full implementation

**Interfaces:**
- Consumes: `db.get_exercises()`, `db.get_exercise()`, `db.save_submission()`, `db.save_claude_feedback()`, `feedback.generate_feedback()`
- Produces: working Tab 2 where Antony solves exercises and gets instant feedback

- [ ] **Step 1: Replace Tab 2 stub in app.py**

Replace the Tab 2 stub block with:

```python
# ─── TAB 2: UBEN ─────────────────────────────────────────────────────────────
with tab2:
    st.header("Aufgaben losen")

    # Filters
    col1, col2 = st.columns(2)
    with col1:
        topic_filter = st.selectbox(
            "Thema filtern",
            options=["Alle Themen"] + exercises.TOPICS,
            key="uben_topic_filter",
        )
    with col2:
        status_filter = st.selectbox(
            "Status filtern",
            options=["Alle", "Neu", "Beim Mentor", "Feedback erhalten"],
            key="uben_status_filter",
        )

    topic_q = None if topic_filter == "Alle Themen" else topic_filter
    status_q = None if status_filter == "Alle" else status_filter

    all_exercises = db.get_exercises(topic_q, status_q)

    if not all_exercises:
        st.info("Keine Aufgaben gefunden. Der Mentor hat noch keine Aufgaben erstellt.")
    else:
        # Exercise list
        if "selected_exercise_id" not in st.session_state:
            st.session_state["selected_exercise_id"] = None

        if st.session_state["selected_exercise_id"] is None:
            for ex in all_exercises:
                status_emoji = {"Neu": "", "Beim Mentor": "", "Feedback erhalten": ""}.get(ex["status"], "")
                with st.container(border=True):
                    c1, c2 = st.columns([4, 1])
                    with c1:
                        st.markdown(f"**{ex['topic']}** - {ex['exercise_type']}")
                        st.caption(f"{status_emoji} {ex['status']} | Erstellt: {ex['created_at'][:10]}")
                    with c2:
                        if st.button("Offnen", key=f"open_{ex['id']}"):
                            st.session_state["selected_exercise_id"] = ex["id"]
                            st.rerun()
        else:
            ex = db.get_exercise(st.session_state["selected_exercise_id"])
            if st.button("Zuruck zur Liste"):
                st.session_state["selected_exercise_id"] = None
                st.session_state.pop("current_answer", None)
                st.rerun()

            st.subheader(f"{ex['topic']} - {ex['exercise_type']}")
            content = ex["content"]

            # Render exercise by type and collect answer
            answer = {}

            if ex["exercise_type"] == "Luckentext":
                st.markdown(content.get("text_with_blanks", ""))
                answers_list = []
                for i, blank in enumerate(content.get("blanks", [])):
                    val = st.text_input(f"Lucke {i+1} ({blank.get('hint', '')})", key=f"blank_{i}")
                    answers_list.append(val)
                answer = {"blanks": answers_list}

            elif ex["exercise_type"] == "Mehrfachauswahl":
                items_answers = []
                for i, item in enumerate(content.get("items", [content])):
                    st.markdown(f"**{i+1}.** {item.get('question', '')}")
                    choice = st.radio(
                        "Ihre Antwort:",
                        options=item.get("options", []),
                        key=f"mc_{i}",
                        label_visibility="collapsed",
                    )
                    items_answers.append(choice)
                answer = {"choices": items_answers}

            elif ex["exercise_type"] == "Satztransformation":
                items_answers = []
                for i, item in enumerate(content.get("items", [])):
                    st.markdown(f"**{i+1}.** {item.get('instruction', '')}")
                    for s in item.get("sentences", []):
                        st.markdown(f"- _{s}_")
                    val = st.text_input("Ihre Antwort:", key=f"trans_{i}")
                    items_answers.append(val)
                answer = {"transformations": items_answers}

            elif ex["exercise_type"] == "Fehlersuche":
                corrections = []
                for i, sentence in enumerate(content.get("sentences", [])):
                    st.markdown(f"**{i+1}.** {sentence['text']}")
                    has_err = st.checkbox("Enthalt einen Fehler", key=f"haserr_{i}")
                    correction = ""
                    if has_err:
                        correction = st.text_input("Korrektur:", key=f"corr_{i}")
                    corrections.append({"has_error": has_err, "correction": correction})
                answer = {"corrections": corrections}

            elif ex["exercise_type"] == "Ubersetzung":
                translations = []
                for i, item in enumerate(content.get("items", [])):
                    st.markdown(f"**{i+1}.** _{item.get('source', '')}_")
                    val = st.text_input("Ubersetzung:", key=f"trans_{i}")
                    translations.append(val)
                answer = {"translations": translations}

            elif ex["exercise_type"] == "Kategoriensortierung":
                st.markdown(content.get("instruction", ""))
                st.markdown("**Worter:** " + ", ".join(content.get("words", [])))
                cat_answers = {}
                for cat in content.get("categories", {}).keys():
                    val = st.text_input(f"{cat}:", key=f"cat_{cat}", placeholder="Worter durch Komma getrennt")
                    cat_answers[cat] = [w.strip() for w in val.split(",") if w.strip()]
                answer = {"categories": cat_answers}

            elif ex["exercise_type"] == "Brief schreiben":
                st.markdown(f"**Aufgabe:** {content.get('prompt', '')}")
                st.markdown("**Zu bearbeitende Punkte (Reihenpunkte):**")
                for punkt in content.get("reihenpunkte", []):
                    st.markdown(f"- {punkt}")
                if content.get("time_limit_minutes"):
                    st.info(f"Zeitlimit: {content['time_limit_minutes']} Minuten")
                letter = st.text_area("Ihr Brief:", height=400, key="brief_text")
                reihenpunkte_checked = []
                st.markdown("**Haben Sie alle Punkte behandelt?**")
                for punkt in content.get("reihenpunkte", []):
                    checked = st.checkbox(punkt, key=f"rp_{punkt}")
                    reihenpunkte_checked.append({"punkt": punkt, "behandelt": checked})
                answer = {"letter": letter, "reihenpunkte": reihenpunkte_checked}

            elif ex["exercise_type"] in ("Leseverstehen", "Horverstehen"):
                if ex["exercise_type"] == "Horverstehen":
                    st.info("Ihr Mentor liest den folgenden Text vor. Horen Sie gut zu.")
                    with st.expander("Text (fur den Mentor zum Vorlesen)"):
                        st.markdown(content.get("text", ""))
                else:
                    st.markdown("**Text:**")
                    st.markdown(content.get("text", ""))
                question_answers = []
                for i, q in enumerate(content.get("questions", [])):
                    st.markdown(f"**Frage {i+1}:** {q['question']}")
                    val = st.text_area("Ihre Antwort:", key=f"lv_{i}", height=80)
                    question_answers.append(val)
                answer = {"question_answers": question_answers}

            elif ex["exercise_type"] == "Sprechaufgabe":
                st.markdown(f"**Sprechanlass:** {content.get('prompt', '')}")
                st.markdown("**Hinweise:**")
                for hint in content.get("hints", []):
                    st.markdown(f"- {hint}")
                st.info("Sprechen Sie mit Ihrem Mentor. Keine schriftliche Eingabe erforderlich.")
                notes = st.text_area("Notizen (optional):", key="sprech_notes", height=100)
                answer = {"notes": notes, "type": "Sprechaufgabe"}

            st.divider()
            if st.button("Antwort einreichen", type="primary"):
                with st.spinner("Claude bewertet Ihre Antwort..."):
                    submission_id = db.save_submission(ex["id"], answer)
                    try:
                        fb_text, error_tags = feedback.generate_feedback(
                            exercise_content=content,
                            exercise_type=ex["exercise_type"],
                            answer=answer,
                        )
                        db.save_claude_feedback(submission_id, fb_text, error_tags)
                        st.session_state["last_feedback"] = fb_text
                    except Exception as e:
                        st.session_state["last_feedback"] = f"Feedback konnte nicht geladen werden: {e}"
                    st.rerun()

            if "last_feedback" in st.session_state:
                st.subheader("Claudes Feedback")
                st.markdown(st.session_state["last_feedback"])
                st.info("Ihr Mentor wird Ihnen zusatzliches Feedback geben.")
```

- [ ] **Step 2: Run the app and test Tab 2**

```bash
streamlit run app.py
```

Expected: Tab 2 shows a list of exercises saved in Task 6. Open one, fill in answers, submit. Verify submission appears in Supabase `submissions` table with `claude_feedback` populated.

- [ ] **Step 3: Commit**

```bash
git add app.py
git commit -m "feat: Tab 2 - exercise solving with instant Claude feedback"
```

---

### Task 8: Tab 3 - "Feedback" (Mentor reviews submissions)

**Files:**
- Modify: `german-trainer/app.py` - replace Tab 3 stub

**Interfaces:**
- Consumes: `db.get_unreviewed_submissions()`, `db.get_all_reviewed_submissions()`, `db.save_mentor_feedback()`
- Produces: working Tab 3 where mentor sees submissions and leaves feedback

- [ ] **Step 1: Replace Tab 3 stub in app.py**

Replace the Tab 3 stub block with:

```python
# ─── TAB 3: FEEDBACK ─────────────────────────────────────────────────────────
with tab3:
    st.header("Eingereichte Aufgaben")

    unreviewed = db.get_unreviewed_submissions()
    reviewed = db.get_all_reviewed_submissions()

    if unreviewed:
        st.subheader(f"Ausstehend ({len(unreviewed)})")
        for sub in unreviewed:
            ex_info = sub.get("exercises", {})
            with st.container(border=True):
                st.markdown(f"**{ex_info.get('topic', '')}** - {ex_info.get('exercise_type', '')}")
                st.caption(f"Eingereicht: {sub['submitted_at'][:10]}")

                with st.expander("Aufgabe anzeigen"):
                    st.json(ex_info.get("content", {}))

                with st.expander("Antwort von Antony"):
                    st.json(sub.get("answer", {}))

                if sub.get("claude_feedback"):
                    with st.expander("Claudes automatisches Feedback"):
                        st.markdown(sub["claude_feedback"])

                mentor_fb = st.text_area(
                    "Ihr Feedback:",
                    key=f"mentor_fb_{sub['id']}",
                    placeholder="Schreiben Sie hier Ihr personliches Feedback...",
                    height=150,
                )
                if st.button("Feedback senden", key=f"send_fb_{sub['id']}", type="primary"):
                    db.save_mentor_feedback(sub["id"], mentor_fb)
                    st.success("Feedback gespeichert!")
                    st.rerun()
    else:
        st.info("Keine ausstehenden Einreichungen.")

    if reviewed:
        st.divider()
        with st.expander(f"Archiv - bereits bewertet ({len(reviewed)})"):
            for sub in reviewed:
                ex_info = sub.get("exercises", {})
                st.markdown(f"**{ex_info.get('topic', '')}** | Bewertet: {sub.get('reviewed_at', '')[:10]}")
                if sub.get("mentor_feedback"):
                    st.markdown(f"Ihr Feedback: _{sub['mentor_feedback']}_")
                st.divider()
```

- [ ] **Step 2: Test Tab 3**

```bash
streamlit run app.py
```

Expected: Tab 3 shows unreviewed submissions. Write feedback, click "Feedback senden". Verify `mentor_feedback` and `reviewed_at` are updated in Supabase. Submission moves to archive on next refresh.

- [ ] **Step 3: Commit**

```bash
git add app.py
git commit -m "feat: Tab 3 - mentor feedback queue and review"
```

---

### Task 9: Tab 4 - "Fortschritt" (Progress and vocabulary)

**Files:**
- Modify: `german-trainer/app.py` - replace Tab 4 stub

**Interfaces:**
- Consumes: `db.get_error_stats()`, `db.get_vocabulary()`, `db.get_exercises()`
- Produces: working Tab 4 with error stats, vocabulary list, and activity counter

- [ ] **Step 1: Replace Tab 4 stub in app.py**

Replace the Tab 4 stub block with:

```python
# ─── TAB 4: FORTSCHRITT ──────────────────────────────────────────────────────
with tab4:
    st.header("Fortschritt")

    all_ex = db.get_exercises(None, None)
    reviewed_subs = db.get_all_reviewed_submissions()
    error_stats = db.get_error_stats()
    vocab = db.get_vocabulary()

    # Activity summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Aufgaben gesamt", len(all_ex))
    with col2:
        st.metric("Bewertet vom Mentor", len(reviewed_subs))
    with col3:
        briefe = [e for e in all_ex if e.get("exercise_type") == "Brief schreiben"]
        st.metric("Briefe geschrieben", len(briefe))

    st.divider()

    # Error stats by topic
    st.subheader("Fehler nach Thema")
    if error_stats:
        sorted_errors = sorted(error_stats.items(), key=lambda x: x[1], reverse=True)
        for topic_name, count in sorted_errors:
            st.markdown(f"**{topic_name}:** {count} Fehler")
            st.progress(min(count / max(error_stats.values()), 1.0))
    else:
        st.info("Noch keine Fehlerdaten vorhanden. Losen Sie Aufgaben und reichen Sie Antworten ein.")

    st.divider()

    # Vocabulary list
    st.subheader(f"Vokabelliste ({len(vocab)} Eintrage)")
    if vocab:
        for entry in vocab:
            with st.container(border=True):
                st.markdown(f"**{entry['word']}**")
                st.markdown(f"_{entry['definition']}_")
                st.caption(f"Beispiel: {entry['example']}")
    else:
        st.info("Noch keine Vokabeln gespeichert. Sie werden automatisch beim Erstellen von Aufgaben gesammelt.")
```

- [ ] **Step 2: Test Tab 4**

```bash
streamlit run app.py
```

Expected: Tab 4 shows exercise count, error stats (if any submissions exist), and vocabulary list pulled from Supabase.

- [ ] **Step 3: Run all tests one final time**

```bash
python -m pytest tests/ -v
```

Expected: all tests pass.

- [ ] **Step 4: Commit**

```bash
git add app.py
git commit -m "feat: Tab 4 - progress tracking, error stats, vocabulary list"
```

---

### Task 10: Deploy to Streamlit Cloud

**Files:**
- No code changes - deploy existing app

**Interfaces:**
- Produces: public URL accessible by mentor with no install

- [ ] **Step 1: Push to GitHub**

Go to https://github.com/CluefullConsultant and create a new repository called `german-trainer` (private or public, your choice).

```bash
git remote add origin https://github.com/CluefullConsultant/german-trainer.git
git push -u origin main
```

- [ ] **Step 2: Deploy on Streamlit Cloud**

Go to https://share.streamlit.io. Click "New app". Select the `german-trainer` repo, branch `main`, file `app.py`.

- [ ] **Step 3: Add secrets in Streamlit Cloud**

In the app's Settings > Secrets, paste:

```toml
ANTHROPIC_API_KEY = "sk-ant-..."
SUPABASE_URL = "https://xxxx.supabase.co"
SUPABASE_KEY = "eyJ..."
```

- [ ] **Step 4: Verify the live app**

Open the public URL. Create one exercise in Tab 1. Solve it in Tab 2. Check feedback appears. Send the URL to mentor and confirm he can open it with no setup.

- [ ] **Step 5: Final commit with live URL in README**

```bash
echo "# Deutsch Trainer\n\nLive: https://YOUR-APP.streamlit.app" > README.md
git add README.md
git commit -m "docs: add live URL to README"
git push
```
