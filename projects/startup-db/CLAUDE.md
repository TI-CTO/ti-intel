# startup-db

## 역할
스타트업 데이터베이스 — 회사·투자·인물·관계·평가 데이터를 `su_` 접두사 테이블에 저장하고,
검색/조회/통계를 MCP 도구로 노출하는 서버.

## Architecture
- **DB**: Supabase PostgreSQL (intel-store와 동일 인스턴스, `su_` 네임스페이스)
- **스키마**: 11개 테이블 (companies, people, investors, funding_rounds, round_investors, acquisitions, company_people, company_relations, collections, collection_items, scores, signals)
- **MCP 도구**: Phase 1 (검색/등록/펀딩/통계), Phase 2 (인물/관계/평가), Phase 3 (intel-store 연동)

## MCP 도구 (Phase 1 — 6개)
| 도구 | 설명 |
|------|------|
| `search_companies` | 이름/카테고리/스테이지/지역/태그 필터 검색 |
| `get_company` | slug로 상세 조회 (라운드, 인물, 스코어 포함) |
| `upsert_company` | 스타트업 추가/업데이트 |
| `get_company_stats` | 카테고리별/스테이지별/지역별 통계 |
| `add_funding_round` | 펀딩 라운드 + 참여 투자자 기록 |
| `upsert_investor` | 투자자 추가/업데이트 |

## DB 테이블 (`su_` 접두사)
- `su_companies` — 스타트업 마스터 (이름, 카테고리, 기술, 제품)
- `su_people` — 인물 (창업자, 임원)
- `su_investors` — 투자자 (VC, 엔젤, CVC)
- `su_funding_rounds` — 펀딩 라운드 (라운드별 독립 레코드)
- `su_round_investors` — 라운드별 참여 투자자 (N:M)
- `su_acquisitions` — 인수합병
- `su_company_people` — 인물-회사 관계 (역할 기반)
- `su_company_relations` — 회사 간 관계 (경쟁/파트너/고객)
- `su_collections` — 컬렉션 (워치리스트, 마켓맵)
- `su_collection_items` — 컬렉션 소속 회사
- `su_scores` — 다차원 평가 (기술/시장/팀/적합도/견인력)
- `su_signals` — intel-store 시그널 연결

## Environment
`.env` 파일에 필요:
- `SUPABASE_URL` — Supabase 프로젝트 URL
- `SUPABASE_KEY` — Supabase anon key

## 실행
```bash
uv run python -m startup_db.mcp_server
```
