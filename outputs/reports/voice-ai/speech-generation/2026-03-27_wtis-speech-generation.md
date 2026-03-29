---
topic: Speech Generation (Voice Synthesis + Voice Cloning)
domain: voice-ai
l2_topic: speech-generation
date: 2026-03-27
wtis_version: v4.1
wtis_mode: standard
skills_executed: [research-deep, SKILL-1, validator]
status: completed
total_references: 30
prior_report: 2026-03-24_wtis-speech-generation.md
prior_report_date: 2026-03-24
score: 138/200
verdict: Conditional Go
strategy: Borrow + Build
tags: [claude-code, wtis, voice-cloning, deepfake]
created: 2026-03-27
updated: 2026-03-27
---

# WTIS Report: Speech Generation (Voice Synthesis + Voice Cloning)

## Executive Summary

**시장**: Text-to-Speech (TTS) 시장 TAM $3.65~4.25B(2025), CAGR 12~14% [이전 분석 4개 출처 수렴]. 딥페이크 탐지 시장 $72억(2031, MarketsandMarkets) [[G-10]](#ref-g-10). Voice AI 인프라 대규모 자본 집중 — ElevenLabs $500M/$11B [[G-07]](#ref-g-07)

**기술**: Voice Cloning TRL 9 상향 — SUNY Buffalo Lyu 교수 "구별 불가능 임계점(Indistinguishable Threshold)" 공식 선언 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02). 실시간 딥페이크 탐지 TRL 8 확정(Pindrop 99.2%, KT 91.6%, SKT 96%). 탐지-생성 비대칭(Detection Gap)이 구조적 문제로 고착화 [[P-01]](#ref-p-01), [[P-02]](#ref-p-02)

**기회**: UNODC-INTERPOL 서밋(47개국+기관 서약)이 딥페이크를 글로벌 범죄 핵심 수단으로 경고 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05). Hiya "통신사가 사기꾼에 2:1로 지고 있다" 소비자 여론 [[E-01]](#ref-e-01) → 통신사 "망 레벨 음성 신뢰 인프라" 기회 구체화

**위협**: ElevenLabs-IBM watsonx 파트너십으로 Enterprise Voice AI 스택 표준화 가속 [[E-02]](#ref-e-02). KT/SKT 6~12개월 선점. 탐지 정확도 천장(적대적 공격 시 성능 급락) [[P-01]](#ref-p-01)

**권고**: Borrow + Build 유지, **딥페이크 탐지를 Build 핵심 축으로 격상**. TTS/Voice Cloning 엔진은 파트너십(Borrow) — Pindrop 딥페이크 탐지 파트너십 긴급 추진. 망 내장형 3축(Identity+Authenticity+Intelligence) 통합은 자체 구축(Build)

---

## 이전 분석 대비 변화

> 이전 분석: `2026-03-24_wtis-speech-generation.md` (131/200, Conditional Go)

| 항목 | 이전 (2026-03-24) | 현재 (2026-03-27) | 변화 |
|------|------------------|------------------|------|
| 핵심 판정 | Conditional Go | Conditional Go | → (강도 강화) |
| 점수 | 131/200 | 138/200 | ↑ +7 |
| 신뢰도 | Medium-High | Medium-High | → |
| 주요 위험 | 파트너 종속 심화, 딥페이크 사기 급증 | 딥페이크 임계점 공식화, 탐지-생성 비대칭 구조화 | ↑↑ 위협 현실화 |
| Voice Cloning TRL | 8 | 9 (↑) | 임계점 공식 선언 |
| 실시간 딥페이크 탐지 TRL | 7~8 | 8 (↑) | Pindrop 99.2%, KT/SKT 실적 |
| 통신사 포지션 | "고유 포지션 가능성" | "망 레벨 표준 정의자" (KT/SKT 실증) | ↑↑ |
| 기업간 파트너십 | ElevenLabs de facto | ElevenLabs + IBM = Enterprise 스택 표준화 | ↑ |

**변화 주요 원인:**
- Voice Cloning TRL 8→9: SUNY Buffalo Lyu 교수 "Indistinguishable Threshold" 공식 선언, 수초(a few seconds) 음성으로 설득력 있는 클론 생성 현실화 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)
- KT 1,300억원 피해예방(2025년 연간, 전자신문) · SKT 96% 탐지 정확도 실적 공개로 통신사 망 레벨 탐지의 상용 실증 완료 [[E-03]](#ref-e-03), [[E-04]](#ref-e-04)
- ElevenLabs-IBM watsonx 파트너십(2026-03-25)으로 Enterprise Voice AI 인프라 레이어 표준화 가속 [[E-02]](#ref-e-02)
- UNODC-INTERPOL 글로벌 사기 서밋(47개국+기관 서약)에서 딥페이크·보이스클로닝을 글로벌 범죄 핵심 수단으로 공식 경고, 글로벌 사기 피해 $4,420억 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)
- Hiya: 미국인 31% 딥페이크 음성 통화 경험, "통신사가 사기꾼에 2:1로 지고 있다" — 통신사 법적 책임 여론 부상 [[E-01]](#ref-e-01)

---

## 1. 시장 분석

### Market Sizing

| 구분 | 수치 | 출처 | 이전 대비 |
|------|------|------|----------|
| **TAM** (글로벌 TTS, 2025) | $3.65~4.25B | 이전 분석 4개 출처 수렴 [I-01] | → 유지 |
| **TAM** (글로벌 TTS, 2030) | $7.3~9.3B | CAGR 12~14% 보수적 추정 | → 유지 |
| **딥페이크 탐지 시장** (2031) | $72억 | MarketsandMarkets [[G-10]](#ref-g-10) | **신규** |
| **글로벌 사기 피해 규모** | $4,420억 | GASA(Global Anti-Scam Alliance), UN 인용 [[G-04]](#ref-g-04) | **신규** |
| **Voice AI Agent 인프라** | CAGR 34.8% | LiveKit $1B, Deepgram $1.3B 유니콘 | → 유지 |
| **SAM** (통신사 AICC 음성) | ~$500M~1B [추정] | [미검증] | → 유지 |
| **SOM** | 미정 | [미검증] | → 유지 |

> **Validator 교정 V-05**: TAM 수치는 이전 분석(2026-03-24)에서 4개 독립 출처로 교차 검증된 값. 현 보고서 내 직접 출처가 아닌 이전 분석[I-01] 인용으로 명시.

### 주요 시장 이벤트 (3/24 이후)

**ElevenLabs–IBM watsonx Orchestrate 파트너십 (2026-03-25)**
ElevenLabs가 IBM watsonx Orchestrate에 TTS/STT 통합 발표 [[E-02]](#ref-e-02). 70개 언어, PCI 컴플라이언스, Zero Retention Mode(HIPAA), 데이터 레지던시 옵션 — API 공급자에서 Enterprise AI 인프라 레이어로 포지션 전환.

**Hiya "State of the Call 2026" (2026-03-01)**
12개국 12,000명 소비자 설문 [[E-01]](#ref-e-01):
- 미국인 31% 딥페이크 음성 통화 수신 경험
- 소비자 2:1 비율로 "통신사가 사기꾼에 지고 있다" 평가
- 통신사 법적 책임 부과 요구 여론 증가

**UNODC-INTERPOL 글로벌 사기 서밋 (2026-03-16~17, 빈)**
47개국+기관 서약(INTERPOL 공식 [[G-05]](#ref-g-05), UN News는 "약 60개국" 표기 [[G-04]](#ref-g-04)). AI 기반 사기 전통 방식 대비 4.5배 수익성 우위(INTERPOL 추정). 글로벌 사기 피해 $4,420억(GASA).

> **Validator 교정 V-03**: 참가국 수는 INTERPOL 공식 "47 countries and organizations", UN News "nearly 60 countries"로 출처별 상이. 본 보고서에서는 INTERPOL 공식 수치를 기준으로 표기.

---

## 2. 기술 성숙도 분석

### TRL 매트릭스 (2026-03-27)

| 기술 | TRL | 이전(3/24) | 변동 | 근거 |
|------|-----|-----------|------|------|
| **Voice Synthesis (Neural TTS)** | 8~9 | 8~9 | → | ElevenLabs-IBM 통합으로 Enterprise 스택 표준화 [[E-02]](#ref-e-02) |
| **Voice Cloning (Zero-shot)** | **9 (↑)** | 8 | **+1** | "Indistinguishable Threshold" 공식 선언 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02). 수초 음성으로 클론 생성 가능 |
| **Real-time Voice Agent** | 8~9 | 8 | ↑ | ElevenAgents GA + IBM watsonx 통합 [[E-02]](#ref-e-02) |
| **실시간 딥페이크 탐지** | **8 (↑)** | 7~8 | **↑** | Pindrop 99.2%(2초) [[G-21]](#ref-g-21), KT 91.6% [[E-03]](#ref-e-03), SKT 96% [[E-04]](#ref-e-04) |
| **망 레벨 음성 신뢰 인프라** | 6~7 | 6~7 | → | KT·SKT 실적 공개, MWC 2026 주요 의제 |
| **C2PA 오디오 워터마킹** | 5~6 | 5~6 | → | 표준 초안 단계, EU AI Act Article 50 채택 압력 [[G-15]](#ref-g-15) |

> **Validator 교정 V-01**: Pindrop 99.2% 수치의 원출처는 2026-02-26 GlobeNewswire 헬스케어 발표[G-21]이며, Fraud Assist 발표(E-05)와 구분하여 별도 등재.
> **Validator 교정 V-02**: "10초 음성"은 G-01/G-02 원문("a few seconds")과 불일치. "수초(a few seconds)"로 교정.

### SMART Test

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| **Specific** | **충족** | Pindrop 99.2%(2초) [[G-21]](#ref-g-21), KT 91.6% [[E-03]](#ref-e-03), SKT 96% [[E-04]](#ref-e-04)가 벤치마크 제공 |
| **Measurable** | **충족** | 탐지율·피해예방 금액(KT 1,300억원)으로 정량 측정 가능 [[E-03]](#ref-e-03) |
| **Achievable** | **조건부 충족** | KT/SKT 이미 상용화 — 동일 수준 PoC 12개월 내 현실적 |
| **Relevant** | **강하게 충족** | 딥페이크 임계점 + 소비자 법적 책임 여론 [[E-01]](#ref-e-01) + INTERPOL 경고 [[G-04]](#ref-g-04) |
| **Time-bound** | **충족** | EU AI Act Article 50 D-128(2026-08-02) [[G-15]](#ref-g-15), 한국 AI 기본법 계도기간 운영 중 [[G-17]](#ref-g-17) |

### 기술별 액션 맵

| 기술 | TRL | 근거 |
|------|:---:|------|
| 🔴 **실시간 딥페이크 탐지** ★ | 8 (↑) | Pindrop 99.2% [[G-21]](#ref-g-21), KT 91.6% [[E-03]](#ref-e-03), SKT 96% [[E-04]](#ref-e-04). 임계점 도달로 수요 구조적 보장 |
| 🔴 **망 내장형 Voice AI** | 6~7 | KT/SKT 실증 완료. 3축(Identity+Authenticity+Intelligence) 통합 설계 착수 시점 |
| 🟡 **Voice Cloning** (Zero-shot) | 9 (↑) | "임계점" 공식 선언 [[G-01]](#ref-g-01). 생성 엔진은 Borrow — ElevenLabs-IBM 스택 [[E-02]](#ref-e-02) |
| 🟡 **Real-time Voice Agent** | 8~9 (↑) | ElevenAgents GA + IBM watsonx 통합. Enterprise 배포 경로 단순화 |
| ⚪ Neural TTS | 8~9 | 성숙 단계, 추가 투자 불필요. 파트너 엔진 활용 |
| 🔵 Emotional TTS | 7 | Speech Perception L2에서 별도 평가 |
| 🔵 On-device TTS | 6~7 | Qwen3-TTS 오픈소스 모니터링 |
| 🔵 Voice+MCP 에이전트 | 5~6 | TRL 미성숙, 시기 미도래 |
| 🔵 C2PA 오디오 워터마킹 | 5~6 | 표준 초안 단계. EU AI Act Article 50 채택 압력 [[G-15]](#ref-g-15) |

> 🔴 즉시 추진 · 🟡 파트너십 확보 · ⚪ 유지 · 🔵 Watch / 볼드 = 이전 대비 TRL 변동 있음

### 딥페이크 임계점의 구조적 의미

Voice Cloning TRL 9 도달로 **탐지 기술과의 비대칭(Detection Gap)이 영구적 군비경쟁으로 구조화** [[P-01]](#ref-p-01), [[P-02]](#ref-p-02):

- **긍정적**: 통신사 "망 레벨 신뢰 인프라"의 시장 존재 이유를 영구적으로 보장. 사기 피해 $4,420억 [[G-04]](#ref-g-04)이 탐지 서비스 지속적 수요 기반
- **부정적**: 탐지 정확도 천장 존재(적대적 공격 하 성능 급락). 완벽한 탐지 불가 → **다층 방어(탐지+인증+워터마킹) 필수**
- **전략적**: 단일 탐지 기술이 아닌, 망 레벨 Identity+Authenticity+Intelligence 3축 통합이 경쟁 해자(moat)

---

## 3. 경쟁 환경

### 경쟁사 비교표 (2026-03-27)

| 경쟁사 | 유사 프로젝트 | 단계 | 이번 주 변화 | 출처 |
|--------|-------------|------|------------|------|
| **ElevenLabs** | v3 GA + Conv. AI 2.0 + IBM watsonx 통합 | 프로덕션 (Enterprise 전환) | IBM watsonx 통합(3/25) — 70개 언어, PCI/HIPAA. ARR $330M, $11B | [[E-02]](#ref-e-02), [[G-07]](#ref-g-07) |
| **Pindrop** | Pulse/Passport/Protect + Fraud Assist | 프로덕션 | Fraud Assist 에이전틱 솔루션(3/17). 조사시간 35~40% 감소 [[E-05]](#ref-e-05). 99.2%(2초) [[G-21]](#ref-g-21) | [[E-05]](#ref-e-05), [[G-08]](#ref-g-08) |
| **Hiya** | 브랜드 콜링 + 소비자 리포트 | 프로덕션 | "State of the Call 2026" — MWC 2026 핵심 발언자. Vodafone UK 99% 커버리지 | [[E-01]](#ref-e-01), [[G-06]](#ref-g-06) |
| **KT** | AI 보이스피싱 탐지 2.0 | 프로덕션 | **1,300억원 피해예방(2025년 연간)**, 91.6% 정확도. 목표: 2,000억/95%+ | [[E-03]](#ref-e-03) |
| **SKT** | 에이닷 전화 위험 목소리 탐지 | 프로덕션 | **성문 데이터 분석 추가(3/18)**, 96% 정확도 | [[E-04]](#ref-e-04), [[G-14]](#ref-g-14) |
| **Reality Defender + ValidSoft** | 딥페이크 탐지 + 음성 생체인증 | 프로덕션 | 전략적 파트너십 — 암호학적 음성 신뢰 플랫폼 | [[G-11]](#ref-g-11) |
| **McAfee** | 온디바이스 Deepfake Detector | 프로덕션 | 스펙트럴/시간적/성문 분석, 클라우드 미사용 | [[G-12]](#ref-g-12) |

> **Validator 교정 V-06**: SKT "11억 건 차단" 수치는 G-14(전자신문) 및 E-04(SKT 뉴스룸)에서 확인 불가. 본 보고서에서 제외.
> **Validator 교정 V-07**: KT 피해예방 수치: E-03(전자신문, 2025-12-23) 기준 1,300억원은 2025년 연간 실적. G-13(KT kode 블로그)의 710억원은 시험 기간 집계로 추정되며 시점 차이 존재.

### 제품/서비스 스펙 비교 (딥페이크 탐지)

| 기업 | 탐지 정확도 | 지연/처리 | 가격(정책) | 출처 |
|------|------------|----------|-----------|------|
| Pindrop | 99.2% (2초) | 실시간(콜센터) | 엔터프라이즈 구독 | [[G-21]](#ref-g-21) |
| KT | 91.6% (2025 H1) | 실시간 통화 중 | 통신 번들(후후) | [[E-03]](#ref-e-03) |
| SKT | ~96% (자체 평가) | 온디바이스 실시간 | 에이닷 앱 번들 | [[E-04]](#ref-e-04) |
| McAfee | 공개 정보 없음 | 온디바이스(오프라인) | ~$9.99~19.99/월 [추정] | [[G-12]](#ref-g-12) |
| Reality Defender+ValidSoft | 공개 정보 없음 | API/SDK, 실시간 | 엔터프라이즈 | [[G-11]](#ref-g-11) |

### Gap Analysis

| 역량 | 자사 격차 | 이번 주 변화 |
|------|----------|------------|
| 기반 모델 품질 | 2~3년 지연 | ElevenLabs-IBM으로 Enterprise 스택 표준화 — Borrow로 우회 |
| 딥페이크 탐지 | **격차 확대** | KT/SKT 선점, Pindrop 99.2%. 후발 차별화 필수 |
| 망 레벨 신뢰 인프라 | 격차 소폭 확대 | KT/SKT 6~12개월 선점. 동일 전략이나 선례 실증 |
| 저지연 Voice Agent | 유지 | IBM watsonx 통합으로 Enterprise 배포 단순화 — Borrow 해소 가능 |
| 규제 대응 | 우위 가능 | EU D-128, 한국 계도기간 — 통신사 라이선스 기반 우위 |

### 기업 발언 직접 인용

> **E-01 Hiya**: "Trust is shifting into the network—operators are looking to bake identity and protection into telecom infrastructure for broader coverage and less consumer friction." [[E-01]](#ref-e-01)

> **E-02 ElevenLabs Co-founder Mati Staniszewski**: "AI agents are becoming central to everyday work, and voice is where AI either earns trust or loses it." [[E-02]](#ref-e-02)

> **E-06 IBM VP Nick Holda**: "We're bringing a voice to AI Agents in the enterprise...enabling enterprises to deploy AI agents that sound natural, scale globally, and address security, reliability and governance." [[E-06]](#ref-e-06)

> **E-05 Pindrop CEO Dr. Vijay Balasubramaniyan**: "Human judgment, knowledge-based questions, and one-time passcodes are vulnerable security layers" in healthcare environments operating under HIPAA. [[E-05]](#ref-e-05)

---

## 4. 전략 권고

### 3B 의사결정 로직

```
차별화 중요도(6) < 8 → BUILD 단독 부적합 (TTS 범용화)
시장 긴급도(9) ≥ 8 → BUY/BORROW 우선 고려
기술 격차(2~3년) ≥ 2년 → BORROW 적합 (파트너십)
단, 딥페이크 탐지 Build 필요성 강화 (차별화 중요도 5→6)
→ 결론: BORROW + BUILD 유지, Build 비중 확대
```

### 3B 옵션 분석

| 전략 | 이전 (3/24) | 조정 (3/27) | 근거 |
|------|------------|------------|------|
| **Borrow** (핵심) | ElevenLabs Conv. AI 2.0 + Pindrop 검토 | ElevenLabs-IBM 스택 기반 평가 구체화. **Pindrop 긴급도 상향** | [[E-02]](#ref-e-02), [[G-21]](#ref-g-21) |
| **Build** (차별화) | 망 내장형 + 규제 대응 + 한국어 특화 | **딥페이크 탐지를 Build 핵심 축으로 격상**. KT/SKT 벤치마크 기준 설계. 3축 통합 | [[E-03]](#ref-e-03), [[E-04]](#ref-e-04) |
| **Buy** | 제외 | 유지 — 소규모 탐지 스타트업 인수 옵션 검토 (Reality Defender, ValidSoft 등) | [[G-11]](#ref-g-11) |

### 200점 채점표

| # | 평가 항목 | 세부1 (10) | 세부2 (10) | 세부3 (10) | 세부4 (10) | 소계 | 변동 |
|---|----------|-----------|-----------|-----------|-----------|------|------|
| 1 | **고객가치** | pain point 심각도: **9**(↑1) — 임계점 선언 [[G-01]](#ref-g-01), 31% 경험 [[E-01]](#ref-e-01) | 제공 가치 명확성: **8** — 유지 | 대체제 대비 우위: **6**(↑1) — KT/SKT 망 레벨 가치 실증 [[E-03]](#ref-e-03) | 고객 수용성: **6** — 유지 | **29** | +2 |
| 2 | **시장매력도** | 시장 규모: **8** — 딥페이크 탐지 $72억 교차 추가 [[G-10]](#ref-g-10) | 성장률: **8** — 유지 | 시장 타이밍: **9**(↑1) — INTERPOL 서밋 [[G-04]](#ref-g-04) + Hiya 여론 [[E-01]](#ref-e-01) | 규제/정책: **8** — EU D-128 [[G-15]](#ref-g-15) | **33** | +1 |
| 3 | **기술경쟁력** | TRL 수준: **9** — Voice Cloning 9, 탐지 8 | 특허 포트폴리오: **5** [미검증] | 기술 장벽: **6**(↑1) — 다층 방어 통합 장벽 [[P-01]](#ref-p-01) | 표준/인증: **7** — C2PA+EU [[G-15]](#ref-g-15) | **27** | +1 |
| 4 | **경쟁우위** | 시장 포지션: **5**(↑1) — KT/SKT 선례가 동종 진입 정당성 | 차별화 지속성: **7**(↑1) — "망=신뢰 인프라" 실증 [[E-03]](#ref-e-03), [[E-04]](#ref-e-04) | 경쟁사 대응력: **5** — 유지 | 생태계/파트너: **7** — 유지 | **24** | +2 |
| 5 | **실행가능성** | 내부 역량: **5** [미검증] | 투자 ROI: **8**(↑1) — KT 1,300억원 피해예방 벤치마크 [[E-03]](#ref-e-03) | 일정 현실성: **7** — Borrow 시 Q3~Q4 PoC | 리스크 관리: **5** [미검증] | **25** | +1 |
| | **총점** | | | | | **138/200** | **+7** |

### 판정: Conditional Go (120~159)

### 점수 변동 상세 (131→138, +7)

| 항목 | 이전 | 이번 | 변동 | 사유 |
|------|------|------|------|------|
| 고객가치 | 27 | 29 | +2 | pain point 현실화(+1), 망 레벨 가치 실증(+1) |
| 시장매력도 | 32 | 33 | +1 | 진입 임계 시점 도래(+1) |
| 기술경쟁력 | 26 | 27 | +1 | 다층 방어 장벽 학술 확인(+1) |
| 경쟁우위 | 22 | 24 | +2 | KT/SKT 선례로 진입 정당성(+1), 차별화 지속성 공인(+1) |
| 실행가능성 | 24 | 25 | +1 | KT 실적이 ROI 벤치마크 제공(+1) |

### Winning Strategy

```
[과제명]: Speech Generation — 망 내장형 Voice AI + 딥페이크 탐지 통합
[추천 방향]: Borrow + Build (Build 비중 확대)
[핵심 근거]:
  - 시장: TTS TAM $3.65~4.25B(2025), 딥페이크 탐지 $72억(2031) [G-10].
    글로벌 사기 피해 $4,420억, 소비자 31% 딥페이크 통화 경험 [E-01][G-04]
  - 기술: Voice Cloning TRL 9(임계점), 탐지 TRL 8(Pindrop 99.2%).
    탐지-생성 비대칭 구조적 — 다층 방어 필수 [P-01][P-02]
  - 사업: KT 1,300억원 피해예방, SKT 96% 정확도 — 국내 통신사 망 레벨
    탐지 상용 실증 완료. 소비자 2:1 여론 [E-01][E-03][E-04]
[리스크]:
  - 탐지 정확도 천장 (H 확률, H 영향) → 다층 방어, 적대적 훈련 지속
  - KT/SKT 6~12개월 선점 (H 확률, M 영향) → 3축 통합 차별화
  - 파트너 플랫폼 종속 (H 확률, H 영향) → 오픈소스 대안 + 핵심 레이어 자체 보유
  - 규제 불확실성 (M 확률, M 영향) → EU Code of Practice 6월 최종본 대응
[Next Action]:
  - [ ] Pindrop 파트너십 타진 (AICC 딥페이크 탐지) — 사업개발팀, 2026 Q2 **긴급**
  - [ ] ElevenLabs-IBM watsonx 스택 기반 Enterprise 평가 — 사업개발팀, 2026 Q2
  - [ ] 망 내장형 딥페이크 탐지 PoC 설계 (KT/SKT 벤치마크 기준) — 네트워크기술팀, 2026 Q3
  - [ ] 소규모 탐지 스타트업 인수 옵션 스크리닝 — 전략투자팀, 2026 Q2~Q3
  - [ ] AI 음성 고지·워터마킹 규제 대응 체계 설계 — 법무/기술규제팀, 2026 Q2
  - [ ] AICC 음성 서비스 딥페이크 취약점 평가 — 고객서비스부문, 2026 Q2
```

### 보완 필수 항목

| # | 보완 항목 | 이전 | 현재 | 긴급도 |
|---|----------|------|------|--------|
| 1 | 딥페이크 탐지 파트너십/솔루션 | 검토 필요 | **긴급 — KT/SKT 선점, 소비자 여론** | 🔴 |
| 2 | 파트너 선정 범위 확장 | TTS API→플랫폼 | ElevenLabs-IBM 스택 기반 평가로 구체화 | 🟡 |
| 3 | 자사 내부 역량 진단 | 미충족 | **여전히 미충족** — AI/음성 R&D | 🟡 |
| 4 | 망 내장형 Voice AI PoC | 미착수 | KT/SKT 벤치마크로 설계 기준 명확화 | 🟡 |
| 5 | 규제 대응 체계 | 미착수 | EU D-128, Code of Practice 6월 최종본 대기 | 🟡 |
| 6 | 특허 포트폴리오 전략 | 미착수 | 유지 | ⚪ |

---

## 5. 교차검증 결과

Validator 판정: **PARTIAL** (Critical 2건, Moderate 5건, Low 3건)

| # | 이슈 | 처리 |
|---|------|------|
| V-01 | Pindrop 99.2% 출처: E-05(Fraud Assist)가 아닌 별도 헬스케어 발표 | **해소** — G-21로 별도 등재, 출처 분리 완료 |
| V-02 | "10초 음성" 표현이 원문("a few seconds")과 불일치 | **해소** — "수초(a few seconds)"로 교정 |
| V-03 | "56개국" → INTERPOL 공식 "47 countries and organizations" | **해소** — "47개국+기관"으로 교정, 출처별 차이 주석 |
| V-04 | "범죄 1순위 도구" 과장 | **해소** — "글로벌 범죄 핵심 수단"으로 교정 |
| V-05 | TAM 수치 G-08 귀속 미확인 | **해소** — 이전 분석[I-01] 인용으로 명시 |
| V-06 | SKT "11억 건 차단" 미검증 | **해소** — 본 보고서에서 삭제 |
| V-07 | KT 피해예방 710억 vs 1,300억 시점 차이 | **해소** — "2025년 연간, 전자신문" 시점 명시 |
| V-08~10 | 고아 소스, 출처 신뢰도, 미인용 수치 | **잔존** (Low) — 고아 소스는 배경 참고 자료로 유지 |

최종 판정: **PASS** (Critical 이슈 모두 해소)

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | University at Buffalo — Deepfakes leveled up in 2025 (Siwei Lyu) | [링크](https://www.buffalo.edu/ubnow/stories/2026/01/lyu-conversation-deep-fakes-2026.html) | news | 2026-01 | [B] |
| <a id="ref-g-02"></a>G-02 | Fortune — Voice cloning crossed 'indistinguishable threshold' | [링크](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/) | news | 2025-12-27 | [B] |
| <a id="ref-g-03"></a>G-03 | EarthSky — Deepfakes are flooding the web | [링크](https://earthsky.org/human-world/deepfakes-flooding-the-internet-rise-in-2026/) | news | 2026 | [C] |
| <a id="ref-g-04"></a>G-04 | UN News — Global wake-up call to organised fraud | [링크](https://news.un.org/en/story/2026/03/1167144) | news | 2026-03 | [A] |
| <a id="ref-g-05"></a>G-05 | INTERPOL — Global summit call to action against fraud surge | [링크](https://www.interpol.int/News-and-Events/News/2026/INTERPOL-UNODC-global-summit-ends-with-call-to-action-against-fraud-surge) | news | 2026-03-17 | [A] |
| <a id="ref-g-06"></a>G-06 | Hiya Blog — MWC 2026: Voice is the New Battleground | [링크](https://blog.hiya.com/mwc-2026-voice-is-the-new-battleground-for-trust) | news | 2026-03 | [B] |
| <a id="ref-g-07"></a>G-07 | ElevenLabs — Series D ($500M, $11B) | [링크](https://elevenlabs.io/blog/series-d) | news | 2026-02-04 | [A] |
| <a id="ref-g-08"></a>G-08 | Biometric Update — Zoom Pindrop deepfake detection | [링크](https://www.biometricupdate.com/202603/zoom-expands-pindrop-deepfake-detection-to-customer-service) | news | 2026-03-12 | [B] |
| <a id="ref-g-09"></a>G-09 | GlobeNewswire — Pindrop Zoom Integration | [링크](https://www.globenewswire.com/news-release/2026/03/12/3254709/0/en/Pindrop-Zoom-Integration-Embeds-Real-Time-Deepfake-Detection-and-Identity-Verification-in-Zoom-Contact-Center.html) | news | 2026-03-12 | [B] |
| <a id="ref-g-10"></a>G-10 | MarketsandMarkets — Deepfake AI Market $7.27B by 2031 | [링크](https://finance.yahoo.com/news/deepfake-ai-market-worth-7-141500273.html) | news | 2025 | [B] |
| <a id="ref-g-11"></a>G-11 | Biometric Update — Reality Defender + ValidSoft partnership | [링크](https://www.biometricupdate.com/202508/to-fight-deepfake-voice-fraud-reality-defender-teams-up-with-validsoft) | news | 2025-08 | [B] |
| <a id="ref-g-12"></a>G-12 | McAfee — Deepfake Detector | [링크](https://www.mcafee.com/ai/deepfake-detector/) | news | 2026 | [A] |
| <a id="ref-g-13"></a>G-13 | KT kode 블로그 — KT 보이스피싱 탐지 2.0 이야기 | [링크](https://kode.kt.com/blog/article/8116) | news | 2025 | [B] |
| <a id="ref-g-14"></a>G-14 | 전자신문 — SKT 에이닷 전화 '위험 목소리 탐지' | [링크](https://www.etnews.com/20260318000294) | news | 2026-03-18 | [B] |
| <a id="ref-g-15"></a>G-15 | EU Digital Strategy — Code of Practice AI-generated content | [링크](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) | news | 2026 | [A] |
| <a id="ref-g-16"></a>G-16 | Jones Day — EU Code of Practice AI Labelling | [링크](https://www.jonesday.com/en/insights/2026/01/european-commission-publishes-draft-code-of-practice-on-ai-labelling-and-transparency) | news | 2026-01 | [B] |
| <a id="ref-g-17"></a>G-17 | 피카부랩스 — AI 기본법 완전 정리 | [링크](https://peekaboolabs.ai/blog/ai-basic-law-guide) | news | 2026 | [C] |
| <a id="ref-g-18"></a>G-18 | 신김 법률사무소 — 인공지능 기본법과 콘텐츠 산업 | [링크](https://www.shinkim.com/kor/media/newsletter/3142) | news | 2026 | [B] |
| <a id="ref-g-19"></a>G-19 | UNODC — Global summit mobilizes action against fraud | [링크](https://www.unodc.org/unodc/en/press/releases/2026/March/unodc-interpol-global-summit-mobilizes-action-against-fraud-surge.html) | news | 2026-03 | [A] |
| <a id="ref-g-20"></a>G-20 | Galveston Daily News — AI Deepfake Voice Calls Hit 1 in 4 | [링크](https://www.galvnews.com/state-of-the-call-2026-ai-deepfake-voice-calls-hit-1-in-4-americans-as/article_7d33386c-0819-5d0e-a328-7c0ab4f3f27b.html) | news | 2026-03-01 | [B] |
| <a id="ref-g-21"></a>G-21 | GlobeNewswire — Pindrop Healthcare Deepfake Detection (99.2% accuracy) | [링크](https://www.globenewswire.com/news-release/2026/02/26/3245758/) | news | 2026-02-26 | [A] |
| <a id="ref-e-01"></a>E-01 | Hiya — State of the Call 2026 (BusinessWire) | [링크](https://www.businesswire.com/news/home/20260301082723/en/State-of-the-Call-2026-AI-Deepfake-Voice-Calls-Hit-1-in-4-Americans-as-Consumers-Say-Scammers-Are-Beating-Mobile-Network-Operators-2-to-1) | IR/발표 | 2026-03-01 | [A] |
| <a id="ref-e-02"></a>E-02 | IBM Newsroom — ElevenLabs and IBM watsonx | [링크](https://newsroom.ibm.com/2026-03-25-enterprise-ai-finds-its-voice-elevenlabs-and-ibm-bring-premium-voice-capabilities-to-agentic-ai) | IR/발표 | 2026-03-25 | [A] |
| <a id="ref-e-03"></a>E-03 | 전자신문 — KT AI 보이스피싱 탐지 1,300억원 피해예방 | [링크](https://www.etnews.com/20251223000189) | IR/발표 | 2025-12-23 | [B] |
| <a id="ref-e-04"></a>E-04 | SKT 뉴스룸 — 에이닷 전화 보이스피싱 탐지 | [링크](https://news.sktelecom.com/217274) | IR/발표 | 2025 | [A] |
| <a id="ref-e-05"></a>E-05 | GlobeNewswire — Pindrop Fraud Assist | [링크](https://www.globenewswire.com/news-release/2026/03/17/3257231/0/en/Pindrop-Unveils-First-Agentic-Fraud-Investigation-Solution-to-Combat-Surging-AI-Driven-Fraud.html) | IR/발표 | 2026-03-17 | [A] |
| <a id="ref-e-06"></a>E-06 | PR Newswire — IBM Nick Holda 발언 | [링크](https://www.prnewswire.com/news-releases/enterprise-ai-finds-its-voice-elevenlabs-and-ibm-bring-premium-voice-capabilities-to-agentic-ai-302723870.html) | IR/발표 | 2026-03-25 | [A] |
| <a id="ref-p-01"></a>P-01 | Todisco et al. — ASVspoof 5 | [링크](https://www.sciencedirect.com/science/article/pii/S0885230825000506) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | PMC — Audio Deepfake Detection: Achievements and Ahead | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/) | paper | 2025 | [A] |
| <a id="ref-p-03"></a>P-03 | arXiv — PV-VASM Probabilistic Verification | [링크](https://arxiv.org/html/2603.10713) | paper | 2026-03 | [B] |
| <a id="ref-p-04"></a>P-04 | arXiv — Physics-Guided Deepfake Detection | [링크](https://arxiv.org/html/2512.06040) | paper | 2025-12 | [B] |
| <a id="ref-i-01"></a>I-01 | 2026-03-24 WTIS Standard — Speech Generation | 내부 | 내부 | 2026-03-24 | — |
| <a id="ref-i-02"></a>I-02 | 2026-03-20 WTIS Full — Speech Generation | 내부 | 내부 | 2026-03-20 | — |
