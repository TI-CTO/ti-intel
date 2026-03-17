"""Auto-monitor 실행 결과를 Obsidian 일지에 기록."""

from __future__ import annotations

import argparse
import json
import logging
from datetime import date
from pathlib import Path

VAULT = Path("/Users/ctoti/Obsidian/Obsidian_Work")
DEVLOG = VAULT / "40-DevLog"

logger = logging.getLogger(__name__)


def build_entry(domain: str, exit_code: int, result: str, log_file: str) -> str:
    """Build a markdown entry for the Obsidian daily log."""
    if exit_code == 0:
        icon = "✅"
        try:
            data = json.loads(result)
            summary = str(data.get("result", "완료"))[:300]
        except (json.JSONDecodeError, TypeError):
            summary = "완료 (상세 로그 확인)"
    else:
        icon = "❌"
        summary = f"exit code {exit_code}"

    return (
        f"\n### Auto-Monitor: {domain} {icon}\n"
        f"- **상태**: {'성공' if exit_code == 0 else '실패'}\n"
        f"- **요약**: {summary}\n"
        f"- **로그**: `{log_file}`\n"
    )


def append_to_daily_log(entry: str) -> Path:
    """Append entry to today's daily log, creating if needed."""
    today = date.today().isoformat()
    log_path = DEVLOG / f"{today}_daily-log.md"

    if log_path.exists():
        content = log_path.read_text(encoding="utf-8")
        content += entry
        log_path.write_text(content, encoding="utf-8")
    else:
        content = (
            f"---\ntags: [daily-log]\n"
            f"created: {today}\n---\n\n"
            f"# {today} 업무일지\n"
            f"{entry}"
        )
        DEVLOG.mkdir(parents=True, exist_ok=True)
        log_path.write_text(content, encoding="utf-8")

    return log_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Log auto-monitor results to Obsidian")
    parser.add_argument("--domain", required=True)
    parser.add_argument("--exit-code", type=int, required=True)
    parser.add_argument("--result", default="")
    parser.add_argument("--log-file", default="")
    args = parser.parse_args()

    entry = build_entry(args.domain, args.exit_code, args.result, args.log_file)
    log_path = append_to_daily_log(entry)
    logger.info("Logged to %s", log_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
