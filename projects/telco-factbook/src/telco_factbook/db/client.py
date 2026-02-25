"""Supabase client wrapper."""

from __future__ import annotations

import logging

from supabase import Client, create_client

from telco_factbook.config import settings

logger = logging.getLogger(__name__)

_client: Client | None = None


def get_client() -> Client:
    """Get or create a Supabase client singleton."""
    global _client  # noqa: PLW0603
    if _client is None:
        if not settings.supabase_url or not settings.supabase_key:
            raise RuntimeError(
                "SUPABASE_URL and SUPABASE_KEY must be set in .env file. "
                "Create a Supabase project at https://supabase.com and copy the credentials."
            )
        _client = create_client(settings.supabase_url, settings.supabase_key)
        logger.info("Supabase client initialized: %s", settings.supabase_url)
    return _client
