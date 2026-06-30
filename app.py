# app.py
import streamlit as st
import exercises
import feedback
import vocabulary
import db
import json

st.set_page_config(page_title="Deutsch Trainer", page_icon="", layout="wide")

st.title("Deutsch Trainer")
st.caption("Ein Lernwerkzeug für Antony und seinen Mentor")

tab1, tab2, tab3, tab4 = st.tabs([
    "Aufgaben erstellen",
    "Uben",
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

    # Show extra text input for Leseverstehen / Horverstehen
    pasted_text = ""
    if selected_type in ("Leseverstehen", "Horverstehen"):
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

# --- TAB 2: UBEN (stub) ---
with tab2:
    st.info("Übungsbereich - wird in Schritt 7 implementiert.")

# --- TAB 3: FEEDBACK (stub) ---
with tab3:
    st.info("Feedback-Bereich - wird in Schritt 8 implementiert.")

# --- TAB 4: FORTSCHRITT (stub) ---
with tab4:
    st.info("Fortschritt - wird in Schritt 9 implementiert.")
