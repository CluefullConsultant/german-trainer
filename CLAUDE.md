# German Trainer — Project Context

*This is the app itself. For Antony's actual level, exam history, and coaching preferences, see `../CLAUDE.md`.*

## What this is

A Streamlit German-learning app with a Supabase database backend (`db.py`, `supabase_schema.sql`). **Used by multiple learners, not just Antony** — treat content and copy accordingly (no personal framing baked into the UI).

**Mid-redesign as of 16.09.2026** — read the "Redesign roadmap" section below before doing anything; it says exactly what's done and what's next.

## Key files / tabs (current, post-redesign-step-1-and-2)

| File | Role |
|---|---|
| `app.py` | Main Streamlit app, assembles all tabs. Current tabs, in order: **Grammatik, Korrektur, Lesen, Hören, Vokabeln** (5 tabs — `Aufgaben erstellen` and the old separate `Theorie`/`Grundlagen` split are both gone, see below). |
| `grammar_theory.py` (4,198 lines) | **Grammatik tab** — 78 grammar rules across CEFR levels A1-C1 (A1: 9, A2: 9, B1: 22, B2: 20, C1: 18). Theorie and Grundlagen were merged into this one tab 16.09.2026 (no more artificial split); the verb conjugator (`render_verb_conjugator_tool`) is embedded at the top of the same tab. Audited against a real telc sample exam and the complete Klett textbook set (B1.1, B1.2, B2.1, B2.2, C1.1, C1.2 — all six half-levels, Antony's own books) — see "Grammar content audit" below. |
| `theory_quiz.py` | Powers the "Kurztest generieren" button under each rule in Grammatik. Answer-position shuffling already in place. **16.09.2026: prompt strengthened** (uncommitted as of this writing — see "Pending, not yet committed" below) to fix real user feedback: quiz questions were clustering on the same sub-case back-to-back (e.g. multiple Akkusativ questions in a row) and answer options were structurally too similar/guessable. |
| `content_feed.py` | Powers **Lesen** (real C1-density RSS: Zeit, Spiegel, Handelsblatt, WirtschaftsWoche — `LESEN_SOURCES`, `fetch_lesen_articles`) and **Hören** (real native-speed podcast RSS: Deutschlandfunk "Der Tag", Lage der Nation, Easy German Podcast, Handelsblatt Audio — `HOEREN_SOURCES`, `fetch_hoeren_episodes`). DW learner-level feed retired 16.09.2026. |
| `sentence_correction.py` | Powers **Korrektur** (new 16.09.2026) — free-form German text box (informal/incomplete register explicitly allowed, not "corrected away"), returns a corrected version plus a per-mistake list (original → correction, one-line reason). Standalone, no DB write — not wired into the `db.save_claude_feedback`/`get_top_errors` mistake-tracking system since that needs an exercise/submission row per the current schema; a good hook point for roadmap step 7 (feedback rebuild) rather than something to force in now. |
| `verb_conjugator.py` | Full conjugation tables for every verb, every tense and mood |
| `vocab_list.py`, `vocab_practice.py`, `vocabulary.py` | Vocabulary tracking and practice (currently 115 curated words — small relative to a full frequency-based A1-C1 sweep; a real 2,833-word frequency source now exists at `../drills/goethe-b1-wortliste.txt` + `../drills/vokabel-tagesplan.md`, not yet wired into this app) |
| `pronunciation.py` | German neural voice via Amazon Polly |
| `writing_topics.py` | Writing practice prompts (formal Brief, Geschäftliche E-Mail, Kurzbericht/Protokoll, informal message) — not yet surfaced in its own tab, still buried/underused |
| `feedback.py` | `generate_feedback`/`db.save_claude_feedback` exist but are **not wired into `app.py` anywhere** — free-form answers don't get auto-corrected in the app |
| `theme.py` | Navy/blue reference-sheet visual theme, dark mode toggle — **not yet redesigned**, this is the "Phase 2" visual overhaul, still pending |
| `db.py` / `supabase_schema.sql` | Supabase persistence layer |

**Removed 16.09.2026**: the Interview tab (`interview_coach.py`, `interview_content.py`, `interview_skeleton.py` — stale, predated current interview-prep standards) and the **Aufgaben erstellen** tab (`exercises.py` + its test, `render_exercise()` — user feedback: unused, and redundant with the Kurztest button already in Grammatik once that's fixed properly, rather than confusing overlap).

## Redesign roadmap — READ THIS FIRST in a new session

Full target tab structure, agreed 16.09.2026: **Grammatik | Lesen | Hören | Schreiben | Sprechen | Vokabeln**. Actual current order (also 16.09.2026, user-directed): **Grammatik | Korrektur | Lesen | Hören | Vokabeln** — Grammatik moved to first, and a **Korrektur** tab (sentence-correction tool, not in the original 6-tab plan — see table above) was added second. Slot Schreiben/Sprechen in wherever makes sense relative to Korrektur when they're built, no fixed position agreed yet. Status:

1. ✅ **Merge Theorie+Grundlagen → Grammatik**, embed verb conjugator — done, committed, pushed, verified live in browser.
2. ✅ **Retire Aufgaben erstellen entirely** (not folded into Grammatik — user explicitly rejected that, wanted it gone since Grammatik's own Kurztest button already covers the need) — done, committed, pushed.
3. ✅ **Split Heute lernen → Lesen tab.** Done, committed (`14fcdc7`), pushed, verified live in browser 16.09.2026. Real RSS sources wired into `content_feed.LESEN_SOURCES`: Zeit, Spiegel, Handelsblatt (Schlagzeilen/Politik/Unternehmen/Finanzen/Technologie/Marktberichte), WirtschaftsWoche (same 6 rubrics). **Correction to the original note**: Handelsblatt/WiWo sub-rubric feeds do NOT sit under `/schlagzeilen/politik` etc. — the working pattern is `https://feeds.cms.handelsblatt.com/politik` and `https://feeds.cms.wiwo.de/rss/politik` (no `schlagzeilen` segment); the old guessed URLs all 404. Bonus unused feed found: `https://feeds.cms.handelsblatt.com/anlagestrategie` (investment-strategy news, not yet added as a rubric).
4. ✅ **Build Hören.** Done, verified live in browser 16.09.2026. `content_feed.HOEREN_SOURCES` + `fetch_hoeren_episodes` wired into a Lesen-style tab (source picker → episode list → detail with `st.audio` player). Verified real RSS+enclosure URLs: Deutschlandfunk "Der Tag" `https://www.deutschlandfunk.de/podcast-104.xml` (found via its `sophoraId`, not discoverable from the show's own page HTML), Lage der Nation `https://feeds.lagedernation.org/feeds/ldn-mp3.xml` (also exposes a `podcast:transcript` VTT URL per episode — not yet used for question generation, a future upgrade), Easy German Podcast `https://podcast.easygerman.org/rss`. **Handelsblatt Audio** `https://feeds.cms.handelsblatt.com/podcast` has no real audio enclosure (its `<enclosure>` is just the cover image) — the UI falls back to an "extern anhören" link for it instead of an embedded player; this is a feed limitation, not a bug. Researched but explicitly did NOT add: generic listicle podcasts (Slow German, Coffee Break German) — those are learner-paced, contradicting the plan's native-speed requirement; "Deutsch mit Schmidt" — no working RSS found in one search pass, worth another look later.
5. ⬜ **Build Schreiben** (new tab, surface `writing_topics.py` properly + the telc-format task types from `../German_C1_Intensive_Plan.md` §5: informal/formal email, Diskussionsvorlage). Not started.
6. ⬜ **Scope + build Sprechen** (new, modest scope — pronunciation + shadowing, this app can't do live conversation practice). Not started.
7. ⬜ **Feedback → mistake-tracking rebuild** (`feedback.py`, dynamic per-user, not hardcoded — this is also where a "priorities" view of a user's actual weak points should live, NOT hardcoded into Grammatik). Not started.
8. ⬜ **Branding copy for Feldmark/Ausländer audience.** Not started.
9. ⬜ **Visual redesign** (Phase 2 — the actual "unique, revolutionary look" that was the original headline ask). Nothing done here yet at all.

## Pending, not yet committed (as of this writing)

- `theory_quiz.py` — the quiz-variation prompt fix (see table above). Syntax-verified, not yet committed/pushed. Ask before committing (standing workflow: commit only when told to, then push separately with confirmation since it redeploys the live app).
- `app.py` + `content_feed.py` — roadmap steps 3 (Lesen) and 4 (Hören), both syntax-verified and confirmed live in browser 16.09.2026. Not yet committed/pushed — same standing workflow applies.

## Grammar content audit (16.09.2026)

The 63→78 rule count reflects a real, complete audit: cross-checked against a telc Deutsch B2·C1 Beruf sample exam's actual Sprachbausteine content, and against the full grammar table of contents of all six Klett half-level textbooks (B1.1, B1.2, B2.1, B2.2, C1.1, C1.2). No official Goethe/telc source publishes a flat grammar checklist per level (confirmed by reading their actual Handbuch PDFs) — this audit method is the most rigorous free alternative to the paid academic reference ("Profile Deutsch") the industry itself uses. Confirmed gaps closed across two passes: Präsens/Perfekt formation, subjective/epistemic modal verbs, modal subordinate clauses (indem etc.), Nomen mit Präposition, Vergleichssätze mit als/wie, Relativsätze mit wer/wen/wem, Adjektivdeklination nach indefiniten Artikelwörtern, Modalitätsverben, Infinitiv-Zeitverhältnis, Es als Platzhalter, Modales Partizip (Gerundiv), Satzstellung mit Infinitiv/Partizip II im Vorfeld, Ausklammerung, Vermutungen mit Futur I. **No remaining known blind spots** in B1-C1.

## Stack

Python, Streamlit, Supabase (Postgres), Amazon Polly (pronunciation).

## Local dev

`.streamlit/secrets.toml` holds local secrets (not committed, never read/edit this file without a specific reason). Run with `python -m streamlit run app.py` (plain `streamlit` command may not be on PATH). To verify UI changes, launch it and check in a real browser (Chrome MCP tools) rather than trusting syntax checks alone — Streamlit tab/button clicks sometimes need `ref`-based clicks (via `read_page`) rather than raw coordinates to register correctly.
