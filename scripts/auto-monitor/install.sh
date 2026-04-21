#!/bin/zsh
# launchd plist 설치/제거 스크립트
# Usage: install.sh [install|uninstall]
# 도메인별 개별 스케줄 (4개) + 금요일 종합 (1개) = 5개 에이전트 등록

set -euo pipefail

ACTION="${1:-install}"
PLIST_DIR="$HOME/Library/LaunchAgents"
SRC_DIR="/Users/ctoti/Project/ClaudeCode/scripts/auto-monitor"
LOG_DIR="/Users/ctoti/Project/ClaudeCode/logs/auto-monitor"

# 현행 에이전트
AGENTS=(voice-ai secure-ai competitor agentic-ai fri health-check)

# 이전 에이전트 (정리 대상)
OLD_AGENTS=(mon tue wed thu)

case "$ACTION" in
  install)
    mkdir -p "$PLIST_DIR" "$LOG_DIR"
    chmod +x "$SRC_DIR/run-domain.sh"
    chmod +x "$SRC_DIR/run-friday.sh"
    chmod +x "$SRC_DIR/health-check.sh"

    # 이전 에이전트 제거
    for old in "${OLD_AGENTS[@]}"; do
      PLIST="com.ctoti.weekly-monitor.${old}.plist"
      launchctl bootout "gui/$(id -u)" "$PLIST_DIR/$PLIST" 2>/dev/null || true
      rm -f "$PLIST_DIR/$PLIST"
    done

    for agent in "${AGENTS[@]}"; do
      PLIST="com.ctoti.weekly-monitor.${agent}.plist"
      if [[ -f "$SRC_DIR/$PLIST" ]]; then
        cp "$SRC_DIR/$PLIST" "$PLIST_DIR/"
        launchctl bootout "gui/$(id -u)" "$PLIST_DIR/$PLIST" 2>/dev/null || true
        launchctl bootstrap "gui/$(id -u)" "$PLIST_DIR/$PLIST"
        echo "Loaded $PLIST"
      fi
    done
    echo ""
    echo "Installed 6 agents:"
    echo "  Mon 08:30  voice-ai"
    echo "  Mon 12:30  secure-ai"
    echo "  Mon 14:00  competitor (skt/kt strategy)"
    echo "  Tue 08:30  agentic-ai"
    echo "  Fri 09:00  주간 종합 + 데이터 체크 (+ 월간/분기 조건부)"
    echo "  Daily 07:00  health-check (launchctl 7 agents + Gmail alert)"
    ;;
  uninstall)
    for agent in "${AGENTS[@]}" "${OLD_AGENTS[@]}"; do
      PLIST="com.ctoti.weekly-monitor.${agent}.plist"
      launchctl bootout "gui/$(id -u)" "$PLIST_DIR/$PLIST" 2>/dev/null || true
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
