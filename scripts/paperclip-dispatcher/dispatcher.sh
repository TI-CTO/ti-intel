#!/bin/zsh
# Paperclip Issue Dispatcher
# Polls regular issues + routine-generated issues and triggers heartbeat for assigned agents.
# Runs every 3 minutes via LaunchAgent.

set -euo pipefail

PAUSE_FLAG="$HOME/.paperclip-dispatcher-paused"
LOG_DIR="/Users/ctoti/Project/ClaudeCode/logs/dispatcher"
LOG_FILE="$LOG_DIR/$(date +%Y-%m-%d).log"
API_BASE="http://127.0.0.1:3100/api/companies/a8aeda24-7cd4-47d2-b235-ac4dbf09b22a"
NPX="/Users/ctoti/.nvm/versions/node/v24.14.0/bin/npx"
LOCKFILE="$LOG_DIR/.dispatcher.lock"

mkdir -p "$LOG_DIR"

log() { echo "[$(date '+%H:%M:%S')] $*" >> "$LOG_FILE"; }

# ─── Pause check ───
if [[ -f "$PAUSE_FLAG" ]]; then
  exit 0
fi

# ─── Lockfile (prevent overlapping polls) ───
if [[ -f "$LOCKFILE" ]]; then
  LOCK_PID=$(cat "$LOCKFILE" 2>/dev/null)
  if kill -0 "$LOCK_PID" 2>/dev/null; then
    log "SKIP: previous heartbeat still active (PID=$LOCK_PID)"
    exit 0
  fi
  rm -f "$LOCKFILE"
fi

# ─── Paperclip 서버 프로세스 확인 ───
# 서버가 실행 중이지 않으면 에러 로그 없이 조용히 종료
if ! pgrep -f "paperclipai" > /dev/null 2>&1; then
  exit 0
fi

# ─── API 가용성 확인 ───
# 서버 프로세스는 있지만 아직 준비 안 된 경우만 로그
curl -sf --max-time 5 "$API_BASE/agents" >/dev/null 2>&1 || {
  log "ERROR: API unreachable"
  exit 0
}

# ─── [A] Routine 이슈 처리 ───
# GET /issues 는 done 이슈만 반환하는 Paperclip 버그가 있음.
# Routine 생성 이슈(originKind=routine_execution)는 /routines 엔드포인트의
# lastRun.linkedIssueId 를 통해서만 접근 가능. checkout 후 heartbeat 필요.
ROUTINES_JSON=$(curl -sf --max-time 10 "$API_BASE/routines" 2>/dev/null) || {
  log "ERROR: routines API unreachable"
  ROUTINES_JSON="[]"
}

ROUTINE_WORK=$(echo "$ROUTINES_JSON" | python3 -c "
import json, sys
routines = json.load(sys.stdin)
for r in routines:
    lr = r.get('lastRun') or {}
    li = lr.get('linkedIssue') or {}
    issue_id = lr.get('linkedIssueId')
    issue_status = li.get('status')
    agent_id = r.get('assigneeAgentId')
    checkout_run = li.get('checkoutRunId') or lr.get('checkoutRunId')
    execution_run = li.get('executionRunId')
    started_at = li.get('startedAt')
    updated_at = li.get('updatedAt') or ''
    # 처리 대상:
    #   1) todo/backlog: 정상 대기 중
    #   2) in_progress + checkout/execution 없음: stale 상태 (서버 재시작·sleep 후 누락)
    #      단, updatedAt이 2시간 이내이면 에이전트가 실행 중으로 간주 → 스킵
    #      (startedAt은 checkout 시점에 설정되므로 실행 여부 판단에 부적합)
    is_pending = issue_status in ('todo', 'backlog')
    if issue_status == 'in_progress' and not checkout_run and not execution_run:
        from datetime import datetime, timezone, timedelta
        try:
            updated = datetime.fromisoformat(updated_at.replace('Z', '+00:00'))
            age_min = (datetime.now(timezone.utc) - updated).total_seconds() / 60
            is_stale_inprogress = age_min > 120  # 2시간 넘게 업데이트 없으면 stale
        except Exception:
            is_stale_inprogress = True
    else:
        is_stale_inprogress = False
    if issue_id and agent_id and (is_pending or is_stale_inprogress):
        print(f'{issue_id}|{agent_id}|{r.get(\"title\",\"?\")[:30]}')
" 2>/dev/null)

if [[ -n "$ROUTINE_WORK" ]]; then
  while IFS= read -r LINE; do
    [[ -z "$LINE" ]] && continue
    ISSUE_ID="${LINE%%|*}"
    REST="${LINE#*|}"
    AGENT_ID="${REST%%|*}"
    TITLE="${REST#*|}"

    log "ROUTINE-CHECKOUT: $ISSUE_ID ($TITLE) → agent $AGENT_ID"
    $NPX paperclipai issue checkout "$ISSUE_ID" \
      --agent-id "$AGENT_ID" \
      --expected-statuses "todo,backlog,blocked,in_progress" \
      2>/dev/null && log "ROUTINE-CHECKOUT-OK: $ISSUE_ID" || \
      log "ROUTINE-CHECKOUT-FAIL: $ISSUE_ID"
  done <<< "$ROUTINE_WORK"
fi

# ─── [B] 일반 이슈 처리 (GET /issues 는 done만 반환하므로 현재 효과 없음, 구조 유지) ───
ISSUES_JSON=$(curl -sf --max-time 10 "$API_BASE/issues?status=backlog,todo" 2>/dev/null) || ISSUES_JSON="[]"

# ─── Promote backlog → todo ───
BACKLOG_IDS=$(echo "$ISSUES_JSON" | python3 -c "
import json, sys
issues = json.load(sys.stdin)
for i in issues:
    if i.get('status') == 'backlog' and i.get('assigneeAgentId'):
        print(i['id'])
" 2>/dev/null)

if [[ -n "$BACKLOG_IDS" ]]; then
  while IFS= read -r ISSUE_ID; do
    [[ -z "$ISSUE_ID" ]] && continue
    curl -sf --max-time 5 -X PATCH "http://127.0.0.1:3100/api/issues/$ISSUE_ID" \
      -H "Content-Type: application/json" \
      -d '{"status":"todo"}' >/dev/null 2>&1 && \
      log "PROMOTE: $ISSUE_ID backlog→todo"
  done <<< "$BACKLOG_IDS"
fi

# ─── Auto-assign unassigned issues to CTO (장재현) ───
CTO_AGENT_ID="d3fc30d8-6480-41bf-a80a-087ddef5bc74"
UNASSIGNED_IDS=$(echo "$ISSUES_JSON" | python3 -c "
import json, sys
issues = json.load(sys.stdin)
for i in issues:
    if not i.get('assigneeAgentId'):
        print(i['id'])
" 2>/dev/null)

if [[ -n "$UNASSIGNED_IDS" ]]; then
  while IFS= read -r ISSUE_ID; do
    [[ -z "$ISSUE_ID" ]] && continue
    curl -sf --max-time 5 -X PATCH "http://127.0.0.1:3100/api/issues/$ISSUE_ID" \
      -H "Content-Type: application/json" \
      -d "{\"assigneeAgentId\":\"$CTO_AGENT_ID\",\"status\":\"todo\"}" >/dev/null 2>&1 && \
      log "ASSIGN-CTO: $ISSUE_ID → 장재현"
  done <<< "$UNASSIGNED_IDS"
  ISSUES_JSON=$(curl -sf --max-time 10 "$API_BASE/issues?status=backlog,todo" 2>/dev/null) || ISSUES_JSON="[]"
fi

# ─── Extract unique assignee agent IDs with pending work (일반 이슈 + Routine checkout된 에이전트) ───
ROUTINE_AGENT_IDS=$(echo "$ROUTINE_WORK" | python3 -c "
import sys
seen = set()
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    parts = line.split('|')
    if len(parts) >= 2 and parts[1] not in seen:
        seen.add(parts[1])
        print(parts[1])
" 2>/dev/null)

ISSUE_AGENT_IDS=$(echo "$ISSUES_JSON" | python3 -c "
import json, sys
issues = json.load(sys.stdin)
seen = set()
for i in issues:
    aid = i.get('assigneeAgentId')
    if aid and aid not in seen:
        seen.add(aid)
        print(aid)
" 2>/dev/null)

AGENT_IDS=$(printf '%s\n%s' "$ROUTINE_AGENT_IDS" "$ISSUE_AGENT_IDS" | sort -u | grep -v '^$' || true)

if [[ -z "$AGENT_IDS" ]]; then
  exit 0
fi

# ─── Fetch agent statuses (skip paused agents) ���──
AGENTS_JSON=$(curl -sf --max-time 10 "$API_BASE/agents" 2>/dev/null) || {
  log "ERROR: agents API unreachable"
  exit 0
}

PAUSED_AGENTS=$(echo "$AGENTS_JSON" | python3 -c "
import json, sys
agents = json.load(sys.stdin)
for a in agents:
    if a.get('status') == 'paused':
        print(a['id'])
" 2>/dev/null)

# ─── Trigger heartbeat for each agent with pending work ───
TRIGGERED=0
PIDS=()

while IFS= read -r AGENT_ID; do
  [[ -z "$AGENT_ID" ]] && continue

  # Skip paused agents
  if echo "$PAUSED_AGENTS" | grep -q "$AGENT_ID"; then
    log "SKIP-PAUSED: $AGENT_ID"
    continue
  fi

  log "HEARTBEAT: $AGENT_ID"
  $NPX paperclipai heartbeat run \
    -a "$AGENT_ID" \
    --source assignment \
    --trigger system \
    --timeout-ms 7200000 \
    >> "$LOG_DIR/heartbeat-$(date +%Y-%m-%d).log" 2>&1 &

  PIDS+=($!)
  TRIGGERED=$((TRIGGERED + 1))
done <<< "$AGENT_IDS"

if [[ $TRIGGERED -gt 0 ]]; then
  log "Triggered $TRIGGERED agent(s)"
  # Write first PID to lockfile so subsequent polls can detect active heartbeats
  echo "${PIDS[1]}" > "$LOCKFILE"
fi

# Fire-and-forget: don't wait for heartbeats to complete.
# The lockfile PID check prevents overlapping dispatches.
# Clean up lockfile when all heartbeats finish (background).
if [[ ${#PIDS[@]} -gt 0 ]]; then
  (
    for pid in "${PIDS[@]}"; do
      wait "$pid" 2>/dev/null
    done
    rm -f "$LOCKFILE"
  ) &
fi
