# ClaudeCode Workspace — Global Context

## Identity
ctoti의 Claude Code 개발/리서치 워크스페이스.
프로젝트, 리서치, 에이전트/스킬 설계가 이 루트 아래에 존재한다.

## Language & Communication
- 대화/설명: 한국어
- 코드, 변수명, 커밋 메시지, docstring: 영어
- 파일명: 영어, lowercase-kebab-case 또는 날짜 접두사

## Technology Stack
- Python 3.11+ with `uv` (pip, conda 사용 금지)
- Git for version control
- VSCode as primary editor
- Anthropic SDK for agent/API work
- MCP protocol for tool integrations

## Coding Conventions
상세 규칙은 `.claude/rules/`에 경로별로 스코핑되어 있음:
- `python-style.md` — Python 컨벤션 (`projects/**/*.py`)
- `testing.md` — pytest 규칙 (`tests/**/*.py`)
- `commit-message.md` — 커밋 메시지 컨벤션

## Workspace Structure
- `projects/` — 활성 코드 프로젝트
- `research/` — 리서치 산출물 (sessions, summaries, references)
- `docs/` — 에이전트/스킬 설계 문서 (*.skill.md, *.agent.md)
- `.claude/` — Claude Code 런타임 (skills, agents, hooks, settings)

## CLAUDE.md Hierarchy
각 폴더에 자체 CLAUDE.md가 있을 수 있다.
서브프로젝트도 자체 CLAUDE.md를 가질 수 있다.
컨텍스트 흐름: root → folder → project (구체적일수록 우선)

## Obsidian Integration
Obsidian 볼트 경로: `/Users/ctoti/Obsidian/Obsidian_Work/`
- 프로젝트 → `10-Projects/`
- 구현 기록 → `60-ClaudeCode/Implementations/`
- 리서치 세션 → `70-Research/Sessions/`
동기화: `/obsidian-bridge` 스킬 사용

## Naming Conventions
| 유형 | 형식 | 예시 |
|------|------|------|
| 프로젝트 | lowercase-kebab-case | `auth-api-refactor` |
| 리서치 | YYYY-MM-DD_topic-slug.md | `2026-02-23_mcp-comparison.md` |
| 스킬 설계 | name.skill.md | `wtis-v2.skill.md` |
| 에이전트 설계 | name.agent.md | `code-reviewer.agent.md` |

## Multi-Agent Architecture
이 워크스페이스는 단일 루트 아래 멀티 에이전트 시스템을 운영한다.

### 원칙
- **프로젝트 = MCP 서버**: 각 `projects/` 하위 프로젝트는 독립 MCP 서버로 구현. `.mcp.json`에 등록하면 모든 스킬/에이전트가 해당 데이터에 접근 가능.
- **프로젝트 격리**: 각 프로젝트는 자체 `pyproject.toml`, `.venv`, `CLAUDE.md`를 가짐. 프로젝트 간 Python import 의존성 없음 — MCP 프로토콜로만 통신.
- **스킬 = 오케스트레이터**: `.claude/skills/`의 스킬이 여러 MCP 서버를 조합하는 워크플로우 역할.
- **CLAUDE.md 계층으로 컨텍스트 관리**: 루트는 전역 규칙만, 프로젝트 CLAUDE.md는 도메인 지식만.

### 협력 구조
```
스킬 (오케스트레이터)
  → projects/telco-factbook MCP  (경쟁사 데이터)
  → projects/trend-tracker MCP   (기술 트렌드)
  → projects/startup-intel MCP   (스타트업 정보)
  → 스킬: pptx-generator         (장표 생성)
```

## Agent Model Selection
- `haiku` — 빠른 탐색, 간단한 질문
- `sonnet` — 구현, 리뷰, 일반 작업
- `opus` — 복잡한 아키텍처 설계, 심층 분석
