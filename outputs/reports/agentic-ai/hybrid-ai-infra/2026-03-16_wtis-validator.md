---
type: wtis-validator
target: skill1.md
date: 2026-03-16
---

# WTIS Validator: Hybrid AI Infra

## 검증 요약
- 최종 판정: **PARTIAL**
- 검증 신뢰도: Medium
- 이슈 건수: 9건 (심각 2, 경미 7)

---

## 1. 인용 검증

### References 테이블 현황
- E-xx: E-01~E-12 (12건 등재)
- G-xx: G-01~G-21, G-24 (G-22/G-23 없음, 22건 등재)
- P-xx: P-01~P-06 (6건 등재)
- T-xx: 데이터 없음 (테이블 유지, 빈 행 명시)
- I-xx: 데이터 없음 (테이블 유지, 빈 행 명시)

### 본문 인용 ↔ References 교차 확인

**본문에서 실제 인용된 코드:**
- E계열: E-01, E-02, E-04, E-05, E-06, E-07, E-08, E-09, E-11, E-12 (10건)
- G계열: G-01, G-02, G-03, G-04, G-05, G-06, G-08, G-09, G-10, G-11, G-12, G-13, G-14, G-15, G-16, G-17, G-18, G-19, G-20, G-21, G-24 (21건)
- P계열: P-01, P-05, P-06 (3건)

**고아 소스 (References 등재 but 본문 미인용):**
| 코드 | 출처 | 비고 |
|------|------|------|
| E-03 | Korea IT Times — KT MWC 2026 기사 | 경쟁사 표 KT 행에 [E-03] 인용 있음 (line 80) — **인용 확인, 오검출 아님** |
| E-10 | Apple ML Research — Core ML Llama 3.1 | 본문 어디에도 [E-10] 인용 없음 → **고아 소스** |
| G-07 | Qualcomm Developer — MWC Talent Arena 2026 | 본문 어디에도 [G-07] 인용 없음 → **고아 소스** |
| P-02 | Han et al. — E2E Intelligence in 6G | 본문 어디에도 [P-02] 인용 없음 → **고아 소스** |
| P-03 | Shokouhi & Wong — Agentic AI for O-RAN | 본문 어디에도 [P-03] 인용 없음 → **고아 소스** |
| P-04 | arXiv — Agent Memory Below the Prompt | 본문 어디에도 [P-04] 인용 없음 → **고아 소스** |

> 재확인: E-03은 경쟁사 표 KT 행 `[E-03][E-04][E-12][G-02]`에 인용됨. 고아 소스 최종 확정: **E-10, G-07, P-02, P-03, P-04 (5건)**

**결손 인용 (본문 인용 but References 미등재):** 없음 — 모든 본문 인용이 테이블에 존재함.

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | E/G/P/T/I 5개 섹션 모두 존재 |
| 모든 [N] 인용 매칭 | ✅ | 본문 인용 전량 테이블에 존재 |
| 미인용 소스(고아) 발견 | ❌ | E-10, G-07, P-02, P-03, P-04 — 5건 |

---

## 2. 수치 교차검증

### 시장 규모 수치

| 수치 주장 | 본문 표기 | 검증 결과 | 소스 수 | 판정 |
|-----------|----------|----------|---------|------|
| Edge AI TAM (시작점) | $47.6B (2026) | Precedence Research 실제 페이지 확인 결과: "2025년 $25.65B → 2034년 $143.06B, CAGR 21.04%" — 시작 연도·금액·CAGR **모두 불일치** | 1 | **심각 불일치** |
| Edge AI TAM (종점) | $143B (2034) | Precedence Research $143.06B(2034) — 종점 수치와 연도는 일치 | 2 (Precedence + STL) | 종점만 일치 |
| Edge AI CAGR | 33.3% | Precedence Research 실제 CAGR **21.04%** — 본문 33.3%와 **12%p 이상 차이** | 1 | **심각 불일치** |
| AI-RAN TAM (시작점) | $3.81B (2026) | Precedence Research 실제: "2025년 $2.96B" — 기준 연도 불일치. 2026년 값이라면 내부 성장률 반영이 필요하나 근거 미제시 | 1 | 경미 불일치 |
| AI-RAN TAM (종점) | $37.2B (2035) | Precedence Research "$37.19B by 2035" — 일치 | 1 | PASS |
| AI-RAN CAGR | 28.8% | Precedence Research "28.79% during 2026-2035" — 일치 | 1 | PASS |
| MEC TAM | $7.78B (2025) → $175.8B (2033), CAGR 47.7% | WebFetch 미검증 (403 에러). 본문 스스로 "과대 가능성" 명시 | 1 | 단일 소스, 주의 |
| STL Partners Edge AI | $157B (2030) | STL Partners 페이지 확인: "$157B by 2030" — 일치 | 1 | PASS |
| 과기정통부 AI·ICT R&D | 1조 2,040억원 (2026) | WebFetch 미검증. 단일 소스 [B] | 1 | [B] 수용 |
| Nokia AI-RAN 상용화 | 2027년 | G-03(Fierce Network), E-05(Nokia Newsroom) 복수 출처 — 일치 | 2 | PASS |
| NVIDIA AI-RAN Alliance | 130개사+ | NVIDIA 공식 페이지 확인: "over 130 participating companies" — 일치 | 2 | PASS |
| KT 믿:음 K | 2.3B Mini, 2025-07 | E-12 참조. E-03(Korea IT Times) 보조 | 2 | PASS |

### 채점표 합산 검증

| 항목 | 세부1 | 세부2 | 세부3 | 세부4 | 소계 | 검증 |
|------|------|------|------|------|------|------|
| 고객가치 | 7 | 7 | 5 | 5 | **24** | 7+7+5+5=24 ✅ |
| 시장매력도 | 9 | 9 | 8 | 9 | **35** | 9+9+8+9=35 ✅ |
| 기술경쟁력 | 8 | 5 | 8 | 9 | **30** | 8+5+8+9=30 ✅ |
| 경쟁우위 | 4 | 6 | 7 | 5 | **22** | 4+6+7+5=22 ✅ |
| 실행가능성 | 5 | 5 | 6 | 4 | **20** | 5+5+6+4=20 ✅ |
| **총점** | | | | | **131** | 24+35+30+22+20=131 ✅ |

채점표 합산은 모두 정확하다.

### CAGR 재계산

**Edge AI CAGR 검증 (Precedence Research 실제 수치 기준):**
- 실제 수치: $25.65B(2025) → $143.06B(2034), 9년
- 실제 CAGR = (143.06/25.65)^(1/9) - 1 ≈ 21.0%
- 본문 주장: CAGR 33.3% — **12%p 과대 계상**
- 본문이 인용한 시작점 "$47.6B(2026)"은 Precedence Research 페이지의 실제 수치($25.65B, 2025)와 상이하며, 이 오류가 CAGR 불일치의 원인으로 추정됨.

**AI-RAN CAGR 검증 (Precedence Research 실제 수치 기준):**
- 실제 수치: $2.96B(2025) → $37.19B(2035), 10년, CAGR 28.79%
- 본문 시작점 "$3.81B(2026)"은 2025년 값에 1년 성장률 적용 시 나올 수 있으나, 기준 연도를 2026으로 표기하면서 원본 Precedence Research의 2026~2035 예측 기간 CAGR 28.79%와 충돌함.
- 결과적으로 CAGR 수치(28.8%)는 맞으나 시작점 금액($3.81B)은 출처 원본($2.96B in 2025)과 불일치.

### 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "Edge AI TAM $47.6B (2026), CAGR 33.3%"
    current_sources: 1
    note: "Precedence Research 실제 페이지 수치($25.65B, 2025, CAGR 21.04%)와 불일치. 제3 리서치사(IDC, Gartner, MarketsandMarkets) 비교 검증 필요"
    suggested_keywords: ["Edge AI market size 2026 IDC", "Edge AI forecast CAGR 2034 Gartner", "edge computing AI market size 2026"]
  - claim: "MEC TAM $7.78B(2025) → $175.8B(2033), CAGR 47.7%"
    current_sources: 1
    note: "단일 소스(Precedence Research), 본문 스스로 과대 추정 가능성 인정. 교차검증 미완료"
    suggested_keywords: ["MEC market size 2033 MarketsandMarkets", "Multi-access edge computing forecast 2033 IDC", "MEC CAGR 2033"]
  - claim: "SAM $3~4B (MEC 레이어 40~50%), SOM $120~200M (2025)"
    current_sources: 0
    note: "자체 추정 [D]. 근거 산식 미제시"
    suggested_keywords: ["Korean telco edge AI revenue 2025", "통신사 MEC 서비스 매출 국내"]
  - claim: "콜센터 AI 자동화 상담사 업무 효율 30%+ 개선"
    current_sources: 1
    note: "E-04(KT Agentic AICC 기사)와 G-14(Picovoice Falcon 블로그), G-19(AssemblyAI 비교)가 인용되나 30%+ 개선 수치의 직접 출처 불명확"
    suggested_keywords: ["contact center AI automation efficiency improvement statistics", "AI AICC 상담사 효율 30% 연구"]
```

---

## 3. 논리 검증

### SMART Test ↔ 최종 판정 일관성

- Specific(부분 충족), Time-bound(부분 충족)인 상태에서 Conditional Go 131점 판정은 논리적으로 적합하다. SMART 부분 충족이 점수에 반영(실행가능성 20/40, 고객가치 24/40)되어 있어 일관성 있음.

### 3B 전략 논리

- Speaker Diarization "Buy + Build" 결정: Market urgency 8/10, Tech gap 1년 근거 → Buy 결론 논리적.
- On-Device sLM "Borrow + Build" 결정: Differentiation 7/10이나 internal capability 부족 → Borrow 결론 논리적.
- Edge AI "Borrow" 결정: Market urgency 5/10, 킬러앱 부재 → 하이퍼스케일러 파트너십 Borrow 논리적.
- AI-RAN "Borrow" 결정: 전 세계 통신사 공통 대기 상태로 Tech gap 동등 → Borrow 논리적.

단, On-Device sLM 3B 결정 섹션(line 119~129)에서 "Borrow + Build"로 결론을 제시하나, 5. 최종 제언(line 170~177) 요약란에서는 "Borrow(오픈소스+NPU 파트너) + Build(통신 Fine-Tuning)"로 표기되어 내용상 일치함.

### TRL 차이의 종합 판정 반영

- TRL 9(Speaker Diarization) → Buy 즉시 수확, TRL 6~7(AI-RAN) → 중기 Watch/Borrow 구분이 명확히 반영됨.
- 4사분면 배치도(베팅/유지/Watch)와 채점 결과 및 3B 전략이 TRL에 기반하여 일관됨. PASS.

### 논리적 도약 여부

- "통신사 인증 + 온디바이스 AI 결합은 고유 가치 제안"(line 216): 이 주장은 [E-02][G-13] 인용이나, 두 소스 모두 SKT 기사 및 Cactus 기술 가이드로 "고유 가치 제안"이라는 결론을 직접 지지하지 않음. **증거보다 강한 주장 — 경미 이슈.**
- "5G 슬라이싱과 결합 시 SLA 보장 가능"(line 217): [P-06][G-16] 인용이나 P-06(Edge-First LM Inference)은 SLA 보장이 아닌 트레이드오프 분석 논문. G-16은 시장 리서치 보고서. SLA 보장 주장의 직접 근거 없음. **경미 이슈.**
- SAM/SOM 산출 근거 미제시: 자체 추정 [D]라고 표기했으나, 산출 기준(MEC 레이어 40~50%라는 비율의 출처)이 없음. [D] 태그 부착으로 불확실성을 인지했으나 근거 산식 없음. **경미 이슈.**

---

## 4. 편향 검증

### 벤더/기술 편향

- Nokia(E-05, G-03)와 NVIDIA(E-08, G-06) 중심의 AI-RAN 생태계 서술이 대부분이나, Ericsson(E-06, G-04) 자체 ASIC 전략도 균형 있게 포함됨.
- Intel 불참(G-09)도 리스크로 명시. NVIDIA 단일 의존 리스크가 리스크 항목에 포함됨. **PASS.**

### 자사 포지션 편향

- 6개 역량 항목 모두 "Behind" 판정하고, 데이터 부족 항목을 낙관적으로 채점하지 않고 보수적(5/10) 처리함.
- 실행가능성 20/40(미흡) 평가는 자사 역량 미확인 상태에서 하향 처리된 것으로 편향 없음.

### 경쟁사 분석 균형

- SKT 우위(AI-RAN Alliance 이사회, ATHENA 6G)를 명시하고 자사 후발 포지션을 인정함.
- KT 자체 sLM(믿:음 K) 선행 사례가 Tech gap ~1년으로 정량화됨.
- 경쟁사 약점 서술 부재: Ericsson T-Mobile Cloud RAN 단계의 상세 약점, DT/T-Mobile의 6G Innovation Hub의 제한적 진행 상황 등은 서술 없음. 그러나 경쟁사 현황 표의 Stage/Timeline 컬럼이 이를 대신하므로 **경미 이슈 수준.**

### 데이터 부족 항목 처리

- 자사 특허, 파트너십, 내부 역량, 투자 ROI, 고객 WTP 5건을 모두 "데이터 부족"으로 명시하고 자동 신뢰도 하향(Medium) 적용. 근거 없는 추정 없음. **PASS.**

---

## 이슈 목록

| # | 심각도 | 유형 | 내용 | 근거 |
|---|--------|------|------|------|
| 1 | **심각** | 수치 불일치 | Edge AI TAM 시작점 "$47.6B(2026)", CAGR "33.3%"가 Precedence Research 실제 수치($25.65B, 2025, CAGR 21.04%)와 불일치 | Precedence Research edge-ai-market 페이지 직접 확인 |
| 2 | **심각** | 수치 불일치 | AI-RAN TAM 시작점 "$3.81B(2026)"이 Precedence Research 실제 기준연도($2.96B, 2025)와 불일치 | Precedence Research ai-ran-market 페이지 직접 확인 |
| 3 | 경미 | 고아 소스 | E-10(Apple Core ML Llama) — References 등재, 본문 미인용 | 전체 인용 추출 교차 확인 |
| 4 | 경미 | 고아 소스 | G-07(Qualcomm Developer Edge AI Workshops) — References 등재, 본문 미인용 | 전체 인용 추출 교차 확인 |
| 5 | 경미 | 고아 소스 | P-02(Han et al. 6G Networks) — References 등재, 본문 미인용 | 전체 인용 추출 교차 확인 |
| 6 | 경미 | 고아 소스 | P-03(Shokouhi & Wong O-RAN) — References 등재, 본문 미인용 | 전체 인용 추출 교차 확인 |
| 7 | 경미 | 고아 소스 | P-04(arXiv KV Cache) — References 등재, 본문 미인용 | 전체 인용 추출 교차 확인 |
| 8 | 경미 | 논리 | "통신사 인증 + 온디바이스 AI = 고유 가치 제안" 주장 — 인용 소스(E-02, G-13)가 이 결론을 직접 지지하지 않음 | E-02는 SKT 기사, G-13은 Cactus 기술 가이드 |
| 9 | 경미 | 논리 | "5G 슬라이싱과 결합 시 SLA 보장 가능" — 인용 P-06(트레이드오프 분석), G-16(시장 리서치)이 직접 근거 아님 | P-06 논문 주제 확인 |

---

## 결론

최종 판정: **PARTIAL**

핵심 근거: Edge AI 시장 규모 시작점($47.6B vs $25.65B)과 CAGR(33.3% vs 21.04%)이 인용 소스(Precedence Research) 실제 페이지 수치와 심각하게 불일치한다. 이 수치는 시장매력도 35/40(우수) 평가의 핵심 근거이므로, 만약 실제 CAGR 21%로 재계산하면 시장 매력도 점수가 하향 조정될 가능성이 있다. 다만 채점표 합산 자체는 정확하고, 논리 구조(TRL 기반 3B 전략, 판정 임계값 적용)는 내부 일관성이 있으며, 데이터 부족 항목에 대한 솔직한 [D] 태그 처리 및 신뢰도 하향 적용은 적절하다. 고아 소스 5건은 반복 발생 패턴(P계열 전량 미인용)이며 심각도는 낮다. 수치 오류 2건에 대한 원본 소스 재확인이 우선 보완 과제다.
