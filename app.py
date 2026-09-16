# app.py
import streamlit as st
import vocabulary
import db
import vocab_practice
import content_feed
import theory_quiz
import verb_conjugator
import theme
import pronunciation
import sentence_correction


def render_pronunciation_button(text: str, key: str):
    """Small inline button that plays back German audio for the given text via Amazon Polly."""
    if st.button("🔊", key=f"pron_{key}", help=f"'{text}' anhören"):
        with st.spinner("Audio wird geladen..."):
            try:
                audio_bytes = pronunciation.synthesize_speech(text)
                st.audio(audio_bytes, format="audio/mp3", autoplay=True)
            except Exception as e:
                st.error(f"Aussprache konnte nicht geladen werden: {e}")


def render_grammar_rule(rule):
    """Render a single grammar_theory.py rule: explanation, examples, mistakes, quiz."""
    rid = rule["id"]

    st.divider()
    st.subheader(rule["title"])

    st.markdown(rule["explanation"])

    if rule.get("examples"):
        st.markdown("---")
        st.markdown("**Beispiele:**")
        for i, ex in enumerate(rule["examples"]):
            st.markdown(f"**{ex['label']}**")
            sent_col, audio_col = st.columns([9, 1])
            with sent_col:
                st.markdown(f"> {ex['sentence']}")
            with audio_col:
                render_pronunciation_button(ex["sentence"].replace("*", ""), key=f"{rid}_ex_{i}")
            if ex.get("note"):
                st.caption(ex["note"])

    extra_key = f"extra_examples_{rid}"
    if st.session_state.get(extra_key):
        st.markdown("**Weitere Beispiele:**")
        for ex in st.session_state[extra_key]:
            st.markdown(f"**{ex.get('label', '')}**")
            st.markdown(f"> {ex.get('sentence', '')}")
            if ex.get("note"):
                st.caption(ex["note"])

    if st.button("Weitere Beispiele generieren", key=f"more_ex_{rid}"):
        with st.spinner("Claude erstellt neue Beispiele..."):
            st.session_state[extra_key] = theory_quiz.generate_more_examples(
                rule["title"], rule["explanation"], rule["level"]
            )
            st.rerun()

    if rule.get("mistakes"):
        st.markdown("---")
        st.markdown("**Häufige Fehler:**")
        for m in rule["mistakes"]:
            st.markdown(f"- {m}")

    if rule.get("exercise_hint"):
        st.markdown("---")
        st.info(f"**Übungsvorschlag für Horst:** {rule['exercise_hint']}")

    st.markdown("---")
    st.markdown("**Kurztest zu dieser Regel**")
    quiz_key = f"quiz_{rid}"
    if st.button("Kurztest generieren", key=f"gen_quiz_{rid}"):
        with st.spinner("Claude erstellt einen Test..."):
            try:
                st.session_state[quiz_key] = theory_quiz.generate_quiz(
                    rule["title"], rule["explanation"], rule["level"]
                )
                st.session_state[f"{quiz_key}_submitted"] = False
                st.rerun()
            except Exception as e:
                st.error(f"Fehler bei der Testgenerierung: {e}")

    if st.session_state.get(quiz_key):
        quiz = st.session_state[quiz_key]
        quiz_answers = []
        diff_labels = {"leicht": "🟢 leicht", "mittel": "🟡 mittel", "schwer": "🔴 schwer"}
        for qi, item in enumerate(quiz):
            diff = diff_labels.get(item.get("schwierigkeit", ""), "")
            st.markdown(f"**{qi+1}. {item.get('frage', '')}** {diff}")
            choice = st.radio(
                "Antwort",
                options=item.get("optionen", []),
                key=f"{quiz_key}_q{qi}",
                index=None,
                label_visibility="collapsed",
            )
            quiz_answers.append(choice)

        if st.button("Test auswerten", key=f"submit_{quiz_key}"):
            st.session_state[f"{quiz_key}_submitted"] = True
            st.rerun()

        if st.session_state.get(f"{quiz_key}_submitted"):
            correct_count = 0
            for qi, item in enumerate(quiz):
                options = item.get("optionen", [])
                correct_idx = item.get("richtig_index", 0)
                correct_answer = options[correct_idx] if correct_idx < len(options) else ""
                given = quiz_answers[qi]
                if given == correct_answer:
                    correct_count += 1
                    st.success(f"{qi+1}. Richtig - {item.get('erklaerung', '')}")
                else:
                    st.error(f"{qi+1}. Falsch. Richtig wäre: {correct_answer} - {item.get('erklaerung', '')}")
            st.metric("Ergebnis", f"{correct_count} / {len(quiz)}")


def render_verb_conjugator_tool():
    """Render the on-demand full verb conjugation expander - mirrors a standard Flexionstabelle
    (Indikativ, Konjunktiv I/II, Imperativ, Partizip Präsens/Perfekt)."""
    with st.expander("Vollständige Verbkonjugation - jedes Verb in jeder Zeit und jedem Modus"):
        st.caption("Indikativ (6 Zeiten), Konjunktiv I (inkl. Futur), Konjunktiv II, Imperativ, Partizip Präsens/Perfekt.")

        st.markdown("**Schnellauswahl - die wichtigsten Verben:**")
        chip_cols = st.columns(6)
        for i, v in enumerate(verb_conjugator.WICHTIGE_VERBEN):
            with chip_cols[i % 6]:
                if st.button(v, key=f"verb_chip_{v}"):
                    st.session_state["conjugator_verb_input"] = v
                    with st.spinner(f"Claude konjugiert '{v}'..."):
                        st.session_state["conjugation_result"] = verb_conjugator.generate_full_conjugation(v)
                    st.rerun()

        verb_input = st.text_input(
            "Oder ein anderes Verb eingeben (Infinitiv)",
            value=st.session_state.get("conjugator_verb_input", ""),
            placeholder="z.B. sprechen, gehen, denken...",
        )
        if st.button("Volle Konjugation anzeigen", type="primary") and verb_input.strip():
            with st.spinner("Claude konjugiert..."):
                st.session_state["conjugation_result"] = verb_conjugator.generate_full_conjugation(verb_input.strip())

        if st.session_state.get("conjugation_result"):
            data = st.session_state["conjugation_result"]
            sf = data.get("stammformen", {})
            st.markdown(f"### {data.get('verb', verb_input)}")
            st.caption(
                f"Infinitiv: {sf.get('infinitiv', '')} | Präteritum (er/sie): {sf.get('praeteritum_3', '')} | "
                f"Partizip II: {sf.get('partizip2', '')} | Hilfsverb: {sf.get('hilfsverb', '')}"
            )

            def _render_tense_grid(tense_group, columns):
                """One table: rows = persons, columns = the given (key, label) tenses. Shows immediately, no clicks."""
                header = "| Person | " + " | ".join(label for _, label in columns) + " |\n"
                header += "|---|" + "---|" * len(columns) + "\n"
                rows = header
                for p in verb_conjugator.PERSON_ORDER:
                    cells = [tense_group.get(key, {}).get(p, "") for key, _ in columns]
                    rows += f"| {verb_conjugator.PERSON_LABELS[p]} | " + " | ".join(cells) + " |\n"
                st.markdown(rows)

            st.markdown("**Indikativ**")
            _render_tense_grid(data.get("indikativ", {}), [
                ("praesens", "Präsens"), ("praeteritum", "Präteritum"), ("perfekt", "Perfekt"),
                ("plusquamperfekt", "Plusquamperfekt"), ("futur1", "Futur I"), ("futur2", "Futur II"),
            ])

            st.markdown("**Konjunktiv I**")
            _render_tense_grid(data.get("konjunktiv1", {}), [
                ("praesens", "Präsens"), ("perfekt", "Perfekt"), ("futur1", "Futur I"), ("futur2", "Futur II"),
            ])

            st.markdown("**Konjunktiv II**")
            _render_tense_grid(data.get("konjunktiv2", {}), [
                ("praeteritum", "Präteritum"), ("plusquamperfekt", "Plusquamperfekt"),
            ])

            st.markdown("**Imperativ**")
            imp = data.get("imperativ", {})
            if imp.get("hat_imperativ", True):
                st.markdown(f"- du: **{imp.get('du', '')}**")
                st.markdown(f"- ihr: **{imp.get('ihr', '')}**")
                st.markdown(f"- Sie: **{imp.get('Sie', '')}**")
            else:
                st.caption("Dieses Verb hat keinen gebräuchlichen Imperativ (z.B. Modalverben).")

            st.markdown("**Unpersönliche Formen**")
            st.markdown(f"- Partizip Präsens: **{data.get('partizip_praesens', '')}**")
            st.markdown(f"- Partizip Perfekt: **{sf.get('partizip2', '')}**")


st.set_page_config(page_title="Deutsch Trainer", page_icon="", layout="wide")

if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False
theme.inject_custom_theme(dark=st.session_state["dark_mode"])

title_col, toggle_col = st.columns([6, 1])
with title_col:
    st.title("Deutsch Trainer")
with toggle_col:
    st.toggle("🌙 Dunkel", key="dark_mode")

try:
    top_errors = db.get_top_errors(3)
    if top_errors:
        st.warning(
            "**Häufigste Fehler:** " +
            " | ".join([f"{e['tag']} ({e['count']}x)" for e in top_errors])
        )
except Exception:
    pass

tab5, tab_korrektur, tab_lesen, tab_hoeren, tab_vocab = st.tabs([
    "Grammatik",
    "Korrektur",
    "Lesen",
    "Hören",
    "Vokabeln",
])

# --- TAB KORREKTUR ---
with tab_korrektur:
    st.header("Korrektur")
    st.caption("Schreib deine eigenen Sätze auf Deutsch - locker, unvollständig, wie du willst. Du bekommst die korrigierte Version und jeden Fehler einzeln erklärt.")

    korrektur_input = st.text_area(
        "Dein Text",
        key="korrektur_input",
        height=150,
        placeholder="z.B. Ich denke das ich morgen zu Termin gehen muss, aber ich bin nicht sicher ob ich Zeit habe...",
    )

    if st.button("Korrigieren", type="primary", disabled=not korrektur_input.strip()):
        with st.spinner("Claude prüft deinen Text..."):
            st.session_state["korrektur_result"] = sentence_correction.correct_sentences(korrektur_input)
            st.rerun()

    if st.session_state.get("korrektur_result"):
        result = st.session_state["korrektur_result"]

        st.markdown("---")
        st.subheader("Korrigierte Version")
        st.caption("Zum Kopieren: Maus über den Text, Symbol oben rechts klicken.")
        st.code(result["corrected"], language=None, wrap_lines=True)

        mistakes = result.get("mistakes", [])
        if mistakes:
            st.subheader(f"Fehler im Detail ({len(mistakes)})")
            for m in mistakes:
                line = f"**{m.get('original', '')}** → **{m.get('correction', '')}**"
                if m.get("reason"):
                    line += f"  \n_{m['reason']}_"
                st.markdown(line)
                st.divider()
        else:
            st.success("Keine Fehler gefunden!")

# --- TAB LESEN ---
with tab_lesen:
    st.header("Lesen")
    st.caption("Echte C1-Texte aus der deutschen Presse, keine Lernvereinfachung.")

    source_col, category_col = st.columns(2)
    with source_col:
        source = st.selectbox("Quelle", options=list(content_feed.LESEN_SOURCES.keys()), key="lesen_source")
    with category_col:
        category = st.selectbox("Rubrik", options=list(content_feed.LESEN_SOURCES[source].keys()), key="lesen_category")

    feed_url = content_feed.LESEN_SOURCES[source][category]
    feed_key = f"{source}:{category}"

    if st.session_state.get("lesen_feed_key") != feed_key:
        with st.spinner("Artikel werden geladen..."):
            st.session_state["lesen_articles"] = content_feed.fetch_lesen_articles(feed_url)
            st.session_state["lesen_feed_key"] = feed_key
            st.session_state["lesen_selected"] = None
            st.session_state["lesen_questions"] = []
            st.session_state["lesen_answers"] = {}
            st.session_state["lesen_tandem_prompts"] = []

    articles = st.session_state.get("lesen_articles", [])

    if not articles:
        st.warning("Keine Artikel gefunden. Bitte Internetverbindung prüfen oder andere Quelle/Rubrik wählen.")
    else:
        if st.session_state.get("lesen_selected") is None:
            st.markdown("**Artikel auswählen**")
            for i, article in enumerate(articles):
                with st.container(border=True):
                    c1, c2 = st.columns([4, 1])
                    with c1:
                        st.markdown(f"**{article['title']}**")
                        st.caption(article['description'][:150] + "..." if len(article['description']) > 150 else article['description'])
                    with c2:
                        if st.button("Lesen", key=f"lesen_{i}"):
                            st.session_state["lesen_selected"] = i
                            st.session_state["lesen_questions"] = []
                            st.session_state["lesen_answers"] = {}
                            st.session_state["lesen_tandem_prompts"] = []
                            st.rerun()
            if st.button("Neue Artikel laden"):
                del st.session_state["lesen_feed_key"]
                st.rerun()
        else:
            article = articles[st.session_state["lesen_selected"]]
            if st.button("Zurück zur Artikelliste"):
                st.session_state["lesen_selected"] = None
                st.rerun()

            st.subheader(article["title"])
            if article.get("link"):
                st.caption(f"Quelle: {source} | [Artikel öffnen]({article['link']})")
            st.markdown(article["description"])

            st.divider()

            dcol1, dcol2 = st.columns(2)
            with dcol1:
                if st.button("Verständnisfragen generieren", type="primary"):
                    with st.spinner("Claude erstellt Fragen..."):
                        st.session_state["lesen_questions"] = content_feed.generate_questions_from_article(
                            article["title"], article["description"]
                        )
                        st.session_state["lesen_answers"] = {}
                        st.rerun()
            with dcol2:
                if st.button("Vokabeln speichern"):
                    with st.spinner("Vokabeln werden extrahiert..."):
                        words = content_feed.extract_vocab_from_article(article["description"])
                        if words:
                            db.save_vocabulary(words, None)
                            st.success(f"{len(words)} Vokabeln gespeichert!")
                        else:
                            st.warning("Keine Vokabeln gefunden.")

            if st.button("Tandem-Vorbereitung", key="lesen_tandem_prep"):
                with st.spinner("Gesprächsanlässe werden erstellt..."):
                    prompts = content_feed.generate_tandem_prompts(
                        article["title"], article["description"]
                    )
                    st.session_state["lesen_tandem_prompts"] = prompts
                    st.rerun()

            if st.session_state.get("lesen_tandem_prompts"):
                st.subheader("Tandem-Gesprächsanlässe")
                st.caption("Bereiten Sie sich auf diese Fragen für Ihr Tandem-Gespräch vor.")
                for i, prompt in enumerate(st.session_state["lesen_tandem_prompts"]):
                    st.markdown(f"**{i+1}.** {prompt}")

            if st.session_state.get("lesen_questions"):
                st.subheader("Verständnisfragen")
                for i, q in enumerate(st.session_state["lesen_questions"]):
                    st.markdown(f"**{i+1}. {q['question']}**")
                    answer = st.text_area("Ihre Antwort:", key=f"lesen_ans_{i}", height=80)
                    if answer:
                        st.session_state["lesen_answers"][i] = answer

                if st.session_state["lesen_answers"] and st.button("Antworten prüfen", type="primary"):
                    for i, q in enumerate(st.session_state["lesen_questions"]):
                        user_ans = st.session_state["lesen_answers"].get(i, "")
                        if user_ans:
                            st.markdown(f"**Frage {i+1}:** Musterlösung: _{q['answer']}_")

# --- TAB HÖREN ---
with tab_hoeren:
    st.header("Hören")
    st.caption("Echte Podcasts in Originalgeschwindigkeit - für Hörverständnis und Shadowing.")

    hoeren_source = st.selectbox("Quelle", options=list(content_feed.HOEREN_SOURCES.keys()), key="hoeren_source")
    hoeren_url = content_feed.HOEREN_SOURCES[hoeren_source]

    if st.session_state.get("hoeren_feed_key") != hoeren_source:
        with st.spinner("Episoden werden geladen..."):
            st.session_state["hoeren_episodes"] = content_feed.fetch_hoeren_episodes(hoeren_url)
            st.session_state["hoeren_feed_key"] = hoeren_source
            st.session_state["hoeren_selected"] = None
            st.session_state["hoeren_questions"] = []
            st.session_state["hoeren_answers"] = {}
            st.session_state["hoeren_tandem_prompts"] = []

    episodes = st.session_state.get("hoeren_episodes", [])

    if not episodes:
        st.warning("Keine Episoden gefunden. Bitte Internetverbindung prüfen oder andere Quelle wählen.")
    else:
        if st.session_state.get("hoeren_selected") is None:
            st.markdown("**Episode auswählen**")
            for i, ep in enumerate(episodes):
                with st.container(border=True):
                    c1, c2 = st.columns([4, 1])
                    with c1:
                        st.markdown(f"**{ep['title']}**" + (f"  ⏱ {ep['duration']}" if ep.get("duration") else ""))
                        st.caption(ep['description'][:150] + "..." if len(ep['description']) > 150 else ep['description'])
                    with c2:
                        if st.button("Hören", key=f"hoeren_{i}"):
                            st.session_state["hoeren_selected"] = i
                            st.session_state["hoeren_questions"] = []
                            st.session_state["hoeren_answers"] = {}
                            st.session_state["hoeren_tandem_prompts"] = []
                            st.rerun()
            if st.button("Neue Episoden laden"):
                del st.session_state["hoeren_feed_key"]
                st.rerun()
        else:
            ep = episodes[st.session_state["hoeren_selected"]]
            if st.button("Zurück zur Episodenliste"):
                st.session_state["hoeren_selected"] = None
                st.rerun()

            st.subheader(ep["title"])
            meta = f"Quelle: {hoeren_source}"
            if ep.get("duration"):
                meta += f" | Dauer: {ep['duration']}"
            st.caption(meta)
            st.markdown(ep["description"])

            if ep.get("audio_url"):
                st.audio(ep["audio_url"])
            elif ep.get("link"):
                st.info(f"Kein eingebetteter Player für diese Quelle - [Episode extern anhören]({ep['link']})")

            if ep.get("transcript_url"):
                st.caption(f"[Transkript verfügbar]({ep['transcript_url']})")

            st.divider()

            dcol1, dcol2 = st.columns(2)
            with dcol1:
                if st.button("Verständnisfragen generieren", type="primary", key="hoeren_gen_q"):
                    with st.spinner("Claude erstellt Fragen..."):
                        st.session_state["hoeren_questions"] = content_feed.generate_questions_from_article(
                            ep["title"], ep["description"]
                        )
                        st.session_state["hoeren_answers"] = {}
                        st.rerun()
            with dcol2:
                if st.button("Vokabeln speichern", key="hoeren_save_vocab"):
                    with st.spinner("Vokabeln werden extrahiert..."):
                        words = content_feed.extract_vocab_from_article(ep["description"])
                        if words:
                            db.save_vocabulary(words, None)
                            st.success(f"{len(words)} Vokabeln gespeichert!")
                        else:
                            st.warning("Keine Vokabeln gefunden.")

            if st.button("Tandem-Vorbereitung", key="hoeren_tandem_prep"):
                with st.spinner("Gesprächsanlässe werden erstellt..."):
                    prompts = content_feed.generate_tandem_prompts(ep["title"], ep["description"])
                    st.session_state["hoeren_tandem_prompts"] = prompts
                    st.rerun()

            if st.session_state.get("hoeren_tandem_prompts"):
                st.subheader("Tandem-Gesprächsanlässe")
                st.caption("Bereiten Sie sich auf diese Fragen für Ihr Tandem-Gespräch vor.")
                for i, prompt in enumerate(st.session_state["hoeren_tandem_prompts"]):
                    st.markdown(f"**{i+1}.** {prompt}")

            if st.session_state.get("hoeren_questions"):
                st.subheader("Verständnisfragen")
                for i, q in enumerate(st.session_state["hoeren_questions"]):
                    st.markdown(f"**{i+1}. {q['question']}**")
                    answer = st.text_area("Ihre Antwort:", key=f"hoeren_ans_{i}", height=80)
                    if answer:
                        st.session_state["hoeren_answers"][i] = answer

                if st.session_state["hoeren_answers"] and st.button("Antworten prüfen", type="primary", key="hoeren_check"):
                    for i, q in enumerate(st.session_state["hoeren_questions"]):
                        user_ans = st.session_state["hoeren_answers"].get(i, "")
                        if user_ans:
                            st.markdown(f"**Frage {i+1}:** Musterlösung: _{q['answer']}_")

# --- TAB VOKABELN ---
with tab_vocab:
    st.header("Vokabeln")

    st.subheader("Neue Wörter für heute")
    if st.button("Neue Wörter für heute", type="primary"):
        with st.spinner("Claude wählt neue Wörter für Sie aus..."):
            existing = [v["word"] for v in db.get_vocabulary()]
            new_words = content_feed.generate_daily_vocab(existing)
            if new_words:
                to_save = [{"word": w["word"], "definition": w["definition"], "example": w["example"]} for w in new_words]
                db.save_vocabulary(to_save, None)
                st.session_state["daily_vocab_preview"] = new_words
                st.rerun()
            else:
                st.warning("Wörter konnten nicht generiert werden.")

    if st.session_state.get("daily_vocab_preview"):
        words = st.session_state["daily_vocab_preview"]
        verbs = [w for w in words if w.get("is_verb")]
        nouns = [w for w in words if not w.get("is_verb")]

        context_badge = {"beruflich": "💼", "alltäglich": "🏙️"}
        level_badge = {"A1": "🟢", "A2": "🟢", "B1": "🟡", "B2": "🟠", "C1": "🔴"}

        with st.expander("Neue Wörter von heute", expanded=True):
            for wi, w in enumerate(nouns + verbs):
                word_col, audio_col = st.columns([9, 1])
                with word_col:
                    st.markdown(f"**{w['word']}** {level_badge.get(w.get('level', ''), '')}{context_badge.get(w.get('context', ''), '')}")
                with audio_col:
                    render_pronunciation_button(w['word'], key=f"daily_vocab_{wi}")
                st.caption(w['definition'])
                st.caption(f"_{w['example']}_")
                st.divider()

    st.markdown("---")
    st.subheader("Vokabeln üben")
    due_words = db.get_due_vocabulary()

    if not due_words:
        st.success("Keine fälligen Vokabeln!")
    else:
        st.caption(f"{len(due_words)} fällig")

        if "vocab_practice_index" not in st.session_state:
            st.session_state["vocab_practice_index"] = 0
        if "vocab_feedback" not in st.session_state:
            st.session_state["vocab_feedback"] = None

        idx = st.session_state["vocab_practice_index"]
        if idx >= len(due_words):
            st.success("Alle fälligen Vokabeln geübt!")
            if st.button("Neu starten"):
                st.session_state["vocab_practice_index"] = 0
                st.session_state["vocab_feedback"] = None
                st.rerun()
        else:
            word = due_words[idx]
            with st.container(border=True):
                word_col, audio_col = st.columns([9, 1])
                with word_col:
                    st.markdown(f"**{word['word']}**")
                with audio_col:
                    render_pronunciation_button(word['word'], key=f"practice_vocab_{idx}")
                st.caption(word['definition'])
                st.caption(f"Beispiel: {word['example']}")

                user_sentence = st.text_input(
                    "Eigener Satz:",
                    key=f"vocab_sentence_{idx}",
                    placeholder=f"Satz mit '{word['word']}'..."
                )

                bcol1, bcol2 = st.columns(2)
                with bcol1:
                    if st.button("Prüfen", type="primary", key=f"check_{idx}"):
                        if user_sentence.strip():
                            with st.spinner("Claude prüft..."):
                                result = vocab_practice.check_sentence(
                                    word["word"], word["definition"], user_sentence
                                )
                                db.update_vocabulary_review(word["id"], result["correct"])
                                st.session_state["vocab_feedback"] = result
                                st.rerun()
                with bcol2:
                    if st.button("Überspringen", key=f"skip_{idx}"):
                        db.update_vocabulary_review(word["id"], False)
                        st.session_state["vocab_practice_index"] = idx + 1
                        st.session_state["vocab_feedback"] = None
                        st.rerun()

                if st.session_state["vocab_feedback"]:
                    fb = st.session_state["vocab_feedback"]
                    if fb["correct"]:
                        st.success(fb["feedback"])
                    else:
                        st.error(fb["feedback"])
                    if st.button("Weiter", key=f"next_{idx}"):
                        st.session_state["vocab_practice_index"] = idx + 1
                        st.session_state["vocab_feedback"] = None
                        st.rerun()

    st.markdown("---")
    vocab_list = db.get_vocabulary()
    st.subheader(f"Vokabelliste ({len(vocab_list)} Einträge)")
    with st.expander("Alle Vokabeln anzeigen"):
        if vocab_list:
            for entry in vocab_list:
                word_col, audio_col = st.columns([9, 1])
                with word_col:
                    st.markdown(f"**{entry['word']}**")
                with audio_col:
                    render_pronunciation_button(entry['word'], key=f"vocab_list_{entry['id']}")
                st.caption(entry['definition'])
                st.caption(f"_{entry['example']}_")
                st.divider()
        else:
            st.info("Noch keine Vokabeln gespeichert.")

# --- TAB 5: THEORIE ---
with tab5:
    from grammar_theory import GRAMMAR_RULES

    st.header("Grammatik")
    st.caption("A1 bis C1 - alle 78 Regeln an einem Ort, geprüft gegen echte telc-Aufgaben und das vollständige B1-C1-Lehrwerk. Plus: die vollständige Verbkonjugation für jedes Verb.")

    render_verb_conjugator_tool()

    categories = sorted(set(r["category"] for r in GRAMMAR_RULES))
    category_filter = st.selectbox(
        "Kategorie wählen (optional, engt alle Niveaus gleichzeitig ein)",
        options=["Alle"] + categories,
        key="theory_category"
    )

    filtered = [
        r for r in GRAMMAR_RULES
        if category_filter == "Alle" or r["category"] == category_filter
    ]

    level_order = ["A1", "A2", "B1", "B2", "C1"]
    level_colors = {"A1": "🔵", "A2": "🟢", "B1": "🟡", "B2": "🟠", "C1": "🔴"}
    level_names = {"A1": "Anfänger", "A2": "Grundstufe", "B1": "Mittelstufe I", "B2": "Mittelstufe II", "C1": "Oberstufe"}

    if not filtered:
        st.info("Keine Regeln für diese Kategorie.")
    else:
        if "theory_selected_rule_id" not in st.session_state:
            st.session_state["theory_selected_rule_id"] = None

        st.markdown("**Regel wählen** - nach Niveau gruppiert, auf einen Abschnitt klicken zum Öffnen:")
        for level in level_order:
            level_rules = sorted(
                [r for r in filtered if r["level"] == level],
                key=lambda r: r["category"]
            )
            if not level_rules:
                continue
            with st.expander(f"{level_colors.get(level, '')} {level} - {level_names.get(level, '')} ({len(level_rules)})"):
                last_category = None
                for r in level_rules:
                    if r["category"] != last_category:
                        st.caption(r["category"])
                        last_category = r["category"]
                    if st.button(r["title"], key=f"theory_pick_{r['id']}", use_container_width=True):
                        st.session_state["theory_selected_rule_id"] = r["id"]
                        st.rerun()

        selected_rule = next((r for r in filtered if r["id"] == st.session_state["theory_selected_rule_id"]), None)
        if selected_rule:
            render_grammar_rule(selected_rule)
        else:
            st.info("Wählen Sie oben ein Niveau und dann eine Regel aus.")

