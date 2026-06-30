# tests/test_db.py
import json
import pytest
from unittest.mock import MagicMock, patch

# We test the logic around db.py without hitting real Supabase.
# Each function is tested by mocking the supabase client.

@patch("db.get_client")
def test_save_exercise_returns_id(mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.table.return_value.insert.return_value.execute.return_value.data = [
        {"id": "abc-123"}
    ]
    import db
    result = db.save_exercise("Konnektoren", "Luckentext", {"text_with_blanks": "test"}, "")
    assert result == "abc-123"

@patch("db.get_client")
def test_get_exercises_no_filter(mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.table.return_value.select.return_value.order.return_value.execute.return_value.data = [
        {"id": "abc-123", "topic": "Konnektoren", "exercise_type": "Luckentext"}
    ]
    import db
    result = db.get_exercises(None, None)
    assert len(result) == 1
    assert result[0]["topic"] == "Konnektoren"

@patch("db.get_client")
def test_save_submission_returns_id(mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.table.return_value.insert.return_value.execute.return_value.data = [
        {"id": "sub-456"}
    ]
    import db
    result = db.save_submission("abc-123", {"answer": "war"})
    assert result == "sub-456"

@patch("db.get_client")
def test_get_error_stats_returns_dict(mock_get_client):
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.table.return_value.select.return_value.execute.return_value.data = [
        {"error_tags": ["Konnektoren", "Trennbare Verben"]},
        {"error_tags": ["Konnektoren"]},
        {"error_tags": None},
    ]
    import db
    result = db.get_error_stats()
    assert result["Konnektoren"] == 2
    assert result["Trennbare Verben"] == 1
