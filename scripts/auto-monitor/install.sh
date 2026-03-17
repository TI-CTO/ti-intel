#!/bin/zsh
# launchd plist 설치/제거 스크립트
# Usage: install.sh [install|uninstall]

set -euo pipefail

ACTION="${1:-install}"
PLIST_DIR="$HOME/Library/LaunchAgents"
SRC_DIR="/Users/ctoti/Project/ClaudeCode/scripts/auto-monitor"
LOG_DIR="/Users/ctoti/Project/ClaudeCode/logs/auto-monitor"
DAYS=(mon tue wed)

case "$ACTION" in
  install)
    mkdir -p "$PLIST_DIR" "$LOG_DIR"
    chmod +x "$SRC_DIR/run-weekly-monitor.sh"
    for day in "${DAYS[@]}"; do
      PLIST="com.ctoti.weekly-monitor.${day}.plist"
      cp "$SRC_DIR/$PLIST" "$PLIST_DIR/"
      launchctl load "$PLIST_DIR/$PLIST" 2>/dev/null || true
      echo "Loaded $PLIST"
    done
    echo "Installed 3 weekly-monitor agents. Schedule: Mon 09:00, Tue 09:00, Wed 09:00"
    ;;
  uninstall)
    for day in "${DAYS[@]}"; do
      PLIST="com.ctoti.weekly-monitor.${day}.plist"
      launchctl unload "$PLIST_DIR/$PLIST" 2>/dev/null || true
      rm -f "$PLIST_DIR/$PLIST"
      echo "Unloaded $PLIST"
    done
    echo "Uninstalled all weekly-monitor agents."
    ;;
  *)
    echo "Usage: $0 [install|uninstall]"
    exit 1
    ;;
esac
