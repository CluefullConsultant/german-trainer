# writing_topics.py
# Curated writing topics grounded in real Telc B2/C1 exam formats.
# Brief: Telc B2 gives a stimulus scenario + task (Beschwerde or Bitte um Informationen),
# 150-200 words, one point per paragraph. Business email/report/informal variants follow the same idea.
# Aufsatz: Telc C1 Erörterung format - a topic with two opposing views, 350-400 words,
# must raise and address at least one counter-argument.

BRIEF_TOPICS = {
    "Formeller Brief (Telc-Stil)": [
        "Sie haben online ein Elektrogerät bestellt, das defekt ankam. Schreiben Sie eine Beschwerde an den Kundenservice.",
        "Sie möchten sich bei einer Sprachschule nach Kursangeboten, Preisen und Öffnungszeiten erkundigen (Bitte um Informationen).",
        "Ihre Heizung ist seit Wochen defekt, trotz mehrfacher Anfragen an die Hausverwaltung. Schreiben Sie eine Beschwerde.",
        "Eine Zeitungsanzeige wirbt für einen Sprachkurs im Ausland, der die versprochenen Leistungen nicht erfüllt hat. Schreiben Sie eine Beschwerde an den Anbieter.",
        "Sie möchten sich bei der Stadtverwaltung nach dem Ablauf einer Ummeldung erkundigen (Bitte um Informationen).",
        "Ein gebuchtes Hotelzimmer entsprach nicht der Beschreibung auf der Buchungsseite. Schreiben Sie eine Beschwerde an das Hotel.",
        "Sie möchten sich bei einer Universität nach den Zulassungsvoraussetzungen für einen Masterstudiengang erkundigen.",
        "Eine bestellte Dienstleistung (z.B. Umzugsfirma) wurde nicht wie vereinbart erbracht. Schreiben Sie eine Beschwerde.",
    ],
    "Geschäftliche E-Mail": [
        "Ein wichtiger Kunde hat seine Lieferung nicht rechtzeitig erhalten. Schreiben Sie eine E-Mail mit Entschuldigung und Lösungsvorschlag.",
        "Sie müssen einen Termin mit einem Kunden verschieben und schlagen einen neuen Termin vor.",
        "Ein Kollege aus einer anderen Abteilung braucht Informationen für einen Bericht - schreiben Sie eine E-Mail mit den wichtigsten Eckdaten.",
        "Sie müssen einem Kunden eine Preiserhöhung mitteilen und diese sachlich begründen.",
        "Sie laden ein Projektteam zu einem Kickoff-Meeting ein und nennen die wichtigsten Agenda-Punkte.",
        "Ein Kunde hat sich über die Qualität einer Beratungsleistung beschwert - antworten Sie professionell und lösungsorientiert.",
        "Sie bewerben sich intern für ein neues Projekt und stellen Ihre Motivation in einer kurzen E-Mail an den Projektleiter dar.",
    ],
    "Kurzbericht / Protokoll": [
        "Fassen Sie die Ergebnisse eines Strategie-Meetings zusammen (Entscheidungen, nächste Schritte, Verantwortlichkeiten).",
        "Schreiben Sie ein Protokoll zu einem Kickoff-Meeting mit einem neuen Kunden.",
        "Fassen Sie den Fortschritt eines Projekts für das Management in einem Kurzbericht zusammen (Status, Risiken, nächste Schritte).",
        "Dokumentieren Sie die wichtigsten Punkte einer Feedback-Runde mit dem Team nach Projektabschluss.",
        "Schreiben Sie einen kurzen Bericht über die Ergebnisse einer Kundenzufriedenheitsumfrage.",
    ],
    "Informelle Nachricht": [
        "Schreib deinem Nachbarn eine Nachricht und frag, ob er dir am Wochenende beim Umzug helfen kann.",
        "Schreib einer Freundin/einem Freund, dass du ein Vorstellungsgespräch hattest, und erzähl kurz, wie es gelaufen ist.",
        "Sag einem Kollegen kurzfristig ab, dass du heute Abend nicht zum Treffen kommen kannst, und schlag einen Ersatztermin vor.",
        "Frag einen Freund, ob er dir einen guten Zahnarzt in Berlin empfehlen kann.",
        "Bedanke dich bei einem Kollegen, der dir bei einem schwierigen Umzug/Behördengang geholfen hat.",
    ],
}

AUFSATZ_TOPICS = [
    {"thema": "Sollte Home-Office gesetzlich zur Pflicht für Unternehmen werden, die es anbieten könnten?", "kontext": "beruflich"},
    {"thema": "Ersetzt Künstliche Intelligenz in Zukunft die Arbeit von Unternehmensberatern?", "kontext": "beruflich"},
    {"thema": "Ist lebenslanges Lernen heute wichtiger als eine einmalige, solide Ausbildung?", "kontext": "gesellschaftlich"},
    {"thema": "Sollten Unternehmen ihren Mitarbeitenden eine Vier-Tage-Woche bei vollem Lohnausgleich anbieten?", "kontext": "beruflich"},
    {"thema": "Ist der Umzug in eine Großstadt wie Berlin für die Karriere heute noch notwendig?", "kontext": "gesellschaftlich"},
    {"thema": "Sollten Bewerbungsgespräche vollständig von Algorithmen (KI) durchgeführt werden?", "kontext": "beruflich"},
    {"thema": "Ist Mehrsprachigkeit im Berufsleben wichtiger als fachliche Spezialisierung?", "kontext": "gesellschaftlich"},
    {"thema": "Sollte Deutschland den Quereinstieg in Führungspositionen stärker fördern?", "kontext": "beruflich"},
    {"thema": "Verlieren traditionelle Bürostrukturen durch New Work ihre Bedeutung?", "kontext": "beruflich"},
    {"thema": "Ist soziale Intelligenz wichtiger als technisches Wissen für erfolgreiche Führungskräfte?", "kontext": "beruflich"},
    {"thema": "Sollten Städte den Autoverkehr in Innenstädten vollständig verbieten?", "kontext": "gesellschaftlich"},
    {"thema": "Fördert Social Media eher den gesellschaftlichen Zusammenhalt oder die Spaltung?", "kontext": "gesellschaftlich"},
    {"thema": "Sollten Unternehmen verpflichtet werden, ihre Gehaltsstrukturen offenzulegen?", "kontext": "beruflich"},
    {"thema": "Ist Perfektionismus im Berufsleben eher hilfreich oder schädlich?", "kontext": "beruflich"},
    {"thema": "Sollte es in Deutschland ein verpflichtendes soziales Jahr für alle jungen Erwachsenen geben?", "kontext": "gesellschaftlich"},
]
