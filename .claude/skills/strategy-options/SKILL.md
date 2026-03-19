---
name: strategy-options
description: "WTIS 평가 이후 Build/Buy/Partner 전략 옵션을 정량 비교하고 CTO 권고안을 도출한다."
user-invokable: true
argument-hint: "[WTIS 리포트 경로 또는 L2 기술명]"
---

# Strategy Options — 전략 옵션 분석

WTIS 평가 결과를 입력받아 **Build / Buy(Acquire) / Partner(Borrow)** 3가지 전략 옵션을 정량 비교하고, CTO에게 제출할 권고안을 산출한다.

## 빠른 시작

```
/strategy-options outputs/reports/voice-ai/2026-03-17_speech-generation/2026-03-17_wtis-speech-generation.md
/strategy-options speech-generation
```
**실행 중:** WTIS 리포트 분석 → 옵션별 리서치 → 정량 비교 → 권고안 작성
**완료 시:** `outputs/reports/{domain}/{date}_{slug}/` 아래에 전략 옵션 리포트 저장

---

## Arguments
- 첫 번째 인자: WTIS 리포트 `.md` 경로 **또는** L2 기술명 (최신 WTIS 세션 자동 탐색)

## I/O Contract

### Input
| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `wtis_report` | yes | 파일 경로 또는 L2 slug | WTIS 평가 완료된 리포트. verdict가 Go 또는 Conditional Go인 경우에 실행 |

### Output Files
| Artifact | Path Pattern | Description |
|----------|-------------|-------------|
| 전략 옵션 리포트 | `outputs/reports/{domain}/{date}_{slug}/{date}_strategy-options-{slug}.md` | Build/Buy/Partner 비교 분석 |

### Return
```yaml
status: pass | partial | fail
summary: "{기술명}: {권고 옵션} 권고 (총점 {N}/100)"
file_path: "리포트 절대 경로"
recommended_option: build | buy | partner | hybrid
```

---

## Process

### Step 0: WTIS 리포트 로딩
1. 인자가 파일 경로면 직접 Read
2. 인자가 L2 slug이면 `outputs/reports/*/` 에서 최신 WTIS 리포트 탐색
3. frontmatter에서 `score`, `verdict`, `strategy`, `domain`, `l2_topic` 추출
4. **verdict가 No-Go 또는 Hold면 중단** — "WTIS 판정이 {verdict}이므로 전략 옵션 분석 대상이 아닙니다" 안내

### Step 1: WTIS 데이터 추출
리포트에서 다음을 파싱:
- **5차원 점수 분해** (고객가치/시장매력도/기술경쟁력/경쟁우위/실행가능성 각 /40)
- **3B 의사결정 요약** (기존 Buy/Borrow/Build 판단)
- **리스크 테이블** (상위 3~5개 리스크)
- **후속 조건 체크리스트** (Conditional Go인 경우)
- **핵심 플레이어** (경쟁사, 잠재 파트너, 인수 후보)

### Step 2: 옵션별 리서치
research-deep 에이전트를 **최대 3개 병렬** 투입하여 각 옵션의 실현 가능성을 조사:

**Build 리서치:**
- 내부 역량 현황 (LG U+ 기존 기술 스택, 인력)
- 개발 기간 추정 (유사 사례 벤치마크)
- 필요 투자 규모 (인력, 인프라, 라이선스)

**Buy 리서치:**
- 인수 후보 기업 리스트 + 밸류에이션 범위
- 최근 유사 M&A 딜 사례 (가격, 시너지)
- 통합 리스크 (기술 스택 호환성, 인력 이탈)

**Partner 리서치:**
- 잠재 파트너 기업 리스트 + 협업 모델 (API, JV, 라이선스)
- 유사 파트너십 사례 (통신사 × 기술기업)
- 파트너 의존도 리스크 (lock-in, 가격 인상)

### Step 3: 옵션 스코어링 (100점 만점)
각 옵션을 5개 기준으로 채점 (기준당 20점):

| 기준 | 설명 | 채점 근거 |
|------|------|----------|
| **전략 적합성** (Strategic Fit) | LG U+ 전략 방향과의 정합성 | WTIS 결과 + 경쟁사 동향 |
| **실행 속도** (Time to Market) | 시장 진입까지 소요 시간 | 벤치마크 사례 |
| **투자 효율** (Cost Efficiency) | 총 투자 대비 기대 가치 | 재무 추정 |
| **리스크** (Risk Profile) | 실패 확률 및 영향도 | 리스크 테이블 |
| **지속 가능성** (Sustainability) | 장기 경쟁력 유지 가능성 | 기술 로드맵 |

채점 방식:
- 각 기준 1~20점 (4점 단위: 4=낮음, 8=보통 이하, 12=보통, 16=높음, 20=매우 높음)
- 반드시 근거 인용 포함 — 추정값이면 `[추정]` 태그

### Step 4: 권고안 작성

**출력 구조:**

```markdown
---
topic: {기술명}
domain: {domain}
l2_topic: {l2_slug}
date: {YYYY-MM-DD}
skill: strategy-options
wtis_score: {N}/200
wtis_verdict: {verdict}
recommended_option: {build|buy|partner|hybrid}
confidence: {high|medium|low}
---

# 전략 옵션 분석: {기술명}

> **WTIS 판정**: {verdict} ({score}/200) | **권고 옵션**: {recommended} | **날짜**: {date}

## Executive Summary
> 3~5줄 요약: WTIS 결과 요약 → 옵션 비교 핵심 → 최종 권고

## 1. WTIS 결과 요약
- 5차원 점수 요약 테이블 (WTIS에서 추출)
- 핵심 강점/약점 2~3개

## 2. 전략 옵션 비교

### 2.1 Build (자체 개발)
- 개요: 무엇을 개발하는가
- 필요 자원: 인력, 기간, 비용
- 장점 / 단점
- 핵심 리스크

### 2.2 Buy (인수/라이선스)
- 후보 기업 테이블 (기업명 / 기술 / 추정 밸류에이션 / 적합도)
- 유사 M&A 사례
- 장점 / 단점
- 핵심 리스크

### 2.3 Partner (제휴/협력)
- 후보 파트너 테이블 (기업명 / 협업 모델 / 기대 효과)
- 유사 파트너십 사례 (특히 통신사 사례)
- 장점 / 단점
- 핵심 리스크

## 3. 정량 비교 매트릭스

| 기준 (각 20점) | Build | Buy | Partner |
|----------------|-------|-----|---------|
| 전략 적합성 | {N} | {N} | {N} |
| 실행 속도 | {N} | {N} | {N} |
| 투자 효율 | {N} | {N} | {N} |
| 리스크 | {N} | {N} | {N} |
| 지속 가능성 | {N} | {N} | {N} |
| **합계** | **{N}/100** | **{N}/100** | **{N}/100** |

## 4. 최종 권고
- 권고 옵션 및 근거 (3~5줄)
- Hybrid 전략인 경우: 조합 방식 명시
- 실행 로드맵 (Q 단위 타임라인)
- 의사결정 전 확인 필요 사항

## 5. 후속 조건 (Conditional Go 연계)
- WTIS 후속 조건 체크리스트와 매핑
- 옵션별 해소 경로

## References
- T5 테이블 (WTIS 형식 준수)
```

### Step 5: 저장 및 안내

1. 리포트를 WTIS 세션 폴더에 저장
2. 포트폴리오에 전략 옵션 결과 반영 여부 안내

---

## Critical Rules

- **WTIS 리포트가 없으면 실행 불가** — 반드시 WTIS 평가가 선행되어야 함
- **No-Go / Hold 판정은 분석 대상 아님** — 안내 후 중단
- **채점 시 추정값 명시** — 정확한 데이터가 없으면 `[추정]` 태그 + 가정 명시
- **통신사 맥락 반영** — 일반적 3B가 아닌 LG U+ 관점에서 분석 (네트워크 자산, 가입자 기반, 규제 환경)
- **research-deep 최대 3개 병렬** — 리소스 경합 방지

---

## Next Steps

저장 완료 후 아래 후속 옵션을 사용자에게 제시한다:

```
📋 Next Steps:
  💰 비즈니스 케이스 작성:
    → /biz-case {strategy-options 리포트 경로}     — ROI·시나리오 분석
  📄 PDF 변환:
    → /report-pdf {리포트 경로}                    — 컨설팅 스타일 PDF
  📂 Obsidian 동기화:
    → /obsidian-bridge {리포트 경로} wtis          — Obsidian 볼트 동기화
  📝 업무일지:
    → /work-log                                   — 작업 내용 기록
```
