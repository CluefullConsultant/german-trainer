import json
import pytest
from unittest.mock import MagicMock, patch


def test_topics_list_not_empty():
    import exercises
    assert len(exercises.TOPICS) > 10
    assert "Konnektoren" in exercises.TOPICS
    assert "Deklination (Nominativ/Akkusativ/Dativ/Genitiv)" in exercises.TOPICS


def test_exercise_types_not_empty():
    import exercises
    assert "Luckentext" in exercises.EXERCISE_TYPES
    assert "Brief schreiben" in exercises.EXERCISE_TYPES


def test_exercise_types_for_topic_brief_schreiben():
    import exercises
    types = exercises.EXERCISE_TYPES_FOR_TOPIC.get("Schriftlicher Ausdruck (Brief)", [])
    assert "Brief schreiben" in types


def test_parse_exercise_json_strips_fences():
    import exercises
    raw = '```json\n{"text_with_blanks": "test"}\n```'
    result = exercises._parse_json(raw)
    assert result["text_with_blanks"] == "test"


def test_parse_exercise_json_plain():
    import exercises
    raw = '{"text_with_blanks": "test"}'
    result = exercises._parse_json(raw)
    assert result["text_with_blanks"] == "test"


def test_parse_exercise_json_invalid_raises():
    import exercises
    with pytest.raises(ValueError):
        exercises._parse_json("this is not json at all")
