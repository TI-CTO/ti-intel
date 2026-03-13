"""Run SQL migration against Supabase via Management API.

Usage:
    SUPABASE_ACCESS_TOKEN=sbp_xxx uv run python scripts/run_migration.py db/migrations/002_add_update_policies.sql

Requires:
    - SUPABASE_ACCESS_TOKEN env var (Personal Access Token from Supabase dashboard)
    - requests library (included in supabase dependency)
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

import requests

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

PROJECT_REF = "wzkmucknomctkyygciof"
API_BASE = f"https://api.supabase.com/v1/projects/{PROJECT_REF}/database/query"


def run_sql(sql: str, token: str) -> dict:
    """Execute SQL via Supabase Management API.

    Args:
        sql: SQL string to execute.
        token: Supabase Personal Access Token.

    Returns:
        API response as dict.
    """
    resp = requests.post(
        API_BASE,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={"query": sql},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    """Parse CLI args and run migration file."""
    if len(sys.argv) < 2:
        print("Usage: SUPABASE_ACCESS_TOKEN=sbp_xxx uv run python scripts/run_migration.py <sql_file>")
        sys.exit(1)

    token = os.environ.get("SUPABASE_ACCESS_TOKEN")
    if not token:
        print("Error: SUPABASE_ACCESS_TOKEN env var required")
        sys.exit(1)

    sql_path = Path(sys.argv[1])
    if not sql_path.exists():
        print(f"Error: File not found: {sql_path}")
        sys.exit(1)

    sql = sql_path.read_text(encoding="utf-8")
    logger.info("Running migration: %s (%d chars)", sql_path.name, len(sql))

    # Split by semicolons and run each statement
    statements = [s.strip() for s in sql.split(";") if s.strip() and not s.strip().startswith("--")]

    for i, stmt in enumerate(statements, 1):
        logger.info("  Statement %d/%d: %.60s...", i, len(statements), stmt.replace("\n", " "))
        try:
            result = run_sql(stmt, token)
            logger.info("    OK")
        except requests.HTTPError as e:
            logger.error("    FAILED: %s", e.response.text if e.response else e)
            # Continue with remaining statements
        except Exception as e:
            logger.error("    FAILED: %s", e)

    logger.info("Migration complete: %s", sql_path.name)


if __name__ == "__main__":
    main()
