# ClaudeCode Workspace

Claude Code를 활용한 개발/리서치 통합 워크스페이스.

## Structure

```
projects/     활성 코드 프로젝트
research/     리서치 산출물 (sessions, summaries, references)
docs/         에이전트/스킬 설계 문서
.claude/      런타임 (skills, agents, hooks, settings)
```

## Agents

| Agent | Purpose | Model |
|-------|---------|-------|
| `researcher` | 읽기 전용 리서치 | haiku |
| `implementer` | 코드 구현 | sonnet |
| `reviewer` | 코드 리뷰 | sonnet |

## Skills

| Skill | Command | Description |
|-------|---------|-------------|
| `new-project` | `/new-project` | 새 프로젝트 스캐폴딩 |
| `research-session` | `/research-session` | 구조화된 리서치 세션 |
| `obsidian-bridge` | `/obsidian-bridge` | Obsidian 볼트 동기화 |
| `wtis` | `/wtis` | LG U+ 기술전략 인텔리전스 |

## Quick Start

```bash
# 새 프로젝트 생성
/new-project my-app

# 리서치 시작
/research-session "Vector DB comparison"

# WTIS 분석
/wtis standard SecureAI

# Obsidian으로 동기화
/obsidian-bridge research/sessions/2026-02-23_vector-db.md research
```

## Obsidian Integration

Vault: `/Users/ctoti/Obsidian/Obsidian_Work/`

| Workspace | Vault |
|-----------|-------|
| research/sessions/ | 70-Research/Sessions/ |
| projects/ logs | 60-ClaudeCode/Implementations/ |
| Q&A sessions | 80-QA-Log/YYYY/MM/ |
