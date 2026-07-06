# interview_content.py
# Ported from career-ops/interview-prep/practice/*.html (index.html, general-interview-prep.html,
# skript-a-selbstvorstellung.html, skript-b-werdegang.html) - source of truth stays those files;
# this is the same content, structured for the Streamlit Interview tab.

ANCHOR = "Mich interessiert an Consulting vor allem die Schnittstelle zwischen Technologie und Menschen - dafür zu sorgen, dass Veränderung nicht nur auf dem Papier, sondern im Alltag wirklich ankommt."

SPOKES = [
    {
        "trigger": "\"Warum Consulting?\" (der Beruf allgemein)",
        "text": "Mich reizt dabei die Vielfalt an Projekten und Branchen, und dass man genau zwischen Strategie und den Menschen steht, die die Veränderung am Ende tatsächlich umsetzen müssen.",
    },
    {
        "trigger": "\"Welchen Teil von Consulting?\" (Spezialisierung)",
        "text": "Am meisten interessiert mich der Teil, der mit Change und Kommunikation zu tun hat - wie man Teams durch eine Veränderung begleitet, nicht nur das fachliche Konzept selbst.",
    },
    {
        "trigger": "\"Was möchtest du bei [Firma] tun?\" (firmenspezifisch - IMMER neu recherchieren)",
        "text": "An die eigene Sprache der Firma andocken + die Spezialisierung aus dem vorherigen Spoke. Das ist der einzige Baustein, den du vor jedem Gespräch neu recherchierst.",
    },
]

PROOFS_ON_DEMAND = [
    "Masterarbeit: emotionale Intelligenz + KI in interkulturellen Teams, veröffentlicht (GILE Journal of Skills Development, 6(1), 150-170, 2026)",
    "TACO-Retrospektiven-Format bei Accenture - konkretes Beispiel für einen sicheren Raum, in dem ein Team offen sprechen kann",
    "Interiors and Home Solutions - nur bei direkter Nachfrage zu eigenständiger Kundenverantwortung, nicht ungefragt einbauen",
]

STAR_STORIES = [
    {
        "id": "taco",
        "title": "1 - TACO-Retrospektiven-Framework",
        "best_for": "Eigeninitiative · Ownership · \"etwas verbessert, ohne gefragt zu werden\"",
        "parts": [
            ("Situation", "SAP-IDM-Transformationsprogramm bei Accenture Berlin - Retrospektiven waren unstrukturiert, wenig Beteiligung."),
            ("Aufgabe", "Ungefragt verbessern - reine Eigeninitiative."),
            ("Aktion", "Eigenes Format entwickelt (TACO: Thrive, Abandon, Changes, Ovation), auf MURAL/MIRO umgesetzt, selbst moderiert."),
            ("Ergebnis", "In 3 Programm-Retrospektiven eingesetzt, vom Programmleiter als Highlight ausgezeichnet."),
            ("Reflexion", "Die einzige Accenture-Geschichte, die wirklich \"selbst entwickelt und geleitet\" ist, nicht \"unterstützt\" - nutzen bei Fragen zu Eigeninitiative/Ownership."),
        ],
    },
    {
        "id": "kpi",
        "title": "2 - KPI-Pipeline + Power-Automate-Automatisierung",
        "best_for": "Prozessverbesserung · Automatisierung · \"Überblick über parallele Projekte\"",
        "parts": [
            ("Situation", "Zwei Workstreams im selben Programm, keine konsolidierte Sichtbarkeit für den Programmleiter, wöchentliches Feedback komplett manuell."),
            ("Aufgabe", "Reporting-Infrastruktur als Teil der Programm-Unterstützung aufbauen."),
            ("Aktion", "Jira-Board mit 15 KPIs über zwei Workstreams und Routing-Tags aufgebaut; Feedback-/Reporting-Workflow mit Power Automate und MS Forms automatisiert."),
            ("Ergebnis", "Erstmals durchgängige Pipeline-Transparenz; ca. 30% weniger Ad-hoc-Statusanfragen; ca. 2h/Woche manuelle Arbeit gespart."),
            ("Reflexion", "Sicher quantifiziert, klar \"unterstützt/aufgebaut\" - kein Überclaiming-Risiko. Standardantwort für Prozessverbesserung/Automatisierung."),
        ],
    },
    {
        "id": "p1",
        "title": "3 - P1-Bridge-Call (Whirlpool, Accenture Bangalore)",
        "best_for": "Arbeiten unter Druck · Krisenkommunikation · Stakeholder-Kommunikation unter Stress",
        "parts": [
            ("Situation", "Ein P1-Incident - höchste Schweregradstufe - bei einem Kunden erforderte einen Live-Bridge-Call mit C-Level-Stakeholdern."),
            ("Aufgabe", "Als ITSM-Koordinator den Bridge-Call bis zur Lösung unterstützen."),
            ("Aktion", "Den Bridge-Call unterstützt, Updates koordiniert, den Incident durchgängig in ServiceNow bis zum Abschluss nachverfolgt."),
            ("Ergebnis", "Incident gelöst; vom Engagement Manager und dem Senior Manager des Kunden ausdrücklich gelobt."),
            ("Reflexion", "Sprachregel: \"unterstützt\", nie \"geleitet\" oder \"moderiert\". Operative ITSM-Tiefe unter echtem Druck, keine Beratungs-Delivery-Story."),
        ],
    },
    {
        "id": "ihs",
        "title": "4 - Interiors and Home Solutions (eigenes Unternehmen)",
        "best_for": "Eigenständige Kundenbeziehung · etwas allein durchziehen · unternehmerisches Denken",
        "parts": [
            ("Situation", "Eigenes kleines Innenausbau-Unternehmen in Indien, vor dem Umzug nach Berlin."),
            ("Aufgabe", "Kundenprojekte allein akquirieren und komplett eigenverantwortlich liefern."),
            ("Aktion", "Erste Kunden über Direktansprache gewonnen, Anforderungen aufgenommen, Subunternehmer koordiniert, zwei parallele Projekte geliefert, komplette Kundenkommunikation von Erstberatung bis Abnahme."),
            ("Ergebnis", "2 Projekte geliefert, ca. 20.000 EUR Umsatz, ca. 20% Marge, pünktlich und im Budget."),
            ("Reflexion", "Die einzige echte End-to-End-Kundenverantwortungs-Story im gesamten Lebenslauf - bei Accenture war die Arbeit Analyst-Scope, nicht stakeholder-seitig."),
        ],
    },
    {
        "id": "pub",
        "title": "5 - Publikation / Masterarbeit",
        "best_for": "\"Was macht dich einzigartig / dein Superpower\" · KI-Adoption · konzeptionelle Tiefe",
        "parts": [
            ("Situation", "Forschung zu emotionaler Intelligenz, psychologischer Sicherheit und KI-Adoption in interkulturellen Beratungsteams."),
            ("Ergebnis", "Peer-reviewed veröffentlicht, GILE Journal of Skills Development, 6(1), 150-170."),
            ("Reflexion", "Seltener Differenziator für Junior-Consultants - die meisten haben entweder Praxis oder akademische Tiefe, nicht beides. Nutzen bei \"was macht dich einzigartig\" oder KI-Adoptions-Fragen."),
        ],
    },
    {
        "id": "ccv",
        "title": "6 - CCVOSSEL (26-Anwendungen-Lifecycle-Management)",
        "best_for": "Technische Tiefe · Compliance/Sicherheit · operative Sorgfalt",
        "parts": [
            ("Situation", "Bei CCVOSSEL brauchte es durchgängige Lifecycle-Verantwortung für 26 Unternehmensanwendungen, nach BMW-Sicherheitsstandards."),
            ("Aufgabe", "Lifecycle-Tracking und Dokumentation über drei Service-Domänen verantworten (Infrastruktur, Zertifikatsmanagement, Service-Identität)."),
            ("Aktion", "Jeden Change und Incident durchgängig in ServiceNow von der Meldung bis zum Abschluss nachverfolgt; Wissensdatenbank-Artikel für alle 26 Anwendungen erstellt und gepflegt."),
            ("Ergebnis", "Strukturierte First-Line-Übergaben; durchgängig aktuelle Lifecycle-Dokumentation über das gesamte Portfolio."),
            ("Reflexion", "Echte technische/Sicherheitstiefe (IAM, OIDC, Zertifikate) - nicht als Transformationserfahrung labeln. BMW nur als Standard-Referenz nennen, nicht als Kunde."),
        ],
    },
]

COMBINE_BRIDGE_STORY = {
    "title": "Bridge-Story - Interiors and Home Solutions (nur bei Immobilien-/Raumfrage, combine-spezifisch)",
    "warning": "Du hast keine direkte Corporate-Real-Estate-Erfahrung - das ist eine echte Lücke, nicht wegreden. Nur nutzen, wenn explizit danach gefragt wird.",
    "verbatim": "Ich habe keine Corporate-Real-Estate-Erfahrung, aber ich habe schon einmal ein Innenausbau-Geschäft geführt - dort war physischer Raum buchstäblich das Produkt. Was mich an combine reizt, ist trotzdem klar die kulturelle Seite, nicht die Flächenplanung.",
    "facts": "Fakten falls nachgefragt: eigenes kleines Unternehmen in Indien, zwei Kundenprojekte über Direktansprache akquiriert, Anforderungen aufgenommen, Subunternehmer koordiniert, ca. EUR 20k Umsatz, ~20% Marge, komplette Kundenkommunikation von Erstberatung bis Abnahme.",
}

CHANGE_MODELS = [
    {
        "title": "Kotter - 8 Stufen",
        "text": "Dringlichkeit -> Führungskoalition -> Vision -> Kommunikation -> Empowerment -> kurzfristige Erfolge -> Konsolidierung -> Verankerung in der Kultur.",
        "verbatim": "Die Verankerungsstufe ist die, die ich in der Praxis am meisten unterschätzt sehe - deshalb war mir bei TACO wichtig, dass es kein Einmal-Workshop bleibt, sondern über drei Retrospektiven wiederholt wird.",
    },
    {
        "title": "ADKAR (Prosci)",
        "text": "Awareness, Desire, Knowledge, Ability, Reinforcement - Modell auf Individuenebene, nicht Organisationsebene.",
        "note": "Guter Begriff, um zu zeigen, dass du zwischen System- und Personenebene unterscheidest.",
    },
    {
        "title": "Lewin - Unfreeze/Change/Refreeze",
        "text": "Das einfachste Modell, gut als Referenzpunkt, wenn nur kurz ein Name genannt werden soll.",
    },
    {
        "title": "Kübler-Ross-Veränderungskurve",
        "text": "Schock, Widerstand, Exploration, Akzeptanz - deine eigentliche Stärke, direkt verknüpfbar mit deiner Forschung zu psychologischer Sicherheit.",
        "verbatim": "Aber ehrlich, meine Stärke ist weniger das Modell selbst, sondern dass ich es schon gebaut und moderiert habe - das war mit TACO genau der Kübler-Ross-Gedanke: Menschen erst Raum geben, bevor man sie zur nächsten Phase drängt.",
    },
]

COMBINE_FACTS = [
    {
        "title": "Wie ist combine entstanden?",
        "text": "2015 aus der Fusion von Quickborner Team (QT, gegründet 1956) und macon (gegründet 1998) - daher \"60 Jahre Erfahrung\" im eigenen Marketing. ~50 Mitarbeitende aus beiden Firmen haben combine gestartet.",
    },
    {
        "title": "Größe & Struktur",
        "text": "~85-90 Mitarbeitende, 100% eigentümergeführt. Standorte München, Berlin, Düsseldorf, Hamburg. Unterzeichner der Charta der Vielfalt.",
    },
    {
        "title": "Kernfeld",
        "text": "Betrieblich genutzte Immobilie (Corporate Real Estate) - komplette Immobilienökonomie von Strategieentwicklung bis Projektmanagement. Diese Stelle ist die Change-Management-Seite davon, nicht die Flächenplanungs-Seite.",
    },
    {
        "title": "Eigene Formulierung",
        "text": "\"Raum und Kultur zusammen denken\" - combines eigene Selbstbeschreibung.",
    },
    {
        "title": "Flaggschiff-Referenz: Serviceplan",
        "text": "\"House of Communication\" München, seit 2018 begleitet, Werksviertel München, 1.700 Mitarbeitende, 40 Agenturen unter einem Dach. Change-Strategie und Roadmap gemeinsam mit Change Agents und künftigen Nutzern entwickelt, im engen Dialog statt am Reißbrett. Konzept: Activity-Based Working. New Work Award 2023 gewonnen.",
        "note": "Bester konkreter Gesprächsaufhänger - zeig, dass du das kennst, bevor sie es erwähnen.",
    },
    {
        "title": "Ihr Change-Prinzip in eigenen Worten",
        "text": "Partizipative Erarbeitung eines Nutzungskonzepts mit relevanten Stakeholdern. Sprechen explizit von \"Change Agents\" - Mitarbeitende, die den Wandel mittragen und verankern. Ziel: Akzeptanz, Identifikation, Begeisterung für New Work. Fast wortgleich mit dem TACO-Gedanken - als direkte Brücke nutzen, nicht als Zufall behandeln.",
    },
]

# (question, answer_anchor) - firm-agnostic, works for EY/OMMAX/Dreso/anyone
GENERAL_QUESTIONS = [
    ("Erzähl mir etwas über dich.", "Selbstvorstellungs-Skelett: Bausteine 1-3 + 5 fest, Baustein 4 firmenspezifisch einsetzen."),
    ("Warum Consulting?", "Anker + Spoke \"Warum Consulting?\" - Vielfalt an Projekten/Branchen, zwischen Strategie und Menschen stehen."),
    ("Welchen Teil von Consulting interessiert dich am meisten?", "Anker + Spoke \"Welchen Teil\" - Change & Kommunikation, Teams durch Veränderung begleiten."),
    ("Erzähl von einer Zeit, in der du etwas verbessert hast, ohne dass man dich darum gebeten hat.", "Story 1 - TACO, volles STAR."),
    ("Wie behältst du den Überblick bei mehreren parallelen Projekten?", "Story 2 - KPI-Pipeline."),
    ("Erzähl von einer Situation unter großem Druck.", "Story 3 - P1-Bridge-Call. Sprachregel: \"unterstützt\", nie \"geleitet\"."),
    ("Erzähl davon, wie du eigenständig eine Kundenbeziehung geführt hast.", "Story 4 - Interiors and Home Solutions."),
    ("Was macht dich einzigartig?", "Story 5 - Publikation. Praxis + akademische Tiefe zusammen ist der seltene Kombi-Vorteil."),
    ("Erzähl von technischer Tiefe oder Compliance-Arbeit.", "Story 6 - CCVOSSEL. Nicht als Transformationserfahrung labeln, BMW nur als Standard-Referenz."),
    ("Was ist deine größte Stärke?", "Offen, aber Kernkandidat: Fähigkeit zuzuhören, zu verstehen, zu unterstützen (Baustein 1) - mit TACO oder der Publikation belegen."),
    ("Wo siehst du dich in 5 Jahren?", "Baustein 5: Entwicklung Richtung Senior-Rolle im Change Management / in der Transformationsberatung."),
    ("Gehaltsvorstellung?", "\"Basierend auf der üblichen Vergütung für Junior-Consulting-Rollen in Berlin ziele ich auf 50.000-52.000 EUR. Ich bin offen, das Gesamtpaket zu besprechen.\"\nFalls unter dem Ziel angeboten: \"Ich vergleiche mit Rollen im Bereich 50.000-55.000 EUR. Angesichts meines Forschungshintergrunds und der Erfahrung bei Accenture, können wir das besprechen?\""),
    ("Wie ist dein Deutschniveau?", "Standard-Default: \"Sehr gute Kenntnisse in Wort und Schrift\" / Formular-Dropdown \"Gute Kenntnisse (mind. B2)\" - NIE ungefragt C1 behaupten. Ausnahme: combine, wo C1 bereits schriftlich zugesagt wurde - dort voll durchziehen, hier NICHT automatisch übertragen."),
    ("Wann kannst du anfangen?", "Ab sofort - keine Kündigungsfrist (Job Seeker Visa)."),
    ("Bist du reisebereit / offen für Umzug?", "Berlin bevorzugt, aber offen für Umzug innerhalb Deutschlands. Reisebereitschaft 50-75%, bereits bestätigt."),
    ("Was ist deine größte Schwäche?", "Absichtlich nicht vorgeschrieben. Echte, kalibrierte Optionen: keine formale Change-Management-Zertifizierung · bei Accenture Analyst-Scope, nicht direkt kundenseitig verantwortlich · je nach Firma ein fachliches Wissensgebiet, das dir fehlt. Wähle eine echte und formuliere sie selbst."),
]

# combine-specific pool - answers assume combine context (e.g. C1 German confirmed, München role)
COMBINE_QUESTIONS = [
    ("Erzähl von einer Situation, in der du Veränderung begleitet hast.", "Story 1 (TACO), volles STAR."),
    ("Wie gehst du vor, wenn du einen Workshop konzipierst?", "TACO-Designprozess: qualitative + quantitative Methoden, Diskussion strukturieren, Ergebnisse sichern, Entscheidungen vorbereiten."),
    ("Du arbeitest an mehreren parallelen Projekten - wie behältst du den Überblick?", "Story 2 (KPI-Pipeline)."),
    ("Warum der Wechsel von SAP/IT-Umfeld zu Corporate Real Estate?", "Raum+Kultur-Narrativ. Ehrlich benennen: keine Immobilienwirtschaft-Erfahrung, aber die New-Work-/Kultur-Seite ist der eigentliche Fit."),
    ("Dein Deutsch wirkt nicht ganz C1 - wie siehst du das?", "Nicht anbieten, nur falls direkt gefragt. Ruhig bleiben, weiter auf Deutsch antworten, keine Entschuldigung.\nVerbatim: \"Ich arbeite seit über einem Jahr komplett auf Deutsch bei Accenture Berlin und in meinem Studium - ich bin überzeugt, dass das Gespräch das am besten zeigt.\" Danach Thema wechseln zurück zur Sache."),
    ("Die Stelle ist in München, du bist in Berlin - wie stehst du dazu?", "Offen für Umzug, bereits der Recruiterin schriftlich bestätigt.\nVerbatim: \"München ist für mich kein Hindernis - ich bin flexibel und würde für die richtige Rolle umziehen. Wie strikt werden die zwei Bürotage in der Praxis gehandhabt?\" (Gegenfrage zeigt echtes Interesse.)"),
    ("Warum Junior-Rolle trotz Berufserfahrung?", "Ehrlich: erste Berufserfahrung ist in der Stellenanzeige explizit akzeptiert. Du willst dich in einem neuen Fachfeld (Corporate Real Estate/Workplace) von Grund auf einarbeiten."),
    ("Was ist deine größte Schwäche?", "Ehrlich wählen - Vorschlag: fehlende Immobilienwirtschafts-Tiefe, aktiv adressiert (z.B. kurze eigene Recherche vor dem Gespräch)."),
    ("Gehalt / Eintrittsdatum?", "Schon beantwortet: 50.000 EUR / ab sofort. Falls nachgefragt, dabei bleiben, nicht neu verhandeln im Erstgespräch."),
]

SKRIPT_A = {
    "title": "Skript A - Selbstvorstellung (Standard, combine)",
    "target_seconds": 90,
    "beats": [
        {
            "cue": "Ich bin Antony...",
            "text": "Ich bin Antony, ich komme ursprünglich aus Indien, seit drei Jahren lebe ich in Berlin. Ich glaube, eine meiner Stärken ist meine Fähigkeit, Menschen **zuzuhören**, sie zu verstehen und zu unterstützen - genau das möchte ich in mein berufliches Leben mit Kunden einbringen.",
        },
        {
            "cue": "Ich habe meinen Master...",
            "text": "Ich habe meinen Master in International Management an der Hochschule Fresenius abgeschlossen. Meine Abschlussarbeit beschäftigt sich mit emotionaler Intelligenz, psychologischer Sicherheit und KI-Tools in interkulturellen Teams - genauer, wie das die Employability von Berufseinsteigern in der Beratung stärkt. Die Arbeit ist mittlerweile in einem Fachjournal veröffentlicht.",
        },
        {
            "cue": "**Parallel dazu** habe ich bei Accenture...",
            "text": "**Parallel dazu** habe ich bei Accenture die Beratungskultur aus der Nähe beobachtet, wie Stakeholder- und Kundenkommunikation funktioniert, und wie schnell man auf die Bedürfnisse von Kunden reagieren muss - unter anderem, indem ich ein eigenes Retrospektiven-Format namens TACO entwickelt und moderiert habe.",
        },
        {
            "cue": "Was mich an combine konkret reizt...",
            "text": "Was mich an combine konkret reizt: Ich habe mir euer Serviceplan-Projekt angeschaut - wie ihr Change Agents und die künftigen Nutzer selbst in die Entwicklung der Change-Strategie eingebunden habt, statt ihnen ein fertiges Konzept vorzusetzen. Genau das ist die Seite von Transformation, die mich interessiert: nicht nur, dass sich etwas ändert, sondern dass Menschen diese Veränderung als Teil ihres eigenen Wachstums annehmen, statt sie nur zu erdulden.",
            "note": "Diese Passage ist dein Beleg für Recherche - sag den Projektnamen ruhig langsam und deutlich.",
        },
        {
            "cue": "**Genau in diese Richtung** will ich mich entwickeln...",
            "text": "**Genau in diese Richtung** will ich mich langfristig entwickeln - hin zu einer Senior-Rolle im Change Management, in der ich Unternehmen durch genau solche Transformationen begleite.",
        },
    ],
}

SKRIPT_B = {
    "title": "Skript B - Kompletter Werdegang (combine, nur auf Nachfrage)",
    "target_seconds": 120,
    "corrections": [
        {
            "wrong": "- zwei Projekte eigenverantwortlich ... geführt.",
            "right": "- dabei habe ich zwei Projekte eigenverantwortlich ... geführt.",
            "rule": "Der zweite Halbsatz nach dem Gedankenstrich hatte kein eigenes Verb. Jeder Halbsatz braucht sein \"habe\".",
        },
        {
            "wrong": "Danach bei Accenture Berlin habe ich ...",
            "right": "Danach habe ich bei Accenture Berlin ...",
            "rule": "Nur EIN Element darf vor dem konjugierten Verb stehen (Verbzweitstellung). \"Danach\" und \"bei Accenture Berlin\" waren beide vorne - das Verb muss direkt nach \"Danach\".",
        },
    ],
    "beats": [
        {
            "cue": "Ich bin Antony...",
            "text": "Ich bin Antony, ich komme ursprünglich aus Indien, seit drei Jahren lebe ich in Berlin. Ich glaube, eine meiner Stärken ist meine Fähigkeit, Menschen zuzuhören, sie zu verstehen und zu unterstützen - genau das möchte ich in mein berufliches Leben mit Kunden einbringen.",
        },
        {
            "cue": "**Angefangen hat es** bei Accenture in Bangalore...",
            "text": "**Angefangen hat es** bei Accenture in Bangalore - dort habe ich drei neue Analysten durch strukturierte Knowledge-Transfer-Sessions in ITSM-Prozesse eingearbeitet.",
        },
        {
            "cue": "**Danach** hatte ich mein eigenes Unternehmen...",
            "text": "**Danach** hatte ich mein eigenes kleines Unternehmen in Indien, Interiors and Home Solutions - ==dabei habe ich== zwei Projekte eigenverantwortlich von der Akquise bis zur Abnahme geführt. Ich habe es bewusst beendet, als klar war, dass es Zeit für meinen Weg nach Deutschland war.",
        },
        {
            "cue": "**Nach dem Umzug** habe ich meinen Master begonnen...",
            "text": "**Nach dem Umzug** habe ich meinen Master in Berlin begonnen und parallel bei CCVOSSEL den Lebenszyklus von 26 Unternehmensanwendungen gesteuert, nach BMW-Sicherheitsstandards.",
        },
        {
            "cue": "**Danach** habe ich bei Accenture Berlin...",
            "text": "**Danach habe ich** ==bei Accenture Berlin== in einem laufenden SAP-Transformationsprogramm mitgearbeitet und dort mein eigenes Retrospektiven-Format TACO entwickelt und moderiert.",
        },
        {
            "cue": "Meine Abschlussarbeit ... ist veröffentlicht...",
            "text": "Meine Abschlussarbeit zu emotionaler Intelligenz und KI-Adoption in interkulturellen Teams ist mittlerweile veröffentlicht, und aktuell beschäftige ich mich intensiv mit der Anthropic-API - ich habe drei eigene Anwendungen gebaut, die live im Einsatz sind.",
        },
        {
            "cue": "**Und jetzt** will ich das alles zusammenbringen...",
            "text": "**Und jetzt** will ich das alles zusammenbringen, bei combine, wo genau diese Verbindung aus Struktur und menschlicher Seite gefragt ist.",
        },
    ],
}
