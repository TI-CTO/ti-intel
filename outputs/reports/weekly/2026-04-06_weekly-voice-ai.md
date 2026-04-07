---
type: weekly-monitor
domain: voice-ai
week: 2026-W15
date: 2026-04-06
l3_count: 8
deep_count: 2
tags:
  - claude-code
  - weekly
created: 2026-04-06
updated: 2026-04-06
---

# 주간 기술 동향: Voice AI (2026-W15)

## Executive Summary

> **이번 주 핵심**: Voice AI 경쟁의 중심이 "TTS 품질"에서 "에이전트 플랫폼 생태계"로 이동하고 있다. ElevenLabs가 4/1 대규모 플랫폼 업데이트(Model Context Protocol Tool Scoping, 동영상→음악, Speech-to-Text URL 전사)를 단행하며 종합 에이전트 플랫폼 전환을 명확히 했고, 학계에서는 OmniVoice가 600+ 언어 제로샷 Text-to-Speech (TTS)를 시연하며 다국어 음성 서비스의 기술 장벽이 급격히 낮아지고 있다. 한편 Apple Siri 개선이 iOS 26.5 베타에도 부재 → iOS 27 이전 출시 불가가 확정(2년 지연)되면서, Samsung Now Nudge·Salesforce Slackbot 등이 컨텍스트 기반 액션 추천 시장을 선점하는 구도가 형성되고 있다.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| Speech Generation | Voice Synthesis | 🟡 | [생태계] ElevenLabs 에이전트 플랫폼 업데이트(4/1, MCP Tool Scoping) · [논문] OmniVoice 600+ 언어 제로샷 TTS · [투자] Miravoice $6.3M Seed |
| | Voice Cloning | 🟢 | W14 시그널(Voxtral 클로닝, McAfee 96%) 이후 소강. 딥페이크 위협 내러티브 지속 |
| Personal Intelligence | Context Action Recommendation | 🟡 | [제품출시] Salesforce Slackbot 30개 AI 기능 + 데스크톱 컨텍스트(3/31) · [경쟁사] Apple Siri iOS 27 이전 불가 확정 · [생태계] Anthropic Conway 상시 에이전트 테스트(4/3) |
| | Persona Plugin | 🟢 | Anthropic Persona Selection Model (PSM) 논문 후속 논의 지속. 구조적 돌파 없음 |
| | Relationship Graph | 🟢 | LLM 기반 Knowledge Graph (KG) 구축 연구 지속(Nature, arXiv). 변화 없음 |
| Speech Perception & Interaction | Interrupt & Turn-Taking | 🟢 | W14 시그널(xAI Grok, SoundHound, SID-Bench) 이후 소강. 변화 없음 |
| | Emotional Analysis | 🟢 | Foundation Model SER 연구 지속. 변화 없음 |
| | Context Recognition | 🟢 | Conversational AI "Year of Context" 내러티브 지속. 변화 없음 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
> **태그** : [기술돌파] [제품출시] [경쟁사] [규제] [투자] [논문] [생태계]

---

## 🟢 Quick 요약 (변화 미미)

### Voice Cloning
- W14의 Mistral Voxtral TTS 3초 제로샷 클로닝, McAfee Deepfake Detector 96% 정확도 시그널 이후 소강. 딥페이크 산업화 위협(기업 사칭 980건, Q3 2025 기준) 내러티브 지속. EU AI Act Article 50 투명성 Code of Practice (CoP) 5~6월 확정 예정. ADD-GP 퓨샷 딥페이크 탐지 프레임워크(Gaussian Process 기반) 발표.

### Interrupt & Turn-Taking
- W14 핵심(xAI Grok Voice Agent API, SoundHound Aragon 리더, SID-Bench 인터럽트 벤치마크) 이후 신규 돌파 없음. 엔터프라이즈 음성 에이전트의 sub-100ms 레이턴시 기대치가 업계 표준으로 고착. Deepgram Flux의 시맨틱 턴 감지(전사 모델 내 대화 흐름 통합) 접근법 주목.

### Emotional Analysis
- Foundation Model 기반 제로샷 Speech Emotion Recognition (SER) 연구 지속. 실시간 딥러닝 SER 시스템(Springer Nature, Long Short-Term Memory (LSTM) 기반 7개 감정 분류) 연구 발표. 구조적 변화 없음.

### Context Recognition
- Conversational AI 채택 "critical velocity" 지속(Gartner). 멀티도메인 Dialogue State Tracking (DST) 동적 지식 융합 논문(Springer Nature) 발표. 30% 이상의 신규 애플리케이션에 자율 에이전트 내장 예측(International Data Corporation, IDC). 구조적 돌파 없음.

### Persona Plugin
- Anthropic이 2/23 발표한 Persona Selection Model (PSM) 프레임워크 후속 논의 지속 — LLM이 프리트레이닝 중 다양한 페르소나 시뮬레이션 능력을 학습하고, 포스트트레이닝이 특정 어시스턴트 페르소나를 정련한다는 이론. AI 페르소나 시뮬레이션이 실제 인간 응답 대비 90%+ 상관관계 달성 주장. 구조적 돌파 없음.

### Relationship Graph
- LLM 기반 KG 구축 정제 기법 논문(Nature Scientific Reports, 2026). 텍스트 컬렉션에서 KG 구축 방법론 종합(arXiv 2603.25862). Mental Disorders Knowledge Graph (MDKG) 1,000만 관계 구축(Nature Communications). GraphRAG 프로덕션 성숙(300~320% Return on Investment (ROI) 보고). 구조적 변화 없음.

---

## 🟡🔴 Deep 심층 분석

### Voice Synthesis — 🟡 주목

#### 이전 대비 변화
- 전주: 오픈웨이트 + 기업 파트너십 2중 공세 — Voxtral TTS 4B, xAI Grok Voice Agent API, ElevenLabs-IBM watsonx, Amazon Polly General Availability (GA)
- 금주: 플랫폼 확장 + 오픈소스 가속 — ElevenLabs 에이전트 플랫폼 업데이트(4/1), Cartesia Sonic-3 AWS 배포 확대, OmniVoice 600+ 언어 논문, Miravoice $6.3M
- 변화 방향: 경쟁 중심이 "단순 TTS 품질"에서 "에이전트 플랫폼 생태계"로 이동. 오픈소스(Kokoro·Dia2)는 온디바이스·스트리밍 특화로 차별화

#### 기술 동향

1. **ElevenLabs 에이전트 플랫폼 대규모 업데이트(4/1) — MCP Tool Scoping, 동영상→음악, STT URL 전사.**
   4월 1일 Application Programming Interface (API) v2.41.1 배포로 종합 에이전트 플랫폼 전환을 명확히 했다. MCP Tool Scoping은 워크플로우 단계별 서브에이전트 도구 접근 권한을 제어하는 엔터프라이즈 거버넌스 기능이다. 동영상→음악 생성, STT URL 전사(YouTube·TikTok 직접 전사), JavaScript Software Development Kit (SDK) v1.0.0 브레이킹 체인지 등이 포함되었다. 2월 업데이트에서 `eleven_v3_conversational` 에이전트 모델, TTS Normalizer 3.1, WhatsApp 아웃바운드가 배포되었다. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)

2. **Cartesia Sonic-3 — State Space Model (SSM) 아키텍처, 42언어, 90ms, AWS SageMaker 통합.**
   2026년 2월 Amazon SageMaker JumpStart에 통합되며 엔터프라이즈 배포 경로를 확장했다. SSM 아키텍처로 대화 맥락을 효율적으로 보존하며, 블라인드 테스트에서 62% 선호도를 기록했다. $100M 펀딩(Kleiner Perkins·Index Ventures·Lightspeed·NVIDIA), ServiceNow·Cresta·Decagon 등 월 수백만 건 대화 처리 중이다. [[G-03]](#ref-g-03), [[G-04]](#ref-g-04)

3. **OmniVoice — 600+ 언어 제로샷 TTS, 확산 언어 모델, 58.1만 시간 학습.**
   4월 1일 arXiv에 발표된 OmniVoice(Zhu et al.)는 확산 언어 모델(Diffusion Language Model)로 텍스트에서 멀티코드북 음향 토큰을 직접 매핑한다. 오픈소스 다국어 데이터 581,000시간을 학습하여 중국어·영어·다언어 벤치마크에서 state-of-the-art를 달성했다. 코드·모델 공개로 재현성을 보장했다. [[P-01]](#ref-p-01)

4. **오픈소스 TTS 확산: Kokoro-82M + Nari Labs Dia2.**
   Kokoro-82M(Apache 2.0)이 HuggingFace 다운로드 220만 건을 돌파했다. 82M 파라미터로 Mean Opinion Score (MOS) 4.2(오픈소스 최고), Real-Time Factor (RTF) 0.03, CPU 구동 가능, $1/1M chars 미만이다. 한국 스타트업 Nari Labs의 Dia2(Apache 2.0, 1B/2B)는 스트리밍 아키텍처로 첫 토큰부터 음성 생성을 시작하며 단일 GPU에서 실시간 동작한다. [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)

5. **Deepgram Aura-2 — 엔터프라이즈 전용 TTS, sub-200ms Time-to-First-Byte (TTFB), 도메인 특화.**
   약물명·법률 용어·날짜·통화 등 도메인별 발음 최적화가 특징이다. 40+ 음성, $0.030/1k chars로 Cartesia($0.038)·ElevenLabs Flash($0.050) 대비 저렴하게 포지셔닝했다. 클라우드·Virtual Private Cloud (VPC)·온프레미스 유연 배포를 지원한다. [[G-07]](#ref-g-07)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | 4/1 에이전트 플랫폼 업데이트: MCP Tool Scoping, 동영상→음악, STT URL 전사, JS SDK v1.0.0. 2월: `eleven_v3_conversational`, WhatsApp 아웃바운드 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02) |
| Cartesia | Sonic-3 AWS SageMaker JumpStart 통합(2월). SSM, 42언어, 90ms. $100M 펀딩, ServiceNow·Cresta·Decagon 고객 | [[G-03]](#ref-g-03), [[G-04]](#ref-g-04) |
| Deepgram | Aura-2 엔터프라이즈 TTS. sub-200ms TTFB, 40+ 음성, 도메인 특화 발음, $0.030/1k chars | [[G-07]](#ref-g-07) |
| Nari Labs | Dia2 오픈소스 스트리밍 TTS(Apache 2.0, 1B/2B). 한국계 20대 창업팀 | [[G-06]](#ref-g-06) |
| Kokoro (hexgrad) | 82M 파라미터, HuggingFace 220만 DL, MOS 4.2, RTF 0.03, Apache 2.0 | [[G-05]](#ref-g-05) |
| Miravoice | $6.3M Seed(Unusual Ventures). AI 음성 에이전트 전화 설문 전문, 14언어, 120문항+ 자율 수행 | [[G-08]](#ref-g-08) |
| Mistral AI | W14 Voxtral TTS 4B 이후 커뮤니티 벤치마크 비교 확산. 신규 발표 없음 | [[G-09]](#ref-g-09) |
| xAI | W14 Grok Voice Agent API 이후 개발자 채택 단계. LiveKit 플러그인 마이그레이션 사례 증가 | [[G-10]](#ref-g-10) |

#### 시장 시그널

**투자 & M&A**
- Q1 2026 글로벌 Venture Capital (VC) $300B 사상 최고. AI 비중 80%($242B). Voice AI 섹터 직접 수혜 [[G-11]](#ref-g-11)
- Miravoice $6.3M Seed: Unusual Ventures 주도, Neo·25madison·Ramp·Atlassian·Google 엔젤 참여 [[G-08]](#ref-g-08)
- Cartesia $100M 확인(Kleiner Perkins·NVIDIA 참여). AWS 배포 채널 확대로 기업가치 재평가 기대 [[G-04]](#ref-g-04)

**파트너십 & 제휴**
- Cartesia + Amazon SageMaker JumpStart: 원클릭 배포 경로 제공(2월) [[G-03]](#ref-g-03)
- ElevenLabs 멀티채널 확장: WhatsApp 아웃바운드 + YouTube/TikTok STT URL 전사 통합 [[G-01]](#ref-g-01)

**시장 전망**
- Voice & Language Intelligence 시장: 2026년 $24.49B → 2035년 $145.03B [[G-12]](#ref-g-12) [추가확인 필요]
- AI Voice Generator: 2025년 $4.16B → 2031년 $20.71B [[G-13]](#ref-g-13) [추가확인 필요]
- AI Voice Agents: 2024년 $2.4B → 2034년 $47.5B (Compound Annual Growth Rate 34.8%) [[G-12]](#ref-g-12) [추가확인 필요]

**연구 동향**
- OmniVoice(Zhu et al., arXiv 4/1): 600+ 언어 제로샷 TTS — 확산 언어 모델 아키텍처로 다국어 음성 서비스 기술 장벽 급감 [[P-01]](#ref-p-01)
- 오픈소스 스트리밍·경량 TTS(Dia2, Kokoro-82M)와 상용 플랫폼(Cartesia sub-100ms, Deepgram sub-200ms) 기준이 수렴 중

**커뮤니티 시그널**
- Kokoro-82M HuggingFace 220만 DL, 커뮤니티 5,600+ 서포터로 오픈소스 TTS 표준 부상 [[G-05]](#ref-g-05)
- 개발자 핵심 페인포인트: 레이턴시 갭(현재 ~510ms vs 인간 ~230ms), 가격 불투명성, 다국어 코드스위칭 미지원 [[C-01]](#ref-c-01)

#### 시장 수요 (voice-of-market)

> Hacker News (HN) 4개 쓰레드 + 업계 공개 자료에서 시그널 추출. YouTube 컨퍼런스 영상 미확보(ElevenLabs Summit London 2026 오프라인 전용).

**고객 페인포인트**
- 레이턴시 갭 — 오케스트레이션 파이프라인(Automatic Speech Recognition + LLM + TTS) 총 지연 ~510ms vs 인간 대화 ~230ms — 출처: Cartesia State of Voice AI 2024
- 긴 입력 할루시네이션·오디오 아티팩트 — 프로덕션 신뢰성 저하 — 출처: HN ChatTTS 쓰레드
- 감정 표현 제어 불가 — 문장 단위 처리로 캐릭터 감정 반영 불가 — 출처: HN ChatTTS 쓰레드

**도입 장벽**
- 가격 불투명성 — 토큰 기반 과금이 대규모 운영 시 비용 예측 불가. "ElevenLabs 가격이 컨슈머 비즈니스를 불가능하게 만든다" — 출처: HN Inworld TTS 쓰레드
- 규제 산업 컴플라이언스 미충족 — Service Organization Controls (SOC) 2, Health Insurance Portability and Accountability Act (HIPAA) Business Associate Agreement, Federal Risk and Authorization Management Program (FedRAMP) 인증 및 온프레미스 배포 요구 — 출처: Deepgram TTS Alternatives 2026
- 실시간 Speech-to-Speech 구축 복잡성 — 재현 가능한 가이드 부재, 6~12개월 엔지니어링 공수 — 출처: HN Ask HN 쓰레드

**시장 니즈**
- 서브 200ms 엔드투엔드 레이턴시 — 콜센터·음성 에이전트 프로덕션 핵심 요구 — 출처: Cartesia State of Voice AI 2024
- 도메인 특화 파인튜닝·커스텀 발음 사전 — 의료·금융·통신 전문 용어 정확도 — 출처: Cartesia State of Voice AI 2024
- 온디바이스/엣지 경량 TTS — 오프라인, 프라이버시, 저지연 — 출처: HN Kitten TTS 쓰레드

#### 전략적 시사점

**기회**
- 에이전트 플랫폼 통합 수요 급증: ElevenLabs·Cartesia 모두 다채널 음성 에이전트 플랫폼으로 전환 중. MCP·WhatsApp·YouTube 통합이 접점 채널을 빠르게 확장
- 오픈소스 온프레미스 수요: Kokoro-82M·Dia2 같은 경량 모델이 데이터 레지던시·보안 요건 높은 엔터프라이즈(금융·의료·공공)에서 부상
- 600+ 언어 지원 현실화: OmniVoice 성과로 신흥 시장(동남아·아프리카) 음성 AI 진입 기회

**위협**
- 빅테크 플랫폼 잠금 위험: Cartesia-AWS, ElevenLabs-IBM 통합이 생태계 종속성 강화
- 오픈웨이트 가격 하방 압력: Voxtral $0.016, Kokoro <$1/1M chars, Dia2 무료 호스팅이 프리미엄 TTS 가격 정당화 압박
- SSM 아키텍처 미검증 리스크: Cartesia Sonic-3의 SSM이 장기 컨텍스트 품질 유지에서 아직 충분히 검증되지 않음 [추가확인 필요]

---

### 컨텍스트 기반 액션 추천 — 🟡 주목

#### 이전 대비 변화
- 전주: Lenovo Qira 프로액티브 AI 슈퍼에이전트(Consumer Electronics Show (CES) 2026). Apple Siri+Gemini 통합 지연 우려
- 금주: Apple Siri iOS 26.5 부재 확정 → iOS 27(9월) 이전 불가. Salesforce Slackbot 데스크톱 컨텍스트(3/31). Samsung Now Nudge 크로스앱(MWC). Anthropic Conway 상시 에이전트(4/3)
- 변화 방향: 컨텍스트 인식 범위가 단일 앱 → 크로스앱 → 데스크톱 전체로 확장. 소비자(Samsung, Apple)와 엔터프라이즈(Slackbot, Microsoft Copilot) 양쪽에서 동시 경쟁 가속

#### 기술 동향

1. **Apple Siri 개선, iOS 26.5 베타 부재 → iOS 27 이전 불가 확정 (3/30).**
   MacRumors(Bloomberg Mark Gurman 인용)가 3/30 보도. Worldwide Developers Conference (WWDC) 2024 최초 공개 이후 약 2년 지연. 지연 원인은 정확도 문제(쿼리 미처리, 응답 지연)로, iOS 26.4 내부 테스트에서 발견되었다. Apple-Google Gemini 딜($1B/년)은 확정이나 실제 탑재 시점이 불투명하다. [[G-14]](#ref-g-14), [[G-15]](#ref-g-15)

2. **Salesforce Slackbot 30개 AI 기능: 데스크톱 컨텍스트 인식 도입 (3/31).**
   핵심은 Slack 인터페이스 밖 데스크톱 전체로 컨텍스트 확장. Customer Relationship Management (CRM) 딜·대화·캘린더·습관 데이터 기반 Actionable Suggestions 제공. MCP 클라이언트 아키텍처로 외부 에이전트 연동 가능. Reusable AI Skills로 커스텀 태스크 정의·재활용. CTO Parker Harris: "Slack이 업무가 실행되는 미래 인터페이스" [[G-16]](#ref-g-16), [[E-01]](#ref-e-01)

3. **Samsung Galaxy S26 "Now Nudge": 크로스앱 컨텍스트 팝업 추천 (MWC 2026).**
   앱 간 컨텍스트를 분석해 타이밍이 맞는 제안을 팝업 형태로 제공. 예시: 메신저 저녁 약속 수신 → 캘린더 충돌 감지 → Nudge 팝업. Now Brief 일일 브리핑 기능 동반. Gemini·Perplexity 멀티에이전트 단일 진입점 지원. [[G-17]](#ref-g-17), [[E-02]](#ref-e-02)

4. **Anthropic "Conway" 상시 구동 에이전트 플랫폼 테스트 (4/3).**
   Claude를 Slack·Jira·코드 저장소에서 상시(always-on) 프로액티브 분석자로 운영하는 플랫폼. 반응형 도구가 아닌 자율적 맥락 분석·제안 구조. 공개 출시 일정 미정. [[G-18]](#ref-g-18)

5. **Microsoft 365 Copilot Work IQ: 장기 메모리 컨텍스트 레이어 (3월 업데이트).**
   Work IQ가 사용자 역할·조직 구조·프로젝트 이력을 M365 전반에 걸쳐 지속 인식. Agent Recommendations가 대화 중 관련 에이전트를 자동 제안. Excel에 이메일·캘린더 컨텍스트 자동 연결. [[G-19]](#ref-g-19)

6. **AgenticRS 아키텍처 프레임워크 정립 (arXiv, 3/27).**
   Alibaba International(Hu et al.)이 추천 모듈을 에이전트로 승격하는 조건을 정의하고, Decision/Evolution/Infrastructure 3계층 구조를 제안했다. Reinforcement Learning 기반 로컬 최적화와 LLM 기반 구조적 혁신을 결합한 진화 메커니즘이 핵심이다. [[P-02]](#ref-p-02)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Apple | Siri 개선 iOS 26.5 부재 확인(3/30). iOS 27(9월) 이전 불가. Gemini 연동 $1B/년 확정이나 탑재 시점 불투명. 2년 지연 공식화 | [[G-14]](#ref-g-14), [[G-15]](#ref-g-15) |
| Salesforce | 3/31 Slackbot 30개 AI 기능: 데스크톱 컨텍스트, MCP 클라이언트, Reusable AI Skills | [[G-16]](#ref-g-16), [[E-01]](#ref-e-01) |
| Samsung | Galaxy S26 Now Nudge 크로스앱 추천, Now Brief 일일 브리핑. Gemini·Perplexity 멀티에이전트 | [[G-17]](#ref-g-17), [[E-02]](#ref-e-02) |
| Microsoft | M365 Copilot Work IQ 장기 메모리, Agent Recommendations(3월 업데이트) | [[G-19]](#ref-g-19) |
| Anthropic | Conway 상시 구동 에이전트 플랫폼 내부 테스트(4/3). 출시 일정 미정 | [[G-18]](#ref-g-18) |
| Google | CC 에이전트(Gmail·Calendar·Drive 통합 일일 브리핑) 12/16 조기 접속 개시 | [[G-20]](#ref-g-20) |

#### 시장 시그널

**시장 전망**
- AI 기반 추천 시스템: 2025년 $22억 → 2026년 $23.7억, CAGR 7.6% [[G-21]](#ref-g-21) [추가확인 필요]
- Context-Aware Computing: 2025년 $838억 → 2034년 $2,898억, CAGR 13.9% [[G-22]](#ref-g-22) [추가확인 필요]

**도입 사례**
- Salesforce Slackbot: CRM 딜·대화·캘린더 기반 데스크톱 전체 Actionable Suggestions. GA 2026/1/13(Business+/Enterprise+) [[G-16]](#ref-g-16)
- Samsung Now Nudge: 크로스앱 컨텍스트 팝업. Galaxy S26 시리즈 탑재 [[G-17]](#ref-g-17)
- Anthropic Conway: Slack·Jira·코드 저장소 상시 프로액티브 분석 (테스트 중) [[G-18]](#ref-g-18)

**연구 동향**
- AgenticRS(Hu et al., arXiv 3/27) — 추천 시스템을 에이전트로 승격하는 체계적 프레임워크. 기능적 폐루프·독립 평가·진화 가능 결정 공간 3조건 정의 [[P-02]](#ref-p-02)
- AMEM4Rec(Nguyen et al., arXiv 2/9) — 크로스유저 메모리 기반 에이전트 추천. Amazon·MIND 데이터셋에서 최신 LLM 추천 모델 대비 성능 향상 [[P-03]](#ref-p-03)

#### 시장 수요 (voice-of-market)

> Lenovo Tech World CES 2026 프레스 릴리즈·핸즈온 리뷰·HN 2개 쓰레드에서 시그널 추출.

**고객 페인포인트**
- 앱 전환 피로 — AI를 쓰려면 별도 앱을 열거나 명시적으로 호출해야 하는 마찰 — 출처: Lenovo Qira 프레스 릴리즈 (Dan Dery VP)
- 크로스 디바이스 컨텍스트 단절 — 기기 전환 시 AI 맥락 초기화 — 출처: Windows Central Qira 핸즈온
- 에이전트 블랙박스 의사결정 — 추천 근거 불투명, 사용자 멘탈 모델 형성 불가 — 출처: HN "AI agents: Less capability, more reliability"

**도입 장벽**
- 데이터 프라이버시 불투명성 — 개인 맥락 데이터 저장 위치·처리 방식 불명확 — 출처: Windows Central Qira 핸즈온
- 멀티스텝 신뢰성 붕괴 — 단계별 99% 정확도라도 20단계 파이프라인이면 시스템 전체 신뢰도 급락 — 출처: HN "The current hype around autonomous agents"
- 엔터프라이즈 컨텍스트 레이어 미성숙 — ERP·타임시리즈 등 구조화 데이터 통합 불가 — 출처: HN "The Enterprise Context Layer"

**시장 니즈**
- Ambient 추천 — 앱 호출 없이 현재 작업 맥락 기반 선제적 제안 — 출처: Lenovo Qira 프레스 릴리즈
- 크로스앱·크로스디바이스 컨텍스트 연속성 — 출처: Lenovo/Motorola Qira (CES 2026)
- Human-in-the-Loop 액션 승인 — 검토 체크포인트·실행 취소 메커니즘 필수 — 출처: HN "AI agents: Less capability, more reliability"

#### 전략적 시사점

**기회**
- 크로스앱 컨텍스트 수집 레이어: Now Nudge·Slackbot 방식의 앱 전환 없는 컨텍스트 통합 수집 미들웨어가 핵심 역량으로 부상
- Apple 공백기 활용: iOS 27 이전 약 5~6개월간(4~8월) Apple 생태계에서 차별화 기능 구현 여지
- MCP 기반 통합: MCP 클라이언트 아키텍처로 이종 에이전트·서비스 간 컨텍스트 연동 비용 절감

**위협**
- Big Tech 번들링: Microsoft(Work IQ), Salesforce(Slackbot), Google(CC+Gemini)이 생산성 플랫폼에 컨텍스트 추천을 내재화
- 프라이버시 규제 리스크: 데스크톱 전체 컨텍스트 수집은 General Data Protection Regulation (GDPR)·국내 개인정보보호법과 충돌 가능성
- Siri 지연의 생태계 분열: Apple 사용자에 대한 컨텍스트 추천 도달 지연으로 Android 중심 기능 격차 발생

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 Voice AI 도메인 관련 SKT·KT 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 에이닷 조직 전면 배치 | 2026 조직개편에서 AI Customer Information Center (CIC) 내 모든 부서명에 "에이닷" 공통 부여. AI 수익화 방점 | persona-plugin | [[E-03]](#ref-e-03) |
| 1인 1 AI 에이전트 전략 | 전 구성원이 AI 에이전트를 직접 설계·업무 적용하는 문화 조성. 에이전틱 AI 시대 내부 AX 전환 | context-action-recommendation | [[E-04]](#ref-e-04) |
| NTT Docomo AI-RAN 백서 | 4/1 가상화 기지국 진화·AI-RAN 구현 핵심 기술 요건 백서 공동 발간 | (L3 밖) | [[E-05]](#ref-e-05) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 에이전틱 AICC (MWC 2026) | 다수 AI 에이전트가 협업해 고객 상담~후속 업무 전 과정 자동화하는 자율형 솔루션 공개(3월) | interrupt-turn-taking | [[E-06]](#ref-e-06) |
| AI 보이스피싱 탐지 2.0 | TTS 생성 변조 음성 판별 딥보이스 탐지 기능 포함. 통화 전 스팸/피싱 차단 강화 | voice-cloning | [[E-07]](#ref-e-07) |
| AICC & CX 인사이트 2026 | 4월 제13회 컨퍼런스 440명 참석. Agentic AI 기반 AICC가 자율 문제 해결 플랫폼으로 진화 조망 | context-action-recommendation | [[G-23]](#ref-g-23) |

### 시사점
- SKT는 에이닷을 중심으로 "1인 1 AI 에이전트" 전략을 전사 수준에서 추진하며 조직 구조까지 재편. 소비자 Voice AI 경쟁에서 페르소나·컨텍스트 추천 역량을 키우려는 방향.
- KT는 B2B AICC에 에이전틱 AI를 접목하여 기업 고객 시장에서 차별화. 보이스피싱 탐지 2.0으로 보안 측면도 강화. 양사 모두 Voice AI를 핵심 성장 축으로 설정.

---

## 규제 & 거버넌스

> Voice AI 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| EU AI Act Article 50 (합성 콘텐츠 투명성 의무) | 2026-08-02 | D-118 |
| EU AI Act 투명성 Code of Practice (CoP) | 2026-05~06 확정 예정 | D-30~60 |
| 한국 AI 기본법 Article 31 (AI 생성 표시 의무) | 2026-01-22 | 시행 중 |

### 신규 발의 & 가이드라인
- **한국 AI 기본법 시행령 입법예고**: 딥페이크 결과물(음성 포함)에 대해 "시각·청각 등을 통해 쉽게 확인할 수 있는 방법"으로 표시 의무화. 비가시적 워터마크만으로는 불인정. 규제 유예 기간 최소 1년(중대한 인명·인권 사안만 예외) [[G-24]](#ref-g-24)
- **EU AI Act 음성 클로닝 컴플라이언스 프레임워크**: 음성 복제 시스템에 투명한 데이터 소싱·화자 명시적 동의·합성 콘텐츠 명확 라벨링 의무. 무단 SNS 오디오 스크래핑은 규제 위반. 위반 시 연 매출 7% 또는 $15M 중 높은 금액 과징금 [[G-25]](#ref-g-25)

### 시사점
- EU CoP 5~6월 확정 후 8월 Article 50 시행으로 TTS/음성 클로닝 서비스의 투명성 표시 의무가 현실화. 한국 AI 기본법도 유사한 방향이나 유예 기간으로 당장의 실무 영향은 제한적.
- 음성 AI 서비스 제공자는 합성 음성 표시 메커니즘(청각적 워터마크 또는 음성 안내)을 사전 준비해야 함.

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **"에이전트 플랫폼" 수렴**: Voice Synthesis(ElevenLabs MCP Tool Scoping)와 Context Action Recommendation(Slackbot MCP 클라이언트, Anthropic Conway)이 동시에 MCP 기반 에이전트 플랫폼으로 수렴하고 있다. 음성 AI가 독립 API가 아닌 워크플로우 내 에이전트 컴포넌트로 재포지셔닝되는 흐름.

2. **오픈소스 가속과 가격 하방 압력**: TTS(Kokoro-82M, Dia2)와 추천 시스템(AgenticRS 오픈 프레임워크) 모두에서 오픈소스 생태계가 빠르게 성숙하며 상용 솔루션의 가격 정당화를 압박. 통신사 입장에서는 자체 호스팅 옵션 확대로 비용 최적화 기회.

3. **Apple 공백이 만드는 기회**: Siri 2년 지연으로 Samsung·Google이 소비자 프로액티브 AI 시장을 선점. 통신사가 Android 기반 에이닷·AICC에서 컨텍스트 추천 기능을 강화할 타이밍.

### 후속 조치 제안

- 🟡 Voice Synthesis 플랫폼 경쟁 심화 → 다음 주 모니터링에서 ElevenLabs SDK v1.0.0 마이그레이션 반응 추적
- 🟡 Context Action Recommendation → Apple WWDC 2026(6월) 발표 전까지 Samsung/Salesforce 동향 지속 모니터링

📋 **Next Steps:**
  📊 프레젠테이션 필요 시:
    → `/slides outputs/reports/weekly/2026-04-06_weekly-voice-ai.md`
  📂 Obsidian 동기화:
    → `/obsidian-bridge outputs/reports/weekly/2026-04-06_weekly-voice-ai.md weekly`
  🔍 특정 L3 심화 조사:
    → `/research-session {L3 주제}`
  📅 다른 도메인 모니터링:
    → `/weekly-monitor agentic-ai` (월) / `/weekly-monitor secure-ai` (수)

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | ElevenLabs — Changelog 2026-04-01 (API v2.41.1) | [링크](https://elevenlabs.io/docs/changelog/2026/4/1) | changelog | 2026-04-01 | [A] |
| <a id="ref-g-02"></a>G-02 | Releasebot — Eleven Labs Release Notes (TTS Normalizer 3.1, WhatsApp) | [링크](https://releasebot.io/updates/eleven-labs) | news | 2026-02-09 | [B] |
| <a id="ref-g-03"></a>G-03 | AWS — Cartesia Sonic 3 on Amazon SageMaker JumpStart | [링크](https://aws.amazon.com/about-aws/whats-new/2026/02/cartesia-sonic-3-on-sagemaker-jumpstart/) | news | 2026-02 | [A] |
| <a id="ref-g-04"></a>G-04 | StartupStag — Cartesia Raises $100M, Launches Sonic-3 | [링크](https://startupstag.com/investments/cartesia-raises-100m-launches-sonic-3-ai-voice-model/) | news | 2025-10 | [B] |
| <a id="ref-g-05"></a>G-05 | HuggingFace — hexgrad/Kokoro-82M (2.2M downloads, MOS 4.2) | [링크](https://huggingface.co/hexgrad/Kokoro-82M) | repository | 2026 | [B] |
| <a id="ref-g-06"></a>G-06 | GitHub — nari-labs/dia2: Streaming conversational TTS | [링크](https://github.com/nari-labs/dia2) | repository | 2025-11 | [B] |
| <a id="ref-g-07"></a>G-07 | Deepgram — Introducing Aura-2: Enterprise-Grade TTS | [링크](https://deepgram.com/learn/introducing-aura-2-enterprise-text-to-speech) | blog | 2025-04 | [B] |
| <a id="ref-g-08"></a>G-08 | Crunchbase — Miravoice Raises $6.3M Seed | [링크](https://news.crunchbase.com/venture/ai-interviewer-miravoice-raises-seed-funding-unusual/) | news | 2026-04 | [B] |
| <a id="ref-g-09"></a>G-09 | VentureBeat — Mistral Voxtral TTS open-weight | [링크](https://venturebeat.com/orchestration/mistral-ai-just-released-a-text-to-speech-model-it-says-beats-elevenlabs-and) | news | 2026-03-26 | [B] |
| <a id="ref-g-10"></a>G-10 | AI Voice Newsletter — xAI Grok Voice Agent API | [링크](https://aivoicenewsletter.com/p/cartesia-s-100m-sonic-3-leap) | news | 2026-03 | [B] |
| <a id="ref-g-11"></a>G-11 | Crunchbase — Q1 2026 $300B Venture Funding Record | [링크](https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/) | news | 2026-04-01 | [B] |
| <a id="ref-g-12"></a>G-12 | Precedence Research — Voice & Language Intelligence Market | [링크](https://www.precedenceresearch.com/voice-and-language-intelligence-market) | report | 2026 | [B] |
| <a id="ref-g-13"></a>G-13 | MarketsandMarkets — AI Voice Generator Market | [링크](https://www.marketsandmarkets.com/PressReleases/ai-voice-generator.asp) | report | 2025 | [B] |
| <a id="ref-g-14"></a>G-14 | MacRumors — New Siri Features Absent From iOS 26.5 Beta | [링크](https://www.macrumors.com/2026/03/30/ios-26-5-no-new-siri-features/) | news | 2026-03-30 | [B] |
| <a id="ref-g-15"></a>G-15 | CNBC — Apple picks Google's Gemini to run AI-powered Siri | [링크](https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html) | news | 2026-01-12 | [A] |
| <a id="ref-g-16"></a>G-16 | SiliconANGLE — Salesforce transforms Slackbot with 30 AI features | [링크](https://siliconangle.com/2026/03/31/salesforce-transforms-slackbot-ultimate-work-assistant-30-new-ai-features/) | news | 2026-03-31 | [B] |
| <a id="ref-g-17"></a>G-17 | Samsung Newsroom — Galaxy AI at MWC 2026 | [링크](https://news.samsung.com/global/samsung-advances-galaxy-ai-and-its-connected-ecosystem-at-mwc-2026) | news | 2026-03 | [A] |
| <a id="ref-g-18"></a>G-18 | Dataconomy — Anthropic Tests Conway Platform | [링크](https://dataconomy.com/2026/04/03/anthropic-tests-conway-platform-for-continuous-claude/) | news | 2026-04-03 | [B] |
| <a id="ref-g-19"></a>G-19 | Microsoft — What's New in M365 Copilot, March 2026 | [링크](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--march-2026/4506322) | news | 2026-03 | [A] |
| <a id="ref-g-20"></a>G-20 | Google Blog — CC AI Agent | [링크](https://blog.google/technology/google-labs/cc-ai-agent/) | news | 2025-12-16 | [A] |
| <a id="ref-g-21"></a>G-21 | Global Growth Insights — AI Recommendation System Market | [링크](https://www.globalgrowthinsights.com/market-reports/ai-based-recommendation-system-market-102057) | report | 2026 | [C] |
| <a id="ref-g-22"></a>G-22 | Fortune Business Insights — Context-Aware Computing Market | [링크](https://www.fortunebusinessinsights.com/industry-reports/context-aware-computing-market-101605) | report | 2026 | [B] |
| <a id="ref-g-23"></a>G-23 | 전자신문 — 제13회 AICC & CX 인사이트 2026 | [링크](https://www.etnews.com/20260329000072) | news | 2026-03-29 | [B] |
| <a id="ref-g-24"></a>G-24 | 정책브리핑 — AI기본법 22일 시행, 생성형 AI 워터마크 표시 의무 | [링크](https://www.korea.kr/news/policyNewsView.do?newsId=148958380) | news | 2026-01 | [A] |
| <a id="ref-g-25"></a>G-25 | AI Tribune — AI Voice Cloning Regulation in 2026 | [링크](https://aitribune.net/2026/02/24/ai-voice-cloning-regulation-in-2026/) | news | 2026-02-24 | [B] |
| <a id="ref-p-01"></a>P-01 | Zhu et al. — OmniVoice: Omnilingual Zero-Shot TTS (arXiv) | [링크](https://arxiv.org/abs/2604.00688) | paper | 2026-04-01 | [A] |
| <a id="ref-p-02"></a>P-02 | Hu et al. — AgenticRS: From Pipelines to Agentic Recommender Systems (arXiv:2603.26100) | [링크](https://arxiv.org/abs/2603.26100) | paper | 2026-03-27 | [A] |
| <a id="ref-p-03"></a>P-03 | Nguyen et al. — AMEM4Rec: Cross-User Memory for Agentic LLM Recommenders (arXiv:2602.08837) | [링크](https://arxiv.org/abs/2602.08837) | paper | 2026-02-09 | [A] |
| <a id="ref-e-01"></a>E-01 | Salesforce CTO Parker Harris — "Slack이 업무가 실행되는 미래 인터페이스" | [링크](https://siliconangle.com/2026/03/31/salesforce-transforms-slackbot-ultimate-work-assistant-30-new-ai-features/) | IR/발표 | 2026-03-31 | [A] |
| <a id="ref-e-02"></a>E-02 | Samsung — Galaxy S26 Unpacked 2026: Now Nudge 공식 발표 | [링크](https://news.samsung.com/global/galaxy-unpacked-2026-a-first-look-at-the-galaxy-s26-series-samsungs-most-intuitive-ai-phone-yet) | IR/발표 | 2026-02 | [A] |
| <a id="ref-e-03"></a>E-03 | The Bell — SKT 에이닷 조직 전면 배치, AI 수익화 방점 | [링크](https://m.thebell.co.kr/m/newsview.asp?svccode=04&newskey=202512311210233800102717) | news | 2025-12 | [B] |
| <a id="ref-e-04"></a>E-04 | SK텔레콤 뉴스룸 — 1인 1 AI 에이전트 전략, 에이전틱 AI 시대 | [링크](https://news.sktelecom.com/223253) | IR/발표 | 2026 | [A] |
| <a id="ref-e-05"></a>E-05 | SK텔레콤 뉴스룸 — SKT-NTT Docomo AI-RAN 백서 공동 발간 | [링크](https://news.sktelecom.com/) | IR/발표 | 2026-04-01 | [A] |
| <a id="ref-e-06"></a>E-06 | 이지경제 — KT MWC 2026 에이전틱 AICC 공개 | [링크](https://www.ezyeconomy.com/news/articleView.html?idxno=232748) | news | 2026-03 | [B] |
| <a id="ref-e-07"></a>E-07 | 디지털투데이 — KT AI 보이스피싱 탐지 서비스 2.0 출시 | [링크](https://www.digitaltoday.co.kr/news/articleView.html?idxno=580815) | news | 2026 | [B] |
| <a id="ref-c-01"></a>C-01 | HN Community — Voice AI 개발자 페인포인트 종합 (ChatTTS, Inworld, Kitten 쓰레드) | [링크](https://news.ycombinator.com/item?id=40507039) | community | 2024-2025 | [C] |
