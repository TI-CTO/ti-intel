# patent-intel

## 역할
USPTO PatentsView API를 통해 특허를 수집·저장하고 MCP 도구로 노출하는 서버.
Tech Intelligence Platform Layer 1 구성 요소.

## MCP 도구 (5개)
- `search_patents(topic, query, since_year, limit)` — USPTO 검색 + DB 저장
- `get_recent_patents(topic, since, limit)` — 출원일 기준 최신 특허 조회
- `get_patent_detail(external_id)` — 단일 특허 상세
- `get_patent_stats(topic, year, quarter)` — 분기 통계 조회
- `update_patent_stats(topic, year, quarter)` — 통계 재집계

## DB 테이블
- `patents` — 특허 메타데이터 (external_id UNIQUE, source, applicant, ipc_codes JSONB)
- `patent_topics` — 특허-토픽 N:M (patent_id, topic_id, relevance)
- `patent_stats` — 분기 통계 (topic_id, stat_year, stat_quarter) UNIQUE

모든 테이블은 `topics(id)` FK를 통해 플랫폼 공유 topics 테이블과 연결됨.

## external_id 형식
- USPTO: `uspto:{patent_number}` (예: `uspto:US11234567B2`)
- EPO (향후): `epo:{publication_number}`

## 데이터 소스
- **USPTO PatentsView API** — https://api.patentsview.org/
  - 무료, API 키 불필요
  - 1976년 이후 미국 특허 커버
  - Rate limit: ~45 req/min

## Supabase
- 프로젝트: tech-intel (ref: wzkmucknomctkyygciof)
- `.env`에 SUPABASE_URL, SUPABASE_KEY 필요

## 실행
```bash
uv run python -m patent_intel.mcp_server
```
