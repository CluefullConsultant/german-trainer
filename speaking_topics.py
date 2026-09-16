# speaking_topics.py
# Level-tagged conversation topics for live speaking practice with a conversation partner
# (mentor, tandem, etc.) - not an AI chat simulator. Each topic gives a subject, a few
# discussion questions, and for B1+ a short stimulus text to read and talk about together.

SPEAKING_TOPICS = [
    # --- A1 ---
    {
        "level": "A1", "topic": "Meine Familie",
        "text": None,
        "questions": [
            "Wie viele Personen sind in deiner Familie?",
            "Was machen deine Eltern beruflich?",
            "Wer in deiner Familie siehst du am meisten?",
        ],
    },
    {
        "level": "A1", "topic": "Mein Tag",
        "text": None,
        "questions": [
            "Wann stehst du normalerweise auf?",
            "Was machst du morgens, bevor du das Haus verlässt?",
            "Was ist dein Lieblingsteil des Tages?",
        ],
    },
    {
        "level": "A1", "topic": "Essen und Trinken",
        "text": None,
        "questions": [
            "Was isst du am liebsten zum Frühstück?",
            "Kochst du gern? Was kochst du oft?",
            "Gibt es ein Essen, das du gar nicht magst?",
        ],
    },
    {
        "level": "A1", "topic": "Hobbys",
        "text": None,
        "questions": [
            "Was machst du gern in deiner Freizeit?",
            "Seit wann machst du dieses Hobby?",
            "Machst du das lieber allein oder mit anderen?",
        ],
    },

    # --- A2 ---
    {
        "level": "A2", "topic": "Wohnort",
        "text": None,
        "questions": [
            "Wo wohnst du und wie gefällt es dir dort?",
            "Was gibt es in deiner Stadt/deinem Viertel Interessantes?",
            "Möchtest du irgendwann umziehen? Wohin?",
        ],
    },
    {
        "level": "A2", "topic": "Urlaub und Reisen",
        "text": None,
        "questions": [
            "Wohin fährst du am liebsten in den Urlaub?",
            "Was war dein schönster Urlaub bisher?",
            "Reist du lieber allein oder mit anderen Menschen?",
        ],
    },
    {
        "level": "A2", "topic": "Wetter und Jahreszeiten",
        "text": None,
        "questions": [
            "Welche Jahreszeit magst du am liebsten und warum?",
            "Was machst du gern, wenn es regnet?",
            "Wie ist das Wetter gerade bei dir?",
        ],
    },
    {
        "level": "A2", "topic": "Einkaufen",
        "text": None,
        "questions": [
            "Kaufst du lieber online oder im Geschäft ein?",
            "Was kaufst du normalerweise am Wochenende ein?",
            "Hast du schon mal etwas zurückgegeben? Warum?",
        ],
    },

    # --- B1 ---
    {
        "level": "B1", "topic": "Arbeit und Freizeit",
        "text": "Immer mehr Menschen in Deutschland arbeiten im Home-Office. Manche finden das gut, weil sie flexibler sind. Andere vermissen den Kontakt zu Kollegen im Büro.",
        "questions": [
            "Was sind für dich die größten Vorteile vom Home-Office?",
            "Vermisst man wirklich etwas, wenn man nicht ins Büro geht?",
            "Wie sieht für dich die ideale Mischung aus Büro und Home-Office aus?",
        ],
    },
    {
        "level": "B1", "topic": "Freundschaft",
        "text": "Manche Menschen haben viele Bekannte, aber nur wenige enge Freunde. Andere sagen, Qualität ist wichtiger als Quantität bei Freundschaften.",
        "questions": [
            "Was macht für dich eine gute Freundschaft aus?",
            "Ist es wichtiger, viele oder wenige, aber enge Freunde zu haben?",
            "Wie hältst du Kontakt zu Freunden, die weit weg wohnen?",
        ],
    },
    {
        "level": "B1", "topic": "Technologie im Alltag",
        "text": "Smartphones begleiten uns fast überall - beim Essen, beim Spazierengehen, sogar im Bett. Manche Experten warnen vor zu viel Bildschirmzeit.",
        "questions": [
            "Wie viel Zeit verbringst du täglich am Handy?",
            "Gibt es Momente, in denen du bewusst offline bleibst?",
            "Was wäre für dich am schwierigsten, wenn du einen Tag ohne Smartphone verbringen müsstest?",
        ],
    },
    {
        "level": "B1", "topic": "Gesundheit und Sport",
        "text": "Viele Menschen nehmen sich vor, mehr Sport zu treiben, schaffen es aber im Alltag oft nicht. Zeitmangel wird häufig als Grund genannt.",
        "questions": [
            "Treibst du regelmäßig Sport? Welchen?",
            "Was hält dich manchmal davon ab, aktiv zu sein?",
            "Wie wichtig ist dir ein gesunder Lebensstil insgesamt?",
        ],
    },

    # --- B2 ---
    {
        "level": "B2", "topic": "Künstliche Intelligenz im Beruf",
        "text": "KI-Tools übernehmen zunehmend Aufgaben, die früher Menschen gemacht haben - von der Textanalyse bis zur Kundenberatung. Unternehmen sehen darin große Effizienzgewinne, Arbeitnehmer sorgen sich um ihre Jobs.",
        "questions": [
            "In welchen Bereichen deiner Arbeit könnte KI dich unterstützen oder ersetzen?",
            "Siehst du KI eher als Bedrohung oder als Chance für deine Karriere?",
            "Welche Fähigkeiten werden deiner Meinung nach trotz KI wichtig bleiben?",
        ],
    },
    {
        "level": "B2", "topic": "Work-Life-Balance",
        "text": "Die Vier-Tage-Woche wird in einigen Ländern getestet, mit dem Ziel, Produktivität und Zufriedenheit gleichzeitig zu erhöhen. Kritiker bezweifeln, dass sich das in jeder Branche umsetzen lässt.",
        "questions": [
            "Würde eine Vier-Tage-Woche in deiner Branche funktionieren?",
            "Was wären für dich persönlich die größten Vorteile?",
            "Welche Nachteile oder Probleme siehst du bei diesem Modell?",
        ],
    },
    {
        "level": "B2", "topic": "Stadtleben vs. Landleben",
        "text": "Immer mehr Berufe lassen sich ortsunabhängig ausüben. Trotzdem ziehen weiterhin viele junge Menschen für die Karriere in die Großstadt.",
        "questions": [
            "Ist ein Umzug in die Großstadt heute noch notwendig für die Karriere?",
            "Was würde dich persönlich mehr reizen: Stadt oder Land?",
            "Welche Kompromisse siehst du, z.B. Vorort oder kleinere Stadt?",
        ],
    },
    {
        "level": "B2", "topic": "Soziale Medien und Gesellschaft",
        "text": "Soziale Medien verbinden Menschen weltweit, werden aber auch für die Verbreitung von Fehlinformationen und für zunehmende gesellschaftliche Polarisierung verantwortlich gemacht.",
        "questions": [
            "Fördern soziale Medien deiner Meinung nach eher Zusammenhalt oder Spaltung?",
            "Hat sich dein eigenes Nutzungsverhalten in den letzten Jahren verändert?",
            "Was könnten Plattformen tun, um negative Effekte zu verringern?",
        ],
    },

    # --- C1 ---
    {
        "level": "C1", "topic": "Führung und New Work",
        "text": "Klassische, hierarchische Führungsstrukturen geraten zunehmend unter Druck. New-Work-Konzepte setzen auf flache Hierarchien, Selbstorganisation und agile Methoden - Kritiker halten das in vielen Branchen für unrealistisch.",
        "questions": [
            "Wie realistisch ist es, flache Hierarchien in traditionellen Branchen wie der Beratung einzuführen?",
            "Welche Führungsqualitäten werden in einer New-Work-Umgebung wichtiger, welche weniger wichtig?",
            "Wo siehst du persönlich die Grenzen von Selbstorganisation im Team?",
        ],
    },
    {
        "level": "C1", "topic": "Lebenslanges Lernen",
        "text": "Angesichts sich schnell wandelnder Berufsbilder wird lebenslanges Lernen oft als Notwendigkeit dargestellt. Gleichzeitig fehlt vielen Berufstätigen neben Vollzeitjob und Familie schlicht die Zeit dafür.",
        "questions": [
            "Wie lässt sich lebenslanges Lernen realistisch mit einem Vollzeitjob vereinbaren?",
            "Sollte die Verantwortung dafür eher beim Individuum oder beim Arbeitgeber liegen?",
            "Welche Rolle spielt Weiterbildung konkret in deiner eigenen Karriereplanung?",
        ],
    },
    {
        "level": "C1", "topic": "Diversität in Führungspositionen",
        "text": "Studien zeigen, dass diverse Führungsteams oft bessere Entscheidungen treffen, dennoch sind Führungsebenen in vielen Unternehmen weiterhin wenig divers. Die Gründe dafür werden kontrovers diskutiert.",
        "questions": [
            "Welche strukturellen Hürden verhindern deiner Meinung nach mehr Diversität in Führungspositionen?",
            "Sind verbindliche Quoten ein sinnvolles Mittel oder eher ein Symptombekämpfung?",
            "Was müsste sich in Unternehmenskultur konkret ändern?",
        ],
    },
    {
        "level": "C1", "topic": "Ethik und Unternehmensverantwortung",
        "text": "Konsumenten und Investoren fordern zunehmend, dass Unternehmen gesellschaftliche und ökologische Verantwortung übernehmen - oft mit dem Vorwurf, dass viele Nachhaltigkeitsversprechen reines Marketing (Greenwashing) sind.",
        "questions": [
            "Wie lässt sich echtes Engagement von reinem Greenwashing unterscheiden?",
            "Sollte Nachhaltigkeit stärker gesetzlich reguliert werden, oder reicht Marktdruck?",
            "Welche Rolle spielt Unternehmensverantwortung für dich bei der Wahl eines Arbeitgebers?",
        ],
    },
]

LEVEL_ORDER = ["A1", "A2", "B1", "B2", "C1"]
