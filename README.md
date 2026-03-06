# Tech Intelligence Platform

기술 인텔리전스를 위한 멀티 에이전트 플랫폼.
Claude Code + MCP 서버 + Supabase로 구성.

## Structure

```
projects/       MCP 서버 프로젝트 (4개)
outputs/        스킬/에이전트 산출물 (reports, weekly)
references/     리포트 참조 파일 (PDF, 사내 문서 등)
docs/           가이드·설계·템플릿 문서
scripts/        유틸리티 스크립트
.claude/        런타임 (skills, agents, hooks, rules)
```

## MCP Projects

| Project | Purpose | Status |
|---------|---------|--------|
| `intel-store` | 논문·특허·뉴스 통합 수집/검색 (14 도구) | Active |
| `trend-tracker` | 트렌드 스냅샷 시계열 비교 (5 도구) | Active |
| `design-system` | 마크다운 → PDF/PPTX 렌더링 (4 도구) | Active |
| `telco-factbook` | 통신사 재무 지표 조회 (CLI 전용) | Maintenance |

## Skills

| Skill | Command | Description |
|-------|---------|-------------|
| `wtis` | `/wtis` | 기술 투자 Go/No-Go 판정 (200점 채점) |
| `weekly-monitor` | `/weekly-monitor {domain}` | 주간 기술 동향 2단계 스캔 |
| `research-session` | `/research-session` | 자유 주제 구조화 리서치 |
| `discover` | `/discover` | 신기술/기회 탐색 |
| `monitor` | `/monitor` | 등록 토픽 변화 감지 |
| `report-pdf` | `/report-pdf` | 마크다운 → PDF 변환 |
| `slides` | `/slides` | 마크다운 → PPTX 변환 |
| `obsidian-bridge` | `/obsidian-bridge` | Obsidian 볼트 동기화 |
| `work-log` | `/work-log` | 업무일지 기록 |
| `new-project` | `/new-project` | 프로젝트 스캐폴딩 |

## Agents

| Agent | Role | Model |
|-------|------|-------|
| `research-deep` | 다중 소스 심층 리서치 | sonnet |
| `validator` | Black-box 독립 검증 | sonnet |
| `researcher` | 빠른 탐색/비교 | haiku |
| `reviewer` | 코드 리뷰 | sonnet |
| `implementer` | 코드 구현/수정 | sonnet |

## Quick Start

```bash
# 1. Clone & setup
git clone <your-repo-url> && cd ti-intel
cp .mcp.json.example .mcp.json

# 2. Install dependencies (each project)
cd projects/intel-store && ~/.local/bin/uv sync && cd ../..
cd projects/trend-tracker && ~/.local/bin/uv sync && cd ../..
cd projects/design-system && ~/.local/bin/uv sync && cd ../..

# 3. Configure .env for each project (Supabase credentials)
```

## Docs

| File | Description |
|------|-------------|
| `docs/guide-platform-overview.md` | 시스템 개요, 워크플로우, 설치 가이드 |
| `docs/guide-tool-reference.md` | 스킬/MCP 도구 상세 레퍼런스 |
| `docs/template-wtis-proposal.md` | WTIS 제안서 입력 템플릿 |
| `docs/template-wtis-report.md` | WTIS 리포트 출력 템플릿 |
| `docs/template-agent-design.md` | 에이전트 설계 프롬프트 |
