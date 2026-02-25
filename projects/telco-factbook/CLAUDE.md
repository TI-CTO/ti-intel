# telco-factbook

통신사(SKT, KT) IR 실적 자료를 수집하여 Supabase에 저장하는 팩트북 시스템.

## Purpose
- 경쟁사 IR 사이트에서 Excel 재무제표를 자동 수집
- 파싱하여 구조화된 재무 지표로 Supabase에 저장
- MCP 서버를 통해 Claude Code/WTIS에서 조회

## Architecture
```
IR Site → Scraper → Excel Parser → Supabase (PostgreSQL)
                                        ↑
                                   MCP Server ← Claude Code
```

## Key Files
- `src/telco_factbook/scrapers/` — 사이트별 스크래퍼 (KT REST API, SKT AJAX)
- `src/telco_factbook/parsers/` — Excel 파싱 로직
- `src/telco_factbook/db/` — Supabase 클라이언트 + Repository
- `src/telco_factbook/mcp_server.py` — MCP 도구 서버
- `src/telco_factbook/cli.py` — CLI 엔트리포인트

## Environment
`.env` 파일에 Supabase 인증 정보 필요:
```
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=eyJ...
```

## Testing
```bash
uv run pytest
uv run ruff check . && uv run ruff format .
```
