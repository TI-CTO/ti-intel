"""Tests for intel_store.db.repository (mocked DB calls)."""

from unittest.mock import MagicMock, patch


class TestBatchLinkTopic:
    """Tests for IntelRepository.batch_link_topic."""

    @patch("intel_store.db.repository.get_client")
    def test_batch_link_topic_single_upsert(self, mock_get_client):
        """batch_link_topic resolves topic once and upserts all rows in one call."""
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client

        # Mock topic resolution
        topic_chain = mock_client.table.return_value.select.return_value
        topic_chain.eq.return_value.limit.return_value.execute.return_value.data = [{"id": 42}]
        # Mock upsert
        mock_client.table.return_value.upsert.return_value.execute.return_value.data = [
            {"item_id": 1, "topic_id": 42},
            {"item_id": 2, "topic_id": 42},
            {"item_id": 3, "topic_id": 42},
        ]

        from intel_store.db.repository import IntelRepository

        repo = IntelRepository()
        result = repo.batch_link_topic([1, 2, 3], "test-topic")

        assert result == 3

        # Verify upsert was called with 3 rows
        upsert_call = mock_client.table.return_value.upsert
        upsert_call.assert_called_once()
        rows = upsert_call.call_args[0][0]
        assert len(rows) == 3
        assert all(r["topic_id"] == 42 for r in rows)
        assert [r["item_id"] for r in rows] == [1, 2, 3]

    @patch("intel_store.db.repository.get_client")
    def test_batch_link_topic_invalid_topic_raises(self, mock_get_client):
        """batch_link_topic raises ValueError for unknown topic."""
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client

        # Mock topic not found
        topic_chain = mock_client.table.return_value.select.return_value
        topic_chain.eq.return_value.limit.return_value.execute.return_value.data = []

        from intel_store.db.repository import IntelRepository

        repo = IntelRepository()

        import pytest

        with pytest.raises(ValueError, match="Topic not found"):
            repo.batch_link_topic([1, 2], "nonexistent-topic")
