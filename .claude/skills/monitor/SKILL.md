---
name: monitor
description: "정기 기술 모니터링. 등록된 토픽(watch_topics)을 스캔하고 이전 스냅샷과 비교하여 변화를 감지한다."
user-invokable: true
argument-hint: "[topic-slug | all]"
---

# Monitor — 기술 모니터링 스킬

등록된 토픽 목록(watch_topics)을 스캔하고, 이전 스냅샷과 비교하여 변화를 감지·보고한다.
변화의 중요도에 따라 🟢 유지 / 🟡 주목 / 🔴 긴급으로 분류한다.

## 빠른 시작

```
/monitor              → 모든 watch_topics 스캔 (8개 토픽)
/monitor ai-network   → 특정 토픽만 스캔
```

**실행 중:**
```
[1/8] ai-network 스캔 중...  [2/8] 6g 스캔 중...  ...
```

**완료 시:**
```
=== Monitor Run: 2026-02-26 ===
총 스캔: 8개 토픽
🟢 변화 없음: 6개
🟡 주목:      2개 — ai-network, llm-telecom
🔴 긴급:      0개

저장된 보고서:
- outputs/reports/2026-02-26_monitor-ai-network.md
- outputs/reports/2026-02-26_monitor-llm-telecom.md
```

---

## Arguments
- (없음): 모든 watch_topics 스캔
- `[topic-slug]`: 특정 토픽만 스캔 (예: `ai-network`, `6g`)

## Process

### Phase 1: 토픽 목록 로드
1. `trend-tracker`: `manage_watch_topics(action="list")` 호출
2. 스캔 대상 토픽 목록 확인
3. 특정 토픽 지정 시 해당 토픽만 처리

### Phase 2: 토픽별 데이터 수집
각 토픽에 대해 다음을 수집한다 (MCP 도구 호출):

**뉴스/트렌드:**
- `trend-tracker`: `search_news(topic=slug, query=slug, limit=20)` — 최신 뉴스
- `trend-tracker`: `get_topic_summary(topic=slug)` — 현재 상태 요약

**학술/특허 (중요도 높은 토픽에만):**
- `research-hub`: `get_trending_papers(topic=slug, since=last_30_days, limit=10)`
- `patent-intel`: `get_recent_patents(topic=slug, limit=10)`

### Phase 3: 스냅샷 비교
- `trend-tracker`: `compare_snapshots(topic=slug)` — 이전 스냅샷과 비교
- 변화 없음 / 소폭 변화 / 유의미한 변화 판정

### Phase 4: 변화 분류 및 중요도 판정
수집 데이터 + 스냅샷 비교 결과를 바탕으로 분류:

```
🟢 변화 없음:
  - 신규 뉴스 없음 또는 기존 동향과 동일
  - 처리: 빈 스냅샷 저장 + 로그

🟡 주목할 변화:
  - 주요 기업 발표, 신규 표준 제안, 주목할 논문
  - 처리: 요약 보고서 생성 + 스냅샷 저장

🔴 긴급 변화:
  - 경쟁사 출시, 규제 변경, 기술 돌파구
  - 처리: 상세 보고서 생성 + 에스컬레이션 알림
```

### Phase 5: 결과 저장
각 토픽별:
1. `trend-tracker`: `upsert_snapshot(...)` — 새 스냅샷 DB 저장
2. 🟡/🔴 토픽에 대해 파일 저장:
   `/Users/ctoti/Project/ClaudeCode/outputs/reports/{YYYY-MM-DD}_monitor-{topic-slug}.md`
3. 종합 요약 출력

## Output Format

### 토픽별 보고서 (🟡/🔴인 경우)
```markdown
---
topic: {topic-slug}
date: {YYYY-MM-DD}
skill: monitor
signal_level: warning | critical
previous_snapshot: {date}
---

# Monitor Report: {Topic Display Name}

## 변화 요약
> (핵심 변화 2-3줄)

## 신규 신호
| 신호 | 출처 | 중요도 | 날짜 |
|------|------|--------|------|

## 이전 대비 변화
- (이전 상태 vs 현재 상태)

## 다음 모니터링 권고
- 일정: (다음 스캔 권고 시점)
- 심화 조사 필요 여부: yes | no

## References
| # | 출처명 | URL | 발행일 | 접근일 | 신뢰도 |
|---|--------|-----|--------|--------|--------|
```

### 종합 요약 (터미널 출력)
```
=== Monitor Run: {YYYY-MM-DD} ===

총 스캔: N개 토픽
🟢 변화 없음: N개
🟡 주목:      N개 — {topic1}, {topic2}
🔴 긴급:      N개 — {topic3}

저장된 보고서:
- {file_path1} (🟡 ai-network)
- {file_path2} (🔴 6g)
```

## Error Handling
- MCP 도구 오류 시: 해당 토픽 스킵 + 오류 로그 → 다른 토픽 계속 처리
- watch_topics 비어있을 시: "등록된 토픽 없음. manage_watch_topics로 토픽을 먼저 등록하세요." 안내
- 모든 MCP 실패 시: WebSearch 대체 수집 + 한계 명시

## Notes
- 첫 실행 시 비교 기준 스냅샷 없음 → 데이터 수집 + 저장만 수행 (변화 감지 불가 안내)
- 스냅샷 비교는 `trend-tracker`의 `compare_snapshots` 도구 위임
- 🔴 긴급 토픽은 `/obsidian-bridge` 동기화 안내 출력
