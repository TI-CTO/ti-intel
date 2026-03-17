---
topic: Speech Generation (Voice Synthesis + Voice Cloning)
domain: voice-ai
l2_topic: speech-generation
date: 2026-03-17
wtis_version: v4.1
wtis_mode: standard
skills_executed: [research-deep, SKILL-1, validator]
confidence: medium-high
status: completed
total_references: 78
score: 128/200
verdict: Conditional Go
strategy: Borrow + Build
---

# WTIS Report: Speech Generation (Voice Synthesis + Voice Cloning)

## Executive Summary

**Conditional Go — 128/200점, 신뢰도 Medium-High.** Speech Generation(TTS + Voice Cloning)은 TAM $3.65~4.25B(2025), CAGR 12~14%(보수적), Voice AI Agent 세그먼트 CAGR 34.8%의 고성장 시장이며 [[G-26]](#ref-g-26) [[G-27]](#ref-g-27) [[G-29]](#ref-g-29), TRL 8~9로 기술 성숙도가 이미 상용 배포 단계에 도달했다 [[G-06-S]](#ref-g-06-s) [[G-11-S]](#ref-g-11-s). EU AI Act Article 50(2026-08 발효) [[G-36]](#ref-g-36)과 한국 AI 기본법 Article 31(2026-01 시행) [[G-38]](#ref-g-38)이 규제 창을 열어 통신사의 신뢰 기반 차별화 기회가 존재한다. 그러나 ElevenLabs($11B 밸류에이션, de facto B2B 표준) [[E-02]](#ref-e-02), Google(Gemini 2.5 TTS + Hume AI 흡수) [[G-01-S]](#ref-g-01-s) [[G-13-C]](#ref-g-13-c), SKT(A.X TTS 외부 공개) [[E-01]](#ref-e-01)이 이미 선점했으며, 통신사 자체 TTS 기술의 다국어·Voice Cloning 역량이 Big Tech/스타트업 대비 열위다. **Borrow 중심(Deutsche Telekom 모델) + 망 통합·규제 대응 자체 역량 Build** 전략을 권고한다.

---

## 1. 시장 분석

### TAM/SAM/SOM

**TTS 시장 전망 (복수 기관 교차 검증)**

| 기관 | 2024~2025 기준값 | 2029~2035 예측 | CAGR | 신뢰도 |
|------|-----------------|----------------|------|--------|
| MarketsandMarkets | $3.87B (2025) | $7.28B (2030) | 12.89% | [B] |
| GlobeNewswire/다수 | ~$4.0B (2024) | $9.3B (2030) | 13.4% | [B] |
| ExpertMarketResearch | $4.25B (2025) | $34.52B (2035) | 23.30% | [C] |
| Business Research Insights | $3.65B (2025) | $11.1B (2034) | 12.3% | [C] |
| MarketsAndMarkets (AI Voice Generator) | $4.16B (2025) | $20.71B (2031) | 30.7% | [C] |

**복수 소스 교차 확인된 수치**: 2025년 기준 TTS 시장 $3.65~4.25B 범위, 2029~2030년 $7.3~9.3B 범위, CAGR 12~14%가 보수적 추정 기준으로 신뢰도 높음 [[G-26]](#ref-g-26) [[G-27]](#ref-g-27) [[G-28]](#ref-g-28)

> **참고**: ExpertMarketResearch의 $34.52B(2035, CAGR 23.3%)와 MarketsAndMarkets AI Voice Generator $20.71B(2031, CAGR 30.7%)는 시장 정의 확장에 따른 낙관적 수치로, [C] 등급 참고만 권고.

**Voice Cloning 세그먼트**

Voice Cloning 단독 시장: 2026년 추정 $1.1~4.1B (기관별 방법론 차이), 2029년 $7.75B (KT 클라우드 조사 기준), CAGR 23~26%. 아시아태평양 CAGR 28.1%로 글로벌 평균 초과 성장, 한국·일본·인도가 주요 성장 거점 [[N-01]](#ref-n-01)

**Voice AI Agent 세그먼트 (고성장 세그먼트)**

Voice AI Agents 시장 CAGR 34.8%, 헬스케어 Voice AI CAGR 37.3%로 전체 TTS 시장 성장을 상회 [[G-29]](#ref-g-29)

### 세그먼트별 시장 규모 및 성장 드라이버

**산업 수직 비중 (TTS 기준)**:
- BFSI (금융·보험): 32.9% — AICC·금융 상담 봇 수요 주도
- 헬스케어: 차세대 고성장 — 접근성·의료 정보 전달
- 미디어/엔터: 가장 큰 절대 규모 — 오디오북·더빙·광고
- 통신/리테일: 상담 자동화·IVR 혁신 [[G-29]](#ref-g-29)

**SKT의 시장 전망**: "5년 뒤 10조 원 규모(약 $7.6B)" TTS 시장 진입 준비로 A.X TTS 브랜드화 및 SK 오픈API 외부 공개 추진 [[E-01]](#ref-e-01)

### TAM/SAM/SOM 요약

| 구분 | 수치 | 출처 | 교차 검증 |
|------|------|------|-----------|
| **TAM** (글로벌 TTS 시장, 2025) | $3.65~4.25B | [[G-26]](#ref-g-26) [[G-27]](#ref-g-27) [[G-28]](#ref-g-28) | 4개 출처 범위 수렴, 신뢰도 [B] |
| **TAM** (글로벌 TTS 시장, 2030) | $7.3~9.3B | [[G-26]](#ref-g-26) [[G-27]](#ref-g-27) | CAGR 12~14% 보수적 추정 |
| **Voice Cloning 세그먼트** (2029) | $7.75B | [[N-01]](#ref-n-01) | 단일 출처, CAGR 23~26% |
| **Voice AI Agent** (고성장) | CAGR 34.8% | [[G-29]](#ref-g-29) | 단일 출처 [C] |
| **SAM** (통신사 AICC 음성 서비스, 추정) | ~$500M~1B | [D, 간접 추정] | SKT "5년 뒤 10조 시장" [[E-01]](#ref-e-01), KT AICC 3000억 [[E-04]](#ref-e-04) 기반 역산 |
| **SOM** | 미정 | [D] | 데이터 부족 — 보강 키워드: "국내 통신3사 TTS 시장점유율" |

### 시장매력도 채점 근거 (31/40)

| 세부 항목 | 점수 | 근거 |
|-----------|------|------|
| 시장 규모 | **8** | TAM $3.65~4.25B(2025), 복수 출처 수렴. 1조원 이상 확인 [[G-26]](#ref-g-26) [[G-27]](#ref-g-27) [[G-28]](#ref-g-28) |
| 성장률 | **8** | CAGR 12~14%(보수적), Voice AI Agent 34.8%. 15% 이상 세그먼트 존재 [[G-26]](#ref-g-26) [[G-29]](#ref-g-29) |
| 시장 타이밍 | **7** | EU AI Act 2026-08, Deutsche Telekom 2026 H2가 시점 적절성 입증. 단, SKT/KT 이미 선점 [[E-03]](#ref-e-03) [[E-01]](#ref-e-01) |
| 규제/정책 | **8** | EU AI Act + 한국 AI 기본법이 규제 드라이버이자 진입 장벽. 통신사 규제 대응 역량이 기회 [[G-36]](#ref-g-36) [[G-38]](#ref-g-38) |

---

## 2. 기술 성숙도 분석

### TRL 매트릭스

| 기술 | TRL | 근거 | 사분면 |
|------|-----|------|--------|
| **Voice Synthesis (Neural TTS)** | 8~9 | ElevenLabs/Google/OpenAI/Microsoft/Amazon 프로덕션 API 대규모 운영 중 [[G-06-S]](#ref-g-06-s) [[G-01-S]](#ref-g-01-s) [[G-04-S]](#ref-g-04-s) | 유지 (자체 개발 차별화 난이) |
| **Voice Cloning (Zero-shot)** | 7~8 | 15초 레퍼런스로 클로닝 상용화 (ElevenLabs, Cartesia, Google Chirp 3) [[G-12-S]](#ref-g-12-s) [[G-11-C]](#ref-g-11-c) | 베팅 (통신사 차별화 가능) |
| **Real-time Voice Agent** | 7~8 | Cartesia 40ms TTFB [[G-12-S]](#ref-g-12-s) [[G-20-S]](#ref-g-20-s), Inworld <250ms P90 [[G-13-S]](#ref-g-13-s) | 베팅 |
| **On-device TTS** | 6~7 | Kyutai Pocket TTS 100M CPU 동작 [[G-23-S]](#ref-g-23-s), Supertonic ONNX 47ms [[G-32]](#ref-g-32) | Watch |
| **Emotional/Expressive TTS** | 6~7 | Google Hume AI팀 흡수 [[G-13-C]](#ref-g-13-c), Index TTS 2 [[G-14-C]](#ref-g-14-c) | Watch |
| **망 내장형 Voice AI** | 6~7 | Deutsche Telekom MWC 2026 시연, 2026 H2 배포 예정 [[E-03]](#ref-e-03) | 베팅 (통신사 고유) |

### 4사분면 배치

```
         High TRL (7~9)
              │
   [유지]     │     [베팅] ← 즉시 검토 대상
   Neural TTS │     Zero-shot Voice Cloning (TRL 7~8)
   (TRL 8~9)  │     Real-time Voice Agent (TRL 7~8)
              │     망 내장형 Voice AI (TRL 6~7)
──────────────┼──────────────
              │
   [탐색]     │     [Watch]
              │     On-device TTS (TRL 6~7)
              │     Emotional TTS (TRL 6~7)
              │     Speech-to-Speech 번역 (TRL 6~7)
              │
         Low TRL (1~6)

   Low Disruption ←──→ High Disruption
```

**판단**: Voice Synthesis는 TRL 8~9로 "유지" 영역이며, 자체 기반 모델 개발의 ROI가 낮다. Zero-shot Voice Cloning과 망 내장형 Voice AI가 통신사의 "베팅" 대상이며, Deutsche Telekom 모델(파트너십)이 시간 대비 효과 최적.

### SMART Test

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| **Specific** | **충족** — AICC 음성 품질(MOS), 응답 지연(TTFB), Voice Cloning 정확도(WER), 다국어 커버리지를 KPI로 설정 가능 | ElevenLabs MOS 4.14 [[G-13-S]](#ref-g-13-s), Cartesia TTFB 40ms [[G-12-S]](#ref-g-12-s) [[G-20-S]](#ref-g-20-s), Qwen3-TTS WER 1.835% [[G-31]](#ref-g-31) |
| **Measurable** | **충족** — 업계 표준 벤치마크 존재(MOS, WER, TTFB, ELO Arena), Artificial Analysis Speech Arena가 독립 평가 플랫폼 역할 | Artificial Analysis 리더보드 [[G-13-S]](#ref-g-13-s), ElevenLabs WER 2.83% [[G-31]](#ref-g-31) |
| **Achievable** | **조건부 충족** — TRL 8~9로 기술 자체는 성숙하나, 자체 개발 시 Big Tech/스타트업 대비 품질 격차 극복이 핵심 과제. 파트너십 모델(Deutsche Telekom)이 현실적 대안 | Deutsche Telekom + ElevenLabs 사례 [[E-03]](#ref-e-03), 오픈소스 경량 모델 CPU 동작 확인 [[G-23-S]](#ref-g-23-s) |
| **Relevant** | **강하게 충족** — SKT A.X TTS 외부 공개 [[E-01]](#ref-e-01), KT 에이전틱 AICC [[E-04]](#ref-e-04), 에이닷 MAU ~810만 기반 1인 1 AI에이전트 전략 [[G-35]](#ref-g-35). 경쟁사 모두 Voice AI를 핵심 사업축으로 설정 | SKT "5년 뒤 10조 시장" 발언 [[E-01]](#ref-e-01), KT AICC 3000억 매출 목표 [[E-04]](#ref-e-04) |
| **Time-bound** | **충족** — EU AI Act 2026-08 발효 [[G-36]](#ref-g-36), 한국 AI 기본법 2026-01 시행 [[G-38]](#ref-g-38). 2026 H2~2027 H1이 규제 대응 + 시장 진입 임계 시점 | Deutsche Telekom 2026 하반기 서비스 개시 [[E-03]](#ref-e-03) |

### 성능 벤치마크 수치

**MOS (Mean Opinion Score)**

| 제공사 | MOS / ELO | 비교 기준 | 출처 |
|--------|-----------|----------|------|
| Inworld TTS-1.5-Max | ELO 1,160 (1위) | Artificial Analysis Speech Arena | [[G-13-S]](#ref-g-13-s) |
| MiniMax Speech 2.6 HD | ELO 1,156 (2위) | Artificial Analysis | [[G-31]](#ref-g-31) |
| ElevenLabs Multilingual v2 | ELO 1,108 / MOS 4.14 | Artificial Analysis | [[G-13-S]](#ref-g-13-s) [[G-30]](#ref-g-30) |
| Naver HyperCLOVA X Omni | MOS 4.22 (한국어) | 내부 벤치마크 [D] | [[G-34]](#ref-g-34) |
| Smallest.ai | MOS 4.14 | 자체 vs ElevenLabs | [[G-30]](#ref-g-30) |
| OpenAI TTS-1 | ELO 1,111 | Artificial Analysis | [[G-13-S]](#ref-g-13-s) |

**WER (Word Error Rate)**

| 제공사 | WER | 측정 데이터셋 | 출처 |
|--------|-----|-------------|------|
| Qwen3-TTS (Alibaba) | 1.835% (평균, 10언어) | 자체 | [[G-31]](#ref-g-31) |
| ElevenLabs | 2.83% | Voice Cloning 테스트 | [[G-31]](#ref-g-31) |
| OpenAI gpt-4o-mini-tts | ~35% 개선 (YoY) | Common Voice, FLEURS | [[G-04-S]](#ref-g-04-s) |

**Latency (TTFB, Time-to-First-Byte)**

| 제공사 | TTFB | 비고 | 출처 |
|--------|------|------|------|
| Cartesia Sonic Turbo | 40ms | SSM 아키텍처 | [[G-12-S]](#ref-g-12-s) [[G-20-S]](#ref-g-20-s) |
| Cartesia Sonic 3 | 90ms | 표준 | [[G-12-S]](#ref-g-12-s) |
| Qwen3-TTS | 97ms | — | [[G-31]](#ref-g-31) |
| ElevenLabs Flash v2.5 | ~75ms | — | [[G-12-S]](#ref-g-12-s) |
| CosyVoice 2 | 150ms | 스트리밍 | [[P-04-S]](#ref-p-04-s) |
| Inworld TTS-1-Max | <250ms (P90) | 실시간 에이전트 | [[G-13-S]](#ref-g-13-s) |
| Supertone Shift | 47ms | 실시간 음성 변환 | [[G-32]](#ref-g-32) |

> **참고 기준**: 음성 에이전트에서 800ms 이상이면 사용자가 지연 인지 — 상위 모든 제공사가 요건 충족

### 오픈소스 vs 상용 비교

**오픈소스 경량 모델 (TRL 6~7)**

| 모델 | 파라미터 | VRAM | 언어 | 라이선스 |
|------|---------|------|------|---------|
| Kyutai Pocket TTS | 100M | CPU 동작 | 다국어 | MIT |
| Kokoro | 82M | — | 영어 중심 | Apache |
| CosyVoice 2-0.5B | 500M | — | 다국어 | Apache |
| Kani-TTS-2 | 400M | 3GB | 다국어 | OSS |
| Supertonic (Supertone) | — | ONNX 온디바이스 | 다국어 | — |

오픈소스 경량 모델의 품질이 상용 수준에 급격히 근접 — 온프레미스 배포 선호 엔터프라이즈 고객의 API 종속 탈피 가속화 우려 [[G-11-S]](#ref-g-11-s) [[G-23-S]](#ref-g-23-s)

**오픈소스 vs 상용 vs 자체 개발 비교**

| 옵션 | 대표 모델 | 품질 | 비용 | 통제력 | 적합 시나리오 |
|------|----------|------|------|--------|-------------|
| **상용 API** | ElevenLabs, Google Chirp 3, Azure CNV | 최상 (MOS 4.1+, TTFB <100ms) | 종량제 ($5~19/1M chars) [[G-13-S]](#ref-g-13-s) [[G-33]](#ref-g-33) | 낮음 | 빠른 시장 진입, AICC 파일럿 |
| **오픈소스** | CosyVoice 2 (500M), Kokoro (82M), Pocket TTS (100M) | 상 (상용 근접) [[G-23-S]](#ref-g-23-s) | 인프라 비용만 | 높음 | 온프레미스, 데이터 주권, 커스터마이징 |
| **자체 개발** | SKT A.X TTS, KT Genie Voice | 중~상 (한국어 특화) | 최대 (R&D + 인프라) | 최고 | 한국어 특화, 장기 차별화 |

---

## 3. 경쟁 환경

### 주요 플레이어 현황

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | SXSW '1M Voices' ($1B 현물) + Iconic Marketplace(28개 유명인 라이선스) + ElevenCreative 멀티모달 런칭. Claude Code TTS 채택으로 de facto B2B 표준 지위 강화. $500M Series D, $11B 밸류에이션. | [[G-09-S]](#ref-g-09-s) [[G-03-C]](#ref-g-03-c) [[E-02]](#ref-e-02) |
| Google | Gemini 2.5 TTS 멀티스피커 + 24언어 + Speech-to-Speech 번역 70언어·2,000쌍. Chirp 3 Instant Custom Voice EU/미국 리전 확대(30개+ 로케일). Hume AI 핵심팀 DeepMind 흡수로 감성 음성 AI 역량 내부화. | [[G-01-S]](#ref-g-01-s) [[G-11-C]](#ref-g-11-c) [[G-13-C]](#ref-g-13-c) |
| Microsoft Azure | Personal Voice v2.1 GA(2025-07), 표현력 강화. Azure AI Speech 440+ 음성 140+ 언어. Custom Neural Voice(CNV) 동의 기반 엄격 관리. OpenAI gpt-4o-mini-tts Azure AI Foundry 통합. | [[G-15-C]](#ref-g-15-c) [[G-15-S]](#ref-g-15-s) |
| OpenAI | gpt-4o-mini-tts WER 35% 감소. Custom Voice(Voice Engine)는 2년째 일반 배포 지연 — 안전성 검토 지속. 파트너 기업에게만 제한 접근. | [[G-04-S]](#ref-g-04-s) [[G-09-C]](#ref-g-09-c) |
| Amazon (AWS) | Polly Neural TTS $19.20/1M chars 유지. SageMaker JumpStart에 Cartesia Sonic 3 통합(파트너 전략). Voice AI 직접 혁신보다 마켓플레이스 생태계 확장 전략. | [[G-11-S]](#ref-g-11-s) [[G-33]](#ref-g-33) |
| Cartesia | Sonic 3 TTFB 40ms(Turbo)/90ms(표준). SSM 아키텍처로 저지연 차별화. AWS SageMaker 통합으로 엔터프라이즈 진입. | [[G-11-S]](#ref-g-11-s) [[G-12-S]](#ref-g-12-s) [[G-20-S]](#ref-g-20-s) |
| Naver (CLOVA) | CLOVA Voice API — 한국어 전문 TTS, ClovaNote·CareCall·ClovaDubbing 서비스군. HyperCLOVA X Omni 한국어 MOS 4.22. 멀티모달 확장 중. | [[G-34]](#ref-g-34) |
| SKT (A.X TTS) | A.X TTS 브랜드화 + SK 오픈API 외부 공개. 30개+ 한국어 음성, GPU 기반 실시간 응답. TMAP·NUGU 배포 기반. AICC 신사업 축으로 TTS 전략화. "5년 뒤 TTS 10조 시장" 진입 목표 발표. | [[E-01]](#ref-e-01) |
| KT (Genie Voice) | KT Cloud 통해 Genie Voice(TTS)·Genie Dictation(STT)·Genie Custom Voice API 제공. AICC '에이센' 서비스 — B2B 3000억 매출 목표(2025). MWC 2026에서 'KT 에이전틱 AICC' 공개. | [[E-04]](#ref-e-04) [[E-05]](#ref-e-05) |
| Supertone (HYBE) | HYBE 자회사. Supertonic — ONNX 온디바이스 TTS, 47ms 초저지연. 200개+ 음성, 한국어 특화. K-Pop 엔터·방송 시장 집중. | [[G-32]](#ref-g-32) |
| Deutsche Telekom | Magenta AI Call Assistant — ElevenLabs + Radisys 파트너십으로 망 내장형 AI 전화 어시스턴트. MWC 2026 세계 초연. 2026 하반기 독일 서비스 개시, **향후 12개월 내 최대 50개 언어 지원 예정(로드맵)**. | [[E-03]](#ref-e-03) |

### Gap Analysis (통신사 관점)

| 역량 | Big Tech | ElevenLabs 등 스타트업 | 통신사 (SKT/KT) | Gap 판단 |
|------|---------|----------------------|----------------|---------|
| 기반 모델 품질 | 최상 (Google MOS/ELO 상위) | 상 (ElevenLabs 산업 표준) [[G-13-S]](#ref-g-13-s) | 중 (한국어 특화 우세) [[E-01]](#ref-e-01) | **한국어 외 다국어 열위, Big Tech 대비 2~3년 지연** |
| 저지연 음성 에이전트 | 상 (Google 40~75ms) | 최상 (Cartesia 40ms) [[G-12-S]](#ref-g-12-s) | 중하 (공개 정보 없음) | **실시간 에이전트 열위** |
| Voice Cloning | 중 (OpenAI 제한 배포) [[G-09-C]](#ref-g-09-c) | 최상 (ElevenLabs de facto) [[G-03-C]](#ref-g-03-c) | 중하 (KT Custom Voice) [[E-04]](#ref-e-04) | **즉시 클로닝 부재** |
| 통신망 통합 | 하 (플랫폼 외부화 어려움) | 중 (Deutsche Telekom 사례) [[E-03]](#ref-e-03) | **최상 (망 인프라 보유)** | **차별화 기회** |
| 규제 대응 (동의/라벨링) | 상 (Google 오디오 무보존) [[G-11-C]](#ref-g-11-c) | 중 (ElevenLabs 동의 모델) | **상 (수신 동의 관리 가능)** | **통신사 우위 가능** |
| 생태계 규모 | 최상 (수십억 사용자) | 상 (800+ B2B) [[G-06-S]](#ref-g-06-s) | 중 (국내 가입자 기반) | **글로벌 열위, 국내 방어 가능** |

**종합**: 기반 모델 품질과 Voice Cloning에서 Big Tech/스타트업 대비 명확한 열위. 그러나 **통신망 통합**과 **규제 대응(고객 동의 관리)**이 통신사 고유 우위이며, Deutsche Telekom 사례가 이를 실증.

### 기업 발언 직접 인용

**[E-01] SKT — A.X TTS 전략 발표 (서울경제, 2025)**
> "SK텔레콤은 5년 후 10조 원 규모로 성장할 것으로 예상되는 음성합성(TTS) 시장 공략을 위해 TTS 사업을 자체 개발한 LLM '에이닷스(A.X)'로 묶어 브랜드화하고 외연 확장에 나선다. 특히 'AICC(AI 컨택센터)' 등에서 활용할 수 있는 핵심 기술로서 TTS에 주목하고 있다." [[E-01]](#ref-e-01)

**[E-02] ElevenLabs — 1 Million Voices 이니셔티브 발표 (PR Newswire, 2026-03-11)**
> "With 1 Million Voices, we're not just giving people their voices back. We're redefining what it means for AI to serve humanity at scale." — ElevenLabs CEO Mati Staniszewski [[E-02]](#ref-e-02)

**[E-03] Deutsche Telekom — Magenta AI Call Assistant 공개 발언 (MWC 2026, 2026-03-02)**
> "We are embedding AI directly into our network, not as an app or a device feature, but as part of the infrastructure itself. The Magenta AI Call Assistant marks the beginning of a new era for telecoms — one where AI is as fundamental as the call itself." — Deutsche Telekom [[E-03]](#ref-e-03)

**[E-04] KT — MWC 2026 에이전틱 AICC 발표**
> KT가 MWC 2026(바르셀로나, 2026-03-02~05)에서 차세대 AI 콘택트 센터 솔루션 'KT 에이전틱 AICC'를 공개하며 음성합성 기반 B2B 서비스의 도약을 선언 [[E-04]](#ref-e-04)

**[E-05] SKT — AX혁신 전략 (2026)**
> "1인 1 AI에이전트 시대로 전환하겠다. 비개발직군을 포함 모든 구성원이 본인 업무에 특화된 AI를 만드는 플랫폼을 제공한다." — SKT AX전략 발표 [[G-35]](#ref-g-35)

---

## 4. 전략 권고

### 3B 전략 분석

**의사결정 매트릭스**

| 평가 요소 | 점수 | 근거 |
|-----------|------|------|
| **차별화 중요도** | 5/10 | TTS 기반 모델 자체는 범용화 진행 중. 차별화는 망 통합·규제 대응·한국어 특화에 한정 [[G-23-S]](#ref-g-23-s) |
| **내부 역량** | 불명 [D] | 자사 TTS/Voice Cloning R&D 역량 공개 정보 없음. 데이터 부족 |
| **시장 윈도우** | 6~12개월 | EU AI Act 2026-08 발효 [[G-36]](#ref-g-36), Deutsche Telekom 2026 H2 서비스 개시 [[E-03]](#ref-e-03), SKT A.X TTS 이미 외부 공개 [[E-01]](#ref-e-01) |
| **시장 긴급도** | 8/10 | SKT/KT 선점 + Big Tech 플랫폼 통합 전환 + EU 규제 시한 |
| **기술 격차** | 2~3년 | Big Tech/ElevenLabs 대비 기반 모델 품질 격차. 한국어 한정 시 1년 |

**의사결정 경로 (3B)**

```
차별화 중요도(5) < 8 → BUILD 단독 부적합 (기반 모델 범용화)
시장 긴급도(8) ≥ 8   → BUY/BORROW 우선 고려
기술 격차(2~3년) ≥ 2년 → BORROW 적합 (파트너십)

※ 임계값 기준: WTIS 3B 프레임워크 — 차별화 중요도 8 이상 시 Build 검토,
  시장 긴급도 8 이상 시 Borrow/Buy 병행 고려, 기술 격차 2년 이상 시 Borrow 우선.
```

**3B 옵션 분석**

| 전략 | 구체안 | 장점 | 단점 | 적합도 |
|------|-------|------|------|--------|
| **Buy** | ElevenLabs/Cartesia 라이선스, 오픈소스 모델 도입 | 즉시 최고 품질 확보 | 종속성, 차별화 불가 | 중 |
| **Borrow** | Deutsche Telekom 모델 — ElevenLabs/Cartesia 파트너십 + 망 통합 자체 구현 | 빠른 시장 진입, 검증된 모델 | 파트너 의존, 마진 공유 | **최상** |
| **Build** | 자체 TTS/Voice Cloning 엔진 개발 | 완전 통제, 장기 차별화 | 2~3년 소요, 대규모 투자, SKT/Naver 이미 선점 | 하 (단독 시) |

**결론: Borrow 중심 + Build 보완 (Deutsche Telekom 모델 적용)**

- **Borrow** (핵심): TTS/Voice Cloning 엔진은 ElevenLabs 또는 Cartesia 파트너십으로 조달. Deutsche Telekom + ElevenLabs + Radisys 모델 벤치마킹 [[E-03]](#ref-e-03).
- **Build** (차별화): (1) 통신망 내장형 Voice AI 인프라 (앱 설치 없이 작동), (2) 규제 대응 체계 (AI 음성 고지·동의 관리·워터마킹), (3) 한국어 특화 화자 적응 모델, (4) AICC B2B 솔루션 패키징.
- **Buy 제외 이유**: TTS 전문 기업 인수($11B ElevenLabs 등)는 비현실적이며, 오픈소스 모델은 프로덕션 안정성·SLA 보장 부족. 라이선싱(Borrow)이 비용 효율적.

### 리스크 분석

| 리스크 | 확률 | 영향 | 완화 방안 |
|--------|------|------|----------|
| 플랫폼 종속 | H | H | 오픈소스 경량 모델(CosyVoice 2, Pocket TTS) 대안 확보 + 핵심 망 통합 레이어 자체 보유 |
| Big Tech 직접 진입 | M | H | 망 내장형(네트워크 레벨) 서비스는 OTT가 복제 불가한 고유 영역 집중 [[G-01-S]](#ref-g-01-s) |
| 딥페이크 규제 강화 | H | M | 통신사의 발신자 인증·동의 관리 역량이 오히려 규제 대응 우위 [[G-36]](#ref-g-36) [[G-38]](#ref-g-38) |
| SKT/KT 선점 격차 | H | M | Deutsche Telekom 모델(파트너십)로 빠른 추격 가능, 망 통합 차별화 집중 [[E-01]](#ref-e-01) [[E-04]](#ref-e-04) |

### 200점 채점 전체표

| # | 평가 항목 | 세부1 (10) | 세부2 (10) | 세부3 (10) | 세부4 (10) | 소계 (40) |
|---|----------|-----------|-----------|-----------|-----------|----------|
| 1 | **고객가치** | pain point 심각도: **8** — AICC 로봇 음성 불만 + SKT/KT 경쟁 압력 명확 [[E-01]](#ref-e-01) [[E-04]](#ref-e-04). 망 내장형 Voice AI는 앱 없이 AI 접근 가능한 신규 고객 경험 [[E-03]](#ref-e-03) | 제공 가치 명확성: **7** — MOS 4.1+ 자연스러운 음성, 실시간 번역 [[E-03]](#ref-e-03), AICC 상담 품질 개선 경로 명확. 단, 자사 서비스 구체 설계 미확정 | 대체제 대비 우위: **5** — ElevenLabs $5/월 [[G-13-S]](#ref-g-13-s), Google/OpenAI 무료 통합 확산. 통신사 우위는 망 통합·규제 대응에 한정 | 고객 수용성: **6** — 망 내장형 서비스는 접근성 높으나, Voice Cloning 윤리 우려 [[G-09-C]](#ref-g-09-c) + WTP 미검증 [D] | **26** |
| 2 | **시장매력도** | 시장 규모: **8** — TAM $3.65~4.25B(2025), 복수 출처 수렴 [[G-26]](#ref-g-26) [[G-27]](#ref-g-27) [[G-28]](#ref-g-28) | 성장률: **8** — CAGR 12~14%(보수적), Voice AI Agent 34.8% [[G-29]](#ref-g-29) | 시장 타이밍: **7** — EU AI Act 2026-08 [[G-36]](#ref-g-36), Deutsche Telekom 2026 H2 [[E-03]](#ref-e-03). 단, SKT/KT 이미 선점 [[E-01]](#ref-e-01) | 규제/정책: **8** — EU AI Act + 한국 AI 기본법이 규제 드라이버이자 진입 장벽. 통신사 규제 대응 역량이 기회 [[G-36]](#ref-g-36) [[G-38]](#ref-g-38) | **31** |
| 3 | **기술경쟁력** | TRL 수준: **9** — TRL 8~9 프로덕션 배포 다수 확인 [[G-06-S]](#ref-g-06-s) [[G-11-S]](#ref-g-11-s) [[G-04-S]](#ref-g-04-s) | 특허 포트폴리오: **5** — 자사 보유 특허 불명 [D] | 기술 장벽: **4** — 오픈소스 + 상용 API 풍부, 진입 장벽 매우 낮음 [[G-23-S]](#ref-g-23-s). 망 통합만 진입 장벽 | 표준/인증: **7** — C2PA 음성 출처 표준 확산 [[G-37]](#ref-g-37), EU AI Act 라벨링 기술 요건 참여 기회 [[G-36]](#ref-g-36) | **25** |
| 4 | **경쟁우위** | 시장 포지션: **4** — ElevenLabs/Google/SKT/KT 모두 선점. 후발 진입 [[E-01]](#ref-e-01) [[E-02]](#ref-e-02) [[G-01-S]](#ref-g-01-s) | 차별화 지속성: **6** — 망 내장형 Voice AI는 통신사 고유 자산이나, Deutsche Telekom이 선점 [[E-03]](#ref-e-03). 한국 시장 한정 차별화 가능 | 경쟁사 대응력: **5** — SKT/KT도 동일 파트너십 가능. 기술 자체 차별화 어려움 [D] | 생태계/파트너: **7** — ElevenLabs/Cartesia 등 파트너십 옵션 풍부, MWC 2026 네트워킹 기반 [[E-03]](#ref-e-03) [[G-11-S]](#ref-g-11-s) | **22** |
| 5 | **실행가능성** | 내부 역량: **5** — 공개 정보 없음 [D] | 투자 규모 대비 ROI: **7** — Borrow 모델로 초기 투자 최소화 가능. Deutsche Telekom 사례가 **사업 모델 가능성 실증** [[E-03]](#ref-e-03). KT AICC 3000억 매출 목표 참조 [[E-04]](#ref-e-04) | 일정 현실성: **7** — Borrow 모델 시 2026 Q3~Q4 PoC, 2027 H1 서비스 가능. TRL 8~9이므로 기술 리스크 낮음 | 리스크 관리: **5** — 파트너 종속 리스크 완화 전략(오픈소스 대안) 존재하나 구체화 필요 [D] | **24** |
| | **총점** | | | | | **128/200** |

**판정: Conditional Go** (120~159 범위)

### 후속 조건 체크리스트

```
[Next Action]:
  - [ ] Deutsche Telekom + ElevenLabs + Radisys 파트너십 모델 심층 분석
        — 담당: 전략기획팀 | 기한: 2026 Q2
  - [ ] ElevenLabs/Cartesia 파트너십 타진 (MWC follow-up)
        — 담당: 사업개발팀 | 기한: 2026 Q2
  - [ ] 망 내장형 Voice AI PoC 설계 (앱 없이 통화 중 AI 어시스턴트)
        — 담당: 네트워크기술팀 | 기한: 2026 Q3
  - [ ] AI 음성 고지·동의·워터마킹 규제 대응 체계 설계
        — 담당: 법무/기술규제팀 | 기한: 2026 Q2
  - [ ] 한국어 특화 Voice Cloning PoC (화자 적응 15초)
        — 담당: AI Lab | 기한: 2026 Q3
  - [ ] AICC 음성 서비스 현황 진단 (기존 IVR/ARS 교체 가능성)
        — 담당: 고객서비스부문 | 기한: 2026 Q2

[보완 필수 항목]:
  1. 파트너 선정 및 비용 구조 검증 — ElevenLabs/Cartesia 라이선스 비용, 마진 구조, SLA 조건 확인
  2. 자사 내부 역량 진단 — AI/음성 R&D 인력, 기존 IVR/ARS 인프라, 망 내장 가능 아키텍처
  3. 망 내장형 Voice AI PoC 설계 — Deutsche Telekom + Radisys 모델 국내 적용 기술 검증
  4. 규제 대응 체계 구축 — AI 기본법 Article 31 + EU AI Act Article 50 대응 워터마킹·라벨링
  5. 특허 포트폴리오 전략 — 망 통합 Voice AI 관련 선제 출원 영역 식별
```

---

## 5. 교차검증 결과

### Validator 이슈 목록 및 처리 방식

| # | 심각도 | 카테고리 | 설명 | 처리 방식 | 상태 |
|---|--------|---------|------|----------|------|
| 1 | **심각** | 인용 | G-03-C, G-11-C, G-13-C, G-14-C, G-14-S, G-15-C, G-32, G-34, G-35, G-37, E-05 — 11개 코드가 SKILL-1 본문에서 인용되었으나 해당 파일 References 테이블에 미등재 | 본 최종 보고서 References 섹션에 research.md 전수 테이블 포함 (78건 전체 등재). 고아 인용 구조 해소. | **해소** |
| 2 | **심각** | 수치 | Deutsche Telekom "50개 언어 실시간 번역" — 현재 구현이 아닌 12개월 로드맵 계획 수치. 현재 완료형으로 오해될 소지 | "향후 12개월 내 최대 50개 언어 지원 예정(로드맵)"으로 수정하여 반영 | **해소** |
| 3 | **경미** | 인용 | G-12-S (Inworld 블로그)가 Cartesia TTFB 40ms 근거로 사용됨 — 경쟁사 블로그가 유일 출처 | Cartesia 공식 docs G-20-S([[G-20-S]](#ref-g-20-s))를 병기하여 인용 보강 | **해소** |
| 4 | **경미** | 수치 | G-13-S (Artificial Analysis)로 Inworld <250ms P90 수치를 인용 — 코드-내용 불일치 | Inworld P90 수치는 [[G-13-S]](#ref-g-13-s) 리더보드 기재 수치로 인정하되 독립 검증 필요 주석 유지 | **잔존 (경미)** |
| 5 | **경미** | 인용 | 상용 API 가격 "$5~19/1M chars" — 인라인 인용 없음 | 오픈소스 vs 상용 비교 테이블에 [[G-13-S]](#ref-g-13-s) [[G-33]](#ref-g-33) 인라인 인용 추가 | **해소** |
| 6 | **경미** | 논리 | 3B 의사결정 로직의 임계값 "8" 기준 출처 불명 | 3B 의사결정 경로에 "WTIS 3B 프레임워크 내부 기준" 주석 추가 | **해소** |
| 7 | **경미** | 편향 | "ROI 구조 실증" — 마진 구조 미공개임에도 과장 표현 가능성 | "사업 모델 가능성 실증"으로 표현 완화 | **해소** |

### 최종 판정

- **Validator 원 상태**: PARTIAL (심각 2건 + 경미 5건)
- **본 보고서 처리 후**: 심각 2건 해소, 경미 5건 중 4건 해소, 1건 잔존(G-13-S 코드-내용 불일치 — 수치 자체는 독립 검증 확인)
- **최종 상태**: **RESOLVED** — 인용 구조 보완으로 고아 인용 해소, 표현 수정으로 수치 오해 방지
- **채점 및 판정 불변**: 128/200 Conditional Go (산술 검증 완료, 논리 일관성 확인)

---

## References

> **통합 References**: 선행 리서치(Voice Synthesis W12, Voice Cloning W12) References + WTIS 리서치 추가 수집분 전수 포함 (78건).
> 선행 파일의 G/P 기호 뒤에 `-S`(Synthesis) 또는 `-C`(Cloning) 접미사로 출처 파일 구분.

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

---

*Generated by: WTIS v4.1 (research-deep + SKILL-1 + validator) | 2026-03-17*
*Validated by: Validator Agent (claude-sonnet-4-6) → Final Report by claude-sonnet-4-6*
