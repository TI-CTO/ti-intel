# Monthly Deal Pipeline Review — 2026-04-03

## Executive Summary

startup-db 808건 중 **deal_stage가 설정된 기업은 2건**에 불과하다. 파이프라인 운영이 아직 초기 단계이며, 대다수 기업(806건)은 deal_stage 미지정 상태다. screening/due_diligence 단계에서 30일 이상 정체된 기업은 없다.

---

## 1. Deal Stage별 현황

| Deal Stage | 건수 | 비율 |
|---|---|---|
| discovered | 1 | 0.1% |
| screening | 1 | 0.1% |
| due_diligence | 0 | — |
| proposed | 0 | — |
| invested | 0 | — |
| partnership | 0 | — |
| passed | 0 | — |
| **미지정 (null)** | **806** | **99.8%** |
| **합계** | **808** | 100% |

### 파이프라인 기업 상세

| 기업 | Deal Stage | 카테고리 | 국가 | Overall Score | 총 누적 투자 |
|---|---|---|---|---|---|
| Mistral AI | discovered | Infra / Foundation Model | 프랑스 | 78 | €3.9B+ |
| ElevenLabs | screening | Model-Engine / Speech | 영국 | 72 | $781M |

---

## 2. 30일 이상 정체 기업 (screening / due_diligence)

> **해당 없음** — 현재 screening 단계에 ElevenLabs 1건만 존재하며, deal_stage 변경 추정 시점(updated_at 2026-03-26)으로부터 **8일 경과**로 정체 기준 미충족. due_diligence 단계에는 기업이 없다.

| 기업 | 단계 | 진입 추정일 | 경과일 | 정체 여부 |
|---|---|---|---|---|
| ElevenLabs | screening | 2026-03-13 (created) | 21일 | ❌ 미정체 |

※ deal_stage 변경 이력을 별도 추적하는 필드가 없어, `created_at`/`updated_at`으로 추정.

---

## 3. 최근 1개월 Deal Stage 변경 이력

DB에 deal_stage 변경 히스토리 테이블이 없으므로, `created_at`/`updated_at` 타임스탬프로 추론한 내역:

| 기업 | 변경 내용 | 추정 시점 | 근거 |
|---|---|---|---|
| Mistral AI | → discovered (신규 등록) | 2026-04-01 | created_at = 2026-04-01 |
| ElevenLabs | → screening (스코어링 완료) | 2026-03-13 ~ 03-26 | created 03-13, updated 03-26 |

---

## 4. 다음 단계 진행 권고

### 4-1. ElevenLabs → due_diligence 권고

| 항목 | 현황 | 평가 |
|---|---|---|
| Overall Score | 72점 | 상위권 (tech 8, team 9, biz_fit 8) |
| 성장 단계 | Late (Series D, $781M 누적) | 검증된 트랙션 |
| 관련 L3 | voice-synthesis | Voice AI 핵심 플레이어 |
| **권고** | **screening → due_diligence** | TTS/더빙 시장 선도 기업, 통신사 AICC/미디어 시너지 검토 가치 있음 |

**DD 시 확인 사항**: 기업 가치평가(최근 라운드 밸류 미등록), B2B 엔터프라이즈 매출 비중, 통신사 파트너십 이력, API 가격 구조.

### 4-2. Mistral AI → screening 권고

| 항목 | 현황 | 평가 |
|---|---|---|
| Overall Score | 78점 | 최상위 (tech 9, team 9, traction 8) |
| 성장 단계 | Late (Series C, €3.9B+ 누적) | 유니콘 |
| Business Fit | 5점 (상대적 약점) | 직접 시너지 제한적 |
| **권고** | **discovered → screening** | ARR $400M, Ericsson 텔레콤 레퍼런스 있으나 직접 시너지 검토 필요. biz_fit 5점 → screening에서 전략적 활용 시나리오 구체화 |

### 4-3. 구조적 개선 권고

| 과제 | 설명 | 우선순위 |
|---|---|---|
| **deal_stage 일괄 태깅** | 808건 중 806건 미지정 → 최소 score 기반 자동 분류(discovered) 검토 | 높음 |
| **변경 이력 추적** | deal_stage_history 테이블 또는 updated_at 외 별도 stage_changed_at 필드 도입 | 중간 |
| **정체 알림 자동화** | screening/DD 30일 초과 시 알림 트리거 (cron + startup-db 쿼리) | 낮음 |

---

*Generated: 2026-04-03 | Source: startup-db MCP (search_companies, get_company, get_company_stats)*
