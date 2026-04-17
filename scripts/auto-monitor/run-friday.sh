#!/bin/zsh
# 금요일 통합 자동화 스크립트
# 매주: 주간 종합 + 데이터 건강 체크
# 매월 첫째 금: + 포트폴리오 리뷰 + 딜 파이프라인 리뷰
# 매월 마지막 금: + 월간 종합 리포트
# 분기 첫째 금 (3,6,9,12월): + WTIS 재평가 + 경쟁사 종합
#
# Usage: run-friday.sh
# Schedule: 매주 금요일 09:00 (launchd)

set -euo pipefail

WORKSPACE="/Users/ctoti/Project/ClaudeCode"
LOG_DIR="$WORKSPACE/logs/auto-monitor"
DATE=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/${DATE}_friday.log"
CLAUDE="$HOME/.local/bin/claude"
UV="$HOME/.local/bin/uv"

# Weekday guard: Friday = 5
DOW=$(date +%u)
if [[ "$DOW" -ne 5 && "${FORCE:-}" != "1" ]]; then
  echo "[SKIP] Friday script scheduled for weekday 5, today is $DOW. Use FORCE=1 to override." | tee -a "$LOG_FILE"
  exit 0
fi

mkdir -p "$LOG_DIR"

# ─── 동시 실행 방지: lockfile ───
LOCKFILE="$LOG_DIR/.friday.lock"
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

# 날짜 판단
DAY_OF_MONTH=$(date +%d)
MONTH=$(date +%m)
IS_FIRST_FRIDAY=false
IS_LAST_FRIDAY=false
IS_QUARTER_MONTH=false

# 첫째 금요일: 1~7일 사이의 금요일
if [[ "$DAY_OF_MONTH" -le 7 ]]; then
  IS_FIRST_FRIDAY=true
fi

# 마지막 금요일: 다음 금요일(+7일)이 다음 달이면 이번이 마지막
NEXT_FRIDAY_MONTH=$(date -v+7d +%m)
if [[ "$NEXT_FRIDAY_MONTH" != "$MONTH" ]]; then
  IS_LAST_FRIDAY=true
fi

# 분기 월: 3, 6, 9, 12
if [[ "$MONTH" == "03" || "$MONTH" == "06" || "$MONTH" == "09" || "$MONTH" == "12" ]]; then
  IS_QUARTER_MONTH=true
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting Friday automation" | tee -a "$LOG_FILE"
echo "  First Friday: $IS_FIRST_FRIDAY | Last Friday: $IS_LAST_FRIDAY | Quarter Month: $IS_QUARTER_MONTH" | tee -a "$LOG_FILE"

# 실패 추적 변수
FAILED_TASKS=""

# ─── 공통: claude 실행 + stderr 캡처 ───
run_claude_task() {
  local task_name="$1"
  local max_turns="$2"
  local prompt="$3"
  local stdout_file="$LOG_DIR/${DATE}_fri_${task_name}.stdout"
  local stderr_file="$LOG_DIR/${DATE}_fri_${task_name}.stderr"

  cd "$WORKSPACE"
  "$CLAUDE" -p \
    --dangerously-skip-permissions \
    --max-turns "$max_turns" \
    --output-format json \
    "$prompt" \
    >"$stdout_file" \
    2>"$stderr_file"
  local exit_code=$?

  if [[ -s "$stderr_file" ]]; then
    echo "[STDERR] ${task_name}:" >> "$LOG_FILE"
    tail -20 "$stderr_file" >> "$LOG_FILE"
  fi

  cat "$stdout_file"
  return $exit_code
}

# ─── 1. 주간 종합 리포트 (매주) ───
echo "[$(date '+%H:%M:%S')] === Task 1: Weekly Summary ===" | tee -a "$LOG_FILE"
RESULT=$(run_claude_task "weekly-summary" 30 \
  "금요일 주간 종합: 이번 주 outputs/reports/weekly/ 에서 최신 주간 리포트(agentic-ai, voice-ai, secure-ai)와 경쟁사 모니터링 결과를 읽고, CTO용 1페이지 주간 요약을 작성해줘. 포함 항목: (1) 도메인별 핵심 시그널 3줄씩, (2) 🔴 긴급 항목 하이라이트, (3) 포트폴리오 현황 변동, (4) 다음 주 주목 이슈. outputs/reports/weekly/${DATE}_weekly-summary.md 로 저장. PDF도 생성.") && EXIT_CODE=0 || EXIT_CODE=$?
echo "[$(date '+%H:%M:%S')] Weekly summary: exit=$EXIT_CODE" | tee -a "$LOG_FILE"
[[ $EXIT_CODE -ne 0 ]] && FAILED_TASKS="${FAILED_TASKS:+$FAILED_TASKS,}weekly-summary:${EXIT_CODE}"

# ─── 2. 데이터 건강 체크 (매주) ───
echo "[$(date '+%H:%M:%S')] === Task 2: Data Health Check ===" | tee -a "$LOG_FILE"
HEALTH_RESULT=$(run_claude_task "health-check" 15 \
  "데이터 건강 체크: get_intel_stats로 intel-store 현황 확인. 체크 항목: (1) 전체 아이템 수, (2) 최근 7일 수집 건수, (3) 소스별 분포(news/paper/patent), (4) 토픽별 건수. 이상 징후(수집 0건, 특정 소스 누락 등)가 있으면 경고 표시. 결과를 간단히 텍스트로 출력해줘.") && HEALTH_CODE=0 || HEALTH_CODE=$?
echo "[$(date '+%H:%M:%S')] Health check: exit=$HEALTH_CODE" | tee -a "$LOG_FILE"
[[ $HEALTH_CODE -ne 0 ]] && FAILED_TASKS="${FAILED_TASKS:+$FAILED_TASKS,}health-check:${HEALTH_CODE}"

# ─── 3. 포트폴리오 리뷰 (매월 첫째 금) ───
if [[ "$IS_FIRST_FRIDAY" == "true" ]]; then
  echo "[$(date '+%H:%M:%S')] === Task 3: Monthly Portfolio Review ===" | tee -a "$LOG_FILE"
  PORT_RESULT=$(run_claude_task "portfolio-review" 30 \
    "월간 포트폴리오 리뷰: outputs/reports/ 아래 3개 도메인(agentic-ai, voice-ai, secure-ai)의 portfolio.md를 읽고 종합 분석해줘. (1) 도메인별 Go/Conditional/No-Go/미평가 현황, (2) 지난 달 대비 점수 변동, (3) 미평가 L2 기술 중 다음 달 WTIS 우선 대상 3건 제안, (4) 전체 포트폴리오 건강도 평가. outputs/reports/${DATE}_monthly-portfolio-review.md 로 저장. PDF도 생성.") && PORT_CODE=0 || PORT_CODE=$?
  echo "[$(date '+%H:%M:%S')] Portfolio review: exit=$PORT_CODE" | tee -a "$LOG_FILE"
  [[ $PORT_CODE -ne 0 ]] && FAILED_TASKS="${FAILED_TASKS:+$FAILED_TASKS,}portfolio-review:${PORT_CODE}"

  # ─── 4. 딜 파이프라인 리뷰 (매월 첫째 금) ───
  echo "[$(date '+%H:%M:%S')] === Task 4: Deal Pipeline Review ===" | tee -a "$LOG_FILE"
  DEAL_RESULT=$(run_claude_task "deal-review" 20 \
    "딜 파이프라인 리뷰: startup-db의 search_companies를 사용해서 deal_stage별 현황을 확인해줘. (1) 각 deal_stage별 건수, (2) screening 또는 due_diligence 단계에서 30일 이상 정체된 기업 목록, (3) 최근 1개월 deal_stage 변경 이력, (4) 다음 단계로 진행 권고 기업. 결과를 outputs/reports/${DATE}_monthly-deal-review.md 로 저장.") && DEAL_CODE=0 || DEAL_CODE=$?
  echo "[$(date '+%H:%M:%S')] Deal review: exit=$DEAL_CODE" | tee -a "$LOG_FILE"
  [[ $DEAL_CODE -ne 0 ]] && FAILED_TASKS="${FAILED_TASKS:+$FAILED_TASKS,}deal-review:${DEAL_CODE}"
fi

# ─── 5. WTIS 전수 재평가 (분기 첫째 금) ───
if [[ "$IS_FIRST_FRIDAY" == "true" && "$IS_QUARTER_MONTH" == "true" ]]; then
  echo "[$(date '+%H:%M:%S')] === Task 5: Quarterly WTIS Re-evaluation ===" | tee -a "$LOG_FILE"
  WTIS_RESULT=$(run_claude_task "wtis-reeval" 60 \
    "분기 WTIS 재평가: outputs/reports/ 아래 3개 도메인의 portfolio.md를 읽고, Go 또는 Conditional Go 판정을 받은 L2 기술들을 확인해줘. 각 기술의 마지막 평가일이 60일 이상 경과한 것만 대상으로, 주요 변화 사항(시장, 경쟁, 기술 성숙도)을 간략히 조사하고 재평가 필요 여부를 판단해줘. 전수 재실행은 하지 말고, 재평가 권고 목록만 작성해서 outputs/reports/${DATE}_quarterly-wtis-reeval.md 로 저장.") && WTIS_CODE=0 || WTIS_CODE=$?
  echo "[$(date '+%H:%M:%S')] WTIS re-eval: exit=$WTIS_CODE" | tee -a "$LOG_FILE"
  [[ $WTIS_CODE -ne 0 ]] && FAILED_TASKS="${FAILED_TASKS:+$FAILED_TASKS,}wtis-reeval:${WTIS_CODE}"

  # ─── 6. 경쟁사 전략 종합 (분기 첫째 금) ───
  echo "[$(date '+%H:%M:%S')] === Task 6: Quarterly Competitor Summary ===" | tee -a "$LOG_FILE"
  COMP_RESULT=$(run_claude_task "competitor-summary" 40 \
    "분기 경쟁사 전략 종합: intel-store에서 search_intel(topic='skt-strategy', limit=50)과 search_intel(topic='kt-strategy', limit=50)으로 최근 3개월 데이터를 수집해줘. (1) SKT 전략 방향 변화 요약 (주요 발표, 투자, 제휴), (2) KT 전략 방향 변화 요약, (3) LG U+ 대비 포지셔닝 시사점, (4) 다음 분기 주목 포인트. outputs/reports/${DATE}_quarterly-competitor-summary.md 로 저장. PDF도 생성.") && COMP_CODE=0 || COMP_CODE=$?
  echo "[$(date '+%H:%M:%S')] Competitor summary: exit=$COMP_CODE" | tee -a "$LOG_FILE"
  [[ $COMP_CODE -ne 0 ]] && FAILED_TASKS="${FAILED_TASKS:+$FAILED_TASKS,}competitor-summary:${COMP_CODE}"
fi

# ─── 7. 월간 종합 리포트 (매월 마지막 금) ───
if [[ "$IS_LAST_FRIDAY" == "true" ]]; then
  YEAR_MONTH=$(date +%Y-%m)
  echo "[$(date '+%H:%M:%S')] === Task 7: Monthly Synthesis ===" | tee -a "$LOG_FILE"
  SYNTH_RESULT=$(run_claude_task "monthly-synthesis" 40 \
    "월간 종합 리포트 작성 (${YEAR_MONTH}):

이번 달 산출물을 읽고 CTO용 월간 종합 브리핑을 작성해줘.

입력 소스:
1. outputs/reports/weekly/${YEAR_MONTH}-*_weekly-summary.md (주간 종합 4건)
2. outputs/reports/weekly/${YEAR_MONTH}-*_weekly-*.md (도메인별 주간 리포트)
3. outputs/reports/${YEAR_MONTH}-*_monthly-portfolio-review.md (포트폴리오 리뷰, 있으면)
4. outputs/reports/${YEAR_MONTH}-*_monthly-deal-review.md (딜 리뷰, 있으면)
5. outputs/reports/*/portfolio.md (각 도메인 최신 포트폴리오)

구성:
1. Executive Summary — 이번 달 핵심 3~5가지 (가장 임팩트 큰 시그널)
2. 도메인별 월간 추이 — 4주 신호 뱃지 집계 테이블 + 트렌드 코멘트
3. 포트폴리오 변동 — 점수 상승/하락, Go 전환 후보, 재평가 결과
4. 경쟁사 포지셔닝 — SKT/KT 월간 핵심 액션 + 차별화 기회
5. 딜 파이프라인 — 신규 진입/단계 변경/탈락 (딜 리뷰 있으면)
6. 수집 통계 — intel-store get_intel_stats로 건수 추이, 유형 분포
7. 다음 달 액션 — WTIS 재평가 대상 + 운영 개선

outputs/reports/${DATE}_monthly-synthesis.md 로 저장. PDF도 생성.") && SYNTH_CODE=0 || SYNTH_CODE=$?
  echo "[$(date '+%H:%M:%S')] Monthly synthesis: exit=$SYNTH_CODE" | tee -a "$LOG_FILE"
  [[ $SYNTH_CODE -ne 0 ]] && FAILED_TASKS="${FAILED_TASKS:+$FAILED_TASKS,}monthly-synthesis:${SYNTH_CODE}"
fi

# ─── 실패 시 Gmail 알림 ───
if [[ -n "$FAILED_TASKS" ]]; then
  echo "[$(date '+%H:%M:%S')] Sending failure alert for: $FAILED_TASKS" | tee -a "$LOG_FILE"
  "$UV" run "$WORKSPACE/scripts/auto-monitor/send-alert.py" \
    --script friday \
    --failures "$FAILED_TASKS" \
    --log-file "$LOG_FILE" || true
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Friday automation completed" | tee -a "$LOG_FILE"

# Obsidian 일지에 결과 기록
"$UV" run "$WORKSPACE/scripts/auto-monitor/log-to-obsidian.py" \
  --domain "friday-summary" \
  --exit-code "$EXIT_CODE" \
  --result "${RESULT:-no-result}" \
  --log-file "$LOG_FILE" \
  --stderr-file "$LOG_DIR/${DATE}_fri_weekly-summary.stderr"

exit 0
