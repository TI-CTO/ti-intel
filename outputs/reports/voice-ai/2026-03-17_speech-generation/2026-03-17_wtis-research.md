---
type: wtis-research
topic: Speech Generation
domain: voice-ai
l2_topic: speech-generation
l2_number: 8
date: 2026-03-17
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, prior-research-voice-synthesis-w12, prior-research-voice-cloning-w12]
---

# WTIS Research: Speech Generation (L2 #8)

> **분석 목적**: Voice Synthesis + Voice Cloning 통합 Go/No-Go 검증을 위한 데이터 수집 (SKILL-1 200점 채점 전달용)
> **선행 리서치**: Voice Synthesis W12 (25건 Ref) + Voice Cloning W12 (22건 Ref) 활용, 중복 수집 배제
> **추가 수집 초점**: 시장 규모(TAM/SAM), 경쟁사 비교, 규제/표준, 통신사 전략, 기술 성숙도 벤치마크

---

## 1. 시장 분석

### TAM/SAM 수치 (다중 소스 교차 검증)

**TTS 시장 전망 (복수 기관 교차 검증)**

| 기관 | 2024~2025 기준값 | 2029~2035 예측 | CAGR | 신뢰도 |
|------|-----------------|----------------|------|--------|
| MarketsandMarkets | $3.87B (2025) | $7.28B (2030) | 12.89% | [B] |
| GlobeNewswire/다수 | ~$4.0B (2024) | $9.3B (2030) | 13.4% | [B] |
| ExpertMarketResearch | $4.25B (2025) | $34.52B (2035) | 23.30% | [C] |
| Business Research Insights | $3.65B (2025) | $11.1B (2034) | 12.3% | [C] |
| MarketsAndMarkets (AI Voice Generator) | $4.16B (2025) | $20.71B (2031) | 30.7% | [C] |

**복수 소스 교차 확인된 수치**: 2025년 기준 TTS 시장 $3.65~4.25B 범위, 2029~2030년 $7.3~9.3B 범위, CAGR 12~14%가 보수적 추정 기준으로 신뢰도 높음 [G-26] [G-27] [G-28]

**Voice Cloning 세그먼트**

Voice Cloning 단독 시장: 2026년 추정 $1.1~4.1B (기관별 방법론 차이), 2029년 $7.75B (KT 클라우드 조사 기준), CAGR 23~26%. 아시아태평양 CAGR 28.1%로 글로벌 평균 초과 성장, 한국·일본·인도가 주요 성장 거점 [N-01]

**Voice AI Agent 세그먼트 (고성장 세그먼트)**

Voice AI Agents 시장 CAGR 34.8%, 헬스케어 Voice AI CAGR 37.3%로 전체 TTS 시장 성장을 상회 [G-29]

### 세그먼트별 시장 규모 및 성장 드라이버

**산업 수직 비중 (TTS 기준)**:
- BFSI (금융·보험): 32.9% — AICC·금융 상담 봇 수요 주도
- 헬스케어: 차세대 고성장 — 접근성·의료 정보 전달
- 미디어/엔터: 가장 큰 절대 규모 — 오디오북·더빙·광고
- 통신/리테일: 상담 자동화·IVR 혁신 [G-29]

**SKT의 시장 전망**: "5년 뒤 10조 원 규모(약 $7.6B)" TTS 시장 진입 준비로 A.X TTS 브랜드화 및 SK 오픈API 외부 공개 추진 [E-01]

---

## 2. 기술 현황 및 성숙도

### TRL 판단 근거

**TRL 8~9 (상용 배포 단계)**

- ElevenLabs, Google, OpenAI, Microsoft, Amazon이 프로덕션 API 제공 중 — 대규모 실서비스 운영 확인
- ElevenLabs: Anthropic Claude Code OEM 채택(2026-03), 800+ B2B 파트너 [G-06-S] [G-07-S]
- Cartesia Sonic 3: AWS SageMaker JumpStart 마켓플레이스 통합(2026-02) — 엔터프라이즈 채널 확보 [G-11-S]
- Deutsche Telekom Magenta AI Call Assistant: 망 통합 실서비스 MWC 2026 시연 → 2026년 하반기 독일 고객 배포 예정 [E-03]
- SKT A.X TTS: SK 오픈API 통해 외부 개방, TMAP·NUGU 자사 서비스 배포 완료 [E-01]

**Zero-shot 및 Few-shot 화자 적응 — TRL 7~8**

- 15초 레퍼런스 오디오로 화자 복제 기술 상용화 (Cartesia Sonic 3, ElevenLabs) [G-12-S]
- Instant Custom Voice 30개+ 로케일 지원 (Google Chirp 3) [G-11-C]
- Azure Personal Voice v2.1 GA 배포(2025-07) [G-15-C]

### 주요 기술 벤치마크 (MOS, WER, Latency)

**MOS (Mean Opinion Score)**

| 제공사 | MOS / ELO | 비교 기준 | 출처 |
|--------|-----------|----------|------|
| Inworld TTS-1.5-Max | ELO 1,160 (1위) | Artificial Analysis Speech Arena | [G-13-S] |
| MiniMax Speech 2.6 HD | ELO 1,156 (2위) | Artificial Analysis | [G-31] |
| ElevenLabs Multilingual v2 | ELO 1,108 / MOS 4.14 | Artificial Analysis | [G-13-S] [G-30] |
| Naver HyperCLOVA X Omni | MOS 4.22 (한국어) | 내부 벤치마크 | [G-W11] |
| Smallest.ai | MOS 4.14 | 자체 vs ElevenLabs | [G-30] |
| OpenAI TTS-1 | ELO 1,111 | Artificial Analysis | [G-13-S] |

**WER (Word Error Rate)**

| 제공사 | WER | 측정 데이터셋 | 출처 |
|--------|-----|-------------|------|
| Qwen3-TTS (Alibaba) | 1.835% (평균, 10언어) | 자체 | [G-31] |
| ElevenLabs | 2.83% | Voice Cloning 테스트 | [G-31] |
| OpenAI gpt-4o-mini-tts | ~35% 개선 (YoY) | Common Voice, FLEURS | [G-04-S] |

**Latency (TTFB, Time-to-First-Byte)**

| 제공사 | TTFB | 비고 | 출처 |
|--------|------|------|------|
| Cartesia Sonic Turbo | 40ms | SSM 아키텍처 | [G-12-S] |
| Cartesia Sonic 3 | 90ms | 표준 | [G-12-S] |
| Qwen3-TTS | 97ms | — | [G-31] |
| ElevenLabs Flash v2.5 | ~75ms | — | [G-12-S] |
| CosyVoice 2 | 150ms | 스트리밍 | [P-04-S] |
| Inworld TTS-1-Max | <250ms (P90) | 실시간 에이전트 | [G-13-S] |
| Supertone Shift | 47ms | 실시간 음성 변환 | [G-32] |

**참고 기준**: 음성 에이전트에서 800ms 이상이면 사용자가 지연 인지 — 상위 모든 제공사가 요건 충족

### 오픈소스 vs 상용 비교

**오픈소스 경량 모델 (TRL 6~7)**

| 모델 | 파라미터 | VRAM | 언어 | 라이선스 |
|------|---------|------|------|---------|
| Kyutai Pocket TTS | 100M | CPU 동작 | 다국어 | MIT |
| Kokoro | 82M | — | 영어 중심 | Apache |
| CosyVoice 2-0.5B | 500M | — | 다국어 | Apache |
| Kani-TTS-2 | 400M | 3GB | 다국어 | OSS |
| Supertonic (Supertone) | — | ONNX 온디바이스 | 다국어 | — |

오픈소스 경량 모델의 품질이 상용 수준에 급격히 근접 — 온프레미스 배포 선호 엔터프라이즈 고객의 API 종속 탈피 가속화 우려 [G-11-S] [G-23-S]

---

## 3. 경쟁 환경

### 플레이어별 포지셔닝

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | SXSW '1M Voices' ($1B 현물) + Iconic Marketplace(28개 유명인 라이선스) + ElevenCreative 멀티모달 런칭. Claude Code TTS 채택으로 de facto B2B 표준 지위 강화. $500M Series D, $11B 밸류에이션. | [[G-09-S]](#ref-g-09-s) [[G-03-C]](#ref-g-03-c) [[E-02]](#ref-e-02) |
| Google | Gemini 2.5 TTS 멀티스피커 + 24언어 + Speech-to-Speech 번역 70언어·2,000쌍. Chirp 3 Instant Custom Voice EU/미국 리전 확대(30개+ 로케일). Hume AI 핵심팀 DeepMind 흡수로 감성 음성 AI 역량 내부화. | [[G-01-S]](#ref-g-01-s) [[G-11-C]](#ref-g-11-c) [[G-13-C]](#ref-g-13-c) |
| Microsoft Azure | Personal Voice v2.1 GA(2025-07), 표현력 강화. Azure AI Speech 440+ 음성 140+ 언어. Custom Neural Voice(CNV) 동의 기반 엄격 관리. OpenAI gpt-4o-mini-tts Azure AI Foundry 통합. | [[G-15-C]](#ref-g-15-c) [[G-15-S]](#ref-g-15-s) |
| OpenAI | gpt-4o-mini-tts WER 35% 감소. Custom Voice(Voice Engine)는 2년째 일반 배포 지연 — 안전성 검토 지속. 파트너 기업에게만 제한 접근. | [[G-04-S]](#ref-g-04-s) [[G-09-C]](#ref-g-09-c) |
| Amazon (AWS) | Polly Neural TTS $19.20/1M chars 유지. SageMaker JumpStart에 Cartesia Sonic 3 통합(파트너 전략). Voice AI 직접 혁신보다 마켓플레이스 생태계 확장 전략. | [[G-11-S]](#ref-g-11-s) [[G-33]](#ref-g-33) |
| Cartesia | Sonic 3 TTFB 40ms(Turbo)/90ms(표준). SSM 아키텍처로 저지연 차별화. AWS SageMaker 통합으로 엔터프라이즈 진입. | [[G-11-S]](#ref-g-11-s) [[G-12-S]](#ref-g-12-s) |
| Naver (CLOVA) | CLOVA Voice API — 한국어 전문 TTS, ClovaNote·CareCall·ClovaDubbing 서비스군. HyperCLOVA X Omni 한국어 MOS 4.22. 멀티모달 확장 중. | [[G-34]](#ref-g-34) |
| SKT (A.X TTS) | A.X TTS 브랜드화 + SK 오픈API 외부 공개. 30개+ 한국어 음성, GPU 기반 실시간 응답. TMAP·NUGU 배포 기반. AICC 신사업 축으로 TTS 전략화. "5년 뒤 TTS 10조 시장" 진입 목표 발표. | [[E-01]](#ref-e-01) |
| KT (Genie Voice) | KT Cloud 통해 Genie Voice(TTS)·Genie Dictation(STT)·Genie Custom Voice API 제공. AICC '에이센' 서비스 — B2B 3000억 매출 목표(2025). MWC 2026에서 'KT 에이전틱 AICC' 공개. | [[E-04]](#ref-e-04) [[E-05]](#ref-e-05) |
| Supertone (HYBE) | HYBE 자회사. Supertonic — ONNX 온디바이스 TTS, 47ms 초저지연. 200개+ 음성, 한국어 특화. K-Pop 엔터·방송 시장 집중. | [[G-32]](#ref-g-32) |
| Deutsche Telekom | Magenta AI Call Assistant — ElevenLabs + Radisys 파트너십으로 망 내장형 AI 전화 어시스턴트. MWC 2026 세계 초연. 2026 하반기 독일 서비스 개시, 12개월 내 50개 언어 확장 계획. | [[E-03]](#ref-e-03) |

### Gap Analysis (통신사 관점)

| 역량 | Big Tech | ElevenLabs 등 스타트업 | 통신사 (SKT/KT) | Gap 판단 |
|------|---------|----------------------|----------------|---------|
| 기반 모델 품질 | 최상 (Google MOS/ELO 상위) | 상 (ElevenLabs 산업 표준) | 중 (한국어 특화 우세) | 한국어 외 다국어 열위 |
| 저지연 음성 에이전트 | 상 (Google 40~75ms) | 최상 (Cartesia 40ms) | 중하 (공개 정보 없음) | 실시간 에이전트 열위 |
| Voice Cloning | 중 (OpenAI 제한 배포) | 최상 (ElevenLabs de facto) | 중하 (KT Custom Voice) | 즉시 클로닝 부재 |
| 통신망 통합 | 하 (플랫폼 외부화 어려움) | 중 (Deutsche Telekom 사례) | 최상 (망 인프라 보유) | 차별화 기회 |
| 규제 대응 (동의/라벨링) | 상 (Google 오디오 무보존) | 중 (ElevenLabs 동의 모델) | 중 (수신 동의 관리 가능) | 통신사 우위 가능 |

### 기업 발언 직접 인용 (E-xx)

**[E-01] SKT — A.X TTS 전략 발표 (서울경제, 2025)**
> "SK텔레콤은 5년 후 10조 원 규모로 성장할 것으로 예상되는 음성합성(TTS) 시장 공략을 위해 TTS 사업을 자체 개발한 LLM '에이닷스(A.X)'로 묶어 브랜드화하고 외연 확장에 나선다. 특히 'AICC(AI 컨택센터)' 등에서 활용할 수 있는 핵심 기술로서 TTS에 주목하고 있다." [E-01]

**[E-02] ElevenLabs — 1 Million Voices 이니셔티브 발표 (PR Newswire, 2026-03-11)**
> "With 1 Million Voices, we're not just giving people their voices back. We're redefining what it means for AI to serve humanity at scale." — ElevenLabs CEO Mati Staniszewski [G-09-S]

**[E-03] Deutsche Telekom — Magenta AI Call Assistant 공개 발언 (MWC 2026, 2026-03-02)**
> "We are embedding AI directly into our network, not as an app or a device feature, but as part of the infrastructure itself. The Magenta AI Call Assistant marks the beginning of a new era for telecoms — one where AI is as fundamental as the call itself." — Deutsche Telekom [E-03]

**[E-04] KT — MWC 2026 에이전틱 AICC 발표**
> KT가 MWC 2026(바르셀로나, 2026-03-02~05)에서 차세대 AI 콘택트 센터 솔루션 'KT 에이전틱 AICC'를 공개하며 음성합성 기반 B2B 서비스의 도약을 선언 [E-04]

**[E-05] SKT — AX혁신 전략 (2026)**
> "1인 1 AI에이전트 시대로 전환하겠다. 비개발직군을 포함 모든 구성원이 본인 업무에 특화된 AI를 만드는 플랫폼을 제공한다." — SKT AX전략 발표 [G-35]

---

## 4. 규제 및 표준

### EU AI Act Article 50 — 합성 음성 라벨링 의무

**핵심 요건** [G-36] [G-37]:
- 2026-08-02 발효 (법적 구속력 발생)
- AI 생성 합성 음성 출력물에 대해 기계 판독 가능한 형식으로 마킹 의무
- 딥페이크 오디오는 청각적(가청) 고지(audible disclaimer) 명시 의무
- 기술적 구현: 워터마킹, 메타데이터 태깅, C2PA 프로토콜 등

**Code of Practice 타임라인**:
- 2025-12-17: 유럽집행위원회 초안 Code of Practice 발표
- 2026-03: 2차 초안 예상
- 2026-06: 최종 Code 확정 예정
- 2026-08-02: Article 50 발효

**컴플라이언스 요건** [G-37]:
- 기술 솔루션은 상호운용성(interoperable), 견고성(robust), 신뢰성(reliable) 요건 충족 필요
- 예외: 순수 예술 작품으로 라벨링이 미적 경험을 훼손하는 경우

### 국내 AI 기본법 (한국) — 음성 합성 관련

**핵심 조항** [G-38] [G-39]:
- 법률: 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」 (2025-01 제정, 2026-01 시행)
- **Article 31**: AI 생성 합성 음성·영상이 현실과 구분 불가 시 AI 생성 명시 의무
- 한국 방통위: AI 생성 콘텐츠(음성·영상·텍스트) 표시 의무, 위반 시 과태료 최대 3000만 원
- 광고 분야: 2026년 1분기부터 AI 생성 광고 콘텐츠에 비례적 표시 의무 강화

**국내 규제 시사점**:
- 통신사(SKT/KT)는 AICC·음성봇 서비스에서 AI 음성 고지 의무 준수 필요
- 에이닷 전화, Genie AI 보이스봇 → 수신자에게 AI 음성 사용 고지 체계 필요

### 미국 규제 동향

- 뉴욕주: 합성 퍼포머 공시 의무 2026-06 시행
- OpenAI: Voice Engine 일반 배포 2년 지연 — 안전성 심사 기준이 사실상 업계 표준화 [G-09-C]
- YouTube: 2026-03-10 딥페이크 탐지 범위 확대(정치인·언론인·정부 관료) → 플랫폼 레벨 음성 진위 검증 인프라 확산 [G-16-C]

### 업계 자율 규제 표준

- C2PA (Content Provenance and Authenticity) — 디지털 콘텐츠 출처 표준, 음성 AI에 적용 확산
- ElevenLabs: Iconic Marketplace에 동의(consent-only) 원칙 적용 — 산업 자율 기준 선도
- Google: Chirp 3 Custom Voice — 오디오 무보존(zero audio retention) 정책 채택 [G-11-C]

---

## 5. 통신사 전략 분석

### SKT 현황

**A.X TTS 전략 (2025~2026)** [E-01]:
- 자체 개발 TTS 엔진 'A.X TTS' — 대량 고품질 음성 데이터 + 딥러닝
- 30개+ 한국어 음성 제공, GPU 기반 실시간 응답
- 현재 TMAP·NUGU 자사 서비스 배포 완료
- SK 오픈API를 통해 외부 B2B 생태계 확장 개시
- 목표 시장: AICC(AI 컨택센터), 에이닷 에이전트 서비스

**에이닷 서비스 맥락** [G-35]:
- 에이닷(A.dot) MAU ~810만 명 (2025년 말 기준)
- A.X K1 — 500B 파라미터 한국어 특화 LLM (2025-12 공개)
- 에이닷 오토(차량용), 에이닷 비즈(기업용) 등 에이전트 플랫폼 확장
- 1인 1 AI에이전트 전략 = 음성 에이전트 기반이 핵심 인프라로 작동

**평가**: SKT의 A.X TTS는 한국어 특화 자체 모델 보유 확인, AICC 신사업 축으로 전략화. 다만 Voice Cloning, Zero-shot 화자 적응, 다국어 지원 관련 공개 정보 미확인.

### KT 현황

**Genie Voice & AICC 전략** [E-04] [E-05]:
- KT Cloud: Genie Voice(TTS), Genie Dictation(STT), Genie Custom Voice 3종 API 제공
- Genie Custom Voice: 기업 특화 음성 B2B 서비스 (REST API + HTTP 2.0)
- AICC '에이센(A'Cen)': 구독형 AI 컨택센터 — 금융·통신 B2B 3000억 매출 목표(2025)
- MWC 2026: 'KT 에이전틱 AICC' 공개 — 에이전트 기반 차세대 컨택센터 전략

**평가**: KT는 B2B AICC를 명확한 수익화 채널로 설정, Genie Voice가 음성합성 핵심 엔진 역할. 독자 보이스 클로닝 기술 수준 및 멀티모달 확장 계획 공개 정보 부족.

### 글로벌 통신사 — Deutsche Telekom (벤치마크)

**Magenta AI Call Assistant (MWC 2026 세계 초연)** [E-03]:
- ElevenLabs(TTS/음성) + Radisys(통신망 통합) 파트너십
- 앱 설치 없이 통신망 내장형 AI 음성 어시스턴트 구현
- 실시간 번역: 50개 언어, 저지연
- "Hey Magenta" 활성화 — 비활성 시 통화 내용 미저장, 옵트인 동의 방식
- 2026 하반기 독일 서비스 개시 → 12개월 내 50개 언어로 확장

**전략적 의의**: 통신사가 자체 TTS 개발 대신 스타트업(ElevenLabs) 파트너십으로 "망 내장형 AI 음성 서비스"를 구현한 최초 대형 사례. SKT/KT의 벤치마크 모델.

### 글로벌 통신사 비교

| 통신사 | Voice AI 전략 | 파트너십 | 출처 |
|--------|-------------|---------|------|
| Deutsche Telekom | 망 내장형 AI Call Assistant, 실시간 번역 50언어 | ElevenLabs + Radisys | [[E-03]](#ref-e-03) |
| SKT | A.X TTS 자체 개발 + SK 오픈API 외부 공개, AICC 신사업화 | 자체 (일부 파트너십 미확인) | [[E-01]](#ref-e-01) |
| KT | Genie Voice/Custom Voice API + 에이전틱 AICC(MWC 2026) | 자체 KT Cloud 기반 | [[E-04]](#ref-e-04) |
| AT&T / Verizon | 공개 Voice AI TTS 전략 정보 없음 | 공개 정보 없음 | — |
| NTT | 공개 Voice AI TTS 전략 정보 없음 | 공개 정보 없음 | — |

**통신사의 Voice AI 구조적 기회**:
1. 망 인프라를 활용한 네트워크 내장형 Voice AI (Deutsche Telekom 사례)
2. AICC(AI 컨택센터) B2B 수익화 — 한국 통신 3사 공통 전략 축
3. 고객 동의 데이터 관리 역량 → 규제 환경에서 경쟁 우위
4. 통화 데이터 기반 화자 적응 모델 학습 가능성 (규제 준수 조건)

**통신사의 Voice AI 위협**:
1. Big Tech의 실시간 번역·멀티스피커 TTS가 통신 서비스 레이어까지 확장
2. ElevenLabs 등 스타트업이 통신사보다 빠른 제품 혁신 및 생태계 확장
3. 오픈소스 경량 TTS의 성숙으로 통신사 자체 API의 차별성 약화

---

## 6. 제품/서비스 스펙 비교

**주요 상용 TTS/Voice Cloning API 스펙**

| 기업 | 지표① (지연/성능) | 지표② (Voice Cloning 요건) | 가격(정책) | 출처 |
|------|-----------------|--------------------------|-----------|------|
| ElevenLabs | TTFB ~75ms, MOS 4.14, ELO 1,108 | 15초 클로닝, 70언어, Instant/Professional 2단계 | $5/월(Starter, 30K크레딧), $11/월(Creator, 100K크레딧) | [[G-13-S]](#ref-g-13-s) [[G-30]](#ref-g-30) |
| Cartesia Sonic 3 | TTFB 40ms(Turbo)/90ms, SSM 아키텍처 | 15초 클로닝, 42언어 | 기업 문의 (SageMaker JumpStart 통합) | [[G-11-S]](#ref-g-11-s) [[G-12-S]](#ref-g-12-s) |
| Google Chirp 3 | 실시간 Speech-to-Speech 70언어 | Instant Custom Voice, 30개+ 로케일, 오디오 무보존 | 공개 정보 없음 (GCP 과금 체계) | [[G-11-C]](#ref-g-11-c) |
| OpenAI gpt-4o-mini-tts | WER 35% 개선, 저지연 | Custom Voice 파트너 제한 공급 | $0.015/1K chars (TTS-1-HD 기준) | [[G-04-S]](#ref-g-04-s) |
| Microsoft Azure | Personal Voice v2.1, CNV 440+ 음성 140언어 | 동의 기반 CNV, 엄격한 접근 심사 | $15/1M chars (Neural), $16 (Standard) | [[G-15-C]](#ref-g-15-c) [[G-33]](#ref-g-33) |
| Amazon Polly | Neural TTS 60+ 음성, 29언어 | Voice Cloning 기능 없음 | $19.20/1M chars (Neural) | [[G-33]](#ref-g-33) |
| SKT A.X TTS | 30개+ 한국어 음성, GPU 실시간 | 보이스 클로닝 공개 정보 없음 | API 단가 미공개 (SK 오픈API) | [[E-01]](#ref-e-01) |
| KT Genie Voice | Genie Custom Voice B2B | Custom Voice B2B (API+PaaS) | API/PaaS 이중 과금 구조 | [[E-04]](#ref-e-04) |
| Inworld TTS-1.5-Max | ELO 1,160 (1위), P90 <250ms | — | ElevenLabs 대비 20배 이상 저렴 (자사 주장) | [[G-13-S]](#ref-g-13-s) |

---

## 7. 신뢰도 평가

**높은 확신 [A/B]**:
- Google Gemini 2.5 TTS 멀티스피커·다국어 업그레이드 (공식 블로그 [A])
- ElevenLabs $500M Series D, $11B 밸류에이션 (보도 복수 교차 [B])
- Anthropic Claude Code ElevenLabs 채택 (TechCrunch + The Decoder [B])
- Deutsche Telekom Magenta AI Call Assistant (공식 보도자료 + 텔레콤 공식 사이트 [A])
- EU AI Act Article 50 발효일 2026-08-02 (EU 공식 [A])
- 한국 AI 기본법 Article 31 합성 음성 고지 의무 (과기정통부 공식 [A])
- SKT A.X TTS 전략 (서울경제 기사 — 명확한 발언 인용 [B])
- KT Genie AICC 에이전틱 MWC 2026 공개 (이지이코노미 [B])
- TTS 시장 2025년 $3.65~4.25B 범위 (복수 리서치 기관 교차 [B])

**추가 검증 필요 [C/D]**:
- 시장 규모 CAGR 추정치 편차 큼 (12.3~30.7%) — 기관별 방법론 상이 [C]
- Inworld TTS '20배 저렴' 주장 — 자사 자료 단일 [D]
- Naver HyperCLOVA X Omni MOS 4.22 — 자사 내부 벤치마크 [C]
- Supertone Shift 47ms latency — 자사 주장 단일 [C]
- SKT A.X TTS API 단가 및 Voice Cloning 기능 — 미공개

**데이터 공백**:
- SKT/KT의 Voice Cloning 기술 수준 및 배포 계획 (공개 정보 없음)
- AT&T, Verizon, NTT의 Voice AI TTS 전략 (공개 정보 없음)
- SoftBank의 음성합성 전략 (공개 정보 없음)
- 국내 보이스피싱 탐지용 합성 음성 탐지(딥페이크 음성 탐지) 규제 세부 기준

---

## References

> **통합 References**: 선행 리서치(Voice Synthesis W12, Voice Cloning W12) References + 이번 WTIS 리서치 추가 수집분 전수 포함.
> 선행 파일의 G/P 기호 뒤에 `-S`(Synthesis) 또는 `-C`(Cloning) 접미사를 붙여 출처 파일 구분.

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01-s"></a>G-01-S | Google Blog — Gemini 2.5 Native Audio upgrade, plus text-to-speech model updates | [링크](https://blog.google/products/gemini/gemini-audio-model-updates/) | blog | 2025-12-12 | [A] |
| <a id="ref-g-02-s"></a>G-02-S | Google Blog — Gemini 2.5 Text-to-Speech model updates | [링크](https://blog.google/technology/developers/gemini-2-5-text-to-speech/) | blog | 2025-12-12 | [A] |
| <a id="ref-g-03-s"></a>G-03-S | TechFinitive — Google's Gemini speech-to-speech translation and native audio refresh | [링크](https://www.techfinitive.com/googles-gemini-in-fine-voice-with-new-speech-to-speech-translation-and-native-audio-refresh/) | news | 2025-12-12 | [B] |
| <a id="ref-g-04-s"></a>G-04-S | OpenAI Developer Blog — Updates for developers building with voice | [링크](https://developers.openai.com/blog/updates-audio-models/) | blog | 2025-12-22 | [A] |
| <a id="ref-g-05-s"></a>G-05-S | OpenAI — Introducing next-generation audio models in the API | [링크](https://openai.com/index/introducing-our-next-generation-audio-models/) | blog | 2025-12-22 | [A] |
| <a id="ref-g-06-s"></a>G-06-S | TechCrunch — Claude Code rolls out a voice mode capability | [링크](https://techcrunch.com/2026/03/03/claude-code-rolls-out-a-voice-mode-capability/) | news | 2026-03-03 | [B] |
| <a id="ref-g-07-s"></a>G-07-S | The Decoder — Anthropic's Claude uses ElevenLabs technology for speech features | [링크](https://the-decoder.com/anthropics-claude-uses-elevenlabs-technology-for-speech-features-rather-than-an-in-house-model/) | news | 2026-03-03 | [B] |
| <a id="ref-g-08-s"></a>G-08-S | Dataconomy — Anthropic Rolls Out New Voice Mode For Claude Code Assistant | [링크](https://dataconomy.com/2026/03/04/anthropic-rolls-out-new-voice-mode-for-claude-code-assistant/) | news | 2026-03-04 | [B] |
| <a id="ref-g-09-s"></a>G-09-S | PR Newswire — ElevenLabs debuts '11 Voices' docuseries at SXSW | [링크](https://www.prnewswire.com/news-releases/elevenlabs-debuts-11-voices-docuseries-at-sxsw-as-part-of-global-campaign-to-reach-1-million-people-with-voice-loss-302711275.html) | press | 2026-03-11 | [A] |
| <a id="ref-g-10-s"></a>G-10-S | ElevenLabs — On a mission to help 1 million people reclaim their voices | [링크](https://elevenlabs.io/impact-program) | blog | 2026-03-11 | [A] |
| <a id="ref-g-11-s"></a>G-11-S | AWS — Cartesia Sonic-3 on Amazon SageMaker JumpStart | [링크](https://aws.amazon.com/about-aws/whats-new/2026/02/cartesia-sonic-3-on-sagemaker-jumpstart/) | news | 2026-02 | [A] |
| <a id="ref-g-12-s"></a>G-12-S | Inworld AI — Best TTS APIs for Real-Time Voice Agents (2026 Benchmarks) | [링크](https://inworld.ai/resources/best-voice-ai-tts-apis-for-real-time-voice-agents-2026-benchmarks) | blog | 2026 | [C] |
| <a id="ref-g-13-s"></a>G-13-S | Artificial Analysis — Text to Speech Leaderboard | [링크](https://artificialanalysis.ai/text-to-speech/leaderboard) | tool | 2026-03 | [B] |
| <a id="ref-g-14-s"></a>G-14-S | Inworld AI — Inworld vs ElevenLabs: 20x Cheaper, Higher-Quality TTS | [링크](https://inworld.ai/resources/inworld-vs-elevenlabs) | blog | 2026 | [C] |
| <a id="ref-g-15-s"></a>G-15-S | Microsoft Azure — Azure AI Speech pricing | [링크](https://azure.microsoft.com/en-us/pricing/details/speech/) | doc | 2026 | [A] |
| <a id="ref-g-16-s"></a>G-16-S | AI Tribune — AI Voice Cloning Regulation in 2026 | [링크](https://aitribune.net/2026/02/24/ai-voice-cloning-regulation-in-2026/) | blog | 2026-02-24 | [B] |
| <a id="ref-g-17-s"></a>G-17-S | WeVenture — AI labeling requirement starting in 2026 | [링크](https://weventure.de/en/blog/ai-labeling) | blog | 2026 | [B] |
| <a id="ref-g-18-s"></a>G-18-S | Camb.ai — Real-Time TTS API for Low-Latency Speech Streaming, 2026 Guide | [링크](https://www.camb.ai/blog-post/real-time-tts-api-for-low-latency-speech-streaming) | blog | 2026 | [C] |
| <a id="ref-g-19-s"></a>G-19-S | Google DeepMind — Advanced audio dialog and generation with Gemini 2.5 | [링크](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-2-5-native-audio/) | blog | 2025-12-12 | [A] |
| <a id="ref-g-20-s"></a>G-20-S | Cartesia — Sonic 3 model page | [링크](https://cartesia.ai/sonic) | doc | 2026 | [A] |
| <a id="ref-g-21-s"></a>G-21-S | PyVideoTrans — Gemini 2.5 Adds Multi-Speaker TTS, Available for Free | [링크](https://pyvideotrans.com/en/blog/geminitts) | blog | 2026-03 | [C] |
| <a id="ref-g-22-s"></a>G-22-S | TestingCatalog — Google expands Gemini TTS with 24 languages, lifelike voices | [링크](https://www.testingcatalog.com/google-expands-gemini-tts-with-24-languages-lifelike-voices/) | news | 2026 | [B] |
| <a id="ref-g-23-s"></a>G-23-S | Kyutai Labs — Pocket TTS GitHub (100M parameter, CPU, MIT license) | [링크](https://github.com/kyutai-labs/pocket-tts) | code | 2026-01 | [A] |
| <a id="ref-p-01-s"></a>P-01-S | Mohanty — Causal Prosody Mediation for TTS: Counterfactual Training in FastSpeech2 | [링크](https://arxiv.org/abs/2603.11683) | paper | 2026-03-12 | [A] |
| <a id="ref-p-02-s"></a>P-02-S | DS-TTS — Zero-Shot Speaker Style Adaptation via Dynamic Dual-Style Feature Modulation | [링크](https://arxiv.org/html/2506.01020v1) | paper | 2026 | [A] |
| <a id="ref-p-03-s"></a>P-03-S | Scientific Reports — High fidelity zero shot speaker adaptation in TTS with denoising diffusion GAN | [링크](https://www.nature.com/articles/s41598-025-90507-0) | paper | 2025 | [A] |
| <a id="ref-p-04-s"></a>P-04-S | FunAudioLLM — CosyVoice 2: Scalable Streaming Speech Synthesis with LLMs | [링크](https://arxiv.org/abs/2412.10117) | paper | 2024-12 | [A] |
| <a id="ref-p-05-s"></a>P-05-S | Towards Controllable Speech Synthesis in the Era of LLMs: A Survey | [링크](https://arxiv.org/html/2412.06602v1/) | paper | 2024-12 | [A] |
| <a id="ref-g-01-c"></a>G-01-C | PR Newswire — ElevenLabs debuts '11 Voices' docuseries at SXSW, 1 Million Voices | [링크](https://www.prnewswire.com/news-releases/elevenlabs-debuts-11-voices-docuseries-at-sxsw-as-part-of-global-campaign-to-reach-1-million-people-with-voice-loss-302711275.html) | press | 2026-03-11 | [A] |
| <a id="ref-g-02-c"></a>G-02-C | ElevenLabs Blog — Honoring Eric Dane's Legacy at SXSW | [링크](https://elevenlabs.io/blog/honoring-eric-danes-legacy-at-sxsw-advancing-1-million-voices) | blog | 2026-03-11 | [A] |
| <a id="ref-g-03-c"></a>G-03-C | AdWeek — ElevenLabs Launches AI Voice Licensing Marketplace, McConaughey as Investor | [링크](https://www.adweek.com/media/elevenlabs-ai-voice-marketplace-matthew-mcconaughey/) | news | 2026-03 | [B] |
| <a id="ref-g-04-c"></a>G-04-C | ElevenLabs Blog — Announcing Partnership with Sir Michael Caine to Iconic Marketplace | [링크](https://elevenlabs.io/blog/announcing-partnership-with-sir-michael-caine-to-newly-launched-iconic-marketplace) | blog | 2026-03 | [A] |
| <a id="ref-g-05-c"></a>G-05-C | Blockchain.news — ElevenLabs Launches ElevenCreative Account: Multimodal AI | [링크](https://blockchain.news/ainews/elevenlabs-launches-elevencreative-account-multimodal-ai-for-voice-cloning-70-language-dubbing-and-music-generation-latest-2026-update) | news | 2026-03-10 | [B] |
| <a id="ref-g-06-c"></a>G-06-C | ElevenLabs — ElevenCreative Platform Overview | [링크](https://elevenlabs.io/creative) | web | 2026-03 | [A] |
| <a id="ref-g-07-c"></a>G-07-C | The Decoder — Anthropic's Claude uses ElevenLabs technology for speech features | [링크](https://the-decoder.com/anthropics-claude-uses-elevenlabs-technology-for-speech-features-rather-than-an-in-house-model/) | news | 2026-03 | [B] |
| <a id="ref-g-08-c"></a>G-08-C | TechCrunch — Claude Code rolls out a voice mode capability | [링크](https://techcrunch.com/2026/03/03/claude-code-rolls-out-a-voice-mode-capability/) | news | 2026-03-03 | [B] |
| <a id="ref-g-09-c"></a>G-09-C | TechCrunch — A year later, OpenAI still hasn't released its voice cloning tool | [링크](https://techcrunch.com/2025/03/06/a-year-later-openai-still-hasnt-released-its-voice-cloning-tool/) | news | 2025-03-06 | [B] |
| <a id="ref-g-10-c"></a>G-10-C | OpenAI — Introducing next-generation audio models in the API | [링크](https://openai.com/index/introducing-our-next-generation-audio-models/) | blog | 2026 | [A] |
| <a id="ref-g-11-c"></a>G-11-C | Google Cloud Docs — Chirp 3: Instant Custom Voice Release Notes | [링크](https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice) | web | 2026-03 | [A] |
| <a id="ref-g-12-c"></a>G-12-C | News.oneboard.network — AI Voice Translation live Demo in Google Meet | [링크](https://news.oneboard.network/2026/03/ai-voice-translation-live-demo-in.html) | news | 2026-03 | [C] |
| <a id="ref-g-13-c"></a>G-13-C | TechCrunch — Google snags team behind AI voice startup Hume AI | [링크](https://techcrunch.com/2026/01/22/google-reportedly-snags-up-team-behind-ai-voice-startup-hume-ai/) | news | 2026-01-22 | [B] |
| <a id="ref-g-14-c"></a>G-14-C | AI Adoption Agency — IndexTeam Index TTS 2: Emotionally Expressive Voice Synthesis | [링크](https://aiadoptionagency.com/indexteam-index-tts-2-emotionally-expressive-voice-synthesis-revealed/) | blog | 2025-09 | [C] |
| <a id="ref-g-15-c"></a>G-15-C | Microsoft Tech Community — Personal Voice upgraded to v2.1 in Azure AI Speech | [링크](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/personal-voice-upgraded-to-v2-1-in-azure-ai-speech-more-expressive-than-ever-bef/4435233) | blog | 2026 | [A] |
| <a id="ref-g-16-c"></a>G-16-C | TechCrunch — YouTube expands AI deepfake detection to politicians and journalists | [링크](https://techcrunch.com/2026/03/10/youtube-expands-ai-deepfake-detection-to-politicians-government-officials-and-journalists/) | news | 2026-03-10 | [B] |
| <a id="ref-g-17-c"></a>G-17-C | The AI Insider — YouTube Expands AI Deepfake Detection Tools | [링크](https://theaiinsider.tech/2026/03/11/youtube-expands-ai-deepfake-detection-tools-to-government-officials-politicians-and-journalists/) | news | 2026-03-11 | [B] |
| <a id="ref-g-18-c"></a>G-18-C | Business Research Company — Voice Cloning Market 2026, Size and Demand Forecast | [링크](https://www.thebusinessresearchcompany.com/report/voice-cloning-global-market-report) | report | 2026 | [B] |
| <a id="ref-g-19-c"></a>G-19-C | AI Tribune — AI Voice Cloning Regulation in 2026 | [링크](https://aitribune.net/2026/02/24/ai-voice-cloning-regulation-in-2026/) | blog | 2026-02-24 | [C] |
| <a id="ref-g-20-c"></a>G-20-C | Hollywood Reporter — Babe Ruth, Lana Turner, McConaughey — ElevenLabs Has the Voices | [링크](https://www.hollywoodreporter.com/business/digital/elevenlabs-ai-voices-babe-ruth-judy-garland-1236423582/) | news | 2026-03 | [B] |
| <a id="ref-g-21-c"></a>G-21-C | Radio World — ElevenLabs Launches AI Voice Licensing Marketplace | [링크](https://www.radioworld.com/columns-and-views/guest-commentaries/elevenlabs-launches-ai-voice-licensing-marketplace) | news | 2026-03 | [B] |
| <a id="ref-g-22-c"></a>G-22-C | Winbuzzer — Anthropic Rolls Out Voice Mode for Claude Code | [링크](https://winbuzzer.com/2026/03/04/anthropic-rolls-out-voice-mode-claude-code-xcxwbn/) | news | 2026-03-04 | [B] |
| <a id="ref-p-01-c"></a>P-01-C | 익명 et al. — Targeted Speaker Poisoning Framework in Zero-Shot TTS (arXiv 2603.07551) | [링크](https://arxiv.org/abs/2603.07551) | paper | 2026-03-08 | [A] |
| <a id="ref-p-02-c"></a>P-02-C | 익명 et al. — Lightweight and Stable Zero-shot TTS with Self-distilled Representation Disentanglement (arXiv 2501.08566) | [링크](https://arxiv.org/html/2501.08566) | paper | 2025-01 | [A] |
| <a id="ref-p-03-c"></a>P-03-C | Bilibili/IndexTeam — IndexTTS: Industrial-Level Controllable Efficient Zero-Shot TTS (arXiv 2502.05512) | [링크](https://arxiv.org/abs/2502.05512) | paper | 2025-02 | [A] |
| <a id="ref-p-04-c"></a>P-04-C | 익명 et al. — Voice Cloning: Comprehensive Survey (arXiv 2505.00579) | [링크](https://arxiv.org/abs/2505.00579) | paper | 2025-05 | [A] |
| <a id="ref-p-05-c"></a>P-05-C | 익명 et al. — Fed-PISA: Federated Voice Cloning via Personalized Identity-Style Adaptation (arXiv 2509.16010) | [링크](https://arxiv.org/html/2509.16010v1) | paper | 2025-09 | [A] |
| <a id="ref-e-01"></a>E-01 | SKT / 서울경제 — '5년뒤 10兆 시장' SKT, 음성합성 볼륨업 (A.X TTS 전략 발표) | [링크](https://www.sedaily.com/NewsView/2DAG6VKSE8) | news/IR | 2025 | [B] |
| <a id="ref-e-02"></a>E-02 | ElevenLabs — Mati Staniszewski CEO 발언 (1M Voices 이니셔티브) | [링크](https://elevenlabs.io/blog/honoring-eric-danes-legacy-at-sxsw-advancing-1-million-voices) | press | 2026-03-11 | [A] |
| <a id="ref-e-03"></a>E-03 | Deutsche Telekom — MWC 2026: World premiere of AI-powered call assistant | [링크](https://www.telekom.com/en/media/media-information/archive/mwc-2026-world-premiere-of-ai-powered-call-assistant-1102906) | press | 2026-03-02 | [A] |
| <a id="ref-e-04"></a>E-04 | KT Enterprise — KT 에이전틱 AICC MWC 2026 공개 | [링크](https://www.ezyeconomy.com/news/articleView.html?idxno=232748) | news | 2026-03 | [B] |
| <a id="ref-e-05"></a>E-05 | KT Enterprise — AI Contact Center 서비스 페이지 | [링크](https://enterprise.kt.com/pd/P_PD_AI_CC_SM.do) | web | 2026 | [A] |
| <a id="ref-n-01"></a>N-01 | Business Research Company — Voice Cloning Global Market Report 2026 | [링크](https://www.thebusinessresearchcompany.com/report/voice-cloning-global-market-report) | report | 2026 | [B] |
| <a id="ref-g-26"></a>G-26 | MarketsandMarkets — Text-to-Speech Market Size, Share, Trends and Industry Analysis 2033 | [링크](https://www.marketsandmarkets.com/Market-Reports/text-to-speech-market-2434298.html) | report | 2024 | [B] |
| <a id="ref-g-27"></a>G-27 | GlobeNewswire — Text-to-Speech Strategic Industry Report 2024: $9.3B by 2030, CAGR 13.4% | [링크](https://www.globenewswire.com/news-release/2024/12/04/2991864/28124/en/Text-to-Speech-Strategic-Industry-Report-2024-Rising-Demand-for-AI-Powered-Voice-Solutions-Spurs-TTS-Adoption-A-US-9-3-Billion-Market-by-2030-Growing-at-a-CAGR-of-13-4-from-2023-to.html) | report | 2024-12 | [B] |
| <a id="ref-g-28"></a>G-28 | Business Research Insights — Text-to-Speech Market Size, CAGR 12.3% | [링크](https://www.businessresearchinsights.com/market-reports/text-to-speech-market-122621) | report | 2024 | [C] |
| <a id="ref-g-29"></a>G-29 | Market.us — Voice AI Agents Market Size, CAGR 34.8% | [링크](https://market.us/report/voice-ai-agents-market/) | report | 2025 | [C] |
| <a id="ref-g-30"></a>G-30 | Smallest.ai — TTS Benchmark 2025: Smallest.ai vs ElevenLabs Report (MOS 비교) | [링크](https://smallest.ai/blog/tts-benchmark-2025-smallestai-vs-elevenlabs-report) | blog | 2025 | [C] |
| <a id="ref-g-31"></a>G-31 | Softcery — How to Choose STT and TTS for Voice Agents: OpenAI, Deepgram, ElevenLabs WER 비교 | [링크](https://softcery.com/lab/how-to-choose-stt-tts-for-ai-voice-agents-in-2025-a-comprehensive-guide) | blog | 2025 | [C] |
| <a id="ref-g-32"></a>G-32 | Supertone — Supertonic: Lightning-Fast On-Device Multilingual TTS (ONNX, 47ms) | [링크](https://github.com/supertone-inc/supertonic) | code | 2025 | [B] |
| <a id="ref-g-33"></a>G-33 | Unrealspeech — Amazon Polly vs. Microsoft Azure AI Speech Pricing & Features 2025 | [링크](https://unrealspeech.com/compare/amazon-polly-text-to-speech-vs-microsoft-text-to-speech) | blog | 2025 | [B] |
| <a id="ref-g-34"></a>G-34 | NAVER Cloud Platform — CLOVA Voice AI Services | [링크](https://www.ncloud.com/v2/product/aiService/clovaVoice) | web | 2025 | [A] |
| <a id="ref-g-35"></a>G-35 | SKT 뉴스룸 — SKT AX혁신 가속: 1인 1 AI에이전트 시대 전환 | [링크](https://news.sktelecom.com/219242) | press | 2026 | [A] |
| <a id="ref-g-36"></a>G-36 | EU AI Act — Article 50: Transparency Obligations for Providers and Deployers | [링크](https://artificialintelligenceact.eu/article/50/) | regulation | 2026-08-02 | [A] |
| <a id="ref-g-37"></a>G-37 | Transparent Audio — Transparency Compliance for Generative AI Audio Companies | [링크](https://www.transparentaudio.ai/resources/transparency-compliance-for-generative-ai-audio-companies-understanding-the-eu-ai-act) | blog | 2026 | [B] |
| <a id="ref-g-38"></a>G-38 | 국가법령정보센터 — 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 | [링크](https://www.law.go.kr/lsInfoP.do?lsiSeq=268543) | regulation | 2025-01 | [A] |
| <a id="ref-g-39"></a>G-39 | Business and Human Rights Centre — S. Korea mandates AI content labelling (딥페이크·음성 합성) | [링크](https://www.business-humanrights.org/en/latest-news/s-korea-governments-mandate-ai-content-labelling-to-counter-misinformation-and-deepfakes/) | news | 2025 | [B] |
| <a id="ref-g-40"></a>G-40 | ElevenLabs Blog — Deutsche Telekom: ElevenLabs and Deutsche Telekom embed AI into telco network | [링크](https://elevenlabs.io/blog/deutsche-telekom-ai-call-assistant) | blog | 2026-03 | [A] |
| <a id="ref-g-41"></a>G-41 | SKT Open API — A.X TTS 서비스 페이지 | [링크](https://openapi.sk.com/products/detail?svcSeq=67) | web | 2025 | [A] |
| <a id="ref-g-42"></a>G-42 | KT Cloud — AI API 지니 Voice 서비스 페이지 | [링크](https://cloud.kt.com/product/aiapi/genie_voice/) | web | 2025 | [A] |
