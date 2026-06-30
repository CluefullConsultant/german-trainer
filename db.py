# db.py
import streamlit as st
from supabase import create_client, Client
from datetime import datetime, timezone


def get_client() -> Client:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)


def save_exercise(topic: str, exercise_type: str, content: dict, mentor_notes: str) -> str:
    client = get_client()
    result = client.table("exercises").insert({
        "topic": topic,
        "exercise_type": exercise_type,
        "content": content,
        "mentor_notes": mentor_notes,
    }).execute()
    return result.data[0]["id"]


def get_exercises(topic_filter: str | None = None, status_filter: str | None = None) -> list[dict]:
    client = get_client()
    query = client.table("exercises").select(
        "*, submissions(id, reviewed_at)"
    ).order("created_at", desc=True)
    if topic_filter:
        query = query.eq("topic", topic_filter)
    rows = query.execute().data

    result = []
    for row in rows:
        subs = row.get("submissions") or []
        if status_filter == "Neu" and subs:
            continue
        if status_filter == "Bearbeitet" and not subs:
            continue
        if status_filter == "Feedback erhalten" and not any(s.get("reviewed_at") for s in subs):
            continue
        # Attach latest status label
        if not subs:
            row["status"] = "Neu"
        elif any(s.get("reviewed_at") for s in subs):
            row["status"] = "Feedback erhalten"
        else:
            row["status"] = "Beim Mentor"
        result.append(row)
    return result


def get_exercise(exercise_id: str) -> dict:
    client = get_client()
    result = client.table("exercises").select("*").eq("id", exercise_id).single().execute()
    return result.data


def save_submission(exercise_id: str, answer: dict) -> str:
    client = get_client()
    result = client.table("submissions").insert({
        "exercise_id": exercise_id,
        "answer": answer,
    }).execute()
    return result.data[0]["id"]


def save_claude_feedback(submission_id: str, feedback: str, error_tags: list[str]) -> None:
    client = get_client()
    client.table("submissions").update({
        "claude_feedback": feedback,
        "error_tags": error_tags,
    }).eq("id", submission_id).execute()


def save_mentor_feedback(submission_id: str, feedback: str) -> None:
    client = get_client()
    client.table("submissions").update({
        "mentor_feedback": feedback,
        "reviewed_at": datetime.now(timezone.utc).isoformat(),
    }).eq("id", submission_id).execute()


def get_unreviewed_submissions() -> list[dict]:
    client = get_client()
    result = client.table("submissions").select(
        "*, exercises(topic, exercise_type, content)"
    ).is_("reviewed_at", "null").order("submitted_at", desc=True).execute()
    return result.data


def get_all_reviewed_submissions() -> list[dict]:
    client = get_client()
    result = client.table("submissions").select(
        "*, exercises(topic, exercise_type, content)"
    ).not_.is_("reviewed_at", "null").order("reviewed_at", desc=True).execute()
    return result.data


def save_vocabulary(words: list[dict], exercise_id: str) -> None:
    client = get_client()
    rows = [
        {"word": w["word"], "definition": w["definition"], "example": w["example"], "exercise_id": exercise_id}
        for w in words
    ]
    if rows:
        client.table("vocabulary").insert(rows).execute()


def get_vocabulary() -> list[dict]:
    client = get_client()
    result = client.table("vocabulary").select("*").order("added_at", desc=True).execute()
    return result.data


def get_error_stats() -> dict:
    client = get_client()
    result = client.table("submissions").select("error_tags").execute()
    counts: dict[str, int] = {}
    for row in result.data:
        tags = row.get("error_tags") or []
        for tag in tags:
            counts[tag] = counts.get(tag, 0) + 1
    return counts
