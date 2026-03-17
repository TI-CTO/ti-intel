---
type: wtis-validator
target: skill1.md
date: 2026-03-16
---

# WTIS Validator: 의도 파악 기술 (Adaptive RAG)

## 검증 요약
- 최종 판정: PARTIAL
- 검증 신뢰도: Medium
- 이슈 건수: 6건 (심각 2, 경미 4)

---

## 1. 인용 검증

### References 테이블 존재 여부

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | PASS | G-xx / E-xx / P-xx 3개 계열 완비 |
| 본문 [N] → 테이블 전수 매칭 | PASS | 미매칭 인용 없음 |
| 고아 소스 (테이블 정의 but 본문 미인용) | FAIL | G-22, P-04 2건 |
| 인용 없는 수치 주장 | PARTIAL | 57%+ 프로덕션 채택 수치 인용 없음 (아래 상세) |

### 인용 코드 전수 비교

**본문에서 사용된 인용 코드 (중복 제거):**

G계열: G-01, G-02, G-03, G-04, G-05, G-06, G-08, G-10, G-12, G-14, G-15, G-16, G-17, G-18, G-19, G-20, G-21, G-23, G-26, G-27 (20건)

E계열: E-01, E-02, E-03, E-04, E-05 (5건)

P계열: P-01, P-02, P-03, P-05 (4건)

**References 테이블에 정의된 코드:**

G계열: G-01~G-06, G-08, G-10, G-12, G-14~G-23, G-26, G-27 (21건)

E계열: E-01~E-05 (5건)

P계열: P-01~P-05 (5건)

**고아 소스 (테이블 정의 but 본문 미인용):**
- `G-22` (Klover.ai, Verizon AI Strategy) — 본문 어디에도 인용되지 않음
- `P-04` (ACM Computing Surveys, Multiturn Dialogue Survey) — 본문 어디에도 인용되지 않음

### 인용 없는 수치 주장

| 위치 | 주장 | 인용 여부 |
|------|------|----------|
| 기술 성숙도 맵 §2 | "Multi-hop Agentic RAG ... 57%+ 프로덕션 채택" | 인용 없음 — [D]도 미표기 |

---

## 2. 수치 교차검증

### TAM/CAGR 수치

| 수치 | 출처 수 | URL 검증 | 판정 |
|------|---------|---------|------|
| RAG TAM $9.86B (2030), CAGR 38.4% | 2건 (G-01 MnM, G-02 GVR) | G-01 URL 직접 확인 — $9.86B, CAGR 38.4% **일치** | PASS |
| RAG TAM $11.0B (GVR) | 1건 (G-02) | URL 미검증 (MnM 교차로 [B] 판정 적절) | PASS (B) |
| SAM $1.2~1.4B | 단일 추정 ([D]) | 편의 계산 — $4.73B × 25~30% = $1.18~1.42B. 계산 자체는 일관. [D] 명시 | PASS |
| CAGR 38.4% vs GVR $1.2B(2024)→$11.0B(2030) | 내부 일관성 | GVR 수치로 CAGR 재계산: (11.0/1.2)^(1/6)-1 ≈ 44.7%. MnM 기준 38.4%와 GVR 암시 CAGR 불일치. 단, 리포트는 GVR에서 CAGR을 인용하지 않으므로 직접 충돌은 아님 | 경미 (참고) |
| AI in Telecom $4.73B (2025), CAGR 37.9% | 1건 (G-23) | URL 미검증 [B] 단일 소스 | 단일 소스 (B) |
| 국내 AI 시장 6조원 | 1건 (G-27) | URL 미검증 [B] 단일 소스 | 단일 소스 (B) |

### G-04 핵심 수치 미확인 (심각)

| 주장 | 출처 | URL 검증 결과 |
|------|------|-------------|
| "Adaptive Routing 30~40% 비용 절감" | G-04 (Techment 블로그) | URL 검증 시 해당 수치 **미발견** — 페이지는 Adaptive RAG 비용 최적화 원리를 서술하나 30~40% 수치 없음 |
| "CRAG 엔터프라이즈 배포 표준 정착" 근거 | G-04 | 동일 — TRL 7~8 수준 근거 불확인 |

> 이 수치(30~40%)는 보고서 전반에 걸쳐 반복 인용됨 (§2 기술표, §4 3B 분석, §5 최종 제언, §6 사업포텐셜). G-04 URL 내에서 해당 수치를 확인할 수 없어 근거가 취약하다.

### G-16 핵심 수치 미확인 (심각)

| 주장 | 출처 | URL 검증 결과 |
|------|------|-------------|
| "Gartner 예측: Conversational AI 콜센터 인건비 $80B 절감" | G-16 (Invoca 블로그) | URL 검증 시 해당 수치 **미발견** — 페이지는 Gartner 85% 리더 인용만 있음. $80B 절감 수치 없음 |

> 이 수치는 §5 최종 제언, §6 사업포텐셜에 Gartner 예측으로 인용됨. 실제 Gartner 원본 없이 블로그 2차 인용인데, 그 블로그에서도 수치가 확인되지 않음.

### G-19 핵심 수치 미확인

| 주장 | 출처 | URL 검증 결과 |
|------|------|-------------|
| "Databricks Mosaic AI 7x 비용 절감" | G-19 (Databricks 제품 페이지) | URL 검증 시 제품 마케팅 콘텐츠 로드 불가 — 수치 확인 불가 |

> URL은 JavaScript 렌더링 의존 페이지로 접근 실패. 수치의 원본 소스 불명.

### AT&T 40% 정확도 향상 — 인용 맥락 불일치 (경미)

| 주장 | 출처 | 검증 결과 |
|------|------|---------|
| "AT&T NeMo 적용 후 정확도 40% 향상" [E-05][G-21] | NVIDIA Case Study | NVIDIA 페이지 확인: 40% 향상은 NeMo Retriever 단독이 아닌 NeMo Curator + Customizer + Evaluator + Retriever **전체 파이프라인** 적용 결과. "post-training" 기준 명시 |

> 리포트는 이를 RAG/Retriever 효과로 서술하나, 실제로는 fine-tuning 포함 전체 파이프라인 효과임. RAG의 단독 기여 과대표현 위험.

### A-RAG 논문 수치

| 주장 | 출처 | 검증 결과 |
|------|------|---------|
| "A-RAG HotpotQA 94.5%, 2WikiMultiHop 89.7%" | P-01 (arXiv 2602.03442) | arXiv 초록 페이지 및 PDF 추출에서 수치 미확인 — 논문은 실재하나 본문 실험 결과 섹션 접근 불가. 수치의 정확성 검증 불가 |

### VoiceAgentRAG 수치

| 주장 | 출처 | 검증 결과 |
|------|------|---------|
| "캐시 히트 316배 속도, 캐시 히트율 75%" | P-02 (arXiv 2603.02206) | arXiv 초록에서 수치 미확인 — 논문 실재 확인되나 구체적 수치 검증 불가 |

### 채점표 합산 검증

| 항목 | 세부1 | 세부2 | 세부3 | 세부4 | 소계 | 검증 |
|------|------|------|------|------|------|------|
| 고객가치 | 8 | 8 | 6 | 6 | 28 | PASS |
| 시장매력도 | 9 | 9 | 7 | 8 | 33 | PASS |
| 기술경쟁력 | 8 | 5 | 6 | 5 | 24 | PASS |
| 경쟁우위 | 4 | 6 | 5 | 6 | 21 | PASS |
| 실행가능성 | 5 | 7 | 7 | 6 | 25 | PASS |
| **총합** | | | | | **131** | **PASS** |

총점 합산 오류 없음.

---

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "Adaptive Routing 30~40% 비용 절감"
    current_sources: 1
    source_verification: UNCONFIRMED (G-04 URL에서 수치 미발견)
    suggested_keywords: ["Adaptive RAG cost reduction percentage", "query routing RAG cost savings enterprise"]
  - claim: "Gartner 예측 2026년 Conversational AI 콜센터 인건비 $80B 절감"
    current_sources: 1
    source_verification: UNCONFIRMED (G-16 URL에서 수치 미발견)
    suggested_keywords: ["Gartner conversational AI contact center savings 80 billion", "Gartner call center labor cost reduction 2026"]
  - claim: "Databricks Mosaic AI Storage-Optimized Vector Search 7x 비용 절감"
    current_sources: 1
    source_verification: URL_INACCESSIBLE
    suggested_keywords: ["Databricks Mosaic AI vector search cost 7x", "Databricks RAG cost optimization benchmark"]
  - claim: "Multi-hop Agentic RAG 57%+ 프로덕션 채택"
    current_sources: 0
    source_verification: NO_CITATION
    suggested_keywords: ["Multi-hop RAG production adoption rate 2024 2025", "Agentic RAG enterprise deployment statistics"]
```

---

## 3. 논리 검증

### SMART Test → Conditional Go 판정 일관성

| SMART 기준 | 판정 | 점수 기반 근거 | 일관성 |
|-----------|------|-------------|------|
| Specific | 충족 | 고객가치 세부1·2 각 8점 | PASS |
| Measurable | 충족 | 업계 벤치마크 명시 | PASS |
| Achievable | 조건부 충족 | 기술경쟁력 8점이나 경쟁우위 4점 | PASS — 조건부 반영 |
| Relevant | 강하게 충족 | 규제 드라이버, 시장매력도 33점 | PASS |
| Time-bound | 충족 | 로드맵 제시 | PASS |

Conditional Go (120~159 범위) 판정 131점 기준 적절. 범위 경계 조건 충족.

### 3B 전략 논리 점검

| 로직 | 근거 | 판정 |
|------|------|------|
| 차별화 중요도 7 < 8 → Build 단독 불충분 | 기준값 8이 어디서 왔는지 미명시 — 임의 기준값 | 경미 (기준 출처 불명) |
| 시장 긴급도 8 ≥ 8 → BUY 고려 | 동일 — 기준값 8 임의 | 경미 |
| 기술 격차 < 2년 → BORROW 적합 | "1~2년"을 "< 2년"으로 단정. 2년 시나리오 제외 논거 없음 | 경미 |
| Buy 제외: Telco RAG 전문 기업 인수 대상 부재 | 인수 대상 부재 주장에 출처 없음 — 단정적 서술 | 경미 |

전반적으로 Borrow+Build 결론 자체의 방향성은 제시된 데이터와 정합하나, 의사결정 매트릭스의 기준값(임계값 8)이 문서 내 미정의 상태.

### 리스크-기회 분석 균형

리스크 4건(프로덕션 실패, 플랫폼 종속, 인력, 컨텍스트 윈도우)과 강점 다수가 균형적으로 제시됨. 리스크 확률·영향도 명시(M/H 등). 논리 검증 PASS.

---

## 4. 편향 검증

### 벤더/기술 편향

| 항목 | 평가 |
|------|------|
| Adaptive RAG에 대한 서술 | 리스크(프로덕션 실패율 90%, 컨텍스트 윈도우 대체 가능성) 명시 — 균형 유지 |
| SKT/KT 경쟁사 평가 | Behind 인정하되 CRAG 세부 구현 미공개 영역에서 차별화 가능성 언급 — 균형 |
| 순수 LLM 파인튜닝 대안 | 대체제 존재를 고객가치 리스크로 명시 — PASS |
| WTP 미검증 | [D] 명시 — PASS |

### 자사 유리 방향 왜곡

"한국어 Telco 특화 CRAG" 차별화 주장은 근거(SKT/KT 미공개 영역)를 명시하였으나, 자사 실제 역량 데이터가 없는 상태에서 "차별화 가능"이라는 방향성이 선험적으로 설정되어 있음. 보고서 자체가 [D] 태그와 "내부 데이터 필요"를 명시하고 있어 과도한 편향은 아니나, 주의 수준.

### 데이터 부족 항목 처리

5개 [D] 항목(SOM, 특허, 표준/인증, 내부 역량, 경쟁사 대응력) 모두 [D] 명시 및 보강 키워드 제시. 편향 검증 PASS.

---

## 이슈 목록

| # | 심각도 | 유형 | 내용 | 비고 |
|---|--------|------|------|------|
| 1 | 심각 | 수치 미확인 | G-04 (Techment) URL에서 "Adaptive Routing 30~40% 비용 절감" 수치 미발견. 보고서 전반 4회 이상 반복 인용 | URL 직접 검증 실패 |
| 2 | 심각 | 수치 미확인 | G-16 (Invoca) URL에서 "Gartner $80B 절감" 수치 미발견. 블로그 2차 인용인데 원 블로그에도 없음 | URL 직접 검증 실패 |
| 3 | 경미 | 고아 소스 | G-22 (Klover.ai Verizon 분석), P-04 (ACM 멀티턴 Survey) — References 등재 but 본문 미인용 | 2건 |
| 4 | 경미 | 미인용 수치 | "Multi-hop Agentic RAG 57%+ 프로덕션 채택" — 본문 인용 없음, [D] 미표기 | §2 기술 성숙도 맵 |
| 5 | 경미 | 인용 맥락 불일치 | AT&T 40% 향상(E-05/G-21) — RAG 단독 효과가 아닌 NeMo 전체 파이프라인(fine-tuning 포함) 효과임. RAG 기여 과대 표현 위험 | NVIDIA 페이지 직접 확인 |
| 6 | 경미 | 수치 미검증 | G-19 Databricks "7x 비용 절감" — URL JavaScript 렌더링으로 수치 확인 불가 | JS 의존 페이지 |

---

## 결론

채점 합산(131/200), References 테이블 구조, [D] 태그 활용, 리스크-기회 균형 측면은 양호하다. 그러나 핵심 수치 2건(G-04 Adaptive Routing 30~40% 절감, G-16 Gartner $80B 절감)이 URL 직접 검증에서 확인되지 않았으며, 이 수치들이 보고서 결론(Borrow+Build 시장성 근거)에 반복 사용되므로 심각 이슈로 분류한다. 고아 소스 2건과 미인용 수치 1건은 인용 체계의 경미한 미완결이다. 최종 판정은 **PARTIAL** — 핵심 수치의 소스 재확인 후 PASS 격상 가능.
