#!/bin/bash
# PreToolUse hook: Block writes that contain potential secrets
# Exit code 2 = block the tool use

# Read the tool input from stdin
INPUT=$(cat)

# Check for common secret patterns
if echo "$INPUT" | grep -qiE '(api[_-]?key|secret[_-]?key|password|token|credentials)\s*[:=]\s*["\x27][^"\x27]{8,}'; then
  echo "BLOCKED: Potential secret detected in file content. Review before writing."
  exit 2
fi

exit 0
