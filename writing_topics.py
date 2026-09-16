# writing_topics.py
# Level-tagged writing tasks, A1-C1. B1-C1 entries grounded in real Telc B1/B2/C1 exam
# formats (see WRITING_TASKS entries for format notes); A1-A2 entries are simple everyday
# tasks appropriate to those levels (postcards, short notes, basic forms).

WRITING_TASKS = [
    # --- A1 ---
    {"level": "A1", "type": "Postkarte", "prompt": "Schreib eine Postkarte an einen Freund/eine Freundin über deinen Urlaub. Wo bist du? Wie ist das Wetter? Was machst du dort?"},
    {"level": "A1", "type": "Kurze Vorstellung", "prompt": "Stell dich kurz vor: Name, Alter, Wohnort, Beruf/Studium, Hobbys. 4-5 Sätze."},
    {"level": "A1", "type": "Kurze Nachricht", "prompt": "Schreib einer Freundin/einem Freund eine kurze Nachricht: Du kannst heute nicht zum Treffen kommen. Sag warum und schlag einen neuen Tag vor."},
    {"level": "A1", "type": "Einfaches Formular", "prompt": "Fülle ein einfaches Anmeldeformular für einen Deutschkurs aus: Name, Adresse, Geburtsdatum, Grund für den Kurs (2-3 Sätze)."},
    {"level": "A1", "type": "Familie beschreiben", "prompt": "Beschreib deine Familie in 4-5 Sätzen: Wer gehört dazu, was machen sie beruflich, wo wohnen sie?"},

    # --- A2 ---
    {"level": "A2", "type": "Informelle Nachricht", "prompt": "Schreib einem Nachbarn eine Nachricht und frag, ob er dir am Wochenende beim Umzug helfen kann."},
    {"level": "A2", "type": "Tagesablauf", "prompt": "Beschreib deinen typischen Tagesablauf unter der Woche, von morgens bis abends."},
    {"level": "A2", "type": "Einfache Beschwerde", "prompt": "Du hast im Restaurant das falsche Essen bekommen. Schreib eine kurze, höfliche Beschwerde-Nachricht an den Kellner/die Kellnerin."},
    {"level": "A2", "type": "Einladung", "prompt": "Lade einen Freund/eine Freundin zu deiner Geburtstagsfeier ein: wann, wo, was mitbringen."},
    {"level": "A2", "type": "Wochenendbericht", "prompt": "Erzähl einer Freundin/einem Freund, was du letztes Wochenende gemacht hast (4-6 Sätze)."},

    # --- B1 ---
    {"level": "B1", "type": "Informelle Nachricht", "prompt": "Schreib einer Freundin/einem Freund, dass du ein Vorstellungsgespräch hattest, und erzähl kurz, wie es gelaufen ist."},
    {"level": "B1", "type": "Informelle Nachricht", "prompt": "Sag einem Kollegen kurzfristig ab, dass du heute Abend nicht zum Treffen kommen kannst, und schlag einen Ersatztermin vor."},
    {"level": "B1", "type": "Informelle Nachricht", "prompt": "Frag einen Freund, ob er dir einen guten Zahnarzt in Berlin empfehlen kann."},
    {"level": "B1", "type": "Informelle Nachricht", "prompt": "Bedanke dich bei einem Kollegen, der dir bei einem schwierigen Umzug/Behördengang geholfen hat."},
    {"level": "B1", "type": "Formeller Brief (Telc-Stil)", "prompt": "Sie möchten sich bei einer Sprachschule nach Kursangeboten, Preisen und Öffnungszeiten erkundigen (Bitte um Informationen)."},
    {"level": "B1", "type": "Formeller Brief (Telc-Stil)", "prompt": "Sie möchten sich bei der Stadtverwaltung nach dem Ablauf einer Ummeldung erkundigen (Bitte um Informationen)."},

    # --- B2 ---
    {"level": "B2", "type": "Formeller Brief (Telc-Stil)", "prompt": "Sie haben online ein Elektrogerät bestellt, das defekt ankam. Schreiben Sie eine Beschwerde an den Kundenservice."},
    {"level": "B2", "type": "Formeller Brief (Telc-Stil)", "prompt": "Ihre Heizung ist seit Wochen defekt, trotz mehrfacher Anfragen an die Hausverwaltung. Schreiben Sie eine Beschwerde."},
    {"level": "B2", "type": "Formeller Brief (Telc-Stil)", "prompt": "Ein gebuchtes Hotelzimmer entsprach nicht der Beschreibung auf der Buchungsseite. Schreiben Sie eine Beschwerde an das Hotel."},
    {"level": "B2", "type": "Geschäftliche E-Mail", "prompt": "Ein wichtiger Kunde hat seine Lieferung nicht rechtzeitig erhalten. Schreiben Sie eine E-Mail mit Entschuldigung und Lösungsvorschlag."},
    {"level": "B2", "type": "Geschäftliche E-Mail", "prompt": "Sie müssen einen Termin mit einem Kunden verschieben und schlagen einen neuen Termin vor."},
    {"level": "B2", "type": "Geschäftliche E-Mail", "prompt": "Ein Kollege aus einer anderen Abteilung braucht Informationen für einen Bericht - schreiben Sie eine E-Mail mit den wichtigsten Eckdaten."},
    {"level": "B2", "type": "Geschäftliche E-Mail", "prompt": "Sie laden ein Projektteam zu einem Kickoff-Meeting ein und nennen die wichtigsten Agenda-Punkte."},

    # --- C1 ---
    {"level": "C1", "type": "Geschäftliche E-Mail", "prompt": "Sie müssen einem Kunden eine Preiserhöhung mitteilen und diese sachlich begründen."},
    {"level": "C1", "type": "Geschäftliche E-Mail", "prompt": "Ein Kunde hat sich über die Qualität einer Beratungsleistung beschwert - antworten Sie professionell und lösungsorientiert."},
    {"level": "C1", "type": "Kurzbericht / Protokoll", "prompt": "Fassen Sie die Ergebnisse eines Strategie-Meetings zusammen (Entscheidungen, nächste Schritte, Verantwortlichkeiten)."},
    {"level": "C1", "type": "Kurzbericht / Protokoll", "prompt": "Fassen Sie den Fortschritt eines Projekts für das Management in einem Kurzbericht zusammen (Status, Risiken, nächste Schritte)."},
    {"level": "C1", "type": "Kurzbericht / Protokoll", "prompt": "Dokumentieren Sie die wichtigsten Punkte einer Feedback-Runde mit dem Team nach Projektabschluss."},
    {"level": "C1", "type": "Diskussionsvorlage (Erörterung)", "prompt": "Sollte Home-Office gesetzlich zur Pflicht für Unternehmen werden, die es anbieten könnten? Nehmen Sie Stellung (350-400 Wörter, mind. ein Gegenargument einbeziehen)."},
    {"level": "C1", "type": "Diskussionsvorlage (Erörterung)", "prompt": "Ersetzt Künstliche Intelligenz in Zukunft die Arbeit von Unternehmensberatern? Nehmen Sie Stellung (350-400 Wörter, mind. ein Gegenargument einbeziehen)."},
    {"level": "C1", "type": "Diskussionsvorlage (Erörterung)", "prompt": "Sollten Bewerbungsgespräche vollständig von Algorithmen (KI) durchgeführt werden? Nehmen Sie Stellung (350-400 Wörter, mind. ein Gegenargument einbeziehen)."},
    {"level": "C1", "type": "Diskussionsvorlage (Erörterung)", "prompt": "Ist lebenslanges Lernen heute wichtiger als eine einmalige, solide Ausbildung? Nehmen Sie Stellung (350-400 Wörter, mind. ein Gegenargument einbeziehen)."},
]

LEVEL_ORDER = ["A1", "A2", "B1", "B2", "C1"]
