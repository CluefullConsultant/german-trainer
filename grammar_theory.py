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
        "level": "C1",
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

    # ==================== VERB TABLES ====================

    {
        "id": "verben_schwach_stark",
        "title": "Schwache, starke und gemischte Verben - alle Stammformen",
        "level": "B1",
        "category": "Verben",
        "explanation": """**Schwache Verben (regelmäßig)** bilden das Präteritum mit **-te** und das Partizip II mit **ge-...-t**.
**Starke Verben (unregelmäßig)** verändern den Vokal im Stammteil - diese Formen muss man auswendig lernen.
**Gemischte Verben** ändern den Vokal wie starke Verben, nehmen aber die Endung -te/-t wie schwache Verben - eine kleine, feste Liste.

Die drei **Stammformen** (Hauptformen) jedes Verbs:
**Infinitiv → Präteritum (er/sie) → Partizip II**

---

### Wie erkenne ich, ob ein Verb stark oder schwach ist?

Es gibt keine 100%-Regel, aber diese Muster helfen sehr:

1. **Schwach ist der Normalfall.** Jedes neue oder geliehene Verb ist automatisch schwach. Alle Verben auf **-ieren** sind IMMER schwach: studieren, organisieren, informieren, telefonieren.
2. **Starke Verben sind eine feste, geschlossene Liste** (ca. 150-200 Verben). Es kommen keine neuen starken Verben dazu. Es sind die ältesten, häufigsten Verben: sein, haben, gehen, kommen, sehen, nehmen, sprechen, finden, essen, trinken...
3. **Zusammengesetzte Verben erben den Typ vom Basisverb.** Wenn 'stehen' stark ist (stand, gestanden), sind auch verstehen, aufstehen, entstehen, bestehen automatisch stark - gleiches Muster.
4. **Der Praxistest:** Sagen Sie das Verb im Präteritum laut. Will der Vokal sich ändern (spreche → sprach)? → stark. Bleibt der Vokal gleich und nur -te kommt dazu (mache → machte)? → schwach.

**Praktischer Rat:** Nicht versuchen, es logisch herzuleiten - die ca. 150 Basisverben auswendig lernen (siehe Tabellen unten). Jedes Verb, das auf einem bekannten Basisverb aufbaut (mit be-/ver-/ent-/auf-/ab- usw.), folgt automatisch dem gleichen Muster.

---

### Schwache Verben (regelmäßig)
| Infinitiv | Präteritum | Partizip II | Bedeutung |
|-----------|-----------|-------------|-----------|
| machen | machte | gemacht | to do/make |
| arbeiten | arbeitete | gearbeitet | to work |
| kaufen | kaufte | gekauft | to buy |
| spielen | spielte | gespielt | to play |
| lernen | lernte | gelernt | to learn |
| fragen | fragte | gefragt | to ask |
| sagen | sagte | gesagt | to say |
| suchen | suchte | gesucht | to search |
| brauchen | brauchte | gebraucht | to need |
| leben | lebte | gelebt | to live |
| glauben | glaubte | geglaubt | to believe |
| hören | hörte | gehört | to hear |
| zeigen | zeigte | gezeigt | to show |
| wohnen | wohnte | gewohnt | to live (reside) |
| schicken | schickte | geschickt | to send |
| kosten | kostete | gekostet | to cost |
| bedeuten | bedeutete | bedeutet | to mean |
| erklären | erklärte | erklärt | to explain |
| bestätigen | bestätigte | bestätigt | to confirm |
| vereinbaren | vereinbarte | vereinbart | to arrange |
| informieren | informierte | informiert | to inform |
| organisieren | organisierte | organisiert | to organise |
| analysieren | analysierte | analysiert | to analyse |
| präsentieren | präsentierte | präsentiert | to present |
| diskutieren | diskutierte | diskutiert | to discuss |

---

### Starke Verben A1-A2 (unregelmäßig - auswendig lernen!)
| Infinitiv | Präteritum | Partizip II | Bedeutung |
|-----------|-----------|-------------|-----------|
| sein | war | **gewesen** | to be |
| haben | hatte | **gehabt** | to have |
| werden | wurde | **geworden** | to become |
| gehen | ging | **gegangen** | to go |
| kommen | kam | **gekommen** | to come |
| fahren | fuhr | **gefahren** | to drive/travel |
| sehen | sah | **gesehen** | to see |
| geben | gab | **gegeben** | to give |
| nehmen | nahm | **genommen** | to take |
| lesen | las | **gelesen** | to read |
| schreiben | schrieb | **geschrieben** | to write |
| sprechen | sprach | **gesprochen** | to speak |
| stehen | stand | **gestanden** | to stand |
| treffen | traf | **getroffen** | to meet |
| wissen | wusste | **gewusst** | to know (fact) |
| tragen | trug | **getragen** | to carry/wear |
| rufen | rief | **gerufen** | to call |
| laufen | lief | **gelaufen** | to run/walk |
| bleiben | blieb | **geblieben** | to stay |
| finden | fand | **gefunden** | to find |
| essen | aß | **gegessen** | to eat |
| trinken | trank | **getrunken** | to drink |
| schlafen | schlief | **geschlafen** | to sleep |
| heißen | hieß | **geheißen** | to be called |

---

### Starke Verben B1-B2
| Infinitiv | Präteritum | Partizip II | Bedeutung |
|-----------|-----------|-------------|-----------|
| helfen | half | **geholfen** | to help |
| verstehen | verstand | **verstanden** | to understand |
| verlieren | verlor | **verloren** | to lose |
| gewinnen | gewann | **gewonnen** | to win |
| halten | hielt | **gehalten** | to hold/stop |
| entscheiden | entschied | **entschieden** | to decide |
| empfehlen | empfahl | **empfohlen** | to recommend |
| einladen | lud ein | **eingeladen** | to invite |
| anfangen | fing an | **angefangen** | to begin |
| aufstehen | stand auf | **aufgestanden** | to get up |
| steigen | stieg | **gestiegen** | to climb/rise |
| ziehen | zog | **gezogen** | to pull/move |
| bitten | bat | **gebeten** | to ask/request |
| vergessen | vergaß | **vergessen** | to forget |
| beginnen | begann | **begonnen** | to begin |
| beschreiben | beschrieb | **beschrieben** | to describe |
| erscheinen | erschien | **erschienen** | to appear |
| vorschlagen | schlug vor | **vorgeschlagen** | to suggest |
| anbieten | bot an | **angeboten** | to offer |
| aufweisen | wies auf | **aufgewiesen** | to show/exhibit |

---

### Starke Verben C1 (häufig in formellen Texten)
| Infinitiv | Präteritum | Partizip II | Bedeutung |
|-----------|-----------|-------------|-----------|
| übertreffen | übertraf | **übertroffen** | to surpass |
| beweisen | bewies | **bewiesen** | to prove |
| vorantreiben | trieb voran | **vorangetrieben** | to drive forward |
| unterliegen | unterlag | **unterlegen** | to be subject to |
| abweichen | wich ab | **abgewichen** | to deviate |
| beitragen | trug bei | **beigetragen** | to contribute |
| einbeziehen | bezog ein | **einbezogen** | to include |
| voraussetzen | setzte voraus | **vorausgesetzt** | to presuppose |
| hervorgehen | ging hervor | **hervorgegangen** | to emerge from |
| zurückgreifen | griff zurück | **zurückgegriffen** | to fall back on |

---

### Gemischte Verben (kleine, feste Liste - Vokalwechsel wie stark, Endung wie schwach)
| Infinitiv | Präteritum | Partizip II | Bedeutung |
|-----------|-----------|-------------|-----------|
| kennen | kannte | **gekannt** | to know (be acquainted with) |
| nennen | nannte | **genannt** | to name |
| brennen | brannte | **gebrannt** | to burn |
| rennen | rannte | **gerannt** | to run |
| senden | sandte | **gesandt** | to send (formal) |
| wenden | wandte | **gewandt** | to turn |
| denken | dachte | **gedacht** | to think |
| bringen | brachte | **gebracht** | to bring |
| wissen | wusste | **gewusst** | to know (a fact) |

---

### Gemischte Verben - volle Konjugation (Präsens und Präteritum, alle Personen)

**wissen** (Präsens ist unregelmäßig - Vorsicht!)
| Person | Präsens | Präteritum |
|--------|---------|-----------|
| ich | **weiß** | wusste |
| du | **weißt** | wusstest |
| er/sie/es | **weiß** | wusste |
| wir | wissen | wussten |
| ihr | wisst | wusstet |
| sie/Sie | wissen | wussten |

**bringen** (Präsens regelmäßig, Präteritum mit Vokalwechsel)
| Person | Präsens | Präteritum |
|--------|---------|-----------|
| ich | bringe | brachte |
| du | bringst | brachtest |
| er/sie/es | bringt | brachte |
| wir | bringen | brachten |
| ihr | bringt | brachtet |
| sie/Sie | bringen | brachten |

**kennen** (Präsens regelmäßig, Präteritum mit Vokalwechsel)
| Person | Präsens | Präteritum |
|--------|---------|-----------|
| ich | kenne | kannte |
| du | kennst | kanntest |
| er/sie/es | kennt | kannte |
| wir | kennen | kannten |
| ihr | kennt | kanntet |
| sie/Sie | kennen | kannten |

**denken** (gleiches Muster wie bringen/kennen)
| Person | Präsens | Präteritum |
|--------|---------|-----------|
| ich | denke | dachte |
| du | denkst | dachtest |
| er/sie/es | denkt | dachte |
| wir | denken | dachten |
| ihr | denkt | dachtet |
| sie/Sie | denken | dachten |

Die übrigen gemischten Verben (nennen, brennen, rennen, senden, wenden) folgen demselben Muster wie kennen: Präsens komplett regelmäßig, nur das Präteritum und Partizip II ändern den Vokal.

**Alle Zeitformen im Zusammenhang** (Präsens, Präteritum, Perfekt, Plusquamperfekt, Futur) werden in der separaten Regel **"Die Zeitformen im Überblick"** erklärt.""",
        "examples": [
            {
                "label": "Schwaches Verb im Satz",
                "sentence": "Er **schickte** gestern die Unterlagen. → Die Unterlagen wurden **geschickt**.",
                "note": "schicken → schickte → geschickt: regelmäßig, kein Vokalwechsel."
            },
            {
                "label": "Starkes Verb im Satz",
                "sentence": "Sie **traf** den Kunden um 10 Uhr. → Sie hat den Kunden **getroffen**.",
                "note": "treffen → traf → getroffen: Vokal ändert sich (e → a → o)."
            },
            {
                "label": "Perfekt mit sein (Bewegung/Zustandswechsel)",
                "sentence": "Er **ist** nach Berlin **gefahren**. / Sie **ist** gekommen.",
                "note": "Verben der Bewegung und des Zustandswechsels bilden Perfekt mit SEIN, nicht haben."
            },
            {
                "label": "Gemischtes Verb im Satz",
                "sentence": "Ich **kannte** den Kollegen schon vorher. → Ich habe ihn schon **gekannt**.",
                "note": "kennen → kannte → gekannt: Vokal ändert sich (e → a) wie bei starken Verben, aber Endung -te/-t wie bei schwachen Verben."
            },
        ],
        "mistakes": [
            "Perfekt mit sein vs. haben: fahren/gehen/kommen/bleiben/sein → sein; die meisten anderen → haben",
            "Partizip II ohne ge-: Verben mit be-/er-/ver-/ent- haben KEIN ge-: bestätigt (nicht gebestätigt), erklärt (nicht geerklärt)",
            "Trennbare Verben: ge- kommt zwischen Präfix und Stamm: einladen → einGEladen, aufstehen → aufGEstanden",
            "Gemischte Verben wie schwach behandeln: ❌ 'ich denkte' → ✅ 'ich dachte' (Vokal ändert sich trotz -te-Endung)",
        ],
        "exercise_hint": "Lückentext: richtiges Präteritum oder Partizip II einsetzen. Fehlersuche: falsche Perfektformen mit haben/sein.",
    },

    {
        "id": "verben_modalverben",
        "title": "Modalverben - alle Formen",
        "level": "A2",
        "category": "Verben",
        "explanation": """Modalverben stehen mit einem zweiten Verb im Infinitiv (am Satzende). Sie drücken Notwendigkeit, Möglichkeit, Erlaubnis oder Wollen aus.

**Die 6 Modalverben:**

| | dürfen | können | mögen | müssen | sollen | wollen |
|--|--------|--------|-------|--------|--------|--------|
| **ich** | darf | kann | mag | muss | soll | will |
| **du** | darfst | kannst | magst | musst | sollst | willst |
| **er/sie/es** | darf | kann | mag | muss | soll | will |
| **wir** | dürfen | können | mögen | müssen | sollen | wollen |
| **ihr** | dürft | könnt | mögt | müsst | sollt | wollt |
| **sie/Sie** | dürfen | können | mögen | müssen | sollen | wollen |

**Präteritum (wichtig!):**
| | dürfen | können | mögen | müssen | sollen | wollen |
|--|--------|--------|-------|--------|--------|--------|
| **ich/er** | durfte | konnte | mochte | musste | sollte | wollte |

**Partizip II** (für Perfekt - selten aber wichtig):
gedurft / gekonnt / gemocht / gemusst / gesollt / gewollt
*(Aber: wenn ein Infinitiv dabei steht → Infinitiv statt Partizip II: "Ich habe kommen **können**")*

---

**Was bedeutet welches Modalverb?**

| Verb | Bedeutung | Beispiel |
|------|-----------|---------|
| **müssen** | Notwendigkeit (Pflicht, innere Notwendigkeit) | Ich muss das Formular ausfüllen. |
| **sollen** | Auftrag von außen (jemand anderes sagt es) | Sie sollen um 9 Uhr erscheinen. |
| **können** | Fähigkeit oder Möglichkeit | Ich kann Ihnen morgen helfen. |
| **dürfen** | Erlaubnis (oder Verbot mit nicht) | Sie dürfen das Büro betreten. |
| **wollen** | eigener Wille/Plan | Ich will das Projekt leiten. |
| **mögen** | Vorliebe; in indirekter Rede auch Wunsch | Er mag keine langen Meetings. |
| **möchten** | höflicher Wunsch (Konjunktiv II von mögen) | Ich möchte einen Termin vereinbaren. |""",
        "examples": [
            {
                "label": "müssen vs. sollen",
                "sentence": "Ich **muss** früher gehen. (innerer Grund) / Ich **soll** früher gehen. (Chef hat es gesagt)",
                "note": "müssen = eigene Notwendigkeit; sollen = Auftrag von außen"
            },
            {
                "label": "dürfen nicht = Verbot",
                "sentence": "Sie **dürfen** diese Daten **nicht** weitergeben.",
                "note": "dürfen nicht = ist verboten (nicht: muss nicht)"
            },
            {
                "label": "müssen nicht = keine Pflicht",
                "sentence": "Sie **müssen** nicht kommen, wenn Sie keine Zeit haben.",
                "note": "müssen nicht ≠ dürfen nicht: müssen nicht = es ist nicht nötig"
            },
        ],
        "mistakes": [
            "dürfen nicht vs. müssen nicht: ❌ 'Sie dürfen nicht pünktlich sein.' → ✅ 'Sie müssen nicht pünktlich sein.' (keine Pflicht)",
            "Wortstellung: Modalverb Position 2, Infinitiv ans Ende: ❌ 'Ich muss gehen früher.' → ✅ 'Ich muss früher gehen.'",
            "Perfekt mit Doppel-Infinitiv: 'Ich habe gehen müssen.' (nicht 'gemusst' wenn Infinitiv dabei)",
        ],
        "exercise_hint": "Lückentext: richtiges Modalverb einsetzen. Mehrfachauswahl: müssen/sollen/dürfen unterscheiden.",
    },

    {
        "id": "verben_reflexiv",
        "title": "Reflexive Verben (sich-Verben)",
        "level": "B1",
        "category": "Verben",
        "explanation": """Reflexive Verben haben ein Reflexivpronomen (sich, mich, dich...). Das Reflexivpronomen zeigt, dass die Handlung auf das Subjekt zurückfällt.

**Reflexivpronomen:**
| Person | Akkusativ | Dativ |
|--------|-----------|-------|
| ich | **mich** | **mir** |
| du | **dich** | **dir** |
| er/sie/es | **sich** | **sich** |
| wir | **uns** | **uns** |
| ihr | **euch** | **euch** |
| sie/Sie | **sich** | **sich** |

**Wann Akkusativ, wann Dativ?**
→ Akkusativ: wenn es kein anderes Akkusativobjekt gibt
→ Dativ: wenn es ein anderes Akkusativobjekt gibt

**Wichtige reflexive Verben:**

| Verb | Kasus | Bedeutung |
|------|-------|-----------|
| sich freuen auf | + Akk | to look forward to |
| sich freuen über | + Akk | to be happy about |
| sich bewerben um | + Akk | to apply for |
| sich kümmern um | + Akk | to take care of |
| sich erinnern an | + Akk | to remember |
| sich gewöhnen an | + Akk | to get used to |
| sich konzentrieren auf | + Akk | to concentrate on |
| sich beziehen auf | + Akk | to refer to |
| sich entscheiden für | + Akk | to decide for |
| sich beschäftigen mit | + Dat | to deal with |
| sich befassen mit | + Dat | to be concerned with |
| sich treffen mit | + Dat | to meet with |
| sich abzeichnen | (kein Obj.) | to become apparent |
| sich entwickeln | (kein Obj.) | to develop |
| sich handeln um | + Akk | to be about (Es handelt sich um...) |""",
        "examples": [
            {
                "label": "Akkusativ-Reflexiv",
                "sentence": "Ich **bewerbe mich** um die Stelle als Berater.",
                "note": "sich bewerben um: mich = Akkusativ (kein anderes Akkusativobjekt)"
            },
            {
                "label": "Dativ-Reflexiv (mit Akkusativobjekt)",
                "sentence": "Ich mache **mir** Notizen während des Meetings.",
                "note": "Notizen = Akkusativobjekt → Reflexivpronomen wird Dativ: mir"
            },
            {
                "label": "Beruflicher Kontext",
                "sentence": "Das Projekt **entwickelt sich** sehr positiv. / Es **handelt sich um** einen strategischen Fehler.",
                "note": "sich entwickeln und sich handeln um sind sehr häufig in Berichten."
            },
        ],
        "mistakes": [
            "mir vs. mich: 'Ich wasche mich.' (kein anderes Objekt → Akk) vs. 'Ich wasche mir die Hände.' (Hände = Akk → Reflexiv wird Dat)",
            "sich im Infinitiv: 'Er möchte sich bewerben.' (sich bleibt immer dabei)",
        ],
        "exercise_hint": "Lückentext: richtiges Reflexivpronomen (mich/mir/sich) einsetzen. Fehlersuche mit reflexiven Verben.",
    },

    {
        "id": "verben_trennbar_untrennbar",
        "title": "Trennbare und untrennbare Verben",
        "level": "A2",
        "category": "Verben",
        "explanation": """Manche Verben haben ein **Präfix** (Vorsilbe). Dieses Präfix ist entweder **trennbar** oder **untrennbar**.

**Untrennbare Präfixe** (nie getrennt, kein Stress):
**be-, er-, ge-, ver-, zer-, ent-, emp-, miss-**
→ Partizip II: KEIN ge- davor

| Verb | Präteritum | Partizip II |
|------|-----------|-------------|
| besuchen | besuchte | besucht |
| erklären | erklärte | erklärt |
| verstehen | verstand | verstanden |
| vergessen | vergaß | vergessen |
| entscheiden | entschied | entschieden |
| empfehlen | empfahl | empfohlen |

**Trennbare Präfixe** (trennen sich im Hauptsatz, Verb ans Ende):
**an-, auf-, aus-, ein-, mit-, vor-, zu-, ab-, nach-, her-, hin-, zurück-, weiter-**
→ Partizip II: ge- kommt ZWISCHEN Präfix und Stamm

| Verb | Hauptsatz | Partizip II |
|------|-----------|-------------|
| anrufen | Er **ruft** mich **an**. | an**ge**rufen |
| aufmachen | Er **macht** das Fenster **auf**. | auf**ge**macht |
| einladen | Ich **lade** Sie **ein**. | ein**ge**laden |
| vorschlagen | Sie **schlägt** das **vor**. | vor**ge**schlagen |
| mitteilen | Er **teilt** es mit. | mit**ge**teilt |
| anfangen | Wir **fangen** jetzt **an**. | an**ge**fangen |
| aufweisen | Die Daten **weisen** Fehler **auf**. | auf**ge**wiesen |
| beitragen | Das **trägt** viel **bei**. | bei**ge**tragen |

**Verben mit zwei möglichen Bedeutungen:**
übersetzen (trennbar) = to ferry across / übersetzen (untrennbar) = to translate
umfahren (trennbar) = to knock over / umfahren (untrennbar) = to drive around""",
        "examples": [
            {
                "label": "Trennbar im Hauptsatz",
                "sentence": "Ich **rufe** Sie morgen **an**.",
                "note": "anrufen: 'an' geht ans Ende des Hauptsatzes."
            },
            {
                "label": "Trennbar im Nebensatz (NICHT getrennt)",
                "sentence": "Ich bin froh, dass ich Sie **anrufen** kann.",
                "note": "Im Nebensatz bleibt das Verb zusammen - Infinitiv ans Ende."
            },
            {
                "label": "Partizip II trennbar",
                "sentence": "Haben Sie schon **angerufen**?",
                "note": "ge- zwischen an und rufen: an-ge-rufen"
            },
        ],
        "mistakes": [
            "Partizip II untrennbar mit ge-: ❌ 'gebesucht, geerklärt' → ✅ 'besucht, erklärt'",
            "Trennbar im Nebensatz trennen: ❌ 'dass ich rufe an' → ✅ 'dass ich anrufe'",
        ],
        "exercise_hint": "Lückentext: trennbare Verben in verschiedenen Zeitformen einsetzen. Fehlersuche mit Partizip-II-Bildung.",
    },

    # ==================== PRÄPOSITIONEN ====================

    {
        "id": "praepositionen_kasus",
        "title": "Präpositionen mit Kasus - Übersicht",
        "level": "A2",
        "category": "Kasus",
        "explanation": """Jede Präposition verlangt einen bestimmten Kasus. Das ist fest - man kann es nicht wählen.

---

### Immer AKKUSATIV:
| Präposition | Bedeutung | Beispiel |
|-------------|-----------|---------|
| **durch** | through | durch den Park |
| **für** | for | für den Kunden |
| **gegen** | against | gegen den Plan |
| **ohne** | without | ohne den Kollegen |
| **um** | around / at (time) | um den Tisch / um 9 Uhr |
| **bis** | until / up to | bis nächsten Montag |
| **entlang** | along | den Fluss entlang |

---

### Immer DATIV:
| Präposition | Bedeutung | Beispiel |
|-------------|-----------|---------|
| **aus** | from / out of | aus dem Büro |
| **bei** | at / with / near | beim (= bei dem) Chef |
| **mit** | with | mit dem Team |
| **nach** | after / to (cities) | nach Berlin / nach dem Meeting |
| **seit** | since / for (time) | seit einem Jahr |
| **von** | from / of / by | von dem Projekt / vom Chef |
| **zu** | to (people/places) | zum (= zu dem) Arzt |
| **gegenüber** | opposite / towards | dem Kunden gegenüber |
| **außer** | except | außer mir |

---

### WECHSELPRÄPOSITIONEN (Akk oder Dat - je nach Kontext):
**an, auf, hinter, in, neben, über, unter, vor, zwischen**

**Regel:**
- **Akkusativ** = Bewegung/Richtung (Wohin?) → Veränderung des Ortes
- **Dativ** = Position/Zustand (Wo?) → kein Ortswechsel

| | Akkusativ (Wohin?) | Dativ (Wo?) |
|--|-------------------|-------------|
| **an** | Ich gehe **an den** Schreibtisch. | Ich sitze **am** (= an dem) Schreibtisch. |
| **auf** | Ich lege das Buch **auf den** Tisch. | Das Buch liegt **auf dem** Tisch. |
| **in** | Ich gehe **in das** (ins) Büro. | Ich bin **im** (= in dem) Büro. |
| **über** | Ich hänge das Bild **über den** Schreibtisch. | Das Bild hängt **über dem** Schreibtisch. |

---

### Immer GENITIV:
wegen, trotz, während, aufgrund, anstatt, innerhalb, außerhalb, mithilfe, bezüglich, hinsichtlich
*(Siehe separate Regel: Genitiv-Präpositionen)*""",
        "examples": [
            {
                "label": "auf + Akkusativ (Wohin?)",
                "sentence": "Ich lege die Unterlagen **auf den** Tisch.",
                "note": "Bewegung → wohin? → Akkusativ"
            },
            {
                "label": "auf + Dativ (Wo?)",
                "sentence": "Die Unterlagen liegen **auf dem** Tisch.",
                "note": "Position → wo? → Dativ"
            },
            {
                "label": "in + Akkusativ vs. Dativ",
                "sentence": "Ich gehe **ins** Büro. (Wohin? Akk) / Ich arbeite **im** Büro. (Wo? Dat)",
                "note": "ins = in das (Akkusativ) / im = in dem (Dativ)"
            },
        ],
        "mistakes": [
            "nach vs. zu: nach + Städte/Länder/Hause; zu + Personen/Institutionen: 'nach Berlin' aber 'zum Arzt', 'zu meinem Kollegen'",
            "von vs. aus: aus = Herkunft aus einem Ort/Material; von = Ausgangspunkt oder Urheber: 'aus Deutschland' (Herkunft), 'von dem Chef' (Urheber)",
            "bei + Dativ immer: ❌ 'bei den Chef' → ✅ 'beim Chef' (bei dem = beim)",
        ],
        "exercise_hint": "Lückentext: Akkusativ oder Dativ nach Wechselpräpositionen. Mehrfachauswahl: richtige Präposition wählen.",
    },

    {
        "id": "verben_mit_praepositionen",
        "title": "Verben mit festen Präpositionen",
        "level": "B1",
        "category": "Kasus",
        "explanation": """Viele deutsche Verben sind fest mit einer Präposition verbunden. Die Präposition bestimmt den Kasus des folgenden Nomens. Diese Verbindungen muss man auswendig lernen - sie sind nicht logisch übersetzbar.

**Warum 'danken für'?**
'jemandem danken' (Dativ, für die Person) + 'für etwas' (Akkusativ, für den Grund) - die für-Phrase ist eine Ergänzung, nicht das Objekt des Verbs selbst. Das gilt für viele Verben: sie haben ein Objekt (Dativ/Akkusativ) UND eine Präpositionalergänzung.

---

### Verben + für + Akkusativ
| Verb | Bedeutung | Beispiel |
|------|-----------|---------|
| danken für | to thank for | Ich danke Ihnen **für** Ihre Hilfe. |
| sich entscheiden für | to decide for | Wir entscheiden uns **für** Option A. |
| sich interessieren für | to be interested in | Er interessiert sich **für** das Projekt. |
| sich bedanken für | to thank for | Ich bedanke mich **für** das Feedback. |
| sorgen für | to take care of | Sie sorgt **für** die Organisation. |
| verantwortlich sein für | to be responsible for | Er ist **für** das Budget verantwortlich. |
| geeignet sein für | to be suitable for | Das ist **für** unsere Zwecke geeignet. |

---

### Verben + auf + Akkusativ
| Verb | Bedeutung | Beispiel |
|------|-----------|---------|
| warten auf | to wait for | Wir warten **auf** die Genehmigung. |
| sich freuen auf | to look forward to | Ich freue mich **auf** das Meeting. |
| sich beziehen auf | to refer to | Ich beziehe mich **auf** Ihre E-Mail. |
| sich konzentrieren auf | to concentrate on | Bitte konzentrieren Sie sich **auf** das Wesentliche. |
| sich vorbereiten auf | to prepare for | Ich bereite mich **auf** das Gespräch vor. |
| aufpassen auf | to pay attention to | Bitte passen Sie **auf** die Details auf. |
| hinweisen auf | to point out | Ich möchte **auf** ein Problem hinweisen. |
| reagieren auf | to react to | Wir reagieren **auf** Kundenfeedback. |
| sich verlassen auf | to rely on | Ich verlasse mich **auf** Ihr Team. |
| Wert legen auf | to value | Wir legen Wert **auf** Qualität. |

---

### Verben + an + Akkusativ
| Verb | Bedeutung | Beispiel |
|------|-----------|---------|
| denken an | to think of | Ich denke **an** den Termin. |
| sich erinnern an | to remember | Erinnern Sie sich **an** unser Gespräch? |
| sich gewöhnen an | to get used to | Ich gewöhne mich **an** die neue Struktur. |
| glauben an | to believe in | Wir glauben **an** unsere Strategie. |
| schreiben an | to write to | Ich schreibe **an** den Kunden. |
| appellieren an | to appeal to | Ich appelliere **an** Ihr Verständnis. |

---

### Verben + über + Akkusativ
| Verb | Bedeutung | Beispiel |
|------|-----------|---------|
| sprechen über | to talk about | Wir sprechen **über** das Budget. |
| sich freuen über | to be pleased about | Ich freue mich **über** das Ergebnis. |
| sich beschweren über | to complain about | Der Kunde beschwert sich **über** die Lieferung. |
| nachdenken über | to think about | Ich denke **über** Ihren Vorschlag nach. |
| diskutieren über | to discuss | Wir diskutieren **über** die Optionen. |
| informieren über | to inform about | Bitte informieren Sie mich **über** die Änderungen. |
| berichten über | to report on | Er berichtet **über** den Projektfortschritt. |
| verfügen über | to have at one's disposal | Das Unternehmen verfügt **über** große Ressourcen. |

---

### Verben + mit + Dativ
| Verb | Bedeutung | Beispiel |
|------|-----------|---------|
| sprechen mit | to speak with | Ich spreche **mit** dem Kunden. |
| sich treffen mit | to meet with | Ich treffe mich **mit** dem Team. |
| sich beschäftigen mit | to deal with | Wir beschäftigen uns **mit** dem Problem. |
| beginnen mit | to begin with | Wir beginnen **mit** der Analyse. |
| aufhören mit | to stop doing | Er hört **mit** der Arbeit auf. |
| rechnen mit | to expect / count on | Ich rechne **mit** Verzögerungen. |
| zusammenarbeiten mit | to collaborate with | Wir arbeiten **mit** dem Kunden zusammen. |
| einverstanden sein mit | to agree with | Ich bin **mit** dem Vorschlag einverstanden. |

---

### Verben + von + Dativ
| Verb | Bedeutung | Beispiel |
|------|-----------|---------|
| abhängen von | to depend on | Das hängt **vom** Budget ab. |
| überzeugen von | to convince of | Ich überzeuge ihn **von** unserem Konzept. |
| sprechen von | to speak of | Er sprach **von** neuen Möglichkeiten. |
| profitieren von | to benefit from | Wir profitieren **von** der Zusammenarbeit. |
| ausgehen von | to assume / start from | Ich gehe **von** einer positiven Entwicklung aus. |

---

### Verben + in + Akkusativ
| Verb | Bedeutung | Beispiel |
|------|-----------|---------|
| sich einarbeiten in | to familiarise with | Ich arbeite mich **in** das Thema ein. |
| investieren in | to invest in | Wir investieren **in** neue Technologien. |
| einwilligen in | to consent to | Er willigt **in** den Vertrag ein. |

---

### Verben + um + Akkusativ
| Verb | Bedeutung | Beispiel |
|------|-----------|---------|
| bitten um | to ask for / request | Ich bitte **um** Ihre Genehmigung. |
| sich bewerben um | to apply for | Sie bewirbt sich **um** die Stelle. |
| sich handeln um | to be about | Es handelt sich **um** einen Fehler. |
| kämpfen um | to fight for | Wir kämpfen **um** den Auftrag. |
| sich kümmern um | to take care of | Ich kümmere mich **um** die Details. |

---

### Merkhilfe: PRÄP-FRAGEN
Bei Verben mit Präpositionen: **Wofür? Worauf? Womit? Wovon? Worüber?** (Sachen)
/ **Für wen? Auf wen? Mit wem? Von wem? Über wen?** (Personen)""",
        "examples": [
            {
                "label": "bitten um (nicht bitten für)",
                "sentence": "Ich bitte Sie **um** einen Termin.",
                "note": "bitten + um + Akkusativ - immer um, nie für"
            },
            {
                "label": "sich freuen auf vs. über",
                "sentence": "Ich freue mich **auf** das Meeting. (Zukunft) / Ich freue mich **über** das Ergebnis. (Vergangenheit/Gegenwart)",
                "note": "auf = Vorfreude auf etwas Zukünftiges; über = Freude über etwas Geschehenes"
            },
            {
                "label": "abhängen von (nicht auf)",
                "sentence": "Das **hängt vom** (= von dem) Budget **ab**.",
                "note": "abhängen von + Dativ - nicht: abhängen auf"
            },
        ],
        "mistakes": [
            "warten auf (nicht warten für): ❌ 'Ich warte für die Antwort.' → ✅ 'Ich warte auf die Antwort.'",
            "sich freuen über vs. auf durcheinander bringen: auf = Zukunft, über = Vergangenheit/Gegenwart",
            "bitten um vs. fragen nach: bitten um = to request; fragen nach = to ask about/enquire",
        ],
        "exercise_hint": "Lückentext: richtige Präposition einsetzen. Zuordnung: Verb + passende Präposition. Fehlersuche mit falschen Präpositionen.",
    },

    # ==================== ZEITFORMEN ====================

    {
        "id": "zeitformen_ueberblick",
        "title": "Die Zeitformen im Überblick - wann benutzt man was?",
        "level": "B1",
        "category": "Verben",
        "explanation": """Deutsch hat 6 Zeitformen (Tempora). Auf B1-C1-Niveau braucht man vor allem Präsens, Perfekt, Präteritum und Futur I - aber alle 6 sollte man erkennen können.

---

### 1. Präsens (Gegenwart) - "ich mache"
**Wann?** Aktuelle Handlungen, allgemeine Wahrheiten, Zukunft mit Zeitangabe, feste Vereinbarungen.
**Bildung:** Verbstamm + Endung (-e, -st, -t, -en, -t, -en)

### 2. Präteritum (einfache Vergangenheit) - "ich machte"
**Wann?** Schriftliche Erzählungen, Berichte, formelle Texte, schriftliches Deutsch allgemein. Auch: sein/haben/Modalverben werden fast immer im Präteritum benutzt, sogar in gesprochener Sprache ("ich war", "ich hatte", "ich konnte").
**Bildung schwach:** Stamm + -te (+ Endung); **stark:** Vokalwechsel + Endung

### 3. Perfekt (zusammengesetzte Vergangenheit) - "ich habe gemacht"
**Wann?** Gesprochene Sprache für die Vergangenheit (mündlich fast immer Perfekt, nicht Präteritum!). "Was hast du gestern gemacht?" - nicht "Was machtest du gestern?"
**Bildung:** haben/sein (Präsens) + Partizip II am Satzende

### 4. Plusquamperfekt (Vorvergangenheit) - "ich hatte gemacht"
**Wann?** Eine Handlung, die VOR einer anderen Vergangenheitshandlung passiert ist. Oft mit 'nachdem' oder 'bevor'.
**Bildung:** haben/sein im Präteritum + Partizip II

### 5. Futur I (Zukunft) - "ich werde machen"
**Wann?** Zukünftige Handlungen (aber oft nimmt man einfach Präsens + Zeitangabe!), Vermutungen über die Gegenwart, Versprechen/Vorsätze.
**Bildung:** werden (Präsens) + Infinitiv am Satzende

### 6. Futur II (vollendete Zukunft) - "ich werde gemacht haben"
**Wann?** Sehr selten. Eine Handlung, die in der Zukunft abgeschlossen sein wird. Oder: Vermutung über die Vergangenheit.
**Bildung:** werden (Präsens) + Partizip II + haben/sein (Infinitiv)

---

### Volle Konjugation - drei Beispielverben (schwach, stark, gemischt)

**machen (schwach)**
| Person | Präsens | Präteritum | Perfekt | Plusquamperfekt | Futur I |
|--------|---------|-----------|---------|-----------------|---------|
| ich | mache | machte | habe gemacht | hatte gemacht | werde machen |
| du | machst | machtest | hast gemacht | hattest gemacht | wirst machen |
| er/sie/es | macht | machte | hat gemacht | hatte gemacht | wird machen |
| wir | machen | machten | haben gemacht | hatten gemacht | werden machen |
| ihr | macht | machtet | habt gemacht | hattet gemacht | werdet machen |
| sie/Sie | machen | machten | haben gemacht | hatten gemacht | werden machen |

**sprechen (stark)**
| Person | Präsens | Präteritum | Perfekt | Plusquamperfekt | Futur I |
|--------|---------|-----------|---------|-----------------|---------|
| ich | spreche | sprach | habe gesprochen | hatte gesprochen | werde sprechen |
| du | **sprichst** | sprachst | hast gesprochen | hattest gesprochen | wirst sprechen |
| er/sie/es | **spricht** | sprach | hat gesprochen | hatte gesprochen | wird sprechen |
| wir | sprechen | sprachen | haben gesprochen | hatten gesprochen | werden sprechen |
| ihr | sprecht | spracht | habt gesprochen | hattet gesprochen | werdet sprechen |
| sie/Sie | sprechen | sprachen | haben gesprochen | hatten gesprochen | werden sprechen |

*Achtung: 'sprechen' hat Vokalwechsel im Präsens bei du/er (e → i) - das betrifft viele starke Verben (nehmen → nimmst, sehen → siehst, essen → isst).*

**bringen (gemischt)**
| Person | Präsens | Präteritum | Perfekt | Plusquamperfekt | Futur I |
|--------|---------|-----------|---------|-----------------|---------|
| ich | bringe | brachte | habe gebracht | hatte gebracht | werde bringen |
| du | bringst | brachtest | hast gebracht | hattest gebracht | wirst bringen |
| er/sie/es | bringt | brachte | hat gebracht | hatte gebracht | wird bringen |
| wir | bringen | brachten | haben gebracht | hatten gebracht | werden bringen |
| ihr | bringt | brachtet | habt gebracht | hattet gebracht | werdet bringen |
| sie/Sie | bringen | brachten | haben gebracht | hatten gebracht | werden bringen |""",
        "examples": [
            {
                "label": "Präteritum vs. Perfekt (mündlich vs. schriftlich)",
                "sentence": "Mündlich: 'Ich **habe** gestern mit dem Kunden **gesprochen**.' / Schriftlich (Bericht): 'Der Berater **sprach** gestern mit dem Kunden.'",
                "note": "Gleiche Bedeutung, andere Zeitform je nach Kontext - mündlich Perfekt, schriftlich oft Präteritum."
            },
            {
                "label": "sein/haben/Modalverben im Präteritum (auch mündlich!)",
                "sentence": "'Ich **war** gestern im Büro.' / 'Ich **konnte** die Frist nicht einhalten.'",
                "note": "Diese Verben benutzt man auch beim Sprechen im Präteritum, nicht im Perfekt."
            },
            {
                "label": "Plusquamperfekt (Vorvergangenheit)",
                "sentence": "Nachdem wir das Angebot **abgeschickt hatten**, rief der Kunde an.",
                "note": "Abschicken passierte VOR dem Anruf → Plusquamperfekt für die frühere Handlung."
            },
            {
                "label": "Futur I für Vermutung",
                "sentence": "Er **wird** wohl noch im Meeting **sein**.",
                "note": "Futur I drückt hier keine Zukunft aus, sondern eine Vermutung über die Gegenwart."
            },
        ],
        "mistakes": [
            "Perfekt statt Präteritum bei sein/haben: ❌ 'Ich bin gestern müde gewesen.' klingt unnatürlich → ✅ 'Ich war gestern müde.'",
            "Präteritum in der gesprochenen Alltagssprache übertreiben: für die meisten Verben ist mündlich Perfekt normal, nicht Präteritum",
            "Plusquamperfekt ohne klaren zeitlichen Bezug benutzen: nur wenn eine Handlung klar VOR einer anderen Vergangenheitshandlung liegt",
            "Futur I für einfache Zukunft überbenutzen: oft reicht Präsens + Zeitangabe: 'Ich fahre morgen nach Berlin' (nicht zwingend 'werde fahren')",
        ],
        "exercise_hint": "Satztransformation: Präsens ↔ Perfekt ↔ Präteritum umformen. Lückentext: richtige Zeitform je nach Kontext (mündlich/schriftlich) wählen.",
    },

    # ==================== ADJEKTIVE UND NOMEN ====================

    {
        "id": "adjektivdeklination",
        "title": "Adjektivdeklination - die richtige Endung finden",
        "level": "B1",
        "category": "Kasus",
        "explanation": """Ein Adjektiv vor einem Nomen bekommt immer eine Endung. Welche Endung, hängt von 3 Dingen ab:
1. **Welcher Artikel?** (bestimmt: der/die/das - unbestimmt: ein/eine - kein Artikel)
2. **Welcher Kasus?** (Nom/Akk/Dat/Gen)
3. **Welches Genus/welche Zahl?** (mask./fem./neutr./Plural)

**Grundprinzip:** Der Artikel ODER die Adjektivendung zeigt Genus und Kasus. Beide zusammen brauchen es nur einmal - deshalb gibt es nach bestimmtem Artikel meist nur **-e** oder **-en**.

---

### 1. Nach bestimmtem Artikel (der/die/das/die)
| | mask. | fem. | neutr. | Plural |
|--|-------|------|--------|--------|
| **Nom.** | der schnell**e** | die schnell**e** | das schnell**e** | die schnell**en** |
| **Akk.** | den schnell**en** | die schnell**e** | das schnell**e** | die schnell**en** |
| **Dat.** | dem schnell**en** | der schnell**en** | dem schnell**en** | den schnell**en** |
| **Gen.** | des schnell**en** | der schnell**en** | des schnell**en** | der schnell**en** |

→ **Merke:** Fast überall -en, außer Nom. (alle Genera) und Akk. fem./neutr. → dort -e.

---

### 2. Nach unbestimmtem Artikel (ein/eine/ein, kein, mein...)
| | mask. | fem. | neutr. | Plural |
|--|-------|------|--------|--------|
| **Nom.** | ein schnell**er** | eine schnell**e** | ein schnell**es** | keine schnell**en** |
| **Akk.** | einen schnell**en** | eine schnell**e** | ein schnell**es** | keine schnell**en** |
| **Dat.** | einem schnell**en** | einer schnell**en** | einem schnell**en** | keinen schnell**en** |
| **Gen.** | eines schnell**en** | einer schnell**en** | eines schnell**en** | keiner schnell**en** |

→ **Merke:** Im Nominativ (mask./neutr.) und Akkusativ (neutr.) trägt das Adjektiv die Endung, die der Artikel NICHT zeigt (weil 'ein' keine Endung hat).

---

### 3. Ohne Artikel (Nullartikel - z.B. bei unzählbaren Nomen oder Plural ohne Artikel)
| | mask. | fem. | neutr. | Plural |
|--|-------|------|--------|--------|
| **Nom.** | schnell**er** Kaffee | frisch**e** Milch | kalt**es** Wasser | frisch**e** Äpfel |
| **Akk.** | schnell**en** Kaffee | frisch**e** Milch | kalt**es** Wasser | frisch**e** Äpfel |
| **Dat.** | schnell**em** Kaffee | frisch**er** Milch | kalt**em** Wasser | frisch**en** Äpfeln |
| **Gen.** | schnell**en** Kaffees | frisch**er** Milch | kalt**en** Wassers | frisch**er** Äpfel |

→ **Merke:** Ohne Artikel trägt das Adjektiv die volle Endung des bestimmten Artikels (der→er, die→e, das→es, den→en...).""",
        "examples": [
            {
                "label": "Nach bestimmtem Artikel",
                "sentence": "Der neu**e** Kollege arbeitet seit Montag mit uns.",
                "note": "Nominativ maskulin nach 'der' → -e"
            },
            {
                "label": "Nach unbestimmtem Artikel",
                "sentence": "Wir haben ein**en** neu**en** Kollegen eingestellt.",
                "note": "Akkusativ maskulin nach 'einen' → -en (Artikel zeigt schon Akkusativ, Adjektiv folgt dem Standardmuster)"
            },
            {
                "label": "Beruflicher Kontext, Dativ",
                "sentence": "Wir haben mit unser**em** neu**en** Kunden ein gutes Gespräch geführt.",
                "note": "Dativ maskulin nach 'unserem' (possessiv, wie 'ein') → -en"
            },
            {
                "label": "Ohne Artikel",
                "sentence": "Gut**e** Ergebnisse erfordern sorgfältig**e** Planung.",
                "note": "Plural Nominativ ohne Artikel → -e; feminin Akkusativ ohne Artikel → -e"
            },
        ],
        "mistakes": [
            "Adjektivendung nach 'ein' im Nominativ mask. vergessen: ❌ 'ein neu Kollege' → ✅ 'ein neuer Kollege'",
            "-e statt -en im Dativ/Genitiv: ❌ 'mit dem neue Kollege' → ✅ 'mit dem neuen Kollegen'",
            "Mehrere Adjektive vor einem Nomen bekommen ALLE dieselbe Endung: 'der große, wichtige Kunde' (beide -e)",
        ],
        "exercise_hint": "Lückentext: richtige Adjektivendung in verschiedenen Kasus/Artikeltypen einsetzen. Fehlersuche mit typischen Endungsfehlern.",
    },

    {
        "id": "n_deklination",
        "title": "N-Deklination (schwache Maskulina)",
        "level": "B2",
        "category": "Kasus",
        "explanation": """Eine kleine Gruppe maskuliner Nomen bekommt in **allen Fällen außer Nominativ Singular** die Endung **-(e)n**. Das nennt man N-Deklination oder 'schwache Maskulina'.

**Betroffen sind vor allem:**
- Männliche Personen- und Berufsbezeichnungen auf **-e**: der Kunde, der Kollege, der Experte, der Praktikant (Ausnahme ohne -e, siehe unten)
- Nationalitäten auf -e: der Franzose, der Ire
- Einige männliche Wesen: der Mensch, der Herr, der Nachbar
- Wörter auf **-ant, -ent, -ist**: der Praktikant, der Präsident, der Journalist, der Assistent

| Kasus | Singular | Plural |
|-------|----------|--------|
| Nom. | der Kund**e** | die Kund**en** |
| Akk. | den Kund**en** | die Kund**en** |
| Dat. | dem Kund**en** | den Kund**en** |
| Gen. | des Kund**en** | der Kund**en** |

**Sonderfall 'der Name' und ähnliche (der Gedanke, der Glaube, der Wille):**
Diese bekommen im Genitiv Singular zusätzlich ein -s: **des Namens** (nicht: des Namen)""",
        "examples": [
            {
                "label": "der Kollege im Akkusativ",
                "sentence": "Ich habe meinen Kollege**n** um Hilfe gebeten.",
                "note": "Akkusativ → -n, nicht nur 'meinen Kollege'"
            },
            {
                "label": "der Kunde im Dativ",
                "sentence": "Wir haben dem Kund**en** ein neues Angebot gemacht.",
                "note": "Dativ → -en am Nomen selbst, zusätzlich zur Artikelendung"
            },
            {
                "label": "der Name (Sonderfall)",
                "sentence": "Die Bedeutung des Name**ns** war uns zunächst unklar.",
                "note": "Genitiv Singular: -ns statt nur -n bei 'der Name', 'der Gedanke', 'der Wille'"
            },
        ],
        "mistakes": [
            "Endung im Akkusativ/Dativ vergessen: ❌ 'Ich sehe den Kunde.' → ✅ 'Ich sehe den Kunden.'",
            "Genitiv bei 'der Name' ohne -s: ❌ 'des Namen' → ✅ 'des Namens'",
            "Nicht alle Maskulina auf -e sind schwach: 'der Käse', 'der Junge' (Junge ist schwach: den Jungen) - im Zweifel nachschlagen",
        ],
        "exercise_hint": "Lückentext: richtige Form von der Kunde/der Kollege/der Experte in verschiedenen Kasus. Fehlersuche mit fehlender -n-Endung.",
    },

    {
        "id": "wortbildung_theorie",
        "title": "Wortbildung - Nomen und Adjektive ableiten",
        "level": "B2",
        "category": "Wortschatz",
        "explanation": """Deutsch bildet neue Wörter systematisch mit Suffixen (Nachsilben). Wenn man die Muster kennt, kann man viele Wörter selbst ableiten - sehr nützlich für C1-Schreibaufgaben und Nominalstil.

---

### Nomen aus Verben
| Suffix | Genus | Beispiel | Bedeutung |
|--------|-------|----------|-----------|
| **-ung** | die | entscheiden → die Entscheid**ung** | sehr produktiv, funktioniert bei den meisten Verben |
| | | lösen → die Lös**ung** | |
| | | planen → die Plan**ung** | |
| **(ohne Suffix)** | die/der | analysieren → die Analyse | manche Verben bilden Nomen ohne Suffix |
| | | beginnen → der Beginn | |

### Nomen aus Adjektiven
| Suffix | Genus | Beispiel | Bedeutung |
|--------|-------|----------|-----------|
| **-heit** | die | wichtig → die Wichtig**heit** | nach Adjektiven auf -ig, -isch, -bar oft -heit |
| **-keit** | die | möglich → die Möglich**keit** | nach Adjektiven auf -lich, -sam oft -keit |
| | | schwierig → die Schwierig**keit** | |
| **-e** | die | schwach → die Schwäch**e** (mit Umlaut) | kurze Adjektive, oft mit Umlaut |

### Nomen mit anderen Suffixen
| Suffix | Genus | Beispiel |
|--------|-------|----------|
| **-schaft** | die | Mitglied → die Mitglied**schaft**; Freund → die Freund**schaft** |
| **-tum** | das | Eigentum, Wachstum |
| **-nis** | das | Ergebnis, Verständnis, Bedürfnis |
| **-ion/-tion** | die | organisieren → die Organisat**ion**; präsentieren → die Präsentat**ion** |

### Adjektive aus Nomen
| Suffix | Beispiel | Bedeutung |
|--------|----------|-----------|
| **-lich** | Geschäft → geschäft**lich** | |
| **-ig** | Wichtigkeit → wicht**ig** (Rückbildung), Ruhe → ruh**ig** | |
| **-isch** | Wirtschaft → wirtschaft**lich** / typisch, wirtschaft**lich** | |
| **-bar** | (aus Verben) lösen → lös**bar**, machen → mach**bar** | kann getan werden |
| **-voll** | Verantwortung → verantwortungs**voll** | |
| **-los** | Verantwortung → verantwortungs**los** | Gegenteil von -voll |

### Zusammengesetzte Nomen (Komposita)
Deutsch bildet oft lange Nomen durch Zusammensetzung. **Das letzte Wort bestimmt Genus und Bedeutung:**
die Kosten + die Analyse → **die Kostenanalyse**
der Kunde + die Zufriedenheit → **die Kundenzufriedenheit**
das Projekt + der Leiter → **der Projektleiter**
oft mit Fugen-s dazwischen: Verantwortung**s**bereich, Geschäft**s**bericht""",
        "examples": [
            {
                "label": "Verb → Nomen mit -ung",
                "sentence": "Nach sorgfältiger **Prüfung** haben wir eine **Entscheidung** getroffen.",
                "note": "prüfen → die Prüfung, entscheiden → die Entscheidung"
            },
            {
                "label": "Adjektiv → Nomen mit -keit",
                "sentence": "Die **Möglichkeit** einer Kostensenkung wird geprüft.",
                "note": "möglich → die Möglichkeit"
            },
            {
                "label": "Kompositum",
                "sentence": "Der **Kundenzufriedenheitsbericht** wird morgen präsentiert.",
                "note": "der Kunde + die Zufriedenheit + der Bericht - das letzte Wort bestimmt: der Bericht"
            },
        ],
        "mistakes": [
            "Falsches Genus bei -ung/-heit/-keit/-schaft/-ion: diese Suffixe sind IMMER feminin (die)",
            "Falsches Genus bei -tum/-nis: -tum ist neutrum (das), -nis ist meistens neutrum (das Ergebnis, aber die Kenntnis - Ausnahme!)",
            "Kompositum-Genus: nicht das erste, sondern das LETZTE Wort bestimmt Genus und Artikel",
        ],
        "exercise_hint": "Wortbildung-Aufgabe: Nomen aus Verben/Adjektiven ableiten. Zuordnung: Suffix zu passendem Genus.",
    },

    {
        "id": "adjektive_mit_praepositionen",
        "title": "Adjektive mit festen Präpositionen",
        "level": "B2",
        "category": "Kasus",
        "explanation": """Wie Verben sind auch viele Adjektive fest mit einer Präposition verbunden (meist mit 'sein' + Adjektiv + Präposition). Auch diese muss man auswendig lernen.

| Adjektiv | Präposition | Beispiel |
|----------|-------------|---------|
| stolz | auf + Akk | Wir sind **stolz auf** dieses Ergebnis. |
| zufrieden | mit + Dat | Der Kunde ist **zufrieden mit** der Lösung. |
| verantwortlich | für + Akk | Sie ist **verantwortlich für** das Budget. |
| abhängig | von + Dat | Der Erfolg ist **abhängig von** der Marktlage. |
| interessiert | an + Dat | Wir sind sehr **interessiert an** einer Zusammenarbeit. |
| überzeugt | von + Dat | Ich bin **überzeugt von** diesem Ansatz. |
| bekannt | für + Akk | Das Unternehmen ist **bekannt für** seine Qualität. |
| einverstanden | mit + Dat | Ich bin **einverstanden mit** dem Vorschlag. |
| begeistert | von + Dat | Das Team ist **begeistert von** der Idee. |
| besorgt | über + Akk | Wir sind **besorgt über** die Entwicklung. |
| enttäuscht | von/über + Dat/Akk | Er ist **enttäuscht von** dem Ergebnis. |
| erfahren | in + Dat | Sie ist sehr **erfahren in** diesem Bereich. |
| geeignet | für + Akk | Dieses Konzept ist **geeignet für** kleine Teams. |
| notwendig | für + Akk | Das Budget ist **notwendig für** den Erfolg. |
| vertraut | mit + Dat | Ich bin **vertraut mit** dem Thema. |""",
        "examples": [
            {
                "label": "verantwortlich für",
                "sentence": "Als Projektleiter bin ich **verantwortlich für** den gesamten Ablauf.",
                "note": "verantwortlich + für + Akkusativ"
            },
            {
                "label": "zufrieden mit",
                "sentence": "Wir sind sehr **zufrieden mit** der Zusammenarbeit.",
                "note": "zufrieden + mit + Dativ"
            },
            {
                "label": "abhängig von",
                "sentence": "Die Entscheidung ist **abhängig von** den verfügbaren Ressourcen.",
                "note": "abhängig + von + Dativ, nicht 'abhängig auf'"
            },
        ],
        "mistakes": [
            "verantwortlich mit statt für: ❌ 'verantwortlich mit dem Projekt' → ✅ 'verantwortlich für das Projekt'",
            "zufrieden für statt mit: ❌ 'zufrieden für die Lösung' → ✅ 'zufrieden mit der Lösung'",
            "interessiert für statt an: ❌ 'interessiert für das Projekt' → ✅ 'interessiert an dem Projekt'",
        ],
        "exercise_hint": "Lückentext: richtige Präposition nach Adjektiv einsetzen. Zuordnung: Adjektiv + passende Präposition.",
    },

    # ==================== SATZBAU ====================

    {
        "id": "negation_nicht_kein",
        "title": "Negation: nicht vs. kein",
        "level": "A2",
        "category": "Wortstellung",
        "explanation": """Deutsch hat zwei Wörter für 'nicht/kein' - welches man benutzt, hängt vom Nomen ab.

**kein** negiert ein Nomen mit unbestimmtem Artikel oder ohne Artikel:
Ich habe ein**en** Termin. → Ich habe **kein**en Termin.
Ich habe Zeit. → Ich habe **keine** Zeit.

**nicht** negiert:
- Verben: Ich **komme nicht**.
- Adjektive/Adverbien: Das ist **nicht** wichtig.
- Nomen mit bestimmtem Artikel: Das ist **nicht der** richtige Ansatz.
- den ganzen Satz (steht dann meist am Ende)

---

### Position von 'nicht'

**Ganzsatznegation** (der ganze Satz wird verneint) → **nicht am Ende:**
Ich verstehe die Frage **nicht**.

**Teilnegation** (nur ein Teil wird verneint) → **nicht direkt vor dem negierten Element:**
Ich arbeite **nicht** heute, sondern morgen. (nicht 'heute' wird negiert)
Er ist **nicht** freundlich. (nicht 'freundlich' wird negiert)

**Vor Präpositionalphrasen und Ortsangaben:** nicht kommt davor:
Ich fahre **nicht** nach Berlin, sondern nach München.""",
        "examples": [
            {
                "label": "kein (Nomen ohne bestimmten Artikel)",
                "sentence": "Wir haben **keine** Einigung erzielt.",
                "note": "eine Einigung → keine Einigung"
            },
            {
                "label": "nicht (Verb/Ganzsatz)",
                "sentence": "Der Kunde hat das Angebot **nicht** angenommen.",
                "note": "Ganzsatznegation → nicht möglichst weit hinten"
            },
            {
                "label": "nicht (Teilnegation)",
                "sentence": "Wir treffen uns **nicht** am Montag, sondern am Dienstag.",
                "note": "Nur 'am Montag' wird negiert, deshalb nicht direkt davor"
            },
        ],
        "mistakes": [
            "kein statt nicht bei bestimmtem Artikel: ❌ 'Das ist keine richtige Lösung.' wenn eigentlich gemeint ist: 'Das ist nicht die richtige Lösung.' (Kontext prüfen)",
            "nicht zu früh im Satz bei Ganzsatznegation: ❌ 'Ich nicht verstehe.' → ✅ 'Ich verstehe nicht.'",
            "kein vor Nomen mit Possessivpronomen: ❌ 'Das ist kein mein Problem.' → ✅ 'Das ist nicht mein Problem.' (Possessiv + nicht, nicht kein)",
        ],
        "exercise_hint": "Fehlersuche: nicht/kein verwechselt. Lückentext: richtige Negation je nach Nomen/Verb einsetzen.",
    },

    {
        "id": "indirekte_fragesaetze",
        "title": "Indirekte Fragesätze",
        "level": "B1",
        "category": "Satzkonstruktion",
        "explanation": """Eine indirekte Frage ist eine Frage, die in einen größeren Satz eingebettet ist. Typisch in höflichen Bitten und professioneller Kommunikation.

**Zwei Typen:**

**1. Ja/Nein-Fragen → mit 'ob'**
Direkte Frage: Kommt er? → Indirekt: Ich weiß nicht, **ob** er **kommt**.

**2. W-Fragen → W-Wort bleibt, Verb ans Ende**
Direkte Frage: Wann beginnt das Meeting? → Indirekt: Ich frage mich, **wann** das Meeting **beginnt**.

**Wichtig:** In beiden Fällen geht das Verb ans Ende des Nebensatzes (wie bei allen Nebensätzen).

**Typische Einleitungen (sehr nützlich für formelle Kommunikation):**
Ich möchte wissen, ob/wann/wie... / Können Sie mir sagen, ob/wann/wie... / Es ist unklar, ob/warum... / Ich frage mich, ob/wann...""",
        "examples": [
            {
                "label": "ob (Ja/Nein-Frage)",
                "sentence": "Können Sie mir sagen, **ob** die Lieferung heute **ankommt**?",
                "note": "Direkte Frage 'Kommt die Lieferung heute an?' wird mit 'ob' eingebettet, Verb ans Ende."
            },
            {
                "label": "W-Frage",
                "sentence": "Ich möchte wissen, **wann** wir mit den Ergebnissen **rechnen können**.",
                "note": "W-Wort 'wann' bleibt erhalten, Verb(en) ans Ende."
            },
            {
                "label": "Beruflicher Kontext",
                "sentence": "Es ist noch unklar, **warum** die Verzögerung **entstanden ist**.",
                "note": "Perfekt im Nebensatz: beide Verbteile (ist/entstanden) ans Ende, Hilfsverb zuletzt."
            },
        ],
        "mistakes": [
            "Hauptsatzstellung im Nebensatz: ❌ 'Ich weiß nicht, ob kommt er.' → ✅ 'ob er kommt'",
            "ob vergessen bei Ja/Nein-Fragen: ❌ 'Ich weiß nicht, kommt er.' → ✅ 'ob er kommt'",
            "wenn statt ob: 'wenn' ist nur für Bedingungen/Zeitangaben, nicht für indirekte Ja/Nein-Fragen",
        ],
        "exercise_hint": "Satztransformation: direkte Fragen in indirekte Fragesätze umformen. Nützlich für höfliche E-Mails und Nachfragen.",
    },
]
