#!/bin/zsh
# 경쟁사(SKT/KT) 모니터링 자동 실행 스크립트
# Usage: run-competitor-monitor.sh
# Schedule: 매주 목요일 09:00

set -euo pipefail

WORKSPACE="/Users/ctoti/Project/ClaudeCode"
LOG_DIR="$WORKSPACE/logs/auto-monitor"
DATE=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/${DATE}_competitor.log"
CLAUDE="$HOME/.local/bin/claude"

# Weekday guard: Thursday = 4
DOW=$(date +%u)
if [[ "$DOW" -ne 4 && "${FORCE:-}" != "1" ]]; then
  echo "[SKIP] Competitor monitor is scheduled for Thursday (4), today is $DOW. Use FORCE=1 to override." | tee -a "$LOG_FILE"
  exit 0
fi

mkdir -p "$LOG_DIR"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting competitor monitor (skt-strategy, kt-strategy)" | tee -a "$LOG_FILE"

# Claude Code CLI로 /monitor 실행
run_monitor() {
  cd "$WORKSPACE"
  "$CLAUDE" -p \
    --dangerously-skip-permissions \
    --max-turns 30 \
    --output-format json \
    "/monitor 경쟁사 토픽(skt-strategy, kt-strategy) 스캔. 자동화 실행: intel-store 검색 + WebSearch로 최신 뉴스 수집. 스냅샷 저장 및 보고서 생성. 완료 후 🟡🔴 토픽만 /obsidian-bridge로 Obsidian 동기화." \
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
  --domain "competitor" \
  --exit-code "$EXIT_CODE" \
  --result "$RESULT" \
  --log-file "$LOG_FILE"

exit $EXIT_CODE
