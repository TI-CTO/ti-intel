---
type: weekly-monitor
domain: voice-ai
week: 2026-W15
date: 2026-04-09
l3_count: 8
deep_count: 1
tags:
  - claude-code
  - weekly
created: 2026-04-09
updated: 2026-04-09
---

# 주간 기술 동향: Voice AI (2026-W15)

## Executive Summary

> **이번 주 핵심**: Text-to-Speech (TTS) 품질 경쟁이 사실상 종료 단계에 접어들며 차별화 축이 3방향으로 분기하고 있다. (1) ElevenLabs가 iOS 음악 생성 앱 ElevenMusic을 출시(4/2)하며 종합 Audio AI 플랫폼으로의 전환을 가속하고, (2) OpenAI가 ChatGPT Advanced Voice Mode를 Apple CarPlay에 통합하여 모빌리티 채널을 확보했으며, (3) 오픈소스 진영에서 Fish Audio S2(80언어, Dual-Autoregressive + Reinforcement Learning 정렬)와 Sopro TTS 169M(CPU 실시간, $100 학습비)이 커뮤니티의 높은 주목을 받고 있다. 오픈소스 최고 모델의 Mean Opinion Score (MOS)가 4.6~4.7에 도달하여 상용 최고(4.8)와 격차 0.1~0.2 수준으로 수렴 중이다.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| Speech Generation | Voice Synthesis | 🟡 | [제품출시] ElevenLabs ElevenMusic iOS 앱(4/2, 음악 AI) · [생태계] OpenAI ChatGPT CarPlay 통합 · [기술돌파] Fish Audio S2 오픈소스(80언어, RL 정렬) · [논문] Sopro 169M CPU 실시간 TTS |
| | Voice Cloning | 🟢 | 전주 시그널(Voxtral, McAfee 96%) 이후 소강. Sopro 제로샷 클로닝 관심 지속 |
| Personal Intelligence | Context Action Recommendation | 🟢 | 전주 시그널(Apple Siri 지연, Salesforce Slackbot) 이후 소강. ChatGPT CarPlay 간접 영향 |
| | Persona Plugin | 🟢 | AI 페르소나 시뮬레이션 도구 확산. 구조적 돌파 없음 |
| | Relationship Graph | 🟢 | DeepLearning.AI Agentic Knowledge Graph (KG) 구축 과정 출시. 구조적 변화 없음 |
| Speech Perception & Interaction | Interrupt & Turn-Taking | 🟢 | Transformer 기반 Voice Activity Projection (VAP) 모델 성숙. 구조적 변화 없음 |
| | Emotional Analysis | 🟢 | Foundation Model 기반 Speech Emotion Recognition (SER) 연구 지속. 멀티모달 융합 트렌드 |
| | Context Recognition | 🟢 | ACM Computing Surveys LLM 멀티턴 대화 서베이 발표. 구조적 변화 없음 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
> **태그** : [기술돌파] [제품출시] [경쟁사] [규제] [투자] [논문] [생태계]

---

## 🟢 Quick 요약 (변화 미미)

### Voice Cloning
- 전주(W14~15) 핵심 시그널(Mistral Voxtral TTS 3초 제로샷 클로닝, McAfee Deepfake Detector 96% 정확도) 이후 신규 돌파 없음. Sopro TTS 169M의 제로샷 클로닝 기능이 커뮤니티에서 관심을 받으나 품질 논란 존재. 딥페이크 위협 내러티브 지속 — 2026년이 "구별 불가능 임계점(indistinguishable threshold)"을 넘는 해가 될 것이라는 예측(Fortune). EU AI Act Article 50 투명성 Code of Practice (CoP) 5~6월 확정 예정.

### Context Action Recommendation
- 전주 핵심(Apple Siri iOS 27 이전 불가 확정, Salesforce Slackbot 30개 AI 기능, Anthropic Conway 테스트) 이후 구조적 변화 없음. OpenAI ChatGPT CarPlay 통합이 간접적으로 모빌리티 컨텍스트 액션 영역에 영향을 미치나, 핵심은 Voice Synthesis에 해당. Proactive AI 트렌드 가속 중 — "프롬프트를 기다리지 않고 맥락을 읽어 먼저 행동하는" AI 어시스턴트가 2026년 핵심 차별화 요소로 부상.

### Persona Plugin
- AI 페르소나 시뮬레이션 도구 확산(Xtensio, Jenova AI, Character.AI). 무한 메모리 기반 세션 간 페르소나 일관성 유지 기술 발전. Anthropic Persona Selection Model (PSM) 프레임워크 후속 논의 지속. 구조적 돌파 없음.

### Relationship Graph
- DeepLearning.AI가 "Agentic Knowledge Graph Construction" 과정을 출시하여 에이전트 기반 Knowledge Graph (KG) 자동 구축 방법론을 교육. GraphRAG 프로덕션 성숙(300~320% Return on Investment, ROI 보고). 2026년 오픈소스 KG 구축 도구 Top 3: DeepSeek-R1, Qwen3-235B, GLM-4.5. 구조적 변화 없음.

### Interrupt & Turn-Taking
- Transformer 기반 Voice Activity Projection (VAP) 모델이 턴 감지를 "반응적 음성 유무 판별"에서 "맥락적 예측 문제"로 전환. 진정한 barge-in과 backchannel("응", "그래") 구분이 핵심 과제. AssemblyAI 시맨틱+오디오 결합 접근, LiveKit smart-turn 프로젝트 주목. sub-100ms 레이턴시 기대치 고착. 신규 돌파 없음.

### Emotional Analysis
- Foundation Model 기반 제로샷 Speech Emotion Recognition (SER) 연구 지속. 멀티모달 융합(오디오 + 텍스트 + 화자 정보 + CRM 메타데이터) 접근이 2026년 최강 시스템의 공통 특징. 음성 바이오마커 기반 건강 모니터링(파킨슨, 알츠하이머) 서브마켓 성장(CAGR 37.3%). 구조적 변화 없음.

### Context Recognition
- ACM Computing Surveys에 "LLM 기반 멀티턴 대화 시스템 서베이" 발표. 하이브리드 접근(LLM 자연어 처리 + 명시적 상태 객체 관리)이 프로덕션 표준으로 정착. 2026년까지 신규 앱의 30%+에 자율 에이전트 내장 예측(International Data Corporation, IDC). 구조적 돌파 없음.

---

## 🟡🔴 Deep 심층 분석

### Voice Synthesis — 🟡 주목

#### 이전 대비 변화
- 전주: 플랫폼 확장 + 오픈소스 가속 — ElevenLabs 에이전트 플랫폼 업데이트(MCP Tool Scoping·Video-to-Music), Cartesia Sonic-3 AWS SageMaker 배포, OmniVoice 600+ 언어 논문, Miravoice $6.3M Seed
- 금주: 음악·모빌리티·오픈소스 3중 확장 — ElevenLabs ElevenMusic iOS 출시, OpenAI ChatGPT CarPlay 통합, Sopro TTS 169M·Fish Audio S2 커뮤니티 주목, Google Gemini 2.5 TTS 24언어 감정 강화
- 변화 방향: TTS 품질 경쟁 수렴 (오픈소스 MOS 4.6~4.7 vs. 상용 4.8) → 차별화 축이 "플랫폼 생태계", "멀티모달·모빌리티", "초경량·온디바이스"로 3분화

#### 기술 동향

1. **ElevenLabs ElevenMusic — iOS 음악 생성 앱 출시로 Audio AI 플랫폼 전환 선언(4/2).**
   자연어 프롬프트로 음악을 생성·리믹스하는 독립 앱을 App Store에 출시했다. 무료 7곡/일, Pro $9.99/월(500트랙/월). Suno·Udio가 저작권 소송 이후 레이블과 사후 합의한 것과 달리, Merlin(독립 레이블)·Kobalt Music 출판사와 **사전 라이선스**를 체결한 것이 핵심 차별화 포인트다. CEO Mati Staniszewski는 "AI 오디오 회사로서 음악 확장은 자연스러운 진화"라고 밝혔다. 누적 1,400만 곡 생성, 음성 크리에이터에게 $1,100만+ 지급 이력도 공개. 2월 Series D $500M(Sequoia 주도, $11B 밸류에이션), ARR $330M+. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[E-01]](#ref-e-01)

2. **Google Gemini 2.5 Flash/Pro TTS 업데이트 — 24언어 감정 표현 강화.**
   세 축 개선: (1) 스타일 프롬프트 지시 준수율 대폭 향상, (2) 컨텍스트 기반 속도 제어(흥분 시 가속, 강조 시 감속), (3) 다중 화자 대화에서 캐릭터별 일관된 음성 유지. Flash(저지연)와 Pro(품질) 이원화. LLM 네이티브 TTS 경로를 기존 Cloud TTS와 병행 구축 중. [[G-03]](#ref-g-03)

3. **OpenAI ChatGPT Advanced Voice Mode — Apple CarPlay 통합(3/31).**
   iOS 26.4+ 기기와 CarPlay 지원 차량에서 핸즈프리 음성 대화 가능. Wake Word 미지원(수동 실행), 차량 기능 제어 불가(Apple 제약). Advanced Voice Mode 자체도 억양·속도·공감·풍자 감정 표현이 강화된 상태. 다만 Voice Mode 할루시네이션(광고·잡음 유사 발화) 이슈가 간헐적으로 보고되고 있으며 OpenAI가 조사 중. [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)

4. **Fish Audio S2 오픈소스 — Dual-Autoregressive (Dual-AR) + Reinforcement Learning (RL) 정렬, 80언어.**
   Slow AR(4B, 시간축 의미 코드북)과 Fast AR(400M, 잔여 코드북)의 비대칭 아키텍처. Group Relative Policy Optimization (GRPO) 기반 학습 후 정렬으로 오픈소스 최초 Seed-TTS 초과 Word Error Rate (WER) 달성(중국어 0.54%, 영어 0.99%). EmergentTTS-Eval 81.88% 승률, 1,000만 시간 학습 데이터. 자연어 인라인 태그([whisper in small voice], [professional broadcast tone])로 단어 단위 감정 제어. [[G-06]](#ref-g-06), [[P-01]](#ref-p-01)

5. **Sopro TTS 169M — CPU 실시간, $100 학습비, Hacker News (HN) 트렌딩.**
   WaveNet 스타일 팽창 컨볼루션 + 경량 크로스-어텐션 아키텍처로 Transformer 미채용. CPU RTF 0.05(M3 기준), 스트리밍 TTFA 250ms, 제로샷 음성 복제(3~12초 참조). 학습 비용 약 $100(L40S GPU 단일), Apache 2.0. HN 커뮤니티에서 품질에 대한 엇갈린 평가("CPU 성능 인상적" vs. "프로덕션 품질 미달")와 함께 Kokoro 82M, Chatterbox-TTS와 비교 논의 활발. [[G-07]](#ref-g-07), [[C-01]](#ref-c-01)

6. **Hume AI Octave 2 — 감정 지능 TTS, 문맥 이해 기반 감정 추론.**
   텍스트를 "읽는" 것이 아닌 "이해"하는 LLM 기반 TTS. 풍자→풍자적 발화, 긴박→급박한 발화로 자동 매핑. 11언어, Time-To-First-Byte (TTFB) 200ms 미만(전작 대비 40% 향상), 15초 참조 오디오 음성 복제. Sambanova 전용 칩 배포로 가격 절반, 분당 1센트 미만. 블라인드 테스트에서 ElevenLabs Voice Design 대비 음질 71.6%, 자연도 51.7%, 설명 일치도 57.7% 선호. [[G-08]](#ref-g-08)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | ElevenMusic iOS 앱(4/2), Merlin·Kobalt 사전 라이선스. Series D $500M($11B). ARR $330M+. 누적 1,400만 곡 | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-09]](#ref-g-09) |
| OpenAI | ChatGPT Advanced Voice → CarPlay 통합(3/31). 억양·감정 강화. 할루시네이션 이슈 조사 중 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| Google | Gemini 2.5 Flash/Pro TTS 24언어, 감정·속도·멀티스피커 강화. AI Studio/API 제공 | [[G-03]](#ref-g-03) |
| Hume AI | Octave 2: 감정 추론 TTS, 11언어, TTFB 200ms 미만, Sambanova 파트너십. ElevenLabs 대비 음질 71.6% 선호 | [[G-08]](#ref-g-08) |
| Fish Audio | S2 Pro 오픈소스(3/9): Dual-AR + GRPO RL, 80언어, EmergentTTS 81.88% 승률 | [[G-06]](#ref-g-06), [[P-01]](#ref-p-01) |
| Alibaba (Qwen) | Qwen3-TTS 오픈소스(1월): 10언어, 97ms 스트리밍, WER 1.835% | [[G-10]](#ref-g-10) |
| Cartesia | Sonic-3 AWS SageMaker 배포 유지. 42언어, 90ms. $100M 펀딩(NVIDIA 참여) | [[G-11]](#ref-g-11) |
| Sesame AI | CSM 기반 초사실적 대화 음성 유지. Fala AI로 리브랜딩. 20언어 확장 예정 | [[G-12]](#ref-g-12) |
| Sopro | 169M CPU RTF 0.05, $100 학습비, HN 트렌딩. 품질 논란 존재 | [[G-07]](#ref-g-07), [[C-01]](#ref-c-01) |

#### 시장 시그널

**투자 & M&A**
- ElevenLabs Series D $500M, $11B 밸류에이션(Sequoia 주도, 2026-02). ARR $330M+, IPO 준비 선언 [[G-09]](#ref-g-09)
- PolyAI Series D $86M(2025-12), 기업가치 $750M. NVentures·Zendesk Ventures 참여 [[G-13]](#ref-g-13)
- Voice AI 섹터 2025년 총 $2.1B VC 유입 [[G-13]](#ref-g-13)

**파트너십 & 제휴**
- ElevenLabs + Merlin/Kobalt: 음악 AI 사전 라이선스 — 법적 분쟁 없이 시장 진입하는 새 모델 [[G-02]](#ref-g-02)
- OpenAI + Apple CarPlay: 제3자 대화 AI가 CarPlay에 진입한 첫 사례 [[G-04]](#ref-g-04)
- Hume AI + Sambanova: 전용 추론 칩 배포로 TTS 비용 50% 절감 [[G-08]](#ref-g-08)

**시장 전망**
- AI Voice Agents 세그먼트: 2024년 $2.4B → 2034년 $47.5B(CAGR 34.8%) [추가확인 필요] [[G-14]](#ref-g-14)
- 음성·음성인식 시장 전체: 2024년 $15.46B → 2032년 $81.59B(CAGR 23.1%) [[G-13]](#ref-g-13)
- TTS 품질 격차 수렴: 오픈소스 MOS 4.6~4.7 vs. 상용 4.8, 격차 0.1~0.2 [[G-15]](#ref-g-15)

**연구 동향**
- Fish Audio S2 Technical Report (Liao et al., 2026) — Dual-AR + GRPO RL로 오픈소스 TTS 품질 상한 견인 [[P-01]](#ref-p-01)
- OmniVoice (Zhu et al., 2026) — 600+ 언어 Diffusion Language Model 비자기회귀 TTS [[P-02]](#ref-p-02)
- Voxtral TTS (Mistral AI, 2026) — 4B 오픈웨이트, ElevenLabs 대비 68.4% 승률 [[P-03]](#ref-p-03)

**커뮤니티 시그널**
- Sopro TTS HN 트렌딩: "CPU 실시간 제로샷 클로닝"이 오픈소스 커뮤니티에서 높은 관심. 품질보다 접근성·비용 우선 세그먼트 확인 [[C-01]](#ref-c-01)
- Fish Audio S2 ComfyUI 통합 노드 등장: 이미지 생성 워크플로우와 TTS 결합 실험 활발 [[G-06]](#ref-g-06)

#### 시장 수요 (voice-of-market)

> HN 커뮤니티 쓰레드 3개 + 전문 벤치마크 분석 2건에서 시그널 추출. YouTube 컨퍼런스 영상 미확보.

**고객 페인포인트**
- 파이프라인 전체 레이턴시가 800ms~2s로 자연스러운 대화(목표 300~500ms) 달성 어려움 — 출처: Speechmatics TTS API 비교 분석
- 오픈소스 모델의 할루시네이션·발음 오류 빈발, SSML 없이 숫자/고유명사 제어 불가 — 출처: HN 커뮤니티 (Coqui.ai TTS, Edge TTS)
- 스케일업 시 숨겨진 품질 저하 및 27× 가격 격차(ElevenLabs $0.30 vs. Speechmatics $0.011/1k chars) — 출처: Speechmatics 비교 분석
- Coqui 프로젝트 단종, XTTS 상업 라이선스 제한으로 오픈소스 장기 채택 어려움 — 출처: HN 커뮤니티

**도입 장벽**
- 50+ 언어 지원 표방에도 아시아·동남아 언어 품질이 영어 대비 현저히 낮음 — 출처: HN 커뮤니티 (Edge TTS)
- Health Insurance Portability and Accountability Act (HIPAA)/General Data Protection Regulation (GDPR)/온프레미스 지원 부재로 의료·금융 부문 도입 불가 — 출처: Inworld TTS 벤치마크
- 고품질 모델의 GPU 의존성으로 엣지·저비용 환경 실용화 어려움 — 출처: HN 커뮤니티
- 벤더 API 불안정성(Edge TTS 블로킹, 정책 변경)으로 프로덕션 신뢰성 확보 어려움 — 출처: HN 커뮤니티

**시장 니즈**
- sub-200ms TTFB 실시간 스트리밍 TTS (콜센터·음성 에이전트용) — 출처: Inworld TTS 벤치마크
- SSML 대신 자연어 인스트럭션 기반 감정·운율 제어 — 출처: Speechmatics 비교 분석
- 단일 발화 내 언어 전환(코드스위칭) 지원 — 출처: Google I/O 발표
- CPU 구동 가능한 엣지 경량 모델(Kokoro 82M 방향) — 출처: HN 커뮤니티
- 3~10초 샘플로 상업 이용 가능한 음성 클로닝 — 출처: Inworld TTS 벤치마크

#### 전략적 시사점

**기회**
- 오픈소스 TTS 품질이 상용 수준에 수렴하면서, 자체 TTS 파이프라인 구축 비용이 급격히 하락. Fish Audio S2(Apache 2.0, 80언어)를 기반으로 한국어 최적화 파인튜닝 시 경쟁력 있는 음성 서비스 구축 가능
- 감정 지능 TTS(Hume Octave, Fish S2 인라인 태그)가 상용화 단계에 진입. AI 컨택센터·가상 캐릭터 서비스의 사용자 경험 차별화 요소로 활용 가능
- ElevenLabs의 음악 확장은 음성 크리에이터 생태계 → 음악 크리에이터 생태계로의 플랫폼 확장 모델을 제시. 통신사 음성 서비스의 플랫폼화 전략 참고

**위협**
- TTS 품질 경쟁 수렴으로 TTS 자체가 commodity화. 단순 음성 품질만으로는 차별화 불가능한 시장 환경 도래
- OpenAI ChatGPT CarPlay 통합은 통신사 AI 어시스턴트(SKT 에이닷, KT 지니)의 차량 내 음성 시장 위협. 빅테크의 모빌리티 채널 선점 가속

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 Voice AI 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 에이닷 오토 차량 탑재 | 르노코리아 신형 '필랑트'에 차세대 차량용 AI 에이전트 '에이닷 오토' 최초 적용 | context-action-recommendation | [[E-02]](#ref-e-02) |
| 1인 1 AI 에이전트 전략 | 전 구성원 참여 AX혁신 가속. 비개발직군 포함 본인 업무 특화 AI 에이전트 구축 목표 | persona-plugin | [[E-03]](#ref-e-03) |
| 에이닷 일상 서비스 확대 | 전화 보안(보이스피싱 탐지), 기록·일정 관리, 브리핑(선제적 정보 제공) 기능 강화 | context-action-recommendation | [[E-04]](#ref-e-04) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 삼성닷컴 챗봇 수주·운영 | 삼성전자 온라인몰 '삼성닷컴' 챗봇 서비스 운영 시작(3/27). STT·TTS·콜봇·챗봇 전영역 기술력 보유 | voice-synthesis | [[E-05]](#ref-e-05) |
| AICC 400개 기업 공급 | 삼성전자·대형 금융사 30여개사 포함 400개+ 기업에 AI Contact Center (AICC) 공급. 평일 상담 40% AI 응대 | voice-synthesis | [[E-06]](#ref-e-06) |
| Agentic AICC 전환 | 시나리오 봇을 넘어 자율실행 AI로 진화. Data Platform(RAG), AI Agent, 개인화 마케팅 솔루션 확장 | context-action-recommendation | [[E-07]](#ref-e-07) |

### 시사점
- SKT는 에이닷을 중심으로 차량(르노코리아)·직원(1인 1 에이전트)·일상(브리핑)으로 컨텍스트 범위를 확장하며, OpenAI ChatGPT CarPlay와 직접 경쟁 구도 형성. KT는 삼성닷컴 챗봇 수주로 B2B AICC 시장 지배력을 입증하며 Agentic AICC로의 진화를 가속.

---

## 규제 & 거버넌스

> Voice AI 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| 한국 AI 기본법 (AI 생성 콘텐츠 고지 의무) | 2026-01-22 | 시행 중 |
| EU AI Act Article 50 (합성 콘텐츠 투명성) | 2026-08-02 | D-115 |
| EU AI Code of Practice (AI 생성 콘텐츠 표시) | 2026-05~06 (확정 예정) | D-52~82 |

### 신규 발의 & 가이드라인
- **EU AI Code of Practice 초안 공개 진행 중**: 180건+ 이해관계자 제출 의견 반영. 음성 합성물 포함 AI 생성 콘텐츠에 대해 기계 판독 가능(machine-readable) 형식의 마킹 의무화. 오디오 콘텐츠의 경우 "시작 시 명확하고 눈에 띄는 공개(audible disclaimer)" 방식을 제안 [[G-16]](#ref-g-16)
- **한국 AI 기본법 시행령 입법예고**: 과학기술정보통신부가 기업 혼란 최소화를 위해 규제 적용을 최소 1년 이상 유예 방침. 실제 과태료 부과는 2027년 이후 가능성 [[G-17]](#ref-g-17)

### 시사점
- Voice Cloning·Voice Synthesis 서비스 제공 시 EU AI Act Article 50(합성 콘텐츠 투명성)과 한국 AI 기본법의 AI 생성 표시 의무에 대비 필요. 특히 EU Code of Practice 확정(5~6월)에 따라 오디오 콘텐츠 마킹 기술 표준이 구체화될 예정

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **TTS commodity화와 플랫폼 전략**: TTS 품질 격차 수렴(MOS 0.1~0.2)으로 Voice Synthesis 단독으로는 차별화 불가. ElevenLabs(음악), OpenAI(CarPlay), Google(LLM 네이티브)처럼 **TTS를 플랫폼의 한 레이어로 포지셔닝**하는 전략이 부상. Speech Generation(Voice Synthesis + Voice Cloning)을 Speech Perception(감정 분석, 턴테이킹)과 결합한 **End-to-End 음성 경험** 설계가 향후 경쟁력의 핵심

2. **오픈소스 가속과 Build 옵션 강화**: Fish Audio S2(80언어, RL 정렬, Apache 2.0)와 Sopro 169M(CPU 실시간, $100) 등 오픈소스 옵션이 급격히 성숙. 자체 Voice AI 파이프라인 구축 시 Build 옵션의 실현 가능성이 크게 높아짐. 한국어 특화 파인튜닝 + 감정 제어 커스터마이징 경로 탐색 필요

3. **모빌리티·에이전트 채널 확장**: OpenAI CarPlay + SKT 에이닷 오토로 차량 내 음성 AI 경쟁 본격화. Context Action Recommendation과 Voice Synthesis가 "차량"이라는 새로운 터치포인트에서 교차하며 통합 경험 설계의 중요성 증가

### 후속 조치 제안

- 🟡 Voice Synthesis 심층 평가 → `/wtis standard speech-generation` Go/No-Go 검증 (오픈소스 Build 옵션 실현 가능성)
- 📂 Obsidian 동기화 → `/obsidian-bridge outputs/reports/weekly/2026-04-09_weekly-voice-ai.md weekly`
- 📅 다른 도메인 모니터링 → `/weekly-monitor secure-ai` (수요일 스케줄)

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | TechCrunch — ElevenLabs releases a new AI-powered music-generation app | [링크](https://techcrunch.com/2026/04/02/elevenlabs-releases-a-new-ai-powered-music-generation-app/) | news | 2026-04-02 | [B] |
| <a id="ref-g-02"></a>G-02 | Music Business Worldwide — ElevenLabs launches ElevenMusic iOS app | [링크](https://www.musicbusinessworldwide.com/elevenlabs-launches-elevenmusic-ios-app-taking-on-suno-and-udio-on-mobile/) | news | 2026-04-01 | [B] |
| <a id="ref-g-03"></a>G-03 | Toolnavs — Google upgrades Gemini 2.5 Flash and Pro TTS | [링크](https://toolnavs.com/en/article/940-google-upgrades-gemini-25-flash-and-pro-tts-to-improve-emotional-expression-and) | news | 2026-04 | [B] |
| <a id="ref-g-04"></a>G-04 | MacRumors — OpenAI Brings ChatGPT to CarPlay | [링크](https://www.macrumors.com/2026/03/31/openai-chatgpt-carplay/) | news | 2026-03-31 | [B] |
| <a id="ref-g-05"></a>G-05 | Releasebot — OpenAI Release Notes April 2026 | [링크](https://releasebot.io/updates/openai) | news | 2026-04 | [B] |
| <a id="ref-g-06"></a>G-06 | Fish Audio Blog — Fish Audio Open-Sources S2 | [링크](https://fish.audio/blog/fish-audio-open-sources-s2/) | blog | 2026-03-09 | [B] |
| <a id="ref-g-07"></a>G-07 | GitHub — samuel-vitorino/sopro | [링크](https://github.com/samuel-vitorino/sopro) | blog | 2026-02-04 | [B] |
| <a id="ref-g-08"></a>G-08 | Hume AI Blog — Octave TTS: first TTS that understands what it's saying | [링크](https://www.hume.ai/blog/octave-the-first-text-to-speech-model-that-understands-what-its-saying) | blog | 2025-10 | [A] |
| <a id="ref-g-09"></a>G-09 | TechCrunch — ElevenLabs raises $500M at $11B valuation | [링크](https://techcrunch.com/2026/02/04/elevenlabs-raises-500m-from-sequioia-at-a-11-billion-valuation/) | news | 2026-02-04 | [B] |
| <a id="ref-g-10"></a>G-10 | Alibaba Cloud — Qwen3-TTS Family Open Sourced | [링크](https://www.alibabacloud.com/blog/602826) | blog | 2026-01 | [B] |
| <a id="ref-g-11"></a>G-11 | Cartesia — Sonic-3 AI Voice Model | [링크](https://cartesia.ai/sonic) | blog | 2026 | [B] |
| <a id="ref-g-12"></a>G-12 | TechCrunch — Sesame releases its base AI model | [링크](https://techcrunch.com/2025/03/13/sesame-the-startup-behind-the-viral-virtual-assistant-maya-releases-its-base-ai-model/) | news | 2025-03-13 | [B] |
| <a id="ref-g-13"></a>G-13 | AssemblyAI — Voice AI in 2026: companies and investments | [링크](https://www.assemblyai.com/blog/voice-ai-in-2026-series-1) | news | 2026 | [B] |
| <a id="ref-g-14"></a>G-14 | VoiceAIWrapper — Voice AI Market Analysis 2026 | [링크](https://voiceaiwrapper.com/insights/voice-ai-market-analysis-trends-growth-opportunities) | blog | 2026 | [C] |
| <a id="ref-g-15"></a>G-15 | CodeSOTA — Speech AI Benchmarks 2026: STT & TTS Leaderboard | [링크](https://www.codesota.com/speech) | blog | 2026-04 | [C] |
| <a id="ref-g-16"></a>G-16 | Ashurst — Transparency of AI-generated content: EU's first draft Code of Practice | [링크](https://www.ashurst.com/en/insights/transparency-of-ai-generated-content-the-eu-first-draft-code-of-practice/) | news | 2026 | [B] |
| <a id="ref-g-17"></a>G-17 | 피카부랩스 — AI 기본법 완전 정리: 2026년 시행 | [링크](https://peekaboolabs.ai/blog/ai-basic-law-guide) | blog | 2026 | [B] |
| <a id="ref-e-01"></a>E-01 | ElevenLabs CEO Mati Staniszewski — "AI 오디오 회사로서 음악 확장은 자연스러운 진화" | [링크](https://www.musicbusinessworldwide.com/elevenlabs-launches-elevenmusic-ios-app-taking-on-suno-and-udio-on-mobile/) | IR/발표 | 2026-04-01 | [B] |
| <a id="ref-e-02"></a>E-02 | SK텔레콤 뉴스룸 — 에이닷 오토 차량 탑재 | [링크](https://news.sktelecom.com/219242) | IR/발표 | 2026 | [A] |
| <a id="ref-e-03"></a>E-03 | SK텔레콤 뉴스룸 — 1인 1 AI 에이전트 전략 | [링크](https://news.sktelecom.com/222847) | IR/발표 | 2026 | [A] |
| <a id="ref-e-04"></a>E-04 | SK텔레콤 뉴스룸 — 2026년 에이닷 일상 서비스 | [링크](https://news.sktelecom.com/218051) | IR/발표 | 2026 | [A] |
| <a id="ref-e-05"></a>E-05 | 머니투데이 — 삼성닷컴 챗봇 따낸 KT의 저력 | [링크](https://www.mt.co.kr/tech/2026/04/06/2026040519505332477) | news | 2026-04-06 | [A] |
| <a id="ref-e-06"></a>E-06 | 머니투데이 — KT AI 고객센터 사업 강세 | [링크](https://www.mt.co.kr/tech/2026/04/05/2026040209245423959) | news | 2026-04-05 | [A] |
| <a id="ref-e-07"></a>E-07 | KT Enterprise — Agentic AICC, 자율실행 AI로 | [링크](https://enterprise.kt.com/bt/P_BT_TI_VW_001.do?bbsId=3796&bbsTP=A) | blog | 2026 | [A] |
| <a id="ref-p-01"></a>P-01 | Liao et al. — Fish Audio S2 Technical Report | [링크](https://arxiv.org/abs/2603.08823) | paper | 2026-03-09 | [A] |
| <a id="ref-p-02"></a>P-02 | Zhu et al. — OmniVoice: Omnilingual Zero-Shot TTS | [링크](https://arxiv.org/abs/2604.00688) | paper | 2026-04-01 | [A] |
| <a id="ref-p-03"></a>P-03 | Mistral AI — Voxtral TTS | [링크](https://arxiv.org/abs/2603.25551) | paper | 2026-04-06 | [A] |
| <a id="ref-c-01"></a>C-01 | Hacker News — Sopro TTS: A 169M model with zero-shot voice cloning on CPU | [링크](https://news.ycombinator.com/item?id=46546113) | community | 2026-04 | [C] |
