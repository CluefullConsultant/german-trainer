import io
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def _styles():
    base = getSampleStyleSheet()
    title = ParagraphStyle(
        "ExTitle", parent=base["Heading1"], fontSize=14, spaceAfter=6
    )
    subtitle = ParagraphStyle(
        "ExSubtitle", parent=base["Normal"], fontSize=10, textColor="#555555", spaceAfter=12
    )
    body = ParagraphStyle(
        "ExBody", parent=base["Normal"], fontSize=11, spaceAfter=8, leading=16
    )
    label = ParagraphStyle(
        "ExLabel", parent=base["Normal"], fontSize=10, textColor="#333333",
        spaceAfter=4, fontName="Helvetica-Bold"
    )
    blank_line = ParagraphStyle(
        "BlankLine", parent=base["Normal"], fontSize=11, spaceAfter=14, leading=20
    )
    return title, subtitle, body, label, blank_line


def generate_exercise_pdf(topic: str, exercise_type: str, content: dict) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2.5 * cm,
        leftMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
    )

    title_style, subtitle_style, body_style, label_style, blank_style = _styles()
    story = []

    story.append(Paragraph(f"Deutsch Trainer", title_style))
    story.append(Paragraph(f"Thema: {topic} | Aufgabentyp: {exercise_type}", subtitle_style))
    story.append(Spacer(1, 0.3 * cm))

    if exercise_type == "Lückentext":
        story.append(Paragraph("Aufgabe: Füllen Sie die Lücken aus.", label_style))
        text = content.get("text_with_blanks", "").replace("___", "____________")
        story.append(Paragraph(text, body_style))
        story.append(Spacer(1, 0.3 * cm))
        story.append(Paragraph("Hinweise zu den Lücken:", label_style))
        for i, blank in enumerate(content.get("blanks", [])):
            story.append(Paragraph(f"{i+1}. {blank.get('hint', '')}", body_style))

    elif exercise_type == "Mehrfachauswahl":
        story.append(Paragraph("Aufgabe: Wählen Sie die richtige Antwort.", label_style))
        for i, item in enumerate(content.get("items", [])):
            story.append(Paragraph(f"{i+1}. {item.get('question', '')}", body_style))
            for opt in item.get("options", []):
                story.append(Paragraph(f"    ☐  {opt}", body_style))
            story.append(Spacer(1, 0.2 * cm))

    elif exercise_type == "Satztransformation":
        story.append(Paragraph("Aufgabe: Transformieren Sie die Sätze.", label_style))
        for i, item in enumerate(content.get("items", [])):
            story.append(Paragraph(f"{i+1}. {item.get('instruction', '')}", body_style))
            for s in item.get("sentences", []):
                story.append(Paragraph(f"    {s}", body_style))
            story.append(Paragraph("Ihre Antwort: _________________________________________________", blank_style))

    elif exercise_type == "Fehlersuche":
        story.append(Paragraph("Aufgabe: Finden und korrigieren Sie den Fehler (wenn vorhanden).", label_style))
        for i, sentence in enumerate(content.get("sentences", [])):
            story.append(Paragraph(f"{i+1}. {sentence.get('text', '')}", body_style))
            story.append(Paragraph("    Fehler? ☐ Ja  ☐ Nein    Korrektur: _______________________________", blank_style))

    elif exercise_type == "Übersetzung":
        story.append(Paragraph(f"Aufgabe: Übersetzen Sie die Sätze.", label_style))
        for i, item in enumerate(content.get("items", [])):
            story.append(Paragraph(f"{i+1}. {item.get('source', '')}", body_style))
            story.append(Paragraph("    Übersetzung: _________________________________________________", blank_style))

    elif exercise_type == "Kategoriensortierung":
        story.append(Paragraph(content.get("instruction", ""), label_style))
        words = ", ".join(content.get("words", []))
        story.append(Paragraph(f"Wörter: {words}", body_style))
        story.append(Spacer(1, 0.3 * cm))
        for cat in content.get("categories", {}).keys():
            story.append(Paragraph(f"{cat}:", label_style))
            story.append(Paragraph("_____________________________________________________________", blank_style))

    elif exercise_type == "Brief schreiben":
        story.append(Paragraph("Aufgabe:", label_style))
        story.append(Paragraph(content.get("prompt", ""), body_style))
        story.append(Spacer(1, 0.3 * cm))
        story.append(Paragraph("Behandeln Sie folgende Punkte (Reihenpunkte):", label_style))
        for punkt in content.get("reihenpunkte", []):
            story.append(Paragraph(f"• {punkt}", body_style))
        if content.get("time_limit_minutes"):
            story.append(Paragraph(f"Zeitlimit: {content['time_limit_minutes']} Minuten", body_style))
        story.append(Spacer(1, 0.5 * cm))
        story.append(Paragraph("Ihr Brief:", label_style))
        for _ in range(18):
            story.append(Paragraph("_____________________________________________________________", blank_style))

    elif exercise_type in ("Leseverstehen", "Hörverstehen"):
        if exercise_type == "Hörverstehen":
            story.append(Paragraph("Hinweis: Ihr Mentor liest den Text vor. Hören Sie gut zu.", label_style))
        else:
            story.append(Paragraph("Lesen Sie den folgenden Text:", label_style))
            story.append(Paragraph(content.get("text", ""), body_style))
            story.append(Spacer(1, 0.4 * cm))
        story.append(Paragraph("Fragen:", label_style))
        for i, q in enumerate(content.get("questions", [])):
            story.append(Paragraph(f"{i+1}. {q.get('question', '')}", body_style))
            story.append(Paragraph("    Antwort: ____________________________________________________", blank_style))

    elif exercise_type == "Sprechaufgabe":
        story.append(Paragraph("Sprechanlass:", label_style))
        story.append(Paragraph(content.get("prompt", ""), body_style))
        story.append(Spacer(1, 0.3 * cm))
        story.append(Paragraph("Hinweise:", label_style))
        for hint in content.get("hints", []):
            story.append(Paragraph(f"• {hint}", body_style))
        story.append(Spacer(1, 0.5 * cm))
        story.append(Paragraph("Notizen:", label_style))
        for _ in range(6):
            story.append(Paragraph("_____________________________________________________________", blank_style))

    doc.build(story)
    buffer.seek(0)
    return buffer.read()
