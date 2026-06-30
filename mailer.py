import smtplib
import streamlit as st
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SENDER = "antonyshreyas777@gmail.com"
ANTONY_EMAIL = "ant.mer29@gmail.com"
HORST_EMAIL = "hohennert@t-online.de"


def _get_password() -> str | None:
    if hasattr(st, "secrets"):
        return st.secrets.get("GMAIL_APP_PASSWORD", None)
    return None


def _send(to: str, subject: str, body: str, attachment_bytes: bytes = None, attachment_name: str = None):
    password = _get_password()
    if not password:
        return

    msg = MIMEMultipart()
    msg["From"] = SENDER
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    if attachment_bytes and attachment_name:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment_bytes)
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f'attachment; filename="{attachment_name}"')
        msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER, password)
        server.sendmail(SENDER, to, msg.as_string())


def send_exercise_to_antony(topic: str, exercise_type: str, pdf_bytes: bytes):
    subject = f"Neue Aufgabe von Horst: {topic} - {exercise_type}"
    body = (
        f"Hallo Antony,\n\n"
        f"Horst hat eine neue Aufgabe für dich erstellt.\n\n"
        f"Thema: {topic}\n"
        f"Aufgabentyp: {exercise_type}\n\n"
        f"Die Aufgabe findest du im Anhang als PDF.\n"
        f"Du kannst sie auch direkt in der App bearbeiten:\n"
        f"https://german-trainer-a68crkoeccwkrafx7a84ue.streamlit.app/\n\n"
        f"Viel Erfolg!\nHorst"
    )
    filename = f"aufgabe_{topic.lower().replace(' ', '_').replace('(', '').replace(')', '')}.pdf"
    _send(ANTONY_EMAIL, subject, body, pdf_bytes, filename)


def send_results_to_horst(topic: str, exercise_type: str, answer: dict, claude_feedback: str):
    subject = f"Antony hat eine Aufgabe eingereicht: {topic}"
    answer_lines = []
    for key, val in answer.items():
        if isinstance(val, list):
            for i, v in enumerate(val):
                if isinstance(v, dict):
                    answer_lines.append(f"  {i+1}. {v}")
                else:
                    answer_lines.append(f"  {i+1}. {v}")
        else:
            answer_lines.append(f"  {key}: {val}")

    body = (
        f"Hallo Horst,\n\n"
        f"Antony hat eine Aufgabe bearbeitet und eingereicht.\n\n"
        f"Thema: {topic}\n"
        f"Aufgabentyp: {exercise_type}\n\n"
        f"--- Antwort von Antony ---\n"
        f"{chr(10).join(answer_lines)}\n\n"
        f"--- Claudes automatisches Feedback ---\n"
        f"{claude_feedback}\n\n"
        f"Sie können Ihr persönliches Feedback in der App hinterlassen:\n"
        f"https://german-trainer-a68crkoeccwkrafx7a84ue.streamlit.app/\n\n"
        f"Mit freundlichen Grüßen\nDeutsch Trainer"
    )
    _send(HORST_EMAIL, subject, body)
