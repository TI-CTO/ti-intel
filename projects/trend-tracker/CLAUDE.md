# trend-tracker

## Purpose
뉴스/웹 기술 트렌드를 누적 추적하는 MCP 서버.
정기 모니터링 데이터를 Supabase에 저장하고, 스냅샷 비교를 통해 변화를 감지한다.

## Architecture
- **MCP 서버**: `python -m trend_tracker.mcp_server`
- **DB**: Supabase (telco-factbook과 동일 인스턴스)
- **소비자**: Layer 2 스킬 (monitor, discover, research-session)

## MCP Tools
| 도구 | 설명 |
|------|------|
| `search_news` | 키워드/토픽으로 저장된 뉴스 검색 |
| `get_trend_timeline` | 토픽의 시계열 트렌드 데이터 조회 |
| `get_topic_summary` | 토픽의 최신 요약 조회 |
| `compare_snapshots` | 두 시점의 스냅샷을 비교하여 변화 감지 |
| `upsert_news` | 뉴스 항목 저장/갱신 |
| `upsert_snapshot` | 트렌드 스냅샷 저장 |
| `manage_watch_topics` | 모니터링 대상 토픽 CRUD |

## Dependencies
- `mcp>=1.0`
- `supabase>=2.0`
- `pydantic-settings>=2.0`

## Environment
`.env` 파일에 `SUPABASE_URL`, `SUPABASE_KEY` 필요.
