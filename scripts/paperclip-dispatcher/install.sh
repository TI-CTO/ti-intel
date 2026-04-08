#!/bin/zsh
set -euo pipefail

ACTION="${1:-install}"
PLIST_DIR="$HOME/Library/LaunchAgents"
SRC_DIR="/Users/ctoti/Project/ClaudeCode/scripts/paperclip-dispatcher"
LOG_DIR="/Users/ctoti/Project/ClaudeCode/logs/dispatcher"
PLIST="com.ctoti.paperclip-dispatcher.plist"

case "$ACTION" in
  install)
    mkdir -p "$PLIST_DIR" "$LOG_DIR"
    chmod +x "$SRC_DIR/dispatcher.sh"
    cp "$SRC_DIR/$PLIST" "$PLIST_DIR/"
    launchctl bootout "gui/$(id -u)" "$PLIST_DIR/$PLIST" 2>/dev/null || true
    launchctl bootstrap "gui/$(id -u)" "$PLIST_DIR/$PLIST"
    echo "Installed: $PLIST (every 3 minutes)"
    echo "Pause:  touch ~/.paperclip-dispatcher-paused"
    echo "Resume: rm ~/.paperclip-dispatcher-paused"
    echo "Logs:   $LOG_DIR/"
    ;;
  uninstall)
    launchctl bootout "gui/$(id -u)" "$PLIST_DIR/$PLIST" 2>/dev/null || true
    rm -f "$PLIST_DIR/$PLIST"
    echo "Uninstalled: $PLIST"
    ;;
  *)
    echo "Usage: $0 [install|uninstall]"
    exit 1
    ;;
esac
