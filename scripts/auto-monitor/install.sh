#!/bin/zsh
# launchd plist 설치/제거 스크립트
# Usage: install.sh [install|uninstall]
# 월~금 5개 에이전트 등록

set -euo pipefail

ACTION="${1:-install}"
PLIST_DIR="$HOME/Library/LaunchAgents"
SRC_DIR="/Users/ctoti/Project/ClaudeCode/scripts/auto-monitor"
LOG_DIR="/Users/ctoti/Project/ClaudeCode/logs/auto-monitor"
DAYS=(mon tue wed thu fri)

case "$ACTION" in
  install)
    mkdir -p "$PLIST_DIR" "$LOG_DIR"
    chmod +x "$SRC_DIR/run-weekly-monitor.sh"
    chmod +x "$SRC_DIR/run-competitor-monitor.sh"
    chmod +x "$SRC_DIR/run-friday.sh"
    for day in "${DAYS[@]}"; do
      PLIST="com.ctoti.weekly-monitor.${day}.plist"
      if [[ -f "$SRC_DIR/$PLIST" ]]; then
        cp "$SRC_DIR/$PLIST" "$PLIST_DIR/"
        launchctl load "$PLIST_DIR/$PLIST" 2>/dev/null || true
        echo "Loaded $PLIST"
      fi
    done
    echo ""
    echo "Installed 5 agents:"
    echo "  Mon 09:00  /weekly-monitor agentic-ai"
    echo "  Tue 09:00  /weekly-monitor voice-ai"
    echo "  Wed 09:00  /weekly-monitor secure-ai"
    echo "  Thu 09:00  /monitor skt/kt-strategy"
    echo "  Fri 09:00  주간 종합 + 데이터 체크 (+ 월간/분기 조건부)"
    ;;
  uninstall)
    for day in "${DAYS[@]}"; do
      PLIST="com.ctoti.weekly-monitor.${day}.plist"
      launchctl unload "$PLIST_DIR/$PLIST" 2>/dev/null || true
      rm -f "$PLIST_DIR/$PLIST"
      echo "Unloaded $PLIST"
    done
    echo "Uninstalled all agents."
    ;;
  *)
    echo "Usage: $0 [install|uninstall]"
    exit 1
    ;;
esac
