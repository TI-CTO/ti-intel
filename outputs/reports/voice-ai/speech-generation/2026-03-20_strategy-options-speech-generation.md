---
topic: Speech Generation (Voice Synthesis + Voice Cloning)
domain: voice-ai
l2_topic: speech-generation
date: 2026-03-20
skill: strategy-options
wtis_score: 128/200
wtis_verdict: Conditional Go
recommended_option: partner
confidence: medium-high
tags: [claude-code, strategy-options, wtis]
created: 2026-03-20
updated: 2026-03-20
---

# 전략 옵션 분석: Speech Generation (Voice Synthesis + Voice Cloning)

> **WTIS 판정**: Conditional Go (128/200) | **권고 옵션**: Partner (Hybrid) | **날짜**: 2026-03-20

## Executive Summary

> Speech Generation은 TRL 8~9로 상용 성숙한 기술이며, WTIS에서 Borrow + Build 하이브리드 전략을 권고한 바 있다. 3개 전략 옵션을 정량 비교한 결과, **Partner(Hybrid)가 72/100으로 최고점**을 기록했다. Deutsche Telekom이 ElevenLabs + Radisys와 구축한 Magenta AI Call Assistant(MWC 2026)가 통신사 망 내장형 Voice AI 파트너십의 검증된 레퍼런스이며, LG U+는 이 모델을 참조하여 한국어 특화(Naver CLOVA/Supertone) + 글로벌(ElevenLabs) 멀티벤더 전략으로 6~12개월 내 서비스 출시가 가능하다. 자체 TTS 엔진(Build)은 2027년 파주 AIDC 가동 이후 선택적 내재화 경로로 유지하되, 독자 기반 모델 개발의 ROI는 낮다.

---

## 1. WTIS 결과 요약

### 5차원 점수 요약

| 평가 항목 | 점수 (/40) | 핵심 판단 |
|-----------|-----------|----------|
| 고객가치 | **26** | AICC 로봇 음성 불만 + 망 내장형 Voice AI 신규 경험, 단 WTP 미검증 |
| 시장매력도 | **31** | TAM $3.65~4.25B(2025), Voice AI Agent CAGR 34.8% |
| 기술경쟁력 | **25** | TRL 8~9 상용 성숙, 오픈소스 진입 장벽 낮음 |
| 경쟁우위 | **22** | ElevenLabs/Google/SKT/KT 선점, 망 통합만 차별화 기회 |
| 실행가능성 | **24** | 내부 역량 불명 [D], Borrow 모델로 초기 투자 최소화 가능 |
| **합계** | **128/200** | **Conditional Go** |

### 핵심 강점
- **망 내장형 Voice AI**: 앱 불필요, 통신사만의 고유 자산 — Deutsche Telekom 실증
- **규제 대응 우위**: 발신자 인증·동의 관리·워터마킹 역량이 통신사 고유 강점

### 핵심 약점
- **자체 TTS 모델 미보유**: ixi-O는 Google Gemini API에 의존 — 서비스 품질 TTS는 외부 의존 상태
- **후발 진입**: SKT A.X TTS(30종 음성), KT 에이전틱 AICC, Naver MOS 4.22가 이미 선점

---

## 2. 전략 옵션 비교

### 2.1 Build (자체 개발)

**개요**: 오픈소스(CosyVoice 2, Qwen3-TTS) 기반 Fine-tuning으로 한국어 특화 TTS 엔진을 자체 구축

**필요 자원**:
| 항목 | 규모 | 비용 (3년) |
|------|------|-----------|
| 인력 | 8인 팀 (Senior 2 + ML Engineer 3 + Data 2 + Infra 1) | 30~45억 원 |
| GPU 인프라 | H100 8~32장 (초기 학습) + 추론 서빙 | 11~36억 원 |
| 데이터 구축 | 한국어 200~500시간 음성 데이터 | 5~12억 원 |
| 기타 | 외주·협력 | 4~11억 원 |
| **합계** | | **50~104억 원 (3년)** [추정] |

- **MVP 기간**: 12~18개월 (오픈소스 Fine-tuning)
- **전기능 서비스**: 18~30개월 (Voice Cloning 포함)
- **독자 기반 모델**: 36~60개월 (SKT/Naver 수준)

**장점**:
- 완전한 기술 통제·IP 확보, API 비용 종속 탈피
- 통신 도메인 특화(AICC 전용 음성, 브랜드 보이스) 차별화
- 2027년 파주 AIDC(GPU 12만 장) 가동 후 학습 인프라 비용 급감
- LG AI Research와 ONE LG 체계 공동 개발 가능

**단점**:
- MVP도 12~18개월 — 시장 기회비용 큼
- SKT(30종 음성, 8년+ 누적), Naver(MOS 4.22) 대비 3~5년 기술 격차
- 국내 TTS 전문 연구인력 풀 극히 제한, 채용 경쟁 치열
- 오픈소스 품질이 자체 개발 완료 시점에 동등 수준 도달 리스크

**핵심 리스크**: 인재 확보 실패 시 개발 일정 무기한 연장

### 2.2 Buy (인수/라이선스)

**후보 기업 테이블**:

| 기업 | 밸류에이션 | 기술 강점 | 한국어 | 인수 가능성 |
|------|-----------|---------|--------|-----------|
| ElevenLabs | $11B | MOS 4.14+, 70언어, $330M ARR | 지원 | 불가 (IPO 준비) |
| Cartesia | $86M 조달 | TTFB 40ms SSM | 42언어 (한국어 미검증) | 중간 |
| Supertone | HYBE 자회사 ($32M 인수) | ONNX 온디바이스 47ms, 한국어 특화 | 최적 | 낮음~중간 (HYBE 의지 불명) |
| Smallest.ai | ~$50-60M 추정 | 30언어, MOS 4.14 | 한국어 약점 | 중간 |

**유사 M&A 사례**:
- Meta ← PlayAI(2025-07) + WaveForms(2025-08): 소규모 팀 흡수, 금액 미공개
- Google/Hume AI(2026-01): acqui-hire + 라이선싱 구조, CEO 포함 8명 DeepMind 합류
- SoundHound ← Interactions($60M): 음성 AI + AICC B2B 포트폴리오
- **통신사 직접 인수 글로벌 선례 없음** — 파트너십/라이선스가 주류

**라이선스 비용 구조**:
| 공급사 | 표준 가격 | Enterprise | 한국 리전 |
|--------|----------|-----------|----------|
| ElevenLabs | $5~1,320/월 | 별도 협상 | EU/US만 (한국 미지원) |
| Cartesia | 크레딧 기반 ($5~299/월) | Custom | AWS SageMaker 통합 |
| Azure CNV | 학습 최대 $4,992 + $24/1M chars | EA 할인 | Korea Central |
| Google Chirp 3 | HD $30/1M chars | CUD 협상 | Korea 리전 |

**장점**:
- 즉시 글로벌 최고 품질 확보, 2~3개월 내 서비스 출시
- Deutsche Telekom 선행 사례로 협상 레버리지 보유
- ixi-O 글로벌 13개국 확장에 다국어 즉시 대응

**단점**:
- ElevenLabs($11B) 인수는 현실적 불가, Supertone도 HYBE 매각 의지 불명
- 라이선스 시 장기 기술 종속 — 경쟁사 동일 기술 사용 가능
- 자체 모델 개발 역량 축적 불가

**핵심 리스크**:
- 인수: 통신사의 AI 스타트업 인수 성공 사례 전무, 문화 충돌
- 라이선스: Vendor Lock-in (SKT 에이닷 API 종료 사례), PlayHT 서비스 종료 사례

### 2.3 Partner (제휴/협력)

**후보 파트너 테이블**:

| 기업 | 협업 모델 | 기대 효과 |
|------|----------|----------|
| ElevenLabs | API 파트너십 (Deutsche Telekom 모델) | 글로벌 최고 품질, Zero Retention Mode, 50+ 언어 |
| Naver CLOVA | 한국어 특화 API 계약 | 한국어 MOS 4.22 최고, PIPA 준수 용이, 국내 서버 |
| Supertone | 온디바이스 TTS + 독점 라이선스 | ONNX 47ms 초저지연, 한국어 특화, 데이터 주권 해결 |
| Cartesia | 저지연 Voice Agent API | TTFB 40ms, AWS SageMaker 통합 |
| Radisys | 망 내장형 AI 미들웨어 | VoLTE/IMS ↔ AI 통합, Deutsche Telekom 기술 담당 |
| Google Cloud | Chirp 3 멀티클라우드 | 30+ 로케일, CUD 할인, Hume AI 감성 음성 내재화 |
| Microsoft Azure | CNV 엔터프라이즈 | AT&T·Swisscom 레퍼런스, Korea Central 리전, 규제 강점 |

**유사 파트너십 사례 (통신사)**:

**Deutsche Telekom + ElevenLabs + Radisys (MWC 2026)**:
```
Deutsche Telekom (망·고객·규제·브랜딩)
    → Radisys (VoLTE/IMS ↔ AI 미들웨어)
    → ElevenLabs (Voice AI 엔진: TTS + STT + Agent)
```
- "Hey Magenta" 음성 활성화, 앱 불필요
- 전 참여자 AI 개입 즉시 고지 (EU AI Act 사전 준수)
- 2026년 하반기 독일 서비스 개시 → 12개월 내 50개 언어 확대
- **LG U+ 적용**: ElevenLabs(또는 Naver CLOVA) + Radisys(또는 국내 SI) 조합으로 동일 아키텍처 복제 가능

**기타 사례**:
- SKT: Persona AI 투자(3대 주주) + 글로벌 AI 파트너 협업, 단 에이닷 외부 API 정책 변경 피해 발생
- KT: 자체 LLM '믿:음 K 2.0' + 에이전틱 AICC로 자립도 강화
- AT&T: Azure CNV로 자사 브랜드 음성 구축 (White-label)
- Global Telco AI Alliance: 5개 통신사 JV → Syntelligence AI로 전환 (기반 모델 발전 속도에 밀림)

**장점**:
- 빠른 시장 진입 (6~12개월), Deutsche Telekom 실증 모델 참조
- 검증된 품질 즉시 활용, R&D 자원을 망 통합·UX에 집중
- 글로벌 13개국 확장에 다국어 즉시 대응 (ElevenLabs 50+, Chirp 3 30+)
- 멀티벤더 전략으로 Lock-in 리스크 관리 가능

**단점**:
- 마진 공유, 대규모 트래픽 시 API 비용 부담
- 동일 API 사용 경쟁사와 음성 품질 차별화 제한
- 장기 종속 시 내부 Voice AI 역량 공동화
- 규제 대응의 제3자 의존 (파트너사 위반 시 연대 책임 가능)

**핵심 리스크**: Lock-in (SKT 에이닷 사례), 서비스 중단 (PlayHT 사례) → 멀티벤더 + 추상화 레이어로 완화

---

## 3. 정량 비교 매트릭스

| 기준 (각 20점) | Build | Buy (License) | Partner (Hybrid) | 채점 근거 |
|----------------|-------|---------------|------------------|----------|
| **전략 적합성** | 12 | 12 | **16** | Partner: DT 모델 검증, 망 통합 통신사 고유 자산. Build: 자율성 높으나 현 역량 부족. Buy: 즉시 획득 가능하나 동일 기술 경쟁사 접근 |
| **실행 속도** | 4 | **16** | **16** | Build: MVP 12~18개월, 전기능 18~30개월. Buy/Partner: 2~6개월 내 PoC, 6~12개월 서비스 출시 |
| **투자 효율** | 8 | 12 | **16** | Build: 50~104억(3년) 불확실 ROI. Buy: 라이선스 관리 가능하나 종속. Partner: 최소 투자로 시작, 선택적 내재화 |
| **리스크** | 8 | 8 | **12** | Build: 인재 확보·품질 달성 불확실. Buy: Lock-in·PlayHT 종료 사례. Partner: 멀티벤더+추상화로 완화, 단 남은 리스크 존재 |
| **지속 가능성** | **16** | 8 | 12 | Build: 완전 통제·IP, AIDC 인프라(2027). Buy: 영구 종속. Partner: 점진적 내재화 경로 유지 |
| **합계** | **48/100** | **56/100** | **72/100** |

---

## 4. 최종 권고

### 권고 옵션: Partner (Hybrid) — 72/100

WTIS의 Borrow + Build 전략과 일치하며, Deutsche Telekom 모델이 통신사 Voice AI 파트너십의 실현 가능성을 실증했다. LG U+는 TTS/Voice Cloning 엔진을 파트너십으로 조달하되, 망 내장형 통합·규제 대응·한국어 특화 UX를 자체 구축하여 차별화한다.

**Hybrid 전략 구성**:
- **Borrow (즉시)**: ElevenLabs Enterprise(글로벌·다국어) + Naver CLOVA(한국어 AICC) 멀티벤더
- **Build (선택적)**: 2027년 AIDC 가동 후 오픈소스(CosyVoice 2/Qwen3-TTS) 기반 한국어 특화 모델 내재화
- **망 통합 (핵심 차별화)**: Radisys 또는 국내 SI와 VoLTE/IMS 내장형 Voice AI 구현

### 실행 로드맵

| 시점 | 마일스톤 | 담당 |
|------|---------|------|
| **2026 Q2** | ElevenLabs/Cartesia Enterprise PoC 착수 + Naver CLOVA B2B 계약 협의 | 사업개발팀 |
| **2026 Q2** | Radisys 또는 국내 SI 파트너 선정 (망 내장형 미들웨어) | 네트워크기술팀 |
| **2026 Q3** | 망 내장형 Voice AI PoC (앱 없이 통화 중 AI 어시스턴트) | 네트워크기술팀 + AI Lab |
| **2026 Q3~Q4** | ixi-O AICC용 TTS 서비스 출시 (Naver CLOVA 한국어 + ElevenLabs 다국어) | 서비스기획팀 |
| **2026 Q4** | Supertone 전략적 투자/독점 라이선스 협의 (온디바이스 TTS) | 전략기획팀 |
| **2027 H1** | 오픈소스 한국어 Fine-tuning 착수 (AIDC 인프라 활용) | AI Lab |
| **2027 H2** | 글로벌 13개국 다국어 Voice AI 서비스 확대 | 글로벌사업팀 |

### 의사결정 전 확인 필요 사항

1. **ElevenLabs 한국 Data Residency**: 현재 EU/US/인도만 — 한국 리전 제공 여부 협상 필수
2. **Naver CLOVA B2B 전용 SLA**: 통신사 규모 트래픽 대응 가능 여부 + 가격 구조
3. **Supertone-HYBE 관계**: 전략적 투자 또는 독점 라이선스 가능 여부 탐색
4. **자사 AICC 트래픽 볼륨**: API 비용 시뮬레이션을 위한 현재 통화 처리량 확인

---

## 5. 후속 조건 (Conditional Go 연계)

WTIS 후속 조건 체크리스트와 전략 옵션별 해소 경로:

| WTIS 후속 조건 | Partner 해소 경로 |
|---------------|-----------------|
| Deutsche Telekom 모델 심층 분석 | ElevenLabs + Radisys 직접 접촉, 계약 구조·비용 협상 |
| ElevenLabs/Cartesia 파트너십 타진 | Enterprise PoC 착수 (2026 Q2) |
| 망 내장형 Voice AI PoC 설계 | Radisys 또는 국내 SI + AI 엔진(ElevenLabs/CLOVA) 조합 (2026 Q3) |
| AI 음성 고지·워터마킹 규제 대응 | ElevenLabs Zero Retention + 자체 규제 대응 체계 구축 |
| 한국어 특화 Voice Cloning PoC | Supertone(온디바이스) 또는 Naver CLOVA(Custom Voice) PoC |
| AICC 음성 서비스 현황 진단 | 현재 IVR/ARS 트래픽 분석 → API 비용 시뮬레이션 |

---

## References

> 본 분석은 3개 research-deep 에이전트의 리서치 결과와 WTIS 리포트(2026-03-17)를 종합했다. 아래는 핵심 인용 출처이다.

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| T-01 | Deutsche Telekom — MWC 2026 Magenta AI Call Assistant 공식 발표 | [링크](https://www.telekom.com/en/media/media-information/archive/mwc-2026-world-premiere-of-ai-powered-call-assistant-1102906) | press | 2026-03-02 | [A] |
| T-02 | ElevenLabs Blog — Deutsche Telekom AI Call Assistant 파트너십 | [링크](https://elevenlabs.io/blog/deutsche-telekom-ai-call-assistant) | blog | 2026-03-02 | [A] |
| T-03 | ElevenLabs — Series D: $500M at $11B Valuation | [링크](https://elevenlabs.io/blog/series-d) | blog | 2026-02-04 | [A] |
| T-04 | CNBC — Nvidia-backed ElevenLabs hits $11B valuation | [링크](https://www.cnbc.com/2026/02/04/nvidia-backed-ai-startup-elevenlabs-11-billion-valuation.html) | news | 2026-02-04 | [B] |
| T-05 | Korea Herald — LG Uplus bets on voice AI for global expansion (ixi-O MWC 2026) | [링크](https://www.koreaherald.com/article/10687790) | news | 2026-03 | [B] |
| T-06 | LGU+ — 익시오 Google Gemini API 의존 공식 인터뷰 (디지털데일리) | [링크](https://www.ddaily.co.kr/page/view/2025111313382958697) | news | 2025-11-13 | [B] |
| T-07 | SKT — '5년뒤 10兆 시장' 음성합성 A.X TTS 전략 발표 (서울경제) | [링크](https://www.sedaily.com/NewsView/2DAG6VKSE8) | news | 2025 | [B] |
| T-08 | Naver Cloud — CLOVA Voice (한국어 MOS 4.22) | [링크](https://www.ncloud.com/v2/product/aiService/clovaVoice) | web | 2025 | [A] |
| T-09 | AWS — Cartesia Sonic-3 on SageMaker JumpStart | [링크](https://aws.amazon.com/about-aws/whats-new/2026/02/cartesia-sonic-3-on-sagemaker-jumpstart/) | news | 2026-02 | [A] |
| T-10 | Supertone — Supertonic ONNX On-Device TTS 47ms | [링크](https://github.com/supertone-inc/supertonic) | code | 2025 | [B] |
| T-11 | LG AI Research — STT/TTS Research Scientist 채용 | [링크](https://www.lgresearch.ai/careers/view?seq=72) | IR | 2024 | [A] |
| T-12 | LGU+ 파주 AIDC 6,156억 투자 공시 (머니투데이) | [링크](https://www.mt.co.kr/tech/2025/04/29/2025042918171779676) | IR | 2025-04-29 | [A] |
| T-13 | ElevenLabs — Zero Retention Mode (Enterprise) | [링크](https://elevenlabs.io/docs/eleven-api/resources/zero-retention-mode) | doc | 2026-03 | [A] |
| T-14 | ElevenLabs — European Data Residency (EU/US/인도) | [링크](https://elevenlabs.io/blog/introducing-european-data-residency) | blog | 2025 | [A] |
| T-15 | TechCrunch — Meta acquires voice startup PlayAI | [링크](https://techcrunch.com/2025/07/13/meta-acquires-voice-startup-play-ai/) | news | 2025-07-13 | [B] |
| T-16 | TechCrunch — Google snags team behind Hume AI | [링크](https://techcrunch.com/2026/01/22/google-reportedly-snags-up-team-behind-ai-voice-startup-hume-ai/) | news | 2026-01-22 | [B] |
| T-17 | SoundHound — Acquisition of Interactions ($60M) | [링크](https://www.soundhound.com/newsroom/press-releases/soundhound-ai-strengthens-its-leadership-in-agentic-ai-with-the-acquisition-of-interactions-a-pioneer-in-ai-for-customer-service-and-workflow-orchestration/) | press | 2025-09-09 | [A] |
| T-18 | Music Business Worldwide — Supertone HYBE $32M 인수 | [링크](https://www.musicbusinessworldwide.com/meet-kyogu-lee-president-of-supertone-the-voice-cloning-ai-company-acquired-by-hybe-for-32m/) | news | 2023 | [B] |
| T-19 | 전자신문 — SKT 에이닷 글로벌 AI 모델 지원 종료 (Lock-in 사례) | [링크](https://www.etnews.com/20260114000119) | news | 2026-01-14 | [B] |
| T-20 | ElevenLabs — PlayHT Alternatives 2026 (서비스 종료 사례) | [링크](https://elevenlabs.io/blog/playht-alternatives-2026) | blog | 2026 | [B] |
| T-21 | CosyVoice 2 — 한국어 zero-shot 지원 (arXiv) | [링크](https://arxiv.org/html/2412.10117v1) | paper | 2024-12 | [A] |
| T-22 | Qwen3-TTS — 한국어 포함 10개 언어 97ms (DEV Community) | [링크](https://dev.to/czmilo/qwen3-tts-the-complete-2026-guide-to-open-source-voice-cloning-and-ai-speech-generation-1in6) | blog | 2026 | [B] |
| T-23 | Microsoft — MWC 2026 Telecom AI ROI 플랫폼 | [링크](https://www.microsoft.com/en-us/industry/blog/telecommunications/2026/02/24/microsoft-accelerates-telecom-return-on-intelligence-with-a-unified-trusted-ai-platform/) | blog | 2026-02-24 | [A] |
| T-24 | The Mobile Network — Syntelligence AI (Global Telco AI Alliance 전환) | [링크](https://the-mobile-network.com/2026/02/syntelligence-ai-is-the-global-telco-ai-alliance-now/) | news | 2026-02 | [B] |
| T-25 | Microsoft Azure — Custom Neural Voice 가격 (Korea Central) | [링크](https://azure.microsoft.com/en-us/pricing/details/speech/) | doc | 2026-03 | [A] |
| T-26 | Fortune — Cartesia $64M Series A | [링크](https://fortune.com/2025/03/11/exclusive-cartesia-voice-ai-startup-raises-64-million-series-a/) | news | 2025-03-11 | [B] |
| T-27 | Google Cloud — Text-to-Speech Pricing (Chirp 3 HD) | [링크](https://cloud.google.com/text-to-speech/pricing) | doc | 2026-03 | [A] |
| T-28 | KT — MWC 2026 에이전틱 AICC 공개 | [링크](https://www.ezyeconomy.com/news/articleView.html?idxno=232748) | news | 2026-03 | [B] |
| T-29 | Sayna — Multi-Provider STT/TTS 추상화 전략 | [링크](https://sayna.ai/blog/multi-provider-stt-tts-strategies-when-and-why-to-abstract-your-speech-stack) | blog | 2025 | [C] |
| T-30 | LGU+·LG AI연구원 ONE LG 체계 (서울신문) | [링크](https://www.seoul.co.kr/news/economy/industry/2026/03/02/20260302500002) | news | 2026-03-02 | [B] |

### 상세 리서치 리포트 (별첨)

| 옵션 | 리서치 파일 | References |
|------|-----------|-----------|
| Build | `outputs/reports/2026-03-20_research-speech-generation-build-option.md` | 25건 |
| Buy | `outputs/reports/2026-03-20_research-speech-generation-buy-option.md` | 39건 |
| Partner | `outputs/reports/2026-03-20_research-speech-gen-partner.md` | 30건 |

---

*Generated by: strategy-options skill (research-deep × 3 parallel) | 2026-03-20*
*WTIS Source: 2026-03-17_wtis-speech-generation.md (128/200, Conditional Go)*
