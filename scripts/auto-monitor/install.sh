#!/bin/zsh
# launchd plist 설치/제거 스크립트
# Usage: install.sh [install|uninstall]
# 월(순차 4단계) + 금(종합) = 2개 에이전트 등록

set -euo pipefail

ACTION="${1:-install}"
PLIST_DIR="$HOME/Library/LaunchAgents"
SRC_DIR="/Users/ctoti/Project/ClaudeCode/scripts/auto-monitor"
LOG_DIR="/Users/ctoti/Project/ClaudeCode/logs/auto-monitor"
DAYS=(mon fri)
OLD_DAYS=(tue wed thu)

case "$ACTION" in
  install)
    mkdir -p "$PLIST_DIR" "$LOG_DIR"
    chmod +x "$SRC_DIR/run-monday.sh"
    chmod +x "$SRC_DIR/run-friday.sh"

    # 기존 화/수/목 에이전트 제거
    for day in "${OLD_DAYS[@]}"; do
      PLIST="com.ctoti.weekly-monitor.${day}.plist"
      launchctl unload "$PLIST_DIR/$PLIST" 2>/dev/null || true
      rm -f "$PLIST_DIR/$PLIST"
    done

    for day in "${DAYS[@]}"; do
      PLIST="com.ctoti.weekly-monitor.${day}.plist"
      if [[ -f "$SRC_DIR/$PLIST" ]]; then
        cp "$SRC_DIR/$PLIST" "$PLIST_DIR/"
        launchctl unload "$PLIST_DIR/$PLIST" 2>/dev/null || true
        launchctl load "$PLIST_DIR/$PLIST"
        echo "Loaded $PLIST"
      fi
    done
    echo ""
    echo "Installed 2 agents:"
    echo "  Mon 07:30  순차: agentic-ai → voice-ai → secure-ai → 경쟁사 브로드스캔"
    echo "  Fri 09:00  주간 종합 + 데이터 체크 (+ 월간/분기 조건부)"
    ;;
  uninstall)
    for day in "${DAYS[@]}" "${OLD_DAYS[@]}"; do
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
