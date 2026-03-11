# Skill Chaining Map

스킬 간 연결 관계와 데이터 흐름을 한 눈에 보는 가이드.

## 체이닝 맵

```
                    ┌─────────────┐
                    │   monitor   │  정기 토픽 스캔
                    └──────┬──────┘
                           │ 🟡🔴 감지
                           ▼
┌──────────┐     ┌─────────────────┐     ┌──────────┐
│ discover │────▶│ weekly-monitor  │────▶│   wtis   │
│ 기회 탐색 │     │   주간 동향      │     │ 기술 검증  │
└──────────┘     └─────────────────┘     └──────────┘
     │                    │                    │
     │                    │                    │
     ▼                    ▼                    ▼
┌──────────────────────────────────────────────────┐
│              research-session                     │
│              자유 주제 심층 리서치                    │
└──────────────────────────────────────────────────┘
                           │
               ┌───────────┼───────────┐
               ▼           ▼           ▼
         ┌──────────┐ ┌────────┐ ┌──────────────┐
         │report-pdf│ │ slides │ │obsidian-bridge│
         │  PDF     │ │ PPTX   │ │  Obsidian    │
         └──────────┘ └────────┘ └──────────────┘
```

## 스킬별 연결 상세

### 분석 스킬 (상류)

| From | Trigger | To | 데이터 전달 |
|------|---------|-----|-----------|
| **monitor** | 🔴 긴급 | wtis standard | 토픽 slug → 검증 대상 |
| **monitor** | 🟡🔴 | weekly-monitor | 도메인 slug → 주간 심층 |
| **monitor** | 🟡 주목 | research-session | 토픽명 → 자유 리서치 |
| **weekly-monitor** | 🔴 긴급 L3 | wtis standard | L2 기술명 → Go/No-Go 검증 |
| **weekly-monitor** | 특정 L3 심화 | research-session | L3 주제 → 심층 리서치 |
| **discover** | 즉시착수 기회 | wtis standard | 기회명 → 타당성 검증 |
| **discover** | 기회 심화 | research-session | 기회명 → 심층 조사 |
| **wtis** (deep) | Phase 1 | discover | 도메인 + competitors → 기회 탐색 |
| **wtis** (all) | Phase 2 | research-deep 에이전트 | Brief + domain-params → 심층 리서치 |
| **research-session** | 기술 검증 필요 | wtis standard | 주제 → 200점 채점 |
| **research-session** | 넓은 탐색 필요 | discover | 도메인 → 기회 발굴 |

### 출력 변환 스킬 (하류)

| From | To | 데이터 전달 |
|------|-----|-----------|
| 모든 분석 스킬 | **report-pdf** | 마크다운 경로 → PDF |
| 모든 분석 스킬 | **slides** | 마크다운 경로 → PPTX |
| 모든 분석 스킬 | **obsidian-bridge** | 파일 경로 + 타입 → 볼트 복사 |
| **wtis** | **obsidian-bridge** (wtis) | 세션 폴더 → final.md + PDF |
| **wtis** | **obsidian-bridge** (portfolio) | portfolio.md + PDF |
| **weekly-monitor** | **obsidian-bridge** (weekly) | 메인 리포트 + PDF |
| **weekly-monitor** | **obsidian-bridge** (research) | Deep 리서치 파일 |

### 보조 스킬

| From | To | 목적 |
|------|-----|------|
| 모든 스킬 | **work-log** | 세션 작업 내용 일지 기록 |

## I/O Contract 요약

모든 분석 스킬은 통일된 Return 형식을 사용한다:

```yaml
status: pass | fail | partial | needs-followup
summary: "200자 이내 요약"
file_path: "주요 산출물 절대 경로"
```

### 스킬별 추가 Return 필드

| Skill | 추가 필드 |
|-------|----------|
| weekly-monitor | `deep_files` (Deep 리서치 파일 목록) |
| wtis | `verdict`, `score`, `strategy`, `session_dir` |
| monitor | `files` (생성된 보고서 목록) |
| research-session | `confidence` |

## 워크플로우 시나리오

### 시나리오 1: 주간 루틴
```
/weekly-monitor agentic-ai
  → 🔴 adaptive-rag 긴급
  → /wtis standard adaptive-rag Go/No-Go 검증
  → /obsidian-bridge {세션 폴더} wtis
  → /work-log
```

### 시나리오 2: 신기술 발굴
```
/discover edge AI for telecom
  → 즉시착수 2건 발견
  → /wtis standard {기회명} 타당성 검증
  → /slides {final.md}
  → /obsidian-bridge {세션 폴더} wtis
```

### 시나리오 3: 정기 모니터링 → 심화
```
/monitor
  → 🟡 ai-network 주목
  → /research-session ai-network 최근 동향
  → /report-pdf {리포트}
  → /obsidian-bridge {리포트} research
```
