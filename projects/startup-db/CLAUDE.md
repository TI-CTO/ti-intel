# startup-db

## 역할
스타트업 데이터베이스 — 회사·투자·인물·관계·평가 데이터를 `su_` 접두사 테이블에 저장하고,
검색/조회/통계를 MCP 도구로 노출하는 서버.

## Architecture
- **DB**: Supabase PostgreSQL (intel-store와 동일 인스턴스, `su_` 네임스페이스)
- **스키마**: 12개 테이블 (companies, people, investors, funding_rounds, round_investors, acquisitions, company_people, company_relations, collections, collection_items, scores, signals, company_topics)
- **MCP 도구**: Phase 1 (검색/등록/펀딩/통계), Phase 2 (인물/관계/평가), Phase 3 (토픽/taxonomy)
- **Taxonomy**: `src/startup_db/taxonomy.py` — 3 L1 × 10 L2 × 25 L3 기술 분류

## MCP 도구 (Phase 1 — 6개)
| 도구 | 설명 |
|------|------|
| `search_companies` | 이름/카테고리/스테이지/지역/태그 필터 검색 |
| `get_company` | slug로 상세 조회 (라운드, 인물, 스코어 포함) |
| `upsert_company` | 스타트업 추가/업데이트 |
| `get_company_stats` | 카테고리별/스테이지별/지역별 통계 |
| `add_funding_round` | 펀딩 라운드 + 참여 투자자 기록 |
| `upsert_investor` | 투자자 추가/업데이트 |

## MCP 도구 (Phase 2 — 7개)
| 도구 | 설명 |
|------|------|
| `score_company` | 5차원 스코어 기록 (tech/market/team/fit/traction) |
| `add_company_relation` | 회사 간 관계 추가 (competitor/partner/customer 등) |
| `search_investors` | 투자자 검색 (이름/유형/국가 필터) |
| `get_investor_portfolio` | 투자자별 포트폴리오 조회 |
| `get_funding_stats` | 펀딩 집계 (연도/라운드/카테고리별) |
| `manage_collection` | 컬렉션 CRUD (워치리스트, 마켓맵) |
| `search_people` | 인물 검색 (이름/조직/역할 필터) |

## MCP 도구 (Phase 3 — 2개)
| 도구 | 설명 |
|------|------|
| `assign_company_topics` | L3 기술 토픽 할당 (유효성 검증 포함) |
| `remove_company_topics` | L3 기술 토픽 제거 |

## Obsidian 연동
- `scripts/export_to_obsidian.py` — 807건 회사 → Obsidian 노트 (wikilink 포함)
- 출력: `/Users/ctoti/Obsidian/Obsidian_Work/50-Startups/companies/`
- Dataview 인덱스: `50-Startups/_index.md`

## 데이터 보강 스크립트
- `scripts/backfill_relations.py` — sub_category+country 기반 competitor 자동 생성
- `scripts/backfill_enrichment.py` — 파생 필드 (one_liner, total_raised, growth_stage 등)
- `scripts/backfill_topics.py` — sub_category→L1 매핑으로 초기 토픽 할당

## DB 테이블 (`su_` 접두사)
- `su_companies` — 스타트업 마스터 (이름, 카테고리, 기술, one_liner, growth_stage, total_raised 등)
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
- `su_company_topics` — L3 기술 토픽 매핑 (M:N, taxonomy.py에서 L1/L2 파생)

## Environment
`.env` 파일에 필요:
- `SUPABASE_URL` — Supabase 프로젝트 URL
- `SUPABASE_KEY` — Supabase anon key

## 실행
```bash
uv run python -m startup_db.mcp_server
```
