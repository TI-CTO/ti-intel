# design-system

멀티 포맷 디자인 시스템. 디자인 토큰 기반으로 마크다운 콘텐츠를 프레젠테이션(PPTX), HTML, 웹페이지 등으로 변환한다.

## Purpose
- W3C DTCG 형식의 디자인 토큰으로 브랜딩/스타일 관리
- 테마 선택/조합으로 다양한 디자인 적용
- MCP 서버를 통해 Claude Code 스킬에서 렌더링 호출

## Architecture
```
Tokens (JSON) → Theme (base + override) → Renderer (pptx/html)
                                                ↑
                                           MCP Server ← Claude Code
```

## Key Files
- `src/design_system/tokens/` — W3C DTCG 형식 디자인 토큰 (JSON)
- `src/design_system/parsers/` — 마크다운 → 슬라이드 구조 파싱
- `src/design_system/renderers/` — 포맷별 렌더러 (PPTX, HTML 등)
- `src/design_system/mcp_server.py` — MCP 도구 서버
- `src/design_system/token_loader.py` — 토큰 로딩 + 테마 병합
- `src/design_system/models.py` — Pydantic 데이터 모델

## Supported Formats
- **PPTX** (Phase 1) — python-pptx 기반
- **HTML slides** (Phase 2, 예정) — Marp/Slidev
- **Web** (Phase 3, 예정) — Astro/Nuxt

## Testing
```bash
uv run pytest
uv run ruff check . && uv run ruff format .
```
