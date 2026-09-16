# German Trainer — Project Context

*This is the app itself. For Antony's actual level, exam history, and coaching preferences, see `../CLAUDE.md`.*

## What this is

A Streamlit German-learning app with a Supabase database backend (`db.py`, `supabase_schema.sql`). ~6,300 lines across 14 files — a real built app, not a scaffold. **Used by multiple learners, not just Antony** — treat content and copy accordingly (no personal framing baked into the UI).

## Key files / tabs

| File | Role |
|---|---|
| `app.py` (939 lines) | Main Streamlit app, assembles all tabs |
| `grammar_theory.py` (4,198 lines) | **Theorie tab** — 78 grammar rules across CEFR levels A1-C1 (A1: 9, A2: 9, B1: 22, B2: 20, C1: 18), grouped into collapsible level sections, each with an inline quiz (`theory_quiz.py`) and an on-demand fresh example generator. Audited 16.09.2026 against a real telc sample exam and the complete Klett textbook set (B1.1, B1.2, B2.1, B2.2, C1.1, C1.2 — all six half-levels) — see the "Grammar content audit" note below. |
| `exercises.py`, `content_feed.py` | **Prüfungssimulation** — mirrors the real telc/Goethe exam structure (5 sections). `content_feed.py` also pulls live Deutsche Welle articles for the **Heute lernen** reading feature. |
| `verb_conjugator.py` | Full conjugation tables for every verb, every tense and mood — shown immediately, not behind nested expanders |
| `vocab_list.py`, `vocab_practice.py`, `vocabulary.py` | Vocabulary tracking and practice (currently 115 curated words — small relative to a full frequency-based A1-C1 sweep, flagged as a known gap) |
| `pronunciation.py` | German neural voice via Amazon Polly |
| `writing_topics.py` | Writing practice prompts (formal Brief, Geschäftliche E-Mail, Kurzbericht/Protokoll, informal message — good overlap with telc B2·C1 Beruf's actual task types) |
| `feedback.py` | Feedback handling — `generate_feedback`/`db.save_claude_feedback` exist but are **not wired into `app.py` anywhere** (confirmed by grep 16.09.2026, same gap first flagged 17.07.2026). Free-form answers don't get auto-corrected in the app; that correction loop currently has to happen outside it. |
| `theme.py` | Navy/blue reference-sheet visual theme, dark mode toggle |
| `db.py` / `supabase_schema.sql` | Supabase persistence layer |

**Removed 16.09.2026**: the Interview tab (`interview_coach.py`, `interview_content.py`, `interview_skeleton.py`) — its content was stale (last touched 19.07.2026, predated the current interview-prep standards) and out of scope for a shared learning tool. Interview coaching may return later as its own, freshly-scoped feature.

## Grammar content audit (16.09.2026)

The 63→78 rule count reflects a real, now-complete audit, not a guess: cross-checked against a telc Deutsch B2·C1 Beruf sample exam's actual Sprachbausteine content, and against the **full grammar table of contents of all six Klett half-level textbooks** (B1.1, B1.2, B2.1, B2.2, C1.1, C1.2 — the entire B1→C1 curriculum, Antony's own books). No official Goethe/telc source publishes a flat grammar checklist per level (confirmed by reading their actual Handbuch PDFs) — this audit method (real exam samples + real textbook curricula, all six half-levels + direct content review of existing rules) is the most rigorous free alternative to the paid academic reference ("Profile Deutsch") that the industry itself uses.

Confirmed gaps closed across two passes: Präsens/Perfekt formation (A1/A2, previously missing entirely), subjective/epistemic modal verbs, modal subordinate clauses (indem etc.), Nomen mit Präposition, Vergleichssätze mit als/wie, Relativsätze mit wer/wen/wem, Adjektivdeklination nach indefiniten Artikelwörtern, Modalitätsverben (haben...zu etc.), Infinitiv-Zeitverhältnis, Es als Platzhalter, Modales Partizip (Gerundiv), Satzstellung mit Infinitiv/Partizip II im Vorfeld, Ausklammerung, Vermutungen mit Futur I — plus two existing rules extended (irreale Konsekutivsätze added to the C1 Konnektoren rule, Relativsätze mit wo added to the B1 relative-clause rule). **No remaining known blind spots** in the B1-C1 range — every half-level book has been checked.

## Recent development (most recent first)

Grammar audit round 2: remaining textbooks (B1.1, B1.2, B2.1, C1.2) checked, 5 more rules added + 2 existing rules extended (73→78), no known blind spots left in B1-C1 → removed stale Interview tab → grammar content audit round 1, 10 new rules added closing confirmed gaps (63→73) → *(uncommitted, pre-existing when this audit happened)* Vokabeln tab added, Deutsche Welle article reading feature added to Heute lernen, quiz answer-shuffling added (fixes positional-shortcut exploit), quiz JSON error handling improved → dark mode toggle → hide Streamlit dev/cloud toolbar for viewers → Amazon Polly pronunciation → collapsible Theorie level sections → navy/blue theme → full verb conjugation tables shown immediately → removed Üben tab (merged into other tabs) → added Grundlagen tab → completed grammar coverage to 58 rules, fixed accuracy issues → fixed Theorie tab rendering (was breaking under DOM weight of 38+ rules always rendered) → curriculum audit (added missing lessons, fixed 2 CEFR level misplacements) → added Prüfungssimulation mode mirroring the real exam structure → integrated career-ops interview-prep content into the Interview tab (later removed, see above).

## Known gaps (as of 16.09.2026, being worked through)

- Vocab list is small (115 words) relative to a real frequency-based A1-C1 sweep — planned expansion, plus a daily-rotation structure and idioms/sayings.
- No standalone Reading tab (currently folded into Heute lernen, DW-only) or Listening tab (no audio/podcast content at all — "Hörverstehen" exercises are text read aloud by a human, not real listening material).
- Feedback/mistake-tracking loop not wired up (see `feedback.py` above) — planned to become an analytics layer surfacing common errors, not per-exercise auto-grading.

## Stack

Python, Streamlit, Supabase (Postgres), Amazon Polly (pronunciation).

## Local dev

`.streamlit/secrets.toml` holds local secrets (not committed). Run with `streamlit run app.py`.
