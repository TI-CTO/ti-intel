# research-hub

## 역할
Semantic Scholar / arXiv API를 통해 학술 논문을 수집·저장하고 MCP 도구로 노출하는 서버.
Tech Intelligence Platform Layer 1 구성 요소.

## MCP 도구 (5개)
- `search_papers(topic, query, since_year, limit)` — Semantic Scholar 검색 + DB 저장
- `get_trending_papers(topic, since, limit)` — 인용 수 기준 정렬 조회
- `get_paper_detail(external_id)` — 단일 논문 상세
- `get_paper_stats(topic, year, month)` — 월간 통계 조회
- `update_paper_stats(topic, year, month)` — 통계 재집계

## DB 테이블
- `papers` — 논문 메타데이터 (external_id UNIQUE, source, reliability_tag DEFAULT 'A')
- `paper_topics` — 논문-토픽 N:M (paper_id, topic_id, relevance)
- `paper_stats` — 월간 통계 (topic_id, stat_year, stat_month) UNIQUE

모든 테이블은 `topics(id)` FK를 통해 플랫폼 공유 topics 테이블과 연결됨.

## external_id 형식
- Semantic Scholar: `ss:{paperId}`
- arXiv (향후): `arxiv:{arxiv_id}`

## Supabase
- 프로젝트: tech-intel (ref: wzkmucknomctkyygciof)
- `.env`에 SUPABASE_URL, SUPABASE_KEY 필요

## 실행
```bash
uv run python -m research_hub.mcp_server
```
