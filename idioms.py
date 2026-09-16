"""Curated, positively-toned German idioms for the 'Redewendung des Tages' card.

Each meaning_de is sourced from the German Wiktionary's own idiom category
(Kategorie:Redewendung (Deutsch), de.wiktionary.org), not invented - only the
English gloss and example sentence are written for this app. Selected for a
positive/encouraging tone; ambiguous double-meaning idioms were trimmed to
their positive sense (see e.g. "mit Pauken und Trompeten").
"""
import random
import streamlit as st

IDIOM_LIST = [
    {"idiom": "auf Wolke sieben schweben", "meaning_de": "extrem (oft auch naiv) glücklich, euphorisch sein", "meaning_en": "cloud nine / walking on air", "example": "Seit dem ersten Date schwebt sie auf Wolke sieben."},
    {"idiom": "Schmetterlinge im Bauch haben", "meaning_de": "verliebt und glücklich sein", "meaning_en": "butterflies in your stomach", "example": "Vor unserem ersten Treffen hatte ich richtig Schmetterlinge im Bauch."},
    {"idiom": "den Nagel auf den Kopf treffen", "meaning_de": "einen präzisen, zutreffenden Kommentar abgeben; das Wesentliche, den Kernpunkt erfassen", "meaning_en": "hit the nail on the head", "example": "Mit deiner Analyse hast du den Nagel auf den Kopf getroffen."},
    {"idiom": "grünes Licht geben", "meaning_de": "genehmigen, die Erlaubnis erteilen ein Vorhaben durchzuführen", "meaning_en": "give the green light", "example": "Der Chef hat endlich grünes Licht für das Projekt gegeben."},
    {"idiom": "mit Leib und Seele", "meaning_de": "mit großer Begeisterung, mit vollem Einsatz sowohl mit dem Körper als auch mit dem Geiste", "meaning_en": "heart and soul, wholeheartedly", "example": "Sie ist mit Leib und Seele Lehrerin."},
    {"idiom": "Feuer und Flamme sein", "meaning_de": "begeistert sein", "meaning_en": "be fired up / enthusiastic", "example": "Nach dem Vortrag war das ganze Team Feuer und Flamme für die Idee."},
    {"idiom": "die Ärmel hochkrempeln", "meaning_de": "umgangssprachlich: sich energisch an die Arbeit machen, bei einer Tätigkeit kräftig mitarbeiten", "meaning_en": "roll up your sleeves", "example": "Jetzt müssen wir einfach die Ärmel hochkrempeln und anfangen."},
    {"idiom": "ein Herz und eine Seele sein", "meaning_de": "eine sehr enge Bindung zueinander haben, sehr eng befreundet sein", "meaning_en": "be inseparable / two peas in a pod", "example": "Die beiden sind seit der Schulzeit ein Herz und eine Seele."},
    {"idiom": "sich ins Zeug legen", "meaning_de": "umgangssprachlich: angestrengt an etwas arbeiten, sich abmühen, keine Mühe scheuen", "meaning_en": "put in serious effort", "example": "Er hat sich für die Prüfung richtig ins Zeug gelegt."},
    {"idiom": "auf Anhieb", "meaning_de": "gleich beim ersten Versuch, beim ersten Mal, von Anfang an", "meaning_en": "right off the bat, on the first try", "example": "Sie hat die Stelle auf Anhieb bekommen."},
    {"idiom": "die Fäden in der Hand haben", "meaning_de": "die Kontrolle haben, das Sagen haben", "meaning_en": "have things under control, pull the strings", "example": "In diesem Projekt hat sie die Fäden in der Hand."},
    {"idiom": "in aller Munde sein", "meaning_de": "der breiten Öffentlichkeit bekannt (und deshalb Gesprächsthema) sein", "meaning_en": "be on everyone's lips, be the talk of the town", "example": "Das neue Restaurant ist gerade in aller Munde."},
    {"idiom": "Hals- und Beinbruch", "meaning_de": "umgangssprachliche Wunschformel für das gute Gelingen eines Vorhabens mit der Bedeutung: Viel Glück!", "meaning_en": "break a leg (good luck)", "example": "Hals- und Beinbruch für dein Vorstellungsgespräch morgen!"},
    {"idiom": "alle Hände voll zu tun haben", "meaning_de": "viel Arbeit haben, beschäftigt sein", "meaning_en": "have your hands full (busy, in demand)", "example": "Vor dem Launch hatten wir alle Hände voll zu tun."},
    {"idiom": "aus dem Vollen schöpfen", "meaning_de": "große Auswahl haben, sich nicht einschränken müssen", "meaning_en": "have plenty to draw from", "example": "Bei der Auswahl an Bewerbern konnten wir aus dem Vollen schöpfen."},
    {"idiom": "das Herz auf dem rechten Fleck haben", "meaning_de": "uneigennützig, hilfsbereit und nett sein, gute Absichten haben, ehrlich sein", "meaning_en": "have your heart in the right place", "example": "Er wirkt streng, aber er hat das Herz auf dem rechten Fleck."},
    {"idiom": "den Rücken stärken", "meaning_de": "jemanden unterstützen", "meaning_en": "have someone's back, back them up", "example": "Die ganze Familie hat ihr in der schweren Zeit den Rücken gestärkt."},
    {"idiom": "die Ohren spitzen", "meaning_de": "aufmerksam zuhören", "meaning_en": "prick up your ears, listen closely", "example": "Als der Chef das Projekt erwähnte, spitzte sie die Ohren."},
    {"idiom": "ein Auge zudrücken", "meaning_de": "etwas durchgehen lassen und nicht bestrafen", "meaning_en": "turn a blind eye (kindly)", "example": "Der Prüfer hat bei der kleinen Verspätung ein Auge zugedrückt."},
    {"idiom": "Gas geben", "meaning_de": "sich beeilen, etwas schneller erledigen; sich mehr anstrengen, mit vollem Einsatz trainieren oder spielen", "meaning_en": "step on it, give it your all", "example": "In den letzten Wochen vor der Prüfung müssen wir Gas geben."},
    {"idiom": "Hand aufs Herz", "meaning_de": "Aufforderung, die Wahrheit zu sagen: nun sag/sagen Sie mal ehrlich …", "meaning_en": "cross your heart, be honest", "example": "Hand aufs Herz: Hast du wirklich schon fertig gelernt?"},
    {"idiom": "im siebten Himmel sein", "meaning_de": "auf Grund von Freude vom Rest der Welt abgeschottet sein, überglücklich sein", "meaning_en": "be in seventh heaven", "example": "Nach der Zusage war sie im siebten Himmel."},
    {"idiom": "mit Pauken und Trompeten", "meaning_de": "mit großem Aufwand und feierlicher Inszenierung, triumphal", "meaning_en": "with flying colors, triumphantly", "example": "Er hat die Prüfung mit Pauken und Trompeten bestanden."},
    {"idiom": "wie am Schnürchen", "meaning_de": "reibungslos, ohne Probleme zu bereiten", "meaning_en": "like clockwork, smoothly", "example": "Am Umzugstag lief alles wie am Schnürchen."},
    {"idiom": "einen grünen Daumen haben", "meaning_de": "Talent für Gärtnerei haben, Geschick im Umgang mit Pflanzen besitzen", "meaning_en": "have a green thumb", "example": "Meine Oma hat einfach einen grünen Daumen, bei ihr wächst alles."},
    {"idiom": "einen Stein ins Rollen bringen", "meaning_de": "den Anstoß zu einer Entwicklung geben, durch eine Handlung eine Kettenreaktion auslösen", "meaning_en": "set something in motion, kick things off", "example": "Diese eine E-Mail hat den Stein ins Rollen gebracht."},
]


def get_daily_idiom() -> dict:
    """Pick one idiom at random, stable for the browser session so it doesn't
    change on every button click/rerun - a fresh one shows up each time the
    app is opened again."""
    if "daily_idiom_index" not in st.session_state:
        st.session_state["daily_idiom_index"] = random.randrange(len(IDIOM_LIST))
    entry = IDIOM_LIST[st.session_state["daily_idiom_index"]]
    return {
        "idiom": entry["idiom"],
        "meaning": f"{entry['meaning_de']} ({entry['meaning_en']})",
        "example": entry["example"],
    }
