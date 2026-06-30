# app.py
import streamlit as st
import exercises
import feedback
import vocabulary
import db
import json
import mailer
import pdf_generator


def render_exercise(content, exercise_type):
    """Render exercise content as readable German text (no raw JSON)."""
    if exercise_type == "Lückentext":
        st.markdown(content.get("text_with_blanks", ""))
        for i, blank in enumerate(content.get("blanks", [])):
            st.markdown(f"- Lücke {i+1}: _{blank.get('hint', '')}_")

    elif exercise_type == "Mehrfachauswahl":
        for i, item in enumerate(content.get("items", [])):
            st.markdown(f"**{i+1}.** {item.get('question', '')}")
            for opt in item.get("options", []):
                st.markdown(f"  - {opt}")

    elif exercise_type == "Satztransformation":
        for i, item in enumerate(content.get("items", [])):
            st.markdown(f"**{i+1}.** {item.get('instruction', '')}")
            for s in item.get("sentences", []):
                st.markdown(f"  - _{s}_")

    elif exercise_type == "Fehlersuche":
        for i, sentence in enumerate(content.get("sentences", [])):
            st.markdown(f"**{i+1}.** {sentence.get('text', '')}")

    elif exercise_type == "Übersetzung":
        for i, item in enumerate(content.get("items", [])):
            st.markdown(f"**{i+1}.** _{item.get('source', '')}_")

    elif exercise_type == "Kategoriensortierung":
        st.markdown(content.get("instruction", ""))
        st.markdown("**Wörter:** " + ", ".join(content.get("words", [])))
        for cat in content.get("categories", {}).keys():
            st.markdown(f"- {cat}")

    elif exercise_type == "Brief schreiben":
        st.markdown(f"**Aufgabe:** {content.get('prompt', '')}")
        for punkt in content.get("reihenpunkte", []):
            st.markdown(f"- {punkt}")

    elif exercise_type in ("Leseverstehen", "Hörverstehen"):
        if exercise_type == "Hörverstehen":
            st.info("Text wird vom Mentor vorgelesen.")
        st.markdown(content.get("text", ""))
        for i, q in enumerate(content.get("questions", [])):
            st.markdown(f"**Frage {i+1}:** {q.get('question', '')}")

    elif exercise_type == "Sprechaufgabe":
        st.markdown(f"**Sprechanlass:** {content.get('prompt', '')}")
        for hint in content.get("hints", []):
            st.markdown(f"- {hint}")

    else:
        st.json(content)


def render_answer(answer, exercise_type):
    """Render Antony's answer as readable text."""
    if exercise_type == "Lückentext":
        for i, val in enumerate(answer.get("blanks", [])):
            st.markdown(f"- Lücke {i+1}: **{val}**")
    elif exercise_type == "Mehrfachauswahl":
        for i, val in enumerate(answer.get("choices", [])):
            st.markdown(f"- Frage {i+1}: **{val}**")
    elif exercise_type == "Satztransformation":
        for i, val in enumerate(answer.get("transformations", [])):
            st.markdown(f"- {i+1}: **{val}**")
    elif exercise_type == "Fehlersuche":
        for i, c in enumerate(answer.get("corrections", [])):
            if c.get("has_error"):
                st.markdown(f"- Satz {i+1}: Fehler - **{c.get('correction', '')}**")
            else:
                st.markdown(f"- Satz {i+1}: kein Fehler")
    elif exercise_type == "Übersetzung":
        for i, val in enumerate(answer.get("translations", [])):
            st.markdown(f"- {i+1}: **{val}**")
    elif exercise_type == "Kategoriensortierung":
        for cat, words in answer.get("categories", {}).items():
            st.markdown(f"- {cat}: **{', '.join(words)}**")
    elif exercise_type == "Brief schreiben":
        st.markdown(answer.get("letter", ""))
    elif exercise_type in ("Leseverstehen", "Hörverstehen"):
        for i, val in enumerate(answer.get("question_answers", [])):
            st.markdown(f"- Frage {i+1}: **{val}**")
    elif exercise_type == "Sprechaufgabe":
        notes = answer.get("notes", "")
        if notes:
            st.markdown(f"Notizen: {notes}")
        else:
            st.markdown("_(Sprechaufgabe - keine schriftliche Antwort)_")
    else:
        st.json(answer)


st.set_page_config(page_title="Deutsch Trainer", page_icon="", layout="wide")

st.title("Deutsch Trainer")
st.caption("Ein Lernwerkzeug für Horst und Antony")

tab1, tab2, tab3, tab4 = st.tabs([
    "Aufgaben erstellen",
    "Üben",
    "Feedback",
    "Fortschritt",
])

# --- TAB 1: AUFGABEN ERSTELLEN ---
with tab1:
    st.header("Neue Aufgabe erstellen")
    st.info(
        "Wählen Sie ein Thema und einen Aufgabentyp. "
        "Claude erstellt die Übung automatisch. "
        "Sie können die Aufgabe dann kontrollieren und speichern."
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

    # Show extra text input for Leseverstehen / Hörverstehen
    pasted_text = ""
    if selected_type in ("Leseverstehen", "Hörverstehen"):
        pasted_text = st.text_area(
            "Text einfügen (optional)",
            height=200,
            placeholder="Fügen Sie hier einen deutschen Text ein. Wenn leer, erstellt Claude einen passenden Text.",
            help="Sie können einen Zeitungsartikel oder anderen Text einfügen. Claude erstellt dann die Fragen dazu.",
        )

    mentor_notes = st.text_input(
        "Zusätzliche Hinweise (optional)",
        placeholder="z.B. 'obwohl vs trotzdem' oder 'Fokus auf trennbare Verben mit statt-'",
        help="Besondere Schwerpunkte oder Hinweise für diese Aufgabe.",
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
        render_exercise(st.session_state["preview_content"], st.session_state["preview_type"])

        with st.expander("Aufgabe bearbeiten"):
            st.caption("Sie können den Text der Aufgabe hier direkt anpassen, bevor Sie speichern.")
            edited_fields = {}
            content = st.session_state["preview_content"]
            ex_type = st.session_state["preview_type"]

            if ex_type == "Lückentext":
                edited_fields["text_with_blanks"] = st.text_area(
                    "Text mit Lücken (___)", value=content.get("text_with_blanks", ""), height=150)
            elif ex_type == "Brief schreiben":
                edited_fields["prompt"] = st.text_area(
                    "Aufgabenstellung", value=content.get("prompt", ""), height=100)
                reihenpunkte_text = "\n".join(content.get("reihenpunkte", []))
                edited_rp = st.text_area(
                    "Reihenpunkte (ein Punkt pro Zeile)", value=reihenpunkte_text, height=100)
                edited_fields["reihenpunkte"] = [r.strip() for r in edited_rp.splitlines() if r.strip()]
            elif ex_type == "Sprechaufgabe":
                edited_fields["prompt"] = st.text_area(
                    "Sprechanlass", value=content.get("prompt", ""), height=100)
                hints_text = "\n".join(content.get("hints", []))
                edited_hints = st.text_area(
                    "Hinweise (ein Hinweis pro Zeile)", value=hints_text, height=100)
                edited_fields["hints"] = [h.strip() for h in edited_hints.splitlines() if h.strip()]
            elif ex_type in ("Leseverstehen", "Hörverstehen"):
                edited_fields["text"] = st.text_area(
                    "Text", value=content.get("text", ""), height=200)
            else:
                st.info("Für diesen Aufgabentyp ist keine direkte Bearbeitung verfügbar. Klicken Sie 'Neu generieren' für eine neue Version.")

            if edited_fields:
                if st.button("Änderungen übernehmen"):
                    updated = {**content, **edited_fields}
                    st.session_state["preview_content"] = updated
                    st.success("Änderungen übernommen.")
                    st.rerun()

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
                    # Email exercise PDF to Antony
                    try:
                        pdf_bytes = pdf_generator.generate_exercise_pdf(
                            st.session_state["preview_topic"],
                            st.session_state["preview_type"],
                            st.session_state["preview_content"],
                        )
                        mailer.send_exercise_to_antony(
                            st.session_state["preview_topic"],
                            st.session_state["preview_type"],
                            pdf_bytes,
                        )
                    except Exception:
                        pass  # Email is best-effort, don't block save
                    del st.session_state["preview_content"]
                    st.success("Aufgabe gespeichert und per E-Mail an Antony gesendet!")
                    st.rerun()

# --- TAB 2: UBEN ---
with tab2:
    st.header("Aufgaben lösen")

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
                        if st.button("Öffnen", key=f"open_{ex['id']}"):
                            st.session_state["selected_exercise_id"] = ex["id"]
                            st.rerun()
        else:
            ex = db.get_exercise(st.session_state["selected_exercise_id"])
            if st.button("Zurück zur Liste"):
                st.session_state["selected_exercise_id"] = None
                st.session_state.pop("current_answer", None)
                st.rerun()

            st.subheader(f"{ex['topic']} - {ex['exercise_type']}")
            content = ex["content"]

            # Render exercise by type and collect answer
            answer = {}

            if ex["exercise_type"] == "Lückentext":
                st.markdown(content.get("text_with_blanks", ""))
                answers_list = []
                for i, blank in enumerate(content.get("blanks", [])):
                    val = st.text_input(f"Lücke {i+1} ({blank.get('hint', '')})", key=f"blank_{i}")
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
                    has_err = st.checkbox("Enthält einen Fehler", key=f"haserr_{i}")
                    correction = ""
                    if has_err:
                        correction = st.text_input("Korrektur:", key=f"corr_{i}")
                    corrections.append({"has_error": has_err, "correction": correction})
                answer = {"corrections": corrections}

            elif ex["exercise_type"] == "Übersetzung":
                translations = []
                for i, item in enumerate(content.get("items", [])):
                    st.markdown(f"**{i+1}.** _{item.get('source', '')}_")
                    val = st.text_input("Übersetzung:", key=f"trans_{i}")
                    translations.append(val)
                answer = {"translations": translations}

            elif ex["exercise_type"] == "Kategoriensortierung":
                st.markdown(content.get("instruction", ""))
                st.markdown("**Wörter:** " + ", ".join(content.get("words", [])))
                cat_answers = {}
                for cat in content.get("categories", {}).keys():
                    val = st.text_input(f"{cat}:", key=f"cat_{cat}", placeholder="Wörter durch Komma getrennt")
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

            elif ex["exercise_type"] in ("Leseverstehen", "Hörverstehen"):
                if ex["exercise_type"] == "Hörverstehen":
                    st.info("Ihr Mentor liest den folgenden Text vor. Hören Sie gut zu.")
                    with st.expander("Text (für den Mentor zum Vorlesen)"):
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
                        # Email results to Horst
                        try:
                            mailer.send_results_to_horst(
                                ex["topic"],
                                ex["exercise_type"],
                                answer,
                                fb_text,
                            )
                        except Exception:
                            pass
                    except Exception as e:
                        st.session_state["last_feedback"] = f"Feedback konnte nicht geladen werden: {e}"
                    st.rerun()

            if "last_feedback" in st.session_state:
                st.subheader("Claudes Feedback")
                st.markdown(st.session_state["last_feedback"])
                st.info("Ihr Mentor wird Ihnen zusätzliches Feedback geben.")

# --- TAB 3: FEEDBACK ---
with tab3:
    st.header("Eingereichte Aufgaben")

    unreviewed = db.get_unreviewed_submissions()
    reviewed = db.get_all_reviewed_submissions()

    if unreviewed:
        st.subheader(f"Ausstehend ({len(unreviewed)})")
        for sub in unreviewed:
            ex_info = sub.get("exercises", {})
            ex_type = ex_info.get("exercise_type", "")
            with st.container(border=True):
                st.markdown(f"**{ex_info.get('topic', '')}** - {ex_type}")
                st.caption(f"Eingereicht: {sub['submitted_at'][:10]}")

                with st.expander("Aufgabe anzeigen"):
                    render_exercise(ex_info.get("content", {}), ex_type)

                with st.expander("Antwort von Antony"):
                    render_answer(sub.get("answer", {}), ex_type)

                if sub.get("claude_feedback"):
                    with st.expander("Claudes automatisches Feedback"):
                        st.markdown(sub["claude_feedback"])

                mentor_fb = st.text_area(
                    "Ihr Feedback:",
                    key=f"mentor_fb_{sub['id']}",
                    placeholder="Schreiben Sie hier Ihr persönliches Feedback...",
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

# --- TAB 4: FORTSCHRITT ---
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
        st.info("Noch keine Fehlerdaten vorhanden. Lösen Sie Aufgaben und reichen Sie Antworten ein.")

    st.divider()

    # Vocabulary list
    st.subheader(f"Vokabelliste ({len(vocab)} Einträge)")
    if vocab:
        for entry in vocab:
            with st.container(border=True):
                st.markdown(f"**{entry['word']}**")
                st.markdown(f"_{entry['definition']}_")
                st.caption(f"Beispiel: {entry['example']}")
    else:
        st.info("Noch keine Vokabeln gespeichert. Sie werden automatisch beim Erstellen von Aufgaben gesammelt.")
