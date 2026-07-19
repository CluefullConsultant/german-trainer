# German Trainer App - Design Spec
**Date:** 2026-06-30  
**Goal:** Replace mentor's paper printout workflow with a shared digital app. Mentor creates exercises with Claude's help; Antony solves them; both track progress toward C1.

---

## 1. Context

- **Learner:** Antony. Telc B2 written failed (56%). Target: C1 within 6 weeks.
- **Mentor:** Non-tech-savvy German man, lives in same house. Previously prepared paper printouts. Needs zero setup - just a URL.
- **Sessions:** Daily 45-minute live sessions (09:45-10:30). Speaking and listening exercises done live together, no recording needed.
- **Scope:** Full A1-C1 German grammar foundations, with immediate focus on B2 written gaps (connectors, separable verbs, Wechselprasitionen, timed letter writing).

---

## 2. Architecture

```
Streamlit App (single URL, one shared page)
├── Tab 1: "Aufgaben erstellen"  — mentor creates exercises via guided form + Claude
├── Tab 2: "Üben"               — Antony solves exercises, gets instant Claude feedback
├── Tab 3: "Feedback"           — mentor reviews submissions, adds human comments
└── Tab 4: "Fortschritt"        — shared progress view, error log, vocabulary list

Claude (Anthropic API)  — generates exercises, gives automated answer feedback
Supabase (free tier)    — persists exercises, submissions, feedback, vocabulary
Streamlit Cloud         — free hosting, mentor accesses via URL only
```

**No login, no passwords.** One URL, both mentor and Antony use all tabs.

---

## 3. Supabase Data Model

### `exercises`
| Column | Type | Notes |
|---|---|---|
| id | uuid | primary key |
| created_at | timestamp | auto |
| topic | text | see topic list below |
| exercise_type | text | see type list below |
| content | jsonb | exercise body (varies by type) |
| mentor_notes | text | optional extra context from mentor |

### `submissions`
| Column | Type | Notes |
|---|---|---|
| id | uuid | primary key |
| exercise_id | uuid | FK to exercises |
| submitted_at | timestamp | auto |
| answer | jsonb | Antony's answer |
| claude_feedback | text | automated feedback |
| mentor_feedback | text | mentor's human comment |
| reviewed_at | timestamp | set when mentor submits feedback |
| error_tags | text[] | e.g. ["Konnektoren-C", "Trennbare Verben"] |

### `vocabulary`
| Column | Type | Notes |
|---|---|---|
| id | uuid | primary key |
| word | text | |
| definition | text | German definition |
| example | text | example sentence from exercise |
| exercise_id | uuid | source exercise |
| added_at | timestamp | |

---

## 4. Exercise Topics (full A1-C1 scope)

Artikel & Genus, Deklination (Nominativ/Akkusativ/Dativ/Genitiv), Personalpronomina, Possessivartikel, Konnektoren (A/B/C Kategorien), Trennbare Verben, Wechselprasitionen, Konjunktiv II, Passiv (Vorgangs- und Zustandspassiv), Relativsatze, Wortstellung, Temporale Konjunktionen, Genitiv-Prasitionen, Partizipialkonstruktionen, Nominalisierung, Infinitiv mit zu, Schriftlicher Ausdruck (Brief), Leseverstehen, Horverstehen, Sprechaufgabe, Wortschatz in Kontext.

---

## 5. Exercise Types

| Type | Description |
|---|---|
| Luckentext | Fill-in-the-blank |
| Mehrfachauswahl | Multiple choice |
| Satztransformation | Rewrite/combine sentences |
| Fehlersuche | Find and correct the error |
| Ubersetzung | Translation (DE-EN or EN-DE) |
| Kategoriensortierung | Sort words into categories (e.g. connector groups) |
| Brief schreiben | Timed letter with Reihepunkte checklist |
| Leseverstehen | Paste a text, Claude generates comprehension questions |
| Horverstehen | Mentor reads aloud, pre-generated questions in app |
| Sprechaufgabe | Prompt shown, done live - no recording |

---

## 6. Tab Designs

### Tab 1: "Aufgaben erstellen" (Mentor)

Mentor sees a guided form - no blank chat box, no need to know how to prompt Claude.

**Form fields:**
- Thema (dropdown from topic list)
- Aufgabentyp (dropdown from type list)
- Zusatzliche Hinweise (optional free text, e.g. "obwohl vs trotzdem")

On submit: Claude generates the exercise using a structured system prompt that enforces correct German grammar pedagogy and the exercise format. Mentor sees a preview, can click "Neu generieren" or edit directly, then "Speichern".

Built-in helper text in simple German explains every field. Mentor never writes an exercise from scratch.

**For Leseverstehen:** extra field appears - "Text einfugen" - mentor pastes any German article/text. Claude generates comprehension questions at C1 level.

**For Horverstehen:** same as Leseverstehen but with a note: "Dieser Text wird von Ihnen vorgelesen. Die Fragen erscheinen fur Antony."

### Tab 2: "Uben" (Antony)

Exercise list with filters: Thema, Status (Neu / Bearbeitet / Feedback erhalten).

Each exercise card shows: topic badge, status indicator, preview line.

On opening an exercise:
- Exercise rendered based on type (blanks, choices, text area, timer for Brief)
- Brief schreiben: countdown timer shown, Reihepunkte checklist visible alongside
- Submit button sends answer to Supabase, triggers Claude feedback immediately
- Claude feedback shown inline - not just right/wrong, explains the grammar rule violated
- Status updates to "Beim Mentor" until mentor reviews

### Tab 3: "Feedback" (Mentor review queue)

List of unreviewed submissions, newest first. Each shows:
- Exercise title and type
- Antony's answer
- Claude's automated feedback (collapsed by default, expandable)
- Text box for mentor's own comment
- "Feedback senden" button

Reviewed submissions move to archive, visible via toggle.

### Tab 4: "Fortschritt"

- **Fehler-Log:** error rate per topic category, updated after each submission. Shows trend over time (e.g. "Konnektoren: 40% Fehler diese Woche vs 65% letzte Woche").
- **Vokabelliste:** running list of words pulled automatically from exercises by Claude. Each entry: word, German definition, example sentence, source exercise.
- **Aktivitat:** streak counter, exercises completed this week, letters written this week.
- Both mentor and Antony see identical data.

---

## 7. Claude Integration

### Exercise Generation Prompt (system)
Claude is instructed to:
- Generate exercises in correct pedagogical order (recognition before production)
- Format output as structured JSON matching the exercise type schema
- Include answer key and explanation for each item
- Flag the grammar rule being tested per item (for error tagging)
- Target B2-C1 production level, covering foundational grammar topics (Deklination, Artikel, etc.) as needed

### Answer Feedback Prompt
Claude receives: exercise content, correct answers, Antony's answer.
Claude returns:
- Per-item: correct/incorrect + specific rule explanation (not generic)
- Overall: which error category this falls under (for tagging)
- One targeted tip for the most common mistake in the submission

### Vocabulary Extraction
After each exercise is saved, Claude extracts 3-5 key vocabulary items from the text and saves them to the `vocabulary` table with German definitions and example sentences.

---

## 8. Stack

| Component | Choice | Reason |
|---|---|---|
| UI | Streamlit | Same pattern as existing tools, free deploy |
| LLM | Claude claude-sonnet-4-5 | Consistent with other tools |
| Database | Supabase (free tier) | Persistent, reliable, connects in ~10 lines |
| Hosting | Streamlit Cloud | Free, mentor gets a URL, no install |
| Language | Python | Consistent with existing tools |

**Key files (to be built):**
- `app.py` - Streamlit UI, 4 tabs
- `exercises.py` - Claude exercise generation logic, prompts
- `feedback.py` - Claude answer feedback logic
- `db.py` - Supabase client, all DB operations
- `vocabulary.py` - Claude vocabulary extraction

