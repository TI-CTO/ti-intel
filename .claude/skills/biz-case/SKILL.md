---
name: biz-case
description: "기술 투자의 비즈니스 케이스를 작성한다. TAM/SAM/SOM 추정, ROI 시나리오, 투자 회수 분석을 포함한다."
user-invokable: true
argument-hint: "[기술명 또는 strategy-options 리포트 경로]"
---

# Biz Case — 비즈니스 케이스 작성

기술 투자에 대한 **비즈니스 정당성**을 구축한다. 시장 규모 추정, 3개 시나리오별 ROI, 투자 회수 타임라인을 산출하여 CTO/경영진 의사결정을 지원한다.

## 빠른 시작

```
/biz-case speech-generation
/biz-case outputs/reports/voice-ai/2026-03-17_speech-generation/2026-03-17_strategy-options-speech-generation.md
```
**실행 중:** 시장 데이터 수집 → TAM/SAM/SOM 추정 → 시나리오 모델링 → 비즈니스 케이스 작성
**완료 시:** `outputs/reports/{domain}/{date}_biz-case-{slug}.md` 저장

---

## Arguments
- 첫 번째 인자: L2 기술명, WTIS 리포트 경로, 또는 strategy-options 리포트 경로
- strategy-options 리포트가 있으면 권고 옵션(Build/Buy/Partner)에 맞춰 비용 구조를 자동 조정

## I/O Contract

### Input
| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `topic` | yes | L2 slug 또는 파일 경로 | 비즈니스 케이스 대상. WTIS/strategy-options 체인 가능 |

### Output Files
| Artifact | Path Pattern | Description |
|----------|-------------|-------------|
| 비즈니스 케이스 | `outputs/reports/{domain}/{date}_biz-case-{slug}.md` | TAM/SAM/SOM + ROI + 시나리오 |

### Return
```yaml
status: pass | partial | fail
summary: "{기술명}: {시나리오} 기준 ROI {N}%, 회수 {N}년"
file_path: "리포트 절대 경로"
base_scenario_roi: "{N}%"
payback_period: "{N}년"
```

---

## Process

### Step 0: 컨텍스트 수집
1. 인자가 파일 경로면 Read → frontmatter에서 `domain`, `l2_topic`, `score`, `recommended_option` 추출
2. 인자가 L2 slug이면 해당 도메인 폴더에서 WTIS/strategy-options 리포트 탐색
3. 기존 리포트가 없어도 실행 가능 — 독립 비즈니스 케이스로 작성

### Step 1: 시장 규모 리서치
research-deep 에이전트로 시장 데이터 수집:

**수집 대상:**
- **TAM** (Total Addressable Market): 글로벌 전체 시장 규모 + CAGR
- **SAM** (Serviceable Available Market): LG U+가 접근 가능한 시장 (한국, 통신사 영역)
- **SOM** (Serviceable Obtainable Market): 현실적으로 확보 가능한 시장 점유율
- **출처**: 시장 조사 기관 보고서 (Gartner, IDC, Markets&Markets 등), 산업 보고서, 경쟁사 실적

**추정 규칙:**
- 정확한 수치가 없으면 Top-down / Bottom-up 양방향 추정 후 교차 검증
- 모든 추정에 `[추정: 가정 설명]` 태그 필수
- 환율: 보고서 기준 환율 명시 (없으면 1 USD = 1,350 KRW 기본)

### Step 2: 비용 구조 설계
strategy-options 권고 옵션에 따라 비용 항목 결정:

**Build 비용 모델:**
| 항목 | 초기 (Y1) | 운영 (Y2~) |
|------|----------|-----------|
| 인력 (개발자 N명) | 인건비 × N | 유지보수 팀 |
| 인프라 (클라우드/온프렘) | 구축비 | 월 운영비 |
| 라이선스/특허 | 초기 비용 | 연간 갱신 |
| 기회비용 | 개발 기간 × 시장 기회 손실 | — |

**Buy 비용 모델:**
| 항목 | 초기 | 운영 (Y2~) |
|------|------|-----------|
| 인수가 | 밸류에이션 | — |
| 통합 비용 | 시스템 통합 + 인력 전환 | 추가 개발 |
| 운영비 | — | 인건비 + 인프라 |

**Partner 비용 모델:**
| 항목 | 초기 | 운영 (Y2~) |
|------|------|-----------|
| 계약 비용 | 계약금/선불 | 레브쉐어 or 라이선스 |
| 통합 비용 | API 연동 개발 | 유지보수 |
| 의존 비용 | — | 가격 인상 리스크 |

### Step 3: 매출 시나리오 모델링
3개 시나리오를 5년 기간으로 모델링:

| 시나리오 | 가정 | SOM 점유율 |
|---------|------|-----------|
| **낙관** (Upside) | 시장 고성장 + 조기 진입 + 경쟁사 지연 | SOM 상한 |
| **기본** (Base) | 시장 전망 중앙값 + 계획대로 실행 | SOM 중앙 |
| **비관** (Downside) | 시장 둔화 + 실행 지연 + 경쟁 심화 | SOM 하한 |

각 시나리오별 산출:
- 연도별 매출 (Y1~Y5)
- 연도별 비용 (고정 + 변동)
- 연도별 영업이익
- 누적 현금흐름 (투자 회수 시점 파악)
- **ROI** = (5년 누적 이익 - 총 투자) / 총 투자 × 100%
- **회수 기간** (Payback Period): 누적 현금흐름이 양전환하는 시점

### Step 4: 리포트 작성

**출력 구조:**

```markdown
---
topic: {기술명}
domain: {domain}
l2_topic: {l2_slug}
date: {YYYY-MM-DD}
skill: biz-case
strategy_option: {build|buy|partner|hybrid}
base_scenario_roi: "{N}%"
payback_period: "{N}년"
confidence: {high|medium|low}
---

# 비즈니스 케이스: {기술명}

> **전략 옵션**: {strategy} | **기본 시나리오 ROI**: {N}% | **회수 기간**: {N}년

## Executive Summary
> 5줄 이내: 시장 기회 → 투자 규모 → ROI → 권고

## 1. 시장 규모

### 1.1 TAM / SAM / SOM
| 구분 | 2025 | 2030 (예측) | CAGR | 출처 |
|------|------|-----------|------|------|
| TAM | ${N}B | ${N}B | {N}% | {출처} |
| SAM | ${N}M | ${N}M | {N}% | {출처} |
| SOM | ${N}M | ${N}M | — | [추정] |

### 1.2 시장 드라이버 & 억제 요인
- 드라이버: (불릿 3~4개)
- 억제 요인: (불릿 2~3개)

## 2. 투자 비용 구조

### 2.1 비용 요약
| 항목 | Y1 | Y2 | Y3 | Y4 | Y5 | 합계 |
|------|----|----|----|----|----|----|
| ... | | | | | | |
| **소계** | | | | | | **{N}** |

### 2.2 주요 가정
- (불릿: 각 비용 항목의 산출 근거)

## 3. 매출 시나리오

### 3.1 시나리오별 매출 전망
| 연도 | 낙관 | 기본 | 비관 |
|------|------|------|------|
| Y1 | | | |
| Y2 | | | |
| Y3 | | | |
| Y4 | | | |
| Y5 | | | |

### 3.2 핵심 가정 비교
| 변수 | 낙관 | 기본 | 비관 |
|------|------|------|------|
| 시장 성장률 | | | |
| SOM 점유율 | | | |
| 가격 수준 | | | |

## 4. ROI & 회수 분석

### 4.1 시나리오별 ROI
| 시나리오 | 총 투자 | 5년 누적 이익 | ROI | 회수 기간 |
|---------|---------|-------------|-----|----------|
| 낙관 | | | {N}% | Y{N} |
| **기본** | | | **{N}%** | **Y{N}** |
| 비관 | | | {N}% | Y{N} |

### 4.2 누적 현금흐름 (테이블)
| 연도 | 비용 | 매출 | 연간 P/L | 누적 |
|------|------|------|---------|------|
| Y1 | | | | |
| ... | | | | |

### 4.3 민감도 분석
- 시장 성장률 ±5%p 시 ROI 변동: {N}% ~ {N}%
- SOM 점유율 ±2%p 시 ROI 변동: {N}% ~ {N}%

## 5. 리스크 & 완화 방안
| 리스크 | 확률 | 영향 | 완화 방안 |
|--------|------|------|----------|
| ... | H/M/L | H/M/L | ... |

## 6. 의사결정 권고
- Go/No-Go 기준: ROI {N}% 이상, 회수 {N}년 이내
- 권고: {Go/Conditional/No-Go} 근거 3줄
- 다음 단계: 의사결정 필요 사항

## References
```

### Step 5: 저장 및 안내
1. 리포트 저장
2. Next Steps 제시

---

## Critical Rules

- **모든 수치에 출처 또는 `[추정]` 태그** — 출처 없는 수치는 신뢰도 저하
- **3개 시나리오 필수** — 단일 시나리오 비즈니스 케이스는 금지
- **통신사 매출 모델 적용** — B2C 가입자 기반, B2B 솔루션, B2G 납품 등 통신사 특화 매출 경로
- **환율·물가 가정 명시** — 재무 추정의 기본 가정을 섹션 2.2에 반드시 포함
- **research-deep 최대 2개 병렬** — 시장 리서치 + 경쟁사 리서치

---

## Next Steps

저장 완료 후 아래 후속 옵션을 사용자에게 제시한다:

```
📋 Next Steps:
  📄 PDF 변환:
    → /report-pdf {리포트 경로}                    — 컨설팅 스타일 PDF
  📊 발표 자료:
    → /slides {리포트 경로}                        — CTO 보고용 PPTX
  📂 Obsidian 동기화:
    → /obsidian-bridge {리포트 경로} wtis          — Obsidian 볼트 동기화
  📝 업무일지:
    → /work-log                                   — 작업 내용 기록
```
