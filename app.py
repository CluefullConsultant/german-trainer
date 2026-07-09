# app.py
import streamlit as st
import exercises
import vocabulary
import db
import vocab_practice
import content_feed
import theory_quiz
import verb_conjugator
import theme


def render_grammar_rule(rule):
    """Render a single grammar_theory.py rule: explanation, examples, mistakes, quiz."""
    rid = rule["id"]

    st.divider()
    st.subheader(rule["title"])

    st.markdown(rule["explanation"])

    if rule.get("examples"):
        st.markdown("---")
        st.markdown("**Beispiele:**")
        for ex in rule["examples"]:
            st.markdown(f"**{ex['label']}**")
            st.markdown(f"> {ex['sentence']}")
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
            st.session_state[quiz_key] = theory_quiz.generate_quiz(
                rule["title"], rule["explanation"], rule["level"]
            )
            st.session_state[f"{quiz_key}_submitted"] = False
            st.rerun()

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


def render_exercise(content, exercise_type):
    """Render exercise content as readable German text (no raw JSON)."""
    if exercise_type == "Lückentext":
        if content.get("instruction"):
            st.info(content["instruction"])
        blanks = content.get("blanks", [])
        segments = content.get("text_with_blanks", "").split("___")
        parts = []
        for i, seg in enumerate(segments):
            parts.append(seg)
            if i < len(blanks):
                parts.append(f"**___({i+1})___**")
        st.markdown("".join(parts))
        if blanks:
            with st.expander("Hinweise anzeigen"):
                for i, blank in enumerate(blanks):
                    st.markdown(f"- ({i+1}) {blank.get('hint', '')}")

    elif exercise_type == "Sprachbausteine":
        if content.get("instruction"):
            st.info(content["instruction"])
        blanks = content.get("blanks", [])
        segments = content.get("text_with_blanks", "").split("___")
        parts = []
        for i, seg in enumerate(segments):
            parts.append(seg)
            if i < len(blanks):
                parts.append(f"**___({i+1})___**")
        st.markdown("".join(parts))
        if blanks:
            letters = ["a", "b", "c", "d"]
            with st.expander("Antwortoptionen anzeigen"):
                for i, blank in enumerate(blanks):
                    st.markdown(f"**({i+1})**")
                    for j, opt in enumerate(blank.get("options", [])):
                        st.markdown(f"  {letters[j]}) {opt}")

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

    elif exercise_type == "Zuordnung":
        if content.get("instruction"):
            st.info(content["instruction"])
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Begriffe:**")
            for item in content.get("items", []):
                st.markdown(f"{item['id']}. {item['text']}")
        with col2:
            st.markdown("**Definitionen:**")
            for opt in content.get("options", []):
                st.markdown(f"{opt['id']}. {opt['text']}")

    elif exercise_type == "Richtig/Falsch/Nicht im Text":
        if content.get("instruction"):
            st.info(content["instruction"])
        st.markdown(content.get("text", ""))
        st.markdown("**Aussagen:**")
        for i, s in enumerate(content.get("statements", [])):
            st.markdown(f"**{i+1}.** {s.get('statement', '')}  _(R / F / N)_")

    elif exercise_type == "Wortbildung":
        if content.get("instruction"):
            st.info(content["instruction"])
        for i, item in enumerate(content.get("items", [])):
            st.markdown(f"**{i+1}.** {item.get('sentence', '')}  _{item.get('base_word', '')}_")

    elif exercise_type == "Aufsatz":
        if content.get("instruction"):
            st.info(content["instruction"])
        st.markdown(f"**Thema:** {content.get('thema', '')}")
        if content.get("position_a") or content.get("position_b"):
            st.markdown(f"- **Position A:** {content.get('position_a', '')}")
            st.markdown(f"- **Position B:** {content.get('position_b', '')}")
        st.markdown("**Leitfragen:**")
        for hint in content.get("leitfragen", []):
            st.markdown(f"- {hint}")

    else:
        st.json(content)


st.set_page_config(page_title="Deutsch Trainer", page_icon="", layout="wide")
theme.inject_custom_theme()

st.title("Deutsch Trainer")
st.caption("Ein Lernwerkzeug für Horst und Antony")

try:
    top_errors = db.get_top_errors(3)
    if top_errors:
        st.warning(
            "**Häufigste Fehler:** " +
            " | ".join([f"{e['tag']} ({e['count']}x)" for e in top_errors])
        )
except Exception:
    pass

tab1, tab4, tab_grundlagen, tab5, tab6 = st.tabs([
    "Aufgaben erstellen",
    "Heute lernen",
    "Grundlagen",
    "Theorie",
    "Interview",
])

# ==================== GRUNDLAGEN-KATEGORIE-IDS ====================
# Diese Regeln werden im Tab "Grundlagen" gezeigt, nicht im Tab "Theorie" (keine Duplikate).
GRUNDLAGEN_RULE_IDS = [
    "grund_wortarten",
    "grund_satzglieder",
    "grund_hauptsatz_nebensatz",
    "grund_fragesaetze",
    "grund_kasus",
    "grund_genus_numerus",
    "adjektivdeklination",
    "n_deklination",
    "grund_verbformen",
    "verben_schwach_stark",
    "zeitformen_ueberblick",
    "grund_partizipien",
    "verb_drei_achsen",
    "genus_verbi_ueberblick",
    "b1_konjunktiv2",
    "imperativ",
]

# --- TAB 1: AUFGABEN ERSTELLEN ---
with tab1:
    st.header("Neue Aufgabe erstellen")

    mode = st.radio(
        "Modus",
        options=["Prüfungssimulation (telc/Goethe-Format)", "Grammatikübung (frei wählbar)"],
        horizontal=True,
        help="Prüfungssimulation folgt dem echten Telc/Goethe-C1-Testformat (5 Prüfungsteile). Grammatikübung lässt frei ein Grammatikthema wählen.",
    )

    custom_topic = ""

    if mode == "Prüfungssimulation (telc/Goethe-Format)":
        st.info(
            "Wählen Sie den Prüfungsteil und den Aufgabentyp - genau wie im echten Test. "
            "Optional können Sie einen Grammatik-Fokus angeben."
        )
        col1, col2 = st.columns(2)
        with col1:
            selected_teil = st.selectbox(
                "Prüfungsteil",
                options=exercises.PRUEFUNGSTEILE,
                help="Welcher Teil der Prüfung soll geübt werden?",
            )
        teil_aufgaben = exercises.PRUEFUNG_AUFGABEN[selected_teil]
        teil_labels = [label for label, _ in teil_aufgaben]
        with col2:
            selected_label = st.selectbox(
                "Aufgabentyp",
                options=teil_labels,
                help="Welche Aufgabenform innerhalb dieses Prüfungsteils?",
            )
        selected_type = dict(teil_aufgaben)[selected_label]

        grammatik_fokus = st.text_input(
            "Grammatik-/Themenfokus (optional)",
            placeholder="z.B. 'Konjunktiv II' oder 'Genitiv-Präpositionen' - leer lassen für gemischte Übung",
            help="Leer lassen für eine realistische, gemischte Prüfungsaufgabe wie im echten Test.",
        )
        selected_topic = grammatik_fokus.strip() if grammatik_fokus.strip() else exercises.PRUEFUNG_DEFAULT_TOPIC.get(selected_teil, selected_teil)

    else:
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

        # Free topic input when "Eigenes Thema" is selected
        if selected_topic == "Eigenes Thema":
            custom_topic = st.text_input(
                "Ihr Thema",
                placeholder="z.B. 'Reflexive Verben mit Präpositionen' oder 'Bewerbungsschreiben' oder 'Zeitungssprache'",
                help="Geben Sie ein beliebiges Grammatik- oder Vokabelthema ein. Claude erstellt eine passende Übung.",
            )

    # Show register selector for Brief schreiben (writing practice)
    selected_register = "Formeller Brief (Telc-Stil)"
    if selected_type == "Brief schreiben":
        selected_register = st.selectbox(
            "Textsorte",
            options=[
                "Formeller Brief (Telc-Stil)",
                "Geschäftliche E-Mail",
                "Kurzbericht / Protokoll",
                "Informelle Nachricht",
            ],
            help="Welche Art von Text soll geübt werden?",
        )
        if st.button("Thema vorschlagen", key="suggest_brief_topic"):
            import random
            from writing_topics import BRIEF_TOPICS
            st.session_state["brief_thema_input"] = random.choice(BRIEF_TOPICS[selected_register])
        brief_thema = st.text_input(
            "Thema/Szenario (leer lassen für zufälliges Thema von Claude)",
            key="brief_thema_input",
            placeholder="z.B. 'Beschwerde über eine defekte Lieferung' - oder auf 'Thema vorschlagen' klicken",
        )

    # Free topic input for Aufsatz (essay - any topic, no restriction)
    aufsatz_thema = ""
    if selected_type == "Aufsatz":
        if st.button("Thema vorschlagen", key="suggest_aufsatz_topic"):
            import random
            from writing_topics import AUFSATZ_TOPICS
            st.session_state["aufsatz_thema_input"] = random.choice(AUFSATZ_TOPICS)["thema"]
        aufsatz_thema = st.text_input(
            "Aufsatzthema (frei wählbar, leer lassen für zufälliges Thema)",
            key="aufsatz_thema_input",
            placeholder="z.B. 'Sollte Home-Office Pflicht werden?' oder 'Digitalisierung und Datenschutz' - beliebiges Thema möglich",
            help="Egal welches Thema - geschäftlich, gesellschaftlich, persönlich. Leer lassen und Claude wählt selbst ein Thema.",
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
                effective_topic = custom_topic.strip() if selected_topic == "Eigenes Thema" and custom_topic.strip() else selected_topic
                effective_notes = mentor_notes
                if selected_type == "Brief schreiben":
                    effective_notes = f"Textsorte: {selected_register}. {mentor_notes}".strip()
                    if brief_thema.strip():
                        effective_notes = f"Thema/Szenario: {brief_thema.strip()}. {effective_notes}".strip()
                elif selected_type == "Aufsatz" and aufsatz_thema.strip():
                    effective_notes = f"Thema: {aufsatz_thema.strip()}. {mentor_notes}".strip()
                content = exercises.generate_exercise(
                    topic=effective_topic,
                    exercise_type=selected_type,
                    mentor_notes=effective_notes,
                    pasted_text=pasted_text,
                )
                st.session_state["preview_content"] = content
                st.session_state["preview_topic"] = effective_topic
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
            content = st.session_state["preview_content"]
            ex_type = st.session_state["preview_type"]
            edited_fields = {}

            if ex_type == "Lückentext":
                edited_fields["instruction"] = st.text_input(
                    "Aufgabenanweisung", value=content.get("instruction", ""))
                edited_fields["text_with_blanks"] = st.text_area(
                    "Text mit Lücken (___)", value=content.get("text_with_blanks", ""), height=150)

            elif ex_type == "Mehrfachauswahl":
                items = content.get("items", [])
                edited_items = []
                for i, item in enumerate(items):
                    st.markdown(f"**Frage {i+1}**")
                    q = st.text_input(f"Frage", value=item.get("question", ""), key=f"edit_mc_q_{i}")
                    opts_text = "\n".join(item.get("options", []))
                    opts = st.text_area(f"Antwortoptionen (eine pro Zeile)", value=opts_text, key=f"edit_mc_opts_{i}", height=100)
                    edited_items.append({**item, "question": q, "options": [o.strip() for o in opts.splitlines() if o.strip()]})
                edited_fields["items"] = edited_items

            elif ex_type == "Satztransformation":
                items = content.get("items", [])
                edited_items = []
                for i, item in enumerate(items):
                    st.markdown(f"**Aufgabe {i+1}**")
                    instr = st.text_input(f"Anweisung", value=item.get("instruction", ""), key=f"edit_trans_instr_{i}")
                    sents_text = "\n".join(item.get("sentences", []))
                    sents = st.text_area(f"Sätze (einer pro Zeile)", value=sents_text, key=f"edit_trans_sents_{i}", height=80)
                    edited_items.append({**item, "instruction": instr, "sentences": [s.strip() for s in sents.splitlines() if s.strip()]})
                edited_fields["items"] = edited_items

            elif ex_type == "Fehlersuche":
                sentences = content.get("sentences", [])
                edited_sentences = []
                for i, s in enumerate(sentences):
                    text = st.text_input(f"Satz {i+1}", value=s.get("text", ""), key=f"edit_err_{i}")
                    edited_sentences.append({**s, "text": text})
                edited_fields["sentences"] = edited_sentences

            elif ex_type == "Übersetzung":
                items = content.get("items", [])
                edited_items = []
                for i, item in enumerate(items):
                    src = st.text_input(f"Satz {i+1}", value=item.get("source", ""), key=f"edit_ue_{i}")
                    edited_items.append({**item, "source": src})
                edited_fields["items"] = edited_items

            elif ex_type == "Kategoriensortierung":
                edited_fields["instruction"] = st.text_input(
                    "Anweisung", value=content.get("instruction", ""))
                words_text = ", ".join(content.get("words", []))
                edited_words = st.text_input("Wörter (durch Komma getrennt)", value=words_text)
                edited_fields["words"] = [w.strip() for w in edited_words.split(",") if w.strip()]

            elif ex_type == "Brief schreiben":
                edited_fields["prompt"] = st.text_area(
                    "Aufgabenstellung", value=content.get("prompt", ""), height=100)
                rp_text = "\n".join(content.get("reihenpunkte", []))
                edited_rp = st.text_area("Reihenpunkte (ein Punkt pro Zeile)", value=rp_text, height=100)
                edited_fields["reihenpunkte"] = [r.strip() for r in edited_rp.splitlines() if r.strip()]

            elif ex_type == "Sprechaufgabe":
                edited_fields["prompt"] = st.text_area(
                    "Sprechanlass", value=content.get("prompt", ""), height=100)
                hints_text = "\n".join(content.get("hints", []))
                edited_hints = st.text_area("Hinweise (ein Hinweis pro Zeile)", value=hints_text, height=100)
                edited_fields["hints"] = [h.strip() for h in edited_hints.splitlines() if h.strip()]

            elif ex_type in ("Leseverstehen", "Hörverstehen"):
                edited_fields["text"] = st.text_area(
                    "Text", value=content.get("text", ""), height=200)
                questions = content.get("questions", [])
                edited_questions = []
                for i, q in enumerate(questions):
                    qtext = st.text_input(f"Frage {i+1}", value=q.get("question", ""), key=f"edit_lv_{i}")
                    edited_questions.append({**q, "question": qtext})
                edited_fields["questions"] = edited_questions

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
                    del st.session_state["preview_content"]
                    st.success("Aufgabe gespeichert!")
                    st.rerun()

# --- TAB 4: HEUTE LERNEN ---
with tab4:
    st.header("Heute lernen")

    vocab_col, content_col = st.columns([1, 2])

    with vocab_col:
        st.subheader("Vokabeln")

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
                for w in nouns + verbs:
                    st.markdown(f"**{w['word']}** {level_badge.get(w.get('level', ''), '')}{context_badge.get(w.get('context', ''), '')}")
                    st.caption(w['definition'])
                    st.caption(f"_{w['example']}_")
                    st.divider()

        st.markdown("**Vokabeln üben**")
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
                    st.markdown(f"**{word['word']}**")
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

        vocab_list = db.get_vocabulary()
        with st.expander(f"Vokabelliste ({len(vocab_list)} Einträge)"):
            if vocab_list:
                for entry in vocab_list:
                    st.markdown(f"**{entry['word']}**")
                    st.caption(entry['definition'])
                    st.caption(f"_{entry['example']}_")
                    st.divider()
            else:
                st.info("Noch keine Vokabeln gespeichert.")

    with content_col:
        st.subheader("Deutsche Welle - Artikel")
        st.caption("Aktuelle Texte auf Deutsch, jeden Tag neu.")

        if "dw_articles" not in st.session_state:
            with st.spinner("Artikel werden geladen..."):
                st.session_state["dw_articles"] = content_feed.fetch_dw_articles()
                st.session_state["dw_selected"] = None
                st.session_state["dw_questions"] = []
                st.session_state["dw_answers"] = {}

        articles = st.session_state.get("dw_articles", [])

        if not articles:
            st.warning("Keine Artikel gefunden. Bitte Internetverbindung prüfen.")
        else:
            if st.session_state.get("dw_selected") is None:
                st.markdown("**Artikel auswählen**")
                for i, article in enumerate(articles):
                    with st.container(border=True):
                        c1, c2 = st.columns([4, 1])
                        with c1:
                            st.markdown(f"**{article['title']}**")
                            st.caption(article['description'][:150] + "..." if len(article['description']) > 150 else article['description'])
                        with c2:
                            if st.button("Lesen", key=f"dw_{i}"):
                                st.session_state["dw_selected"] = i
                                st.session_state["dw_questions"] = []
                                st.session_state["dw_answers"] = {}
                                st.rerun()
                if st.button("Neue Artikel laden"):
                    del st.session_state["dw_articles"]
                    st.rerun()
            else:
                article = articles[st.session_state["dw_selected"]]
                if st.button("Zurück zur Artikelliste"):
                    st.session_state["dw_selected"] = None
                    st.rerun()

                st.subheader(article["title"])
                if article.get("link"):
                    st.caption(f"Quelle: Deutsche Welle | [Artikel öffnen]({article['link']})")
                st.markdown(article["description"])

                st.divider()

                dcol1, dcol2 = st.columns(2)
                with dcol1:
                    if st.button("Verständnisfragen generieren", type="primary"):
                        with st.spinner("Claude erstellt Fragen..."):
                            st.session_state["dw_questions"] = content_feed.generate_questions_from_article(
                                article["title"], article["description"]
                            )
                            st.session_state["dw_answers"] = {}
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

                if st.button("Tandem-Vorbereitung", key="tandem_prep"):
                    with st.spinner("Gesprächsanlässe werden erstellt..."):
                        prompts = content_feed.generate_tandem_prompts(
                            article["title"], article["description"]
                        )
                        st.session_state["tandem_prompts"] = prompts
                        st.rerun()

                if st.session_state.get("tandem_prompts"):
                    st.subheader("Tandem-Gesprächsanlässe")
                    st.caption("Bereiten Sie sich auf diese Fragen für Ihr 16:30 Tandem-Gespräch vor.")
                    for i, prompt in enumerate(st.session_state["tandem_prompts"]):
                        st.markdown(f"**{i+1}.** {prompt}")

                if st.session_state.get("dw_questions"):
                    st.subheader("Verständnisfragen")
                    for i, q in enumerate(st.session_state["dw_questions"]):
                        st.markdown(f"**{i+1}. {q['question']}**")
                        answer = st.text_area("Ihre Antwort:", key=f"dw_ans_{i}", height=80)
                        if answer:
                            st.session_state["dw_answers"][i] = answer

                    if st.session_state["dw_answers"] and st.button("Antworten prüfen", type="primary"):
                        for i, q in enumerate(st.session_state["dw_questions"]):
                            user_ans = st.session_state["dw_answers"].get(i, "")
                            if user_ans:
                                st.markdown(f"**Frage {i+1}:** Musterlösung: _{q['answer']}_")

# --- TAB 5: THEORIE ---
with tab_grundlagen:
    from grammar_theory import GRAMMAR_RULES

    st.header("Grundlagen")
    st.caption("Die Bausteine, auf denen alles andere aufbaut: Wortarten, Kasus, Deklination, Verbformen, Zeiten, Partizip, Konjunktiv.")

    render_verb_conjugator_tool()

    rules_by_id = {r["id"]: r for r in GRAMMAR_RULES}
    grundlagen_rules = [rules_by_id[rid] for rid in GRUNDLAGEN_RULE_IDS if rid in rules_by_id]

    grund_labels = [r["title"] for r in grundlagen_rules]
    grund_idx = st.radio(
        "Thema wählen",
        options=range(len(grundlagen_rules)),
        format_func=lambda i: grund_labels[i],
        key="grundlagen_rule_pick",
    )
    render_grammar_rule(grundlagen_rules[grund_idx])

with tab5:
    from grammar_theory import GRAMMAR_RULES

    st.header("Grammatik-Theorie")
    st.caption("B1 bis C1 - alle Regeln, die du für Telc und den Arbeitsalltag brauchst. Die Grundlagen (Kasus, Deklination, Verbformen, Zeiten) findest du im Tab \"Grundlagen\".")

    filter_col1, filter_col2 = st.columns(2)
    with filter_col1:
        level_filter = st.selectbox(
            "Niveau wählen",
            options=["Alle", "A1", "A2", "B1", "B2", "C1"],
            key="theory_level"
        )
    with filter_col2:
        categories = sorted(set(r["category"] for r in GRAMMAR_RULES if r["id"] not in GRUNDLAGEN_RULE_IDS))
        category_filter = st.selectbox(
            "Kategorie wählen",
            options=["Alle"] + categories,
            key="theory_category"
        )

    filtered = [
        r for r in GRAMMAR_RULES
        if r["id"] not in GRUNDLAGEN_RULE_IDS
        and (level_filter == "Alle" or r["level"] == level_filter)
        and (category_filter == "Alle" or r["category"] == category_filter)
    ]

    level_order = {"A1": 0, "A2": 1, "B1": 2, "B2": 3, "C1": 4}
    filtered.sort(key=lambda r: (level_order.get(r["level"], 99), r["category"]))

    level_colors = {"A1": "🔵", "A2": "🟢", "B1": "🟡", "B2": "🟠", "C1": "🔴"}

    if not filtered:
        st.info("Keine Regeln für dieses Niveau.")
    else:
        rule_labels = [f"{level_colors.get(r['level'], '')} {r['level']} - {r['title']}" for r in filtered]
        selected_idx = st.radio(
            "Regel wählen",
            options=range(len(filtered)),
            format_func=lambda i: rule_labels[i],
            key=f"theory_rule_pick_{level_filter}",
        )
        render_grammar_rule(filtered[selected_idx])

# --- TAB 6: INTERVIEW ---
with tab6:
    from interview_skeleton import DEFAULT_BAUSTEINE, INTERVIEW_TIPS
    import interview_coach
    import interview_content
    import re as re_module
    import time as time_module

    st.header("Interview-Vorbereitung")

    interview_mode = st.radio(
        "Ansicht",
        options=[
            "Selbstvorstellung üben (Skript A/B, combine)",
            "Anker + Spokes",
            "Story Bank (STAR)",
            "Fragen-Training",
            "combine: Fakten & Change-Modelle",
            "Bausteine frei bearbeiten (jede Firma)",
        ],
    )
    st.divider()

    def _format_beat_html(text):
        text = re_module.sub(r'\*\*(.+?)\*\*', r'<strong style="color:#a6432f;">\1</strong>', text)
        text = re_module.sub(r'==(.+?)==', r'<span style="background:#dcece1;border-radius:3px;padding:0 3px;">\1</span>', text)
        return text

    if interview_mode == "Selbstvorstellung üben (Skript A/B, combine)":
        script_choice = st.radio(
            "Skript",
            ["Skript A - Standard (~90 Sek)", "Skript B - Kompletter Werdegang (~2 Min, nur auf Nachfrage)"],
            horizontal=True,
        )
        script = interview_content.SKRIPT_A if script_choice.startswith("Skript A") else interview_content.SKRIPT_B
        st.subheader(script["title"])

        if "corrections" in script:
            with st.expander("Zwei Korrekturen gegenüber dem Original (zum Mitlernen)", expanded=True):
                for c in script["corrections"]:
                    st.markdown(f"~~{c['wrong']}~~")
                    st.markdown(f"→ **{c['right']}**")
                    st.caption(c["rule"])
                    st.divider()

        practice_view = st.radio("Modus", ["Volltext", "Übungsmodus"], horizontal=True, key=f"view_{script_choice}")

        timer_key = f"skript_timer_{script_choice}"
        if timer_key not in st.session_state:
            if st.button("Timer starten", key=f"start_{script_choice}"):
                st.session_state[timer_key] = time_module.time()
                st.rerun()
        else:
            elapsed = int(time_module.time() - st.session_state[timer_key])
            target = script["target_seconds"]
            st.info(f"Laufzeit: {elapsed // 60}:{elapsed % 60:02d} (Ziel: {target // 60}:{target % 60:02d})")
            if st.button("Stopp", key=f"stop_{script_choice}"):
                del st.session_state[timer_key]
                st.rerun()

        st.caption("Übungsmodus: nur der Einstiegssatz bleibt sichtbar. Rekonstruiere den Abschnitt frei, bevor du ihn aufklappst - nicht auswendig lernen, den roten Faden verinnerlichen.")
        st.divider()

        for beat in script["beats"]:
            cue_plain = beat["cue"].replace("**", "")
            formatted_text = _format_beat_html(beat["text"])
            if practice_view == "Volltext":
                with st.container(border=True):
                    st.markdown(f"**{cue_plain}**")
                    st.markdown(formatted_text, unsafe_allow_html=True)
                    if beat.get("note"):
                        st.caption(beat["note"])
            else:
                with st.expander(cue_plain, expanded=False):
                    st.markdown(formatted_text, unsafe_allow_html=True)
                    if beat.get("note"):
                        st.caption(beat["note"])

    elif interview_mode == "Anker + Spokes":
        st.caption("Aus persona-narrative.md - dieselbe Grundfrage wird oft dreimal anders formuliert. Immer denselben Anker zuerst sagen, dann den passenden Spoke wählen - nie live neu improvisieren.")
        st.subheader("Der Anker (immer zuerst, egal wie die Frage gestellt wird)")
        st.info(interview_content.ANCHOR)

        st.subheader("Spokes (je nach genauer Formulierung der Frage)")
        for spoke in interview_content.SPOKES:
            with st.container(border=True):
                st.markdown(f"**{spoke['trigger']}**")
                st.markdown(spoke["text"])

        st.subheader("Beweise auf Abruf (nur falls nachgefragt: \"Warum glaubst du das?\")")
        for p in interview_content.PROOFS_ON_DEMAND:
            st.markdown(f"- {p}")

    elif interview_mode == "Story Bank (STAR)":
        st.caption("Jeden Buchstaben einzeln aufdecken und frei sprechen, bevor der nächste kommt - nicht den ganzen Absatz auf einmal lesen.")
        for story in interview_content.STAR_STORIES:
            with st.expander(story["title"]):
                st.caption(f"Passt zu: {story['best_for']}")
                cols = st.columns(len(story["parts"]))
                for i, (label, _) in enumerate(story["parts"]):
                    key = f"star_{story['id']}_{label}"
                    with cols[i]:
                        if st.button(label, key=f"btn_{key}"):
                            st.session_state[key] = not st.session_state.get(key, False)
                for label, text in story["parts"]:
                    key = f"star_{story['id']}_{label}"
                    if st.session_state.get(key):
                        st.markdown(f"**{label}:** {text}")

        st.divider()
        b = interview_content.COMBINE_BRIDGE_STORY
        with st.expander(b["title"]):
            st.warning(b["warning"])
            st.markdown(f"> {b['verbatim']}")
            st.caption(b["facts"])

    elif interview_mode == "Fragen-Training":
        pool_choice = st.radio("Fragen-Pool", ["combine-spezifisch", "Allgemein (jede Firma)"], horizontal=True)
        pool = interview_content.COMBINE_QUESTIONS if pool_choice == "combine-spezifisch" else interview_content.GENERAL_QUESTIONS

        if st.session_state.get("interview_quiz_pool") != pool_choice:
            st.session_state["interview_quiz_pool"] = pool_choice
            st.session_state["interview_quiz_idx"] = None
            st.session_state["interview_quiz_revealed"] = False

        st.caption("Zufällige Frage ziehen, laut beantworten, dann erst den Antwort-Anker aufdecken - nicht umgekehrt.")

        import random
        if st.button("Neue Frage", type="primary"):
            choices = list(range(len(pool)))
            current_idx = st.session_state.get("interview_quiz_idx")
            if current_idx in choices and len(choices) > 1:
                choices.remove(current_idx)
            st.session_state["interview_quiz_idx"] = random.choice(choices)
            st.session_state["interview_quiz_revealed"] = False
            st.rerun()

        idx = st.session_state.get("interview_quiz_idx")
        if idx is not None and idx < len(pool):
            q, a = pool[idx]
            with st.container(border=True):
                st.markdown(f"### {q}")
                if st.button("Antwort-Anker zeigen", key="reveal_interview_quiz"):
                    st.session_state["interview_quiz_revealed"] = True
                    st.rerun()
                if st.session_state.get("interview_quiz_revealed"):
                    st.info(a)
        else:
            st.caption("Klicke \"Neue Frage\", um zu starten.")

        if pool_choice == "Allgemein (jede Firma)":
            st.divider()
            st.warning("**Noch offen - nicht vorgeschrieben:** \"Was ist deine größte Schwäche?\" Wähle eine echte, kalibrierte Antwort und formuliere sie selbst - das ist keine, die auswendig gelernt werden sollte.")

    elif interview_mode == "combine: Fakten & Change-Modelle":
        st.subheader("combine-Fakten (Gesprächsaufhänger)")
        for fact in interview_content.COMBINE_FACTS:
            with st.expander(fact["title"]):
                st.markdown(fact["text"])
                if fact.get("note"):
                    st.caption(fact["note"])

        st.divider()
        st.subheader("Change-Management-Modelle (falls gefragt)")
        st.caption("Nicht ungefragt herunterbeten. Kurz 1-2 nennen, dann zurück zu TACO als eigene Praxis.")
        for model in interview_content.CHANGE_MODELS:
            with st.expander(model["title"]):
                st.markdown(model["text"])
                if model.get("verbatim"):
                    st.markdown(f"> {model['verbatim']}")
                if model.get("note"):
                    st.caption(model["note"])

    else:
        st.caption("Fünf Bausteine mit Stichpunkten - kein auswendig gelernter Text. Du sprichst frei, die Reihenfolge und Kernfakten bleiben fix. Für eine andere Firma als combine hier neu schreiben.")

        with st.expander("Warum diese Methode funktioniert (Recherche zu deutschen Recruitern)"):
            for tip in INTERVIEW_TIPS:
                st.markdown(f"- {tip}")

        try:
            interview_state = db.get_interview_state()
        except Exception:
            interview_state = {}

        practice_counts = interview_state.get("practice_counts", {})
        company_variants = interview_state.get("company_variants", {})
        scripts = interview_state.get("scripts", {})
        full_runs = interview_state.get("full_runs", 0)
        current_company = interview_state.get("current_company", "")

        def _save_state():
            try:
                db.save_interview_state({
                    "practice_counts": practice_counts,
                    "company_variants": company_variants,
                    "scripts": scripts,
                    "full_runs": full_runs,
                    "current_company": current_company,
                })
            except Exception:
                st.warning("Fortschritt konnte nicht gespeichert werden (Verbindungsproblem).")

        st.divider()
        st.subheader("Vor diesem Gespräch: Firma eintragen")
        company_input = st.text_input(
            "Für welches Unternehmen übst du gerade?",
            value=current_company,
            placeholder="z.B. combine, Tekkr, ...",
            key="interview_company_input",
        )
        if company_input != current_company:
            current_company = company_input
            _save_state()

        if current_company and current_company in company_variants:
            st.success(f"Gespeicherte Baustein-4-Variante für '{current_company}' gefunden - unten vorausgefüllt.")

        st.divider()
        st.subheader("Die fünf Bausteine")

        for baustein in DEFAULT_BAUSTEINE:
            bid = str(baustein["id"])
            count = practice_counts.get(bid, 0)
            variable_tag = " 🔁 ändert sich pro Interview" if baustein["variable"] else ""
            with st.container(border=True):
                st.markdown(f"**{baustein['id']}. {baustein['title']}**{variable_tag}")
                st.caption(f"Ziel-Dauer: {baustein['dauer']} | Geübt: {count}x")

                for punkt in baustein["stichpunkte"]:
                    st.markdown(f"- {punkt}")

                if baustein["variable"]:
                    extra_context = st.text_input(
                        f"Was weißt du über '{current_company or 'das Unternehmen'}' (für den Claude-Entwurf, optional)",
                        key=f"extra_ctx_{bid}",
                        placeholder="z.B. 'Serviceplan-Projekt: Change Agents und künftige Nutzer wurden von Anfang an eingebunden'",
                    )
                    if current_company and st.button("Claude-Entwurf vorschlagen", key=f"draft_variant_{bid}"):
                        with st.spinner("Claude formuliert einen Vorschlag..."):
                            draft = interview_coach.draft_script(
                                baustein["title"], baustein["stichpunkte"], baustein["dauer"], extra_context
                            )
                            st.session_state[f"variant_{bid}"] = draft
                            st.rerun()

                    default_variant = company_variants.get(current_company, "") if current_company else ""
                    if not default_variant and current_company.strip().lower() == "combine":
                        default_variant = interview_content.SKRIPT_A["beats"][3]["text"].replace("**", "")
                    variant_text = st.text_area(
                        f"Dein Skript für '{current_company or 'dieses Unternehmen'}' (voll ausformuliert - zum Lesen):",
                        value=default_variant,
                        key=f"variant_{bid}",
                        height=100,
                        placeholder="Schreib hier den vollen Satz/Absatz aus - Beispiel: 'Ich kenne euer Projekt mit Serviceplan, bei dem ihr...' Zum lauten Lesen, nicht zum Auswendiglernen.",
                    )
                    if current_company and st.button("Skript speichern", key=f"save_variant_{bid}"):
                        company_variants[current_company] = variant_text
                        _save_state()
                        st.success(f"Skript für '{current_company}' gespeichert.")
                else:
                    if st.button("Claude-Entwurf vorschlagen", key=f"draft_script_{bid}"):
                        with st.spinner("Claude formuliert einen Vorschlag..."):
                            draft = interview_coach.draft_script(
                                baustein["title"], baustein["stichpunkte"], baustein["dauer"]
                            )
                            st.session_state[f"script_{bid}"] = draft
                            st.rerun()

                    script_text = st.text_area(
                        "Dein Skript (voll ausformuliert - zum Lesen):",
                        value=scripts.get(bid, ""),
                        key=f"script_{bid}",
                        height=100,
                        placeholder="Schreib hier aus den Stichpunkten oben einen vollständigen Text, den du laut vorlesen kannst - oder lass Claude einen Vorschlag machen.",
                    )
                    if st.button("Skript speichern", key=f"save_script_{bid}"):
                        scripts[bid] = script_text
                        _save_state()
                        st.success("Skript gespeichert.")

                col1, col2 = st.columns(2)
                with col1:
                    timer_key = f"baustein_timer_{bid}"
                    if timer_key not in st.session_state:
                        if st.button("Sprechzeit stoppen starten", key=f"start_{bid}"):
                            st.session_state[timer_key] = time_module.time()
                            st.rerun()
                    else:
                        elapsed = time_module.time() - st.session_state[timer_key]
                        st.info(f"Läuft: {elapsed:.1f} Sek")
                        if st.button("Stopp", key=f"stop_{bid}"):
                            del st.session_state[timer_key]
                            st.rerun()
                with col2:
                    if st.button("Runde absolviert (+1)", key=f"round_{bid}"):
                        practice_counts[bid] = count + 1
                        _save_state()
                        st.rerun()

        st.divider()
        st.subheader("Volltext - alle Bausteine zusammen")
        st.caption("Zum Lesen üben. Ziel: mit der Zeit immer weniger draufschauen müssen.")

        full_script_parts = []
        for baustein in DEFAULT_BAUSTEINE:
            bid = str(baustein["id"])
            if baustein["variable"]:
                text = company_variants.get(current_company, "") if current_company else ""
            else:
                text = scripts.get(bid, "")
            if text.strip():
                full_script_parts.append(f"**{baustein['id']}. {baustein['title']}**\n\n{text}")

        if full_script_parts:
            with st.container(border=True):
                st.markdown("\n\n---\n\n".join(full_script_parts))
        else:
            st.info("Noch keine Skripte geschrieben. Schreib oben bei jedem Baustein deinen Text und speichere ihn - hier erscheint dann der Volltext.")

        st.divider()
        st.subheader("Kompletter Durchlauf")
        st.caption("Alle fünf Bausteine am Stück, frei gesprochen. Zielzeit: ca. 1:20 - 1:40 Min.")

        full_timer_key = "interview_full_timer"
        if full_timer_key not in st.session_state:
            if st.button("Durchlauf starten", type="primary"):
                st.session_state[full_timer_key] = time_module.time()
                st.rerun()
        else:
            elapsed = time_module.time() - st.session_state[full_timer_key]
            mins = int(elapsed // 60)
            secs = int(elapsed % 60)
            st.info(f"Laufzeit: {mins}:{secs:02d}")
            if st.button("Durchlauf beendet"):
                del st.session_state[full_timer_key]
                full_runs += 1
                _save_state()
                st.rerun()

        st.metric("Komplette Durchläufe insgesamt", full_runs)
