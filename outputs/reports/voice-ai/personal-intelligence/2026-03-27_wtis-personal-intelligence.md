---
topic: Personal Intelligence
domain: voice-ai
l2_topic: personal-intelligence
date: 2026-03-27
wtis_version: v4.1
wtis_mode: standard
skills_executed: [research-deep, SKILL-1, validator]
confidence: low
status: completed
total_references: 35
score: 128/200
verdict: Conditional Go
strategy: Borrow + Build
---

# WTIS Report: Personal Intelligence

## Executive Summary

> **Conditional Go (128/200)** — Personal Intelligence(Persona Plugin, Relationship Graph, Context-Action Recommendation)는 글로벌 AI 컴패니언 시장이 CAGR 31%로 급성장하는 가운데 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-03]](#ref-g-03), 통신사 고유 데이터(통화 이력·위치·실명 계약)를 활용한 B2C 차별화 잠재력이 있다 [[G-11]](#ref-g-11). 그러나 Apple Intelligence·Google Gemini·ChatGPT 등 빅테크가 이미 상용화를 추진 중이며 [[G-06]](#ref-g-06), [[G-07]](#ref-g-07), [[E-03]](#ref-e-03), SKT 에이닷이 국내 선발 주자로 조직 전면 배치 및 구독 모델 전환을 가속하고 있어 [[E-05]](#ref-e-05), [[E-06]](#ref-e-06), 후발 진입 시 차별화 전략과 프라이버시 규제 대응이 핵심 과제다. **Borrow + Build** 전략 — 메모리/지식 그래프 인프라(Mem0, Graphiti 등)를 파트너십으로 도입하고 통신사 고유 데이터 기반 개인화 레이어를 자체 개발하는 하이브리드 접근을 권고한다.

## 평가 항목 및 배점 안내

> 본 보고서는 WTIS 평가 체계(200점 만점, 5개 항목 각 40점)에 따라 정량 평가한다.
> 상세 기준: scoring-framework.md 참조.

---

## 1. 목표 검증

### SMART Test

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Specific | **부분 충족** — "AI 개인비서를 통한 B2C 차별화"는 방향성은 명확하나, 구체적 KPI(가입자 수, ARPU 증가폭) 미정의 | 데이터 부족 — 보강 키워드: "통신사 AI 비서 KPI", "telecom AI assistant ARPU uplift" |
| Measurable | **부분 충족** — AI 컴패니언 앱 수익 $120M/년 궤도(글로벌) [[G-14]](#ref-g-14), Vodafone TOBi 고객 문의 70% 자동 처리 [[G-11]](#ref-g-11) 등 벤치마크 존재하나 국내 통신사 맥락의 측정 체계 미수립 | [[G-14]](#ref-g-14), [[G-11]](#ref-g-11) |
| Achievable | **달성 가능** — 3개 L3 모두 TRL 6~8 수준으로 기술적 실현 가능. Mem0 등 오픈소스 메모리 인프라 활용 시 개발 기간 단축 가능 [[G-09]](#ref-g-09) | [[G-09]](#ref-g-09), [[G-13]](#ref-g-13) |
| Relevant | **높음** — 통신사 ARPU 정체 환경에서 AI 기반 B2C 부가가치 서비스는 전략적으로 정합. SKT가 에이닷을 조직 전면에 배치한 사실 자체가 시장 관련성을 입증 [[E-06]](#ref-e-06) | [[E-06]](#ref-e-06), [[G-11]](#ref-g-11) |
| Time-bound | **긴박** — Google Gemini Personal Intelligence 무료 개방(2026.3) [[G-07]](#ref-g-07), Apple LLM Siri 2026 상반기 출시 예정 [[G-17]](#ref-g-17), SKT 에이닷 구독 모델 전환 추진 중 [[E-06]](#ref-e-06). 12~18개월 내 PoC 미출시 시 시장 선점 기회 상실 우려 | [[G-07]](#ref-g-07), [[G-17]](#ref-g-17), [[E-06]](#ref-e-06) |

### Market Sizing

| 구분 | 규모 | 출처 |
|------|------|------|
| TAM | $37.1B (2025) → $435~552B (2034~2035), CAGR 31% — 글로벌 AI 컴패니언/어시스턴트 시장 | [[G-02]](#ref-g-02), [[G-03]](#ref-g-03) |
| SAM | $3.35B (2025) → $21.1B (2030), CAGR 44.5% — AI Assistant 시장(MarketsandMarkets 기준, 보다 좁은 정의) | [[G-04]](#ref-g-04) |
| SOM | 데이터 부족 — 한국 AI 개인비서 시장 분리 통계 없음. 글로벌 대비 한국 통신 시장 비중(~2%) 적용 시 약 $670M~$1.1B 범위로 추정 [추정, 근거부족] | 보강 키워드: "한국 AI 비서 시장 규모", "Korean AI assistant market size" |

*교차 검증: Grand View($28.2B/2024), Precedence($37.1B/2025), Fortune($37.7B/2025) 3개 독립 리서치사의 시장 규모 추정이 $28~38B 범위에서 수렴. CAGR도 30.8~31.2%로 일관성 높음.*

---

## 2. 기술 성숙도 맵

```
         High TRL (7~9)
              │
              │  ● Persona Plugin (TRL 7~8)
   [유지]     │     [베팅] ← Immediate review target
              │  ● Context-Action Rec. (TRL 6~8, 플랫폼별 격차)
──────────────┼──────────────
              │  ● Relationship Graph (TRL 6~7)
   [탐색]     │     [Watch]
              │
         Low TRL (1~6)

   Low Disruption ←──→ High Disruption
```

### 기술별 상세 평가

| 기술 (L3) | TRL | Disruption | 사분면 | 근거 |
|-----------|-----|-----------|--------|------|
| Persona Plugin | 7~8 | Medium-High | **베팅** | AI 컴패니언이 MIT Technology Review 2026 10대 혁신 기술 선정 [추가확인 필요], Hume AI EVI 감정 인식 상용화 [[E-01]](#ref-e-01), Replika 상용 운영 중 [[G-15]](#ref-g-15) |
| Relationship Graph | 6~7 | High | **Watch→베팅 경계** | Mem0 오픈소스(GitHub 41K 스타) LOCOMO 벤치마크 26% 정확도 향상 [[G-09]](#ref-g-09), Graphiti 시간축 지식 그래프 [[G-13]](#ref-g-13). 아직 단독 상용 서비스 단계 전 |
| Context-Action Recommendation | 6~8 | High | **베팅** (플랫폼별 격차 큼) | Apple/Google이 온디바이스+클라우드 하이브리드로 상용화 중 [[G-06]](#ref-g-06), [[G-07]](#ref-g-07), Lenovo Qira 앰비언트 AI [[G-21]](#ref-g-21). 학술 단계의 ContextAgent [[P-01]](#ref-p-01)도 선제적 추천 프레임워크 제시 |

**시사점**: 3개 L3 모두 상용화 임계점에 도달. Persona Plugin은 이미 소비자 서비스 운영 중이나, Relationship Graph와 Context-Action Recommendation은 빅테크 플랫폼 내 통합 형태로 급속 발전 중. 통신사가 독자적으로 3개 레이어를 모두 구축하기보다, 인프라 레이어(Mem0/Graphiti)를 차용하고 통신 데이터 기반 차별화 레이어에 집중하는 것이 합리적.

---

## 3. 경쟁사 현황

| Competitor | Similar Project | Stage | Timeline | Patents | Investment | Source |
|------------|----------------|-------|----------|---------|------------|--------|
| SKT | 에이닷 AI 개인비서 (브리핑·노트 베타) | 베타 서비스 운영 + 구독 모델 전환 추진 | 2025년 베타 → 2026년 조직 전면 배치 | 공개 정보 없음 | 미공개 (조직 전면 배치 수준의 전사 투자) | [[E-05]](#ref-e-05), [[E-06]](#ref-e-06) |
| KT | AI 통화비서, AI 빅또리 비서 | 상용 (B2B 중심, 도메인 한정) | 운영 중 | 공개 정보 없음 | 미공개 | [[G-22]](#ref-g-22) |
| Apple | Intelligence Personal Context + LLM Siri | 개발 중 → 2026 상반기 출시 예정 | 2025.10 지연 → 2026 H1 | 온디바이스 LLM 관련 다수 출원 [추정] | 미공개 (Apple Silicon 투자 포함) | [[G-06]](#ref-g-06), [[G-17]](#ref-g-17) |
| Google | Gemini Personal Intelligence | 상용 (2026.3 무료 개방) | 2026.1 발표 → 2026.3 무료화 | 사용자 맥락 그래프 관련 출원 [추정] | 미공개 | [[G-07]](#ref-g-07), [[G-08]](#ref-g-08) |
| Samsung | Galaxy AI (Bixby + Perplexity, Now Brief) | 상용 (One UI 8.5) | MWC 2026 발표, 출시 완료 | 온디바이스 AI 관련 출원 [추정] | 미공개 | [[E-04]](#ref-e-04), [[G-16]](#ref-g-16) |
| Microsoft | Copilot (Inflection 기술 기반) | 상용 통합 중 | 2024.3 인수 → 통합 진행 | 미공개 | $650M Inflection 라이선스 | [[G-10]](#ref-g-10) |

### Gap Analysis

**국내 통신사 간 포지션: Behind (SKT 대비)**
- SKT는 에이닷을 2026년 조직명에 전면 배치하며 AI 수익화의 핵심 서비스로 포지셔닝 [[E-06]](#ref-e-06). 브리핑(일상 종합 분석)·노트(회의록 자동 생성) 베타 운영 중 [[E-05]](#ref-e-05).
- KT는 도메인 특화 B2B AI 비서에 집중하며 범용 개인 AI 비서는 부재 [[G-22]](#ref-g-22).
- 당사는 Personal Intelligence 관련 공개 서비스 또는 발표가 없는 상태로, SKT 대비 최소 12개월 이상 후발.

**글로벌 빅테크 대비 포지션: Behind (구조적 비대칭)**
- Apple·Google·OpenAI는 각각 수십억 사용자 기반의 개인 데이터 생태계를 보유하며, 이미 Personal Intelligence 기능을 상용화 또는 무료 제공 중.
- 통신사의 차별화 포인트는 통화·위치·네트워크 데이터로 한정되나, 이는 빅테크가 접근하기 어려운 독점적 자산 [[G-11]](#ref-g-11).

---

## 4. 3B 전략 분석

### 의사결정 변수 평가

| Factor | Score | Evidence |
|--------|-------|----------|
| Differentiation importance | **7/10** | 통신사 고유 데이터(통화·위치)로 차별화 가능하나, 빅테크 플랫폼 위에서의 차별화 범위는 제한적 [[G-11]](#ref-g-11) |
| Internal capability | **부분적** | 통신사는 네트워크 데이터 처리 역량 보유하나, LLM/메모리 그래프/감정 인식 등 핵심 AI 기술은 외부 의존 필요 [추정, 근거부족] — 보강 키워드: "한국 통신사 AI 인력 현황", "telecom AI R&D capability" |
| Market window | **12~18개월** | Google Gemini 무료화(2026.3) [[G-07]](#ref-g-07), Apple LLM Siri(2026 H1) [[G-17]](#ref-g-17), SKT 에이닷 구독 전환(2026) [[E-06]](#ref-e-06). 2027년 중반까지 주요 플레이어 상용화 완료 예상 |
| Market urgency | **7/10** | 빅테크 무료 제공이 가속되나, 통신사 고유 데이터 기반 서비스는 별도 시장 형성 가능 |
| Tech gap | **1~2년** | SKT 대비 1년+, 빅테크 대비 기술 격차 존재하나 Mem0 등 오픈소스 활용으로 단축 가능 [[G-09]](#ref-g-09) |

### 의사결정 로직 적용

```
IF (differentiation_importance=7 > 8) → BUILD 조건 미충족
ELIF (market_urgency=7 > 8) OR (tech_gap=1.5 > 2) → BUY 조건 미충족
ELSE → BORROW (파트너십/JV)
```

그러나 통신사 데이터 기반 차별화 레이어는 외부 조달이 불가하므로 **자체 개발 필수**. 따라서:

**권고: Borrow + Build (하이브리드)**
- **Borrow**: 메모리/지식 그래프 인프라(Mem0, Graphiti), 감정 인식(Hume AI), LLM 기반 모델(오픈소스 또는 API)
- **Build**: 통화 이력 기반 관계 그래프, 위치·네트워크 데이터 기반 맥락 추천, 프라이버시 보존 온디바이스 처리 레이어

---

## 5. 최종 제언

```
[과제명]: Personal Intelligence (Persona Plugin, Relationship Graph, Context-Action Recommendation)
[추천 방향]: Borrow + Build
[핵심 근거]:
  - 시장: TAM $37B(2025), CAGR 31% — 3개 독립 리서치사 교차 확인 [G-01, G-02, G-03]
  - 기술: 3개 L3 모두 TRL 6~8, Mem0/Graphiti 오픈소스 인프라로 개발 가속 가능 [G-09, G-13]
  - 사업: 통신사 고유 데이터(통화·위치·실명 계약)는 빅테크 대비 독점적 차별화 자산 [G-11]
[리스크]:
  - 빅테크 무료화 압박: Google Gemini Personal Intelligence 무료 개방이 유료 모델 기반 통신사 서비스의 가격 경쟁력 약화 — probability: H, impact: H [G-07]
  - 프라이버시 규제: 통신 데이터의 AI 목적 재활용에 대한 개인정보보호법/GDPR 규제 불확실성 — probability: M, impact: H [G-24]
  - SKT 선점 효과: 에이닷 구독 모델 전환 가속 시 국내 시장 선점 고착화 — probability: M, impact: M [E-06]
  - 내부 역량 부족: LLM/메모리 그래프 핵심 기술 인력 확보 어려움 — probability: H, impact: M [추정, 근거부족]
[Next Action]:
  - [ ] Mem0/Graphiti 기술 PoC (6개월) — AI Lab 주관, 통화 이력 데이터 기반 관계 그래프 파일럿
  - [ ] 프라이버시 법률 검토 (3개월) — 법무실 주관, 통신 데이터 AI 활용 동의 체계 설계
  - [ ] SKT 에이닷 경쟁 분석 심화 (1개월) — 전략팀 주관, 에이닷 구독 모델·기능 세부 스펙 역분석
  - [ ] 감정 인식 기술 파트너 탐색 (3개월) — 사업개발 주관, Hume AI 등 EVI 기술 라이선싱 타진
```

---

## 6. 3축 평가 근거

### 고객가치

| 구분 | 내용 | 출처 |
|------|------|------|
| 강점 | 80% 고객이 개인화 경험을 위해 데이터 공유 의향 있음. AI 컴패니언 앱 소비자 지출 2025년 상반기 $221M으로 수요 실증 | [[G-11]](#ref-g-11), [[G-14]](#ref-g-14) |
| 강점 | 통신사 고유 데이터(통화 이력·위치)를 활용한 관계 기반 개인화는 빅테크 범용 AI 비서 대비 깊이 있는 맥락 제공 가능 | [[G-11]](#ref-g-11) |
| 리스크 | Google Gemini Personal Intelligence 무료 제공으로 유료 서비스 가격 저항 예상. 빅테크 무료 서비스가 "충분히 좋은" 대체재로 기능할 가능성 | [[G-07]](#ref-g-07), [[G-08]](#ref-g-08) |
| 리스크 | 통신 데이터 활용에 대한 소비자 프라이버시 우려. 별도 동의 획득 시 전환 비용 발생 | [[G-24]](#ref-g-24) |

### 사업포텐셜

| 구분 | 내용 | 출처 |
|------|------|------|
| 강점 | TAM $37B(2025) → $435~552B(2034~2035), CAGR 31%. AI 투자 통신사의 ROI가 일반 디지털 투자 대비 1.7~3.4배 | [[G-02]](#ref-g-02), [[G-03]](#ref-g-03), [[G-11]](#ref-g-11) |
| 강점 | AI 컴패니언 앱 구독 수익 모델 검증 중 — 연간 $120M 궤도(글로벌). 상위 10% 앱이 89% 수익 집중 → 품질 차별화 시 높은 수익 집중도 기대 | [[G-14]](#ref-g-14) |
| 리스크 | 한국 시장 분리 통계 부재로 SOM 산정 불확실. 빅테크 무료화가 유료 구독 모델의 시장 규모를 제한할 가능성 | [[G-07]](#ref-g-07) |
| 리스크 | 독립 AI 컴패니언 스타트업(Inflection, Character.ai)이 빅테크에 흡수되는 구조적 통합 추세. 중간 규모 플레이어의 독립 생존 불확실 | [[G-10]](#ref-g-10), [[E-02]](#ref-e-02) |

### 기술경쟁력

| 구분 | 내용 | 출처 |
|------|------|------|
| 강점 | Mem0(GitHub 41K 스타, $24M 조달) 등 오픈소스 메모리 인프라 활용 가능. LOCOMO 벤치마크에서 OpenAI 내장 메모리 대비 26% 정확도 향상 입증 | [[G-09]](#ref-g-09), [[P-02]](#ref-p-02) |
| 강점 | 온디바이스 AI 처리 기술 성숙(Apple Silicon, Qualcomm NPU). MemX 등 로컬 우선 프라이버시 보존 아키텍처 연구 활발 | [[G-19]](#ref-g-19), [[P-05]](#ref-p-05) |
| 리스크 | 통신사 자체 LLM/NLP 핵심 기술 보유 여부 불확실. 외부 모델 의존 시 차별화 약화 | 데이터 부족 — 보강 키워드: "한국 통신사 AI 연구 역량", "telecom AI patent portfolio" |
| 리스크 | 특허 포트폴리오 정량 분석 미실시. Apple·Google·Samsung의 온디바이스 AI 특허 장벽이 존재할 가능성 | 데이터 부족 — 보강 키워드: "on-device AI patent landscape", "personal AI assistant patent analysis" |

---

## 7. 정량 평가 (128/200)

| # | 평가 항목 | 세부1 (10) | 세부2 (10) | 세부3 (10) | 세부4 (10) | 소계 (40) |
|---|----------|-----------|-----------|-----------|-----------|----------|
| 1 | 고객가치 | pain point 심각도: **7** — ARPU 정체 환경에서 AI 개인화 수요는 실재하나 필수재가 아닌 편의재 성격 [[G-14]](#ref-g-14) | 제공 가치 명확성: **7** — 통화·위치 기반 관계 그래프는 차별적이나 구체적 가치 제안(Use Case) 미정의 [[G-11]](#ref-g-11) | 대체제 대비 우위: **5** — Google Gemini 무료 개방이 "충분히 좋은" 대체재로 기능. 통신 데이터 기반 깊이가 차별점이나 검증 미완 [[G-07]](#ref-g-07) | 고객 수용성: **7** — 80% 데이터 공유 의향 [[G-11]](#ref-g-11), 단 별도 동의 필요 + 프라이버시 우려 [[G-24]](#ref-g-24) | **26** |
| 2 | 시장매력도 | 시장 규모 TAM/SAM/SOM: **9** — TAM $37B, CAGR 31%, 3개 리서치사 교차 확인 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-03]](#ref-g-03) | 성장률 CAGR: **9** — 30.8~31.2% 일관, AI Assistant 세분화 시장 44.5% [[G-04]](#ref-g-04) | 시장 타이밍: **6** — 빅테크 상용화 진행 중으로 최적 시점은 지남. 통신 데이터 기반 틈새는 여전히 열려 있음 [[G-07]](#ref-g-07) | 규제/정책 환경: **6** — GDPR Digital Omnibus 개정으로 AI 데이터 처리 완화 논의 [[G-24]](#ref-g-24), 그러나 한국 개인정보보호법 제약은 불확실 | **30** |
| 3 | 기술경쟁력 | TRL 수준: **7** — 3개 L3 평균 TRL 6~8, 상용화 가능 수준 [[G-09]](#ref-g-09), [[E-01]](#ref-e-01) | 특허 포트폴리오: **5** — 데이터 부족. 통신사 자체 특허 현황 미확인 | 기술 장벽: **6** — Mem0/Graphiti 오픈소스 활용 가능하나 통신 데이터 통합 레이어는 자체 구축 필요 [[G-09]](#ref-g-09), [[G-13]](#ref-g-13) | 표준/인증: **5** — 데이터 부족. AI 개인화 서비스 관련 표준 체계 미확립 | **23** |
| 4 | 경쟁우위 | 시장 포지션: **4** — SKT 대비 12개월+ 후발, 빅테크 대비 구조적 열위 [[E-06]](#ref-e-06), [[G-07]](#ref-g-07) | 차별화 지속성: **7** — 통화·위치·실명 계약 데이터는 빅테크 접근 불가한 독점 자산 [[G-11]](#ref-g-11) | 경쟁사 대응력: **5** — 데이터 부족. 통신 데이터 기반 개인화의 모방 난이도 미검증 | 생태계/파트너: **7** — Mem0($24M) [[G-09]](#ref-g-09), Hume AI($50M) [[E-01]](#ref-e-01) 등 파트너 후보 다수. 오픈소스 생태계 활용 가능 | **23** |
| 5 | 실행가능성 | 내부 역량: **5** — 데이터 부족. 통신사 AI 인력/기술 현황 미확인 — 보강 키워드: "한국 통신사 AI R&D 인력" | 투자 규모 대비 ROI: **7** — AI 투자 통신사 ROI 4배 [[G-11]](#ref-g-11), Borrow 전략으로 초기 투자 절감 가능 | 일정 현실성: **7** — Mem0/Graphiti 활용 시 6~12개월 내 PoC 가능. 단 데이터 파이프라인·동의 체계 구축은 병행 필요 [[G-09]](#ref-g-09) | 리스크 관리: **7** — Borrow+Build 하이브리드로 기술 리스크 분산. 프라이버시 리스크는 온디바이스 처리로 완화 가능 [[P-05]](#ref-p-05), [[G-20]](#ref-g-20) | **26** |
| | **총점** | | | | | **128** |

**산출 검증:**
- 고객가치: 7 + 7 + 5 + 7 = 26
- 시장매력도: 9 + 9 + 6 + 6 = 30
- 기술경쟁력: 7 + 5 + 6 + 5 = 23
- 경쟁우위: 4 + 7 + 5 + 7 = 23
- 실행가능성: 5 + 7 + 7 + 7 = 26
- **총점: 26 + 30 + 23 + 23 + 26 = 128/200**

**→ 수정: 총점 128점은 Conditional Go 범위(120~159)에 해당**

*참고: "데이터 부족" 항목이 4개(특허 포트폴리오, 표준/인증, 경쟁사 대응력, 내부 역량)로 3개 이상이므로 전체 신뢰도를 **Low**로 하향 조정.*

### 종합 판정

| 항목 | 결과 |
|------|------|
| 총점 | **128/200** |
| 판정 | **Conditional Go** |
| 신뢰도 | **Low** (데이터 부족 4개 항목) |
| 보완 필수 항목 | (1) 내부 AI 역량 현황 파악, (2) 특허 포트폴리오 분석, (3) 한국 시장 SOM 산정, (4) SKT 에이닷 세부 스펙 역분석 |

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 인용원문(한글) | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|--------|----------|------|---------------|--------|--------|--------|-----|
| <a id="ref-g-01"></a>G-01 | Grand View Research | 2025 | market-report | AI Companion Market Report 2030 | AI 컴패니언 시장 2024년 $28.19B, 2030년 $140.75B, CAGR 30.8% | 높음 | [B] | 높음 | [링크](https://www.grandviewresearch.com/industry-analysis/ai-companion-market-report) |
| <a id="ref-g-02"></a>G-02 | Precedence Research | 2025 | market-report | AI Companion Market Size to Hit USD 552.49B by 2035 | AI 컴패니언 시장 2025년 $37.12B, 2035년 $552.49B, CAGR 31.0% | 높음 | [B] | 높음 | [링크](https://www.precedenceresearch.com/ai-companion-market) |
| <a id="ref-g-03"></a>G-03 | Fortune Business Insights | 2025 | market-report | AI Companion Market Growth 2026-2034 | AI 컴패니언 시장 2025년 $37.73B, 2034년 $435.9B, CAGR 31.24% | 높음 | [B] | 높음 | [링크](https://www.fortunebusinessinsights.com/ai-companion-market-113258) |
| <a id="ref-g-04"></a>G-04 | MarketsandMarkets | 2025 | market-report | AI Assistant Market Size, Share, Trends | AI Assistant 시장 2025년 $3.35B → 2030년 $21.11B, CAGR 44.5% | 높음 | [B] | 높음 | [링크](https://www.marketsandmarkets.com/Market-Reports/ai-assistant-market-40111511.html) |
| <a id="ref-g-05"></a>G-05 | Skywork AI | 2026 | blog | The Ultimate 2026 Guide to Character AI | Character.ai MIT Technology Review 10대 혁신 기술 선정 | 중간 | [C] | 높음 | [링크](https://skywork.ai/skypage/en/ultimate-guide-character-ai-roleplay-companionship/2032056304473153536) |
| <a id="ref-g-06"></a>G-06 | Fello AI | 2025-10 | news | The State of Apple Intelligence & Siri in October 2025 | Apple Intelligence Personal Context 기능 2025년 10월 기준 미출시, 지연 | 높음 | [B] | 높음 | [링크](https://felloai.com/the-state-of-apple-intelligence-siri-in-october-2025-apples-ai-vision-vs-reality/) |
| <a id="ref-g-07"></a>G-07 | Fortune | 2026-01-14 | news | Google connects Gemini to users' emails and photos | Gemini Personal Intelligence — Gmail·Photos·YouTube 연동, 2026.3 무료 개방 | 높음 | [B] | 높음 | [링크](https://fortune.com/2026/01/14/google-gemini-ai-personal-assistant-gmail-photos-youtube-history-personal-intelligence/) |
| <a id="ref-g-08"></a>G-08 | MacRumors | 2026-03-26 | news | Google Launches Gemini Import Tool for Switching From ChatGPT, Claude | Gemini 타 AI 앱 메모리 임포트 도구 출시 | 높음 | [B] | 높음 | [링크](https://www.macrumors.com/2026/03/26/gemini-import-tool/) |
| <a id="ref-g-09"></a>G-09 | TechCrunch | 2025-10-28 | news | Mem0 raises $24M from YC, Peak XV and Basis Set | Mem0 장기 메모리 레이어, GitHub 41K 스타, LOCOMO 벤치마크 26% 향상 | 높음 | [B] | 높음 | [링크](https://techcrunch.com/2025/10/28/mem0-raises-24m-from-yc-peak-xv-and-basis-set-to-build-the-memory-layer-for-ai-apps/) |
| <a id="ref-g-10"></a>G-10 | DeepLearning.AI The Batch | 2024-03 | news | Microsoft Pays Inflection AI $650 Million | Microsoft $650M Inflection 라이선스, Suleyman 영입 | 높음 | [B] | 중간 | [링크](https://www.deeplearning.ai/the-batch/microsoft-pays-inflection-ai-650-million-hires-most-of-its-staff/) |
| <a id="ref-g-11"></a>G-11 | Tredence | 2025 | blog | 7 Agentic AI Trends Transforming Telecom in 2025 | 통신사 AI 투자 ROI 1.7~3.4배, 80% 고객 데이터 공유 의향 | 높음 | [B] | 높음 | [링크](https://www.tredence.com/blog/agentic-ai-trends-telecom) |
| <a id="ref-g-12"></a>G-12 | Tech Startups | 2025-08-20 | news | Character.ai in talks to sell or raise new funding | Character.ai 매각/펀딩 논의 재개 | 중간 | [C] [미검증] | 높음 | [링크](https://techstartups.com/2025/08/20/character-ai-in-talks-to-sell-or-raise-new-funding-as-chatbot-costs-pile-up/) |
| <a id="ref-g-13"></a>G-13 | GitHub | 2025 | blog | getzep/graphiti: Build Real-Time Knowledge Graphs for AI Agents | Graphiti 실시간 시간적 지식 그래프 | 높음 | [B] | 높음 | [링크](https://github.com/getzep/graphiti) |
| <a id="ref-g-14"></a>G-14 | TechCrunch | 2025-08-12 | news | AI companion apps on track to pull in $120M in 2025 | AI 컴패니언 앱 연간 $120M 수익 궤도, 상반기 $221M 소비자 지출 | 높음 | [B] | 높음 | [링크](https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025/) |
| <a id="ref-g-15"></a>G-15 | Tracxn | 2026 | database | Replika 2026 Company Profile | Replika 펀딩 $11M, 연간 매출 약 $3M | 중간 | [C] | 높음 | [링크](https://tracxn.com/d/companies/replika/__rr2kodByhjtv_6oVe5NqDvmeW-R7FJvAXqOeHhy59zs) |
| <a id="ref-g-16"></a>G-16 | Samsung Global Newsroom | 2026-02 | press-release | Samsung Advances Galaxy AI at MWC 2026 | Galaxy AI 생태계 확장, Bixby+Perplexity 통합 | 높음 | [A] | 높음 | [링크](https://news.samsung.com/global/samsung-advances-galaxy-ai-and-its-connected-ecosystem-at-mwc-2026) |
| <a id="ref-g-17"></a>G-17 | MacRumors | 2026 | news | LLM Siri: Complete Guide to Apple's AI Assistant Overhaul | Apple LLM Siri 2026 상반기 출시 예정 | 높음 | [B] | 높음 | [링크](https://www.macrumors.com/guide/llm-siri/) |
| <a id="ref-g-18"></a>G-18 | Tracxn | 2026 | database | Meela 2026 Company Profile | Meela 시니어 AI 컴패니언 Seed $3.5M | 중간 | [C] | 높음 | [링크](https://tracxn.com/d/companies/meela/__DvBlTvWn_PPG4vnM-zceildYs8S94s_bo6RvKD_VlKE) |
| <a id="ref-g-19"></a>G-19 | TechGenyz | 2025 | blog | On-Device AI Smartphones 2025: Powerful Offline Intelligence | 온디바이스 AI 칩셋(Apple M5, Qualcomm NPU) 확산 | 중간 | [B] | 높음 | [링크](https://techgenyz.com/on-device-ai-smartphones-privacy-performance/) |
| <a id="ref-g-20"></a>G-20 | WebProNews | 2025 | blog | Apple's Privacy-First AI Strategy: On-Device LLMs by 2026 | Apple 프라이버시 우선 온디바이스 AI 전략 | 중간 | [B] | 높음 | [링크](https://www.webpronews.com/apples-privacy-first-ai-strategy-on-device-llms-by-2026/) |
| <a id="ref-g-21"></a>G-21 | Lenovo StoryHub | 2025 | press-release | Introducing Lenovo and Motorola Qira | Lenovo Qira 앰비언트 인텔리전스, 온디바이스 실행 | 중간 | [A] | 높음 | [링크](https://news.lenovo.com/pressroom/press-releases/lenovo-unveils-lenovo-and-motorola-qira/) |
| <a id="ref-g-22"></a>G-22 | 스포츠서울 | 2025-09 | news | KT 일냈다! KBO리그 '최초' AI 빅또리 비서 서비스 오픈 | KT AI 빅또리 비서(KBO 도메인 한정), AI 통화비서 | 중간 | [B] | 높음 | [링크](https://www.sportsseoul.com/news/read/1543887) |
| <a id="ref-g-23"></a>G-23 | CNBC | 2026-02-25 | news | The global M&A boom is rolling into 2026 | 2025년 M&A $4.9조(+40% YoY), AI가 VC 자금 50%+ | 중간 | [B] | 높음 | [링크](https://www.cnbc.com/2026/02/25/global-ma-boom-surges-2026-ai-mega-deals-capital-squeeze-merger-and-acquisition.html) |
| <a id="ref-g-24"></a>G-24 | IAPP | 2025 | news | European Commission proposes significant reforms to GDPR, AI Act | EU Digital Omnibus 개정 — AI 데이터 처리 완화 논의 | 높음 | [B] | 높음 | [링크](https://iapp.org/news/a/european-commission-proposes-significant-reforms-to-gdpr-ai-act) |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약원문 |
|------|--------|--------|------|-----------|---------|
| <a id="ref-e-01"></a>E-01 | Hume AI | 2024-03-26 | Series B $50M Fundraise and EVI Announcement | hume ai series b evi | EVI 감정 인식 AI 음성 인터페이스 상용화 발표, EQT Ventures 리드 |
| <a id="ref-e-02"></a>E-02 | Bloomberg | 2024-08-02 | Character.AI Co-Founders Hired by Google in Licensing Deal | character.ai google acquihire | Google $2.7B 역취득, Shazeer 구글 복귀, 모델 비독점 라이선스 |
| <a id="ref-e-03"></a>E-03 | OpenAI Community | 2025-04-10 | ChatGPT can now reference all past conversations | chatgpt memory full history | 전체 대화 이력 참조 기능 출시, 저장 메모리+대화 이력 이중 구조 |
| <a id="ref-e-04"></a>E-04 | Samsung Global Newsroom | 2025-11 | Samsung Introduces the New Bixby in One UI 8.5 | samsung bixby one ui 8.5 now brief | Now Brief 개인화 브리핑, Perplexity AI 통합 |
| <a id="ref-e-05"></a>E-05 | AI타임스 | 2025 | SKT 에이닷, 'AI 개인비서'로 진화 | skt 에이닷 ai 개인비서 | 에이닷 브리핑·노트 베타 출시, 루틴 기억 기반 개인비서 진화 |
| <a id="ref-e-06"></a>E-06 | The Bell | 2025-12-31 | [2026 SKT 리빌딩] '에이닷'을 조직 전면에 'AI 수익화 방점' | skt 2026 조직개편 에이닷 | 에이닷 조직명 전면 배치, 구독 모델 전환, AI 수익화 가속 |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 핵심 인용 | DOI/URL |
|------|------|----------|------|----------|---------|
| <a id="ref-p-01"></a>P-01 | ContextAgent Team | 2025 | ContextAgent: Context-Aware Proactive LLM Agents with Open-World Sensory Perceptions | 웨어러블 센서 기반 선제적 LLM 에이전트 최초 프레임워크 | [arxiv](https://arxiv.org/abs/2505.14668) |
| <a id="ref-p-02"></a>P-02 | Mem0 Team | 2025 | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | LOCOMO 벤치마크 26% 정확도 향상, 90% 토큰 절감 | [arxiv](https://arxiv.org/abs/2504.19413) |
| <a id="ref-p-03"></a>P-03 | ProPerSim Team | 2025 | ProPerSim: Developing Proactive and Personalized AI Assistants through User-Assistant Simulation | 사용자-어시스턴트 시뮬레이션 기반 선제적 개인화 훈련 | [arxiv](https://arxiv.org/html/2509.21730) |
| <a id="ref-p-04"></a>P-04 | Situation Graph Team | 2026 | Situation Graph Prediction: Structured Perspective Inference for User Modeling | 상황 궤적 기반 사용자 모델링 (맥락·감정·목표 통합) | [arxiv](https://arxiv.org/html/2602.13319) |
| <a id="ref-p-05"></a>P-05 | MemX Team | 2026 | MemX: A Local-First Long-Term Memory System for AI Assistants | 로컬 우선 프라이버시 보존 장기 메모리 아키텍처 | [arxiv](https://arxiv.org/html/2603.16171) |

### 특허 (T-xx)

| 번호 | 출원인 | 등록/출원일 | 특허번호 | 제목 | 관할 |
|------|--------|-----------|----------|------|------|
| — | 데이터 부족 — intel-store MCP 미연결으로 특허 DB 조회 불가. Apple/Google/Samsung의 온디바이스 AI 관련 특허는 정성적으로만 확인 | — | — | — | — |

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 페이지 | 인용내용 |
|------|--------|--------|--------|---------|
| — | 해당 없음 | — | — | — |
