#!/bin/bash
# PostToolUse hook: Auto-format Python files after edits
# Only runs on .py files

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | grep -o '"file_path":"[^"]*"' | head -1 | cut -d'"' -f4)

if [[ "$FILE_PATH" == *.py ]]; then
  if command -v ruff &> /dev/null; then
    ruff format "$FILE_PATH" 2>/dev/null
  fi
fi

exit 0
