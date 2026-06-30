import pytest
from unittest.mock import patch


def test_parse_vocabulary_response():
    import vocabulary
    raw = '[{"word": "trotzdem", "definition": "dennoch, aber", "example": "Er war müde, trotzdem ging er."}]'
    result = vocabulary._parse_vocab_response(raw)
    assert len(result) == 1
    assert result[0]["word"] == "trotzdem"


def test_parse_vocabulary_strips_markdown():
    import vocabulary
    raw = '```json\n[{"word": "obwohl", "definition": "auch wenn", "example": "Obwohl er müde war..."}]\n```'
    result = vocabulary._parse_vocab_response(raw)
    assert result[0]["word"] == "obwohl"


def test_parse_vocabulary_invalid_returns_empty():
    import vocabulary
    result = vocabulary._parse_vocab_response("keine json hier")
    assert result == []
