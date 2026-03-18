# Tech Intelligence Platform — 팀 Quick Start

> 5분 안에 플랫폼을 사용할 수 있는 빠른 시작 가이드.
> 상세 도구 레퍼런스: `docs/guide-tool-reference.md`

---

## 1. 환경 설정

### 필수 조건
- macOS (터미널)
- Claude Code CLI (`~/.local/bin/claude`)
- 환경변수: `.env` 파일에 API 키 설정 완료

### 시작
```bash
cd /Users/ctoti/Project/ClaudeCode
claude
```

---

## 2. 30초 치트시트

| 하고 싶은 일 | 명령어 |
|-------------|--------|
| "이 기술 투자해야 해?" | `/wtis standard {기술명}` |
| "이번 주 뭐 바뀌었어?" | `/weekly-monitor {도메인}` |
| "이 주제 조사해줘" | `/research-session {주제}` |
| "새 기술 기회 찾아줘" | `/discover {분야}` |
| "스타트업 찾아줘" | `/startup-scout {도메인}` |
| "이 회사 분석해줘" | `/startup-analyst {기업명}` |
| "리포트 PDF로" | `/report-pdf {파일경로}` |
| "발표자료 만들어줘" | `/slides {파일경로}` |

> 슬래시 명령어 대신 자연어로 말해도 됩니다: "PQC 기술 Go/No-Go 판정해줘"

---

## 3. 도메인 구조

```
L1 도메인 (3개)        L2 기술영역 (10개)          L3 세부기술 (25개)
━━━━━━━━━━━━          ━━━━━━━━━━━━━━━          ━━━━━━━━━━━━━━━
Agentic AI (월)  ──── Self Evolving Architecture ── Agentic Context Engineering
                 ├── Model & Delta Foundry ──────── FeedbackOps, EvaluationOps, MLOps, GPU Orch.
                 ├── Trusted Multi-Agent ─────────── Agent Orchestration, Agent-Oriented Orch.
                 ├── Hybrid AI Infra ─────────────── OnDevice sLM, Speaker Diarization, Edge AI, 5G/6G
                 └── 의도 파악 기술 ──────────────── Adaptive RAG

Voice AI (화)    ──── Speech Perception ──────────── Emotional Analysis, Context Recog., Turn-Taking
                 ├── Personal Intelligence ───────── Persona, Relationship Graph, Context Action
                 └── Speech Generation ───────────── Voice Cloning, Voice Synthesis

Secure AI (수)   ──── 스팸/피싱탐지 ──────────────── 스팸/피싱 감지, OCR 이미지 스팸
                 └── 양자/동형 암호 ──────────────── PQC 통화 암호화, HE 키워드 검색, Secure Vector
```

---

## 4. 주요 시나리오별 사용법

### 시나리오 A: "이번 주 기술 동향 알려줘"

```
/weekly-monitor secure-ai
```
→ 5개 L3 빠른 스캔 → 변화 감지된 L3 심층 분석 → 주간 리포트 + PDF

### 시나리오 B: "이 기술에 투자할까?"

```
/wtis standard 동형암호 키워드 검색
```
→ 심층 리서치 → 200점 정량 평가 → Go/Conditional/No-Go 판정 → PDF + 포트폴리오

### 시나리오 C: "경쟁사가 뭐 하고 있어?"

```
"SKT KT 양자암호 최근 동향 알려줘"
```
→ intel-store에서 `skt-strategy`, `kt-strategy` 토픽 검색 + 웹 서치

### 시나리오 D: "이 분야 스타트업 후보 찾아줘"

```
/startup-scout voice AI 한국
```
→ 웹 리서치 → 후보 쇼트리스트 → DB 저장 제안

### 시나리오 E: "특정 기업 심층 분석"

```
/startup-analyst Hume AI
```
→ 기업 조사 → 분석 리포트 + DB 입력용 정규화 데이터

---

## 5. 산출물 위치

```
outputs/reports/
  agentic-ai/                     ← Agentic AI WTIS 분석
    agentic-ai-portfolio.md       ← 포트폴리오 (L2별 점수 요약)
    2026-03-09_multi-agent/       ← WTIS 세션
  voice-ai/                       ← Voice AI WTIS 분석
    voice-ai-portfolio.md
  secure-ai/                      ← Secure AI WTIS 분석
    secure-ai-portfolio.md
  weekly/                         ← 주간 모니터링
    2026-03-18_weekly-secure-ai.md
    2026-03-18_weekly-secure-ai.pdf
    2026-03-18_research-*.md       ← Deep 리서치 (L3별)
```

---

## 6. 포트폴리오 현황 (2026-03-18)

### 전체 L2 판정 요약

| 판정 | L2 수 | 기술 목록 |
|------|-------|----------|
| Conditional Go | 5 | Multi-Agent(155), Hybrid AI(131), Adaptive RAG(131), Speech Generation(128), HE 키워드검색(125) |
| 재검토 | 3 | Speech Perception(118), 스팸/피싱(115), OnDevice AI(107) |
| Watch | 2 | Model & Delta Foundry, Personal Intelligence |

### 읽는 법
- **Go (160+)**: 즉시 추진
- **Conditional Go (120~159)**: 조건 충족 시 추진 (조건 목록 확인)
- **재검토 (80~119)**: 근본적 재설계 필요
- **No-Go (~79)**: 추진 부적합

---

## 7. 주간 운영 스케줄

| 요일 | 도메인 | 자동화 | 명령어 |
|------|--------|--------|--------|
| 월 | Agentic AI | 스크립트 준비 | `/weekly-monitor agentic-ai` |
| 화 | Voice AI | 스크립트 준비 | `/weekly-monitor voice-ai` |
| 수 | Secure AI | 스크립트 준비 | `/weekly-monitor secure-ai` |
| 목 | (자유) | — | WTIS, 리서치, 스타트업 분석 등 |
| 금 | (자유) | — | 리뷰, 포트폴리오 정리, 이관 |

---

## 8. 자주 묻는 질문

**Q: 데이터가 없는 새 주제를 검색하면?**
A: 먼저 수집이 필요합니다. "PQC 논문 수집해줘" → `collect_all` 실행 → 이후 검색 가능.

**Q: MCP 도구를 직접 호출해야 하나?**
A: 아닙니다. 자연어로 말하면 Claude가 적절한 도구를 자동 선택합니다. "PQC 관련 뉴스 찾아줘"라고 하면 됩니다.

**Q: VSCode에서 사용 가능한가?**
A: MCP 도구 호출은 터미널 Claude Code에서만 가능합니다. VSCode Claude 확장에서는 일반 대화만 가능합니다.

**Q: SerpAPI 쿼터가 걱정되는데?**
A: 특허 수집(`collect_patents`)만 SerpAPI를 사용합니다. 뉴스/논문 수집은 무료 API이므로 자유롭게 사용하세요.

**Q: 리포트를 Obsidian에서 보고 싶어요**
A: `/obsidian-bridge {파일경로} {유형}`으로 동기화합니다. 유형: `wtis`, `weekly`, `research`, `reference`.

---

## 9. 장애 대응

| 증상 | 원인 | 대응 |
|------|------|------|
| "MCP 도구 호출 실패" | MCP 서버 미시작 | 터미널 재시작 또는 `claude` 재실행 |
| "collect 결과 0건" | API 키 만료 또는 쿼터 초과 | `.env` 키 확인, `get_intel_stats`로 현황 체크 |
| "PDF 생성 실패" | Playwright 미설치 | `uv run --extra browser playwright install chromium` |
| "Obsidian 파일 안 보여" | 동기화 미실행 | `/obsidian-bridge`로 수동 동기화 |
| "WTIS 타임아웃" | opus 에이전트 과부하 | 재실행 (2차 시도에서 성공하는 패턴) |

---

## 10. 참고 문서

| 문서 | 위치 | 내용 |
|------|------|------|
| 도구 레퍼런스 (상세) | `docs/guide-tool-reference.md` | 전체 도구 목록, 파라미터, 사용 예시 |
| 스킬 체이닝 맵 | `docs/guide-skill-chaining.md` | 스킬 간 연결 관계 + 시나리오 |
| 기술 분류체계 | `.claude/skills/wtis/references/tech-taxonomy.md` | L1/L2/L3 전체 정의 + 검색 키워드 |
| 3주 시범운영 통계 | `outputs/reports/2026-03-18_3week-pilot-summary.md` | KPI 달성, 데이터 현황 |
