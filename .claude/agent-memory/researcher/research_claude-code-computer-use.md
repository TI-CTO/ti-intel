---
name: Claude Code CLI Computer Use Support
description: Computer use is Desktop-only feature on macOS, not available in terminal/CLI
type: reference
---

## Research Question
Does Claude Code CLI (terminal version) support computer use? Is there a flag to enable it?

## Key Finding
**Computer Use is Desktop-only and NOT available in Claude Code CLI/terminal.**

Computer use was introduced March 2026 as a new Anthropic feature, but it is exclusive to:
- Claude Desktop app (macOS only, Windows coming soon)
- Claude Cowork (web desktop control app)

The terminal/CLI version of Claude Code does NOT have computer use capabilities, and there is:
- No `--computer-use` flag
- No setting in `~/.claude/settings.json` to enable it
- No way to activate it in the CLI

## Evidence
1. **Official Desktop Docs** ([https://code.claude.com/docs/en/desktop](https://code.claude.com/docs/en/desktop)): "Desktop adds these capabilities on top of the standard Claude Code experience: Computer use to open apps and control your screen on macOS" — Computer use listed as Desktop-exclusive feature.

2. **Anthropic Blog** ([https://claude.com/blog/dispatch-and-computer-use](https://claude.com/blog/dispatch-and-computer-use)): "For now, computer use is supported on macOS only, and you'll need to enable it in the desktop app settings" — Explicitly says "desktop app"

3. **Official CLI Reference** ([https://code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference)): Complete CLI flags list includes `--chrome` for browser integration but NO computer use flag. `--chrome` is the closest terminal capability for web automation.

4. **Multiple third-party sources** confirm computer use is macOS Desktop app feature, with Windows support rolling out later. Terminal not mentioned as support surface.

## Why This Matters
- **For terminal users**: Claude Code CLI can use `--chrome` flag for browser automation instead
- **For desktop users**: Computer use allows Claude to click, type, scroll, and control macOS applications
- **For remote/headless**: Remote Control (`--remote-control`) is the terminal-compatible alternative for off-machine tasks

## Related Flags (Terminal Alternatives)
- `--chrome`: Enable Chrome browser integration for web automation/testing (terminal-compatible)
- `--remote-control`: Start interactive session controllable from claude.ai or Claude app
- Standard tools: Bash, Read, Edit work in terminal for command-line automation

