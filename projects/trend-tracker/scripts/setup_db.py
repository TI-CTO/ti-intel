"""Set up trend-tracker database tables via Supabase Management API."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

MIGRATION_DIR = (
    Path(__file__).resolve().parent.parent / "src" / "trend_tracker" / "db" / "migrations"
)

MANAGEMENT_API = "https://api.supabase.com/v1/projects/{project_id}/database/query"


def run_query(project_id: str, access_token: str, sql: str) -> list[dict]:
    """Execute SQL via Supabase Management API."""
    resp = requests.post(
        MANAGEMENT_API.format(project_id=project_id),
        headers={"Authorization": f"Bearer {access_token}"},
        json={"query": sql},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    """Run all migration files against the database."""
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")

    project_id = os.environ.get("SUPABASE_PROJECT_ID", "wzkmucknomctkyygciof")
    access_token = os.environ.get("SUPABASE_ACCESS_TOKEN")
    if not access_token:
        print("Error: SUPABASE_ACCESS_TOKEN not found in .env file")
        print("  Generate at: https://supabase.com/dashboard/account/tokens")
        sys.exit(1)

    migration_files = sorted(MIGRATION_DIR.glob("*.sql"))
    if not migration_files:
        print("No migration files found.")
        sys.exit(1)

    for migration_file in migration_files:
        print(f"Running: {migration_file.name}")
        sql = migration_file.read_text()
        run_query(project_id, access_token, sql)
        print(f"  OK: {migration_file.name}")

    print("\nAll migrations completed successfully.")


if __name__ == "__main__":
    main()
