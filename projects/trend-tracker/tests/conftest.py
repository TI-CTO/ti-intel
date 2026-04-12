"""Shared fixtures for trend-tracker tests."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest


def make_mock_client() -> MagicMock:
    """Create a mock Supabase client with fluent-chaining support.

    Each call to client.table(name) returns a fresh MagicMock chain
    that terminates at .execute() → MagicMock(data=[...]).
    Use client.table.return_value.execute.return_value to set data.
    """
    client = MagicMock()
    return client


@pytest.fixture()
def mock_client():
    """Patch get_client and return mock Supabase client."""
    client = make_mock_client()
    with patch("trend_tracker.db.repository.get_client", return_value=client):
        yield client


@pytest.fixture()
def repo(mock_client):
    """Create a TrendRepository with mocked Supabase client."""
    from trend_tracker.db.repository import TrendRepository

    return TrendRepository()
