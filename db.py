# db.py
import streamlit as st
from supabase import create_client, Client
from datetime import datetime, timezone
import time


@st.cache_resource
def get_client() -> Client:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)


def _execute_with_retry(fn, retries=3, delay=1):
    """Execute a Supabase query with retries on connection error."""
    import httpx
    last_err = None
    for attempt in range(retries):
        try:
            return fn()
        except (httpx.ConnectError, httpx.TimeoutException, Exception) as e:
            last_err = e
            if attempt < retries - 1:
                time.sleep(delay)
    raise last_err


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
    rows = _execute_with_retry(lambda: query.execute().data)

    result = []
    for row in rows:
        subs = row.get("submissions") or []
        if status_filter == "Neu" and subs:
            continue
        if status_filter == "Beim Mentor" and not subs:
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


def save_vocabulary(words: list[dict], exercise_id: str | None = None) -> None:
    client = get_client()
    rows = []
    for w in words:
        row = {"word": w["word"], "definition": w["definition"], "example": w["example"]}
        if exercise_id is not None:
            row["exercise_id"] = exercise_id
        rows.append(row)
    if rows:
        client.table("vocabulary").insert(rows).execute()


def get_due_vocabulary():
    """Words due for review: not reviewed in 3+ days OR never reviewed. Max 10."""
    client = get_client()
    from datetime import datetime, timedelta, timezone
    cutoff = (datetime.now(timezone.utc) - timedelta(days=3)).isoformat()
    never = client.table("vocabulary").select("*").is_("last_reviewed", "null").limit(5).execute()
    old = client.table("vocabulary").select("*").lt("last_reviewed", cutoff).limit(5).execute()
    seen_ids = {r["id"] for r in never.data}
    combined = never.data + [r for r in old.data if r["id"] not in seen_ids]
    return combined[:10]


def update_vocabulary_review(vocab_id: str, correct: bool):
    client = get_client()
    from datetime import datetime, timezone
    row = client.table("vocabulary").select("correct_count,review_count").eq("id", vocab_id).single().execute().data
    client.table("vocabulary").update({
        "last_reviewed": datetime.now(timezone.utc).isoformat(),
        "review_count": row["review_count"] + 1,
        "correct_count": row["correct_count"] + (1 if correct else 0),
    }).eq("id", vocab_id).execute()


def get_vocabulary() -> list[dict]:
    client = get_client()
    result = client.table("vocabulary").select("*").order("added_at", desc=True).execute()
    return result.data


def get_top_errors(limit: int = 3) -> list[dict]:
    """Return the most frequent error tags across all submissions."""
    client = get_client()
    result = client.table("submissions").select("error_tags").not_.is_("error_tags", "null").execute()
    from collections import Counter
    counter = Counter()
    for row in result.data:
        for tag in (row.get("error_tags") or []):
            counter[tag] += 1
    return [{"tag": tag, "count": count} for tag, count in counter.most_common(limit)]


def get_submissions_for_exercise(exercise_id: str) -> list[dict]:
    client = get_client()
    result = client.table("submissions").select("*").eq("exercise_id", exercise_id).order("submitted_at", desc=True).execute()
    return result.data


def get_streak() -> int:
    """Count consecutive days with at least one submission ending today."""
    client = get_client()
    from datetime import datetime, timedelta, timezone
    result = client.table("submissions").select("submitted_at").order("submitted_at", desc=True).execute()
    if not result.data:
        return 0
    dates = sorted(set(r["submitted_at"][:10] for r in result.data), reverse=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if dates[0] != today:
        return 0
    streak = 1
    for i in range(1, len(dates)):
        expected = (datetime.now(timezone.utc) - timedelta(days=i)).strftime("%Y-%m-%d")
        if dates[i] == expected:
            streak += 1
        else:
            break
    return streak


def get_error_stats() -> dict:
    client = get_client()
    result = client.table("submissions").select("error_tags").execute()
    counts: dict[str, int] = {}
    for row in result.data:
        tags = row.get("error_tags") or []
        for tag in tags:
            counts[tag] = counts.get(tag, 0) + 1
    return counts
