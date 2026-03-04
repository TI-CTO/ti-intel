# intel-store

## 역할
통합 인텔리전스 저장소 — 뉴스·논문·특허·기업발언·리포트를 단일 `intel_items` 테이블에 저장하고, 벡터+키워드 하이브리드 검색(RRF)을 MCP 도구로 노출하는 서버.

## Architecture
- **DB**: Supabase PostgreSQL + pgvector (HNSW 인덱스)
- **임베딩**: multilingual-e5-large (로컬, 1024차원, 한영 다국어)
- **전문검색**: tsvector + GIN 인덱스 (simple config)
- **하이브리드 검색**: Reciprocal Rank Fusion (k=60) — keyword + semantic 결과 병합
- **수집기**: Semantic Scholar, arXiv, Google Patents (SerpAPI), Tavily, GDELT, Naver News

## MCP 도구 (13개)
| 도구 | 설명 |
|------|------|
| `search_intel` | 통합 검색 (keyword/semantic/hybrid with RRF) |
| `find_similar` | 유사 아이템 탐색 (중복/관련성) |
| `get_weekly_diff` | 이번 주 vs 지난 주 비교 |
| `upsert_items` | 아이템 저장 (content_hash 중복 체크) |
| `get_item_detail` | 단건 상세 조회 |
| `link_topics` | 토픽 연결 |
| `link_relation` | 아이템 간 관계 생성 |
| `collect_papers` | Semantic Scholar → 수집+저장 |
| `collect_arxiv` | arXiv → 수집+저장 (Semantic Scholar 대안) |
| `collect_patents` | Google Patents (SerpAPI) → 수집+저장 |
| `collect_news` | Tavily/GDELT/Naver → 수집+저장 |
| `collect_all` | 전체 소스 일괄 수집 (papers+arxiv+patents+news) |
| `get_intel_stats` | 실시간 집계 통계 |

## 수집기
| 수집기 | 소스 | 유형 | Rate Limit |
|--------|------|------|------------|
| Semantic Scholar | 학술 논문 | paper | 1 req/sec |
| arXiv | 학술 논문 (프리프린트) | paper | 3초 간격 |
| Google Patents (SerpAPI) | 글로벌 특허 | patent | 250 req/월 (free) |
| Tavily | AI 최적화 뉴스 | news | 1,000 req/월 (free) |
| GDELT | 글로벌 뉴스 | news | 무제한 |
| Naver News | 한국어 뉴스 | news | API 키 필요 |

## DB 테이블
- `intel_items` — 통합 저장 (벡터 1024차원 + tsvector + JSONB metadata)
- `intel_item_topics` — 토픽 연결 N:M (relevance, assigned_by)
- `intel_item_relations` — 아이템 간 관계 (cites/mentions/same_event/updates/contradicts)

## content_hash 규칙
- `SHA-256(title + abstract[:200])` — 정확 중복 방지
- `embedding` 코사인 유사도 — 의미 중복 탐지

## 임베딩 텍스트 구성
- passage: `"passage: " + title + ". " + abstract`
- query: `"query: " + search_text`
- multilingual-e5-large는 "query:"/"passage:" 접두사로 비대칭 검색

## Environment
`.env` 파일에 필요:
- `SUPABASE_URL` — Supabase 프로젝트 URL
- `SUPABASE_KEY` — Supabase anon key
- `TAVILY_API_KEY` — Tavily 검색 API 키 (optional)
- `NAVER_CLIENT_ID` — Naver 개발자 Client ID (optional, 한국어 뉴스)
- `NAVER_CLIENT_SECRET` — Naver 개발자 Client Secret (optional, 한국어 뉴스)
- `SERPAPI_API_KEY` — SerpAPI 키 (optional, Google Patents 특허 수집)

## 실행
```bash
uv run python -m intel_store.mcp_server
```
