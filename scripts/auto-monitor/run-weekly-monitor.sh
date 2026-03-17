#!/bin/zsh
# weekly-monitor 자동 실행 스크립트
# Usage: run-weekly-monitor.sh <domain>
# Domains: agentic-ai | voice-ai | secure-ai

set -euo pipefail

DOMAIN="${1:?Usage: $0 <agentic-ai|voice-ai|secure-ai>}"
WORKSPACE="/Users/ctoti/Project/ClaudeCode"
LOG_DIR="$WORKSPACE/logs/auto-monitor"
DATE=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/${DATE}_${DOMAIN}.log"
CLAUDE="$HOME/.local/bin/claude"

# Validate domain
if [[ ! "$DOMAIN" =~ ^(agentic-ai|voice-ai|secure-ai)$ ]]; then
  echo "Invalid domain: $DOMAIN" >&2
  exit 1
fi

# Weekday guard: skip if launchd catch-up fires on wrong day
DOW=$(date +%u)  # 1=Mon, 2=Tue, 3=Wed
case "$DOMAIN" in
  agentic-ai) EXPECTED_DOW=1 ;;
  voice-ai)   EXPECTED_DOW=2 ;;
  secure-ai)  EXPECTED_DOW=3 ;;
esac

if [[ "$DOW" -ne "$EXPECTED_DOW" && "${FORCE:-}" != "1" ]]; then
  echo "[SKIP] $DOMAIN is scheduled for weekday $EXPECTED_DOW, today is $DOW. Use FORCE=1 to override." | tee -a "$LOG_FILE"
  exit 0
fi

mkdir -p "$LOG_DIR"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting weekly-monitor for $DOMAIN" | tee -a "$LOG_FILE"

# Claude Code CLI로 weekly-monitor 실행
run_monitor() {
  cd "$WORKSPACE"
  "$CLAUDE" -p \
    --dangerously-skip-permissions \
    --max-turns 50 \
    --output-format json \
    "/weekly-monitor ${DOMAIN}. 자동화 실행: 추가 키워드 없이 기본 진행. Deep 대상 5개 이하면 전부 자동 승인. PDF 생성 포함. 완료 후 /obsidian-bridge로 메인 리포트 Obsidian 동기화." \
    2>>"$LOG_FILE"
}

RESULT=$(run_monitor) && EXIT_CODE=0 || EXIT_CODE=$?

# 실패 시 재시도 1회
if [[ $EXIT_CODE -ne 0 ]]; then
  echo "[RETRY] First attempt failed (exit=$EXIT_CODE), retrying in 30s..." | tee -a "$LOG_FILE"
  sleep 30
  RESULT=$(run_monitor) && EXIT_CODE=0 || EXIT_CODE=$?
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Finished with exit code $EXIT_CODE" | tee -a "$LOG_FILE"

# Obsidian 일지에 결과 기록
"$HOME/.local/bin/uv" run "$WORKSPACE/scripts/auto-monitor/log-to-obsidian.py" \
  --domain "$DOMAIN" \
  --exit-code "$EXIT_CODE" \
  --result "$RESULT" \
  --log-file "$LOG_FILE"

exit $EXIT_CODE
