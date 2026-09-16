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

**Verb geht immer ans Ende des Relativsatzes!**

**Relativsätze mit wo** (Ort/Zeit, oft eleganter als "in dem/an dem"):
"Das ist die Firma, **wo** ich gearbeitet habe." (= in der ich gearbeitet habe)
Bei Ortsnamen und geografischen Angaben ist "wo" sogar die einzig natürliche Option: "Berlin, wo ich wohne, ..." """,
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
- **so...dass** (Grad + Folge: Es war so teuer, dass...)

**IRREALE KONSEKUTIVSÄTZE (eine Folge, die NICHT eintritt):**
- **zu... als dass** + Konjunktiv II: die Folge im Nebensatz tritt gerade NICHT ein, weil der Grad zu hoch/niedrig ist
  "Das Projekt ist **zu** riskant, **als dass** wir es ohne Genehmigung starten **würden**." (= wir starten es nicht)
  Unterschied zu 'sodass': 'sodass' beschreibt eine wirkliche Folge, 'zu... als dass' eine verhinderte Folge - deshalb immer Konjunktiv II im Nebensatz.""",
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
            "Indikativ statt Konjunktiv II nach 'als dass': ❌ '...als dass wir es starten.' → ✅ '...als dass wir es starten würden.' (die verhinderte Folge braucht immer Konjunktiv II)",
        ],
        "exercise_hint": "Kategoriensortierung: Konnektoren nach kausal/final/konsekutiv einordnen. Satztransformation: einfache Konnektoren durch formellere ersetzen. Kontrastpaar sodass (reale Folge) vs. zu...als dass (verhinderte Folge).",
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
| **entlang** | along | den Fluss entlang (nachgestellt → Akk.; vorangestellt: 'entlang des Flusses' Gen./formell) |

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

→ **Merke:** Ohne Artikel trägt das Adjektiv die volle Endung des bestimmten Artikels (der→er, die→e, das→es, den→en...). **Ausnahme Genitiv mask./neutr.:** dort -en, nicht -es (kalt**en** Wassers, nicht 'kaltes Wassers') - das Nomen trägt bereits die Genitiv-Endung, das Adjektiv verdoppelt sie nicht.""",
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
        "level": "B1",
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
| **-isch** | Chaos → chaot**isch**, Typ → typ**isch** | |
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

    # ==================== VERBACHSEN: TEMPUS, MODUS, GENUS VERBI ====================

    {
        "id": "verb_drei_achsen",
        "title": "Die drei Achsen des Verbs: Tempus, Modus, Genus Verbi",
        "level": "C1",
        "category": "Verben",
        "explanation": """Jede deutsche Verbform ist eine Kombination aus drei unabhängigen Kategorien. Wenn man diese drei Achsen kennt, hört jede Verbform auf, isoliert und verwirrend zu wirken - sie ist einfach eine Kombination aus drei Entscheidungen.

**1. Tempus (Zeit) - WANN?**
Präsens, Präteritum, Perfekt, Plusquamperfekt, Futur I, Futur II
→ Siehe eigene Regel "Die Zeitformen im Überblick"

**2. Modus (Redeweise) - WELCHE HALTUNG zur Aussage?**
- **Indikativ** - Tatsache, das Normale (95% aller Sätze)
- **Konjunktiv I** - fremde Aussage wiedergegeben (indirekte Rede)
- **Konjunktiv II** - hypothetisch, unwirklich, Wunsch, höfliche Bitte
- **Imperativ** - Aufforderung, Befehl, Bitte
→ Siehe eigene Regeln "Indirekte Rede - Konjunktiv I", "Konjunktiv II", "Imperativ"

**3. Genus Verbi (Handlungsrichtung) - WER handelt, wer wird behandelt?**
- **Aktiv** - das Subjekt handelt selbst
- **Passiv** - das Subjekt wird behandelt, der Handelnde tritt zurück
→ Siehe eigene Regeln "Passiv", "Passiv mit Modalverben", "Passiv-Ersatzformen"

**Jede Verbform, die du siehst, ist ein Punkt in diesem dreidimensionalen Raum: eine Zeit + ein Modus + eine Richtung.**

---

### Naming-Falle: Modalverben ≠ Modus

"Modalverben" (können, müssen, dürfen, sollen, wollen, mögen) klingt wie "Modus", ist aber etwas völlig anderes: Modalverben sind eine lexikalische Gruppe von Verben. Modus ist die grammatische Kategorie oben (Indikativ/Konjunktiv/Imperativ). Nicht verwechseln.""",
        "examples": [
            {
                "label": "Alle drei Achsen in einer Form",
                "sentence": "**Er wäre gegangen.** = Konjunktiv II (Modus) + Plusquamperfekt (Tempus) + Aktiv (Genus Verbi)",
                "note": "Drei unabhängige Entscheidungen, in einer Verbform kombiniert."
            },
            {
                "label": "Andere Kombination",
                "sentence": "**Es wird gemacht.** = Indikativ (Modus) + Präsens (Tempus) + Passiv (Genus Verbi)",
                "note": "Gleiches Prinzip, andere Werte auf jeder Achse."
            },
            {
                "label": "Konjunktiv I Beispiel",
                "sentence": "**Er habe gesagt.** = Konjunktiv I (Modus) + Perfekt (Tempus) + Aktiv (Genus Verbi)",
                "note": "Typisch in indirekter Rede/Berichten: 'Der Kunde teilte mit, er habe das Angebot bereits erhalten.'"
            },
        ],
        "mistakes": [
            "Modalverben mit Modus verwechseln: 'können/müssen' sind Verben, keine Redeweise-Kategorie.",
            "Annehmen, Konjunktiv sei immer 'unwahrscheinlich': Konjunktiv I ist neutral berichtend, nicht automatisch zweifelhaft.",
            "Partizip II für einen eigenen Modus halten: Partizip II ist nur ein Baustein, der in Perfekt, Passiv und Konjunktiv-Vergangenheit wiederverwendet wird - kein eigener Modus.",
        ],
        "exercise_hint": "Mehrfachauswahl: Verbform analysieren - welche Zeit, welcher Modus, welche Richtung? Fehlersuche: falsche Kombination der drei Achsen erkennen.",
    },

    {
        "id": "imperativ",
        "title": "Imperativ - Befehle und Aufforderungen",
        "level": "A2",
        "category": "Verben",
        "explanation": """Der Imperativ drückt eine Aufforderung, Bitte oder einen Befehl aus. Es gibt drei Formen, je nach Anrede:

**du-Form:** Verbstamm (ohne Endung; mit -e bei Stamm auf -t/-d/-ig, sonst meist ohne)
machen → **Mach!** | gehen → **Geh!** | arbeiten → **Arbeite!** (Stamm endet auf -t)

**ihr-Form:** wie Präsens ihr, aber ohne Pronomen
machen → **Macht!** | gehen → **Geht!**

**Sie-Form:** Infinitiv + Sie (Pronomen bleibt, umgekehrte Wortstellung wie bei Fragen)
machen → **Machen Sie!** | gehen → **Gehen Sie!**

---

### Unregelmäßigkeiten

**Vokalwechsel e→i/ie im Präsens gilt auch im du-Imperativ:**
nehmen → **Nimm!** (nicht "Nehm!") | sprechen → **Sprich!** | lesen → **Lies!** | geben → **Gib!**

**sein ist unregelmäßig:**
**Sei** pünktlich! / **Seid** pünktlich! / **Seien Sie** pünktlich!

**haben verkürzt oft:**
**Hab** keine Angst! / **Habt** keine Angst! / **Haben Sie** keine Angst!

---

### Negation
'nicht' kommt nach dem Verb (oder nach dem Objekt): **Mach das nicht!** / **Warten Sie nicht!**

### Höfliche Alternative im Beruf
Der direkte Imperativ wirkt oft zu hart für den Arbeitskontext. Höflicher mit Konjunktiv II: **Könnten Sie...?** / **Würden Sie...?** statt eines nackten Imperativs.""",
        "examples": [
            {
                "label": "du-Form, regelmäßig",
                "sentence": "**Schick** mir bitte die Unterlagen.",
                "note": "Verbstamm ohne Endung, informell (unter Kollegen)"
            },
            {
                "label": "Sie-Form, formell",
                "sentence": "**Schicken Sie** mir bitte die Unterlagen.",
                "note": "Infinitiv + Sie, Standard im Berufskontext"
            },
            {
                "label": "Vokalwechsel im du-Imperativ",
                "sentence": "**Nimm** dir Zeit für die Analyse, bevor du entscheidest.",
                "note": "nehmen → nimmst (Präsens) → Nimm! (Imperativ), nicht 'Nehm!'"
            },
            {
                "label": "Höfliche Alternative statt Imperativ",
                "sentence": "Direkt: 'Schicken Sie mir die Unterlagen.' / Höflicher: '**Könnten Sie** mir die Unterlagen schicken?'",
                "note": "Konjunktiv II mildert die Aufforderung ab - typisch in professioneller Kommunikation."
            },
        ],
        "mistakes": [
            "du-Imperativ mit -e bei Vokalwechsel-Verben: ❌ 'Nehme das!' → ✅ 'Nimm das!'",
            "Sie-Imperativ ohne Pronomen: ❌ 'Machen!' → ✅ 'Machen Sie!'",
            "nicht vor dem Verb: ❌ 'Nicht mach das!' → ✅ 'Mach das nicht!'",
        ],
        "exercise_hint": "Lückentext: richtige Imperativform (du/ihr/Sie) einsetzen, inkl. unregelmäßiger Verben (nehmen, sein, haben). Satztransformation: Aussage in Imperativ umformen, dann in höfliche Konjunktiv-II-Bitte.",
    },

    {
        "id": "genus_verbi_ueberblick",
        "title": "Genus Verbi: Aktiv und Passiv im Überblick",
        "level": "B1",
        "category": "Verben",
        "explanation": """Genus Verbi (auch: Diathese) beschreibt, ob das Subjekt eines Satzes die Handlung selbst ausführt (Aktiv) oder die Handlung an ihm ausgeführt wird (Passiv). Es ist die dritte Achse neben Tempus und Modus (siehe "Die drei Achsen des Verbs").

**Aktiv:** Subjekt = Handelnder
"Der Berater **erstellt** den Bericht." (Der Berater tut etwas)

**Passiv:** Subjekt = wird behandelt, der Handelnde tritt in den Hintergrund oder fällt ganz weg
"Der Bericht **wird erstellt** (vom Berater)." (Der Bericht steht im Fokus, nicht wer ihn erstellt)

---

### Aktiv/Passiv im Vergleich (Präsens und Präteritum)

| Tempus | Aktiv | Passiv |
|--------|-------|--------|
| Präsens | Man prüft den Bericht. | Der Bericht **wird geprüft**. |
| Präteritum | Man prüfte den Bericht. | Der Bericht **wurde geprüft**. |
| Perfekt | Man hat den Bericht geprüft. | Der Bericht **ist geprüft worden**. |

**Ausführliche Bildungsregeln, Zeitformen im Passiv, Passiv mit Modalverben und Passiv-Ersatzformen (sein...zu, sich lassen):** siehe die eigenen Regeln "Passiv", "Passiv mit Modalverben" und "Passiv-Ersatzformen".

### Warum benutzt man Passiv?
- Der Handelnde ist unbekannt oder unwichtig: "Die Fenster **wurden** letzte Nacht **eingeschlagen**." (von wem, ist egal)
- Formeller, distanzierter Ton in Berichten: "Die Ergebnisse **wurden** ausgewertet." statt "Wir haben die Ergebnisse ausgewertet."
- Der Fokus soll auf der Sache liegen, nicht auf der Person.""",
        "examples": [
            {
                "label": "Aktiv → Passiv, gleiche Bedeutung",
                "sentence": "Aktiv: 'Das Team **hat** das Projekt **abgeschlossen**.' → Passiv: 'Das Projekt **ist abgeschlossen worden**.'",
                "note": "Fokus verschiebt sich vom Team auf das Projekt."
            },
            {
                "label": "Passiv ohne Nennung des Handelnden",
                "sentence": "**Es wird** noch **diskutiert**, wie das Budget verteilt wird.",
                "note": "Wer diskutiert, bleibt offen - typisch für Berichte."
            },
        ],
        "mistakes": [
            "Aktiv und Passiv beliebig für austauschbar halten: der Fokus/Ton ändert sich, auch wenn die Kernaussage gleich bleibt.",
            "Passiv mit sein-Zustand verwechseln: 'Die Tür ist geschlossen.' (Zustand, kein Passiv) vs. 'Die Tür wird geschlossen.' (Vorgang, echtes Passiv)",
        ],
        "exercise_hint": "Satztransformation: Aktivsätze ins Passiv umformen und umgekehrt, über mehrere Zeitformen hinweg.",
    },

    # ==================== NEU: LÜCKEN AUS PRODUKT-AUDIT ====================

    {
        "id": "komparation",
        "title": "Komparation - Steigerung der Adjektive und Adverbien",
        "level": "A2",
        "category": "Wortschatz",
        "explanation": """Adjektive und Adverbien werden in drei Stufen gesteigert: Positiv (Grundform), Komparativ (Vergleich), Superlativ (höchste Stufe).

**Regelmäßige Steigerung:**
Positiv + **-er** (Komparativ) | **am** + Positiv + **-sten** (Superlativ)
schnell → schnell**er** → **am** schnell**sten**

**Adjektive auf -el/-er verlieren im Komparativ das e:**
dunkel → dunk**ler** (nicht "dunkeler") | teuer → teu**rer**

**Umlaut bei vielen einsilbigen Adjektiven:**
alt → **ä**lter → am **ä**ltesten | groß → gr**ö**ßer → am gr**ö**ßten | jung → j**ü**nger → am j**ü**ngsten

**Adjektive auf -d/-t/-s/-z/-sch/-ß brauchen -esten im Superlativ (Aussprache):**
laut → lauter → am laut**esten**

**Unregelmäßige Formen (auswendig lernen!):**
| Positiv | Komparativ | Superlativ |
|---------|-----------|-----------|
| gut | besser | am besten |
| viel | mehr | am meisten |
| gern | lieber | am liebsten |
| hoch | höher | am höchsten |
| nah | näher | am nächsten |

---

### Vergleiche bilden

**als** (Ungleichheit, Komparativ): "Diese Lösung ist effizienter **als** die vorherige."
**so ... wie** (Gleichheit): "Das Ergebnis ist **so** gut **wie** erwartet."

**Superlativ als Adjektiv vor dem Nomen** (normale Adjektivdeklination): "der schnell**ste** Läufer", "die beste Lösung"
**Superlativ als Adverb** (am + -sten): "Diese Option funktioniert am besten." """,
        "examples": [
            {
                "label": "Beruflicher Vergleich",
                "sentence": "Diese Strategie ist **effizienter als** die alte, aber die neue Lösung ist **am effizientesten**.",
                "note": "Komparativ mit als, Superlativ mit am...-sten"
            },
            {
                "label": "Unregelmäßige Form",
                "sentence": "Das ist die **beste** Option, die wir bisher gefunden haben.",
                "note": "gut → besser → am besten / der/die/das beste (unregelmäßig)"
            },
            {
                "label": "Gleichheit mit so...wie",
                "sentence": "Das Budget ist **nicht so hoch wie** letztes Jahr geplant.",
                "note": "so...wie für Gleichheit/Ungleichheit ohne Steigerungsform"
            },
        ],
        "mistakes": [
            "Doppelte Steigerung: ❌ 'mehr besser' → ✅ 'besser'",
            "wie statt als beim Komparativ: ❌ 'größer wie ich' (umgangssprachlich falsch) → ✅ 'größer als ich'",
            "Umlaut vergessen: ❌ 'alter' → ✅ 'älter'",
        ],
        "exercise_hint": "Lückentext: Komparativ-/Superlativformen einsetzen, inkl. unregelmäßiger Formen. Fehlersuche: als/wie-Verwechslung.",
    },

    {
        "id": "genitiv_grundlagen",
        "title": "Genitiv - Formen und Gebrauch",
        "level": "B1",
        "category": "Kasus",
        "explanation": """Der Genitiv zeigt Zugehörigkeit oder Besitz: "das Auto **des Mannes**" = wessen Auto? Anders als bei den Genitiv-Präpositionen (eigene Regel) geht es hier um den Genitiv als **Attribut** direkt bei einem Nomen.

**Bildung:**
| | maskulin | feminin | neutral | Plural |
|--|----------|---------|---------|--------|
| Artikel | des | der | des | der |
| Nomen | +(e)s | (bleibt gleich) | +(e)s | (bleibt gleich) |

der Mann → **des Mannes** | die Frau → **der Frau** | das Kind → **des Kindes** | die Leute → **der Leute**

**Genitiv-s:** bei einsilbigen Wörtern meist **-es** (des Mannes, des Kindes), bei mehrsilbigen meist nur **-s** (des Computers, des Berichts).

---

### Genitiv vs. von + Dativ
In der gesprochenen Sprache ersetzt man den Genitiv oft durch **von + Dativ**: "das Auto **von dem** Mann". Das ist umgangssprachlich korrekt, aber **im formellen Schreiben und auf C1-Niveau gilt der Genitiv als Standard** - "von" wirkt dort stilistisch schwächer.

### Genitiv bei Eigennamen
Bei Personennamen einfach **-s** anhängen, ohne Artikel: "**Marias** Auto", "**Berlins** Sehenswürdigkeiten". Bei Namen auf -s/-x/-z: Apostroph statt -s: "**Max'** Bericht".""",
        "examples": [
            {
                "label": "Genitiv als Attribut, beruflich",
                "sentence": "Die Ergebnisse **des Projekts** übertreffen die Erwartungen.",
                "note": "das Projekt → des Projekts (Genitiv neutral)"
            },
            {
                "label": "Genitiv vs. von + Dativ",
                "sentence": "Formell: 'die Meinung **des Kunden**.' / Umgangssprachlich: 'die Meinung **von dem** Kunden.'",
                "note": "Im Aufsatz/Bericht immer die Genitiv-Variante bevorzugen."
            },
            {
                "label": "Eigenname im Genitiv",
                "sentence": "**Antonys** Vorschlag wurde vom Team positiv aufgenommen.",
                "note": "Eigenname + s, kein Artikel nötig"
            },
        ],
        "mistakes": [
            "Genitiv-s vergessen: ❌ 'die Meinung des Kunde' → ✅ 'die Meinung des Kunden' - Vorsicht: 'der Kunde' ist ein N-Deklinations-Nomen (siehe eigene Regel), Genitiv Singular ist 'des Kunden' (kein zusätzliches -s)",
            "von + Dativ im formellen Text überbenutzen: klingt auf C1-Niveau schwächer als der echte Genitiv",
            "Apostroph vergessen bei Namen auf -s: ❌ 'Max Bericht' → ✅ 'Max' Bericht'",
        ],
        "exercise_hint": "Lückentext: richtige Genitivform einsetzen. Satztransformation: von+Dativ-Konstruktionen in Genitiv umformen (für formelle Texte).",
    },

    {
        "id": "funktionsverbgefuege",
        "title": "Funktionsverbgefüge (Nomen-Verb-Verbindungen)",
        "level": "C1",
        "category": "Stil",
        "explanation": """Ein Funktionsverbgefüge ist eine feste Kombination aus einem eher "leeren" Verb (bringen, stellen, nehmen, ziehen, kommen, geben...) und einem Nomen, die zusammen eine eigene Bedeutung haben. Typisch für Berichte, offizielle Texte und C1-Register - eine Ergänzung zum Nominalstil (eigene Regel).

**Häufige Funktionsverbgefüge:**

| Ausdruck | Bedeutung |
|----------|-----------|
| **in Betracht ziehen** | erwägen |
| **zur Verfügung stellen** | geben, bereitstellen |
| **in Kraft treten** | gültig werden |
| **zum Ausdruck bringen** | ausdrücken |
| **Rücksicht nehmen auf** | berücksichtigen |
| **eine Entscheidung treffen** | entscheiden |
| **unter Beweis stellen** | beweisen |
| **in Anspruch nehmen** | nutzen, beanspruchen |
| **zum Abschluss bringen** | abschließen |
| **Stellung nehmen zu** | sich äußern zu |

**Warum benutzen?** Funktionsverbgefüge klingen formeller und nominaler als das einfache Verb - typisch für Geschäftsberichte, Verträge und offizielle Kommunikation. Das Nomen im Gefüge hat oft keinen Artikel oder einen festen Artikel, und die Präposition muss mitgelernt werden - nicht frei kombinierbar.""",
        "examples": [
            {
                "label": "in Betracht ziehen",
                "sentence": "Wir **ziehen** auch alternative Lösungen **in Betracht**.",
                "note": "= Wir erwägen auch alternative Lösungen. Formeller Klang."
            },
            {
                "label": "zur Verfügung stellen",
                "sentence": "Das Unternehmen **stellt** den Mitarbeitenden moderne Technik **zur Verfügung**.",
                "note": "= gibt den Mitarbeitenden moderne Technik"
            },
            {
                "label": "Stellung nehmen zu",
                "sentence": "Der Vorstand hat noch nicht **Stellung** zu dem Vorwurf **genommen**.",
                "note": "= hat sich noch nicht geäußert zu dem Vorwurf"
            },
        ],
        "mistakes": [
            "Falsche Präposition: jedes Funktionsverbgefüge hat eine feste Präposition, die mitgelernt werden muss - 'Rücksicht nehmen AUF', nicht 'für' oder 'bei'",
            "Verb im Gefüge frei austauschen: ❌ 'eine Entscheidung machen' → ✅ 'eine Entscheidung treffen' (fest, nicht 'machen')",
            "Artikel falsch setzen: viele Funktionsverbgefüge stehen ohne Artikel ('Stellung nehmen', nicht 'eine Stellung nehmen')",
        ],
        "exercise_hint": "Zuordnung: Verb + passendes Nomen zum Funktionsverbgefüge. Lückentext: richtiges Verb im Gefüge einsetzen.",
    },

    {
        "id": "textkohaerenz",
        "title": "Textkohärenz: Pronominaladverbien, Verweiswörter und Gliederungssignale",
        "level": "C1",
        "category": "Stil",
        "explanation": """Auf C1-Niveau muss ein Text zusammenhängend wirken, ohne Wörter ständig zu wiederholen. Drei Werkzeuge dafür:

---

### 1. Pronominaladverbien (da(r)- und wo(r)-Komposita)
Wenn man sich auf eine **Sache oder Idee** bezieht (nicht auf eine Person), ersetzt man Präposition + Pronomen durch **da(r) + Präposition**:
"Ich denke an das Meeting." → "Ich denke **daran**." (nicht "an es")

Bei **Personen** bleibt die normale Form: "Ich denke an **ihn**." (keine da-Form bei Personen!)

Für Fragen zu Sachen: **wo(r) + Präposition**, nicht "über was", "für was":
"**Worüber** sprichst du?" (nicht "Über was sprichst du?")

Häufige Formen: darauf, damit, dazu, davon, dagegen, dafür, darüber / worauf, womit, wozu, wovon, wogegen, wofür, worüber

### 2. Verweiswörter (Rückbezug ohne Wiederholung)
diesbezüglich · in diesem Zusammenhang · dabei · hierbei · dementsprechend · folglich · diesem Punkt zufolge

### 3. Gliederungssignale (eine Argumentation strukturieren)
**zunächst** / zum einen → **des Weiteren** / zum anderen → **abschließend** / zusammenfassend

Besonders nützlich für die Erörterung (Aufsatz-Tab): Einleitung mit "zunächst ist zu betonen", Gegenargument mit "dem ist entgegenzuhalten, dass", Schluss mit "zusammenfassend lässt sich festhalten".""",
        "examples": [
            {
                "label": "da-Form bei Sachbezug",
                "sentence": "Wir haben das Budget erhöht. **Damit** können wir die Deadline halten.",
                "note": "damit bezieht sich auf 'das Budget erhöhen' (eine Handlung/Sache), nicht auf eine Person"
            },
            {
                "label": "wo-Form in der Frage",
                "sentence": "**Worauf** bezieht sich diese Aussage genau?",
                "note": "Frage nach einer Sache → wo(r)-Form, nicht 'Auf was'"
            },
            {
                "label": "Gliederungssignale in der Erörterung",
                "sentence": "**Zunächst** ist festzuhalten, dass... **Des Weiteren** zeigt sich... **Abschließend** lässt sich sagen, dass...",
                "note": "Klassisches Gerüst für einen Aufsatz/eine Erörterung"
            },
        ],
        "mistakes": [
            "da- vergessen bei Sachbezug: ❌ 'Ich interessiere mich für es.' → ✅ 'Ich interessiere mich dafür.'",
            "'über was' statt 'worüber': in geschriebenem C1-Deutsch gilt die wo-Form als Standard, 'was' + Präposition ist umgangssprachlich",
            "da-Form bei Personen: ❌ 'Ich denke daran' wenn eine Person gemeint ist → ✅ 'Ich denke an ihn/sie'",
        ],
        "exercise_hint": "Satztransformation: Präposition+Pronomen in da-/wo-Form umformen. Aufsatz-Baustein: Gliederungssignale in einen Text einbauen.",
    },

    # ==================== GRUNDLAGEN (A1) ====================

    {
        "id": "grund_wortarten",
        "title": "Wortarten - Die Bausteine des Satzes",
        "level": "A1",
        "category": "Grundlagen",
        "explanation": """Jedes Wort in einem deutschen Satz gehört zu einer **Wortart** (Wortklasse). Die Wortart bestimmt, wie sich ein Wort verhält - ob es dekliniert, konjugiert wird oder unverändert bleibt.

**Die wichtigsten Wortarten:**

| Wortart | Frage/Merkmal | Beispiel |
|---------|---------------|----------|
| **Nomen** (Substantiv) | Person, Sache, Begriff; hat immer Genus und Artikel | der Bericht, die Kollegin |
| **Verb** | Handlung oder Zustand; wird konjugiert | arbeiten, sein |
| **Adjektiv** | Eigenschaft; beschreibt ein Nomen näher | wichtig, schnell |
| **Adverb** | beschreibt Verb/Adjektiv/Satz näher; bleibt unverändert | oft, dort, leider |
| **Pronomen** | steht anstelle eines Nomens | er, dieser, mein |
| **Präposition** | verbindet ein Nomen mit dem Satz, bestimmt den Kasus | in, mit, wegen |
| **Konjunktion** | verbindet Sätze oder Satzteile | und, weil, aber |
| **Artikel** | begleitet das Nomen, zeigt Genus/Kasus/Numerus | der, ein, kein |

---

### Wie erkennt man die Wortart?

- **Nomen:** Großschreibung; man kann einen Artikel davorsetzen (der/die/das Bericht → der Bericht)
- **Verb:** verändert sich mit der Person (ich arbeite, du arbeitest); Infinitiv endet meist auf -en
- **Adjektiv:** kann vor einem Nomen mit Endung stehen (ein wichtig**er** Termin) oder nach 'sein' (Der Termin ist wichtig)
- **Adverb:** bleibt immer gleich, egal in welchem Satz - bekommt selbst nie Endungen
- **Pronomen:** ersetzt ein Nomen, das schon bekannt ist (Der Kunde ruft an. **Er** hat eine Frage.)
- **Präposition:** steht vor einem Nomen/Pronomen und verlangt einen bestimmten Kasus (mit **dem** Kunden → Dativ)
- **Konjunktion:** verbindet zwei Teile, verändert sich selbst nie""",
        "examples": [
            {
                "label": "Nomen erkennen",
                "sentence": "Der **Kollege** hat den **Bericht** fertiggestellt.",
                "note": "Beide Wörter sind großgeschrieben und tragen einen Artikel - typisch für Nomen."
            },
            {
                "label": "Verb erkennen",
                "sentence": "Sie **arbeitet** seit drei Jahren im Unternehmen.",
                "note": "'arbeitet' verändert sich mit der Person (ich arbeite, du arbeitest...) - das ist ein Verb."
            },
            {
                "label": "Adjektiv vs. Adverb",
                "sentence": "Das ist ein **schnelles** Auto. Er fährt **schnell**.",
                "note": "Als Adjektiv vor dem Nomen bekommt 'schnell' eine Endung; als Adverb bleibt es unverändert."
            },
            {
                "label": "Präposition + Kasus",
                "sentence": "Wir sprechen **über** das Projekt.",
                "note": "'über' ist eine Präposition und bestimmt hier den Akkusativ ('das Projekt')."
            },
        ],
        "mistakes": [
            "Adjektiv und Adverb verwechseln: ❌ 'Er fährt schnelles.' → ✅ 'Er fährt schnell.' (Adverb bekommt nie eine Endung)",
            "Nomen ohne Großschreibung notieren: Nomen sind im Deutschen IMMER großgeschrieben, auch mitten im Satz: ❌ 'der bericht' → ✅ 'der Bericht'",
            "Präposition und Konjunktion verwechseln: 'wegen' (Präposition + Genitiv) vs. 'weil' (Konjunktion + Nebensatz) drücken beide einen Grund aus, funktionieren aber grammatisch unterschiedlich.",
        ],
        "exercise_hint": "Zuordnung: Wörter aus einem Satz der passenden Wortart zuordnen. Mehrfachauswahl: Wortart eines markierten Wortes bestimmen.",
    },

    {
        "id": "grund_kasus",
        "title": "Die vier Kasus (Fälle) - Nominativ, Akkusativ, Dativ, Genitiv",
        "level": "A1",
        "category": "Grundlagen",
        "explanation": """Der Kasus (Plural: Kasus oder Fälle) zeigt, welche Rolle ein Nomen oder Pronomen im Satz hat. Deutsch hat vier Kasus. Artikel, Adjektiv und manche Pronomen verändern ihre Form je nach Kasus (siehe eigene Regeln zur Deklination).

| Kasus | Frage | Funktion im Satz |
|-------|-------|-------------------|
| **Nominativ** | Wer/Was? | Subjekt (wer handelt / worum es geht) |
| **Akkusativ** | Wen/Was? | Akkusativobjekt (direktes Objekt) |
| **Dativ** | Wem? | Dativobjekt (indirektes Objekt) |
| **Genitiv** | Wessen? | Genitivattribut (Zugehörigkeit/Besitz, direkt bei einem Nomen) |

---

### Alle vier Kasus in einem Satz

**Der Chef (Nominativ) gibt dem Kunden (Dativ) den Bericht (Akkusativ) des Projekts (Genitiv).**

- **Der Chef** → Nominativ: Wer gibt? → Subjekt
- **dem Kunden** → Dativ: Wem gibt er? → Dativobjekt
- **den Bericht** → Akkusativ: Was gibt er? → Akkusativobjekt
- **des Projekts** → Genitiv: Wessen Bericht? → Genitivattribut (gehört zu 'den Bericht', nicht zum Verb)

**Wichtig:** Der Kasus hängt vom Verb (bzw. von der Präposition) ab - nicht von der Position im Satz. Deshalb kann man im Deutschen die Wortstellung relativ frei ändern, ohne die Bedeutung zu verlieren.""",
        "examples": [
            {
                "label": "Nominativ (Subjekt)",
                "sentence": "**Der Kunde** ruft an.",
                "note": "Wer ruft an? → der Kunde → Nominativ."
            },
            {
                "label": "Akkusativ (direktes Objekt)",
                "sentence": "Ich sehe **den Kunden**.",
                "note": "Wen sehe ich? → den Kunden → Akkusativ."
            },
            {
                "label": "Dativ (indirektes Objekt)",
                "sentence": "Ich helfe **dem Kunden**.",
                "note": "Wem helfe ich? → dem Kunden → Dativ."
            },
            {
                "label": "Genitiv (Zugehörigkeit)",
                "sentence": "Das ist das Büro **des Kunden**.",
                "note": "Wessen Büro? → des Kunden → Genitiv."
            },
        ],
        "mistakes": [
            "Kasus mit Satzposition verwechseln: die Reihenfolge im Satz zeigt NICHT automatisch den Kasus - nur die Frage (Wer/Wen/Wem/Wessen) zeigt den Kasus zuverlässig.",
            "Akkusativ und Dativ vertauschen: ❌ 'Ich helfe den Kunden.' → ✅ 'Ich helfe dem Kunden.' (helfen verlangt Dativ, nicht Akkusativ - siehe eigene Regel zu Dativverben)",
            "Genitiv für das ganze Prädikat statt für ein einzelnes Nomen halten: auf diesem Niveau gehört der Genitiv fast immer zu einem anderen Nomen ('der Bericht des Kunden'), nicht zum Verb - Ausnahme: eine kleine Gruppe seltener Genitiv-Verben wie bedürfen/gedenken (siehe eigene Regel für Fortgeschrittene).",
        ],
        "exercise_hint": "Mehrfachauswahl: zu einem markierten Wort im Satz die richtige Frage (Wer/Wen/Wem/Wessen?) und den Kasus bestimmen.",
    },

    {
        "id": "grund_genus_numerus",
        "title": "Genus und Numerus - der/die/das und Singular/Plural",
        "level": "A1",
        "category": "Grundlagen",
        "explanation": """**Genus** (grammatisches Geschlecht) und **Numerus** (Anzahl) sind zwei feste Eigenschaften jedes Nomens.

### Genus: maskulin, feminin, neutral
Jedes deutsche Nomen hat eines von drei Genera, sichtbar am bestimmten Artikel:
- **der** → maskulin (der Bericht, der Kollege)
- **die** → feminin (die Firma, die Kollegin)
- **das** → neutral (das Meeting, das Team)

**Wichtig:** Das Genus ist meistens **arbiträr** (zufällig) und hat oft nichts mit der realen Bedeutung zu tun (das Mädchen ist neutral, obwohl es eine Person ist - weil das Diminutivsuffix -chen immer neutral macht). Es gibt **keine zuverlässige Regel**, um das Genus eines Nomens vorherzusagen - man muss es **immer zusammen mit dem Nomen lernen** (also nicht 'Bericht' lernen, sondern 'der Bericht').

**Zwei feste, ausnahmslose Regeln** (nicht nur Tendenzen):
- Wörter auf **-chen, -lein** sind immer neutral (das Mädchen, das Fräulein)
- Wörter auf **-ung, -heit, -keit, -schaft, -ion** sind immer feminin (die Zeitung, die Freiheit)

**Ein paar schwache Tendenzen** (keine festen Regeln, viele Ausnahmen):
- Wörter auf **-e** sind oft feminin (die Firma - aber: der Junge!)
- Wörter auf **-ismus, -us** sind oft maskulin (der Kapitalismus)

### Numerus: Singular und Plural
Jedes Nomen kann in der Einzahl (Singular) oder Mehrzahl (Plural) stehen. Der Plural wird auf sehr unterschiedliche Weise gebildet (-e, -er, -en, -s, Umlaut, oder keine Veränderung) - auch das muss man mit jedem Nomen mitlernen.""",
        "examples": [
            {
                "label": "Drei Genera",
                "sentence": "**der** Bericht, **die** Firma, **das** Meeting",
                "note": "Maskulin, feminin, neutral - erkennbar am bestimmten Artikel."
            },
            {
                "label": "Genus ist arbiträr",
                "sentence": "**das** Mädchen, **der** Tisch, **die** Wand",
                "note": "Kein logischer Zusammenhang zwischen Bedeutung und Genus - jedes Genus muss auswendig gelernt werden."
            },
            {
                "label": "Singular vs. Plural",
                "sentence": "**ein** Kollege → **zwei** Kolleg**en**",
                "note": "Der Plural verändert sowohl den Artikel als auch oft die Endung des Nomens."
            },
        ],
        "mistakes": [
            "Genus aus der Bedeutung ableiten wollen: ❌ 'das Sonne' (weil man an ein neutrales Objekt denkt) → ✅ 'die Sonne' - Genus hat oft nichts mit der Bedeutung zu tun.",
            "Genus eines Nomens ohne Artikel lernen: Nomen sollte man nie ohne Artikel lernen, sondern immer als Einheit ('die Firma', nicht nur 'Firma').",
            "Ein festes Pluralmuster für alle Nomen annehmen: ❌ 'die Berichts' → ✅ 'die Berichte' - jedes Nomen hat seine eigene Pluralform, die man mitlernen muss.",
        ],
        "exercise_hint": "Zuordnung: Nomen dem richtigen Artikel (der/die/das) zuordnen. Lückentext: Singular- und Pluralformen einsetzen.",
    },

    {
        "id": "grund_partizipien",
        "title": "Partizip I und Partizip II - was ist ein Partizip?",
        "level": "A1",
        "category": "Grundlagen",
        "explanation": """Ein Partizip ist eine Verbform, die man wie ein Adjektiv oder Adverb benutzen kann, aber die von einem Verb abgeleitet ist. Deutsch hat zwei Partizipien.

---

### Partizip I - Infinitiv + d
**Bildung:** Infinitiv + **-d** (z. B. arbeiten → arbeite**nd**, lachen → lache**nd**)

**Bedeutung:** eine Handlung, die **gleichzeitig** und **aktiv** abläuft (noch im Gange) - "während sie tut"

Beispiel: der **arbeitende** Kollege = der Kollege, der (gerade) arbeitet

### Partizip II - ge- + Stamm + -t/-en
**Bildung:** meistens **ge-** + Verbstamm + **-t** (schwache Verben: gearbeitet) oder **-en** (starke Verben: gesprochen); bei Verben mit untrennbarem Präfix (be-, ver-, ent-...) oder auf -ieren entfällt das ge- (besucht, organisiert)

**Bedeutung:** eine Handlung, die **abgeschlossen** ist, oder ein **passiver** Vorgang - "nachdem etwas getan wurde" bzw. "das, was gemacht wurde"

Beispiel: der **geschriebene** Bericht = der Bericht, der geschrieben wurde

---

**Wichtig auf dieser Stufe:** Diese Regel definiert nur, WAS die beiden Partizipien sind und wie sie gebildet werden. WIE man sie in Sätzen einsetzt (als Partizipialkonstruktion vor dem Nomen, im Perfekt, im Passiv), erklären die eigenen Regeln **"Partizipialkonstruktionen als Adjektiv"**, **"Erweiterte Partizipialkonstruktionen (C1)"**, **"Passiv"** und **"Die Zeitformen im Überblick"**.""",
        "examples": [
            {
                "label": "Partizip I bilden",
                "sentence": "lachen → **lachend** | steigen → **steigend**",
                "note": "Infinitiv + d; beschreibt eine laufende, aktive Handlung."
            },
            {
                "label": "Partizip II bilden (schwach)",
                "sentence": "planen → **geplant**",
                "note": "ge- + Stamm + -t, weil 'planen' ein schwaches Verb ist."
            },
            {
                "label": "Partizip II bilden (stark)",
                "sentence": "schreiben → **geschrieben**",
                "note": "ge- + Stamm (mit Vokalwechsel) + -en, weil 'schreiben' ein starkes Verb ist."
            },
            {
                "label": "Partizip II ohne ge-",
                "sentence": "organisieren → **organisiert**",
                "note": "Verben auf -ieren und mit untrennbarem Präfix (be-/ver-/ent-...) bilden das Partizip II ohne ge-."
            },
        ],
        "mistakes": [
            "Partizip I und II verwechseln: ❌ 'der geschrieben Bericht' für eine noch laufende Handlung → Partizip I (schreibend) beschreibt Gleichzeitigkeit, Partizip II (geschrieben) beschreibt Abgeschlossenes/Passives.",
            "ge- bei Verben auf -ieren ergänzen: ❌ 'georganisiert' → ✅ 'organisiert'",
            "Partizip I ohne vollen Infinitivstamm bilden: ❌ 'arbeitd' → ✅ 'arbeitend' (Infinitiv bleibt komplett erhalten, nur -d wird angehängt).",
        ],
        "exercise_hint": "Zuordnung: Infinitiv → Partizip I und Partizip II bilden. Mehrfachauswahl: Partizip I oder II im Satz erkennen.",
    },

    {
        "id": "grund_verbformen",
        "title": "Verbformen-Grundbegriffe - Infinitiv, Personalform, Modus",
        "level": "A1",
        "category": "Grundlagen",
        "explanation": """Um Verbformen zu verstehen, braucht man drei Grundbegriffe.

### Infinitiv (Grundform)
Die Form, die im Wörterbuch steht - unverändert, ohne Bezug zu einer bestimmten Person. Endet fast immer auf **-en** (arbeiten, sein) oder **-n** (lächeln).
→ Der Infinitiv steht z. B. nach Modalverben und am Satzende: "Ich **muss** das Angebot **prüfen**."

### Personalform (finite Verbform)
Die Form, die an eine bestimmte Person angepasst (konjugiert) ist. Sie trägt die Information über Person, Numerus und Zeit.
Infinitiv **arbeiten** → Personalform: ich arbeit**e**, du arbeit**est**, er arbeit**et**...
→ Jeder vollständige deutsche Hauptsatz braucht genau eine Personalform an Position 2.

### Modus (Redeweise)
Der Modus zeigt die Haltung des Sprechers zur Aussage. Es gibt drei Modi:
- **Indikativ** - eine Tatsache, das Normale (der weitaus häufigste Modus): "Er **arbeitet** heute im Büro."
- **Konjunktiv** - etwas Berichtetes, Hypothetisches oder Unwirkliches: "Er **arbeite** heute im Büro." (berichtet) / "Er **würde** heute im Büro **arbeiten**." (hypothetisch)
- **Imperativ** - eine Aufforderung oder ein Befehl: "**Arbeiten** Sie heute im Büro!"

**Für die Vertiefung:** siehe die eigenen Regeln **"Konjunktiv II"**, **"Indirekte Rede - Konjunktiv I"**, **"Imperativ"** und **"Die drei Achsen des Verbs: Tempus, Modus, Genus Verbi"**.""",
        "examples": [
            {
                "label": "Infinitiv",
                "sentence": "Wir planen, das Projekt bis Freitag **abzuschließen**.",
                "note": "Grundform des Verbs, hier nach 'planen, ... zu' - keine Personalendung."
            },
            {
                "label": "Personalform",
                "sentence": "Der Kollege **prüft** die Zahlen.",
                "note": "'prüft' ist an die 3. Person Singular angepasst - das ist die Personalform."
            },
            {
                "label": "Drei Modi im Vergleich",
                "sentence": "Indikativ: 'Sie **ist** pünktlich.' / Konjunktiv: 'Sie **wäre** pünktlich, wenn...' / Imperativ: '**Seien** Sie pünktlich!'",
                "note": "Gleiches Verb (sein), drei verschiedene Haltungen zur Aussage."
            },
        ],
        "mistakes": [
            "Infinitiv als Personalform benutzen: ❌ 'Ich arbeiten heute.' → ✅ 'Ich arbeite heute.' (Personalform nötig, kein Infinitiv im Hauptsatz)",
            "Modus mit Modalverben verwechseln: 'können/müssen/wollen' sind eine Wortart (Modalverben), kein Modus - siehe eigene Regel 'Die drei Achsen des Verbs'.",
            "Konjunktiv für 'selten/unwichtig' halten: der Konjunktiv ist keine Ausnahme, sondern ein fester, häufig gebrauchter Modus (indirekte Rede, Höflichkeit, Hypothesen).",
        ],
        "exercise_hint": "Mehrfachauswahl: Ist die markierte Verbform ein Infinitiv oder eine Personalform? Welcher Modus liegt vor?",
    },

    {
        "id": "grund_satzglieder",
        "title": "Satzglieder - Subjekt, Prädikat, Objekt",
        "level": "A1",
        "category": "Grundlagen",
        "explanation": """Ein Satz besteht aus **Satzgliedern** - Wörtern oder Wortgruppen, die zusammen eine grammatische Funktion erfüllen. Die wichtigsten drei:

| Satzglied | Kasus | Frage | Funktion |
|-----------|-------|-------|----------|
| **Subjekt** | Nominativ | Wer/Was? | führt die Handlung aus / worum es im Satz geht |
| **Prädikat** | - | Was passiert? | das Verb (konjugiert); der Kern jedes Satzes |
| **Akkusativobjekt** | Akkusativ | Wen/Was? | das direkte Objekt der Handlung |
| **Dativobjekt** | Dativ | Wem? | das indirekte Objekt (oft die Person, die etwas erhält) |

**Wichtig:** Jeder deutsche Hauptsatz braucht ein Subjekt und ein Prädikat. Objekte sind nur nötig, wenn das Verb sie verlangt (siehe eigene Regeln zu Verben mit Dativ/Akkusativ).

---

### Ein Satz, alle Teile markiert

**Die Assistentin (Subjekt) schickt (Prädikat) dem Kunden (Dativobjekt) die Rechnung (Akkusativobjekt).**

- **Die Assistentin** → Nominativ, Subjekt: Wer schickt?
- **schickt** → Prädikat: Was passiert?
- **dem Kunden** → Dativ, Dativobjekt: Wem schickt sie?
- **die Rechnung** → Akkusativ, Akkusativobjekt: Was schickt sie?""",
        "examples": [
            {
                "label": "Subjekt und Prädikat",
                "sentence": "**Das Team** (Subjekt) **arbeitet** (Prädikat) konzentriert.",
                "note": "Minimaler vollständiger Satz: Subjekt + Prädikat reichen aus."
            },
            {
                "label": "Mit Akkusativobjekt",
                "sentence": "Die Kollegin **liest** den **Bericht**.",
                "note": "'liest' verlangt ein Akkusativobjekt: Was liest sie? → den Bericht."
            },
            {
                "label": "Mit Dativ- und Akkusativobjekt",
                "sentence": "Der Chef **gibt** der **Praktikantin** eine **Aufgabe**.",
                "note": "'geben' verlangt zwei Objekte: Dativ (der Praktikantin) und Akkusativ (eine Aufgabe)."
            },
        ],
        "mistakes": [
            "Subjekt und Akkusativobjekt verwechseln: nur die Frage Wer/Was (Nominativ) zeigt das Subjekt - nicht die Position am Satzanfang, da im Deutschen auch Objekte vorne stehen können: 'Den Bericht liest die Kollegin.' (Subjekt bleibt 'die Kollegin')",
            "Prädikat für nur den Infinitiv halten: das Prädikat ist die konjugierte Verbform (Personalform), nicht der Infinitiv - siehe eigene Regel zu Infinitiv/Personalform.",
            "Satz ohne Prädikat für vollständig halten: ❌ 'Der Kunde die Rechnung.' ist kein vollständiger Satz - es fehlt das Prädikat (Verb).",
        ],
        "exercise_hint": "Mehrfachauswahl: Satzglieder (Subjekt/Prädikat/Objekt) in einem Beispielsatz markieren und benennen.",
    },

    # ==================== NEUE REGELN - LÜCKENAUDIT (B1) ====================

    {
        "id": "b1_als_wenn",
        "title": "Temporalsätze mit 'als' und 'wenn' - einmalig oder wiederholt?",
        "level": "B1",
        "category": "Konnektoren",
        "explanation": """'als' und 'wenn' leiten beide einen Temporalsatz ein (Verb ans Ende) und werden oft verwechselt, weil sie im Englischen beide 'when' entsprechen können. Die Wahl hängt von zwei Fragen ab: **Wann?** und **Wie oft?**

| | Zeit | Häufigkeit | Beispiel |
|--|------|-----------|---------|
| **als** | nur Vergangenheit | einmaliges Ereignis | **Als** ich den Vertrag unterschrieb, war ich noch skeptisch. |
| **wenn** | Vergangenheit | wiederholtes Ereignis ('immer wenn') | **Wenn** der Kunde anrief, übernahm meistens meine Kollegin. |
| **wenn** | Gegenwart / Zukunft | einmalig ODER wiederholt | **Wenn** das Meeting beginnt, schalte ich mein Handy aus. |

**Merkregel:** 'als' gibt es NUR für die Vergangenheit, und NUR für ein einziges, abgeschlossenes Ereignis. Für alles andere (Gegenwart, Zukunft, oder Wiederholung in der Vergangenheit) nimmt man 'wenn'.""",
        "examples": [
            {
                "label": "als (einmalig, Vergangenheit)",
                "sentence": "**Als** ich am Montag ins Büro kam, war die Präsentation schon fertig.",
                "note": "Ein einziges, konkretes Ereignis in der Vergangenheit."
            },
            {
                "label": "wenn (wiederholt, Vergangenheit)",
                "sentence": "**Wenn** ich früher Überstunden machte, brachte mir der Chef immer einen Kaffee.",
                "note": "'immer wenn' - wiederholtes Ereignis in der Vergangenheit → wenn, nicht als."
            },
            {
                "label": "wenn (Gegenwart/Zukunft)",
                "sentence": "**Wenn** der Vertrag unterschrieben ist, informiere ich das ganze Team.",
                "note": "Gegenwart/Zukunft nimmt immer 'wenn', egal ob einmalig oder wiederholt."
            },
        ],
        "mistakes": [
            "als für Wiederholung in der Vergangenheit: ❌ 'Als wir Probleme hatten, rief ich immer den Support an.' → ✅ 'Wenn wir Probleme hatten, ...' (immer = wiederholt → wenn)",
            "wenn für ein einmaliges Ereignis in der Vergangenheit: ❌ 'Wenn ich letztes Jahr die Stelle wechselte, war ich nervös.' → ✅ 'Als ich letztes Jahr die Stelle wechselte, ...'",
            "als für Gegenwart/Zukunft: ❌ 'Als das Meeting morgen beginnt, ...' → ✅ 'Wenn das Meeting morgen beginnt, ...' (als gibt es nur in der Vergangenheit)",
        ],
        "exercise_hint": "Lückentext: als oder wenn je nach Zeit und Häufigkeit einsetzen. Fehlersuche mit typischen als/wenn-Verwechslungen.",
    },

    {
        "id": "b1_personalpronomen",
        "title": "Personalpronomen - volle Deklination",
        "level": "B1",
        "category": "Kasus",
        "explanation": """Personalpronomen ersetzen ein Nomen, das schon bekannt ist. Wie Nomen verändern sie ihre Form je nach Kasus - hier aber unregelmäßig und komplett auswendig zu lernen.

| Person | Nominativ | Akkusativ | Dativ |
|--------|-----------|-----------|-------|
| ich | ich | **mich** | **mir** |
| du | du | **dich** | **dir** |
| er | er | **ihn** | **ihm** |
| sie (sg.) | sie | **sie** | **ihr** |
| es | es | **es** | **ihm** |
| wir | wir | **uns** | **uns** |
| ihr | ihr | **euch** | **euch** |
| sie (Pl.) | sie | **sie** | **ihnen** |
| Sie (Höflichkeitsform) | Sie | **Sie** | **Ihnen** |

**Auffälligkeiten:**
- **er → ihn/ihm**, aber **es → es/ihm**: es bleibt im Akkusativ gleich, bekommt im Dativ aber die gleiche Form wie 'er' (ihm).
- **sie (Singular feminin)** und **sie (Plural)** sehen im Nominativ/Akkusativ gleich aus, unterscheiden sich aber im Dativ: **ihr** (Singular) vs. **ihnen** (Plural).
- Die Höflichkeitsform **Sie/Sie/Ihnen** wird immer großgeschrieben und hat dieselben Endungen wie die 3. Person Plural (sie/sie/ihnen).""",
        "examples": [
            {
                "label": "Akkusativ (er)",
                "sentence": "Ich habe den Kollegen gesucht, aber ich habe **ihn** nicht gefunden.",
                "note": "er → ihn im Akkusativ (direktes Objekt)."
            },
            {
                "label": "Dativ (sie, Singular)",
                "sentence": "Ich habe mit der Kundin gesprochen und **ihr** ein Angebot gemacht.",
                "note": "sie (feminin, Singular) → ihr im Dativ - nicht zu verwechseln mit dem Possessivartikel 'ihr'."
            },
            {
                "label": "Dativ (sie, Plural) vs. Höflichkeitsform",
                "sentence": "Ich habe **ihnen** (den Kollegen) die Zahlen geschickt, und ich habe auch **Ihnen** (Herr Neumann) eine Kopie geschickt.",
                "note": "ihnen (Plural, klein) vs. Ihnen (Höflichkeitsform, immer groß) - gleiche Form, unterschiedliche Bedeutung."
            },
        ],
        "mistakes": [
            "es im Dativ falsch bilden: ❌ 'Ich schenke es Aufmerksamkeit.' → ✅ 'Ich schenke ihm Aufmerksamkeit.' (es → ihm im Dativ, nicht 'es')",
            "ihr (Dativ von sie, Singular) mit dem Possessivartikel 'ihr' verwechseln: 'Ich helfe ihr.' (Pronomen, Dativobjekt) vs. 'Das ist ihr Büro.' (Possessivartikel vor Nomen) - äußerlich gleich, grammatisch unterschiedlich.",
            "Höflichkeitsform klein schreiben: ❌ 'Ich danke ihnen für Ihre Zeit.' wenn eine einzelne angeredete Person gemeint ist → ✅ 'Ich danke Ihnen für Ihre Zeit.' (Höflichkeitsform immer groß)",
        ],
        "exercise_hint": "Lückentext: richtiges Personalpronomen (Akkusativ/Dativ) für die passende Person einsetzen. Fehlersuche mit Groß-/Kleinschreibung der Höflichkeitsform.",
    },

    {
        "id": "b1_possessivartikel",
        "title": "Possessivartikel - volle Deklination",
        "level": "B1",
        "category": "Kasus",
        "explanation": """Possessivartikel zeigen Besitz oder Zugehörigkeit (mein, dein...) und stehen wie ein Artikel vor einem Nomen. Jeder Possessivartikel hat einen festen Stamm, abhängig vom Besitzer:

| Person | Possessivartikel |
|--------|-------------------|
| ich | **mein** |
| du | **dein** |
| er | **sein** |
| sie (sg.) | **ihr** |
| es | **sein** |
| wir | **unser** |
| ihr | **euer** |
| sie (Pl.) | **ihr** |
| Sie | **Ihr** |

**Deklination:** Possessivartikel dekliniert man genau wie 'ein/kein' (siehe Regel 'Adjektivdeklination'). Am Stamm (z. B. mein-) hängt man je nach Kasus/Genus dieselben Endungen an:

| | mask. | fem. | neutr. | Plural |
|--|-------|------|--------|--------|
| **Nom.** | mein | mein**e** | mein | mein**e** |
| **Akk.** | mein**en** | mein**e** | mein | mein**e** |
| **Dat.** | mein**em** | mein**er** | mein**em** | mein**en** |
| **Gen.** | mein**es** | mein**er** | mein**es** | mein**er** |

**Sonderfall 'euer':** Wenn eine Endung angehängt wird, fällt das zweite **e** im Stamm weg: **euer** → **eure**, **euren**, **eurem**, **eurer** (nicht 'euere').""",
        "examples": [
            {
                "label": "Nominativ",
                "sentence": "**Unser** Angebot ist wettbewerbsfähig.",
                "note": "unser + keine Endung im Nominativ neutrum, wie 'ein'."
            },
            {
                "label": "Akkusativ",
                "sentence": "Wir haben **euren** Vorschlag geprüft.",
                "note": "euer → eur- (das zweite e fällt weg) + -en im Akkusativ maskulin."
            },
            {
                "label": "Dativ",
                "sentence": "Ich habe mit **ihrer** Kollegin gesprochen.",
                "note": "ihr (Possessivartikel, 3. Person) + -er im Dativ feminin."
            },
            {
                "label": "Höflichkeitsform",
                "sentence": "Könnten Sie mir **Ihre** Unterlagen schicken?",
                "note": "Ihr (Höflichkeitsform, immer groß) + -e im Akkusativ Plural."
            },
        ],
        "mistakes": [
            "euer ohne Elision: ❌ 'euere Idee' → ✅ 'eure Idee' (das zweite e im Stamm fällt bei jeder Endung weg)",
            "sein (er/es) mit ihr (sie, Singular feminin) verwechseln: 'Der Kollege bringt **seinen** Laptop mit.' (er → sein) vs. 'Die Kollegin bringt **ihren** Laptop mit.' (sie → ihr)",
            "Possessivartikel-Endung im Dativ/Genitiv vergessen: ❌ 'mit mein Kollegen' → ✅ 'mit meinem Kollegen' (Dativ maskulin braucht -em)",
        ],
        "exercise_hint": "Lückentext: richtigen Possessivartikel mit passender Endung je nach Kasus/Genus einsetzen. Fehlersuche mit 'euer' → 'eure'.",
    },

    {
        "id": "b1_indefinitpronomen",
        "title": "Indefinitpronomen - man, jemand, niemand, etwas, nichts, jeder, alle",
        "level": "B1",
        "category": "Wortschatz",
        "explanation": """Indefinitpronomen bezeichnen unbestimmte Personen oder Mengen - man weiß nicht (oder es ist unwichtig), wer oder wie viele genau gemeint sind.

---

### man - die unbestimmte Person
'man' steht nur im **Nominativ** und hat keinen Plural. Es bedeutet 'jemand/die Leute/du/ich' allgemein - sehr häufig in Anleitungen und allgemeinen Aussagen.
Die obliquen Formen (Akkusativ/Dativ) werden mit **einen/einem** gebildet, der Possessivartikel ist **sein**:
"**Man** sollte **seine** E-Mails täglich checken. Das hilft **einem**, den Überblick zu behalten."

### jemand / niemand - eine unbestimmte Person / keine Person
Werden dekliniert, aber die Endungen im Akkusativ/Dativ sind im modernen Deutsch oft optional:
| Nom. | Akk. | Dat. |
|------|------|------|
| jemand | jemand(en) | jemand(em) |
| niemand | niemand(en) | niemand(em) |

### etwas / nichts - eine unbestimmte Sache / keine Sache
Bleiben in **jedem** Kasus unverändert: etwas, nichts (keine Deklination).

### jeder / alle / einige / manche - unbestimmte Mengen
- **jeder** (Singular, jede/r Einzelne) dekliniert wie der bestimmte Artikel: jeder, jeden, jedem, jedes
- **alle** (Plural, die Gesamtheit) dekliniert wie der bestimmte Artikel Plural: alle, alle, allen, aller
- **einige / manche** (Plural, ein Teil einer Menge) deklinieren wie Adjektive ohne Artikel: einige gute Ideen, mit einigen Kollegen""",
        "examples": [
            {
                "label": "man (Nominativ)",
                "sentence": "In diesem Beruf muss **man** flexibel sein.",
                "note": "man = eine allgemeine, unbestimmte Person - nur Nominativ."
            },
            {
                "label": "man → einem (obliqu)",
                "sentence": "Solche Fehler können **einem** leicht passieren.",
                "note": "Dativ von 'man' ist 'einem', nicht 'man'."
            },
            {
                "label": "jemand / niemand",
                "sentence": "Hat **jemand** eine Frage? - Nein, **niemand** hat eine Frage.",
                "note": "jemand/niemand bleiben im Nominativ unverändert."
            },
            {
                "label": "jeder vs. alle",
                "sentence": "**Jeder** Mitarbeiter bekommt Zugang; **alle** Mitarbeiter wurden informiert.",
                "note": "jeder = Singular, jeder Einzelne; alle = Plural, die Gesamtheit."
            },
        ],
        "mistakes": [
            "man im Akkusativ/Dativ verwenden: ❌ 'Das hilft man.' → ✅ 'Das hilft einem.' (man nur Nominativ, sonst einen/einem)",
            "etwas/nichts deklinieren: ❌ 'mit etwasem Geduld' → ✅ 'mit etwas Geduld' (etwas/nichts bleiben immer unverändert)",
            "jeder mit Plural-Verb kombinieren: ❌ 'jeder Mitarbeiter kommen' → ✅ 'jeder Mitarbeiter kommt' (jeder ist Singular, Verb entsprechend konjugieren)",
        ],
        "exercise_hint": "Lückentext: man/einen/einem oder jemand/niemand/etwas/nichts/jeder/alle je nach Kontext und Kasus einsetzen.",
    },

    {
        "id": "b1_brauchen_zu",
        "title": "brauchen + nicht + zu - Alternative zu 'nicht müssen'",
        "level": "B1",
        "category": "Verben",
        "explanation": """'nicht brauchen + zu + Infinitiv' ist eine gebräuchliche Alternative zu 'nicht müssen'. Beide drücken aus, dass etwas nicht notwendig ist.

**Bildung:** Subjekt + brauchen (konjugiert) + ... + nicht/nur/kein + zu + Infinitiv (am Satzende)

"Sie **brauchen** das Formular **nicht** auszufüllen." = "Sie **müssen** das Formular **nicht** ausfüllen."

**Wichtig:** Anders als beim einfachen Vollverb 'brauchen' (= etwas nötig haben, z. B. 'Ich brauche Zeit') steht hier ein **zu + Infinitiv**, ähnlich wie bei anderen Infinitivkonstruktionen. Im formellen/geschriebenen Deutsch (und im Telc/Goethe-Kontext) gehört das **zu** immer dazu - im gesprochenen Umgangsdeutsch wird es oft weggelassen, gilt aber als nicht standardsprachlich.

**Auch mit 'nur':** 'brauchen nur ... zu' drückt eine Einschränkung aus (= es reicht, wenn...):
"Sie **brauchen** die Unterlagen **nur** noch zu unterschreiben." = Es ist nur noch diese eine Sache nötig.""",
        "examples": [
            {
                "label": "nicht brauchen zu (= nicht müssen)",
                "sentence": "Sie **brauchen** sich **nicht** zu entschuldigen.",
                "note": "= Sie müssen sich nicht entschuldigen. 'zu' gehört fest zur Konstruktion."
            },
            {
                "label": "nur brauchen zu (Einschränkung)",
                "sentence": "Sie **brauchen** nur **zu** unterschreiben, den Rest erledigen wir.",
                "note": "= Es ist nur diese eine Handlung nötig, mehr nicht."
            },
            {
                "label": "Beruflicher Kontext",
                "sentence": "Der Kunde **braucht** die Rechnung **nicht** sofort **zu** bezahlen.",
                "note": "Höflichere/formellere Alternative zu 'Der Kunde muss die Rechnung nicht sofort bezahlen.'"
            },
        ],
        "mistakes": [
            "zu weglassen im formellen Schreiben: ❌ 'Sie brauchen das nicht machen.' (nur in lockerer Umgangssprache akzeptiert) → ✅ 'Sie brauchen das nicht zu machen.'",
            "nicht brauchen zu mit einem Verbot (dürfen nicht) verwechseln: 'nicht brauchen zu' = keine Notwendigkeit (= nicht müssen), kein Verbot: ❌ 'Sie brauchen das nicht zu tun' als Verbot missverstehen.",
            "brauchen + zu ohne einschränkendes Wort benutzen: die Konstruktion funktioniert nur mit nicht/nur/kein davor - ohne diese bleibt 'brauchen' ein normales Vollverb mit Akkusativobjekt: 'Ich brauche mehr Zeit.' (kein Infinitiv mit zu)",
        ],
        "exercise_hint": "Satztransformation: Sätze mit 'nicht müssen' in 'nicht brauchen ... zu' umformen und umgekehrt.",
    },

    # ==================== NEUE REGELN - LÜCKENAUDIT (B2/C1) ====================

    {
        "id": "b2_konditionalsaetze",
        "title": "Konditionalsätze - Typ I, II und III",
        "level": "B2",
        "category": "Verbformen",
        "explanation": """Konditionalsätze (Bedingungssätze) verbinden eine Bedingung (wenn-Satz) mit einer Folge (Hauptsatz). Auf B2/C1-Niveau unterscheidet man drei Typen, je nachdem, wie realistisch die Bedingung ist. **Beide Satzteile stehen im selben Typ** - Bedingung und Folge müssen zusammenpassen.

| Typ | Bedeutung | Wenn-Satz | Hauptsatz (Folge) |
|-----|-----------|-----------|---------------------|
| **Typ I** | real, möglich | Indikativ (Präsens) | Indikativ (Präsens/Futur) |
| **Typ II** | hypothetisch, Gegenwart/Zukunft (unwahrscheinlich oder unwirklich) | Konjunktiv II Präsens | Konjunktiv II Präsens (würde + Infinitiv) |
| **Typ III** | irreal, Vergangenheit (kann nicht mehr geändert werden) | Konjunktiv II Vergangenheit | Konjunktiv II Vergangenheit |

---

### Typ I - real
Indikativ in beiden Teilen - die Bedingung ist real erfüllbar.
**Wenn wir das Budget erhöhen, können wir die Kampagne ausweiten.**

### Typ II - hypothetisch (Gegenwart/Zukunft)
Konjunktiv II Präsens: 'würde + Infinitiv' (die meisten Verben) oder die unregelmäßigen Formen wäre/hätte/könnte... (siehe Regel 'Konjunktiv II').
**Wenn wir mehr Budget hätten, würden wir die Kampagne sofort ausweiten.**

### Typ III - irreal (Vergangenheit)
**Bildung: Konjunktiv II Vergangenheit = hätte/wäre (Konjunktiv II von haben/sein) + Partizip II - in BEIDEN Satzteilen.**
Ob hätte oder wäre, richtet sich nach demselben Prinzip wie beim Perfekt (haben oder sein als Hilfsverb - siehe Regel 'Schwache, starke und gemischte Verben').

**Wenn wir das Budget erhöht hätten, hätten wir die Kampagne ausgeweitet.**
(= Wir haben das Budget nicht erhöht → die Kampagne wurde nicht ausgeweitet. Beides liegt in der Vergangenheit und ist nicht mehr änderbar.)

Mit einem sein-Verb: **Wenn er früher losgefahren wäre, wäre er nicht zu spät gekommen.**

**Mit Modalverben im Typ III:** Doppelinfinitiv (Ersatzinfinitiv) statt Partizip II des Modalverbs:
**Wenn wir das gewusst hätten, hätten wir anders entscheiden können.** (nicht: "...hätten wir anders entscheiden gekonnt")""",
        "examples": [
            {
                "label": "Typ I (real)",
                "sentence": "**Wenn** der Kunde zusagt, **unterschreiben** wir noch diese Woche.",
                "note": "Indikativ Präsens in beiden Teilen - realistische Bedingung."
            },
            {
                "label": "Typ II (hypothetisch, Gegenwart)",
                "sentence": "**Wenn** ich mehr Zeit **hätte**, **würde** ich die Analyse noch vertiefen.",
                "note": "Konjunktiv II Präsens - momentan nicht der Fall, aber vorstellbar."
            },
            {
                "label": "Typ III (irreal, Vergangenheit)",
                "sentence": "**Wenn** wir den Fehler früher **entdeckt hätten**, **hätten** wir den Schaden **vermeiden können**.",
                "note": "Konjunktiv II Vergangenheit (hätten + Partizip II) in beiden Teilen; Modalverb 'können' als Doppelinfinitiv am Ende."
            },
            {
                "label": "Typ III mit sein",
                "sentence": "**Wenn** sie pünktlich **losgefahren wäre**, **wäre** sie nicht zu spät **gekommen**.",
                "note": "losfahren/kommen bilden das Perfekt mit sein → also auch hier wäre, nicht hätte."
            },
        ],
        "mistakes": [
            "Typ III mit würde + Infinitiv statt hätte/wäre + Partizip II bilden: ❌ 'Wenn wir das gewusst würden, würden wir anders handeln.' → ✅ 'Wenn wir das gewusst hätten, hätten wir anders gehandelt.' (Vergangenheit braucht Konjunktiv II Vergangenheit, nicht die würde-Form)",
            "hätte statt wäre bei sein-Verben: ❌ 'Wenn er früher losgefahren hätte' → ✅ 'Wenn er früher losgefahren wäre' (losfahren bildet das Perfekt mit sein)",
            "Modalverb im Typ III als Partizip II statt Doppelinfinitiv: ❌ '...hätten wir anders entscheiden gekonnt' → ✅ '...hätten wir anders entscheiden können'",
            "Typ II und Typ III unbeabsichtigt mischen: die beiden Satzteile sollten im selben Typ stehen, sonst entsteht eine (nur bewusst einzusetzende) gemischte Bedingung.",
        ],
        "exercise_hint": "Satztransformation: Sätze zwischen Typ I, II und III umformen. Fehlersuche: falsche Hilfsverb-Wahl (hätte/wäre) und falsche Modalverb-Bildung im Typ III.",
    },

    {
        "id": "b2_substantivierte_adjektive",
        "title": "Substantivierte Adjektive und Partizipien - der/die Angestellte, der/die Deutsche",
        "level": "B2",
        "category": "Kasus",
        "explanation": """Manche Nomen sind eigentlich Adjektive oder Partizipien, die wie ein Nomen benutzt werden (großgeschrieben, mit Artikel) - aber sie **deklinieren weiterhin wie ein Adjektiv**, nicht wie ein normales Nomen.

**Typische substantivierte Adjektive/Partizipien:** der/die Angestellte, der/die Deutsche, der/die Bekannte, der/die Erwachsene, der/die Vorsitzende, der/die Reisende

**Grundprinzip:** Genau dieselbe Endung wie ein normales Adjektiv vor einem Nomen an derselben Stelle (siehe Regel 'Adjektivdeklination') - nur dass hier kein zusätzliches Nomen mehr folgt.

---

### Mit bestimmtem Artikel
| | mask. | fem. |
|--|-------|------|
| **Nom.** | der Angestellt**e** | die Angestellt**e** |
| **Akk.** | den Angestellt**en** | die Angestellt**e** |
| **Dat.** | dem Angestellt**en** | der Angestellt**en** |
| **Gen.** | des Angestellt**en** | der Angestellt**en** |

### Mit unbestimmtem Artikel (kein Artikel zeigt die Endung → Adjektiv muss sie zeigen)
| | mask. | fem. |
|--|-------|------|
| **Nom.** | ein Angestellt**er** | eine Angestellt**e** |
| **Akk.** | einen Angestellt**en** | eine Angestellt**e** |
| **Dat.** | einem Angestellt**en** | einer Angestellt**en** |
| **Gen.** | eines Angestellt**en** | einer Angestellt**en** |

### Plural
mit Artikel: in allen vier Kasus dieselbe Endung -en (die/die/den/der Angestellt**en**) - nur der Artikel ändert sich; ohne Artikel: Angestellt**e** (Nom./Akk.)""",
        "examples": [
            {
                "label": "Bestimmter Artikel, Nominativ",
                "sentence": "**Der Angestellte** hat den Vertrag unterschrieben.",
                "note": "Wie ein Adjektiv nach 'der' → Endung -e (Nominativ maskulin)."
            },
            {
                "label": "Unbestimmter Artikel, Akkusativ",
                "sentence": "Wir haben **einen Deutschen** als neuen Berater eingestellt.",
                "note": "Nach 'einen' (kein Artikel-Ende sichtbar außer -en) → Adjektivendung -en (Akkusativ maskulin, wie bei jedem Adjektiv nach 'einen')."
            },
            {
                "label": "Feminin, Dativ",
                "sentence": "Ich habe mit **einer Bekannten** über das Angebot gesprochen.",
                "note": "Nach 'einer' → Endung -en (Dativ feminin)."
            },
            {
                "label": "Plural ohne Artikel",
                "sentence": "**Erwachsene** zahlen den vollen Preis, Kinder die Hälfte.",
                "note": "Plural ohne Artikel → Endung -e, wie beim Adjektiv ohne Artikel."
            },
        ],
        "mistakes": [
            "Wie ein normales Nomen ohne Adjektivendung behandeln: ❌ 'der Angestellter' → ✅ 'der Angestellte' (nach bestimmtem Artikel im Nominativ ist die Endung -e, nicht -er)",
            "Falsche Endung nach 'ein' im Nominativ maskulin: ❌ 'ein Deutsche' → ✅ 'ein Deutscher' (kein Artikel-Signal → Adjektiv braucht -er)",
            "Eigene weibliche Form mit -in erfinden: ❌ 'die Angestelltin' → ✅ 'die Angestellte' (substantivierte Adjektive haben keine -in-Form; das Genus zeigt allein der Artikel + die Adjektivendung)",
        ],
        "exercise_hint": "Lückentext: richtige Endung von der/die Angestellte, Deutsche, Bekannte je nach Artikeltyp und Kasus einsetzen.",
    },

    {
        "id": "b2_lassen_kausativ",
        "title": "Kausativkonstruktion mit 'lassen' - jemanden etwas machen lassen",
        "level": "B2",
        "category": "Verben",
        "explanation": """'lassen' + Akkusativobjekt (Person) + Infinitiv beschreibt, dass man **jemand anderen** etwas tun **lässt** oder **veranlasst** - man tut es nicht selbst. Das ist die Kausativkonstruktion.

**Bildung:** Subjekt + lassen (konjugiert) + Akkusativobjekt (Person) + ... + Infinitiv (Satzende)

"Der Chef **lässt** den Assistenten die Präsentation **vorbereiten**." = Der Chef veranlasst, dass der Assistent die Präsentation vorbereitet (der Chef selbst tut es nicht).

**Zwei Bedeutungen von 'lassen' + Person + Infinitiv:**
1. **Veranlassen** (jemanden etwas tun lassen): Ich lasse den Techniker den Drucker reparieren.
2. **Erlauben** (zulassen): Sie lässt ihren Mitarbeiter früher gehen.

**Perfekt: Doppelinfinitiv (Ersatzinfinitiv)** - wie bei Modalverben - **lassen** bleibt im Infinitiv, statt 'gelassen' zu benutzen:
"Der Chef **hat** den Assistenten die Präsentation **vorbereiten lassen**." (nicht: "...vorbereiten gelassen")

**Wichtig - nicht verwechseln mit 'sich lassen' (Passiv-Ersatzform, siehe eigene Regel 'Passiv-Ersatzformen'):**
- **Kausativ:** Subjekt lässt eine ANDERE Person etwas tun → "Er lässt **den Techniker** das Gerät reparieren." (Agent genannt)
- **sich lassen (Passiv-Ersatz):** die SACHE selbst ist Subjekt, kein Akkusativobjekt-Person nötig → "Das Gerät **lässt sich** reparieren." (= kann repariert werden)""",
        "examples": [
            {
                "label": "Kausativ (veranlassen)",
                "sentence": "Wir **lassen** die Buchhaltung die Rechnung **prüfen**.",
                "note": "Wir tun es nicht selbst - wir veranlassen, dass die Buchhaltung es tut."
            },
            {
                "label": "Kausativ (erlauben)",
                "sentence": "Der Vorstand **lässt** die Mitarbeiter im Homeoffice **arbeiten**.",
                "note": "lassen = erlauben, zulassen."
            },
            {
                "label": "Perfekt mit Doppelinfinitiv",
                "sentence": "Sie **hat** ihr Auto in der Werkstatt **reparieren lassen**.",
                "note": "Ersatzinfinitiv 'lassen' statt 'gelassen' im Perfekt."
            },
            {
                "label": "Kausativ vs. sich lassen",
                "sentence": "Er **lässt** einen Experten die Software **installieren**. / Die Software **lässt sich** leicht **installieren**.",
                "note": "Erster Satz: jemand anderes handelt (Kausativ). Zweiter Satz: die Software selbst kann installiert werden (Passiv-Ersatz)."
            },
        ],
        "mistakes": [
            "Perfekt mit 'gelassen' statt Doppelinfinitiv: ❌ 'Er hat sein Auto reparieren gelassen.' → ✅ 'Er hat sein Auto reparieren lassen.'",
            "Kausativ und sich lassen verwechseln: ❌ 'Er lässt sich das Problem lösen.' wenn eigentlich gemeint ist, dass das Problem gelöst werden kann → dafür braucht man die SACHE als Subjekt: 'Das Problem lässt sich lösen.'",
            "Akkusativobjekt (Person) vergessen: ❌ 'Der Chef lässt vorbereiten.' → ✅ 'Der Chef lässt den Assistenten vorbereiten.' (die handelnde Person steht im Akkusativ)",
        ],
        "exercise_hint": "Satztransformation: Aktivsätze mit einem zweiten Handelnden in die Kausativkonstruktion mit 'lassen' umformen. Fehlersuche: Doppelinfinitiv im Perfekt vs. 'sich lassen'.",
    },

    {
        "id": "b2_zustandspassiv_vorgangspassiv",
        "title": "Zustandspassiv vs. Vorgangspassiv - Ergebnis oder Vorgang?",
        "level": "B2",
        "category": "Verbformen",
        "explanation": """Deutsch unterscheidet zwei Arten von Passiv, je nachdem, ob man einen **laufenden Vorgang** oder ein **fertiges Ergebnis** beschreibt.

**Vorgangspassiv: werden + Partizip II**
→ beschreibt eine Handlung, die passiert (gerade oder regelmäßig) - der Fokus liegt auf dem Prozess.

**Zustandspassiv: sein + Partizip II**
→ beschreibt das Ergebnis einer abgeschlossenen Handlung - einen Zustand, der daraus entstanden ist.

---

### Direkter Vergleich

| | Vorgangspassiv (werden) | Zustandspassiv (sein) |
|--|--------------------------|-------------------------|
| Präsens | Die Tür **wird geschlossen**. (jemand schließt sie gerade) | Die Tür **ist geschlossen**. (sie ist zu, Ergebnis) |
| Präteritum | Die Tür **wurde geschlossen**. (der Vorgang fand statt) | Die Tür **war geschlossen**. (der Zustand bestand) |

**Faustregel:** Wenn man fragt "Was passiert gerade / passierte damals?" → Vorgangspassiv. Wenn man fragt "In welchem Zustand ist/war etwas?" → Zustandspassiv.

**Vorsicht bei der Abgrenzung zum echten Adjektiv:** Das Zustandspassiv sieht aus wie 'sein + Adjektiv', ist aber von einem Verb abgeleitet (Partizip II) und beschreibt das Resultat EINER Handlung: "Das Fenster **ist repariert**." (jemand hat es repariert) vs. ein echtes Adjektiv ohne zugrunde liegende Handlung: "Das Fenster **ist kaputt**." (kaputt ist kein Partizip).""",
        "examples": [
            {
                "label": "Vorgangspassiv (Prozess)",
                "sentence": "Die Unterlagen **werden** gerade **geprüft**.",
                "note": "Der Vorgang läuft im Moment - jemand prüft sie."
            },
            {
                "label": "Zustandspassiv (Ergebnis)",
                "sentence": "Die Unterlagen **sind** bereits **geprüft**.",
                "note": "Die Prüfung ist abgeschlossen - Fokus auf dem Ergebnis, nicht auf dem Prozess."
            },
            {
                "label": "Beide im Kontrast",
                "sentence": "Das Büro **wird** um 18 Uhr **abgeschlossen**. Ab 18 Uhr **ist** es **abgeschlossen**.",
                "note": "Erster Satz: der Vorgang des Abschließens. Zweiter Satz: der resultierende Zustand."
            },
        ],
        "mistakes": [
            "Zustandspassiv als Vorgang missverstehen: 'Die Tür ist geschlossen' beschreibt keinen laufenden Vorgang, sondern einen Zustand - für den Vorgang braucht man 'wird geschlossen'.",
            "Zustandspassiv mit echtem Adjektiv gleichsetzen: nicht jedes 'sein + Wort' ist Zustandspassiv - nur wenn das Wort ein Partizip II eines Verbs ist ('ist repariert'), nicht bei echten Adjektiven ('ist kaputt', 'ist neu').",
            "werden im Zustandspassiv verwenden: ❌ 'Die Tür wird seit einer Stunde geschlossen.' wenn ein bereits bestehender Zustand gemeint ist → ✅ 'Die Tür ist seit einer Stunde geschlossen.'",
        ],
        "exercise_hint": "Satztransformation/Fehlersuche: Vorgangspassiv (werden) und Zustandspassiv (sein) im Kontext unterscheiden und korrekt bilden.",
    },

    {
        "id": "b2_wahrnehmungsverben",
        "title": "Wahrnehmungsverben + Infinitiv ohne zu - hören, sehen, fühlen, spüren",
        "level": "B2",
        "category": "Verben",
        "explanation": """Verben der direkten Sinneswahrnehmung (hören, sehen, fühlen, spüren) können mit einem **Akkusativobjekt + Infinitiv ohne zu** kombiniert werden, wenn man eine Handlung direkt und gleichzeitig wahrnimmt - ähnlich wie bei Modalverben und bei 'lassen' (siehe eigene Regel).

**Bildung:** Subjekt + Wahrnehmungsverb (konjugiert) + Akkusativobjekt + Infinitiv (Satzende, OHNE zu)

"Ich **höre** ihn **singen**." = Ich höre, wie er (gerade) singt - direkte, gleichzeitige Wahrnehmung.

**Perfekt:** Wie bei 'lassen' ist der Doppelinfinitiv (Ersatzinfinitiv) die Standardform: "Ich **habe** ihn **singen hören**." Anders als bei 'lassen' gilt bei hören/sehen im Sprachgebrauch aber auch die Form mit Partizip II ("...singen gehört") als akzeptabel - im schriftlichen/formellen Deutsch bleibt der Doppelinfinitiv trotzdem die sicherere Wahl.

**Alternative mit dass-Satz:** Wenn man eher berichtet als direkt/gleichzeitig wahrnimmt, ist ein dass-Satz natürlicher:
"Ich habe gehört, **dass** er ein neues Projekt **leitet**." (Bericht, keine direkte gleichzeitige Wahrnehmung)""",
        "examples": [
            {
                "label": "hören + Infinitiv",
                "sentence": "Ich **höre** die Kollegin telefonieren.",
                "note": "Direkte, gleichzeitige Wahrnehmung - Infinitiv ohne zu."
            },
            {
                "label": "sehen + Infinitiv",
                "sentence": "Wir **sehen** die Kollegen ins Büro **kommen**.",
                "note": "sehen + Akkusativobjekt (die Kollegen) + Infinitiv (kommen)."
            },
            {
                "label": "Perfekt mit Doppelinfinitiv",
                "sentence": "Ich **habe** ihn im Nebenraum **sprechen hören**.",
                "note": "Ersatzinfinitiv 'hören' statt Partizip II 'gehört' - die Standardform im geschriebenen Deutsch."
            },
            {
                "label": "Alternative mit dass",
                "sentence": "Ich habe gehört, **dass** das Projekt verzögert **wird**.",
                "note": "Bericht statt direkter Wahrnehmung - hier passt eher ein dass-Satz als der bloße Infinitiv."
            },
        ],
        "mistakes": [
            "zu vor dem Infinitiv ergänzen: ❌ 'Ich höre ihn zu singen.' → ✅ 'Ich höre ihn singen.' (Infinitiv ohne zu, wie bei Modalverben)",
            "Akkusativobjekt vergessen: ❌ 'Ich höre singen.' ohne Bezug auf eine Person → ✅ 'Ich höre ihn/sie/die Kollegin singen.'",
            "Falsche Wortstellung: ❌ 'Ich höre singen ihn.' → ✅ 'Ich höre ihn singen.' (Akkusativobjekt steht vor dem Infinitiv, Infinitiv ganz am Ende)",
        ],
        "exercise_hint": "Satztransformation: dass-Sätze in Wahrnehmungsverb-Konstruktionen mit Infinitiv ohne zu umformen. Fehlersuche mit 'zu' und falscher Wortstellung.",
    },

    {
        "id": "c1_als_ob",
        "title": "Irrealer Vergleich - 'als ob' / 'als wenn' + Konjunktiv II",
        "level": "C1",
        "category": "Verbformen",
        "explanation": """'als ob' und 'als wenn' (bedeutungsgleich, 'als ob' ist gebräuchlicher) leiten einen **irrealen Vergleichssatz** ein: man vergleicht die reale Situation mit einer erfundenen, nicht-wirklichen. Deshalb steht danach immer der **Konjunktiv II**.

**Bildung 1: als ob / als wenn + Nebensatz (Verb ans Ende)**
Er tut, **als ob** er nichts **wüsste**. (in Wirklichkeit weiß er wahrscheinlich etwas)

**Bildung 2: als + Inversion (ohne ob/wenn, Verb direkt nach als)**
Er tut, **als wüsste** er nichts. (gleiche Bedeutung, kompaktere Konstruktion)

**Welche Zeitform des Konjunktivs?**
- **Konjunktiv II Präsens** (wäre, hätte, würde + Infinitiv, käme...): wenn der Vergleich sich auf die GLEICHE Zeit wie der Hauptsatz bezieht.
- **Konjunktiv II Vergangenheit** (hätte/wäre + Partizip II): wenn der Vergleich sich auf eine FRÜHERE Zeit bezieht als der Hauptsatz.

Sie sah aus, **als ob** sie die ganze Nacht **gearbeitet hätte**. (Vergleich bezieht sich auf VORHER, deshalb Konjunktiv II Vergangenheit)""",
        "examples": [
            {
                "label": "als ob + Konjunktiv II Präsens",
                "sentence": "Er tut, **als ob** er nichts **wüsste**.",
                "note": "Gleichzeitiger, irrealer Vergleich - Konjunktiv II Präsens von 'wissen'."
            },
            {
                "label": "als + Inversion (ohne ob)",
                "sentence": "Sie reagierte, **als wäre** nichts **passiert**.",
                "note": "Kompaktere Variante ohne 'ob' - das Verb steht direkt nach 'als'."
            },
            {
                "label": "Konjunktiv II Vergangenheit (vorzeitig)",
                "sentence": "Er klang am Telefon, **als ob** er **geweint hätte**.",
                "note": "Der Vergleich bezieht sich auf etwas VOR dem Anruf → Konjunktiv II Vergangenheit."
            },
        ],
        "mistakes": [
            "Indikativ statt Konjunktiv II: ❌ 'Er tut, als ob er nichts weiß.' → ✅ '...als ob er nichts wüsste.'",
            "Konjunktiv II Präsens statt Vergangenheit bei vorzeitigem Vergleich: ❌ 'Sie sah aus, als ob sie die ganze Nacht arbeiten würde.' → ✅ '...als ob sie die ganze Nacht gearbeitet hätte.' (die Handlung liegt VOR dem Hauptsatz)",
            "als + Nebensatzstellung ohne Inversion: ❌ 'als er nichts wüsste' (ohne ob, aber ohne Inversion) → ✅ entweder 'als ob er nichts wüsste' (Verb am Ende) ODER 'als wüsste er nichts' (Verb direkt nach als, Inversion) - nicht mischen.",
        ],
        "exercise_hint": "Satztransformation: Sätze mit 'als ob'/Inversion und passender Konjunktiv-II-Zeitform bilden. Fehlersuche mit Indikativ-Fehlern.",
    },

    {
        "id": "c1_indirekte_aufforderung",
        "title": "Indirekte Aufforderung - sollen in der indirekten Rede",
        "level": "C1",
        "category": "Verbformen",
        "explanation": """Die Regel 'Indirekte Rede - Konjunktiv I' behandelt wiedergegebene Aussagen. Wird stattdessen eine **Aufforderung, Bitte oder ein Befehl** wiedergegeben (im Original ein Imperativ), benutzt man **sollen** statt eines wiederholten Imperativs.

**Bildung:** Einleitungsverb (sagen, bitten, auffordern...) + dass-Satz oder dass-los + sollen (Konjunktiv I oder II) + Infinitiv

Direkte Aufforderung: "**Warten** Sie hier!"
Indirekte Aufforderung: Er sagte, ich **solle** hier warten. (solle = Konjunktiv I von sollen)

**Konjunktiv I oder II?** Dieselbe Regel wie bei der indirekten Rede allgemein: Wenn die Konjunktiv-I-Form mit dem Indikativ identisch ist (bei wir/sie/Sie: 'sollen' = Indikativ UND Konjunktiv I), weicht man auf **Konjunktiv II ('sollten')** aus, um eindeutig zu bleiben:

Er sagte, **wir sollten** nicht zu spät kommen. (nicht 'wir sollen', das wäre nicht von der Realität unterscheidbar)

**Alternative (oft eleganter):** Infinitivkonstruktion mit 'bitten/auffordern + Akkusativ + zu':
Er bat mich **darum**, ihm die Unterlagen **zu schicken**. (= Er sagte, ich solle ihm die Unterlagen schicken.)""",
        "examples": [
            {
                "label": "solle (Konjunktiv I, eindeutig)",
                "sentence": "Der Vorgesetzte sagte, ich **solle** den Bericht bis Freitag fertigstellen.",
                "note": "solle ≠ soll (Indikativ) - eindeutig als Konjunktiv erkennbar, deshalb keine Ausweichform nötig."
            },
            {
                "label": "sollten (Konjunktiv II, weil solle=soll bei Plural gleich wäre)",
                "sentence": "Sie teilte mit, wir **sollten** die Präsentation überarbeiten.",
                "note": "'wir sollen' wäre mit dem Indikativ identisch, deshalb Konjunktiv II 'sollten'."
            },
            {
                "label": "Negative Aufforderung",
                "sentence": "Er ermahnte uns, wir **sollten** die Frist nicht erneut **verpassen**.",
                "note": "Verneinte indirekte Aufforderung - 'nicht' vor dem Infinitiv, sollten trägt den Konjunktiv."
            },
            {
                "label": "Alternative mit Infinitivkonstruktion",
                "sentence": "Die Kundin bat den Kollegen darum, sie **zurückzurufen**.",
                "note": "bitten + Akkusativ + zu + Infinitiv - oft eleganter als die sollen-Konstruktion."
            },
        ],
        "mistakes": [
            "Indikativ 'soll/sollen' statt Konjunktiv verwenden, wo Mehrdeutigkeit entsteht: ❌ 'Er sagte, wir sollen pünktlich sein.' → ✅ '...wir sollten pünktlich sein.' (sollen ist bei wir/sie/Sie mit dem Indikativ identisch)",
            "Den ursprünglichen Imperativ direkt wiederholen: ❌ 'Er sagte, warten Sie hier.' → ✅ 'Er sagte, ich solle hier warten.' (der Imperativ wird nicht einfach zitiert, sondern mit sollen umformuliert)",
            "sollen mit müssen verwechseln: sollen in der indirekten Aufforderung gibt den ursprünglichen Auftrag/die Bitte einer anderen Person wieder, nicht eine eigene innere Notwendigkeit (siehe Regel 'Modalverben - alle Formen', müssen vs. sollen).",
        ],
        "exercise_hint": "Satztransformation: direkte Imperativsätze in indirekte Aufforderungen mit sollen umformen, inklusive der Konjunktiv-I/II-Auswahlregel.",
    },

    {
        "id": "c1_genitiv_verben",
        "title": "Seltene Genitiv-Verben - sich erfreuen, bedürfen, gedenken",
        "level": "C1",
        "category": "Kasus",
        "explanation": """Eine kleine Gruppe von Verben verlangt einen **Genitiv** als Objekt statt Akkusativ oder Dativ. Diese Verben gehören zum sehr formellen, geschriebenen Register (Reden, offizielle Texte, gehobene Berichte) und sind im gesprochenen Alltagsdeutsch selten.

| Verb | Bedeutung | Beispiel |
|------|-----------|---------|
| **sich erfreuen + Gen.** | genießen, positiv erleben | Das Angebot erfreut sich großer Beliebtheit. |
| **bedürfen + Gen.** | brauchen, erfordern (formell) | Die Entscheidung bedarf einer genauen Prüfung. |
| **gedenken + Gen.** | sich erinnern an, ehren (formell, oft in Reden) | Wir gedenken der Opfer des Unglücks. |

**Konjugation von 'bedürfen'** (unregelmäßig, wie 'dürfen'): ich bed**a**rf, du bed**a**rfst, er bed**a**rf, wir bedürfen, ihr bedürft, sie bedürfen. Präteritum: bedurfte. Partizip II: bedurft.

**Konjugation von 'gedenken'** (wie 'denken', mit Vorsilbe ge-): ich gedenke... Präteritum: gedachte. Partizip II: gedacht.""",
        "examples": [
            {
                "label": "sich erfreuen + Genitiv",
                "sentence": "Das neue Produkt **erfreut sich** großen **Interesses** bei den Kunden.",
                "note": "erfreuen + Gen. - formeller Ausdruck für 'ist beliebt/interessant für'."
            },
            {
                "label": "bedürfen + Genitiv",
                "sentence": "Ein Projekt dieser Größe **bedarf** einer sorgfältigen **Planung**.",
                "note": "bedürfen + Gen. - formeller Ausdruck für 'braucht'."
            },
            {
                "label": "gedenken + Genitiv",
                "sentence": "In seiner Rede **gedachte** der Vorstand **der langjährigen Mitarbeiter**.",
                "note": "gedenken + Gen. - typisch in Reden und Gedenkveranstaltungen."
            },
        ],
        "mistakes": [
            "Akkusativ statt Genitiv nach gedenken: ❌ 'Wir gedenken die Opfer.' → ✅ 'Wir gedenken der Opfer.'",
            "Akkusativ statt Genitiv nach bedürfen: ❌ 'Das bedarf eine Prüfung.' → ✅ 'Das bedarf einer Prüfung.'",
            "bedürfen im Präsens wie ein schwaches Verb konjugieren: ❌ 'es bedürft' → ✅ 'es bedarf' (Vokalwechsel wie bei dürfen: ich darf/bedarf)",
        ],
        "exercise_hint": "Lückentext: richtige Genitivform nach sich erfreuen/bedürfen/gedenken einsetzen. Fehlersuche mit Akkusativ-statt-Genitiv-Fehlern.",
    },

    {
        "id": "c1_erweiterte_modalpartikeln",
        "title": "Erweiterte Modalpartikeln - denn, schon, bloß, nur",
        "level": "C1",
        "category": "Wortstellung",
        "explanation": """Über die vier Modalpartikeln aus der Regel 'Modalpartikeln - Gefühle und Haltungen ausdrücken' (doch, mal, ja, eigentlich...) hinaus gibt es weitere, die auf C1-Niveau den Ton eines Satzes feiner steuern.

| Partikel | Kontext | Bedeutung |
|----------|---------|-----------|
| **denn** | in Fragen | macht eine Frage weicher, zeigt echtes Interesse (nicht zu verwechseln mit der Konjunktion 'denn' = weil) |
| **schon** | Aussagen (Zuversicht) | drückt Zuversicht/Beruhigung aus (nicht zu verwechseln mit 'schon' = bereits) |
| **bloß / nur** | in Aufforderungen (Imperativ) | verstärkt eine Warnung oder Bitte - dringlich oder beruhigend, je nach Ton |

**denn (Modalpartikel) vs. denn (Konjunktion):**
Als Modalpartikel steht 'denn' in einer Frage und macht sie höflicher/interessierter: "Wie geht es Ihnen **denn**?" Als Konjunktion verbindet 'denn' zwei Hauptsätze und bedeutet 'weil': "Er kam nicht, **denn** er war krank." Nur der Kontext (Frage vs. Grund) unterscheidet die beiden.

**schon (Modalpartikel) vs. schon (Zeitadverb):**
Als Modalpartikel drückt 'schon' Zuversicht aus: "Das **schaffen** wir **schon**." (= keine Sorge, das klappt) Als Zeitadverb bedeutet 'schon' 'bereits': "Er ist **schon** angekommen."

**bloß / nur in Aufforderungen:** verstärken einen Imperativ - je nach Tonfall als dringliche Warnung oder als beruhigende Einschränkung:
"Vergessen Sie das **bloß** nicht!" (eindringliche Warnung)
"Rufen Sie mich **nur** an, wenn es Probleme gibt." (beruhigende Einladung, keine Dringlichkeit)""",
        "examples": [
            {
                "label": "denn in einer Frage",
                "sentence": "Wo warst du **denn** die ganze Zeit?",
                "note": "Zeigt echtes Interesse/leichte Verwunderung - keine Konjunktion, kein zweiter Hauptsatz nötig."
            },
            {
                "label": "schon (Zuversicht)",
                "sentence": "Machen Sie sich keine Sorgen, das **wird schon klappen**.",
                "note": "schon = Zuversicht, nicht 'bereits' - eine Zeitbedeutung wäre hier unpassend."
            },
            {
                "label": "bloß im Imperativ (Warnung)",
                "sentence": "Sag das **bloß** nicht dem Kunden!",
                "note": "Verstärkt die Warnung - dringlicher als ohne Partikel."
            },
            {
                "label": "nur im Imperativ (beruhigend)",
                "sentence": "Fragen Sie **nur**, wenn etwas unklar ist.",
                "note": "nur wirkt hier einladend/beruhigend, nicht dringlich."
            },
        ],
        "mistakes": [
            "denn (Modalpartikel) mit denn (Konjunktion) verwechseln: die Modalpartikel steht in Fragen und braucht keinen zweiten Hauptsatz; die Konjunktion 'denn' verbindet zwei Hauptsätze und bedeutet 'weil' - unterschiedliche Funktion, gleiches Wort.",
            "schon als Modalpartikel für 'bereits' halten: ❌ 'Das wird schon klappen' als Zeitangabe missverstehen → hier ist 'schon' reine Zuversicht, keine Zeitangabe.",
            "Modalpartikeln am Satzanfang verwenden: wie die meisten Modalpartikeln (siehe Grundregel) stehen auch denn/schon/bloß/nur nie am Satzanfang, sondern im Mittelfeld nach dem finiten Verb.",
        ],
        "exercise_hint": "Mehrfachauswahl: welche Bedeutung hat die Partikel im Kontext (Modalpartikel vs. Konjunktion/Zeitadverb)? Ton-Analyse: dringliche vs. beruhigende Wirkung von bloß/nur erkennen.",
    },

    # ==================== ERGAENZUNG - HAUPTSATZ/NEBENSATZ, FRAGESAETZE, DASS, WANN/WENN, SATZZEICHEN ====================

    {
        "id": "grund_hauptsatz_nebensatz",
        "title": "Hauptsatz und Nebensatz - wo steht das Verb?",
        "level": "A1",
        "category": "Grundlagen",
        "explanation": """Ein deutscher Satz ist entweder ein Hauptsatz oder ein Nebensatz - das entscheidet, wo das konjugierte Verb steht.

**Hauptsatz:**
- Kann allein stehen (vollständiger Gedanke)
- Das konjugierte Verb steht an **Position 2**

"Ich lerne heute Deutsch."

**Nebensatz:**
- Kann NICHT allein stehen - braucht einen Hauptsatz dazu
- Wird eingeleitet durch eine subordinierende Konjunktion (weil, dass, wenn, obwohl...), ein Relativpronomen (der/die/das...) oder ein Fragewort (wann, warum...)
- Das konjugierte Verb steht am **ENDE**

"..., weil ich morgen einen Test schreibe."

---

### Zwei Hauptsätze zusammen
Verbunden durch und/aber/oder/denn - beide Teile bleiben Hauptsätze, jeder mit eigenem Verb an Position 2:
"Ich lerne Deutsch, **und** ich höre auch Podcasts."

### Hauptsatz + Nebensatz - Reihenfolge ist frei
- **Hauptsatz zuerst:** "Ich schreibe eine Prüfung, weil ich Deutsch lernen **will**." (Nebensatz-Verb am Ende)
- **Nebensatz zuerst:** "Weil ich Deutsch lernen will, **schreibe** ich eine Prüfung." (Nebensatz-Verb am Ende; danach im Hauptsatz Verb-Subjekt-Inversion)

**Wichtig:** Steht der Nebensatz VOR dem Hauptsatz, zählt der ganze Nebensatz als Position 1. Das Verb des Hauptsatzes rückt direkt danach auf Position 2 - vor das Subjekt (Inversion).""",
        "examples": [
            {
                "label": "Hauptsatz allein",
                "sentence": "Ich lerne heute Deutsch.",
                "note": "Vollständiger Satz, kann allein stehen, Verb an Position 2."
            },
            {
                "label": "Nebensatz mit weil (Verb am Ende)",
                "sentence": "Ich bin müde, weil ich schlecht **geschlafen habe**.",
                "note": "weil leitet den Nebensatz ein, das Verb (habe) steht ganz am Ende."
            },
            {
                "label": "Nebensatz vorne, Inversion im Hauptsatz",
                "sentence": "Weil ich schlecht geschlafen habe, **bin** ich müde.",
                "note": "Nebensatz = Position 1, danach sofort Verb, dann Subjekt im Hauptsatz."
            },
            {
                "label": "Zwei Hauptsätze mit und",
                "sentence": "Ich koche, und mein Kollege **deckt** den Tisch.",
                "note": "Beide Teile sind Hauptsätze, jeweils mit eigenem Verb an Position 2."
            },
        ],
        "mistakes": [
            "Verb im Nebensatz an Position 2 statt am Ende: ❌ '..., weil ich bin müde.' → ✅ '..., weil ich müde bin.'",
            "Nach vorangestelltem Nebensatz keine Inversion: ❌ 'Weil ich müde bin, ich gehe früh ins Bett.' → ✅ 'Weil ich müde bin, gehe ich früh ins Bett.'",
            "Nebensatz als eigenständigen Satz ohne Hauptsatz stehen lassen: ❌ 'Weil ich müde bin.' (allein) ist kein vollständiger Satz - er braucht einen Hauptsatz.",
        ],
        "exercise_hint": "Satztransformation: Haupt- und Nebensatz kombinieren, Nebensatz einmal vorne und einmal hinten üben (mit Inversion). Fehlersuche: Verbposition im Nebensatz.",
    },

    {
        "id": "grund_fragesaetze",
        "title": "Fragesätze - W-Fragen und Ja/Nein-Fragen",
        "level": "A1",
        "category": "Grundlagen",
        "explanation": """Es gibt zwei Fragetypen im Deutschen, mit unterschiedlicher Wortstellung.

**W-Fragen (Ergänzungsfragen):**
Fragewort (wer, was, wann, wo, warum, wie...) + Verb (Position 2) + Rest

"**Wann** **beginnt** das Meeting?"

**Ja/Nein-Fragen (Entscheidungsfragen):**
Kein Fragewort - das Verb rückt direkt an den Satzanfang (Position 1), das Subjekt folgt danach.

"**Beginnt** das Meeting um 9 Uhr?"

---

### Kontrast: Aussagesatz vs. Frage
- Aussage: "Das Meeting beginnt um 9 Uhr." (Verb Position 2)
- Ja/Nein-Frage: "Beginnt das Meeting um 9 Uhr?" (Verb Position 1 - dieselbe Wortstellung wie beim Imperativ)
- W-Frage: "Wann beginnt das Meeting?" (Fragewort, dann Verb an Position 2)

**Wichtig:** Diese direkte Fragewortstellung gilt nur für direkte Fragen. Wird eine Frage in einen Nebensatz eingebettet ("Er fragt, wann..."), ändert sich die Wortstellung - siehe eigene Regel "Indirekte Fragesätze".""",
        "examples": [
            {
                "label": "W-Frage",
                "sentence": "**Wo** **wohnst** du?",
                "note": "Fragewort zuerst, dann das Verb an Position 2."
            },
            {
                "label": "Ja/Nein-Frage",
                "sentence": "**Wohnst** du in Berlin?",
                "note": "Kein Fragewort - das Verb steht an Position 1."
            },
            {
                "label": "W-Frage mit Modalverb",
                "sentence": "**Warum** **kannst** du heute nicht kommen?",
                "note": "Das Modalverb steht an Position 2, das Vollverb (kommen) am Satzende."
            },
            {
                "label": "Drei Varianten im Vergleich",
                "sentence": "Er kommt heute. / **Kommt** er heute? / **Wann** **kommt** er?",
                "note": "Aussage (Verb Pos. 2) - Ja/Nein-Frage (Verb Pos. 1) - W-Frage (Fragewort + Verb Pos. 2)."
            },
        ],
        "mistakes": [
            "Ja/Nein-Frage nur durch Intonation markieren, ohne die Wortstellung zu ändern: ❌ 'Du wohnst in Berlin?' als geschriebene Frage → ✅ 'Wohnst du in Berlin?' (Verb muss an Position 1)",
            "Nach dem Fragewort das Verb nicht an Position 2 setzen: ❌ 'Wo du wohnst?' → ✅ 'Wo wohnst du?'",
            "Die direkte Fragewortstellung in einer indirekten Frage beibehalten: siehe eigene Regel 'Indirekte Fragesätze' - dort steht das Verb am Ende, nicht an Position 2.",
        ],
        "exercise_hint": "Satztransformation: Aussagesätze in W-Fragen und Ja/Nein-Fragen umformen.",
    },

    {
        "id": "a2_dass_saetze",
        "title": "dass-Sätze - Nebensätze mit dass",
        "level": "A2",
        "category": "Konnektoren",
        "explanation": """'dass' leitet einen Nebensatz ein, der als Objekt oder Subjekt eines übergeordneten Verbs/Ausdrucks dient. Wie bei jedem Nebensatz steht das konjugierte Verb am Ende.

**Typische auslösende Verben/Ausdrücke:**
glauben, wissen, hoffen, sagen, denken, finden, sich freuen (dass), froh sein (dass), es ist wichtig (dass)...

"Ich glaube, **dass** der Kunde morgen **anruft**."

---

### dass vs. ob - oft verwechselt
- **dass** = eine Tatsache oder Meinung wiedergeben (kein Zweifel, DASS es passiert)
- **ob** = Ja/Nein-Unsicherheit ausdrücken

"Ich weiß, **dass** er kommt." (Tatsache) vs. "Ich weiß nicht, **ob** er kommt." (Unsicherheit)

### dass vs. Infinitivkonstruktion mit zu
Sind Haupt- und Nebensatz-Subjekt gleich, ist oft eine einfache Infinitivkonstruktion mit 'zu' eleganter als ein dass-Satz:

"Ich hoffe, **dass ich** die Prüfung bestehe." = "Ich hoffe, die Prüfung **zu bestehen**." (gleiches Subjekt: ich)

Sind die Subjekte unterschiedlich, MUSS ein dass-Satz stehen: "Ich hoffe, **dass er** die Prüfung besteht." (er ≠ ich - kein zu-Infinitiv möglich)""",
        "examples": [
            {
                "label": "dass nach glauben",
                "sentence": "Ich glaube, **dass** das Angebot **passt**.",
                "note": "dass leitet den Nebensatz ein, Verb steht am Ende."
            },
            {
                "label": "dass vs. ob",
                "sentence": "Ich bin sicher, **dass** sie kommt. / Ich bin nicht sicher, **ob** sie kommt.",
                "note": "dass = Tatsache/Meinung, ob = echte Unsicherheit."
            },
            {
                "label": "dass bei unterschiedlichem Subjekt",
                "sentence": "Er hofft, **dass** wir pünktlich **sind**.",
                "note": "Subjekte (er/wir) sind unterschiedlich - dass-Satz nötig, kein zu-Infinitiv möglich."
            },
            {
                "label": "dass-Satz als Subjekt am Satzanfang",
                "sentence": "**Dass** er zu spät **kam**, hat niemanden überrascht.",
                "note": "Ein dass-Satz kann auch als Subjekt des Hauptsatzes am Satzanfang stehen."
            },
        ],
        "mistakes": [
            "Verb im dass-Satz nicht ans Ende stellen: ❌ 'Ich glaube, dass ist das richtig.' → ✅ 'Ich glaube, dass das richtig ist.'",
            "dass und ob verwechseln: ❌ 'Ich weiß nicht, dass er kommt.' bei echter Unsicherheit → ✅ 'Ich weiß nicht, ob er kommt.'",
            "dass-Satz benutzen, obwohl das Subjekt identisch ist und ein zu-Infinitiv eleganter wäre: nicht falsch, aber auf B1+ Niveau stilistisch schwächer - 'Ich hoffe, zu kommen.' besser als 'Ich hoffe, dass ich komme.' wenn beide Subjekte gleich sind.",
        ],
        "exercise_hint": "Lückentext: dass oder ob je nach Kontext einsetzen. Satztransformation: dass-Satz in zu-Infinitiv umformen (bei gleichem Subjekt).",
    },

    {
        "id": "b1_wann_wenn",
        "title": "wann (Fragewort) vs. wenn (Konjunktion)",
        "level": "B1",
        "category": "Konnektoren",
        "explanation": """'wann' und 'wenn' werden oft verwechselt, weil beide im Englischen 'when' entsprechen können - sie haben aber unterschiedliche Funktionen.

**wann = Fragewort** (fragt nach einem Zeitpunkt, direkt oder indirekt)

"**Wann** kommst du?" (direkte Frage) / "Ich weiß nicht, **wann** er **kommt**." (indirekte Frage - siehe eigene Regel "Indirekte Fragesätze")

**wenn = Konjunktion** (leitet einen Nebensatz ein, Verb ans Ende)
- Bedingung (= falls): "**Wenn** es regnet, bleibe ich zu Hause."
- Zeitpunkt in Gegenwart/Zukunft, oder wiederholt in der Vergangenheit (siehe eigene Regel "als vs. wenn"): "**Wenn** das Meeting beginnt, schalte ich mein Handy aus."

**Der Trigger-Test:** Lässt sich das Wort durch "zu welchem Zeitpunkt?" ersetzen und bleibt eine echte Frage? → **wann**. Lässt es sich durch "falls" oder "jedes Mal wenn" ersetzen? → **wenn**.""",
        "examples": [
            {
                "label": "wann als Fragewort",
                "sentence": "**Wann** beginnt die Prüfung?",
                "note": "Direkte Frage nach dem Zeitpunkt."
            },
            {
                "label": "wann in indirekter Frage",
                "sentence": "Er hat gefragt, **wann** die Prüfung **beginnt**.",
                "note": "Verb am Ende, weil es sich um einen Nebensatz handelt."
            },
            {
                "label": "wenn als Bedingung",
                "sentence": "**Wenn** ich Zeit habe, rufe ich dich an.",
                "note": "wenn = falls, keine Frage."
            },
            {
                "label": "Kontrast im selben Kontext",
                "sentence": "**Wann** kommst du? / **Wenn** du kommst, sag Bescheid.",
                "note": "Erstes: Frage nach dem Zeitpunkt. Zweites: Bedingung/Zeitpunkt, kein Fragewort."
            },
        ],
        "mistakes": [
            "wenn statt wann in einer echten Frage: ❌ 'Wenn beginnt das Meeting?' → ✅ 'Wann beginnt das Meeting?'",
            "wann statt wenn in einem Bedingungssatz: ❌ 'Wann es regnet, bleibe ich zu Hause.' → ✅ 'Wenn es regnet, bleibe ich zu Hause.'",
            "wann in indirekter Frage mit Hauptsatz-Wortstellung: ❌ 'Er hat gefragt, wann beginnt die Prüfung.' → ✅ 'Er hat gefragt, wann die Prüfung beginnt.' (Verb ans Ende, da Nebensatz)",
        ],
        "exercise_hint": "Lückentext: wann oder wenn je nach Funktion (Frage vs. Bedingung/Zeitpunkt) einsetzen.",
    },

    {
        "id": "a2_satzzeichen",
        "title": "Satzzeichen - die wichtigsten Kommaregeln",
        "level": "A2",
        "category": "Satzkonstruktion",
        "explanation": """Deutsche Kommaregeln folgen meist der Satzstruktur, nicht dem Sprechrhythmus - anders als im Englischen.

**Komma IMMER vor einem Nebensatz** (egal ob er vor oder nach dem Hauptsatz steht):
"Ich bleibe zu Hause**,** weil es regnet." / "Weil es regnet**,** bleibe ich zu Hause."

**Komma IMMER vor Relativsätzen:**
"Das ist der Kollege**,** der mir geholfen hat."

**Komma IMMER vor 'aber' und 'sondern'** (auch zwischen zwei vollständigen Hauptsätzen):
"Ich wollte kommen**,** aber ich hatte keine Zeit."

**Komma vor 'und'/'oder' zwischen zwei vollständigen Hauptsätzen ist OPTIONAL** (seit der Rechtschreibreform von 1996), wird aber oft zur Klarheit gesetzt:
"Ich koche**,** und mein Kollege deckt den Tisch." (Komma möglich, aber nicht verpflichtend)

**KEIN Komma vor 'und'/'oder', wenn beide Verben ein gemeinsames Subjekt teilen** (nur eine Personalform, kein zweiter vollständiger Satz):
"Ich koche und decke den Tisch." (ein Subjekt "ich", zwei Verben - kein Komma)

**Komma um Infinitivgruppen mit 'zu':**
Bei Infinitivgruppen, die mit **um, ohne, (an)statt** eingeleitet werden, ist das Komma verpflichtend:
"Er kam früher, **um** die Präsentation vorzubereiten."

Bei anderen, einfachen zu-Infinitivgruppen (ohne um/ohne/(an)statt) ist das Komma seit der Reform von 1996 optional, wird aber oft zur Klarheit gesetzt:
"Er hat versucht**,** pünktlich zu kommen." (Komma hier möglich, nicht verpflichtend)""",
        "examples": [
            {
                "label": "Komma vor Nebensatz (weil)",
                "sentence": "Er kam zu spät, weil der Zug Verspätung hatte.",
                "note": "Komma trennt Hauptsatz und Nebensatz - immer verpflichtend."
            },
            {
                "label": "Komma vor Relativsatz",
                "sentence": "Das ist die E-Mail, die ich gestern geschickt habe.",
                "note": "Komma vor dem Relativpronomen - immer verpflichtend."
            },
            {
                "label": "Komma vor aber",
                "sentence": "Wir wollten früher gehen, aber das Meeting dauerte länger.",
                "note": "Vor 'aber' steht immer ein Komma, auch zwischen zwei Hauptsätzen."
            },
            {
                "label": "Kein Komma bei gemeinsamem Subjekt und 'und'",
                "sentence": "Sie liest den Bericht und schreibt eine Antwort.",
                "note": "Ein Subjekt (sie), zwei Verben - kein Komma vor 'und'."
            },
        ],
        "mistakes": [
            "Komma vor Nebensatz vergessen: ❌ 'Ich bleibe zu Hause weil es regnet.' → ✅ 'Ich bleibe zu Hause, weil es regnet.'",
            "Komma vor 'und' setzen, obwohl nur ein Subjekt vorhanden ist: ❌ 'Sie liest den Bericht, und schreibt eine Antwort.' → ✅ 'Sie liest den Bericht und schreibt eine Antwort.' (kein zweites Subjekt, kein Komma)",
            "Komma vor 'aber' vergessen: ❌ 'Ich wollte kommen aber ich hatte keine Zeit.' → ✅ 'Ich wollte kommen, aber ich hatte keine Zeit.' (aber verlangt IMMER ein Komma davor)",
        ],
        "exercise_hint": "Fehlersuche: fehlende oder falsch gesetzte Kommas in Sätzen mit Nebensätzen, Relativsätzen und aber/und identifizieren und korrigieren.",
    },

    {
        "id": "grund_praesens",
        "title": "Präsens - die Gegenwartsform bilden",
        "level": "A1",
        "category": "Verben",
        "explanation": """Das Präsens ist die Grundform des Verbs im Deutschen - man braucht sie für die Gegenwart und oft auch für die nahe Zukunft.

**Regelmäßige Endungen** (Verbstamm + Endung):

| Person | Endung | arbeiten |
|--------|--------|----------|
| ich | -e | arbeit**e** |
| du | -st | arbeit**est** |
| er/sie/es | -t | arbeit**et** |
| wir | -en | arbeit**en** |
| ihr | -t | arbeit**et** |
| sie/Sie | -en | arbeit**en** |

**Wichtige Stammveränderungen bei du/er/sie/es** (nur bei manchen starken Verben):
- **e → i:** sprechen → du **sprichst**, er **spricht**
- **e → ie:** sehen → du **siehst**, er **sieht**
- **a → ä:** fahren → du **fährst**, er **fährt**

Diese Veränderung gilt NUR für du/er/sie/es - bei ich/wir/ihr/sie bleibt der Stammvokal normal.""",
        "examples": [
            {
                "label": "Regelmäßig",
                "sentence": "Ich **arbeite** heute im Büro, mein Kollege **arbeitet** von zu Hause.",
                "note": "arbeiten: ich → -e, er → -et"
            },
            {
                "label": "e → i",
                "sentence": "Sprichst du mit dem Kunden, oder spreche ich mit ihm?",
                "note": "sprechen: du/er wechseln zu -i-, ich bleibt bei -e-"
            },
            {
                "label": "a → ä",
                "sentence": "Der Zug **fährt** um 9 Uhr, aber wir **fahren** erst um 10 Uhr los.",
                "note": "fahren: er → fährt (Umlaut), wir → fahren (kein Umlaut)"
            },
        ],
        "mistakes": [
            "Stammveränderung auch bei ich/wir/ihr anwenden: ❌ 'Ich spriche.' → ✅ 'Ich spreche.' (Wechsel nur bei du/er/sie/es)",
            "-e bei du vergessen: ❌ 'Du arbeitst.' → ✅ 'Du arbeitest.' (Verbstamm endet auf -t, deshalb -est statt -st)",
            "sein und haben unregelmäßig konjugieren wie normale Verben: ❌ 'du habst', 'er seit' → ✅ 'du hast', 'er ist' - diese zwei müssen separat auswendig gelernt werden.",
        ],
        "exercise_hint": "Lückentext: Verben im Präsens konjugieren, mit Fokus auf die du/er-Stammveränderungen. Verbliste mit Alltags- und Berufsverben (arbeiten, sprechen, helfen, nehmen, lesen, fahren, treffen).",
    },

    {
        "id": "grund_perfekt",
        "title": "Perfekt - haben oder sein, und wie man das Partizip II bildet",
        "level": "A2",
        "category": "Verben",
        "explanation": """Das Perfekt ist die wichtigste Vergangenheitsform in der gesprochenen Sprache. Man braucht zwei Teile: **haben/sein (konjugiert, Position 2) + Partizip II (am Satzende)**.

**1. haben oder sein?**
- **sein**: bei Bewegung/Ortswechsel (gehen, fahren, kommen) und Zustandswechsel (aufwachen, einschlafen, werden) - plus sein, bleiben, passieren
- **haben**: bei fast allen anderen Verben, vor allem bei Verben mit Akkusativobjekt

**2. Partizip II bilden:**
| Verbtyp | Muster | Beispiel |
|---------|--------|----------|
| schwach (regelmäßig) | ge- + Stamm + -t | machen → ge**macht** |
| stark (unregelmäßig) | ge- + Stamm(oft verändert) + -en | schreiben → ge**schrieben** |
| mit be-/er-/ver-/ent-/emp-/ge- | KEIN ge-, nur Endung | bestellen → **bestellt** (nicht 'gebestellt') |
| trennbar | ge- zwischen Präfix und Stamm | einladen → ein**ge**laden |
| auf -ieren | KEIN ge-, nur -t | organisieren → organisier**t**""",
        "examples": [
            {
                "label": "haben, schwach",
                "sentence": "Ich **habe** die E-Mail schon **beantwortet**.",
                "note": "beantworten: be- Präfix → kein ge-"
            },
            {
                "label": "sein, Bewegung",
                "sentence": "Sie **ist** gestern nach Hamburg **gefahren**.",
                "note": "fahren = Ortswechsel → sein"
            },
            {
                "label": "trennbar",
                "sentence": "Wir **haben** das Meeting kurzfristig **abgesagt**.",
                "note": "absagen: ge- kommt zwischen ab- und -sagt"
            },
        ],
        "mistakes": [
            "sein statt haben bei Verben ohne Ortswechsel: ❌ 'Ich bin gearbeitet.' → ✅ 'Ich habe gearbeitet.' (arbeiten = keine Bewegung)",
            "ge- bei be-/er-/ver-/ent-Verben ergänzen: ❌ 'Ich habe es geverstanden.' → ✅ 'Ich habe es verstanden.'",
            "ge- bei trennbaren Verben ans falsche Ende setzen: ❌ 'Ich habe gestattgefunden.' → ✅ 'Ich habe stattgefunden.' wird 'es hat stattgefunden' (ge- zwischen Präfix und Stamm: statt**ge**funden)",
        ],
        "exercise_hint": "Sätze im Präsens in Perfekt umwandeln, mit gemischten Verbtypen (schwach, stark, be-/ver-, trennbar). Separate Runde nur zur haben/sein-Entscheidung.",
    },

    {
        "id": "b2_subjektive_modalverben",
        "title": "Subjektive Modalverben - Vermutungen und Behauptungen wiedergeben",
        "level": "B2",
        "category": "Verben",
        "explanation": """Modalverben haben neben der bekannten (objektiven) Bedeutung - können = Fähigkeit, müssen = Notwendigkeit - eine zweite, **subjektive** Bedeutung: der Sprecher drückt aus, wie sicher er sich über etwas ist, oder gibt wieder, was jemand anderes behauptet.

**Vermutungen (Gegenwart):**
| Modalverb | Sicherheit | Beispiel |
|-----------|-----------|----------|
| **muss** | fast sicher | Er **muss** im Büro sein. (Licht ist an) |
| **dürfte** | wahrscheinlich | Sie **dürfte** die Unterlagen schon haben. |
| **kann/könnte** | möglich | Das **könnte** stimmen. |
| **kann nicht** | fast ausgeschlossen | Das **kann nicht** richtig sein. |

**Vermutungen (Vergangenheit):** Modalverb (Präsens) + Partizip II + haben/sein
"Er **muss** das Meeting **verpasst haben**." (= vermutlich hat er es verpasst)

**Wiedergabe fremder Behauptungen (sollen und wollen):**
- **sollen**: gibt wieder, was ANDERE über die Person sagen (der Sprecher übernimmt keine Verantwortung dafür)
  "Die neue Kollegin **soll** sehr kompetent sein." (= man sagt/es heißt, dass sie kompetent ist)
- **wollen**: gibt wieder, was die Person SELBST über sich behauptet (oft mit Zweifel des Sprechers)
  "Er **will** von dem Fehler nichts gewusst haben." (= er behauptet das, aber ob es stimmt, ist fraglich)""",
        "examples": [
            {
                "label": "müssen, Vermutung Gegenwart",
                "sentence": "Das Licht brennt noch - der Chef **muss** noch im Haus sein.",
                "note": "muss (subjektiv) = fast sichere Vermutung, nicht Notwendigkeit"
            },
            {
                "label": "müssen, Vermutung Vergangenheit",
                "sentence": "Die Zahlen stimmen nicht - jemand **muss** sich **verrechnet haben**.",
                "note": "Modalverb + Partizip II + haben (Vermutung über die Vergangenheit)"
            },
            {
                "label": "sollen, fremde Behauptung",
                "sentence": "Das neue System **soll** die Fehlerquote deutlich gesenkt haben.",
                "note": "sollen = das wird berichtet, der Sprecher bestätigt es nicht selbst"
            },
            {
                "label": "wollen, Selbstaussage mit Zweifel",
                "sentence": "Der Kollege **will** die E-Mail nie erhalten haben.",
                "note": "wollen = er behauptet es selbst, Zweifel mitschwingend"
            },
        ],
        "mistakes": [
            "sollen und müssen verwechseln: ❌ 'Er muss reich sein' für eine fremde, ungeprüfte Behauptung → ✅ 'Er soll reich sein' (sollen = man sagt es, nicht sicher bestätigt)",
            "Vermutung über die Vergangenheit ohne Partizip II bilden: ❌ 'Er muss es gewusst.' → ✅ 'Er muss es gewusst haben.'",
            "wollen (subjektiv) mit dem normalen Vollverb 'wollen' (= etwas wünschen) verwechseln: 'Er will es nicht gewusst haben' bedeutet nicht, dass er es NICHT wissen möchte, sondern dass er BEHAUPTET, es nicht gewusst zu haben.",
        ],
        "exercise_hint": "Situationen beschreiben, dann eine passende Vermutung mit müssen/dürfte/könnte formulieren. Zweite Runde: Gerüchte/Aussagen über Dritte mit sollen/wollen wiedergeben.",
    },

    {
        "id": "b2_modale_nebensaetze",
        "title": "Modale Nebensätze - Art und Weise ausdrücken (indem, dadurch dass, ohne dass)",
        "level": "B2",
        "category": "Satzkonstruktion",
        "explanation": """Um auszudrücken, WIE oder WODURCH etwas geschieht, benutzt man modale Nebensätze - nicht zu verwechseln mit Kausalsätzen (warum) oder Finalsätzen (wozu).

**indem** - drückt das Mittel/die Methode aus (wie erreicht man etwas?)
"Er hat den Fehler behoben, **indem** er den Code neu geschrieben hat."
= Die Methode war: den Code neu schreiben.

**dadurch, dass** - ähnlich wie indem, etwas formeller, betont die Ursache/das Mittel
"Wir haben Zeit gespart, **dadurch, dass** wir zwei Schritte parallel gemacht haben."

**ohne dass / ohne ... zu** - eine erwartete Begleitumstand fehlt
"Er hat gekündigt, **ohne dass** er einen neuen Job hatte." (zwei verschiedene Subjekte → ohne dass)
"Er hat gekündigt, **ohne** einen neuen Job **zu** haben." (gleiches Subjekt → ohne...zu, eleganter)

Alle drei sind Nebensätze (Kategorie C) - das Verb steht am Ende.""",
        "examples": [
            {
                "label": "indem - Methode",
                "sentence": "Sie hat das Team motiviert, **indem** sie jede Woche persönliches Feedback gegeben hat.",
                "note": "Die Methode: persönliches Feedback geben"
            },
            {
                "label": "dadurch, dass",
                "sentence": "**Dadurch, dass** wir früh angefangen haben, konnten wir die Deadline einhalten.",
                "note": "Kann auch am Satzanfang stehen, dann folgt Inversion im Hauptsatz"
            },
            {
                "label": "ohne dass",
                "sentence": "Die Änderung wurde umgesetzt, **ohne dass** die Kunden informiert wurden.",
                "note": "Zwei verschiedene Subjekte (die Änderung / die Kunden) → ohne dass, nicht ohne...zu"
            },
        ],
        "mistakes": [
            "indem mit weil verwechseln: 'indem' beantwortet WIE, nicht WARUM. ❌ 'Er ist müde, indem er lange gearbeitet hat.' → ✅ 'Er ist müde, weil er lange gearbeitet hat.'",
            "ohne...zu bei zwei verschiedenen Subjekten verwenden: ❌ 'Er ging, ohne das Licht auszuschalten.' wenn ein Dritter das Licht anlassen sollte → braucht 'ohne dass'.",
            "Verb nicht ans Ende stellen: ❌ '..., indem er hat den Code neu geschrieben.' → ✅ '..., indem er den Code neu geschrieben hat.'",
        ],
        "exercise_hint": "Zwei einfache Sätze zu einem indem-Satz kombinieren (Ziel + Methode). Kontrastübung: indem vs. weil vs. damit anhand derselben Situation.",
    },

    {
        "id": "b2_nomen_mit_praepositionen",
        "title": "Nomen mit festen Präpositionen",
        "level": "B2",
        "category": "Kasus",
        "explanation": """Wie Verben und Adjektive haben auch viele Nomen eine feste Präposition, die mitgelernt werden muss - die Präposition ergibt sich nicht aus der Bedeutung allein.

**Die wichtigsten Nomen mit fester Präposition:**

| Nomen + Präposition | Beispiel |
|---|---|
| die Freude **an** + Dat. | die Freude an der Arbeit |
| das Interesse **an/für** | das Interesse an dem Projekt |
| der Anspruch **auf** + Akk. | der Anspruch auf Urlaub |
| die Angst **vor** + Dat. | die Angst vor Fehlern |
| die Bitte **um** + Akk. | die Bitte um Feedback |
| die Verantwortung **für** + Akk. | die Verantwortung für das Team |
| die Beziehung **zu** + Dat. | die Beziehung zu den Kunden |
| der Zusammenhang **mit/zwischen** | der Zusammenhang mit den Zahlen |

Oft gehört das Nomen zu einem Verb oder Adjektiv mit derselben Präposition (sich freuen an/über → die Freude an), aber nicht immer identisch - im Zweifel das Nomen separat lernen.""",
        "examples": [
            {
                "label": "die Freude an",
                "sentence": "Er hat große Freude **an** seiner neuen Aufgabe.",
                "note": "Dativ nach 'an' hier, nicht Akkusativ"
            },
            {
                "label": "der Anspruch auf",
                "sentence": "Jeder Mitarbeiter hat Anspruch **auf** 30 Tage Urlaub.",
                "note": "Akkusativ nach 'auf'"
            },
            {
                "label": "die Verantwortung für",
                "sentence": "Sie trägt die Verantwortung **für** das gesamte Projekt.",
                "note": "immer für + Akkusativ, nicht 'über'"
            },
        ],
        "mistakes": [
            "Präposition vom verwandten Verb falsch übertragen: 'sich interessieren FÜR' aber 'das Interesse AN' ist auch korrekt (beide möglich, nicht identisch mit jedem Verb).",
            "Verantwortung mit über statt für: ❌ 'die Verantwortung über das Team' → ✅ 'die Verantwortung für das Team'",
            "Präposition weglassen und nur den Kasus raten: ohne feste Präposition + Kasus-Kombination ist der Satz unvollständig - beides gehört fest zusammen, wie ein Paket.",
        ],
        "exercise_hint": "Lückentext: passende Präposition + Kasus zum Nomen ergänzen, Sätze aus Bewerbungs-/Berichtskontext. Kontrastpaare Nomen/Verb derselben Wortfamilie (Interesse an / sich interessieren für).",
    },

    {
        "id": "b2_vergleichssaetze",
        "title": "Vergleichssätze mit als und wie",
        "level": "B2",
        "category": "Satzkonstruktion",
        "explanation": """Um zwei Dinge oder Situationen als Nebensatz zu vergleichen, benutzt man **als** (bei Ungleichheit) oder **wie** (bei Gleichheit) - anders als bei der einfachen Adjektiv-Steigerung (komparation), hier folgt ein ganzer Nebensatz.

**als** - nach einem Komparativ, drückt Ungleichheit aus
"Es war schwieriger, **als** ich gedacht hatte."
"Das Meeting hat länger gedauert, **als** wir geplant hatten."

**wie** - nach 'so...', drückt Gleichheit aus
"Es ist genau so gelaufen, **wie** ich es erwartet hatte."
"Sie arbeitet so gründlich, **wie** man es von ihr erwartet."

Beide sind Nebensätze (Kategorie C) - das Verb steht am Ende. Häufig steht im Nebensatz ein Plusquamperfekt oder Konjunktiv II, weil der Vergleichspunkt oft in der Vergangenheit liegt oder hypothetisch ist.""",
        "examples": [
            {
                "label": "als - Ungleichheit",
                "sentence": "Das Projekt hat mehr Zeit gekostet, **als** wir ursprünglich kalkuliert hatten.",
                "note": "Komparativ (mehr) + als, Verb am Ende"
            },
            {
                "label": "wie - Gleichheit",
                "sentence": "Die Präsentation lief genau so gut, **wie** wir es geübt hatten.",
                "note": "so + Adjektiv + wie, Verb am Ende"
            },
            {
                "label": "hypothetischer Vergleich",
                "sentence": "Er reagierte, **als ob** nichts passiert wäre.",
                "note": "als ob + Konjunktiv II (eigene, verwandte Regel: irrealer Vergleich)"
            },
        ],
        "mistakes": [
            "wie statt als nach Komparativ: ❌ 'schwieriger, wie ich dachte' (umgangssprachlich) → ✅ 'schwieriger, als ich dachte'",
            "Verb nicht ans Ende des Vergleichssatzes stellen: ❌ '..., als wir hatten geplant.' → ✅ '..., als wir geplant hatten.'",
            "als/wie mit als ob verwechseln: 'als ob' braucht Konjunktiv II und drückt etwas Irreales/Angenommenes aus, einfaches 'als'/'wie' vergleicht reale Fakten.",
        ],
        "exercise_hint": "Zwei Aussagen (Erwartung vs. Realität) zu einem als/wie-Satz kombinieren. Kontext: Projektnachbesprechungen, Erwartung vs. Ergebnis.",
    },

    {
        "id": "b2_relativsaetze_wer_wen_wem",
        "title": "Relativsätze mit wer, wen, wem (freie Relativsätze)",
        "level": "B2",
        "category": "Satzkonstruktion",
        "explanation": """Anders als normale Relativsätze (b1_relativsaetze) beziehen sich freie Relativsätze mit **wer/wen/wem/wessen** auf KEIN konkretes Nomen - sie bedeuten "die Person, die..." / "derjenige, der...".

**wer** (Nominativ): "**Wer** zu spät kommt, verpasst den Anfang." (= Derjenige, der zu spät kommt, ...)
**wen** (Akkusativ): "**Wen** man einmal enttäuscht, gewinnt man schwer zurück."
**wem** (Dativ): "**Wem** man vertraut, dem gibt man auch Verantwortung."
**wessen** (Genitiv, selten): "**Wessen** Idee überzeugt, der bekommt das Budget."

**Wichtig - der Hauptsatz braucht oft ein Korrelat** (der/den/dem), besonders wenn der Kasus im Hauptsatz anders ist als im Relativsatz:
"**Wer** pünktlich ist, **den** respektiert man." (wer = Nom. im Relativsatz, den = Akk. im Hauptsatz - beide Kasus nötig, weil unterschiedlich)
"**Wer** pünktlich ist, **wird** respektiert." (kein Korrelat nötig, wenn beide Sätze denselben Kasus/dieselbe Rolle hätten oder Passiv genutzt wird)""",
        "examples": [
            {
                "label": "wer, gleicher Kasus",
                "sentence": "**Wer** Fragen hat, kann sich gerne melden.",
                "note": "wer = Subjekt in beiden Sätzen, kein Korrelat nötig"
            },
            {
                "label": "wer + Korrelat bei unterschiedlichem Kasus",
                "sentence": "**Wer** zu spät kommt, **den** lassen wir nicht mehr rein.",
                "note": "wer (Nom.) im Relativsatz, den (Akk.) im Hauptsatz - beide nötig"
            },
            {
                "label": "wem",
                "sentence": "**Wem** die Entscheidung nicht gefällt, kann Einspruch einlegen.",
                "note": "wem (Dativ, gefallen verlangt Dativ)"
            },
        ],
        "mistakes": [
            "wer mit der/die/das (normalem Relativpronomen) verwechseln: freie Relativsätze mit wer beziehen sich auf keine konkrete, vorher genannte Person - 'wer' selbst bedeutet schon 'die Person, die'.",
            "Korrelat vergessen bei unterschiedlichem Kasus: ❌ 'Wer zu spät kommt, lassen wir nicht mehr rein.' → ✅ 'Wer zu spät kommt, den lassen wir nicht mehr rein.' (lassen braucht Akkusativobjekt)",
            "wen/wem verwechseln: wen = Akkusativ (wen fragt man?), wem = Dativ (wem hilft man?) - denselben Test wie bei normalen Fragewörtern anwenden.",
        ],
        "exercise_hint": "Sprichwörter und Regeln mit wer/wen/wem vervollständigen (viele feste Redewendungen nutzen genau diese Struktur). Korrelat-Erkennung: wann ist der/den/dem im Hauptsatz nötig?",
    },

    {
        "id": "c1_adjektivdeklination_indefinit",
        "title": "Adjektivdeklination nach indefiniten Artikelwörtern (jeder, manche, welche, einige)",
        "level": "C1",
        "category": "Kasus",
        "explanation": """Wörter wie jeder, mancher, solcher, welcher, sämtliche, einige, mehrere, viele, wenige stehen oft vor einem Adjektiv + Nomen - und sie verhalten sich nicht alle gleich. Das ist eine eigene Feinheit, zusätzlich zu den drei Grundmustern (bestimmt/unbestimmt/ohne Artikel).

**Wie der bestimmte Artikel** (der-Wörter, Singular): jeder, jede, jedes, jeder (Dat.), dieser, solcher, mancher, welcher
→ Adjektiv bekommt dieselbe Endung wie nach der/die/das
"**jeder neue** Kollege" (wie "der neue Kollege")

**Im Plural uneinheitlich:**
- **alle, beide, sämtliche** + Adjektiv auf **-en** (wie nach 'die'): "alle neu**en** Kollegen"
- **einige, mehrere, viele, wenige** (ohne Artikelfunktion, eher wie Zahlwörter) + Adjektiv oft auf **-e/-en** parallel zur Nullartikel-Deklination: "einige neu**e** Kollegen" (Nom./Akk.), aber "mit einigen neu**en** Kollegen" (Dat.)""",
        "examples": [
            {
                "label": "jeder - wie bestimmter Artikel",
                "sentence": "**Jeder** neu**e** Mitarbeiter bekommt eine Einführung.",
                "note": "jeder verhält sich wie 'der' → Adjektiv -e (Nominativ)"
            },
            {
                "label": "alle - Plural wie 'die'",
                "sentence": "**Alle** wichtig**en** Unterlagen liegen bereit.",
                "note": "alle + Adjektiv -en, parallel zu 'die wichtigen Unterlagen'"
            },
            {
                "label": "einige - Nullartikel-Muster",
                "sentence": "**Einige** erfahren**e** Kolleginnen haben das Projekt übernommen.",
                "note": "einige (Nom.) + Adjektiv -e, wie ohne Artikel"
            },
        ],
        "mistakes": [
            "jeder/manche im Plural wie Singular behandeln: 'jeder' hat keinen Plural (dafür 'alle') - ❌ 'jede neuen Kollegen' → ✅ 'alle neuen Kollegen'.",
            "einige/mehrere/viele im Dativ ohne -en: ❌ 'mit einigen neue Kollegen' → ✅ 'mit einigen neuen Kollegen' (im Dativ Plural immer -en, unabhängig vom Artikelwort davor)",
            "alle/beide/sämtliche mit dem Nullartikel-Muster statt dem bestimmten Muster deklinieren: diese drei verhalten sich wie 'die', nicht wie 'einige'.",
        ],
        "exercise_hint": "Sortierübung: Artikelwörter in die zwei Gruppen (der-Wort-Muster vs. Nullartikel-Muster) einordnen, dann Lückentext mit Adjektivendungen dazu.",
    },

    {
        "id": "c1_modalitaetsverben",
        "title": "Modalitätsverben - Alternativen zu den klassischen Modalverben",
        "level": "C1",
        "category": "Verben",
        "explanation": """Neben den bekannten Modalverben (müssen, können, sollen...) gibt es Verb+zu-Infinitiv-Konstruktionen, die eine ähnliche modale Bedeutung ausdrücken, aber formeller/schriftsprachlicher klingen - typisch für C1-Texte, Berichte und offizielle Kommunikation.

| Konstruktion | Bedeutung | Beispiel |
|---|---|---|
| **haben ... zu** + Inf. | müssen (aktiv) | Sie **haben** den Bericht bis Freitag **abzugeben**. |
| **es gilt ... zu** + Inf. | man muss/sollte | **Es gilt**, die Frist einzuhalten. |
| **scheinen ... zu** + Inf. | vermutlich (Anschein) | Das Problem **scheint** gelöst **zu** sein. |
| **pflegen ... zu** + Inf. | gewöhnlich tun | Er **pflegt**, montags früh anzufangen. |
| **drohen ... zu** + Inf. | negative Erwartung | Das Projekt **droht** zu scheitern. |
| **versprechen ... zu** + Inf. | positive Erwartung | Die Zahlen **versprechen**, gut auszufallen. |

Anders als 'sein...zu' (Passiv-Ersatzform, das Subjekt ist der Betroffene) ist 'haben...zu' aktivisch - das Subjekt handelt selbst.""",
        "examples": [
            {
                "label": "haben...zu (aktiv, = müssen)",
                "sentence": "Die Abteilungsleiter **haben** ihre Berichte monatlich **einzureichen**.",
                "note": "= Die Abteilungsleiter müssen ihre Berichte einreichen. Aktivisch, nicht Passiv."
            },
            {
                "label": "scheinen...zu (Vermutung)",
                "sentence": "Der Kunde **scheint** mit der Lösung zufrieden **zu** sein.",
                "note": "= Es sieht so aus, als wäre der Kunde zufrieden - Vermutung aufgrund von Anzeichen"
            },
            {
                "label": "drohen...zu (negative Erwartung)",
                "sentence": "Ohne zusätzliche Ressourcen **droht** die Deadline zu **reißen**.",
                "note": "drückt eine befürchtete, negative Entwicklung aus"
            },
        ],
        "mistakes": [
            "haben...zu mit sein...zu verwechseln: 'haben...zu' ist aktiv (das Subjekt muss handeln), 'sein...zu' ist eine Passiv-Ersatzform (das Subjekt wird betroffen) - ❌ 'Der Bericht hat abzugeben.' → ✅ 'Der Bericht ist abzugeben.' oder 'Wir haben den Bericht abzugeben.'",
            "zu vor dem Infinitiv vergessen: ❌ 'Das Projekt droht scheitern.' → ✅ 'Das Projekt droht zu scheitern.'",
            "scheinen...zu für eine sichere Tatsache statt eine Vermutung benutzen: 'scheinen' drückt immer einen Anschein aus, keine bestätigte Tatsache.",
        ],
        "exercise_hint": "Sätze mit müssen/vermutlich/gewöhnlich umformulieren mit der passenden Modalitätsverb-Konstruktion. Kontrastpaar haben...zu vs. sein...zu an denselben Sätzen üben.",
    },

    {
        "id": "c1_infinitiv_zeitverhaeltnis",
        "title": "Infinitiv mit zu - Gleichzeitigkeit und Vorzeitigkeit",
        "level": "C1",
        "category": "Verbformen",
        "explanation": """Ein Infinitiv mit zu kann zwei verschiedene Zeitverhältnisse zum übergeordneten Satz ausdrücken - das erkennt man an der Form des Infinitivs.

**Gleichzeitigkeit** (die Handlung passiert zur selben Zeit): einfacher Infinitiv
"Er behauptet, die Wahrheit **zu sagen**." (= er sagt gerade jetzt die Wahrheit)

**Vorzeitigkeit** (die Handlung ist schon vorbei, bevor die Hauptsatz-Handlung beginnt): Infinitiv Perfekt (**zu + Partizip II + haben/sein**)
"Er behauptet, die Wahrheit **gesagt zu haben**." (= er sagt jetzt, dass er FRÜHER die Wahrheit gesagt hat)

Das gilt genauso im Passiv:
"Die Unterlagen scheinen **bearbeitet worden zu sein**." (Vorzeitigkeit + Passiv)""",
        "examples": [
            {
                "label": "Gleichzeitigkeit",
                "sentence": "Sie scheint das Problem **zu verstehen**.",
                "note": "Sie versteht es gerade jetzt - einfacher Infinitiv"
            },
            {
                "label": "Vorzeitigkeit",
                "sentence": "Sie scheint das Problem bereits **verstanden zu haben**.",
                "note": "Sie hat es VOR dem Zeitpunkt des Hauptsatzes verstanden - Infinitiv Perfekt"
            },
            {
                "label": "Vorzeitigkeit im Passiv",
                "sentence": "Der Vertrag scheint schon **unterschrieben worden zu sein**.",
                "note": "Passiv + Vorzeitigkeit: Partizip II + worden + zu sein"
            },
        ],
        "mistakes": [
            "Vorzeitigkeit nicht markieren, obwohl die Handlung klar vorher passiert ist: ❌ 'Er behauptet, es zu wissen.' wenn er es schon vor langer Zeit erfahren hat und jetzt nur noch darüber spricht → ✅ 'Er behauptet, es gewusst zu haben.' (je nach gemeintem Zeitpunkt)",
            "haben/sein bei der Vorzeitigkeit vergessen: ❌ 'zu gesagt' → ✅ 'gesagt zu haben'",
            "worden im Passiv-Vorzeitigkeits-Infinitiv weglassen: ❌ 'bearbeitet zu sein' (das ist nur Zustandspassiv) → ✅ 'bearbeitet worden zu sein' für echte Vorzeitigkeit im Vorgangspassiv.",
        ],
        "exercise_hint": "Zwei Sätze (Hauptaussage + zeitlich vorherige Nebenhandlung) zu einem Infinitivsatz mit Vorzeitigkeit kombinieren. Kontrastübung Gleichzeitigkeit vs. Vorzeitigkeit an denselben Verben.",
    },

    {
        "id": "b2_es_platzhalter",
        "title": "Es als Platzhalter (Vorfeld-es und Korrelat-es)",
        "level": "B2",
        "category": "Satzkonstruktion",
        "explanation": """'Es' hat im Deutschen mehrere Funktionen - eine davon ist der reine Platzhalter, ohne eigene Bedeutung. Zwei Fälle:

**1. Vorfeld-es**: wenn ein dass-Satz, ein Infinitiv+zu oder eine indirekte Frage das eigentliche Subjekt/Objekt ist, aber nicht am Satzanfang stehen soll, springt 'es' als Platzhalter in Position 1 ein - und verschwindet, sobald etwas anderes dort steht.
"**Es** ärgert mich, dass er zu spät kommt." → "Dass er zu spät kommt, ärgert mich." (kein 'es' mehr nötig)

**2. Korrelat-es**: bei manchen Verben/Ausdrücken bleibt 'es' als feste Ankündigung stehen, auch wenn der eigentliche Inhalt (dass-Satz, Infinitiv) folgt - unabhängig von der Satzstellung:
"Ich finde **es** wichtig, dass wir pünktlich sind." (es bleibt, weil 'finden' + Adjektiv + es-Korrelat feste Konstruktion ist)""",
        "examples": [
            {
                "label": "Vorfeld-es, verschwindet",
                "sentence": "**Es** ist schwierig, diese Frage zu beantworten.",
                "note": "Ohne 'es' am Anfang: 'Diese Frage zu beantworten ist schwierig.'"
            },
            {
                "label": "Korrelat-es, bleibt immer",
                "sentence": "Ich habe **es** satt, immer dieselben Fehler zu korrigieren.",
                "note": "'es satt haben' braucht das Korrelat-es immer, egal wo der Infinitiv steht"
            },
            {
                "label": "indirekte Frage",
                "sentence": "**Es** ist noch unklar, ob das Projekt genehmigt wird.",
                "note": "Platzhalter für die indirekte Frage 'ob das Projekt genehmigt wird'"
            },
        ],
        "mistakes": [
            "Vorfeld-es stehen lassen, wenn schon etwas anderes in Position 1 steht: ❌ 'Dass er zu spät kommt, es ärgert mich.' → ✅ 'Dass er zu spät kommt, ärgert mich.'",
            "Korrelat-es weglassen bei festen Ausdrücken: ❌ 'Ich finde wichtig, dass...' → ✅ 'Ich finde es wichtig, dass...' (bei 'finden + Adjektiv' ist das Korrelat obligatorisch)",
            "es doppelt setzen: nur eine der beiden Funktionen gleichzeitig, nie 'es' am Anfang UND als Korrelat im selben Satz.",
        ],
        "exercise_hint": "Sätze umstellen (dass-Satz/Infinitiv an den Anfang) und prüfen, ob 'es' verschwindet oder bleibt - Kontrastpaare mit Vorfeld-es vs. festen Korrelat-Ausdrücken (es satt haben, es gut meinen, es sich überlegen).",
    },

    {
        "id": "c1_modales_partizip",
        "title": "Modales Partizip (Gerundiv) - zu + Partizip I als Adjektiv",
        "level": "C1",
        "category": "Verbformen",
        "explanation": """Eine sehr knappe, formelle Konstruktion für 'etwas, das getan werden muss/kann' - typisch für Berichte, Ausschreibungen und offizielle Texte. Bildung: **zu + Partizip I**, dekliniert wie ein normales Adjektiv.

**Bedeutung:** immer eine Notwendigkeit oder Möglichkeit (wie 'sein...zu' oder 'müssen/können' im Passiv), nie eine reine Beschreibung.

"die **zu lösende** Aufgabe" = die Aufgabe, die gelöst werden muss
"das **zu erwartende** Ergebnis" = das Ergebnis, das erwartet werden kann/wird
"ein **nicht zu unterschätzendes** Risiko" = ein Risiko, das man nicht unterschätzen darf""",
        "examples": [
            {
                "label": "Notwendigkeit",
                "sentence": "Die **einzureichenden** Unterlagen finden Sie im Anhang.",
                "note": "= die Unterlagen, die eingereicht werden müssen"
            },
            {
                "label": "Möglichkeit/Erwartung",
                "sentence": "Das **zu erwartende** Wachstum liegt bei drei Prozent.",
                "note": "= das Wachstum, das erwartet werden kann"
            },
            {
                "label": "mit Verneinung",
                "sentence": "Ein **nicht zu vernachlässigender** Faktor ist die Kundenzufriedenheit.",
                "note": "nicht + zu + Partizip I = etwas, das man nicht ignorieren darf"
            },
        ],
        "mistakes": [
            "Mit Partizip II statt Partizip I bilden: ❌ 'die zu gelöste Aufgabe' → ✅ 'die zu lösende Aufgabe' (immer Partizip I + Endung, nie Partizip II)",
            "Adjektivendung vergessen: ❌ 'ein zu lösend Problem' → ✅ 'ein zu lösendes Problem' (dekliniert wie jedes andere Adjektiv vor einem Nomen)",
            "Für reine Beschreibung ohne Notwendigkeit/Möglichkeit verwenden: das modale Partizip funktioniert nur bei Verben, die sinnvoll mit 'müssen/können + Passiv' umschrieben werden können.",
        ],
        "exercise_hint": "sein...zu-Sätze (schon bekannt) in das modale Partizip umformen und umgekehrt - zeigt, dass beide dieselbe Bedeutung haben, nur unterschiedlich knapp. Quelle: offizielle/formelle Beispieltexte (Ausschreibungen, Berichte).",
    },

    {
        "id": "c1_satzstellung_vorfeld_verb",
        "title": "Besonderheiten der Satzstellung - Infinitiv/Partizip II im Vorfeld (Position 1)",
        "level": "C1",
        "category": "Satzkonstruktion",
        "explanation": """Normalerweise steht in Position 1 (Vorfeld) ein Satzglied wie Subjekt, Objekt oder eine Angabe. Auf C1-Niveau, vor allem in wissenschaftlichen/argumentativen Texten und in gesprochener Sprache zur Betonung, kann auch ein Teil des Prädikats (Infinitiv oder Partizip II) dort stehen - der Rest des Verbs (das konjugierte Hilfs-/Modalverb) bleibt an Position 2.

**Funktion:** starke Fokussierung/Kontrastierung auf die Handlung selbst, oft mit einer Einschränkung danach.

"**Kommen** wird er sicher, aber pünktlich wird er nicht sein." (Fokus auf 'kommen', Kontrast zu 'pünktlich sein')
"**Gelesen** habe ich das Buch, aber verstanden habe ich es nicht wirklich." (Fokus/Kontrast zwischen zwei Handlungen)""",
        "examples": [
            {
                "label": "Infinitiv im Vorfeld",
                "sentence": "**Zustimmen** wird der Vorstand dem Vorschlag kaum.",
                "note": "Fokus auf 'zustimmen' - das konjugierte 'wird' bleibt Position 2"
            },
            {
                "label": "Partizip II im Vorfeld",
                "sentence": "**Geplant** war das Projekt anders, **umgesetzt** wurde es dann ganz neu.",
                "note": "Doppelter Kontrast zwischen zwei Partizipien im Vorfeld"
            },
        ],
        "mistakes": [
            "Konjugiertes Verb mit ins Vorfeld ziehen: ❌ 'Wird kommen er sicher.' → ✅ 'Kommen wird er sicher.' (nur der infinite Teil wandert, das konjugierte Verb bleibt an Position 2)",
            "Diese Struktur ohne Kontrast/Fokus-Funktion verwenden: sie klingt nur dann natürlich, wenn wirklich eine Betonung oder ein Gegensatz gemeint ist, nicht als Standard-Wortstellung.",
        ],
        "exercise_hint": "Neutrale Sätze in die fokussierte Vorfeld-Struktur umformen, jeweils mit einem passenden Kontrastsatz danach - zeigt den kommunikativen Zweck, nicht nur die Form.",
    },

    {
        "id": "c1_ausklammerung",
        "title": "Ausklammerung - Elemente nach dem Satzende stellen",
        "level": "C1",
        "category": "Satzkonstruktion",
        "explanation": """Normalerweise steht das Prädikat (Partizip II, Infinitiv, trennbares Präfix) ganz am Ende des Satzes, mit allem anderen davor (im 'Satzklammer'-Feld). Bei der Ausklammerung wird ein Element bewusst NACH diesem Satzende gestellt - meist Vergleiche, Präpositionalphrasen oder Nachträge, aus Gründen der Verständlichkeit oder Betonung.

**Typische ausgeklammerte Elemente:** Vergleiche mit als/wie, lange Präpositionalphrasen, nachgestellte Erklärungen.

"Er hat schneller reagiert, **als wir erwartet hatten**." (Vergleich nach dem Satzende ausgeklammert, statt 'Er hat, als wir erwartet hatten, schneller reagiert.')
"Sie hat das Angebot abgelehnt, **aus Gründen, die sie nicht nannte**." (Nachtrag ausgeklammert, für bessere Lesbarkeit)

**Warum:** ein sehr langes Element VOR dem Satzende zu stellen würde das Verb zu weit vom restlichen Satz trennen - Ausklammerung hält den Satz verständlich.""",
        "examples": [
            {
                "label": "Vergleich ausgeklammert",
                "sentence": "Das Projekt hat länger gedauert, **als ursprünglich geplant war**.",
                "note": "Ohne Ausklammerung wäre der Satz mit allem vor dem Verb kaum lesbar"
            },
            {
                "label": "Präpositionalphrase ausgeklammert",
                "sentence": "Wir haben das Ziel erreicht, **trotz erheblicher Widerstände im Team**.",
                "note": "Nachgestellt für Betonung und Lesbarkeit"
            },
        ],
        "mistakes": [
            "Jedes lange Element automatisch ausklammern: Ausklammerung ist eine bewusste stilistische Wahl für bestimmte Elementtypen (Vergleiche, Nachträge), nicht eine generelle Lizenz, beliebig etwas ans Ende zu hängen.",
            "Kernelemente des Satzes (Objekte, notwendige Ergänzungen) ausklammern: nur Zusätzliches/Erklärendes gehört ausgeklammert, keine für den Satz notwendigen Teile.",
        ],
        "exercise_hint": "Sehr lange, schwer lesbare Sätze (alles vor dem Verb) analysieren und durch Ausklammerung des Vergleichs/Nachtrags verbessern - direkter Vorher-Nachher-Kontrast zeigt den Lesbarkeitsgewinn.",
    },

    {
        "id": "b1_vermutungen_futur1",
        "title": "Vermutungen mit Futur I (werden + Infinitiv)",
        "level": "B1",
        "category": "Verbformen",
        "explanation": """Futur I (werden + Infinitiv) wird nicht nur für die Zukunft benutzt, sondern auch, um eine **Vermutung über die Gegenwart** auszudrücken - oft zusammen mit 'wohl', 'sicher' oder 'wahrscheinlich'.

**Unterschied zur echten Zukunft:** der Kontext (oft ein Zeitbezug zur Gegenwart, kein Zukunfts-Zeitwort) zeigt, dass es sich um eine Einschätzung des JETZT handelt, nicht um etwas, das erst noch passiert.

"Er **wird** wohl noch im Büro **sein**." (= vermutlich ist er gerade jetzt im Büro, nicht: er wird es später sein)
"Sie **werden** das schon **wissen**." (= ich nehme an, sie wissen es bereits)""",
        "examples": [
            {
                "label": "Vermutung über die Gegenwart",
                "sentence": "Das **wird** wohl der Grund für die Verzögerung **sein**.",
                "note": "Keine Zukunft gemeint - eine Einschätzung der aktuellen Situation"
            },
            {
                "label": "mit sicher",
                "sentence": "Sie **wird** sicher schon informiert **worden sein**.",
                "note": "Futur I mit Vorzeitigkeit (Perfekt-Infinitiv) - Vermutung über etwas, das bereits geschehen ist"
            },
        ],
        "mistakes": [
            "Mit echter Zukunft verwechseln: nur der Kontext (kein Zukunfts-Zeitwort, oft 'wohl'/'sicher'/'wahrscheinlich') zeigt, dass eine Vermutung über JETZT gemeint ist, nicht ein späteres Ereignis.",
            "wohl/sicher/wahrscheinlich weglassen, obwohl der Satz sonst wie eine echte Zukunftsaussage klingt - diese Wörter signalisieren dem Hörer, dass es sich um eine Einschätzung handelt.",
            "Mit den subjektiven Modalverben (müssen/dürfte/können) verwechseln: beide drücken Vermutung aus, aber Futur I braucht immer 'werden', die Modalverb-Variante nie.",
        ],
        "exercise_hint": "Situationen beschreiben, dann eine Vermutung sowohl mit Futur I (werden + wohl/sicher) als auch mit dem subjektiven Modalverb (müssen/dürfte) formulieren - zeigt, dass beide Wege zum selben Zweck führen.",
    },
]
