# outputs — 산출물 저장 규칙

모든 스킬과 에이전트는 이 규칙에 따라 산출물을 저장한다.
**루트(`outputs/reports/`)에 직접 파일을 생성하지 않는다.**
이 문서는 **산출물 경로/파일명 규칙 전용**이다. WTIS의 실행 순서, 상태값, 예외 처리는 `.claude/skills/wtis/SKILL.md`를 최종 기준으로 따른다.

## 폴더 구조

```
outputs/reports/
  {domain}/{l2_slug}/     ← L2 기술 귀속 분석 (WTIS, strategy, biz-case, 관련 리서치)
  spot/                   ← L2 미소속 스팟 리서치 (자유 주제, 기업 이벤트 분석 등)
  startups/               ← startup-scout + startup-analyst 결과
  weekly/                 ← 주간 모니터링 + 경쟁사 모니터
  summaries/              ← 여러 리포트를 종합한 정리
```

## 경로 결정 규칙

산출물을 저장할 때 아래 순서로 적절한 폴더를 결정한다:

| 조건 | 저장 위치 | 예시 |
|------|----------|------|
| L2 기술에 귀속 (WTIS, strategy-options, biz-case, 관련 리서치) | `{domain}/{l2_slug}/` | `voice-ai/speech-generation/2026-03-20_wtis-full-speech-generation.md` |
| 주간 모니터링 또는 경쟁사 모니터 | `weekly/` | `weekly/2026-03-18_weekly-secure-ai.md` |
| startup-scout 또는 startup-analyst 결과 | `startups/` | `startups/2026-03-13_startup-voicerun.md` |
| L2에 속하지 않는 자유 주제 리서치 | `spot/` | `spot/2026-03-20_research-kaist-soulmate-ai-chip.md` |
| 포트폴리오 | `{domain}/` (도메인 루트) | `voice-ai/voice-ai-portfolio.md` |
| 종합 정리 (3건+ 누적 시) | `summaries/` | `summaries/summary_ondevice-ai.md` |

### "L2 귀속" 판단 기준

- WTIS standard/full 실행 결과 → 해당 L2 폴더
- strategy-options, biz-case → 체이닝 원본 WTIS의 L2 폴더
- research-deep이 WTIS/strategy-options/biz-case **내부에서** 호출된 경우 → 호출한 스킬의 L2 폴더
- research-session이 **특정 L2 기술**을 주제로 한 경우 → 해당 L2 폴더
- research-session이 **L2에 속하지 않는 자유 주제**인 경우 → `spot/`

## 파일명 규칙

모든 파일은 `{YYYY-MM-DD}_{type}-{slug}.md` 형식:

| 유형 | 파일명 패턴 |
|------|-----------|
| WTIS Standard | `{date}_wtis-{l2_slug}.md` |
| WTIS Full | `{date}_wtis-full-{l2_slug}.md` |
| Strategy Options | `{date}_strategy-options-{l2_slug}.md` |
| Biz Case | `{date}_biz-case-{l2_slug}.md` |
| Research (WTIS 내부) | `{date}_wtis-research.md` |
| Research (독립) | `{date}_research-{slug}.md` |
| Fact Check | `{date}_factcheck-{slug}.md` |
| Weekly Monitor | `{date}_weekly-{domain}.md` |
| Startup Scout | `{date}_scout-{domain}.md` |
| Startup Analyst | `{date}_startup-{company-slug}.md` |
| 포트폴리오 | `{domain}-portfolio.md` (날짜 없음) |

## 파일 생성 주체

| 스킬/에이전트 | 저장 위치 |
|--------------|-----------|
| `/wtis standard` | `reports/{domain}/{l2_slug}/{date}_wtis-{slug}.md` |
| `/wtis full` | `reports/{domain}/{l2_slug}/{date}_wtis-full-{slug}.md` |
| `/strategy-options` | `reports/{domain}/{l2_slug}/{date}_strategy-options-{slug}.md` |
| `/biz-case` | `reports/{domain}/{l2_slug}/{date}_biz-case-{slug}.md` |
| `/weekly-monitor` | `reports/weekly/{date}_weekly-{domain}.md` |
| `/monitor` | `reports/weekly/{date}_monitor-{topic}.md` |
| `/research-session` | L2 귀속 → `reports/{domain}/{l2_slug}/`, 자유 → `reports/spot/` |
| `/discover` | `reports/spot/{date}_discover-{domain}.md` |
| `/startup-scout` | `reports/startups/{date}_scout-{domain}.md` |
| `/startup-analyst` | `reports/startups/{date}_startup-{slug}.md` |
| `research-deep` (WTIS 내부) | 호출한 스킬의 L2 폴더 |
| `research-deep` (독립) | L2 귀속 → 해당 폴더, 자유 → `reports/spot/` |
| `fact-checker` | 검증 대상과 같은 폴더 |

## Obsidian 동기화 대응

| git 경로 | Obsidian 경로 |
|---------|-------------|
| `reports/{domain}/{l2_slug}/` | `30-Reports/{domain}/{l2_slug}/` |
| `reports/weekly/` | `30-Reports/weekly/` |
| `reports/startups/` | `60-Spot/companies/` 또는 `50-Startups/` |
| `reports/spot/` | `30-Reports/spot/` |

## Rules

- **루트에 직접 파일 생성 금지** — 반드시 위 폴더 중 하나에 저장
- 같은 주제 리포트가 3개 이상 쌓이면 `summaries/`에 종합 정리 작성
- 유의미한 발견은 `/obsidian-bridge`로 Obsidian 볼트에 동기화
- 외부 소스를 인용할 때는 리포트 본문에 각주로 출처 기록
- 과거 산출물에 남아 있는 구형 상태값(`partial` 등)은 레거시 결과물로 취급한다. 신규 실행 계약의 상태값 기준은 WTIS/validator 문서를 따른다.
