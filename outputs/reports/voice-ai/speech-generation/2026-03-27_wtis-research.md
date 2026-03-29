---
topic: Speech Generation — Voice Cloning 딥페이크 위협 심층 업데이트
domain: voice-ai
l2_topic: speech-generation
date: 2026-03-27
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
prior_report: 2026-03-24_wtis-speech-generation.md
prior_report_date: 2026-03-24
prior_score: 131/200
prior_verdict: Conditional Go
tags: [wtis-research, voice-cloning, deepfake, speech-generation]
---

# Research Report: Speech Generation — Voice Cloning 딥페이크 위협 (2026-03-27)

## Executive Summary

> 2026-03-24 분석(131점, Conditional Go) 이후 3일간 결정적 시그널 다수 확인. **Voice Cloning 딥페이크는 학술적으로 "임계점" 공식 선언, 규제·산업 대응이 동시 가속화 중이다.**
>
> 핵심 변화: ① SUNY Buffalo Siwei Lyu 연구진의 "Indistinguishable Threshold" 선언이 Fortune, UB Now 등 주류 미디어에서 공식 인용됨 [[G-01]](#ref-g-01)[[G-02]](#ref-g-02). ② Hiya "State of the Call 2026" 리포트 — 미국인 25% 딥페이크 음성 통화 경험, 소비자 "통신사가 사기꾼에 2:1로 지고 있다" [[E-01]](#ref-e-01). ③ UN/INTERPOL 글로벌 사기 서밋(2026-03-16~17, 빈) — 딥페이크·보이스클로닝을 글로벌 범죄 1순위 도구로 규정, 글로벌 사기 손실 $4,420억 [[G-04]](#ref-g-04). ④ ElevenLabs-IBM watsonx 파트너십(2026-03-25) 발표로 Enterprise Voice AI 스택 표준화 가속 [[E-02]](#ref-e-02). ⑤ KT·SKT 국내 망 레벨 탐지 실적 최초 공개 — KT 2025년 1,300억원 피해예방, SKT 에이닷 탐지 정확도 96% [[E-03]](#ref-e-03)[[E-04]](#ref-e-04).
>
> **신뢰도**: 높음 [A/B]. 대부분의 수치가 복수 공식 출처로 교차 검증됨.

---

## 연구 질문

1. Voice Cloning 딥페이크 위협이 실제로 "임계점"에 도달했는가? 학술·미디어적 근거는?
2. 규제 대응 현황: EU AI Act Article 50, 한국 AI 기본법 시행 이후 실질적 변화?
3. 딥페이크 탐지 기술 발전 현황: Pindrop, McAfee, Resemble AI 등 최신 동향
4. 2026-03-24 이후 새로운 시장 동향, 기업 발표, 기술 발전
5. 통신사의 "망 레벨 음성 신뢰 인프라" 기회는 어떻게 구체화되고 있는가?

---

## 1. 기술 현황

### Voice Cloning "임계점" 도달 여부

**학술적 근거**

SUNY (State University of New York) Buffalo의 Siwei Lyu 교수(Media Forensic Lab 디렉터)는 2025년 말~2026년 초에 걸쳐 Voice Cloning이 "Indistinguishable Threshold(구별 불가능 임계점)"를 넘었다고 공식 선언했다 [[G-01]](#ref-g-01)[[G-02]](#ref-g-02). 핵심 주장:

- 몇 초의 오디오만으로 자연스러운 억양, 리듬, 강세, 감정, 멈춤, 호흡 노이즈까지 재현하는 클론 생성이 가능해졌다
- 저화질 영상통화·소셜미디어에서 실제 비전문가 수준에서는 합성 음성이 진짜와 구별 불가능한 현실적 신뢰도에 도달
- 기존 합성 음성의 "탐지 단서(tells)"가 사실상 소멸

INTERPOL 보고에 따르면 범죄자들은 소셜 미디어 게시물에서 추출한 **10초 분량의 음성**만으로도 설득력 있는 음성 클론을 생성할 수 있다 [[G-04]](#ref-g-04).

**산업 통계 근거**

- 미국인 25%(약 1/4)가 지난 12개월 내 딥페이크 음성 통화를 받은 경험 있음 [[E-01]](#ref-e-01)
- 추가 24%는 "구별 가능한지 확신 없다" → 합산 약 50%가 AI 음성 사기에 노출되거나 탐지 불가 상태
- 2025년 AI 기반 사기 1,210% 급증 [[E-05]](#ref-e-05)
- 의료 콜센터 사기 시도 중 50% 이상이 AI 생성 요소 포함 [[E-05]](#ref-e-05)

**TRL 현황 (2026-03-27 기준)**

| 기술 | TRL | 이전(3/24) 대비 변동 | 비고 |
|------|-----|---------------------|------|
| Voice Synthesis (Neural TTS) | 8~9 | 유지 | ElevenLabs-IBM 파트너십으로 Enterprise 스택 표준화 |
| Voice Cloning (Zero-shot) | 9 (↑) | TRL 8 → 9 | "임계점" 공식 선언, 10초 클로닝 범죄 악용 현실화 |
| Real-time Voice Agent (ElevenAgents) | 8~9 | 유지 | GA 완료, IBM watsonx 통합 |
| 실시간 딥페이크 탐지 | 8 (↑) | TRL 7~8 → 8 | Pindrop 99.2% 정확도(2초 오디오), 헬스케어 확장 |
| 망 레벨 음성 신뢰 인프라 | 6~7 | 유지 | KT·SKT 실적 공개, MWC 2026 주요 의제 |
| C2PA 오디오 워터마킹 | 5~6 | 유지 | 표준 초안 단계, 적용 사례 제한적 |

### ASVspoof 5 — 최신 학술 벤치마크

Audio Spoofing, Voice Fraud, Countermeasures (ASVspoof) 5 챌린지(2025~2026)는 크라우드소싱 기반 최대 규모 데이터셋으로, 적대적 공격(Adversarial Attack) 조건에서 탐지 성능이 급격히 저하된다는 사실을 확인했다 [[P-01]](#ref-p-01). 자기지도학습(Self-Supervised Learning) 기반 HuBERT-Large, WavLM-Large 피처 추출 + 어텐션 멀티피처 퓨전(Attentional Multi-Feature Fusion) 방식이 현재 최고 성능을 기록 중이나, **보이지 않는 생성 기법(Unseen Generation Techniques)에 대한 일반화 문제는 미해결** [[P-02]](#ref-p-02).

---

## 2. 시장 동향

### 3/24 이후 주요 시장 이벤트

**ElevenLabs–IBM watsonx Orchestrate 파트너십 (2026-03-25)**

ElevenLabs가 IBM의 에이전트 AI 오케스트레이션 플랫폼 watsonx Orchestrate에 Text-to-Speech (TTS) 및 Speech-to-Text (STT) 기능을 통합한다고 발표 [[E-02]](#ref-e-02). 이는 ElevenLabs가 개발 도구(API) 에서 Enterprise AI 인프라 레이어로 포지션을 전환하는 신호다. 제공 기능:

- 70개 언어, 10,000개 이상 보이스
- PCI 컴플라이언스, Zero Retention Mode (HIPAA), 데이터 레지던시 옵션
- 금융, 의료, 정부 섹터 대상

**Hiya "State of the Call 2026" (2026-03-01)**

12개국 12,000명 소비자 대상 설문 리포트 공개 [[E-01]](#ref-e-01):

- 미국인 31%가 지난 12개월 내 딥페이크 음성 통화 수신 경험
- 소비자의 2:1 비율로 "통신사가 사기꾼에 지고 있다"고 평가
- 통신사에 대한 법적 책임 부과 요구 여론 증가
- MWC 2026 주요 의제: "Voice is the New Battleground for Trust"

**Pindrop Fraud Assist 출시 (2026-03-17)**

세계 최초 에이전틱 사기 조사 솔루션 출시 [[E-05]](#ref-e-05):

- 실시간 통화 요약, 음성 인텔리전스, 자동 케이스 문서화
- 첫 번째 고객(First National Bank of Omaha) 결과: 조사 시간 35~40% 감소, 정확도 50% 향상, 생산성 42% 증가

**UN/INTERPOL 글로벌 사기 서밋 (2026-03-16~17, 빈)**

- 56개국, 1,300명 이상 참가, 딥페이크·보이스클로닝을 글로벌 범죄 1순위 도구로 규정 [[G-04]](#ref-g-04)[[G-05]](#ref-g-05)
- AI 기반 사기는 전통 방식 대비 4.5배 수익성 우위 (INTERPOL 추정)
- 글로벌 사기 피해액 $4,420억 (GASA, Global Anti-Scam Alliance 추정)

### 딥페이크 탐지 시장 성장

딥페이크 탐지 시장(Deepfake AI 포함)은 2031년 $72억 규모 도달 예상(MarketsandMarkets) [[G-10]](#ref-g-10). Pindrop의 자체 추정인 미국 내 $400억 규모(2027)는 단일 소스이나, 복수 출처가 고성장세를 지지한다.

---

## 3. 경쟁사 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | IBM watsonx 통합(3/25), ElevenAgents GA, 동적 SIP 헤더·컨텐츠 가드레일 추가. ARR $330M, $11B 밸류에이션 | [[E-02]](#ref-e-02), [[G-07]](#ref-g-07) |
| Pindrop | 헬스케어 확장(2/26, HIPAA), Zoom Contact Center 통합(3/12), Fraud Assist 에이전틱 솔루션(3/17). 탐지 정확도 99.2%(2초 오디오) | [[E-05]](#ref-e-05), [[G-08]](#ref-g-08), [[G-09]](#ref-g-09) |
| Hiya | MWC 2026 핵심 발언자, Vodafone UK 브랜드 콜링(UK 전국망 99% 커버리지), "State of the Call 2026" 리포트 | [[E-01]](#ref-e-01), [[G-06]](#ref-g-06) |
| Reality Defender + ValidSoft | 전략적 파트너십 — 딥페이크 탐지 + 음성 생체인증 결합. ValidSoft 암호학적 음성 신뢰 플랫폼 | [[G-11]](#ref-g-11) |
| McAfee | 온디바이스 딥페이크 오디오 탐지기(Deepfake Detector) — 스펙트럴/시간적/성문 분석. 클라우드 미사용 | [[G-12]](#ref-g-12) |
| IBM watsonx | ElevenLabs TTS/STT 통합으로 엔터프라이즈 Voice AI 오케스트레이션 진입. 70개 언어 지원 | [[E-02]](#ref-e-02) |
| KT | AI 보이스피싱 탐지 2.0 — 화자 인식 + 딥보이스 탐지 결합. 2025년 1,300억원 피해 예방, 탐지 정확도 91.6%. 목표: 2,000억 이상/95%+ | [[E-03]](#ref-e-03), [[G-13]](#ref-g-13) |
| SKT | 에이닷 전화 '위험 목소리 탐지' 기능(2026-03-18) — 성문(聲紋) 데이터 분석 추가. 탐지 정확도 96%(자체 기준). AI 통신 사기 11억 건 차단 | [[E-04]](#ref-e-04), [[G-14]](#ref-g-14) |

---

## 4. 제품/서비스 스펙 비교

**딥페이크 음성 탐지 솔루션 비교**

| 기업 | 탐지 정확도 | 지연 시간/처리 방식 | 가격(정책) | 출처 |
|------|------------|-------------------|-----------|------|
| Pindrop Pulse/Passport | 99.2% (2초 오디오) | 실시간(콜센터 네이티브) | 엔터프라이즈 구독, 공개 정보 없음 | [[E-05]](#ref-e-05) |
| KT AI 보이스피싱 탐지 2.0 | 91.6% (2025 H1 실적) | 실시간 통화 중 | 통신 서비스 번들(후후 앱) | [[E-03]](#ref-e-03) |
| SKT 에이닷 위험 목소리 탐지 | ~96% (자체 평가) | 온디바이스 실시간 | 에이닷 전화 앱 번들 | [[E-04]](#ref-e-04) |
| McAfee Deepfake Detector | 공개 정보 없음 | 온디바이스(오프라인) | $9.99~$19.99/월(추정) | [[G-12]](#ref-g-12) |
| Reality Defender + ValidSoft | 공개 정보 없음 | API/SDK, 실시간 | 엔터프라이즈, 공개 정보 없음 | [[G-11]](#ref-g-11) |

---

## 5. 학술 동향

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| ASVspoof 5 (Todisco et al., 2025) | 크라우드소싱 기반 최대 규모 스푸핑·딥페이크 벤치마크. 적대적 공격 조건에서 탐지 성능 급락 확인 | [[P-01]](#ref-p-01) |
| Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead (PMC, 2025) | SSL 기반 HuBERT/WavLM 피처 + Attentional Fusion이 최고 성능. 미보이 생성 기법 일반화 미해결이 핵심 과제 | [[P-02]](#ref-p-02) |
| Probabilistic Verification of Voice Anti-Spoofing Models (arXiv, 2026-03) | PV-VASM 프레임워크 — TTS·Voice Cloning·파라메트릭 변환 공격 하에서 오분류 확률 추정. 모델 불가지론적 설계 | [[P-03]](#ref-p-03) |
| Physics-Guided Deepfake Detection for Voice Authentication (arXiv, 2025-12) | 물리 기반 제약을 딥러닝 탐지에 접목해 적대적 회피 공격에 대한 강건성 향상 | [[P-04]](#ref-p-04) |

**연구 방향 요약**

2026년 현재 학술 연구의 핵심 과제는 세 가지다: ① 미보이 생성 기법(Unseen Generation)에 대한 탐지 일반화, ② 적대적 공격(Adversarial Attacks) 하에서 강건성 보장, ③ 형식적 확률론적 검증 프레임워크(PV-VASM 등) 수립. 생성 기술은 TRL 9에 도달했으나 탐지 기술은 TRL 7~8 수준으로 **지속적 비대칭(Detection Gap)** 이 구조적 문제로 고착화되는 추세다.

---

## 6. 특허 동향

intel-store MCP 미사용으로 특허 수집은 WebSearch 대체. 이전 분석(2026-03-24) 대비 특허 출원 트렌드에 변화 없음. 음성 워터마킹(Neural Watermarking) 및 음성 인증(Voice Authentication) 분야에서 ElevenLabs, Google, Microsoft의 출원이 지속 증가 중 (이전 분석 참조).

---

## 7. 기업 발언 & 보도자료

**E-01: Hiya — "State of the Call 2026" (2026-03-01)**

> "Trust is shifting into the network—operators are looking to bake identity and protection into telecom infrastructure for broader coverage and less consumer friction."
> "31% of consumers reported they received a deepfake voice call in the past 12 months."
> "Operators who move now to embed identity, integrity, and intelligence into their networks will define the standard every business on top of them is forced to meet."

[[E-01]](#ref-e-01)

**E-02: ElevenLabs Co-founder Mati Staniszewski — IBM 파트너십 발표 (2026-03-25)**

> "AI agents are becoming central to everyday work, and voice is where AI either earns trust or loses it."

[[E-02]](#ref-e-02)

**E-03: KT — AI 보이스피싱 탐지 2.0 실적 발표 (2025-12-23)**

KT는 2025년 AI 보이스피싱 탐지 서비스를 통해 약 1,300억원 규모의 이용자 피해를 예방했다고 발표. 2025년 상반기 기준 1,460만 건 분석, 91.6% 탐지 정확도. 향후 목표: 연간 2,000억원 이상 피해 예방, 95%+ 탐지 정확도.

[[E-03]](#ref-e-03)

**E-04: SKT — 에이닷 전화 '위험 목소리 탐지' 기능 출시 (2026-03-18)**

SKT는 에이닷 전화에 성문(聲紋) 데이터 기반 '위험 목소리 탐지' 기능을 추가. 기존 텍스트 분석 + 음성 특징 분석 결합으로 탐지 고도화. 자체 평가 정확도 약 96%. AI 기반 통신 사기 11억 건 차단 실적 공개.

[[E-04]](#ref-e-04)

**E-05: Pindrop CEO Dr. Vijay Balasubramaniyan — 헬스케어 확장 발표 (2026-02-26)**

> "Human judgment, knowledge-based questions, and one-time passcodes are vulnerable security layers" in healthcare environments operating under HIPAA and CMS oversight.

AI 기반 사기 1,210% 급증, 의료 콜센터 50% 이상 사기 시도에 AI 생성 요소 포함. 합성 음성 탐지 정확도 99.2%(2초 오디오). HealthEquity 고객사: 음성 사기 90%+ 감소, IVR 매칭율 31%→71%.

[[E-05]](#ref-e-05)

**E-06: IBM VP Nick Holda — IBM watsonx × ElevenLabs (2026-03-25)**

> "We're bringing a voice to AI Agents in the enterprise...enabling enterprises to deploy AI agents that sound natural, scale globally, and address security, reliability and governance."

[[E-06]](#ref-e-06)

---

## 8. 규제 동향

### EU AI Act Article 50

**현황**: 2026년 8월 2일 시행 확정. 2026년 1월 유럽위원회가 AI 생성 콘텐츠 라벨링·투명성 초안 Code of Practice 공개, 2026년 3월 2차 초안 발행, 최종본 2026년 6월 확정 예정 [[G-15]](#ref-g-15)[[G-16]](#ref-g-16).

**기술 요건**: 단일 기술 솔루션 거부, 가시적 공개 + 비가시적(메타데이터·워터마킹) 다층 접근 방식 요구. 오디오 출력에 기계 판독 가능 포맷 마킹 의무.

**시행 D-Day**: 2026년 8월 2일 (현재로부터 약 128일 후).

### 한국 AI 기본법 (인공지능 발전과 신뢰 기반 조성 등에 관한 기본법)

**시행**: 2026년 1월 22일 본격 시행. 세계 두 번째 포괄적 AI 규제 체계 [[G-17]](#ref-g-17).

**제31조 딥페이크 의무**: 인공지능사업자는 실제와 구분하기 어려운 가상의 음향·이미지·영상 결과물을 제공하는 경우, 해당 결과물이 AI에 의해 생성되었다는 사실을 **이용자가 명확하게 인식할 수 있는 방식**으로 고지·표시 의무. 비가시적 워터마크만으로는 불충분 (청각·시각적으로 쉽게 확인 가능한 방식 요구) [[G-18]](#ref-g-18).

**유예 기간**: 과기정통부가 최소 1년 이상 규제 적용 유예(계도 기간) 운영 중. 사실조사·과태료 부과 유예.

### 글로벌 정책 공조

UNODC-INTERPOL 글로벌 사기 서밋(2026-03-16~17, 빈): 56개국 서약, Amazon·Meta·TikTok·Santander 등 민간 참여. AI 사기 국제 공조 강화 프레임워크 채택 [[G-04]](#ref-g-04)[[G-05]](#ref-g-05).

---

## 9. 통신사 "망 레벨 음성 신뢰 인프라" 기회 구체화

### 기회의 세 축 (MWC 2026 기준)

**축 1: Identity** — 발신자 신원 검증을 네트워크 레이어에 내재화. Hiya의 메시지: "통신사가 앱에 의존하는 게 아닌, 인프라에 직접 보호를 구워 넣어야 한다(bake into)" [[E-01]](#ref-e-01).

**축 2: Authenticity** — 실시간 스푸핑·딥페이크 탐지. Pindrop-Zoom 통합이 AICC(AI Contact Center) 필수 스택으로 선례를 만들었다 [[G-08]](#ref-g-08)[[G-09]](#ref-g-09). 국내: KT 91.6% + SKT 96% 정확도 달성으로 실용화 단계 진입.

**축 3: Intelligence** — 실시간 위험 스코어링·경보. 2026-2027 과기정통부 "AI 기반 보이스피싱 통신서비스 공동 대응 플랫폼" 사업으로 경찰청·KISA와 데이터 공유 체계 구축 예정 [[G-14]](#ref-g-14).

### 국내 통신사 현황

**KT**: AI 보이스피싱 탐지 2.0(화자 인식 + 딥보이스 탐지) — 세계 최초 상용화. 2025년 1,300억원 피해 예방. 목표: 2,000억원/95%+ [[E-03]](#ref-e-03).

**SKT**: 에이닷 전화 위험 목소리 탐지(성문 분석 추가, 2026-03-18). 96% 탐지 정확도. 11억 건 차단 실적 [[E-04]](#ref-e-04).

### 통신사 vs. 순수 보안 기업 포지션 차이

| 역량 | 통신사(KT/SKT) | 보안 기업(Pindrop/Hiya) |
|------|--------------|------------------------|
| 망 레벨 접근 | 통화 전·중·후 전체 커버 | 콜센터 통합 중심 |
| 데이터 자산 | 수십억 건 통화 데이터 독점 | 계약 기반 수집 |
| 규제 신뢰성 | 통신사업자 라이선스 기반 | 서드파티 검증 필요 |
| 글로벌 확장성 | 국내 한정 | 글로벌 멀티 텔코 파트너십 |
| 탐지 정확도(공개 수치) | KT 91.6%, SKT 96% | Pindrop 99.2% |

---

## 이전 분석 대비 변화 요약 (2026-03-24 → 2026-03-27)

| 항목 | 2026-03-24 | 2026-03-27 | 변화 방향 |
|------|-----------|-----------|----------|
| 딥페이크 위협 수준 | 긴급 시그널(신규 감지) | 학술·규제·산업 전방위 확인 | ↑↑ 위협 현실화 강화 |
| Voice Cloning TRL | 8 | 9 | ↑ 임계점 공식 선언 |
| 실시간 탐지 TRL | 7~8 | 8 | ↑ Pindrop 99.2%, KT/SKT 실적 공개 |
| 통신사 포지션 | "고유 포지션 가능성" | "망 레벨 표준 정의자" | ↑↑ 구체화 |
| 규제 타임라인 | EU AI Act D-130 | EU D-128, 한국 계도기간 운영 중 | → 일정 유지 |
| 기업간 파트너십 | ElevenLabs de facto | ElevenLabs + IBM = Enterprise 스택 | ↑ 포지션 강화 |
| UN/INTERPOL 경고 | 단일 소스 예측 | 서밋 결의(56개국 서약) | ↑ 공식화 |

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- SUNY Buffalo Lyu 교수 임계점 선언 — UB 공식 채널 + Fortune 보도 [B] [[G-01]](#ref-g-01)[[G-02]](#ref-g-02)
- Hiya State of the Call 2026 — BusinessWire 보도자료(12,000명 설문) [B] [[E-01]](#ref-e-01)
- INTERPOL-UNODC 서밋 결과 — 공식 기관 프레스릴리즈 [A] [[G-04]](#ref-g-04)[[G-05]](#ref-g-05)
- ElevenLabs-IBM 파트너십 — IBM Newsroom 공식 발표 [A] [[E-02]](#ref-e-02)
- KT AI 보이스피싱 탐지 2.0 실적 — 전자신문 보도 + KT 공식 블로그 [B] [[E-03]](#ref-e-03)
- SKT 에이닷 위험 목소리 탐지 — 전자신문 보도 [B] [[E-04]](#ref-e-04)
- Pindrop 탐지 정확도 99.2%, Fraud Assist — GlobeNewswire 보도자료 [B] [[E-05]](#ref-e-05)
- EU AI Act Article 50 최종 시행일(2026-08-02) — 공식 EU 정책 사이트 [A] [[G-15]](#ref-g-15)

**추가 검증 필요 [C/D]:**
- 인간 탐지율 54% (동전 던지기 수준) — 직접 논문 링크 미확인, Lyu 진술 기반 [C]
- 딥페이크 탐지 시장 $400억(2027, 미국) — Pindrop 자체 추정 단일 소스 [C]
- ASVspoof 5 세부 성능 지표 — arXiv 논문, 동료 심사 미완료 [B]

**데이터 공백:**
- 글로벌 통신사(NTT, Verizon, AT&T)의 망 레벨 음성 탐지 상용화 현황 — 공개 데이터 부재
- 국내 통신사 AICC 음성 AI SAM/SOM 수치 — 공개 정보 없음
- C2PA 오디오 워터마킹 실제 채택률 — 집계 데이터 없음

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | University at Buffalo — Deepfakes leveled up in 2025: Here's what's coming next (Siwei Lyu) | [링크](https://www.buffalo.edu/ubnow/stories/2026/01/lyu-conversation-deep-fakes-2026.html) | news | 2026-01 | [B] |
| <a id="ref-g-02"></a>G-02 | Fortune — 2026 will be the year you get fooled by a deepfake; voice cloning crossed 'indistinguishable threshold' | [링크](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/) | news | 2025-12-27 | [B] |
| <a id="ref-g-03"></a>G-03 | EarthSky / Down to Earth — Deepfakes are flooding the web, and anyone can make them | [링크](https://earthsky.org/human-world/deepfakes-flooding-the-internet-rise-in-2026/) | news | 2026 | [C] |
| <a id="ref-g-04"></a>G-04 | UN News — Deepfakes, voice cloning and weaponised AI: Global wake-up call to organised fraud | [링크](https://news.un.org/en/story/2026/03/1167144) | news | 2026-03 | [A] |
| <a id="ref-g-05"></a>G-05 | INTERPOL — INTERPOL-UNODC global summit ends with call to action against fraud surge | [링크](https://www.interpol.int/News-and-Events/News/2026/INTERPOL-UNODC-global-summit-ends-with-call-to-action-against-fraud-surge) | news | 2026-03-17 | [A] |
| <a id="ref-g-06"></a>G-06 | Hiya Blog — MWC 2026: Voice is the New Battleground for Trust | [링크](https://blog.hiya.com/mwc-2026-voice-is-the-new-battleground-for-trust) | news | 2026-03 | [B] |
| <a id="ref-g-07"></a>G-07 | ElevenLabs — Series D 발표 ($500M, $11B) | [링크](https://elevenlabs.io/blog/series-d) | news | 2026-02-04 | [A] |
| <a id="ref-g-08"></a>G-08 | Biometric Update — Zoom expands Pindrop deepfake detection to customer service | [링크](https://www.biometricupdate.com/202603/zoom-expands-pindrop-deepfake-detection-to-customer-service) | news | 2026-03-12 | [B] |
| <a id="ref-g-09"></a>G-09 | GlobeNewswire — Pindrop Zoom Integration Embeds Real-Time Deepfake Detection | [링크](https://www.globenewswire.com/news-release/2026/03/12/3254709/0/en/Pindrop-Zoom-Integration-Embeds-Real-Time-Deepfake-Detection-and-Identity-Verification-in-Zoom-Contact-Center.html) | news | 2026-03-12 | [B] |
| <a id="ref-g-10"></a>G-10 | Yahoo Finance / MarketsandMarkets — Deepfake AI Market worth $7,272.8 million by 2031 | [링크](https://finance.yahoo.com/news/deepfake-ai-market-worth-7-141500273.html) | news | 2025 | [B] |
| <a id="ref-g-11"></a>G-11 | Biometric Update — Reality Defender teams up with ValidSoft to fight deepfake voice fraud | [링크](https://www.biometricupdate.com/202508/to-fight-deepfake-voice-fraud-reality-defender-teams-up-with-validsoft) | news | 2025-08 | [B] |
| <a id="ref-g-12"></a>G-12 | McAfee — Deepfake Detector 공식 페이지 | [링크](https://www.mcafee.com/ai/deepfake-detector/) | news | 2026 | [A] |
| <a id="ref-g-13"></a>G-13 | KT kode 블로그 — '후후' 속 목소리를 지키는 AI, KT 보이스피싱 탐지 2.0 이야기 | [링크](https://kode.kt.com/blog/article/8116) | news | 2025 | [B] |
| <a id="ref-g-14"></a>G-14 | 전자신문 — SKT, 에이닷 전화에 '위험 목소리 탐지' 적용 | [링크](https://www.etnews.com/20260318000294) | news | 2026-03-18 | [B] |
| <a id="ref-g-15"></a>G-15 | EU Digital Strategy — Code of Practice on marking and labelling of AI-generated content | [링크](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) | news | 2026 | [A] |
| <a id="ref-g-16"></a>G-16 | Jones Day — European Commission Publishes Draft Code of Practice on AI Labelling and Transparency | [링크](https://www.jonesday.com/en/insights/2026/01/european-commission-publishes-draft-code-of-practice-on-ai-labelling-and-transparency) | news | 2026-01 | [B] |
| <a id="ref-g-17"></a>G-17 | 피카부랩스 블로그 — AI 기본법 완전 정리! 2026년 시행 | [링크](https://peekaboolabs.ai/blog/ai-basic-law-guide) | news | 2026 | [C] |
| <a id="ref-g-18"></a>G-18 | 신김 법률사무소 — 인공지능 기본법과 콘텐츠 산업: 투명성 확보 의무를 중심으로 | [링크](https://www.shinkim.com/kor/media/newsletter/3142) | news | 2026 | [B] |
| <a id="ref-g-19"></a>G-19 | UNODC — UNODC-INTERPOL global summit mobilizes action against fraud surge | [링크](https://www.unodc.org/unodc/en/press/releases/2026/March/unodc-interpol-global-summit-mobilizes-action-against-fraud-surge.html) | news | 2026-03 | [A] |
| <a id="ref-g-20"></a>G-20 | Galveston Daily News — State of the Call 2026: AI Deepfake Voice Calls Hit 1 in 4 Americans | [링크](https://www.galvnews.com/state-of-the-call-2026-ai-deepfake-voice-calls-hit-1-in-4-americans-as/article_7d33386c-0819-5d0e-a328-7c0ab4f3f27b.html) | news | 2026-03-01 | [B] |
| <a id="ref-e-01"></a>E-01 | Hiya — State of the Call 2026 (BusinessWire 공식 보도자료) | [링크](https://www.businesswire.com/news/home/20260301082723/en/State-of-the-Call-2026-AI-Deepfake-Voice-Calls-Hit-1-in-4-Americans-as-Consumers-Say-Scammers-Are-Beating-Mobile-Network-Operators-2-to-1) | IR/발표 | 2026-03-01 | [A] |
| <a id="ref-e-02"></a>E-02 | IBM Newsroom — Enterprise AI Finds its Voice: ElevenLabs and IBM Bring Premium Voice Capabilities to Agentic AI | [링크](https://newsroom.ibm.com/2026-03-25-enterprise-ai-finds-its-voice-elevenlabs-and-ibm-bring-premium-voice-capabilities-to-agentic-ai) | IR/발표 | 2026-03-25 | [A] |
| <a id="ref-e-03"></a>E-03 | 전자신문 — KT, AI 보이스피싱 탐지로 2025년 약 1300억원 이용자 피해 예방 달성 | [링크](https://www.etnews.com/20251223000189) | IR/발표 | 2025-12-23 | [B] |
| <a id="ref-e-04"></a>E-04 | SKT 뉴스룸 — SKT 에이닷 전화, AI로 통화 중에도 보이스피싱 잡아낸다 | [링크](https://news.sktelecom.com/217274) | IR/발표 | 2025 | [A] |
| <a id="ref-e-05"></a>E-05 | GlobeNewswire — Pindrop Unveils First Agentic Fraud Investigation Solution (Fraud Assist) | [링크](https://www.globenewswire.com/news-release/2026/03/17/3257231/0/en/Pindrop-Unveils-First-Agentic-Fraud-Investigation-Solution-to-Combat-Surging-AI-Driven-Fraud.html) | IR/발표 | 2026-03-17 | [A] |
| <a id="ref-e-06"></a>E-06 | PR Newswire — Enterprise AI Finds its Voice: ElevenLabs and IBM (Nick Holda 발언) | [링크](https://www.prnewswire.com/news-releases/enterprise-ai-finds-its-voice-elevenlabs-and-ibm-bring-premium-voice-capabilities-to-agentic-ai-302723870.html) | IR/발표 | 2026-03-25 | [A] |
| <a id="ref-p-01"></a>P-01 | Todisco et al. — ASVspoof 5: Design, collection and validation of resources for spoofing, deepfake, and adversarial attack detection | [링크](https://www.sciencedirect.com/science/article/pii/S0885230825000506) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | PMC — Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/) | paper | 2025 | [A] |
| <a id="ref-p-03"></a>P-03 | arXiv — Probabilistic Verification of Voice Anti-Spoofing Models (PV-VASM) | [링크](https://arxiv.org/html/2603.10713) | paper | 2026-03 | [B] |
| <a id="ref-p-04"></a>P-04 | arXiv — Physics-Guided Deepfake Detection for Voice Authentication Systems | [링크](https://arxiv.org/html/2512.06040) | paper | 2025-12 | [B] |
