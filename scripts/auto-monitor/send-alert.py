"""Auto-monitor failure alert via Gmail SMTP."""

from __future__ import annotations

import argparse
import logging
import smtplib
from email.mime.text import MIMEText
from pathlib import Path

logger = logging.getLogger(__name__)

ENV_FILE = Path(__file__).parent / ".env"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


def load_env() -> dict[str, str]:
    """Load key=value pairs from .env file."""
    env: dict[str, str] = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().strip().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def build_body(script: str, failures: str, log_file: str, log_dir: Path) -> str:
    """Build alert email body with error details."""
    lines = [
        f"Auto-Monitor {script} 실행 중 실패가 발생했습니다.\n",
        f"스크립트: {script}",
        f"로그: {log_file}\n",
        "실패 항목:",
    ]

    for item in failures.split(","):
        if ":" not in item:
            continue
        domain, code = item.split(":", 1)
        lines.append(f"\n  ● {domain} (exit code {code})")

        # stderr에서 에러 요약 추출
        stderr_path = log_dir / f"{_today()}_{domain}.stderr"
        if script == "friday":
            stderr_path = log_dir / f"{_today()}_fri_{domain}.stderr"
        if stderr_path.exists() and stderr_path.stat().st_size > 0:
            stderr_lines = stderr_path.read_text(errors="replace").strip().splitlines()
            tail = [l.strip() for l in stderr_lines[-3:] if l.strip()]
            if tail:
                lines.append("    " + "\n    ".join(tail))

    lines.append("\n\n이 알림은 자동 생성되었습니다.")
    return "\n".join(lines)


def _today() -> str:
    from datetime import date
    return date.today().isoformat()


def send_email(address: str, password: str, subject: str, body: str) -> None:
    """Send email via Gmail SMTP."""
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = address
    msg["To"] = address
    msg["Subject"] = subject

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(address, password)
        server.send_message(msg)

    logger.info("Alert sent to %s", address)


def main() -> None:
    parser = argparse.ArgumentParser(description="Send auto-monitor failure alert")
    parser.add_argument("--script", required=True, help="Script name (monday/friday/domain)")
    parser.add_argument("--failures", required=True, help="domain:exitcode,... format")
    parser.add_argument("--log-file", default="")
    args = parser.parse_args()

    env = load_env()
    address = env.get("GMAIL_ADDRESS", "")
    password = env.get("GMAIL_APP_PASSWORD", "")

    if not address or not password:
        logger.error("GMAIL_ADDRESS or GMAIL_APP_PASSWORD not set in %s", ENV_FILE)
        return

    today = _today()
    subject = f"[Auto-Monitor] {args.script} 실패 알림 ({today})"
    log_dir = Path(__file__).parent.parent.parent / "logs" / "auto-monitor"
    body = build_body(args.script, args.failures, args.log_file or str(log_dir / f"{today}_{args.script}.log"), log_dir)

    try:
        send_email(address, password, subject, body)
        print(f"[ALERT] Failure notification sent to {address}")
    except Exception as e:
        print(f"[ALERT] Failed to send notification: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
