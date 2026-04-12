#!/bin/zsh
# 단일 도메인 주간 모니터링 실행 스크립트
# run-monday.sh의 순차 실행을 개별 스케줄로 분리
#
# Usage: run-domain.sh <domain>
#   domain: agentic-ai | voice-ai | secure-ai | competitor
# Schedule: LaunchAgent에서 도메인별 개별 호출

set -euo pipefail

DOMAIN="${1:?Usage: run-domain.sh <domain>}"
WORKSPACE="/Users/ctoti/Project/ClaudeCode"
LOG_DIR="$WORKSPACE/logs/auto-monitor"
DATE=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/${DATE}_${DOMAIN}.log"
CLAUDE="$HOME/.local/bin/claude"
UV="$HOME/.local/bin/uv"
RETRY_WAIT=300   # 재시도 대기: 5분

mkdir -p "$LOG_DIR"

# ─── 동시 실행 방지: lockfile (도메인별) ───
LOCKFILE="$LOG_DIR/.${DOMAIN}.lock"
if [[ -f "$LOCKFILE" ]]; then
  LOCK_PID=$(cat "$LOCKFILE" 2>/dev/null)
  if kill -0 "$LOCK_PID" 2>/dev/null; then
    echo "[SKIP] ${DOMAIN} already running (PID=$LOCK_PID). Exiting." | tee -a "$LOG_FILE"
    exit 0
  fi
  rm -f "$LOCKFILE"
fi
echo $$ > "$LOCKFILE"

# ─── 절전 방지: caffeinate ───
caffeinate -s -w $$ &
CAFFEINATE_PID=$!
cleanup() {
  kill "$CAFFEINATE_PID" 2>/dev/null || true
  rm -f "$LOCKFILE"
}
trap cleanup EXIT

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting ${DOMAIN} (caffeinate PID=$CAFFEINATE_PID)" | tee -a "$LOG_FILE"

# ─── Claude 실행 ───
STDOUT_FILE="$LOG_DIR/${DATE}_${DOMAIN}.stdout"
STDERR_FILE="$LOG_DIR/${DATE}_${DOMAIN}.stderr"

run_claude() {
  cd "$WORKSPACE"

  local prompt
  if [[ "$DOMAIN" == "competitor" ]]; then
    prompt="/monitor 경쟁사 토픽(skt-strategy, kt-strategy) 스캔. 자동화 실행: intel-store 검색 + WebSearch로 최신 뉴스 수집. 도메인별 리포트에 이미 포함된 기술 동향은 제외하고, 전략/경영/인사/M&A/실적 등 도메인에 걸리지 않는 뉴스에 집중. 스냅샷 저장 및 보고서 생성."
  else
    prompt="/weekly-monitor ${DOMAIN}. 자동화 실행: 추가 키워드 없이 기본 진행. Deep 대상 5개 이하면 전부 자동 승인. PDF 생성 포함. 완료 후 /obsidian-bridge로 메인 리포트 Obsidian 동기화."
  fi

  local max_turns=50
  [[ "$DOMAIN" == "competitor" ]] && max_turns=30

  "$CLAUDE" -p \
    --dangerously-skip-permissions \
    --max-turns "$max_turns" \
    --output-format json \
    "$prompt" \
    >"$STDOUT_FILE" \
    2>"$STDERR_FILE"
}

# 실행 + 실패 시 1회 재시도
run_claude && EXIT_CODE=0 || EXIT_CODE=$?

if [[ $EXIT_CODE -ne 0 ]]; then
  echo "[RETRY] ${DOMAIN} failed (exit=$EXIT_CODE), retrying in ${RETRY_WAIT}s..." | tee -a "$LOG_FILE"
  if [[ -s "$STDERR_FILE" ]]; then
    echo "[STDERR]:" >> "$LOG_FILE"
    tail -20 "$STDERR_FILE" >> "$LOG_FILE"
  fi
  sleep $RETRY_WAIT
  run_claude && EXIT_CODE=0 || EXIT_CODE=$?
fi

echo "[$(date '+%H:%M:%S')] ${DOMAIN}: exit=$EXIT_CODE" | tee -a "$LOG_FILE"

if [[ -s "$STDERR_FILE" ]]; then
  echo "[STDERR]:" >> "$LOG_FILE"
  tail -20 "$STDERR_FILE" >> "$LOG_FILE"
fi

# ─── Obsidian 일지 기록 ───
RESULT=""
[[ -f "$STDOUT_FILE" ]] && RESULT=$(cat "$STDOUT_FILE")

"$UV" run "$WORKSPACE/scripts/auto-monitor/log-to-obsidian.py" \
  --domain "$DOMAIN" \
  --exit-code "$EXIT_CODE" \
  --result "${RESULT:-no-result}" \
  --log-file "$LOG_FILE" \
  --stderr-file "$STDERR_FILE"

# ─── Obsidian 산출물 동기화 ───
OBSIDIAN_WEEKLY="$OBSIDIAN_VAULT_PATH/30-Reports/weekly"
SRC_WEEKLY="$WORKSPACE/outputs/reports/weekly"
if [[ -d "$OBSIDIAN_WEEKLY" ]]; then
  for f in "$SRC_WEEKLY"/${DATE}_*; do
    fname=$(basename "$f")
    # validator 파일 제외, 현재 도메인 관련 파일만
    if [[ "$fname" != *-validator* ]] && [[ "$fname" == *"${DOMAIN}"* || "$fname" == *monitor-skt* || "$fname" == *monitor-kt* ]]; then
      # competitor 도메인일 때만 skt/kt 복사, 아닌 경우 도메인명 매칭
      if [[ "$DOMAIN" == "competitor" ]]; then
        if [[ "$fname" == *monitor-skt* || "$fname" == *monitor-kt* ]]; then
          cp "$f" "$OBSIDIAN_WEEKLY/"
          echo "[SYNC] $fname → Obsidian" >> "$LOG_FILE"
        fi
      else
        if [[ "$fname" == *"${DOMAIN}"* ]]; then
          cp "$f" "$OBSIDIAN_WEEKLY/"
          echo "[SYNC] $fname → Obsidian" >> "$LOG_FILE"
        fi
      fi
    fi
  done
fi

# ─── 실패 시 Gmail 알림 ───
if [[ $EXIT_CODE -ne 0 ]]; then
  echo "[$(date '+%H:%M:%S')] Sending failure alert..." | tee -a "$LOG_FILE"
  "$UV" run "$WORKSPACE/scripts/auto-monitor/send-alert.py" \
    --script "$DOMAIN" \
    --failures "${DOMAIN}:${EXIT_CODE}" \
    --log-file "$LOG_FILE" || true
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] ${DOMAIN} completed" | tee -a "$LOG_FILE"
exit 0
