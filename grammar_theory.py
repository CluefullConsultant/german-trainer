# grammar_theory.py
# Complete B1-C1 grammar theory for self-study.
# Each entry: id, title, level, category, explanation, examples, mistakes, exercise_hint

GRAMMAR_RULES = [

    # ==================== B1 ====================

    {
        "id": "b1_tekamolo",
        "title": "TEKAMOLO - Die Reihenfolge im Satz",
        "level": "B1",
        "category": "Wortstellung",
        "explanation": """Im deutschen Satz gibt es eine feste Reihenfolge für Angaben (Adverbien und Adverbiale). Diese Reihenfolge heißt TEKAMOLO:

**TE** = Temporal (Wann?) → Zeit
**KA** = Kausal (Warum?) → Grund
**MO** = Modal (Wie?) → Art und Weise
**LO** = Lokal (Wo? Wohin?) → Ort

Die Grundregel: **Zuerst WANN, dann WARUM, dann WIE, dann WO.**

Wenn mehrere Angaben im Satz sind, kommen sie in dieser Reihenfolge - nicht umgekehrt.""",
        "examples": [
            {
                "label": "Richtig (TE → LO)",
                "sentence": "Ich fahre **morgen** (TE) **mit dem Zug** (MO) **nach Berlin** (LO).",
                "note": "Zuerst wann, dann wie, dann wohin."
            },
            {
                "label": "Falsch",
                "sentence": "Ich fahre nach Berlin morgen mit dem Zug.",
                "note": "Lokal steht nicht vor Temporal."
            },
            {
                "label": "Berufliches Beispiel",
                "sentence": "Der Kunde hat **gestern** (TE) **wegen des Fehlers** (KA) **telefonisch** (MO) **im Büro** (LO) angerufen.",
                "note": "Alle vier Elemente in der richtigen Reihenfolge."
            },
        ],
        "mistakes": [
            "Lokal vor Temporal stellen: ❌ 'Ich bin im Büro gestern gewesen.' → ✅ 'Ich bin gestern im Büro gewesen.'",
            "Modal vor Kausal stellen: ❌ 'Er hat telefonisch wegen des Problems angerufen.' → ✅ 'Er hat wegen des Problems telefonisch angerufen.'",
        ],
        "exercise_hint": "Lückentext: Sätze mit zwei oder drei Angaben, Student bringt sie in die richtige TEKAMOLO-Reihenfolge.",
    },

    {
        "id": "b1_konnektoren",
        "title": "Konnektoren - Sätze verbinden",
        "level": "B1",
        "category": "Konnektoren",
        "explanation": """Konnektoren verbinden zwei Sätze oder Satzteile. Es gibt drei Typen:

**1. Koordinierende Konnektoren** (Hauptsatz + Hauptsatz, Verb bleibt an Position 2):
- **und** (und), **aber** (but), **oder** (or), **denn** (because/for), **sondern** (but rather)

**2. Subordinierende Konnektoren** (leiten einen Nebensatz ein, Verb geht ans Ende):
- **weil** (because), **obwohl** (although), **wenn** (when/if), **dass** (that), **damit** (so that), **falls** (in case), **sodass** (so that), **während** (while), **bevor** (before), **nachdem** (after)

**3. Adverbiale Konnektoren** (stehen am Satzanfang, Verb kommt direkt danach - Inversion!):
- **deshalb / daher / deswegen** (therefore), **trotzdem** (nevertheless), **außerdem** (furthermore), **dennoch** (nevertheless)""",
        "examples": [
            {
                "label": "weil (Verb ans Ende)",
                "sentence": "Das Meeting wurde verschoben, **weil** der Kunde verhindert **war**.",
                "note": "Nach 'weil' geht das Verb ans Ende des Nebensatzes."
            },
            {
                "label": "obwohl (Verb ans Ende)",
                "sentence": "Wir haben das Projekt abgeschlossen, **obwohl** das Budget knapp **war**.",
                "note": "Gegensatz: obwohl = although/even though."
            },
            {
                "label": "deshalb (Inversion)",
                "sentence": "Das Budget ist begrenzt. **Deshalb müssen** wir Prioritäten setzen.",
                "note": "Nach 'deshalb' kommt sofort das Verb, dann das Subjekt."
            },
            {
                "label": "trotzdem (Inversion)",
                "sentence": "Es gab Probleme. **Trotzdem haben** wir die Deadline eingehalten.",
                "note": "trotzdem ≠ obwohl: trotzdem leitet einen neuen Hauptsatz ein."
            },
        ],
        "mistakes": [
            "weil mit Hauptsatzstellung: ❌ 'weil ich habe keine Zeit' → ✅ 'weil ich keine Zeit habe'",
            "trotzdem mit obwohl verwechseln: ❌ 'Obwohl, wir haben es geschafft.' → trotzdem/dennoch für neuen Satz",
            "denn vs. weil: 'denn' = Hauptsatz (kein Verb ans Ende), 'weil' = Nebensatz (Verb ans Ende)",
        ],
        "exercise_hint": "Satztransformation: Zwei Sätze mit dem richtigen Konnektor verbinden. Mischung aus weil/obwohl/trotzdem/deshalb.",
    },

    {
        "id": "b1_konjunktiv2",
        "title": "Konjunktiv II - Wünsche, Möglichkeiten, höfliche Bitten",
        "level": "B1",
        "category": "Verbformen",
        "explanation": """Der Konjunktiv II drückt aus:
- **Wünsche und Träume:** Was man gern hätte, aber (noch) nicht hat
- **Hypothesen:** Was wäre, wenn...
- **Höfliche Bitten:** Statt einer direkten Aufforderung
- **Ratschläge:** Was man tun sollte

**Bildung:**
- **würde + Infinitiv** (für fast alle Verben): ich würde gehen, wir würden arbeiten
- **Unregelmäßige Formen** (auswendig lernen!):
  - sein → **wäre** (ich wäre, er wäre)
  - haben → **hätte** (ich hätte, er hätte)
  - können → **könnte** (ich könnte)
  - müssen → **müsste** (ich müsste)
  - dürfen → **dürfte**
  - sollen → **sollte**
  - wollen → **wollte**""",
        "examples": [
            {
                "label": "Höfliche Bitte (beruflich)",
                "sentence": "**Könnten** Sie mir die Unterlagen bis Freitag schicken?",
                "note": "Viel höflicher als: 'Schicken Sie mir die Unterlagen.'"
            },
            {
                "label": "Hypothese",
                "sentence": "Wenn wir mehr Budget **hätten**, **würden** wir das Projekt sofort starten.",
                "note": "Wenn + Konjunktiv II im Nebensatz, würde im Hauptsatz."
            },
            {
                "label": "Ratschlag",
                "sentence": "An Ihrer Stelle **würde** ich das Angebot annehmen.",
                "note": "'An Ihrer Stelle' = klassische Einleitung für Ratschläge auf C1-Niveau."
            },
        ],
        "mistakes": [
            "würde + würde doppelt: ❌ 'Ich würde sein' → ✅ 'Ich wäre'",
            "würde + hätte: ❌ 'Ich würde haben' → ✅ 'Ich hätte'",
            "Konditionalsatz ohne wenn: 'Hätten wir mehr Zeit, würden wir...' (Inversion möglich ohne 'wenn')",
        ],
        "exercise_hint": "Satztransformation: Direkte Aussagen in höfliche Konjunktiv-II-Formen umschreiben. Fehlersuche mit den häufigsten Fehlern.",
    },

    {
        "id": "b1_passiv",
        "title": "Passiv - Vorgänge beschreiben",
        "level": "B1",
        "category": "Verbformen",
        "explanation": """Das Passiv benutzt man, wenn die Handlung wichtiger ist als die Person, die sie ausführt. Typisch in Berichten, E-Mails, formellen Texten.

**Bildung: werden + Partizip II**

| Zeitform | Aktiv | Passiv |
|----------|-------|--------|
| Präsens | Man prüft den Bericht. | Der Bericht **wird geprüft**. |
| Präteritum | Man prüfte den Bericht. | Der Bericht **wurde geprüft**. |
| Perfekt | Man hat den Bericht geprüft. | Der Bericht **ist geprüft worden**. |
| Futur | Man wird den Bericht prüfen. | Der Bericht **wird geprüft werden**. |

**Von wem?** Mit 'von + Dativ':
Der Bericht wurde **vom** (= von dem) Vorstand genehmigt.""",
        "examples": [
            {
                "label": "Präsens Passiv (beruflich)",
                "sentence": "Die Daten **werden** täglich **aktualisiert**.",
                "note": "Wer es macht, ist egal oder unbekannt."
            },
            {
                "label": "Präteritum Passiv",
                "sentence": "Das Projekt **wurde** im letzten Quartal **abgeschlossen**.",
                "note": "Typisch in Berichten über vergangene Ereignisse."
            },
            {
                "label": "mit von",
                "sentence": "Der Vertrag **wurde** vom Geschäftsführer **unterzeichnet**.",
                "note": "'von + Dativ' für den Handelnden (Agent)."
            },
        ],
        "mistakes": [
            "sein-Passiv mit werden verwechseln: 'Die Tür ist geschlossen.' (Zustand/Adjektiv) vs. 'Die Tür wird geschlossen.' (Vorgang)",
            "Perfekt Passiv: ❌ 'wurde geprüft worden' → ✅ 'ist geprüft worden'",
            "Kein Akkusativobjekt im Passiv: ❌ 'Er wird geholfen.' → ✅ 'Ihm wird geholfen.' (helfen + Dativ bleibt Dativ)",
        ],
        "exercise_hint": "Satztransformation: Aktivsätze ins Passiv umformen (Präsens und Präteritum). Dann Passivsätze zurück ins Aktiv.",
    },

    {
        "id": "b1_relativsaetze",
        "title": "Relativsätze - Nomen näher beschreiben",
        "level": "B1",
        "category": "Satzkonstruktion",
        "explanation": """Relativsätze geben mehr Information über ein Nomen. Das Relativpronomen richtet sich nach:
1. **Genus** des Bezugsnomens (maskulin/feminin/neutral/Plural)
2. **Kasus** im Relativsatz (welche Rolle hat es im Nebensatz?)

| | Nom. | Akk. | Dat. | Gen. |
|--|------|------|------|------|
| mask. | **der** | **den** | **dem** | **dessen** |
| fem. | **die** | **die** | **der** | **deren** |
| neut. | **das** | **das** | **dem** | **dessen** |
| Pl. | **die** | **die** | **denen** | **deren** |

**Verb geht immer ans Ende des Relativsatzes!**""",
        "examples": [
            {
                "label": "Nominativ (der Kollege ist Subjekt im Nebensatz)",
                "sentence": "Das ist der Kollege, **der** das Projekt leitet.",
                "note": "'der Kollege' ist maskulin → 'der'; er ist Subjekt im Nebensatz → Nominativ"
            },
            {
                "label": "Akkusativ",
                "sentence": "Das ist das Dokument, **das** ich Ihnen geschickt habe.",
                "note": "'das Dokument' ist neutral → 'das'; es ist Objekt → Akkusativ"
            },
            {
                "label": "Dativ",
                "sentence": "Das ist der Kunde, **dem** wir das Angebot gemacht haben.",
                "note": "'dem Kunden' das Angebot machen → Dativ"
            },
            {
                "label": "mit Präposition",
                "sentence": "Das ist das Projekt, **auf das** wir uns gefreut haben.",
                "note": "sich freuen auf → Akkusativ; Präposition + Relativpronomen zusammen"
            },
        ],
        "mistakes": [
            "Verb nicht ans Ende: ❌ 'der Kollege, der leitet das Projekt' → ✅ 'der das Projekt leitet'",
            "Falschen Kasus: ❌ 'dem Dokument, das ich gesendet habe' → das Dokument ist Akkusativ-Objekt → 'das'",
            "was statt das: 'was' nur nach Pronomen (alles, nichts, etwas) oder nach einem ganzen Satz",
        ],
        "exercise_hint": "Lückentext: Relativpronomen in verschiedenen Kasus einsetzen. Satztransformation: Zwei Sätze mit Relativsatz verbinden.",
    },

    {
        "id": "b1_verben_kasus",
        "title": "Verben mit Dativ und Akkusativ",
        "level": "B1",
        "category": "Kasus",
        "explanation": """Die meisten Verben nehmen Akkusativ. Aber eine wichtige Gruppe von Verben nimmt immer **Dativ**. Diese muss man auswendig lernen.

**Wichtige Dativverben:**
helfen, danken, gratulieren, antworten, zustimmen, widersprechen, folgen, gehören, gefallen, passen, fehlen, begegnen, schaden, nützen, vertrauen, glauben (jemandem), zuhören

**Verben mit zwei Objekten (Dativ + Akkusativ):**
geben (Dat + Akk), schicken, zeigen, erklären, empfehlen, mitteilen, anbieten

Formel: **jemandem** (Dat) **etwas** (Akk) geben/schicken/zeigen...""",
        "examples": [
            {
                "label": "Dativverb",
                "sentence": "Ich danke **Ihnen** für Ihre schnelle Antwort.",
                "note": "'danken' nimmt immer Dativ: jemandem danken"
            },
            {
                "label": "Zwei Objekte",
                "sentence": "Ich schicke **dem Kunden** (Dat) **die Unterlagen** (Akk).",
                "note": "Person = Dativ, Sache = Akkusativ"
            },
            {
                "label": "zustimmen (Dativ)",
                "sentence": "Ich stimme **Ihrem Vorschlag** zu.",
                "note": "einem Vorschlag zustimmen → Dativ"
            },
        ],
        "mistakes": [
            "helfen mit Akkusativ: ❌ 'Ich helfe dich.' → ✅ 'Ich helfe dir.'",
            "antworten mit Akkusativ: ❌ 'Ich antworte dich.' → ✅ 'Ich antworte dir.'",
            "Reihenfolge bei zwei Pronomen: 'Ich gebe es ihm.' (Akk vor Dat wenn beide Pronomen)",
        ],
        "exercise_hint": "Lückentext: richtigen Kasus (ihm/ihn, ihr/sie, dem/den) einsetzen. Fehlersuche mit typischen Dativfehlern.",
    },

    # ==================== B2 ====================

    {
        "id": "b2_zweiteilige_konnektoren",
        "title": "Zweiteilige Konnektoren",
        "level": "B2",
        "category": "Konnektoren",
        "explanation": """Zweiteilige Konnektoren kommen immer in Paaren. Sie verbinden zwei Informationen und zeigen deren Beziehung.

| Konnektor | Bedeutung | Beispiel |
|-----------|-----------|---------|
| **sowohl...als auch** | both...and (positiv) | sowohl professionell als auch freundlich |
| **nicht nur...sondern auch** | not only...but also | nicht nur günstig, sondern auch effizient |
| **weder...noch** | neither...nor (negativ) | weder Zeit noch Geld |
| **entweder...oder** | either...or | entweder Montag oder Dienstag |
| **zwar...aber** | admittedly...but | zwar teuer, aber qualitativ hochwertig |
| **je...desto/umso** | the more...the more | je mehr Daten, desto besser die Analyse |""",
        "examples": [
            {
                "label": "sowohl...als auch",
                "sentence": "Das Konzept überzeugt **sowohl** inhaltlich **als auch** visuell.",
                "note": "Keine Negation; betont, dass BEIDE Aspekte zutreffen."
            },
            {
                "label": "nicht nur...sondern auch",
                "sentence": "Wir bieten **nicht nur** günstige Preise, **sondern auch** erstklassigen Service.",
                "note": "Verstärkt: Es gibt noch mehr als erwartet."
            },
            {
                "label": "je...desto",
                "sentence": "**Je** früher wir starten, **desto** mehr Zeit haben wir für Korrekturen.",
                "note": "Nach 'je': Nebensatzstellung. Nach 'desto': Inversion (Verb dann Subjekt)."
            },
            {
                "label": "zwar...aber",
                "sentence": "Das Angebot ist **zwar** teuer, **aber** die Qualität rechtfertigt den Preis.",
                "note": "Einräumung: Man gibt etwas zu, aber relativiert es dann."
            },
        ],
        "mistakes": [
            "sowohl...wie auch: regional möglich, aber 'als auch' ist Standard",
            "je...umso/desto: Nach 'desto/umso' kommt das Adjektiv/Adverb direkt, dann Verb: 'desto besser ist das Ergebnis'",
            "weder...noch mit Verb: 'Er hat weder angerufen noch eine E-Mail geschickt.' (Verb bleibt an Position 2 im Hauptsatz)",
        ],
        "exercise_hint": "Satztransformation: Zwei Sätze mit zweiteiligem Konnektor verbinden. Kategoriensortierung: welcher Konnektor passt in welche Situation.",
    },

    {
        "id": "b2_passiv_modal",
        "title": "Passiv mit Modalverben",
        "level": "B2",
        "category": "Verbformen",
        "explanation": """Modalverben können mit dem Passiv kombiniert werden. Sehr häufig in formellen Texten, Anweisungen, Berichten.

**Bildung: Modalverb + Partizip II + werden (Infinitiv)**

| Zeitform | Formel | Beispiel |
|----------|--------|---------|
| Präsens | muss/kann/soll + PP + werden | Das muss erledigt werden. |
| Präteritum | musste/konnte/sollte + PP + werden | Das musste genehmigt werden. |
| Perfekt | hat + PP + werden + müssen | Das hat erledigt werden müssen. |

**Häufigste Kombinationen:**
- **muss...werden** → Pflicht/Notwendigkeit
- **kann...werden** → Möglichkeit
- **soll...werden** → Auftrag/Plan
- **darf nicht...werden** → Verbot""",
        "examples": [
            {
                "label": "Präsens (Pflicht)",
                "sentence": "Der Bericht **muss** bis Freitag **eingereicht werden**.",
                "note": "Passiv mit müssen: Partizip II + werden am Ende."
            },
            {
                "label": "Präteritum",
                "sentence": "Der Vertrag **musste** vom Anwalt **geprüft werden**.",
                "note": "Modalverb ins Präteritum, Passivteil bleibt gleich."
            },
            {
                "label": "Möglichkeit",
                "sentence": "Die Kosten **können** noch **reduziert werden**.",
                "note": "Passiv mit können: etwas ist möglich."
            },
        ],
        "mistakes": [
            "Wortstellung: ❌ 'muss werden eingereicht' → ✅ 'muss eingereicht werden'",
            "Perfekt Passiv mit Modal ist sehr komplex - im Telc B2 reicht Präsens und Präteritum",
        ],
        "exercise_hint": "Satztransformation: Aktivsätze mit Modalverben ins Passiv umformen. Lückentext: richtiges Modalverb + Passiv einsetzen.",
    },

    {
        "id": "b2_infinitivkonstruktionen",
        "title": "Infinitivkonstruktionen: um...zu, ohne...zu, anstatt...zu",
        "level": "B2",
        "category": "Satzkonstruktion",
        "explanation": """Diese drei Konstruktionen ersetzen Nebensätze mit 'damit', 'ohne dass', 'anstatt dass'. Sie sind kürzer und eleganter - typisch für C1-Niveau.

**Bedingung:** Das Subjekt beider Sätze muss GLEICH sein!

| Konstruktion | Bedeutung | Ersetzt |
|-------------|-----------|---------|
| **um...zu** | in order to (Ziel) | damit + gleiche Person |
| **ohne...zu** | without doing sth | ohne dass + gleiche Person |
| **anstatt...zu** | instead of doing | anstatt dass + gleiche Person |

**Bildung:** Konstruktion + Infinitiv ganz ans Ende""",
        "examples": [
            {
                "label": "um...zu (Ziel)",
                "sentence": "Ich rufe an, **um** einen Termin **zu** vereinbaren.",
                "note": "Ziel/Zweck: warum tut man etwas? Gleiche Person (ich)."
            },
            {
                "label": "ohne...zu",
                "sentence": "Er hat die E-Mail beantwortet, **ohne** die Anhänge **zu** lesen.",
                "note": "Er hat beantwortet UND er hat nicht gelesen - gleiche Person."
            },
            {
                "label": "anstatt...zu",
                "sentence": "**Anstatt** lange **zu** diskutieren, sollten wir eine Entscheidung treffen.",
                "note": "Ersatz für eine andere Handlung - gleiche Person."
            },
            {
                "label": "Verschiedene Personen → damit (kein Infinitiv möglich)",
                "sentence": "Ich erkläre das, **damit** mein Kollege es versteht.",
                "note": "Verschiedene Personen → 'damit' + Nebensatz, NICHT 'um...zu'"
            },
        ],
        "mistakes": [
            "Verschiedene Personen: ❌ 'Ich erkläre das, um er es zu verstehen.' → ✅ 'damit er es versteht'",
            "zu vergessen: ❌ 'um einen Termin vereinbaren' → ✅ 'um einen Termin zu vereinbaren'",
            "Trennbare Verben: 'um anzurufen' (nicht 'um zu anrufen')",
        ],
        "exercise_hint": "Satztransformation: damit/ohne dass/anstatt dass in Infinitivkonstruktionen umformen und umgekehrt.",
    },

    {
        "id": "b2_partizipialkonstruktionen",
        "title": "Partizipialkonstruktionen als Adjektiv",
        "level": "B2",
        "category": "Satzkonstruktion",
        "explanation": """Partizipien (I und II) können wie Adjektive vor einem Nomen stehen. Das ersetzt einen Relativsatz und klingt formeller.

**Partizip I** (Verb + -end) = aktiver, laufender Vorgang
→ das Partizip I beschreibt etwas, das gerade passiert

**Partizip II** (gemacht, geschrieben...) = abgeschlossener oder passiver Vorgang
→ das Partizip II beschreibt etwas, das schon fertig ist oder passiv ist

**Deklination:** Das Partizip wird wie ein Adjektiv dekliniert!""",
        "examples": [
            {
                "label": "Partizip I (aktiv, laufend)",
                "sentence": "Das **laufende** Projekt muss bis Ende des Monats abgeschlossen werden.",
                "note": "laufen → laufend → das laufende Projekt (Relativsatz: das Projekt, das gerade läuft)"
            },
            {
                "label": "Partizip II (passiv/abgeschlossen)",
                "sentence": "Das **abgeschlossene** Projekt wurde präsentiert.",
                "note": "abschließen → abgeschlossen → das abgeschlossene Projekt"
            },
            {
                "label": "Erweitertes Partizip (C1-Niveau)",
                "sentence": "Der **vom Vorstand genehmigte** Bericht liegt jetzt vor.",
                "note": "Der Bericht, der vom Vorstand genehmigt wurde → komprimiert vor dem Nomen"
            },
        ],
        "mistakes": [
            "Partizip I ohne Adjektivendung: ❌ 'das laufend Projekt' → ✅ 'das laufende Projekt'",
            "Partizip II statt I für aktive Vorgänge: ❌ 'der gearbeitete Kollege' → nicht möglich",
        ],
        "exercise_hint": "Satztransformation: Relativsätze in Partizipialkonstruktionen umformen. Fehlersuche mit falschen Partizipien.",
    },

    {
        "id": "b2_indirekte_rede",
        "title": "Indirekte Rede - Konjunktiv I",
        "level": "B2",
        "category": "Verbformen",
        "explanation": """Die indirekte Rede benutzt man, wenn man wiedergibt, was jemand anderes gesagt hat. Dafür braucht man den **Konjunktiv I**.

**Bildung Konjunktiv I:** Verbstamm + Endungen (-e, -est, -e, -en, -et, -en)

| Person | sein | haben | kommen |
|--------|------|-------|--------|
| ich | sei | habe | komme |
| er/sie | **sei** | **habe** | **komme** |
| wir | seien | haben* | kommen* |

*Wenn Konjunktiv I = Indikativ (z.B. 'wir haben'), nimmt man **Konjunktiv II** stattdessen.

**Einleitungsverben:** sagen, berichten, erklären, betonen, behaupten, mitteilen""",
        "examples": [
            {
                "label": "Direkt → Indirekt",
                "sentence": "Der Kunde sagt: 'Ich bin zufrieden.' → Der Kunde sagt, er **sei** zufrieden.",
                "note": "er ist → er sei (Konjunktiv I von 'sein')"
            },
            {
                "label": "mit haben",
                "sentence": "Sie berichtet: 'Wir haben das Problem gelöst.' → Sie berichtet, sie **hätten** das Problem gelöst.",
                "note": "'wir haben' = Indikativ, deshalb Konjunktiv II: 'hätten'"
            },
            {
                "label": "Beruflicher Kontext",
                "sentence": "Der Vorstand teilte mit, das Projekt **werde** pünktlich abgeschlossen.",
                "note": "werden → werde (Konjunktiv I) für Zukunft in indirekter Rede"
            },
        ],
        "mistakes": [
            "Konjunktiv I bei 'ich': 'ich sei' klingt sehr formell - in Alltagssprache oft Konjunktiv II",
            "Zeitform vergessen: direkte Rede Vergangenheit → indirekte Rede mit Konjunktiv I Perfekt: 'er habe gesagt'",
            "dass weglassen: 'Er sagt, er sei krank.' (kein 'dass' nötig, aber Wortstellung ändert sich)",
        ],
        "exercise_hint": "Satztransformation: Direkte Rede in indirekte Rede umwandeln. Berufliche Kontexte: Protokoll schreiben.",
    },

    {
        "id": "b2_genitiv_praepositionen",
        "title": "Genitiv-Präpositionen",
        "level": "B2",
        "category": "Kasus",
        "explanation": """Diese Präpositionen verlangen immer den **Genitiv**. Sie klingen formal und sind typisch für geschriebenes Deutsch und C1-Niveau.

**Die wichtigsten Genitiv-Präpositionen:**

| Präposition | Bedeutung |
|-------------|-----------|
| **wegen** | because of |
| **trotz** | despite |
| **während** | during |
| **aufgrund** | due to / because of |
| **anstatt / statt** | instead of |
| **innerhalb** | within |
| **außerhalb** | outside of |
| **mithilfe** | with the help of |
| **hinsichtlich** | with regard to |
| **bezüglich** | regarding |""",
        "examples": [
            {
                "label": "wegen + Genitiv",
                "sentence": "**Wegen des schlechten Wetters** wurde das Meeting verschoben.",
                "note": "das Wetter → des Wetters (Genitiv maskulin/neutral)"
            },
            {
                "label": "aufgrund + Genitiv",
                "sentence": "**Aufgrund der gestiegenen Kosten** müssen wir das Budget anpassen.",
                "note": "die Kosten → der Kosten (Genitiv Plural)"
            },
            {
                "label": "trotz + Genitiv",
                "sentence": "**Trotz des großen Drucks** hat das Team gute Arbeit geleistet.",
                "note": "der Druck → des Drucks (Genitiv maskulin)"
            },
            {
                "label": "bezüglich (formelle E-Mail)",
                "sentence": "**Bezüglich Ihrer Anfrage** vom 15. März teile ich Ihnen mit, dass...",
                "note": "Standard-Formulierung in Geschäftsbriefen."
            },
        ],
        "mistakes": [
            "wegen + Dativ (Umgangssprache): 'wegen dem Wetter' - im Telc immer Genitiv verwenden",
            "trotz + Dativ: ❌ 'trotz dem Problem' → ✅ 'trotz des Problems'",
            "Genitiv Plural: 'aufgrund der Ergebnisse' (nicht 'der Ergebnissen')",
        ],
        "exercise_hint": "Lückentext: richtige Genitivform nach Genitiv-Präpositionen einsetzen. Satztransformation: 'weil'-Satz in Genitiv-Präposition umformen.",
    },

    {
        "id": "b2_modalpartikeln",
        "title": "Modalpartikeln - Gefühle und Haltungen ausdrücken",
        "level": "B2",
        "category": "Wortschatz",
        "explanation": """Modalpartikeln (auch: Abtönungspartikeln) geben einem Satz eine emotionale Färbung. Sie zeigen die Haltung des Sprechers. Sie sind nicht übersetzbar - man lernt sie durch Kontext.

**Die wichtigsten:**

| Partikel | Typische Bedeutung | Typischer Kontext |
|----------|-------------------|-------------------|
| **doch** | Bestätigung erwünscht; Widerspruch; Erinnerung | Das wissen Sie doch! / Kommen Sie doch rein! |
| **mal** | Bitte lockerer machen; kurze Handlung | Schauen Sie mal hier. / Kommen Sie mal kurz. |
| **ja** | Selbstverständlichkeit; leichte Warnung | Das ist ja klar. / Das wissen wir ja alle. |
| **eigentlich** | Einschränkung; eigentliche Meinung | Das ist eigentlich eine gute Idee (aber...). |
| **halt/eben** | keine Alternative; so ist es nun mal | Das dauert halt etwas länger. |
| **wohl** | Vermutung | Er ist wohl krank. |""",
        "examples": [
            {
                "label": "doch (Erinnerung/Vorwurf)",
                "sentence": "Das haben wir **doch** bereits besprochen.",
                "note": "Signalisiert: Ich dachte, du weißt das schon."
            },
            {
                "label": "mal (höfliche Bitte)",
                "sentence": "Können Sie **mal** kurz ins Büro kommen?",
                "note": "'mal' macht eine Bitte lockerer und freundlicher."
            },
            {
                "label": "eigentlich (Einschränkung)",
                "sentence": "Das ist **eigentlich** eine gute Lösung, aber wir müssen die Kosten prüfen.",
                "note": "Zeigt: Im Prinzip ja, aber es gibt eine Einschränkung."
            },
        ],
        "mistakes": [
            "Modalpartikeln in formellen Briefen: 'mal' und 'halt' vermeiden - zu umgangssprachlich",
            "Position: Modalpartikeln stehen nie am Satzanfang (außer 'eigentlich')",
        ],
        "exercise_hint": "Mehrfachauswahl: welche Modalpartikel passt in welchen Kontext. Übersetzung: englische Sätze mit passendem Ton ins Deutsche.",
    },

    # ==================== C1 ====================

    {
        "id": "c1_nominalstil",
        "title": "Nominalstil - Verben in Nomen umwandeln",
        "level": "C1",
        "category": "Stil",
        "explanation": """Nominalstil bedeutet: statt eines Verbs benutzt man ein Nomen. Das klingt formeller, kompakter und ist typisch für Berichte, Protokolle, wissenschaftliche Texte und C1-Niveau.

**Häufige Nominalisierungen:**

| Verb | Nomen |
|------|-------|
| entscheiden | die Entscheidung |
| analysieren | die Analyse |
| entwickeln | die Entwicklung |
| prüfen | die Prüfung |
| vorstellen | die Vorstellung / die Präsentation |
| verbessern | die Verbesserung |
| durchführen | die Durchführung |
| berücksichtigen | die Berücksichtigung |

**Typische Konstruktionen mit Nominalstil:**
- eine Entscheidung **treffen** (statt: entscheiden)
- eine Analyse **durchführen** (statt: analysieren)
- einen Beitrag **leisten** (statt: beitragen)
- in Betracht **ziehen** (statt: bedenken)""",
        "examples": [
            {
                "label": "Verbal → Nominal",
                "sentence": "❌ Verbal: 'Wir haben entschieden, das Projekt zu starten.'\n✅ Nominal: 'Die Entscheidung, das Projekt zu starten, wurde getroffen.'",
                "note": "Nominal klingt distanzierter und formeller."
            },
            {
                "label": "Typische C1-Formulierung",
                "sentence": "Die **Umsetzung** der Strategie erfordert eine sorgfältige **Planung** und klare **Verantwortlichkeiten**.",
                "note": "Drei Nominalisierungen in einem Satz - typisch für Berichte."
            },
            {
                "label": "Feste Ausdrücke",
                "sentence": "Wir **ziehen** auch alternative Lösungen **in Betracht**.",
                "note": "'in Betracht ziehen' = fester Nominalstil-Ausdruck für 'bedenken/erwägen'"
            },
        ],
        "mistakes": [
            "Zu viel Nominalstil: Texte werden schwer lesbar. Mischung aus Verbal- und Nominalstil ist ideal.",
            "Falsche Präposition: 'die Entscheidung über + Akk.', 'die Analyse von + Dat.', 'die Lösung für + Akk.'",
        ],
        "exercise_hint": "Satztransformation: Verbalsätze in Nominalsätze umformen und umgekehrt. Typisch für C1-Schreibaufgaben.",
    },

    {
        "id": "c1_passiv_ersatzformen",
        "title": "Passiv-Ersatzformen: sein...zu und sich lassen",
        "level": "C1",
        "category": "Verbformen",
        "explanation": """Statt des Passivs kann man im Deutschen elegantere Konstruktionen verwenden. Diese sind typisch für C1.

**1. sein + zu + Infinitiv** (= muss/kann + Passiv)
→ Drückt Notwendigkeit oder Möglichkeit aus
→ Typisch in formellen Texten, Anweisungen

**2. sich lassen + Infinitiv** (= kann + Passiv)
→ Drückt Möglichkeit aus
→ Etwas ist machbar/realisierbar

**3. Adjektiv auf -bar / -lich** (= kann + Passiv)
→ lösbar, machbar, erreichbar, vermeidbar""",
        "examples": [
            {
                "label": "sein...zu (Notwendigkeit)",
                "sentence": "Die Unterlagen **sind** bis Freitag **einzureichen**.",
                "note": "= Die Unterlagen müssen bis Freitag eingereicht werden."
            },
            {
                "label": "sein...zu (Möglichkeit)",
                "sentence": "Das Problem **ist** noch **zu lösen**.",
                "note": "= Das Problem kann noch gelöst werden."
            },
            {
                "label": "sich lassen (Möglichkeit)",
                "sentence": "Die Kosten **lassen sich** noch **reduzieren**.",
                "note": "= Die Kosten können noch reduziert werden. Eleganter!"
            },
            {
                "label": "-bar Adjektiv",
                "sentence": "Das Ziel ist **erreichbar**, wenn wir die Ressourcen richtig einsetzen.",
                "note": "erreichen → erreichbar (= kann erreicht werden)"
            },
        ],
        "mistakes": [
            "sein...zu mit transitiven Verben: nur möglich wenn das Subjekt das Passiv-Objekt ist",
            "sich lassen nicht reflexiv: 'Das Problem lässt sich lösen' - kein 'sich' beim Infinitiv",
        ],
        "exercise_hint": "Satztransformation: Passivsätze in sein...zu und sich lassen umformen. Wortbildung: Adjektive auf -bar bilden.",
    },

    {
        "id": "c1_konzessivsaetze",
        "title": "Konzessivsätze - Einräumungen und Gegensätze",
        "level": "C1",
        "category": "Konnektoren",
        "explanation": """Konzessivsätze drücken einen Gegensatz aus: Obwohl X, passiert Y trotzdem. Auf C1-Niveau gibt es viele Möglichkeiten, diesen Gegensatz auszudrücken.

| Mittel | Typ | Beispiel |
|--------|-----|---------|
| **obwohl** | Konnektor (Nebensatz) | obwohl es teuer war, ... |
| **trotzdem / dennoch** | Adverb (Inversion) | Es war teuer. Trotzdem... |
| **obgleich / obschon** | formell (= obwohl) | obgleich die Kosten stiegen... |
| **wenngleich** | sehr formell | wenngleich das Risiko besteht... |
| **auch wenn** | Konnektor | Auch wenn es schwierig ist, ... |
| **selbst wenn** | Konnektor (Hypothese) | Selbst wenn wir scheitern, ... |
| **ungeachtet** + Genitiv | Präposition (formell) | ungeachtet der Kosten |""",
        "examples": [
            {
                "label": "obwohl vs. trotzdem",
                "sentence": "**Obwohl** das Budget knapp war, haben wir das Projekt erfolgreich abgeschlossen. / Das Budget war knapp. **Trotzdem** haben wir das Projekt abgeschlossen.",
                "note": "Beide bedeuten dasselbe - aber unterschiedliche Satzstruktur."
            },
            {
                "label": "auch wenn (Hypothese oder Realität)",
                "sentence": "**Auch wenn** der Aufwand hoch ist, lohnt sich die Investition.",
                "note": "Kann real oder hypothetisch sein."
            },
            {
                "label": "ungeachtet (sehr formell)",
                "sentence": "**Ungeachtet der** wirtschaftlichen Lage hat das Unternehmen seine Ziele erreicht.",
                "note": "Formellste Variante - typisch für Geschäftsberichte."
            },
        ],
        "mistakes": [
            "trotzdem mit Nebensatzstellung: ❌ 'trotzdem es teuer war' → trotzdem leitet Hauptsatz ein",
            "obwohl am Satzende: ❌ 'Es war teuer obwohl.' → obwohl leitet immer einen Nebensatz ein",
        ],
        "exercise_hint": "Satztransformation: obwohl ↔ trotzdem umformen. Fehlersuche mit Konzessivfehlern. Stil: verschiedene Konzessivformen in einen Text einbauen.",
    },

    {
        "id": "c1_erweiterte_partizipien",
        "title": "Erweiterte Partizipialkonstruktionen (C1)",
        "level": "C1",
        "category": "Satzkonstruktion",
        "explanation": """Auf C1-Niveau kann man ganze Relativsätze durch erweiterte Partizipialkonstruktionen ersetzen. Das klingt kompakter und formeller.

**Prinzip:** Alles, was im Relativsatz steht (außer dem Relativpronomen und dem Verb), steht jetzt zwischen Artikel und Nomen.

**Schema:** der/die/das + [Erweiterung] + Partizip + Nomen

**Nur möglich wenn:**
- Das Partizip I oder II als Adjektiv steht
- Die Erweiterung eindeutig ist""",
        "examples": [
            {
                "label": "Relativsatz → Partizip II Konstruktion",
                "sentence": "Der Bericht, **der vom Vorstand genehmigt wurde** → Der **vom Vorstand genehmigte** Bericht",
                "note": "Partizip II (passiv/abgeschlossen) + Adjektivdeklination"
            },
            {
                "label": "Relativsatz → Partizip I Konstruktion",
                "sentence": "Die Kosten, **die kontinuierlich steigen** → Die **kontinuierlich steigenden** Kosten",
                "note": "Partizip I (aktiv/laufend) + Adjektivdeklination"
            },
            {
                "label": "In einem Satz",
                "sentence": "Die **im letzten Quartal erzielten** Ergebnisse übertreffen die Erwartungen.",
                "note": "Die Ergebnisse, die im letzten Quartal erzielt wurden → komprimiert."
            },
        ],
        "mistakes": [
            "Zu lang: Sehr lange erweiterte Partizipien sind schwer lesbar - max. 3-4 Wörter zwischen Artikel und Partizip",
            "Falsche Deklination: das Partizip muss wie ein Adjektiv dekliniert werden",
        ],
        "exercise_hint": "Satztransformation: Relativsätze in erweiterte Partizipialkonstruktionen umformen (und zurück). C1-Schreibaufgaben mit Textoptimierung.",
    },

    {
        "id": "c1_kausale_finale_konsekutive",
        "title": "Kausale, finale und konsekutive Konnektoren (C1)",
        "level": "C1",
        "category": "Konnektoren",
        "explanation": """Auf C1-Niveau benutzt man präzisere Konnektoren als nur 'weil' und 'deshalb'. Hier sind die wichtigsten mit ihren Nuancen:

**KAUSAL (Grund angeben):**
- **weil** (weil + Nebensatz, allgemein)
- **da** (da + Nebensatz, formeller; Grund ist bekannt)
- **aufgrund + Genitiv** (formell, schriftlich)
- **angesichts + Genitiv** (in Anbetracht einer Situation)

**FINAL (Ziel/Zweck angeben):**
- **damit** (damit + Nebensatz, verschiedene Personen)
- **um...zu** (gleiche Person, Infinitiv)
- **mit dem Ziel + zu** (sehr formell)
- **zwecks + Genitiv** (sehr formell, geschäftlich)

**KONSEKUTIV (Folge/Ergebnis):**
- **sodass** (sodass + Nebensatz, Folge)
- **deshalb / daher / deswegen** (Inversion, Folge)
- **folglich / infolgedessen** (formell, Schlussfolgerung)
- **so...dass** (Grad + Folge: Es war so teuer, dass...)""",
        "examples": [
            {
                "label": "da (bekannter Grund, formell)",
                "sentence": "**Da** das Budget bereits genehmigt ist, können wir sofort starten.",
                "note": "'da' statt 'weil' wenn der Grund schon bekannt ist - klingt formeller."
            },
            {
                "label": "zwecks (sehr formell)",
                "sentence": "Wir treffen uns **zwecks** der Projektbesprechung.",
                "note": "zwecks + Genitiv - sehr formell, typisch in Behörden und Geschäftsbriefen."
            },
            {
                "label": "infolgedessen (Schlussfolgerung)",
                "sentence": "Die Nachfrage ist gestiegen. **Infolgedessen** müssen wir die Produktion erhöhen.",
                "note": "Formeller als 'deshalb'; typisch in Berichten und Analysen."
            },
            {
                "label": "so...dass (Grad + Folge)",
                "sentence": "Die Ergebnisse waren **so** überzeugend, **dass** der Vorstand sofort zustimmte.",
                "note": "Graduierung + Konsequenz in einem Satz."
            },
        ],
        "mistakes": [
            "da am Satzende: ❌ 'wir starten da das Budget genehmigt ist' → Verb ans Ende: 'da das Budget genehmigt ist'",
            "zwecks + Dativ: ❌ 'zwecks dem Gespräch' → ✅ 'zwecks des Gesprächs' (Genitiv)",
        ],
        "exercise_hint": "Kategoriensortierung: Konnektoren nach kausal/final/konsekutiv einordnen. Satztransformation: einfache Konnektoren durch formellere ersetzen.",
    },
]
