#!/bin/zsh
# LaunchAgent health check for auto-monitor + paperclip automation.
#
# Verifies that all 7 required LaunchAgents are loaded. Sends Gmail alert
# on any missing. Does NOT attempt auto-remediation (avoids bootout/bootstrap
# conflicts with actively running jobs).
#
# Manual recovery on alert:
#   scripts/auto-monitor/install.sh install
#   scripts/paperclip-dispatcher/install.sh install
#   paperclipai onboard --yes   # if com.ctoti.paperclip missing
#
# Schedule: every day 07:00 (before Mon 08:30 voice-ai).
# Skips if already ran today (sentinel file).

set -euo pipefail

WORKSPACE="/Users/ctoti/Project/ClaudeCode"
LOG_DIR="$WORKSPACE/logs/auto-monitor"
DATE=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/${DATE}_health-check.log"
SENTINEL="$LOG_DIR/.health-check-alert-${DATE}"
UV="$HOME/.local/bin/uv"

mkdir -p "$LOG_DIR"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"; }

REQUIRED_AGENTS=(
  com.ctoti.paperclip
  com.ctoti.paperclip-dispatcher
  com.ctoti.weekly-monitor.voice-ai
  com.ctoti.weekly-monitor.secure-ai
  com.ctoti.weekly-monitor.competitor
  com.ctoti.weekly-monitor.agentic-ai
  com.ctoti.weekly-monitor.fri
)

log "Starting LaunchAgent health check (expecting ${#REQUIRED_AGENTS[@]} agents)"

LOADED=$(launchctl list | awk '/com\.ctoti\./ {print $3}' || true)

MISSING=()
for agent in "${REQUIRED_AGENTS[@]}"; do
  if ! echo "$LOADED" | grep -qx "$agent"; then
    MISSING+=("$agent")
  fi
done

if [[ ${#MISSING[@]} -eq 0 ]]; then
  log "OK: all ${#REQUIRED_AGENTS[@]} LaunchAgents loaded"
  # Clear sentinel so a future failure can alert again
  rm -f "$SENTINEL"
  exit 0
fi

log "MISSING: ${#MISSING[@]} agent(s) not loaded: ${MISSING[*]}"

# Skip alert if already sent today (avoid spam on 10-minute reruns if any)
if [[ -f "$SENTINEL" ]]; then
  log "SKIP-ALERT: already alerted today ($SENTINEL exists)"
  exit 0
fi

# Build failures string for send-alert.py (domain:reason format)
FAILURES=""
for agent in "${MISSING[@]}"; do
  [[ -n "$FAILURES" ]] && FAILURES="${FAILURES},"
  FAILURES="${FAILURES}${agent}:not-loaded"
done

log "Sending Gmail alert..."
"$UV" run "$WORKSPACE/scripts/auto-monitor/send-alert.py" \
  --script "health-check" \
  --failures "$FAILURES" \
  --log-file "$LOG_FILE" 2>>"$LOG_FILE" || {
    log "ALERT-SEND-FAIL"
    exit 1
  }

touch "$SENTINEL"
log "Alert sent. Manual recovery: scripts/auto-monitor/install.sh install"
exit 0
