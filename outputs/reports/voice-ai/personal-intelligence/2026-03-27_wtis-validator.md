---
type: wtis-validator
target: 2026-03-27_wtis-skill1.md
date: 2026-03-27
validator_status: partial
---

# Validation Report

## 검증 요약

- **상태**: PARTIAL (critical 2건, minor 4건, 고아 소스 5건)
- **총점 합산**: 정확 (26+30+23+23+26 = 128/200, 자체 검증 포함)
- **판정 일치**: Conditional Go (120~159 범위) 정확
- **주요 이슈**:
  1. G-11 "ROI 4배" 주장 — 원문 페이지에 해당 수치 없음 (Critical)
  2. G-05 Character.ai MIT TR 선정 — 소스 귀속 오류, 실제 출처는 MIT TR 공식 페이지 (Critical)
  3. G-07 단독으로 "2026.3 무료 개방" 미지지 (Minor)
  4. G-14 "$221M 상반기" 표기 — 원문은 "2025년 7월 기준 누적"으로 시점 표기 부정확 (Minor)
  5. 고아 소스 5건: G-12, G-18, G-23, P-03, P-04 (References 등재 but 본문 미인용)

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | G(24건), E(6건), P(5건), T(0건), I(0건) |
| 모든 [N] 인용 매칭 | ✅ | 본문 인용 코드 전량 References 테이블에 정의됨 |
| 미인용(고아) 소스 발견 | ❌ | G-12, G-18, G-23, P-03, P-04 (5건) — 테이블 등재 후 본문 미인용 |

### 고아 소스 상세

| 코드 | 내용 | 비고 |
|------|------|------|
| G-12 | Tech Startups — Character.ai 매각/펀딩 논의 | 본문 어디서도 인용되지 않음 |
| G-18 | Tracxn — Meela 시니어 AI 컴패니언 | 본문 어디서도 인용되지 않음 |
| G-23 | CNBC — 2025 M&A $4.9조 | 본문 어디서도 인용되지 않음 |
| P-03 | ProPerSim 논문 | 본문 어디서도 인용되지 않음 |
| P-04 | Situation Graph Prediction 논문 | 본문 어디서도 인용되지 않음 |

---

## 2. 수치 검증

| 수치 | 소스 수 | 판정 | 비고 |
|------|---------|------|------|
| AI 컴패니언 TAM $37.1B(2025), CAGR 31% | 3 (G-01/G-02/G-03) | ✅ [A] | 3개 리서치사 수렴 확인 |
| AI Assistant SAM $3.35B→$21.1B, CAGR 44.5% | 1 (G-04) | [B] | MarketsandMarkets 단일, 원문 확인됨 |
| 통신사 AI 투자 ROI 4배 | 1 (G-11) | ❌ Critical | G-11(Tredence) 원문에 "4배" 없음. "1.7x~3.4x" 언급만 확인됨 |
| 80% 고객 데이터 공유 의향 | 1 (G-11) | [B] | Tredence 원문 확인됨 |
| Vodafone TOBi 고객 문의 70% 자동 처리 | 1 (G-11) | [B] | Tredence 원문 확인됨 |
| AI 컴패니언 앱 연간 $120M 수익 | 1 (G-14) | [B] | TechCrunch 원문 확인됨 |
| AI 컴패니언 앱 상반기 소비자 지출 $221M | 1 (G-14) | ⚠️ Minor | 원문은 "2025년 7월 기준 누적" — 본문의 "상반기" 표기 부정확 |
| 상위 10% 앱 89% 수익 집중 | 1 (G-14) | [B] | WebSearch로 교차 확인됨 (TechCrunch 원문 일부 미로드) |
| Mem0 GitHub 41K 스타 | 1 (G-09) | [B] | TechCrunch 기사에는 스타 수 없음; Mem0 논문(P-02)에서 확인 필요 |
| Mem0 LOCOMO 벤치마크 26% 향상 | 2 (G-09+P-02) | [B] | P-02 arxiv 원문 확인됨 (G-09는 미확인, P-02에서 지지) |
| Mem0 $24M 투자 | 1 (G-09) | [B] | TechCrunch 원문 확인됨 |
| Microsoft Inflection $650M | 1 (G-10) | [B] | DeepLearning.AI 원문 확인됨 |
| Hume AI Series B $50M | 1 (E-01) | [B] | References에 발표 언급만 있고 URL 없음 — E 계열 URL 미등재 |
| Google Gemini 2026.3 무료 개방 | 1 (G-07) | ⚠️ Minor | G-07(Fortune 2026-01-14)은 무료화 일정 미언급, 실제 무료화는 3/17 확인됨(G-08 범위 밖). 단독 소스로 "3월 무료 개방" 주장 미지지 |
| 채점 총점 128/200 | 내부 계산 | ✅ | 세부 합산 재검증 완료 |

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "AI 투자 통신사의 ROI가 일반 디지털 투자 대비 약 4배"
    current_sources: 1 (G-11, 원문 불일치)
    suggested_keywords: ["telecom AI investment ROI", "McKinsey telecom AI return", "telecom digital investment ROI benchmark"]

  - claim: "Google Gemini Personal Intelligence 무료 개방(2026.3)"
    current_sources: 1 (G-07, 무료화 일정 미지지)
    suggested_keywords: ["Gemini personal intelligence free tier rollout March 2026", "9to5google gemini personal intelligence free"]

  - claim: "AI 컴패니언 앱 소비자 지출 2025년 상반기 $221M"
    current_sources: 1 (G-14, 시점 표기 불일치)
    suggested_keywords: ["AI companion app consumer spending 2025 H1", "data.ai sensor tower ai companion revenue 2025"]
```

---

## 5. URL-Content 검증

| # | URL 상태 | 본문 주장 | 판정 | 비고 |
|---|---------|---------|------|------|
| G-01 | 200 OK | AI 컴패니언 시장 2024년 $28.19B, CAGR 30.8% | ✅ 일치 | |
| G-02 | 200 OK | AI 컴패니언 시장 2025년 $37.12B, CAGR 31.0% | ✅ 일치 | |
| G-03 | 200 OK | AI 컴패니언 시장 2025년 $37.73B, 2034년 $435.9B, CAGR 31.24% | ✅ 일치 | |
| G-04 | 200 OK | AI Assistant 시장 $3.35B→$21.11B, CAGR 44.5% | ✅ 일치 | |
| G-05 | 200 OK | Character.ai MIT Technology Review 10대 혁신 기술 선정 | ❌ 불일치 | Skywork AI 블로그 원문에 MIT TR 내용 없음. 실제 출처: MIT TR 공식(https://www.technologyreview.com/2026/01/12/1130018/ai-companions-chatbots-relationships-2026-breakthrough-technology/) — "AI Companions" 카테고리로 선정됨 |
| G-06 | 200 OK | Apple Intelligence Personal Context 2025.10 기준 미출시, 지연 | ✅ 일치 | |
| G-07 | 200 OK | Gemini Personal Intelligence Gmail·Photos·YouTube 연동 | ✅ 일치 | 단, "2026.3 무료 개방" 일정은 G-07에 없음 ⚠️ |
| G-08 | 200 OK | Gemini 타 AI 앱 메모리 임포트 도구 출시 | ✅ 일치 | |
| G-09 | 200 OK | Mem0 $24M 투자 유치 | ✅ 일치 | GitHub 41K 스타·LOCOMO 26% 수치는 기사에 없음; P-02에서 확인 |
| G-10 | 200 OK | Microsoft $650M Inflection 라이선스, Suleyman 영입 | ✅ 일치 | |
| G-11 | 200 OK | 통신사 AI 투자 ROI 4배, 80% 고객 데이터 공유 의향 | ❌ 불일치 | 80% 데이터 공유는 확인됨. ROI 4배는 페이지에 없음. "1.7x~3.4x" 언급이 전부 |
| G-12 | 200 OK | Character.ai 매각/펀딩 논의 (고아 소스) | 🔵 미인용 | 본문에서 인용 없음 |
| G-13 | 200 OK | Graphiti 실시간 시간적 지식 그래프 | ✅ 일치 | |
| G-14 | 200 OK | AI 컴패니언 앱 연간 $120M, 상반기 $221M, 89% 수익 집중 | ⚠️ 부분 일치 | $120M 확인. $221M은 "2025년 7월 기준 누적"으로 "상반기" 표기 부정확. 89% 집중은 WebSearch 교차 확인 |
| G-15 | 🔗 접근 불가 | Replika 펀딩 $11M, 매출 $3M | 🔗 미확인 | Tracxn 페이지 로드 실패 (CSS만 반환) |
| G-16 | 🔗 접근 불가 | Samsung Galaxy AI MWC 2026, Bixby+Perplexity | 🔗 미확인 | 연결 타임아웃 2회. Samsung Newsroom 공식 페이지로 신뢰도 양호하나 원문 미확인 |
| G-17 | 200 OK | Apple LLM Siri 2026 상반기 출시 예정 | ✅ 일치 | 단, "2026 상반기"는 추측(Spring 2026 rumors), Apple 공식은 "2026년" 확인만 |
| G-18 | 🔗 접근 불가 | Meela Seed $3.5M (고아 소스) | 🔗 미확인 + 미인용 | Tracxn 페이지 로드 실패 |
| G-19 | 🔗 접근 불가 | 온디바이스 AI 칩셋 확산 | 🔗 미확인 | 403 오류 |
| G-20 | 🔗 접근 불가 | Apple 프라이버시 우선 온디바이스 AI | 🔗 미확인 | 403 오류 |
| G-21 | 200 OK | Lenovo Qira 앰비언트 AI, 온디바이스 실행 | ✅ 일치 | |
| G-22 | 200 OK | KT AI 빅또리 비서(KBO 도메인 한정) | ⚠️ 부분 일치 | KT AI 빅또리 비서 확인. AI 통화비서는 해당 기사에 없음. 본문 "AI 통화비서, AI 빅또리 비서" 중 통화비서 소스 미지지 |
| G-23 | 🔗 접근 불가 | 2025 M&A $4.9조 +40% YoY (고아 소스) | 🔗 미확인 + 미인용 | 403 오류 |
| G-24 | 200 OK | EU Digital Omnibus GDPR/AI Act 개정 | ✅ 일치 | |
| E-01~E-06 | URL 없음 | 전 E계열 출처 | 🔗 미확인 | E계열 테이블에 URL이 없고 검색 키워드만 제공됨 — 직접 검증 불가 |
| P-01 | 200 OK | ContextAgent 웨어러블 센서 기반 선제적 LLM 에이전트 | ✅ 일치 | NeurIPS 2025 수락 확인 |
| P-02 | 200 OK | Mem0 LOCOMO 벤치마크 26% 향상, 90% 토큰 절감 | ✅ 일치 | |
| P-03 | 200 OK | ProPerSim 사용자-어시스턴트 시뮬레이션 (고아 소스) | 🔵 미인용 | 논문 내용 확인됨, 본문에서 인용 없음 |
| P-04 | 200 OK | Situation Graph Prediction (고아 소스) | 🔵 미인용 | 논문 내용 확인됨, 본문에서 인용 없음 |
| P-05 | 200 OK | MemX 로컬 우선 프라이버시 보존 아키텍처 | ✅ 일치 | |

---

## 3. 논리 검증

**채점 합산 정확성**: ✅
- 고객가치: 7+7+5+7 = 26
- 시장매력도: 9+9+6+6 = 30
- 기술경쟁력: 7+5+6+5 = 23
- 경쟁우위: 4+7+5+7 = 23
- 실행가능성: 5+7+7+7 = 26
- 총점: 26+30+23+23+26 = 128/200
- **판정 Conditional Go (120~159 범위): 정확**

**3B 의사결정 로직**: ⚠️ 주의 필요
- 코드 블록 내 `IF differentiation_importance=7 > 8` 조건이 BORROW 결론으로 이어지나, 이후 "통신사 데이터 기반 차별화 레이어는 외부 조달 불가"라는 별도 근거로 Build 추가를 정당화. 이 전환 논리는 타당하나, 원래 의사결정 트리와 별개의 주관적 판단이 개입된 점은 명시적 한계로 기술되어 있어 수용 가능.

**결론↔근거 일치**: ✅
- Borrow + Build 권고는 분석 내용(오픈소스 가용, 통신 데이터 독점성)으로 지지됨.
- "SKT 대비 12개월 이상 후발" 주장은 인용 근거(E-05, E-06) 있음.

**논리적 도약**: 없음

---

## 4. 편향 검증

**리스크 균형**: ✅
- 강점과 리스크를 각 항목별로 병렬 제시. 빅테크 무료화 압박, 프라이버시 규제, SKT 선점, 내부 역량 부족 등 4개 핵심 리스크 명시.

**데이터 부족 인정**: ✅
- 데이터 부족 항목 4개를 명시하고 신뢰도 Low로 자체 하향. 보강 키워드도 제공.

**낙관 편향**: 낮음
- SOM을 "데이터 부족"으로 처리하고 [추정, 근거부족] 태그 부여. 시장 타이밍 점수도 "최적 시점은 지남"으로 현실적 평가.

**경쟁사 분석 단면성**: ⚠️ 경미
- KT 경쟁 분석이 단일 기사(G-22)에만 의존하며, AI 통화비서 관련 소스가 해당 기사에 포함되지 않음. KT 경쟁력 과소 평가 가능성.

---

## 상세 이슈 목록

| # | 유형 | 심각도 | 내용 | 권고 |
|---|------|--------|------|------|
| I-01 | URL-Content 불일치 | Critical | G-11(Tredence) "AI 투자 ROI 4배" — 원문에 없음. 원문 수치는 1.7x~3.4x | G-11 인용 삭제 또는 McKinsey/Accenture 등 2차 소스로 교체 |
| I-02 | URL-Content 불일치 | Critical | G-05(Skywork AI 블로그) "Character.ai MIT TR 10대 혁신기술" — 해당 블로그에 없음 | 대안 출처: https://www.technologyreview.com/2026/01/12/1130018/ai-companions-chatbots-relationships-2026-breakthrough-technology/ |
| I-03 | 수치 시점 오류 | Minor | G-14 "$221M 상반기 소비자 지출" — 원문은 "2025년 7월 기준 누적" (상반기 수치는 $82M) | "2025년 7월 기준 누적 $221M" 또는 "상반기 $82M"으로 수정 |
| I-04 | 단일소스 불지지 | Minor | G-07 단독으로 "2026.3 무료 개방" 미지지 (G-07은 2026-01-14 기사로 무료화 미언급) | G-08 또는 9to5google 기사 추가 인용 권고 |
| I-05 | 고아 소스 | Minor | G-12(Character.ai 매각), G-18(Meela), G-23(M&A 붐) — 본문 미인용 | References에서 제거하거나 본문에 인용 추가 |
| I-06 | 고아 소스 | Minor | P-03(ProPerSim), P-04(Situation Graph) — 본문 미인용 | References에서 제거하거나 기술 성숙도 섹션 등에 인용 추가 |
| I-07 | 소스 제한 | 참고 | E계열 6건 전량 URL 없이 검색 키워드만 제공 — 독립 검증 불가 | E계열은 원문 URL 등재 권고 |
| I-08 | 소스 접근 불가 | 참고 | G-15(Tracxn Replika), G-16(Samsung MWC), G-19, G-20, G-23 — 403/타임아웃 | Samsung G-16은 공식 Newsroom으로 신뢰도 양호. G-15/G-19/G-20 내용 재확인 권고 |
| I-09 | 소스 부분 일치 | 참고 | G-22(스포츠서울) — KT AI 통화비서 소스로 활용하나 해당 기사는 빅또리 비서만 다룸 | KT AI 통화비서 별도 소스 추가 |

---

## 결론

**최종 판정: PARTIAL**

채점 합산(128/200)과 판정(Conditional Go) 자체는 정확하다. 그러나 사업 잠재성 논거로 반복 사용된 G-11 "ROI 4배" 수치가 원문에 존재하지 않는 Critical 오류가 있고, G-05 소스 귀속도 블로그 원문이 아닌 MIT TR 공식 페이지로 교체가 필요한 Critical 오류다. 수치 부정확(G-14 시점 오류), 단일 소스 미지지(G-07 무료화 일정), 고아 소스 5건(G-12/G-18/G-23/P-03/P-04)은 Minor이나 누적 시 신뢰도 하락 요인이다. E계열 URL 전량 미등재 문제는 향후 검증 가능성을 제한하므로 개선이 권고된다.
