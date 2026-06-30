import pytest
from unittest.mock import MagicMock, patch


def test_parse_feedback_response_extracts_text_and_tags():
    import feedback
    raw = '{"feedback": "Sehr gut! Obwohl ist korrekt.", "error_tags": ["Konnektoren"]}'
    text, tags = feedback._parse_feedback_response(raw)
    assert "Sehr gut" in text
    assert "Konnektoren" in tags


def test_parse_feedback_response_empty_tags():
    import feedback
    raw = '{"feedback": "Alles korrekt!", "error_tags": []}'
    text, tags = feedback._parse_feedback_response(raw)
    assert tags == []


def test_parse_feedback_strips_markdown():
    import feedback
    raw = '```json\n{"feedback": "Gut gemacht.", "error_tags": ["Trennbare Verben"]}\n```'
    text, tags = feedback._parse_feedback_response(raw)
    assert "Gut gemacht" in text
    assert "Trennbare Verben" in tags
