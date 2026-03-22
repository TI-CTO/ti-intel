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

### 지식베이스 폴더 구조
`10-지식베이스/` 용도별 3폴더 체계:
- `시작하기/` — 온보딩 (퀵스타트, 시스템 개요)
- `워크플로우/` — 실무 참조 (WTIS 2-Tier, 스킬 체이닝, 대시보드)
- `레퍼런스/` — 필요 시 조회 (분류체계, 도구, UI 스펙)
- `docs/` 원본은 번호 없이 `guide-`/`spec-` 접두사 유지, `/obsidian-bridge`가 변환
- 매핑 테이블: `.claude/skills/obsidian-bridge/SKILL.md`

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

## Skills & Agents 요약

> 상세: `docs/guide-tool-reference.md`

### 스킬 (사용자 호출, `/스킬명`)

| 스킬 | 용도 |
|------|------|
| `wtis` | 기술 평가 — standard(Go/No-Go) / full(종합 기술 전략 제안서) |
| `weekly-monitor` | 주간 기술 동향 (L1 도메인별 L3 스캔) |
| `monitor` | 등록 토픽 정기 모니터링 |
| `discover` | 신기술/기회 탐색 |
| `research-session` | 자유 주제 심층 리서치 |
| `strategy-options` | Build/Buy/Partner 전략 비교 (독립 실행 시) |
| `biz-case` | ROI 시나리오 분석 (독립 실행 시) |
| `startup-scout` | 스타트업 후보 발굴 |
| `startup-analyst` | 특정 기업 심층 분석 |
| `report-pdf` | 마크다운 → PDF 변환 |
| `slides` | 마크다운 → PPTX 변환 |
| `obsidian-bridge` | Obsidian 볼트 동기화 |
| `work-log` | 업무일지 기록 |
| `dashboard-implement` | 대시보드 구현 + 자동 검증 |

### 에이전트 (자동 실행, 스킬이 내부 호출)

| 에이전트 | 역할 | 모델 |
|----------|------|------|
| `research-deep` | 다중 소스 심층 리서치 | sonnet |
| `fact-checker` | 외부 사실 검증 (Devil's Advocate) | sonnet |
| `validator` | 내부 일관성 검증 (Black-box) | sonnet |
| `researcher` | 빠른 탐색/비교 | haiku |
| `reviewer` | 코드 리뷰 | sonnet |
| `implementer` | 코드 구현/수정 | sonnet |

## Agent Model Selection
- `haiku` — 빠른 탐색, 간단한 질문
- `sonnet` — 구현, 리뷰, 일반 작업
- `opus` — 복잡한 아키텍처 설계, 심층 분석

### 자동 에스컬레이션
작업 복잡도에 따라 사용자 확인 없이 에이전트를 자동 전환한다:
- 단순 파일/코드 탐색 → `researcher` (haiku)
- 웹 소스 종합, 비교 분석, 다중 출처 교차 검증 → `research-deep` (sonnet)으로 바로 투입
- 핵심 주장 팩트 체크 (최초/유일 등 강한 주장) → `fact-checker` (sonnet)로 반례 탐색

### 서브에이전트 병렬 실행 제한
- 5개+ research-deep 병렬 실행 시 MCP/WebSearch 리소스 경합으로 hang 발생
- **최대 3~4개 동시 실행**, 5개 이상이면 2배치로 분할
