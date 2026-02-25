# outputs — 스킬/에이전트 산출물

스킬과 에이전트가 생성하는 분석 리포트, 요약본.

## Structure
- `reports/` — 개별 실행 결과 (YYYY-MM-DD_topic-slug.md)
- `summaries/` — 여러 리포트를 종합한 정리 (summary_topic-slug.md)

## Rules
- 같은 주제 리포트가 3개 이상 쌓이면 `summaries/`에 종합 정리 작성
- 유의미한 발견은 `/obsidian-bridge`로 Obsidian 볼트에 동기화
- 외부 소스를 인용할 때는 리포트 본문에 각주로 출처(URL 또는 파일명) 기록

## 파일 생성 주체
| 스킬/에이전트 | 저장 위치 |
|--------------|-----------|
| `/wtis` | `outputs/reports/YYYY-MM-DD_wtis-{slug}-{step}.md` |
| `/research-session` | `outputs/reports/YYYY-MM-DD_{topic-slug}.md` |
| `/discover` | `outputs/reports/YYYY-MM-DD_discover-{domain}.md` |
| `/monitor` | `outputs/reports/YYYY-MM-DD_monitor-{topic}.md` |
| `research-deep` agent | `outputs/reports/YYYY-MM-DD_deep-{slug}.md` |
