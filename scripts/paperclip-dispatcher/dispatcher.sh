#!/bin/zsh
# Paperclip Issue Dispatcher
# Polls for backlog/todo issues and triggers heartbeat for assigned agents.
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

# ─── Fetch pending issues (single API call) ───
ISSUES_JSON=$(curl -sf --max-time 10 "$API_BASE/issues?status=backlog,todo" 2>/dev/null) || {
  log "ERROR: API unreachable"
  exit 0
}

# ─── Promote backlog → todo (agents only see todo in inbox) ───
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
    curl -sf --max-time 5 -X PATCH "$API_BASE/issues/$ISSUE_ID" \
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
    curl -sf --max-time 5 -X PATCH "$API_BASE/issues/$ISSUE_ID" \
      -H "Content-Type: application/json" \
      -d "{\"assigneeAgentId\":\"$CTO_AGENT_ID\",\"status\":\"todo\"}" >/dev/null 2>&1 && \
      log "ASSIGN-CTO: $ISSUE_ID → 장재현"
  done <<< "$UNASSIGNED_IDS"
  # Re-fetch issues after assignment
  ISSUES_JSON=$(curl -sf --max-time 10 "$API_BASE/issues?status=backlog,todo" 2>/dev/null) || exit 0
fi

# ─── Extract unique assignee agent IDs with pending work ───
AGENT_IDS=$(echo "$ISSUES_JSON" | python3 -c "
import json, sys
issues = json.load(sys.stdin)
seen = set()
for i in issues:
    aid = i.get('assigneeAgentId')
    if aid and aid not in seen:
        seen.add(aid)
        print(aid)
" 2>/dev/null)

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
    --timeout-ms 600000 \
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
