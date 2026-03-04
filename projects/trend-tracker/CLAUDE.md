# trend-tracker

## Purpose
트렌드 스냅샷 비교와 모니터링 토픽 관리 전용 MCP 서버.
뉴스/논문/특허 검색·수집·저장은 **intel-store**로 이관됨.

## Architecture
- **MCP 서버**: `python -m trend_tracker.mcp_server`
- **DB**: Supabase (telco-factbook과 동일 인스턴스)
- **소비자**: Layer 2 스킬 (monitor, discover, research-session)

## MCP Tools
| 도구 | 설명 |
|------|------|
| `get_trend_timeline` | 토픽의 시계열 트렌드 데이터 조회 |
| `get_topic_summary` | 토픽의 최신 요약 조회 |
| `compare_snapshots` | 두 시점의 스냅샷을 비교하여 변화 감지 |
| `upsert_snapshot` | 트렌드 스냅샷 저장 |
| `manage_watch_topics` | 모니터링 대상 토픽 CRUD |

> **Deprecated** (intel-store로 이관): `search_news`, `upsert_news`, `collect_news`

## Dependencies
- `mcp>=1.0`
- `supabase>=2.0`
- `pydantic-settings>=2.0`

## Environment
`.env` 파일에 `SUPABASE_URL`, `SUPABASE_KEY` 필요.
