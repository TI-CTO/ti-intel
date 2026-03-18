---
type: wtis-research
topic: speech-perception
domain: voice-ai
l2_topic: speech-perception
date: 2026-03-18
parent: 2026-03-18_wtis-speech-perception
agent: research-deep
confidence: medium-high
status: completed
sources_used: [websearch, webfetch]
---

# WTIS 심층 리서치: Speech Perception & Interaction

## Executive Summary

> Speech Perception & Interaction(음성 지각·상호작용)은 감정 인식(Emotional Analysis), 대화 맥락 인식(Context Recognition), 턴테이킹 예측(Interrupt/Turn-Taking)의 3개 L3로 구성되며, 상이한 성숙도를 보인다. 글로벌 감정 인식 시장은 2024년~2030년 CAGR 16%로 성장, 2030년 최소 65억~최대 1,365억 달러(기관별 추정 범위 큰 편)로 전망된다. Conversational AI 시장은 CAGR 23.7%로 더욱 빠르게 성장 중이며, 통신사 AICC 시장은 국내 연 23.7% 성장 추정이다. 기술 성숙도 측면에서 실시간 감정 분석(TRL 7~8)은 이미 상용 배포 단계이나, 멀티모달 정밀도(TRL 6~7)와 자연스러운 턴테이킹(TRL 7)은 여전히 개선 중이다. EU AI Act Article 5(1)(f)가 2025년 2월부터 직장 내 감정 인식을 원칙적으로 금지하는 등 규제 리스크가 주요 변수로 부상했다. 신뢰도: 시장 규모 [B], 기술 지표 [A/B], 규제 현황 [A].

---

## 연구 질문

> Speech Perception & Interaction L2의 (1) 시장 규모·성장성, (2) L3별 기술 성숙도 및 성능 벤치마크, (3) 국내외 주요 플레이어의 경쟁 구도, (4) 적용 규제·표준 현황을 종합적으로 파악하여 WTIS 200점 채점 근거를 마련한다.

---

## 1. 시장 분석

### TAM / SAM / SOM

**글로벌 TAM — 감정 탐지·인식 (EDR)**

감정 탐지 및 인식(EDR) 시장은 2024년 약 220~310억 달러 수준으로 추정되며, 기관마다 범위 정의가 달라 추정치 편차가 크다 [[G-01]](#ref-g-01)[[G-02]](#ref-g-02).

- Grand View Research: 2024~2030 CAGR 16.0%, 2030년 **USD 136.46B** [[G-01]](#ref-g-01)
- MarketsandMarkets: 2027년 **USD 42.9B** (CAGR 명시 없음) [[G-02]](#ref-g-02)
- Fortune Business Insights: 2032년까지 성장 지속 추정 [[G-03]](#ref-g-03)
- Newstrail/Emergen Research: 음성 감정 인식 세부 세그먼트 2025~2032 CAGR 12%, 2025년 USD 1.3B → 2032년 USD 3.1B [[G-04]](#ref-g-04)

> 주의: 기관별 "EDR 시장"의 정의 범위(생체센서 포함 여부, 영상·음성·텍스트 모두 포함 여부)가 달라 수치 편차 10배 이상 발생. 음성 전용 세그먼트는 Newstrail 수치(1.3B→3.1B)가 더 보수적이고 실질적.

**글로벌 SAM — Conversational AI (Turn-Taking·Context 포함)**

- Grand View Research: 2024년 USD 11.58B → 2030년 **USD 41.39B**, CAGR **23.7%** [[G-05]](#ref-g-05)
- MarketsandMarkets: 2025년 USD 17.05B → 2031년 USD 49.80B, CAGR **19.6%** [[G-06]](#ref-g-06)
- Voice Assistant 세부 시장: 2024년 USD 7.35B → 2030년 USD 33.74B, CAGR **26.5%** [[G-07]](#ref-g-07)

**국내 SOM — AICC (AI Contact Center)**

- 글로벌 AICC: 2020~2025 CAGR 25%, 2025년 도달 규모 USD 36.1B [[G-08]](#ref-g-08)
- 국내 AICC: 2020~2030 CAGR **23.7%** 추정 [[G-08]](#ref-g-08)
- SKT·KT·LG U+: 국내 AICC 시장 규모 **약 5,000억 원** 공략 선언 (2023년 기준, 이후 성장) [[G-09]](#ref-g-09)
- KT: 2025년 AICC 매출 목표 **3,000억 원 이상** [[G-10]](#ref-g-10)

### 연도별 시장 전망

**Conversational AI 시장 성장 추이 (글로벌)**

| 연도 | 규모 (USD) | CAGR 출처 |
|------|-----------|-----------|
| 2024 | 11.58B | [[G-05]](#ref-g-05) |
| 2025 | 17.05B | [[G-06]](#ref-g-06) |
| 2026 | 예상 ~14~20B | 추정치 |
| 2030 | 41.39B | [[G-05]](#ref-g-05) |
| 2031 | 49.80B | [[G-06]](#ref-g-06) |

**음성 감정 인식 세그먼트 전망**

| 연도 | 규모 (USD) | 출처 |
|------|-----------|------|
| 2025 | 1.3B | [[G-04]](#ref-g-04) |
| 2032 | 3.1B (CAGR 12%) | [[G-04]](#ref-g-04) |
| 2030 | 136.46B (전체 EDR) | [[G-01]](#ref-g-01) |

---

## 2. 기술 성숙도

### TRL 현황 (L3별)

**L3 성숙도 요약**

| L3 기술 | TRL | 상용화 단계 | 비고 |
|---------|-----|------------|------|
| Emotional Analysis (음성 감정 인식) | 7~8 | 부분 상용 배포 | AICC 통합 다수, 정밀도 한계 |
| Context Recognition (대화 맥락 인식) | 7~8 | 상용 배포 확대 중 | LLM 통합으로 급속 발전 |
| Interrupt / Turn-Taking 예측 | 6~7 | 검증·초기 배포 | 저지연 자연스러움 미완성 |

- **TRL 정의**: 1=기초 연구, 5=유효성 검증, 7=시연, 8=완성, 9=성공적 운용 [D]

### 성능 벤치마크

**음성 감정 인식 — IEMOCAP 벤치마크**

| 모델 | Accuracy (IEMOCAP) | 모달리티 | 출처 |
|------|-------------------|---------|------|
| MemoCMT (Cross-Modal Transformer) | UW 81.33% / W 81.85% | 음성+텍스트 | [[P-01]](#ref-p-01) |
| Edge Compact Transformer | ~81% UW | 비디오+오디오+텍스트 | [[P-02]](#ref-p-02) |
| MAMBA Trimodal Fusion | 74.3% | 3-modal | [[P-03]](#ref-p-03) |
| Hierarchical Transformer | 71.10% Acc / 70.97% F1 | 다모달 | [[P-04]](#ref-p-04) |
| EmoShiftNet (Multi-Task) | F1 0.6885 | 대화 감정 | [[P-05]](#ref-p-05) |

> 2025년 최고 성능: IEMOCAP UW 81.33% (MemoCMT). 2023년 대비 약 3~5%p 향상. 실용 배포 임계치(80%+)에 근접했으나 실제 환경 노이즈·방언·문화적 차이에서는 성능 하락 예상.

**턴테이킹 / 바지-인 감지 — 레이턴시 벤치마크**

| 지표 | 수치 | 기준 | 출처 |
|------|------|------|------|
| Production 목표 레이턴시 | ≤ 800ms | P95 응답 | [[G-11]](#ref-g-11) |
| 이상적 응답 레이턴시 | 500ms 이하 | 인간 대화 수준 | [[G-11]](#ref-g-11) |
| Hume AI EVI 3 | < 300ms TTS 출력 (실질 1.2초) | May 2025 | [[G-12]](#ref-g-12) |
| Cartesia | 45ms 레이턴시 | March 2025 | [[G-13]](#ref-g-13) |
| 오디오 청크 처리 | 10~20ms 간격 | VAD 기준 | [[G-14]](#ref-g-14) |
| Deepgram Nova | 300ms 미만 실시간 STT | 스트리밍 오디오 | [[G-15]](#ref-g-15) |

**대화 상태 추적 (DST) — LLM 기반**

- SpokenWOZ 데이터셋 기반 Speech-LLM DST: 기존 대비 state-of-the-art 달성 (2025) [[P-06]](#ref-p-06)
- LDST (오픈소스 소형 LLM 기반 DST): ChatGPT 수준 성능, 제로샷/퓨샷 모두 SOTA [[P-07]](#ref-p-07)
- 한계: 복잡한 멀티턴, 시각적 그라운딩이 필요한 작업에서 여전히 성능 저하 [[G-16]](#ref-g-16)

### 핵심 기술 진전

**감정 인식**
- Whisper 임베딩 + 수공 오디오 디스크립터 결합으로 경량 모델 성능 향상 [[P-08]](#ref-p-08)
- 600+ 감정 태그 인식 (Hume AI Expression Measurement) [[G-13]](#ref-g-13)
- EV4-mini (Hume AI, 2026.01): 11개 언어 지원, 한국어 포함 [[G-12]](#ref-g-12)
- 멀티모달(음성+비디오+텍스트) 융합이 단일 모달 대비 7~10%p 성능 우위

**턴테이킹**
- VAD(Voice Activity Detector) 기반에서 LLM 맥락 인식 기반 턴테이킹으로 전환 중
- OpenAI: 오디오 팀 통합, 2026 Q1 목표로 맥락 인식 턴테이킹 모델 개발 중 [[G-17]](#ref-g-17)
- 실시간 스트리밍 처리와 배경 노이즈 억제가 핵심 과제

**대화 맥락**
- Naver CLOVA Speech X: 감정 표현 가능한 음성 합성, 멀티모달 오디오+이미지 이해 [[G-18]](#ref-g-18)
- LLM 통합 End-to-End 방식이 파이프라인 방식 대체 가속화

---

## 3. 경쟁 환경

### 글로벌 플레이어

**주요 글로벌 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Hume AI | EVI 3 (May 2025) 출시, 300ms 레이턴시 달성. EV4-mini (Jan 2026) 11개 언어 멀티링구얼 지원. 개발자 10만+ 확보, 2026년 매출 $100M 목표. 총 조달 $72.8M (Series B). | [[G-12]](#ref-g-12), [[G-13]](#ref-g-13) |
| Google | Contact Center AI에 DeepMind 음성 모델+LLM 결합, 감정·뉘앙스 음성 합성. Gemini Live 업데이트로 인간 유사 발화 패턴 구현. | [[G-19]](#ref-g-19) |
| Amazon | Alexa+ (2025) 출시, 대화형 업그레이드 및 에이전틱 기능 강화. | [[G-19]](#ref-g-19) |
| Microsoft | Azure Speech: 엔터프라이즈 STT/TTS/실시간 번역. 헬스케어·생산성 도구 통합 강점. 감정 특화 기능은 Hume 대비 제한적. | [[G-19]](#ref-g-19) |
| Deepgram | 300ms 미만 실시간 STT 95%+ 정확도. 감정·의도·토픽 감지 API 제공. 2026.02 IBM watsonx Orchestrate 통합 발표. | [[G-15]](#ref-g-15), [[G-20]](#ref-g-20) |
| AssemblyAI | 사전 녹음 STT 96~98% 정확도, 감정·의도·화자 구분 우수. 문장 레벨 감정 분석 제공. | [[G-15]](#ref-g-15) |
| OpenAI | GPT-4o 실시간 음성 모달리티, $40B 조달 (Mar 2025). 오디오 팀 통합 후 2026 Q1 목표 고급 음성 모델 개발 중. | [[G-17]](#ref-g-17), [[G-13]](#ref-g-13) |
| Affectiva (Smart Eye) | MIT 미디어랩 스핀오프, 2020년 Smart Eye 인수. 얼굴+음성 멀티모달 감정 AI. 자동차·광고·의료 분야 특화. | [[G-04]](#ref-g-04) |
| ElevenLabs | $281M 조달, Fortune 500 60% 채택. 음성 생성 품질 지배적, 감정 특화 제한. | [[G-13]](#ref-g-13) |
| Cartesia | 45ms 레이턴시, 고객지원·아바타 분야 타겟. | [[G-13]](#ref-g-13) |

### 국내 플레이어

**주요 국내 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| SKT | 2025년 3월 'SKT AI CCaaS' 구독형 AICC 출시. 3개월 내 기업 고객 10+ 확보. NUGU 음성모델 기반, 음성봇·자동요약·상담품질 분석 제공. 페르소나AI(감정 특화 스타트업)에 전략 투자. AX 시리즈(SKT 자체 LLM) 연동 예정. | [[E-01]](#ref-e-01), [[G-09]](#ref-g-09) |
| KT | KT 에이센(AICC) 서비스: 음성 감정 상태 그래프 인사이트 제공, STT 자동 VOC 분류, 실시간 지식 추천. 2025년 매출 목표 3,000억 원 이상. | [[E-02]](#ref-e-02), [[G-10]](#ref-g-10) |
| Naver | CLOVA Speech X: 감정 표현 가능 음성 합성. CLOVA Note, CLOVA Care Call, CLOVA Dubbing 등 음성 AI 서비스 포트폴리오 구축. HyperCLOVA X 멀티모달 오디오+이미지 이해 지원. | [[G-18]](#ref-g-18) |
| Kakao | Kanana LLM 개발, 음성 AI 통합 방향 확인. 감정 특화 서비스 공개 정보 없음 — 추가 확인 필요. | [[G-18]](#ref-g-18) |
| 페르소나AI | SKT 전략 투자 수령. 감정 인식 특화 AICC 솔루션 개발. 구체 스펙 공개 정보 없음. | [[G-09]](#ref-g-09) |

### Gap Analysis

- **글로벌 vs 국내**: 글로벌(Hume AI, OpenAI 등)은 감정 인식을 제품의 핵심 가치 제안으로 설계하는 반면, 국내 통신사(SKT/KT)는 AICC 인프라의 부가 기능으로 통합하는 접근
- **음성 전용 vs 멀티모달**: 국내 솔루션은 음성 단독 감정 분석이 주류; 글로벌은 얼굴+음성+텍스트 멀티모달 통합이 표준화 중
- **레이턴시 경쟁**: Hume AI 1.2초 실질 레이턴시 vs Cartesia 45ms — 인프라·모델 최적화 격차 존재
- **감정 태그 세밀도**: Hume AI 600+ 태그 vs 국내 솔루션 "감정 상태 그래프" 수준 — 세밀도 격차

---

## 4. 제품/서비스 스펙 비교

**주요 제품 스펙 비교 (음성 감정 인식 중심)**

| 기업 | 응답 레이턴시 | 감정 인식 정밀도 | 가격(정책) | 출처 |
|------|------------|----------------|-----------|------|
| Hume AI EVI 3 | 실질 ~1.2s (TTS <300ms) | 600+ 태그, SOTA 수준 | $3~$500/월 (Tier), 기업 별도 | [[G-12]](#ref-g-12), [[G-13]](#ref-g-13) |
| Deepgram | STT <300ms | 감정·의도 감지 (정밀도 수치 공개 없음) | 사용량 기반, 기업 별도 | [[G-15]](#ref-g-15) |
| AssemblyAI | 사전 녹음 기준 96~98% STT | 문장 레벨 감정 분석 | 사용량 기반 | [[G-15]](#ref-g-15) |
| Cartesia | 45ms | 감정 특화 정보 없음 | 공개 정보 없음 | [[G-13]](#ref-g-13) |
| SKT AI CCaaS | 공개 정보 없음 | 음성봇+자동요약 제공 | 구독형 (가격 비공개) | [[E-01]](#ref-e-01) |
| KT 에이센 | 공개 정보 없음 | 음성 감정 그래프 (정확도 비공개) | 기업 협상 | [[E-02]](#ref-e-02) |
| Google Contact Center AI | 공개 정보 없음 | 감정+뉘앙스 음성 합성 | GCP 사용량 기반 | [[G-19]](#ref-g-19) |
| Microsoft Azure Speech | 공개 정보 없음 | 엔터프라이즈 STT/TTS | Azure 구독 기반 | [[G-19]](#ref-g-19) |

---

## 5. 학술 동향

### 최근 주요 논문 (2025)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| MemoCMT: Cross-modal transformer feature fusion (Nature Scientific Reports, 2025) | IEMOCAP UW 81.33% / W 81.85% 달성, 크로스모달 트랜스포머로 감정 인식 새 SOTA | [[P-01]](#ref-p-01) |
| Real-Time Multimodal Emotion Recognition for Edge Virtual Assistants (preprint, 2025) | 엣지 디바이스용 경량 트랜스포머, 비디오+오디오+텍스트 융합, ~81% IEMOCAP | [[P-02]](#ref-p-02) |
| Quality-Controlled Multimodal Emotion Recognition with MAMBA Fusion (arxiv, 2025) | MAMBA 기반 3-모달 융합, 74.3% IEMOCAP, 신원 기반 전이학습 적용 | [[P-03]](#ref-p-03) |
| EmoShiftNet: Shift-aware multi-task learning for emotion in multi-party conversations (Frontiers AI, 2025) | 다자 대화 감정 인식, 감정 전환 예측, F1 0.6885 on IEMOCAP | [[P-05]](#ref-p-05) |
| Advancing SER with Whisper embeddings and hand-crafted audio descriptors (ScienceDirect, 2025) | Whisper 임베딩 + 수공 오디오 피처 결합으로 경량 모델 성능 향상 | [[P-08]](#ref-p-08) |
| The Speech-LLM Takes It All: Fully End-to-End Spoken DST (arxiv, 2025) | Speech-LLM으로 SpokenWOZ SOTA 달성, 구어체 DST 완전 E2E 구현 | [[P-06]](#ref-p-06) |

### 연구 방향

- **멀티모달 융합 강화**: 음성 단독에서 음성+텍스트+비디오 3-모달 통합으로 이동
- **경량화·엣지 배포**: 클라우드 의존성 줄이고 엣지 기기(스마트폰, 자동차 등)에서 실시간 처리
- **대화형 감정 인식**: 단일 발화에서 멀티턴 대화 흐름의 감정 변화 추적으로 진화
- **LLM 통합 DST**: 파이프라인 방식 → Speech-LLM E2E 방식으로 대화 상태 추적 전환
- **문화·언어 특화**: 한국어·일본어 등 비영어권 감정 인식 모델 수요 증가

---

## 6. 특허 동향

> 참고: 이번 분석에서 intel-store MCP 특허 수집을 활용하지 못했으며, 아래 내용은 웹 검색 기반 개요이다. 정밀 특허 분석은 별도 collect_patents() 호출 필요 [C].

- **주요 출원인**: Google, Microsoft, Amazon, Nuance(Microsoft 인수), IBM, Samsung, Naver, SKT 계열사 [[G-21]](#ref-g-21)
- Google vs Microsoft vs Amazon 간 AI 특허 경쟁에서 음성·감정 인식 관련 특허가 포함된 AI 포트폴리오가 수천 건 규모 [[G-21]](#ref-g-21)
- Affectiva(Smart Eye): MIT 미디어랩 스핀오프로 감정 인식 핵심 특허 다수 보유 [[G-04]](#ref-g-04)
- 한국: SKT 페르소나AI 투자, KT AI 연구원 중심 출원 추정 — 공개 데이터 부족 [D]

---

## 7. 기업 발언 & 보도자료

**기업 발언 직접 인용**

| 기업 | 발언/보도자료 요약 | 출처 |
|------|-----------------|------|
| SKT | "AI CCaaS는 클라우드 기반 All-in-One 구독형 AICC 솔루션으로, 최첨단 AI 기술을 적용해 고객 상담 품질을 높이고 기업 운영 효율을 극대화한다." — SKT 뉴스룸 2025.03 | [[E-01]](#ref-e-01) |
| KT | "고객 음성에서 감정 상태에 대한 인사이트를 그래프로 제공, 상담사가 고객 감정 상태를 실시간으로 파악할 수 있도록 지원한다." — KT Enterprise AICC 소개 | [[E-02]](#ref-e-02) |
| Hume AI | "EVI 3 is the world's most realistic and instructible speech-to-speech foundation model." — Hume AI 공식 사이트, 2025.05 | [[E-03]](#ref-e-03) |
| Hume AI (EV4-mini) | "EV4-mini adds multilingual support across English, Japanese, Korean, Spanish, French, Portuguese, Italian, German, Russian, Hindi, and Arabic." — January 2026 발표 | [[G-12]](#ref-g-12) |
| Deepgram + IBM | "Deepgram and IBM introduce advanced voice capabilities for enterprise AI" — IBM Newsroom, 2026.02.24. IBM watsonx Orchestrate에 Deepgram STT/TTS 통합 | [[E-04]](#ref-e-04) |
| Hume AI (고객 성과) | "Vonova: 40% lower operational costs, 20% higher resolution rates after integrating EVI." — Contrary Research, 2026.01 | [[G-13]](#ref-g-13) |
| Naver CLOVA | "Speech X는 기존 음성인식 및 합성 기술보다 진화한 모델로, 언어 구조와 발음 정확도가 향상됐으며, 인간처럼 감정을 표현할 수 있다." — CLOVA 공식 소개 | [[E-05]](#ref-e-05) |

---

## 8. 규제·정책 동향

### EU AI Act — 감정 인식 규제

EU AI Act Article 5(1)(f)는 **2025년 2월 2일부터 직장 및 교육기관에서의 AI 감정 인식을 원칙적으로 금지**한다 [[G-22]](#ref-g-22).

- 금지 범위: 직장 내 웹캠·음성으로 직원 감정(분노 등) 추적, 채용 과정 중 감정 인식 AI 활용
- 예외 허용: 의료적 이유 또는 생명·건강 보호 목적에만 제한적 허용 (좁게 해석)
- 위반 시 제재: **EUR 35,000,000 또는 전 세계 연간 매출의 7% 중 더 높은 금액** [[G-22]](#ref-g-22)
- 적용 지침: 2025년 2월 4일 유럽위원회, 금지 AI 관행 실행 가이드라인 비구속적 초안 승인 [[G-23]](#ref-g-23)

> 콜센터·AICC에 대한 직접 적용: 고객 감정 분석(고객→기업 방향)은 금지 대상이 아니나, 상담원 감정 모니터링은 명백히 금지됨.

### 한국 AI기본법

- 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」: 2024년 12월 26일 국회 통과, 2025년 1월 21일 공포, **2026년 1월 22일 시행** [[G-24]](#ref-g-24)
- 시행령 입법예고: 2025년 11월 12일 ~ 12월 22일 [[G-24]](#ref-g-24)
- 음성·감정 분석 직접 금지 조항 없으나, 고위험 AI 분류 및 투명성 의무 부과 가능성
- 개인정보보호위원회: 2025년 8월 생성형 AI 개인정보 처리 안내서 발표 — 감정 데이터의 민감 정보 분류 적용 가능 [[G-25]](#ref-g-25)

### 개인정보 판례 (국내)

- 2025년 6월: 감정 분석 스타트업이 카카오톡 대화 데이터를 AI 학습에 무단 사용, **개인정보보호법 위반 판결** (1심) — 위자료 지급 명령 [[G-25]](#ref-g-25)
- 시사점: 음성·감정 데이터의 동의 없는 AI 학습 활용 시 법적 리스크

### ISO/IEC 표준

- ISO/IEC JTC 1/SC 42 (AI 표준화): 감정 AI 관련 표준 논의 중 [C]
- 구체 표준 번호 및 발효 시기 공개 정보 없음 — 추가 확인 필요 [D]

---

## 9. 전략적 시사점

### 기회

- **AICC 고성장 시장**: 국내 AICC CAGR 23.7%, 통신사 기존 고객 기반과 음성 감정 분석 결합 시 즉각적 SAM 공략 가능
- **한국어 특화 우위**: 글로벌 플레이어의 한국어 모델 완성도 한계 (Hume EV4-mini Jan 2026 한국어 추가 = 비교적 최근) → 한국어 특화 감정 모델 차별화 가능
- **B2B 엔터프라이즈 진입**: AICC에서 확인된 실적(KT 3000억 목표, SKT CCaaS 10+ 기업 채택) → 레퍼런스 기반 확장
- **멀티모달 확장**: 음성 단독 → 텍스트+음성+영상 통합 감정 분석으로 정확도·활용도 향상

### 위협

- **EU AI Act 규제 확산**: 직장 내 감정 인식 금지가 글로벌 기업 대상 솔루션 확장 제약 (국내는 현재 명시 금지 없으나 입법 방향 모니터링 필요)
- **Big Tech 통합 위협**: Google CCAI, Microsoft Azure, Amazon Connect 등이 감정 분석을 플랫폼에 통합 시 스탠드얼론 솔루션 경쟁력 약화
- **레이턴시 경쟁 심화**: Cartesia 45ms vs 현재 국내 솔루션 — 기술 격차 확대 위험
- **개인정보 리스크**: 국내 법원 판결(2025.06) 및 개인정보보호위원회 지침 강화로 음성 감정 데이터 수집·활용 동의 체계 강화 의무화
- **OpenAI 음성 모델**: 오디오 팀 통합 및 2026 고급 음성 모델 출시 계획 → 시장 게임체인저 가능성

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- EU AI Act Article 5(1)(f) 내용 및 시행일 (2025.02.02) [A]
- IEMOCAP 벤치마크 수치 (논문 기반) [A]
- Hume AI 펀딩·제품 출시 일정 [B]
- Conversational AI 시장 규모 추정 (복수 기관 교차 확인) [B]
- SKT/KT AICC 서비스 출시·매출 목표 [B]

**추가 검증 필요 [C/D]:**
- 음성 전용 감정 인식 세부 시장 규모 (기관 간 편차 10배 이상) [C]
- 국내 AICC 감정 인식 정확도 수치 (공개 정보 없음) [D]
- ISO/IEC 감정 AI 표준 진행 상황 [D]
- 특허 출원 통계 (세부 분석 미완) [C]
- Kakao 음성 감정 분석 제품 현황 [D]

**데이터 공백:**
- intel-store MCP 특허/논문 수집 미활용 (도구 접근 불가) → WebSearch 대체
- 국내 솔루션 실제 감정 인식 정확도 공개 수치 없음
- 한국 AI기본법 시행령 최종본 (2026.01.22 시행이나 시행령 세부 내용 미확정)
- ISO/IEC SC 42 감정 AI 표준 구체 일정

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Grand View Research — Emotion Detection & Recognition Market ($136.46B by 2030, CAGR 16%) | [링크](https://www.grandviewresearch.com/press-release/global-emotion-detection-recognition-market) | market-report | 2024 | [B] |
| <a id="ref-g-02"></a>G-02 | MarketsandMarkets — Emotion Detection and Recognition Market worth $42.9B by 2027 | [링크](https://www.marketsandmarkets.com/PressReleases/emotion-detection-recognition.asp) | market-report | 2023 | [B] |
| <a id="ref-g-03"></a>G-03 | Fortune Business Insights — Emotion Detection and Recognition Market Size & Growth [2032] | [링크](https://www.fortunebusinessinsights.com/industry-reports/emotion-detection-and-recognition-market-101326) | market-report | 2024 | [B] |
| <a id="ref-g-04"></a>G-04 | Emergen Research — Top 10 Companies in Emotion AI Market 2025 (Affectiva, Beyond Verbal 포함) | [링크](https://www.emergenresearch.com/blog/top-10-companies-in-global-emotion-ai-market) | news | 2025 | [B] |
| <a id="ref-g-05"></a>G-05 | Grand View Research — Conversational AI Market ($41.39B by 2030, CAGR 23.7%) | [링크](https://www.prnewswire.com/news-releases/conversational-ai-market-to-be-worth-41-39-billion-by-2030-at-cagr-23-7---grand-view-research-inc-302452404.html) | market-report | 2025 | [B] |
| <a id="ref-g-06"></a>G-06 | MarketsandMarkets — Conversational AI Market worth $49.80B by 2031 (CAGR 19.6%) | [링크](https://www.marketsandmarkets.com/PressReleases/conversational-ai.asp) | market-report | 2024 | [B] |
| <a id="ref-g-07"></a>G-07 | NextMSC — Voice Assistant Market Size 2024 ($7.35B) → 2030 ($33.74B), CAGR 26.5% | [링크](https://www.nextmsc.com/report/voice-assistant-market) | market-report | 2025 | [B] |
| <a id="ref-g-08"></a>G-08 | Goover AI — AI 콜센터의 미래: 한국 통신사 AICC 도입 현황 (국내 CAGR 23.7%) | [링크](https://seo.goover.ai/report/202503/go-public-report-ko-fd857d32-0e7b-49b1-8787-ff28fd4b3fe0-0-0.html) | news | 2025-03 | [C] |
| <a id="ref-g-09"></a>G-09 | News2Day — SKT·KT·LG유플러스, 5000억원대 AICC시장 공략 | [링크](https://www.news2day.co.kr/article/20230823500193) | news | 2023-08-23 | [B] |
| <a id="ref-g-10"></a>G-10 | GoodKyung — 통신 3사 AICC 공격적 확장, KT 3000억 목표 | [링크](https://www.goodkyung.com/news/articleView.html?idxno=265681) | news | 2024 | [B] |
| <a id="ref-g-11"></a>G-11 | Retell AI — Sub-second latency voice assistants benchmarks (P95 Final ≤ 800ms) | [링크](https://www.retellai.com/resources/sub-second-latency-voice-assistants-benchmarks) | blog | 2025 | [C] |
| <a id="ref-g-12"></a>G-12 | eesel.ai — What is Hume AI? EVI 3 (May 2025), EV4-mini (Jan 2026) 11개 언어 | [링크](https://www.eesel.ai/blog/hume-ai) | blog | 2026-01 | [C] |
| <a id="ref-g-13"></a>G-13 | Contrary Research — Hume AI Business Breakdown ($72.8M 조달, 100K 개발자, Cartesia 45ms) | [링크](https://research.contrary.com/company/hume-ai) | analyst-report | 2026-01 | [B] |
| <a id="ref-g-14"></a>G-14 | gnani.ai — Real-Time Barge-In AI for Voice Conversations (VAD 10-20ms 처리) | [링크](https://www.gnani.ai/resources/blogs/real-time-barge-in-ai-for-voice-conversations-31347) | blog | 2025 | [C] |
| <a id="ref-g-15"></a>G-15 | Deepgram — Best Voice AI Platforms: Enterprise Comparison 2026 (Deepgram vs AssemblyAI) | [링크](https://deepgram.com/learn/best-voice-ai-platforms-enterprise-comparison) | blog | 2026 | [C] |
| <a id="ref-g-16"></a>G-16 | MarkTechPost — The State of Voice AI in 2025: Trends, Breakthroughs, and Market Leaders | [링크](https://www.marktechpost.com/2025/08/29/the-state-of-voice-ai-in-2025-trends-breakthroughs-and-market-leaders/) | news | 2025-08-29 | [B] |
| <a id="ref-g-17"></a>G-17 | i10x.ai — OpenAI Merges Audio Teams for 2026 Voice AI Breakthrough | [링크](https://i10x.ai/news/openai-audio-teams-merger-conversational-ai-2026) | news | 2025 | [C] |
| <a id="ref-g-18"></a>G-18 | Korea Herald — Korea's AI challengers take on ChatGPT (Naver, Kakao, SKT AX 시리즈) | [링크](https://www.koreaherald.com/article/10566046) | news | 2025 | [B] |
| <a id="ref-g-19"></a>G-19 | Business Standard — Year ender 2025: AI assistants from reactive to proactive (Google, Amazon, Microsoft) | [링크](https://www.business-standard.com/technology/tech-news/year-ender-2025-ai-assistants-rise-alexa-siri-google-assistant-chatgpt-meta-gemini-125122200324_1.html) | news | 2025-12-22 | [B] |
| <a id="ref-g-20"></a>G-20 | IBM Newsroom — Deepgram and IBM introduce advanced voice capabilities for enterprise AI (Feb 2026) | [링크](https://newsroom.ibm.com/2026-02-24-deepgram-and-ibm-introduce-advanced-voice-capabilities-for-enterprise-ai) | press-release | 2026-02-24 | [A] |
| <a id="ref-g-21"></a>G-21 | PatentPC — AI Patent Showdown: Google vs. Microsoft vs. Amazon | [링크](https://patentpc.com/blog/ai-patent-showdown-google-vs-microsoft-vs-amazon-who-holds-the-most) | blog | 2025 | [C] |
| <a id="ref-g-22"></a>G-22 | Wolters Kluwer — Prohibition of AI Emotion Recognition Technologies in the Workplace under the AI Act | [링크](https://legalblogs.wolterskluwer.com/global-workplace-law-and-policy/the-prohibition-of-ai-emotion-recognition-technologies-in-the-workplace-under-the-ai-act/) | legal-blog | 2025-02 | [A] |
| <a id="ref-g-23"></a>G-23 | Inside Privacy — EU Commission Guidelines on Prohibited AI Practices (Feb 4, 2025) | [링크](https://www.insideprivacy.com/artificial-intelligence/european-commission-guidelines-on-prohibited-ai-practices-under-the-eu-artificial-intelligence-act/) | legal-news | 2025-02 | [A] |
| <a id="ref-g-24"></a>G-24 | 법제처 — 인공지능기본법 시행령 입법예고 (2026.01.22 시행) | [링크](https://www.moleg.go.kr/lawinfo/makingInfo.mo?lawSeq=84360&lawCd=0&lawType=TYPE5&mid=a10104010000) | official | 2025-11 | [A] |
| <a id="ref-g-25"></a>G-25 | Kim & Chang — 생성형 AI 개인정보 처리 안내서 (개인정보보호위원회 2025.08) | [링크](https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=32696) | legal-news | 2025-08 | [A] |
| <a id="ref-g-26"></a>G-26 | ElevenLabs — Voice agents and Conversational AI: 2026 developer trends | [링크](https://elevenlabs.io/blog/voice-agents-and-conversational-ai-new-developer-trends-2025) | blog | 2025 | [C] |
| <a id="ref-g-27"></a>G-27 | Twilio — Core Latency in AI Voice Agents (guide) | [링크](https://www.twilio.com/en-us/blog/developers/best-practices/guide-core-latency-ai-voice-agents) | blog | 2025 | [C] |
| <a id="ref-g-28"></a>G-28 | Softcery — Real-Time vs Turn-Based Voice Agent Architecture | [링크](https://softcery.com/lab/ai-voice-agents-real-time-vs-turn-based-tts-stt-architecture) | blog | 2025 | [C] |
| <a id="ref-g-29"></a>G-29 | SparkCo — Optimizing Voice Agent Barge-in Detection for 2025 | [링크](https://sparkco.ai/blog/optimizing-voice-agent-barge-in-detection-for-2025) | blog | 2025 | [C] |
| <a id="ref-g-30"></a>G-30 | Nextiva — 50+ Conversational AI Statistics for 2026 | [링크](https://www.nextiva.com/blog/conversational-ai-statistics.html) | blog | 2025 | [C] |
| <a id="ref-p-01"></a>P-01 | MemoCMT: Multimodal emotion recognition using cross-modal transformer-based feature fusion (Nature Scientific Reports, 2025) | [링크](https://www.nature.com/articles/s41598-025-89202-x) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | Real-Time Multimodal Emotion Recognition for Edge Virtual Assistants (preprint, 2025) | [링크](https://d197for5662m48.cloudfront.net/documents/publicationstatus/269419/preprint_pdf/8f4b35802cf04ae43871f04f0159883a.pdf) | paper | 2025 | [B] |
| <a id="ref-p-03"></a>P-03 | Quality-Controlled Multimodal Emotion Recognition with Identity-Based Transfer Learning and MAMBA Fusion (arxiv 2511.14969) | [링크](https://arxiv.org/html/2511.14969) | paper | 2025-11 | [A] |
| <a id="ref-p-04"></a>P-04 | Multimodal conversational emotion recognition based on hierarchical Transformer (Francis Academic Press, 2025) | [링크](https://francis-press.com/papers/18162) | paper | 2025 | [B] |
| <a id="ref-p-05"></a>P-05 | EmoShiftNet: Shift-aware multi-task learning for emotion recognition in multi-party conversations (Frontiers AI, 2025) | [링크](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1618698/full) | paper | 2025 | [A] |
| <a id="ref-p-06"></a>P-06 | The Speech-LLM Takes It All: A Truly Fully End-to-End Spoken Dialog State Tracking Approach (arxiv 2510.09424) | [링크](https://arxiv.org/abs/2510.09424) | paper | 2025-10 | [A] |
| <a id="ref-p-07"></a>P-07 | Towards LLM-driven Dialogue State Tracking (EMNLP 2023 / LDST framework) | [링크](https://aclanthology.org/2023.emnlp-main.48.pdf) | paper | 2023 | [A] |
| <a id="ref-p-08"></a>P-08 | Advancing SER with Whisper model embeddings and hand-crafted audio descriptors (ScienceDirect, 2025) | [링크](https://www.sciencedirect.com/science/article/pii/S2773186325001914) | paper | 2025 | [A] |
| <a id="ref-e-01"></a>E-01 | SK텔레콤 — AI로 고객 상담 효율, 고객 만족도 높이는 'SKT AI CCaaS' | [링크](https://news.sktelecom.com/208852) | press-release | 2025-03 | [A] |
| <a id="ref-e-02"></a>E-02 | KT Enterprise — 사람처럼 대화하는 인공지능 기반 컨택센터, KT AICC | [링크](https://enterprise.kt.com/bt/dxstory/1057.do) | official | 2024 | [A] |
| <a id="ref-e-03"></a>E-03 | Hume AI — 공식 사이트 (EVI 3, Octave 2 소개) | [링크](https://www.hume.ai/) | official | 2025-05 | [A] |
| <a id="ref-e-04"></a>E-04 | IBM Newsroom — Deepgram and IBM Introduce Advanced Voice Capabilities for Enterprise AI | [링크](https://newsroom.ibm.com/2026-02-24-deepgram-and-ibm-introduce-advanced-voice-capabilities-for-enterprise-ai) | press-release | 2026-02-24 | [A] |
| <a id="ref-e-05"></a>E-05 | NAVER CLOVA — NAVER AI Product: Speech X, CLOVA Note, CLOVA Dubbing | [링크](https://clova.ai/en/naver-ai-product) | official | 2025 | [A] |
| <a id="ref-e-06"></a>E-06 | SKT 뉴스룸 — SKT, 국내 AICC 선도기업 '페르소나AI'에 투자 | [링크](https://news.sktelecom.com/197640) | press-release | 2023 | [A] |
