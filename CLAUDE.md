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
- `outputs/` — 스킬/에이전트 산출물 (reports/, summaries/)
- `references/` — 리포트 작성 시 참조한 로컬 파일 (PDF, 사내 보고서 등)
- `docs/` — 에이전트/스킬 설계 문서 (*.skill.md, *.agent.md)
- `.claude/` — Claude Code 런타임 (skills, agents, hooks, settings)

## CLAUDE.md Hierarchy
각 폴더에 자체 CLAUDE.md가 있을 수 있다.
서브프로젝트도 자체 CLAUDE.md를 가질 수 있다.
컨텍스트 흐름: root → folder → project (구체적일수록 우선)

## Obsidian Integration
Obsidian 볼트 경로: `$OBSIDIAN_VAULT_PATH` (settings.local.json에서 설정)
- 레퍼런스 (가이드/설계) → `10-지식베이스/`
- 목표 추적 → `20-Goals/`
- 리포트 (WTIS/리서치) → `30-Reports/`, 주간 → `30-Reports/weekly/`
- 작업 로그 → `40-DevLog/`
동기화: `/obsidian-bridge` 스킬 사용

### 지식베이스 파일 번호 규칙
`10-지식베이스/` 서브폴더 파일명에 2자리 번호 접두사(`{NN}-`)로 읽는 순서를 정렬에 반영:
- **01–09**: 온보딩 필수 (Quick Start, 개요)
- **10–19**: 아키텍처·상세 가이드
- **20–29**: 레퍼런스 (도구, 분류체계)
- `docs/` 원본은 번호 없이 `guide-`/`spec-` 접두사 유지, `/obsidian-bridge`가 변환
- 규칙 문서: `10-지식베이스/00-전체-개요.md` 하단, 매핑: `.claude/skills/obsidian-bridge/SKILL.md`

## Naming Conventions
| 유형 | 형식 | 예시 |
|------|------|------|
| 프로젝트 | lowercase-kebab-case | `auth-api-refactor` |
| 리서치 | YYYY-MM-DD_topic-slug.md | `2026-02-23_mcp-comparison.md` |
| 스킬 설계 | name.skill.md | `wtis.skill.md` |
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
  → projects/intel-store MCP     (논문/뉴스/특허 수집·검색)
  → projects/trend-tracker MCP   (트렌드 스냅샷)
  → projects/telco-factbook MCP  (경쟁사 IR 데이터)
  → projects/design-system MCP   (PDF/PPTX 렌더링)
```

## Agent Model Selection
- `haiku` — 빠른 탐색, 간단한 질문
- `sonnet` — 구현, 리뷰, 일반 작업
- `opus` — 복잡한 아키텍처 설계, 심층 분석

### 자동 에스컬레이션
작업 복잡도에 따라 사용자 확인 없이 에이전트를 자동 전환한다:
- 단순 파일/코드 탐색 → `researcher` (haiku)
- 웹 소스 종합, 비교 분석, 다중 출처 교차 검증 → `research-deep` (sonnet)으로 바로 투입

### 서브에이전트 병렬 실행 제한
- 5개+ research-deep 병렬 실행 시 MCP/WebSearch 리소스 경합으로 hang 발생
- **최대 3~4개 동시 실행**, 5개 이상이면 2배치로 분할
