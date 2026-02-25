"""Tests for trend_tracker.db.repository — helper functions only.

Repository integration tests require a live Supabase connection.
These tests cover utility functions that don't need DB access.
"""

import json

from trend_tracker.db.repository import _parse_json_list


def test_parse_json_list_from_string():
    result = _parse_json_list('["a", "b", "c"]')
    assert result == ["a", "b", "c"]


def test_parse_json_list_from_list():
    result = _parse_json_list(["x", "y"])
    assert result == ["x", "y"]


def test_parse_json_list_empty_string():
    result = _parse_json_list("[]")
    assert result == []


def test_parse_json_list_invalid_json():
    result = _parse_json_list("not json")
    assert result == []


def test_parse_json_list_none():
    result = _parse_json_list(None)
    assert result == []
