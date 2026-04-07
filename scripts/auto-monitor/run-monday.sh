#!/bin/zsh
# 월요일 순차 자동화 스크립트
# 3개 도메인 weekly-monitor + 경쟁사 브로드스캔을 순차 실행
#
# Usage: run-monday.sh
# Schedule: 매주 월요일 07:30 (launchd)

set -euo pipefail

WORKSPACE="/Users/ctoti/Project/ClaudeCode"
LOG_DIR="$WORKSPACE/logs/auto-monitor"
DATE=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/${DATE}_monday.log"
CLAUDE="$HOME/.local/bin/claude"
UV="$HOME/.local/bin/uv"
RETRY_WAIT=300   # 재시도 대기: 5분
COOLDOWN=900     # 단계 간 쿨다운: 15분

# Weekday guard: Monday = 1
DOW=$(date +%u)
if [[ "$DOW" -ne 1 && "${FORCE:-}" != "1" ]]; then
  echo "[SKIP] Monday script scheduled for weekday 1, today is $DOW. Use FORCE=1 to override." | tee -a "$LOG_FILE"
  exit 0
fi

mkdir -p "$LOG_DIR"

# ─── 동시 실행 방지: lockfile ───
LOCKFILE="$LOG_DIR/.monday.lock"
if [[ -f "$LOCKFILE" ]]; then
  LOCK_PID=$(cat "$LOCKFILE" 2>/dev/null)
  if kill -0 "$LOCK_PID" 2>/dev/null; then
    echo "[SKIP] Another instance running (PID=$LOCK_PID). Exiting." | tee -a "$LOG_FILE"
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

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting Monday automation (caffeinate PID=$CAFFEINATE_PID)" | tee -a "$LOG_FILE"

# ─── 공통 함수 ───
run_weekly_monitor() {
  local domain="$1"
  local stdout_file="$LOG_DIR/${DATE}_${domain}.stdout"
  local stderr_file="$LOG_DIR/${DATE}_${domain}.stderr"

  cd "$WORKSPACE"
  "$CLAUDE" -p \
    --dangerously-skip-permissions \
    --max-turns 50 \
    --output-format json \
    "/weekly-monitor ${domain}. 자동화 실행: 추가 키워드 없이 기본 진행. Deep 대상 5개 이하면 전부 자동 승인. PDF 생성 포함. 완료 후 /obsidian-bridge로 메인 리포트 Obsidian 동기화." \
    >"$stdout_file" \
    2>"$stderr_file"
  local exit_code=$?

  # stderr 내용을 메인 로그에도 기록
  if [[ -s "$stderr_file" ]]; then
    echo "[STDERR] ${domain}:" >> "$LOG_FILE"
    tail -20 "$stderr_file" >> "$LOG_FILE"
  fi

  # stdout 반환 (caller가 읽을 수 있도록)
  cat "$stdout_file"
  return $exit_code
}

run_with_retry() {
  local domain="$1"
  local label="$2"

  echo "[$(date '+%H:%M:%S')] === ${label} ===" | tee -a "$LOG_FILE"
  local RESULT EXIT_CODE
  RESULT=$(run_weekly_monitor "$domain") && EXIT_CODE=0 || EXIT_CODE=$?

  if [[ $EXIT_CODE -ne 0 ]]; then
    echo "[RETRY] ${label} failed (exit=$EXIT_CODE), retrying in ${RETRY_WAIT}s..." | tee -a "$LOG_FILE"
    sleep $RETRY_WAIT
    RESULT=$(run_weekly_monitor "$domain") && EXIT_CODE=0 || EXIT_CODE=$?
  fi

  echo "[$(date '+%H:%M:%S')] ${label}: exit=$EXIT_CODE" | tee -a "$LOG_FILE"

  # Obsidian 일지 기록
  "$UV" run "$WORKSPACE/scripts/auto-monitor/log-to-obsidian.py" \
    --domain "$domain" \
    --exit-code "$EXIT_CODE" \
    --result "${RESULT:-no-result}" \
    --log-file "$LOG_FILE" \
    --stderr-file "$LOG_DIR/${DATE}_${domain}.stderr"

  return $EXIT_CODE
}

# ─── 1. Agentic AI ───
run_with_retry "agentic-ai" "Step 1/4: Agentic AI" || true

# ─── 쿨다운 (rate limit 회복) ───
echo "[$(date '+%H:%M:%S')] Cooldown ${COOLDOWN}s before next step..." | tee -a "$LOG_FILE"
sleep $COOLDOWN

# ─── 2. Voice AI ───
run_with_retry "voice-ai" "Step 2/4: Voice AI" || true

# ─── 쿨다운 ───
echo "[$(date '+%H:%M:%S')] Cooldown ${COOLDOWN}s before next step..." | tee -a "$LOG_FILE"
sleep $COOLDOWN

# ─── 3. Secure AI ───
run_with_retry "secure-ai" "Step 3/4: Secure AI" || true

# ─── 쿨다운 ───
echo "[$(date '+%H:%M:%S')] Cooldown ${COOLDOWN}s before next step..." | tee -a "$LOG_FILE"
sleep $COOLDOWN

# ─── 4. 경쟁사 전략 브로드스캔 ───
echo "[$(date '+%H:%M:%S')] === Step 4/4: Competitor Broad Scan ===" | tee -a "$LOG_FILE"

COMP_STDOUT="$LOG_DIR/${DATE}_competitor.stdout"
COMP_STDERR="$LOG_DIR/${DATE}_competitor.stderr"

run_competitor() {
  cd "$WORKSPACE"
  "$CLAUDE" -p \
    --dangerously-skip-permissions \
    --max-turns 30 \
    --output-format json \
    "/monitor 경쟁사 토픽(skt-strategy, kt-strategy) 스캔. 자동화 실행: intel-store 검색 + WebSearch로 최신 뉴스 수집. 도메인별 리포트에 이미 포함된 기술 동향은 제외하고, 전략/경영/인사/M&A/실적 등 도메인에 걸리지 않는 뉴스에 집중. 스냅샷 저장 및 보고서 생성." \
    >"$COMP_STDOUT" \
    2>"$COMP_STDERR"
}
run_competitor && COMP_CODE=0 || COMP_CODE=$?

if [[ $COMP_CODE -ne 0 ]]; then
  echo "[RETRY] Competitor scan failed (exit=$COMP_CODE), retrying in ${RETRY_WAIT}s..." | tee -a "$LOG_FILE"
  if [[ -s "$COMP_STDERR" ]]; then
    echo "[STDERR] competitor:" >> "$LOG_FILE"
    tail -20 "$COMP_STDERR" >> "$LOG_FILE"
  fi
  sleep $RETRY_WAIT
  run_competitor && COMP_CODE=0 || COMP_CODE=$?
fi

if [[ -s "$COMP_STDERR" ]]; then
  echo "[STDERR] competitor:" >> "$LOG_FILE"
  tail -20 "$COMP_STDERR" >> "$LOG_FILE"
fi

COMP_RESULT=""
[[ -f "$COMP_STDOUT" ]] && COMP_RESULT=$(cat "$COMP_STDOUT")

echo "[$(date '+%H:%M:%S')] Competitor scan: exit=$COMP_CODE" | tee -a "$LOG_FILE"

"$UV" run "$WORKSPACE/scripts/auto-monitor/log-to-obsidian.py" \
  --domain "competitor" \
  --exit-code "$COMP_CODE" \
  --result "${COMP_RESULT:-no-result}" \
  --log-file "$LOG_FILE" \
  --stderr-file "$COMP_STDERR"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Monday automation completed" | tee -a "$LOG_FILE"
exit 0
