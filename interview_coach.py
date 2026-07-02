# interview_coach.py
import streamlit as st
import anthropic

_SYSTEM_PROMPT = """Du hilfst einem Bewerber, einen Baustein seiner mündlichen Selbstpräsentation für ein deutsches Vorstellungsgespräch zu formulieren.

WICHTIGE REGELN (basierend auf Recherche zu deutschen Recruitern):
- Natürliche, gesprochene Sprache - keine Schriftsprache, keine verschachtelten Sätze.
- KEINE Floskeln oder Klischees: "sehr motiviert", "Teamplayer", "Herausforderungen lieben", "hochmotiviert", "dynamisch" - diese Wörter sind bei deutschen Recruitern verbrannt.
- Nur die gegebenen Stichpunkte verwenden - KEINE neuen Fakten erfinden.
- Konkret statt abstrakt: wenn ein Stichpunkt eine Leistung nennt, kurz benennen WAS es war, nicht nur dass es gut war.
- Der Text ist ein Vorschlag zum Ausformulieren, kein auswendig zu lernendes Skript - der Bewerber wird ihn in eigenen Worten sprechen. Schreibe ihn trotzdem so, dass er beim lauten Lesen natürlich klingt (kurze Sätze, keine Schachtelsätze).
- Passe die Länge an die Ziel-Sprechdauer an (Faustregel: ca. 2,3 Wörter pro Sekunde gesprochen).
- Register: professionell, aber persönlich und direkt - nicht steif, nicht übertrieben förmlich.

Antworte NUR mit dem fertigen deutschen Text - kein Vorspann, keine Erklärung, keine Anführungszeichen drumherum."""


def draft_script(title: str, stichpunkte: list[str], dauer: str, extra_context: str = "") -> str:
    """Generate a natural-sounding spoken-German draft for one Baustein, grounded only in the given bullet points."""
    api_key = st.secrets.get("ANTHROPIC_API_KEY") if hasattr(st, "secrets") else None
    client = anthropic.Anthropic(api_key=api_key)

    points_text = "\n".join(f"- {p}" for p in stichpunkte)
    context_section = f"\nZusätzlicher Kontext vom Bewerber: {extra_context}" if extra_context.strip() else ""

    user_prompt = f"""Baustein: "{title}"
Ziel-Sprechdauer: {dauer}

Stichpunkte (nur diese Fakten verwenden):
{points_text}
{context_section}

Formuliere daraus einen natürlichen, gesprochenen deutschen Text für diesen Baustein."""

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=512,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response.content[0].text.strip()
