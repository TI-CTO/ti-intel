"""Run a SQL migration file against Supabase via the Management API.

Usage:
    SUPABASE_ACCESS_TOKEN=<pat> uv run scripts/run_migration.py <migration_file>

Example:
    SUPABASE_ACCESS_TOKEN=sbp_xxx uv run scripts/run_migration.py \
        docs/db/migrations/002_key_highlights_source_refs.sql
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import requests


PROJECT_REF = "wzkmucknomctkyygciof"
API_URL = f"https://api.supabase.com/v1/projects/{PROJECT_REF}/database/query"


def run_migration(sql_path: Path, pat: str) -> None:
    sql = sql_path.read_text()

    # Split on semicolons; strip comment lines from each chunk before filtering
    def strip_comments(chunk: str) -> str:
        lines = [ln for ln in chunk.splitlines() if not ln.strip().startswith("--")]
        return "\n".join(lines).strip()

    statements = [stripped for s in sql.split(";") if (stripped := strip_comments(s))]

    headers = {
        "Authorization": f"Bearer {pat}",
        "Content-Type": "application/json",
    }

    for i, stmt in enumerate(statements, 1):
        print(f"[{i}/{len(statements)}] {stmt[:60]}...")
        resp = requests.post(API_URL, headers=headers, json={"query": stmt + ";"}, timeout=30)
        if resp.status_code not in (200, 201):
            print(f"  ERROR {resp.status_code}: {resp.text}")
            sys.exit(1)
        print(f"  OK")

    print(f"\nMigration complete: {sql_path.name}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: run_migration.py <migration_file>")
        sys.exit(1)

    pat = os.environ.get("SUPABASE_ACCESS_TOKEN")
    if not pat:
        print("Error: SUPABASE_ACCESS_TOKEN environment variable not set.")
        print("  Get your PAT from: https://supabase.com/dashboard/account/tokens")
        print("  Then run: SUPABASE_ACCESS_TOKEN=sbp_xxx uv run scripts/run_migration.py <file>")
        sys.exit(1)

    sql_path = Path(sys.argv[1])
    if not sql_path.exists():
        print(f"Error: File not found: {sql_path}")
        sys.exit(1)

    run_migration(sql_path, pat)


if __name__ == "__main__":
    main()
