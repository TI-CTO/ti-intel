---
type: weekly-monitor
domain: voice-ai
week: 2026-W13
date: 2026-03-24
l3_count: 8
deep_count: 4
---

# 주간 기술 동향: Voice AI (2026-W13)

## Executive Summary

> **이번 주 핵심**: 음성 AI 인프라 투자가 $648M+로 폭증하며 "음성 에이전트 인프라 전쟁"이 본격화. ElevenLabs Conversational AI 2.0이 독자 턴테이킹 신경망(95% 인터럽트 감지)으로 플랫폼 수직 통합을 완성하고, 보이스 클로닝은 "구별 불가능 임계점(Indistinguishable Threshold)"을 공식 돌파하며 딥페이크 사기가 미국인 25%에 도달. EU AI Act Article 50 D-131 카운트다운이 산업 전반의 컴플라이언스 압력을 가중시키고 있다.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| Speech Generation | Voice Cloning | 🔴 | "구별 불가능 임계점" 공식 선언. Hiya: 미국인 25% 딥페이크 통화 경험. ElevenLabs Eleven v3 GA(70언어). Pindrop-Zoom 딥페이크 탐지 통합. UN·INTERPOL 음성 클로닝 조직 사기 경고 |
| | Voice Synthesis | 🟡 | Hume TADA 오픈소스(RTF 0.09, 환각 제로). ElevenLabs 11.ai MCP 음성비서 알파. Google Gemini 2.5 TTS GA. Microsoft Dragon HD Omni 700+ 음성 프리뷰. Kitten TTS 25MB 엣지 TTS |
| Speech Perception & Interaction | Interrupt & Turn-Taking | 🟡 | 음성에이전트 인프라 투자 $648M+(LiveKit $100M, ElevenLabs $500M 등). ElevenLabs Conv AI 2.0 독자 턴테이킹 신경망. τ-Voice 벤치마크. Deepgram Flux ~260ms EOT |
| | Emotional Analysis | 🟡 | Hume Octave 2 다국어 감정 TTS(11언어, 200ms). VoxEmo 벤치마크(15언어, 35코퍼스). EU 직장 내 감정 인식 금지 발효. WHO 정신건강 AI 로드맵 |
| | Context Recognition | 🟢 | Conversational AI 채택 critical velocity 도달(Gartner). 구조적 변화 없음 |
| Personal Intelligence | Persona Plugin | 🟢 | Life-long Personalization LLM 연구 지속. 구조적 돌파 없음 |
| | Relationship Graph | 🟢 | LLM-TEXT2KG 2026 워크숍. GraphRAG 산업 표준화 지속. 구조적 변화 없음 |
| | Context Action Recommendation | 🟢 | Apple Siri+Gemini 통합 iOS 26.5 지연 중. Arahi Rahi 프로액티브 비서 출시 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음

---

## 🟢 Quick 요약 (변화 미미)

### Context Recognition
- Gartner에 따르면 Conversational AI 채택이 "critical velocity"에 도달. LLM 기반 멀티턴 대화 시스템이 산업 표준으로 정착 지속 중이나, W12 대비 구조적 돌파구 없음.

### Persona Plugin
- Life-long Personalization of Large Language Model (LLM) 연구가 지속 중. 동적 프로필 적응 트렌드가 이어지나, 이번 주 구조적 돌파 없음.

### Relationship Graph
- LLM-TEXT2KG 2026 워크숍 개최. Nature Scientific Reports에 Knowledge Graph (KG) 구축 논문 게재. GraphRAG 산업 표준화 지속. W12 대비 변화 없음.

### Context Action Recommendation
- Apple Siri + Google Gemini 통합이 iOS 26.5 베타(3/30 예상)로 지연 중. Arahi Rahi 프로액티브 AI 개인 비서 출시. Anthropic Claude 메모리 기능 전체 사용자 롤아웃. 점진적 발전이나 구조적 변화 수준은 아님.

---

## 🟡🔴 Deep 심층 분석

### Voice Cloning — 🔴 긴급

#### 이전 대비 변화
- 전주: ElevenLabs SXSW "1M Voices"($1B), Iconic Marketplace(28명 유명인 라이선스), YouTube 딥페이크 탐지 확대
- 금주: "구별 불가능 임계점" 공식 선언, 딥페이크 통화 25% 도달, Pindrop-Zoom 실시간 탐지 통합, UN·INTERPOL 글로벌 경고
- 변화 방향: 기술 성숙 → 보안 위협 현실화 + 탐지 인프라 구축 가속

#### 기술 동향

1. **"구별 불가능 임계점" 공식 선언 — 인간 탐지율 54%.**
   Fortune/SUNY Buffalo 연구진(Siwei Lyu)이 보이스 클로닝이 "indistinguishable threshold"를 넘었다고 공식 선언. 수초 분량의 오디오만으로 억양·리듬·감정·호흡까지 복제 가능. 인간 탐지율 54%(동전 던지기 수준)로 하락. [[G-01]](#ref-g-01)

2. **Hiya "State of the Call 2026" — 미국인 25% 딥페이크 통화 경험.**
   미국·영국·캐나다·프랑스·독일·스페인 12,000명 대상 조사. 미국인 4명 중 1명이 지난 12개월 내 딥페이크 음성 통화를 경험. 추가 24%는 구별 가능 여부 불확실. 통신사에 대한 규제·금융 책임 요구 급증. [[G-02]](#ref-g-02)

3. **ElevenLabs Eleven v3 GA — 70언어, Audio Tags, 오류율 68%↓.**
   2026-02-02 정식 출시. Audio Tags([whispers], [sighs], [shouts])로 감정 제어. Text to Dialogue API로 멀티스피커 대화 생성. 화학식·전화번호 등 복잡 텍스트 오류율 15.3% → 4.9%(68% 감소). [[G-03]](#ref-g-03)

4. **Pindrop-Zoom 실시간 딥페이크 탐지 통합 (2026-03-12).**
   Pindrop Pulse·Passport·Protect가 Zoom Contact Center에 통합. 패시브 음성 인증 + 실시간 사기 탐지. AI 기반 사기 2025년 대비 1,210% 증가(Pindrop 자체 조사). 금융·헬스케어·통신 대상. [[G-04]](#ref-g-04)

5. **Pindrop Agentic Fraud Investigation 솔루션 발표 (2026-03-17).**
   업계 최초 에이전틱 사기 조사 솔루션. AI 에이전트가 사기 패턴을 자동 탐지·조사·보고. 딥페이크 탐지에서 사기 조사 자동화로 확장. [[G-05]](#ref-g-05)

6. **UN·INTERPOL 글로벌 사기 서밋 비엔나 (2026-03-16~17).**
   UNODC·INTERPOL 공동 개최. 보이스 클로닝·딥페이크가 조직 범죄에 무기화. 다크웹에서 수초 샘플로 음성·얼굴 복제 앱 유통. 글로벌 사기 손실 $442B(Global Anti-Scam Alliance). [[G-06]](#ref-g-06)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | Eleven v3 GA(70언어, Audio Tags). $500M Series D, $11B 밸류에이션(Sequoia 리드). 서울 포함 14개 도시 글로벌 확장 | [[G-03]](#ref-g-03), [[G-07]](#ref-g-07) |
| Pindrop | Zoom Contact Center 딥페이크 탐지 통합(3/12). 에이전틱 사기 조사 솔루션(3/17). 99% 정확도 주장 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| McAfee | Deepfake Detector 2026 업데이트. 96% 정확도, 로컬 디바이스 실행, 3초 이내 플래깅 | [[G-01]](#ref-g-01) |
| Hiya | "State of the Call 2026" 발표(3/1). 미국인 25% 딥페이크 경험. 통신사 책임론 대두 | [[G-02]](#ref-g-02) |

#### 시장 시그널

**투자 & M&A**
- ElevenLabs $500M Series D(Sequoia 리드, a16z·ICONIQ 참여), $11B 밸류에이션. 총 누적 $781M [[G-07]](#ref-g-07)

**시장 전망**
- AI 음성 사기 1,210% 증가(2025, Pindrop). 글로벌 사기 손실 $442B(GASA) [[G-04]](#ref-g-04), [[G-06]](#ref-g-06)
- 미국인 25% 딥페이크 통화 경험, 49% 구별 불가 또는 불확실(Hiya) [[G-02]](#ref-g-02)

**도입 사례**
- Pindrop-Zoom Contact Center 통합: 금융·헬스케어·통신 대상 실시간 딥페이크 탐지 상용 배포 [[G-04]](#ref-g-04)

**연구 동향**
- Fortune/Siwei Lyu: 보이스 클로닝 "indistinguishable threshold" 공식 선언, 인간 탐지율 54% [[G-01]](#ref-g-01)

#### 시장 수요 (voice-of-market)

컨퍼런스 영상에서 수요 시그널을 확인하지 못함.

#### 전략적 시사점

**기회**
- Pindrop-Zoom 모델이 통신사 컨택센터에 직접 적용 가능한 레퍼런스. 자사 AICC에 실시간 딥페이크 탐지 도입 검토
- Hiya 리포트의 "통신사 책임론" 대두: 선제적 보이스피싱 탐지 서비스 강화로 차별화 기회

**위협**
- 인간 탐지율 54%: 고객 교육만으로는 보호 불가, 인프라 레벨 방어가 필수
- EU AI Act Article 50(2026-08-02) 시행까지 D-131: 합성 음성 라벨링 의무화 대비 필요
- $442B 글로벌 사기 손실: 통신사가 "사기 방조" 책임 회피 불가능한 수준

---

### Voice Synthesis — 🟡 주목

#### 이전 대비 변화
- 전주: Big Tech 반격 — Google Gemini 2.5 TTS 멀티스피커+실시간 번역, OpenAI WER 35%↓, Anthropic ElevenLabs OEM 채택
- 금주: 오픈소스 혁신 — Hume TADA(환각 제로, RTF 0.09), Kitten TTS(25MB 엣지). 플랫폼 전쟁 — ElevenLabs 11.ai MCP 음성비서, Google Gemini 2.5 TTS GA, MS Dragon HD Omni
- 변화 방향: "모델 성능 경쟁" → "플랫폼 통합 + 에이전트 연동 + 엣지 배포" 3축으로 분화

#### 기술 동향

1. **Hume AI TADA 오픈소스 — RTF 0.09, 환각 제로, 700초 컨텍스트 (2026-03-10).**
   Text-Acoustic Dual Alignment (TADA): 텍스트와 음성을 1:1 동기화하는 신규 토크나이제이션. Meta Llama 3.2 기반 1B 파라미터. LibriTTSR 1,000+ 샘플에서 환각 0건. 유사 LLM 기반 TTS 대비 5배 이상 빠른 생성. 모델·코드·arXiv 논문 동시 공개. [[G-08]](#ref-g-08)

2. **ElevenLabs 11.ai MCP 음성비서 알파 출시.**
   Model Context Protocol (MCP)를 활용한 음성 우선(voice-first) AI 비서. Google Calendar, Linear, Slack, Perplexity 등 워크플로우 도구 연결. 커스텀 MCP 서버 지원. 태스크 의존성 파악·크로스태스크 컨텍스트 유지. 알파 기간 무료 접근. [[G-09]](#ref-g-09)

3. **Google Gemini 2.5 TTS Flash/Pro GA — 30스피커, 80+ 로케일.**
   자연어 프롬프트로 스타일·억양·속도·감정 세밀 제어. 단일·멀티스피커 합성 모두 지원. Flash(저지연 최적화), Pro(품질 최적화) 이원화. Google AI Studio 및 Vertex AI 제공. [[G-10]](#ref-g-10)

4. **Microsoft Dragon HD Omni 프리뷰 — 700+ 음성, 100+ 스타일.**
   Azure Speech 차세대 TTS. 통합 모델로 700+ 고품질 음성, 150+ 언어, 100+ 스피킹 스타일. Temperature(0.3~1.0)로 표현 변이 제어. 기존 SSML 튜닝 의존도 대폭 감소. [[G-11]](#ref-g-11)

5. **Kitten TTS v0.8 — 25MB CPU 전용 오픈소스 엣지 TTS.**
   ONNX 기반 15M~80M 파라미터(25~80MB). GPU 불필요, CPU 전용 실행. 8개 음성, 24kHz 오디오. Nano(15M, 25MB) 모델로 극저사양 디바이스 배포 가능. [[G-12]](#ref-g-12)

6. **Hume Octave 2 — 감정 TTS, 11언어, 200ms, 50% 가격인하.**
   한국어 포함 11개 언어 지원. 200ms 레이턴시. 기존 대비 50% 가격 인하. 감정 표현 TTS의 상용화 장벽 대폭 낮춤. [[G-13]](#ref-g-13)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Hume AI | TADA 오픈소스(3/10, RTF 0.09, 환각 0). Octave 2 감정 TTS(11언어, 200ms, 50% 가격인하) | [[G-08]](#ref-g-08), [[G-13]](#ref-g-13) |
| ElevenLabs | 11.ai MCP 음성비서 알파. Eleven v3 GA. $500M Series D / $11B 밸류에이션 | [[G-09]](#ref-g-09), [[G-03]](#ref-g-03), [[G-07]](#ref-g-07) |
| Google | Gemini 2.5 TTS Flash/Pro GA(30스피커, 80+ 로케일) | [[G-10]](#ref-g-10) |
| Microsoft | Dragon HD Omni 프리뷰(700+ 음성, 150+ 언어, Temperature 제어) | [[G-11]](#ref-g-11) |
| KittenML | Kitten TTS v0.8(25MB, CPU 전용, 오픈소스 엣지 TTS) | [[G-12]](#ref-g-12) |

#### 시장 시그널

**투자 & M&A**
- ElevenLabs $500M Series D / $11B 밸류에이션(Sequoia 리드). TTS 인프라 기업 역대 최대 규모 [[G-07]](#ref-g-07)

**파트너십 & 제휴**
- ElevenLabs 11.ai: MCP 프로토콜로 Slack·Calendar·Linear 등 엔터프라이즈 도구 직접 연결 [[G-09]](#ref-g-09)

**시장 전망**
- TTS 경쟁 축이 모델 성능 → 플랫폼·에이전트 통합으로 전환. 빅테크(Google, Microsoft) GA 릴리스로 엔터프라이즈 도입 가속

**도입 사례**
- Google Gemini 2.5 TTS: Google AI Studio 및 Vertex AI를 통해 프로덕션 배포 가능 [[G-10]](#ref-g-10)

**연구 동향**
- Hume AI TADA (2026-03-10) — LLM 기반 TTS의 환각 문제를 Text-Acoustic Dual Alignment로 해결. 오픈소스 공개 [[G-08]](#ref-g-08)

#### 시장 수요 (voice-of-market)

컨퍼런스 영상에서 수요 시그널을 확인하지 못함.

#### 전략적 시사점

**기회**
- Hume TADA 오픈소스: 환각 제로 TTS 기술을 자사 음성 서비스에 통합 가능. 한국어 적응 시 품질 검증 필요
- Kitten TTS 25MB: 온디바이스 TTS 파일럿에 즉시 활용 가능. GPU 없는 IoT/웨어러블 시나리오
- Hume Octave 2 한국어 지원: 감정 TTS 한국어 품질 검증 후 AICC 감정 응답에 활용 가능

**위협**
- Google Gemini 2.5 TTS GA + Microsoft Dragon HD Omni: 빅테크 TTS 품질이 전용 TTS 벤더 수준에 도달. 차별화 근거 약화
- ElevenLabs 11.ai가 MCP로 워크플로우 통합 시 "TTS API" → "음성 에이전트 플랫폼"으로 전환. 경쟁 구도 자체가 변화

---

### Interrupt & Turn-Taking — 🟡 주목

#### 이전 대비 변화
- 전주: Full-Duplex-Bench 수치 공개(Gemini 1.3s vs Moshi 0.27s), OpenAI gpt-realtime 정식, LiveKit 한국어 지원
- 금주: 음성에이전트 인프라 투자 $648M+ 폭증. ElevenLabs Conversational AI 2.0 독자 턴테이킹 신경망. τ-Voice 벤치마크로 full-duplex 평가 표준 확장
- 변화 방향: "기술 성숙" → "인프라 투자 폭증 + 엔터프라이즈 배포 가속"

#### 기술 동향

1. **ElevenLabs Conversational AI 2.0 — 독자 턴테이킹 신경망, 95% 인터럽트 감지.**
   통합 Retrieval-Augmented Generation (RAG) 내장. 텍스트·음성·멀티모달 에이전트 통합 정의. Eleven v3 Conversational 모델 탑재. 독자 턴테이킹 신경망으로 95% 인터럽트 정확 감지. [[G-14]](#ref-g-14)

2. **τ-Voice 벤치마크 — Full-duplex 음성 에이전트 실환경 평가 (arXiv 2603.13686).**
   Sierra Research(Ray et al.). τ²-bench를 음성으로 확장. 복잡 멀티턴 대화 + 도메인 정책 준수 + 환경 인터랙션 통합 평가. 다양한 억양·소음 환경·턴테이킹 다이나믹스를 포함한 제어 가능한 음성 사용자 시뮬레이터. [[P-01]](#ref-p-01)

3. **Huawei 차세대 Voice Virtual Agent — MWC 2026 (2026-03-02).**
   Artificial Intelligence Contact Center (AICC) 차세대 음성 에이전트. 높은 비즈니스 프로세스 준수, 정밀 인텐트 인식, 도구 호출, 멀티턴 대화 "폐쇄 루프" 문제 해결. 자기해결률 20% 향상 주장. [[G-15]](#ref-g-15)

4. **Deepgram Flux — 모델 통합 End-of-Turn 감지, ~260ms.**
   Nova-3 수준 정확도 유지. 설정 가능한 턴테이킹 다이나믹스. 음성 에이전트 파이프라인 최적화. ElevenLabs Scribe v2 Realtime과 함께 최저 end-of-speech 레이턴시. [[G-16]](#ref-g-16)

5. **Grok Voice Mode 대폭 업그레이드 (2026-03).**
   xAI, 신규 Text-to-Speech API 출시(3/16). 실시간 음성-텍스트 변환 정확도 향상. 음성 대화 내 첨부 파일 지원. [[G-17]](#ref-g-17)

6. **CrescitAI AI Voice Agent 출시 (2026-03-20).**
   모든 통화 즉시 응답, 실시간 리드 검증, 자동 예약. 24시간 운영 SMB 대상. IVR 대체 트렌드의 SMB 확산 사례. [[G-18]](#ref-g-18)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | Conversational AI 2.0: 독자 턴테이킹 신경망(95% 인터럽트), 통합 RAG, 멀티모달 에이전트. $500M/$11B | [[G-14]](#ref-g-14), [[G-07]](#ref-g-07) |
| LiveKit | $100M Series C / $1B 유니콘(Index 리드, Salesforce·Altimeter 참여). OpenAI·xAI·Tesla 고객사 | [[G-19]](#ref-g-19) |
| Synthflow | $20M Series A(Accel 리드). No-code 음성 에이전트 플랫폼. 엔터프라이즈 확장 | [[G-20]](#ref-g-20) |
| Newo.ai | $25M Series A. 15,000+ AI 에이전트 생성. SMB 프론트데스크 자동화. 200+ 파트너 | [[G-21]](#ref-g-21) |
| Deepgram | Flux: ~260ms EOT 감지. 통신사 배포 확대(Telnyx 등) | [[G-16]](#ref-g-16) |
| Huawei | MWC 2026: AICC 차세대 음성 에이전트. 자기해결률 20%↑ | [[G-15]](#ref-g-15) |
| xAI | Grok Voice Mode 업그레이드: 신규 TTS API, 음성 대화 첨부 파일 지원 | [[G-17]](#ref-g-17) |

#### 시장 시그널

**투자 & M&A**
- 음성 에이전트 인프라 투자 $648M+: LiveKit $100M/$1B, ElevenLabs $500M/$11B, Synthflow $20M, Newo.ai $25M, Hamming.ai $3.8M [[G-19]](#ref-g-19), [[G-07]](#ref-g-07), [[G-20]](#ref-g-20), [[G-21]](#ref-g-21), [[G-22]](#ref-g-22)

**시장 전망**
- Gartner: 2026년 Conversational AI가 컨택센터 에이전트 인건비 $80B 절감 예측
- AI 음성 에이전트 배포 기업: Average Handle Time (AHT) 40~60% 감소(Gartner 컨택센터 리서치)

**도입 사례**
- Huawei AICC: MWC 2026에서 차세대 음성 에이전트 시연, end-to-end 폐쇄 루프 문제 해결 [[G-15]](#ref-g-15)
- CrescitAI: SMB 대상 AI 음성 에이전트 상용 출시(3/20) [[G-18]](#ref-g-18)

**연구 동향**
- τ-Voice (Ray et al., arXiv 2603.13686) — Full-duplex 음성 에이전트의 실환경 벤치마크. 태스크 완료 + 대화 다이나믹스 통합 평가 [[P-01]](#ref-p-01)

#### 시장 수요 (voice-of-market)

컨퍼런스 영상에서 수요 시그널을 확인하지 못함.

#### 전략적 시사점

**기회**
- $648M+ 투자 폭증이 음성 에이전트 인프라 성숙 가속화. 자사 AICC에 LiveKit/Deepgram 인프라 도입으로 빠른 음성 에이전트 구축 가능
- ElevenLabs Conv AI 2.0의 통합 RAG + 턴테이킹: 엔터프라이즈 음성 에이전트 레퍼런스 아키텍처
- Hamming.ai($3.8M): 음성 에이전트 QA/테스팅 전문 도구 등장. 배포 전 품질 보증 체계 구축 가능

**위협**
- Huawei AICC가 통신사 채널에서 직접 경쟁. SKT·KT 플랫폼 전략에 변수
- SMB 시장까지 AI 음성 에이전트 확산(CrescitAI, Newo): IVR 대체가 가속되면 통신사 부가서비스 수익 구조 변화
- ElevenLabs의 $11B 밸류에이션과 14개 도시 글로벌 확장(서울 포함): 국내 시장 직접 진입 가능성

---

### Emotional Analysis — 🟡 주목

#### 이전 대비 변화
- 전주: Foundation Model zero-shot SER 공식화(Nature npj AI), MME-Emotion ICLR 2026(최고 39.3%), Hume AI EVI 3 출시
- 금주: Hume Octave 2 다국어 감정 TTS(11언어, 200ms). VoxEmo 벤치마크(15언어, 35코퍼스). EU 직장 내 감정 인식 금지 발효. WHO 정신건강 AI 로드맵(3/20)
- 변화 방향: 감정 AI가 "연구 → 규제·윤리 프레임워크" 단계로 이동. 기술은 점진 발전, 거버넌스 가속

#### 기술 동향

1. **Hume Octave 2 — 다국어 감정 TTS, 11언어, 200ms, 50% 가격인하.**
   한국어 포함 11개 언어에서 감정 표현 TTS 지원. 200ms 레이턴시로 실시간 대화 적용 가능. 가격 50% 인하로 상용화 접근성 대폭 향상. [[G-13]](#ref-g-13)

2. **VoxEmo 벤치마크 — 15언어, 35코퍼스 SER 평가 표준 (arXiv 2603.08936).**
   Speech LLM 기반 Speech Emotion Recognition (SER)의 표준 평가 프레임워크. 분포 인식(soft-label) 프로토콜 + 프롬프트 앙상블 전략으로 어노테이터 불일치 모사. Zero-shot Speech LLM은 hard-label 정확도에서 지도학습 기준선에 미달하지만, 인간 주관적 분포와 고유한 정렬 보임. [[P-02]](#ref-p-02)

3. **ElevenLabs Japan — 고객 폭언(Customer Harassment) 감정 AI 솔루션.**
   일본 시장 특화. 고객 통화 중 감정 자동 분석으로 폭언·위협 실시간 감지. AICC 상담원 보호 및 에스컬레이션 자동화. [[G-23]](#ref-g-23)

4. **Microsoft DragonHD — 감정 자동 감지, 실시간 톤 조절.**
   Dragon HD Omni에 감정 큐 자동 감지 기능 포함. 대화 맥락에 따라 실시간 톤 조절. TTS와 감정 분석의 통합 트렌드. [[G-11]](#ref-g-11)

5. **WHO 정신건강 AI 로드맵 발표 (2026-03-20).**
   30+ 국제 전문가 참여 워크숍. 핵심 권고: (1) 생성 AI 사용을 공중 정신건강 우려로 인정, (2) AI 솔루션 영향 평가에 정신건강 통합, (3) 정신건강 AI 도구는 전문가·경험자와 공동 설계 필수. Collaborating Centres on AI for Health 컨소시엄 구축 중. [[G-24]](#ref-g-24)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Hume AI | Octave 2 감정 TTS(11언어, 200ms, 50% 가격인하). TADA 오픈소스(3/10) | [[G-13]](#ref-g-13), [[G-08]](#ref-g-08) |
| ElevenLabs | Japan 고객 폭언 감정 AI 솔루션. Eleven v3 감정 제어 Audio Tags | [[G-23]](#ref-g-23), [[G-03]](#ref-g-03) |
| Microsoft | Dragon HD Omni: 감정 큐 자동 감지, 실시간 톤 조절 | [[G-11]](#ref-g-11) |
| WHO | 정신건강 AI 로드맵(3/20). AI for Health 컨소시엄 구축 | [[G-24]](#ref-g-24) |

#### 시장 시그널

**시장 전망**
- 감정 AI 시장: $5.7B(2023) → $38.5B(2035), CAGR 20.9% (Roots Analysis, 전주 기준 유지)
- Hume Octave 2의 50% 가격인하: 감정 TTS 상용화 임계점 도달 시그널

**도입 사례**
- ElevenLabs Japan: 고객 폭언 감정 AI 솔루션 — 일본 AICC 시장 실도입 [[G-23]](#ref-g-23)

**연구 동향**
- VoxEmo (arXiv 2603.08936) — 15언어, 35코퍼스 SER 벤치마크. Speech LLM zero-shot이 인간 주관 분포와 정렬 [[P-02]](#ref-p-02)
- How Attention Shapes Emotion (arXiv 2603.15120) — SER에서 어텐션 메커니즘 비교 연구 [[P-03]](#ref-p-03)

#### 시장 수요 (voice-of-market)

컨퍼런스 영상에서 수요 시그널을 확인하지 못함.

#### 전략적 시사점

**기회**
- Hume Octave 2 한국어 지원 + 50% 가격인하: AICC 감정 응답 파일럿 비용 대폭 절감
- ElevenLabs Japan 고객 폭언 솔루션: 국내 AICC 상담원 보호에 직접 적용 가능한 레퍼런스
- WHO 로드맵: 음성 바이오마커 기반 정신건강 서비스의 글로벌 표준 프레임워크 형성

**위협**
- EU AI Act Article 5: 직장 내 감정 인식 금지 발효(2025-02). 국내 규제 확산 시 AICC 감정 분석 서비스 제한 가능
- VoxEmo 결과: zero-shot SER이 지도학습 미달 → 프로덕션 배포 시 품질 보증 리스크 상존
- Microsoft Dragon HD의 감정 감지 통합: TTS + 감정 분석 번들링이 독립 감정 AI API 차별화 근거 약화

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 Voice AI 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| A.auto(에이닷 오토) 차량용 AI 에이전트 | 르노코리아 필랑트에 탑재. A.X 4.0 한국어 특화 LLM 기반. 운행 패턴 분석·선제 제안·에어컨/창문 음성 제어. 타 브랜드 확장 계획 | context-action-recommendation, interrupt-turn-taking | [[E-01]](#ref-e-01) |
| MWC 2026 익시오 확장 (전주 연속) | "음성이 다시 사람을 연결하는 본질적 수단" — 스마트안경·자율주행차·휴머노이드 연결 | context-recognition | [[E-02]](#ref-e-02) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| AI 보이스피싱 탐지 2.0 운영 성과 | 화자인식 + 딥보이스(합성음성) 탐지 통합. 탐지 정확도 93%+(4분기). 2025년 약 1,300억원 피해 예방 | voice-cloning | [[E-03]](#ref-e-03) |
| 6G = AI 인프라 전략 (전주 연속) | MWC 2026에서 6G를 'AI 인프라'로 재정의 | (L3 밖) | [[E-02]](#ref-e-02) |

### 시사점
- SKT A.auto는 차량 내 음성 에이전트를 통해 Voice AI를 "모바일 밖"으로 확장하는 전략. Context Action Recommendation + Interrupt & Turn-Taking 기술의 실차 적용 사례. 타 브랜드 확장 시 생태계 효과.
- KT AI 보이스피싱 탐지 2.0의 93%+ 정확도와 1,300억원 피해 예방은 국내 통신사 음성 보안의 레퍼런스. Pindrop-Zoom 모델(99% 주장)과 비교 시 정확도 갭 존재.

---

## 규제 & 거버넌스

> Voice AI 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| 한국 AI 기본법 Article 31 (AI 생성 콘텐츠 표시 의무) | 2026-01-22 | 시행 중 |
| EU AI Act Article 5 (직장 내 감정 인식 금지) | 2025-02-02 | 시행 중 |
| EU AI Act Article 50 (합성 콘텐츠 투명성·라벨링) | 2026-08-02 | D-131 |

### 신규 발의 & 가이드라인
- **EU AI Act Article 50 Code of Practice 2차 초안** — 2026년 3월 중 공개 예정, 최종본 6월 예상. 합성 오디오 라벨링 실무 가이드라인 구체화 중 [[G-25]](#ref-g-25)
- **WHO 정신건강 AI 로드맵 (2026-03-20)** — 생성 AI를 공중 정신건강 우려로 인정. 감정 의존 방지·청소년 보호 권고. AI for Health 컨소시엄 구축 [[G-24]](#ref-g-24)
- **UN·INTERPOL 글로벌 사기 서밋 비엔나 선언 (2026-03-16~17)** — 음성 클로닝·딥페이크 조직 범죄 무기화 경고. 글로벌 사기 손실 $442B [[G-06]](#ref-g-06)

### 시사점
- EU AI Act Article 50 D-131: 합성 음성 라벨링 의무화가 131일 후 시행. TTS/Voice Cloning 서비스에 기술적 워터마킹·메타데이터 삽입 필수. 코드 오브 프랙티스 최종본(6월)에 맞춰 구현 계획 수립 필요.
- 한국 AI 기본법 Article 31 이미 시행 중: 합성 음성이 실제와 구별 불가능할 경우 AI 생성 표시 의무. 자사 TTS/음성 서비스의 컴플라이언스 현황 점검 필요.

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **"음성 에이전트 인프라 전쟁"이 W13의 지배적 메타 트렌드.** $648M+ 투자(LiveKit $100M, ElevenLabs $500M, Synthflow $20M, Newo $25M, Hamming $3.8M)가 음성 에이전트 스택 전 계층에 몰리고 있다. 인프라(LiveKit) → 플랫폼(ElevenLabs Conv AI 2.0) → 수직 SaaS(Synthflow, Newo, CrescitAI) → QA(Hamming)까지 생태계가 완성되는 양상.

2. **ElevenLabs의 수직 통합이 W13에 정점에 도달.** $500M/$11B 펀딩 + Eleven v3 GA + Conversational AI 2.0 + 11.ai MCP 음성비서 + Japan 감정 AI. Voice Cloning·Synthesis·Turn-Taking·Emotional Analysis 전 영역을 관통하는 단일 플랫폼으로 자리잡음. 서울 포함 14개 도시 확장은 국내 시장 직접 진입 시그널.

3. **보이스 클로닝의 "구별 불가능 임계점" 돌파가 규제·보안·사업 모든 면에서 임팩트.** 인간 탐지율 54% → 인프라 레벨 방어 필수. EU AI Act D-131 + 한국 AI 기본법 시행 중 + UN/INTERPOL 경고가 동시에 수렴. 통신사는 "사기 방조" 책임론에서 자유로울 수 없는 상황.

4. **오픈소스 TTS의 엣지 진출 가속.** Hume TADA(환각 제로, RTF 0.09)와 Kitten TTS(25MB, CPU 전용)가 동시 등장. 클라우드 의존 없는 온디바이스 TTS가 현실적 옵션으로 부상. SKT A.auto 같은 차량·IoT 시나리오에서 직접 활용 가능.

### 후속 조치 제안

- 🔴 Voice Cloning 보안 대응: Pindrop-Zoom 모델 참조하여 자사 AICC에 실시간 딥페이크 탐지 도입 검토 → `/wtis standard speech-generation` Go/No-Go 검증
- 🔴 합성 음성 컴플라이언스: EU AI Act Article 50(D-131) + 한국 AI 기본법 Article 31 대응. 자사 TTS 서비스 워터마킹·라벨링 구현 계획 수립
- 🟡 ElevenLabs 국내 진입 모니터링: 서울 오피스 설립 + 일본 시장 진출 → 한국 시장 직접 진입 시나리오 분석
- 🟡 온디바이스 TTS PoC: Kitten TTS(25MB) 또는 TADA(오픈소스)를 활용한 차량·웨어러블 시나리오 파일럿

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Fortune — Voice cloning crossed indistinguishable threshold (Siwei Lyu) | [링크](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/) | news | 2025-12-27 | [B] |
| <a id="ref-g-02"></a>G-02 | Hiya — State of the Call 2026: 1 in 4 Americans deepfake voice call | [링크](https://www.businesswire.com/news/home/20260301082723/en/State-of-the-Call-2026-AI-Deepfake-Voice-Calls-Hit-1-in-4-Americans-as-Consumers-Say-Scammers-Are-Beating-Mobile-Network-Operators-2-to-1) | report | 2026-03-01 | [A] |
| <a id="ref-g-03"></a>G-03 | ElevenLabs Blog — Eleven v3: Most Expressive AI TTS Model | [링크](https://elevenlabs.io/blog/eleven-v3) | blog | 2026-02-02 | [A] |
| <a id="ref-g-04"></a>G-04 | GlobeNewsWire — Pindrop Zoom Integration Real-Time Deepfake Detection | [링크](https://www.globenewswire.com/news-release/2026/03/12/3254709/0/en/Pindrop-Zoom-Integration-Embeds-Real-Time-Deepfake-Detection-and-Identity-Verification-in-Zoom-Contact-Center.html) | press | 2026-03-12 | [A] |
| <a id="ref-g-05"></a>G-05 | GlobeNewsWire — Pindrop Agentic Fraud Investigation Solution | [링크](https://www.globenewswire.com/news-release/2026/03/17/3257231/0/en/Pindrop-Unveils-First-Agentic-Fraud-Investigation-Solution-to-Combat-Surging-AI-Driven-Fraud.html) | press | 2026-03-17 | [A] |
| <a id="ref-g-06"></a>G-06 | UN News — Deepfakes, voice cloning: global wake-up call to organised fraud | [링크](https://news.un.org/en/story/2026/03/1167144) | news | 2026-03 | [A] |
| <a id="ref-g-07"></a>G-07 | TechCrunch — ElevenLabs raises $500M from Sequoia at $11B valuation | [링크](https://techcrunch.com/2026/02/04/elevenlabs-raises-500m-from-sequioia-at-a-11-billion-valuation/) | news | 2026-02-04 | [B] |
| <a id="ref-g-08"></a>G-08 | Hume AI Blog — Opensourcing TADA: Fast Reliable Speech Generation | [링크](https://www.hume.ai/blog/opensource-tada) | blog | 2026-03-10 | [A] |
| <a id="ref-g-09"></a>G-09 | ElevenLabs Blog — Introducing 11.ai Personal AI Voice Assistants | [링크](https://elevenlabs.io/blog/introducing-11ai) | blog | 2026-03 | [A] |
| <a id="ref-g-10"></a>G-10 | Google Blog — Gemini 2.5 Text-to-Speech model updates | [링크](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-2-5-text-to-speech/) | blog | 2026-03 | [A] |
| <a id="ref-g-11"></a>G-11 | Microsoft Tech Community — Dragon HD Omni Azure Speech Preview | [링크](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-dragon-hd-omni-azure-speech-new-voice-type-now-in-preview-via-micros/4481288) | blog | 2026-01 | [A] |
| <a id="ref-g-12"></a>G-12 | GitHub — KittenML/KittenTTS: State-of-the-art TTS under 25MB | [링크](https://github.com/KittenML/KittenTTS) | code | 2026-02 | [B] |
| <a id="ref-g-13"></a>G-13 | Hume AI — Octave 2 multilingual emotional TTS | [링크](https://www.hume.ai/blog/opensource-tada) | blog | 2026-03 | [A] |
| <a id="ref-g-14"></a>G-14 | ElevenLabs Blog — Conversational AI 2.0 voice agents now live | [링크](https://elevenlabs.io/blog/conversational-ai-2-0) | blog | 2026-03 | [A] |
| <a id="ref-g-15"></a>G-15 | Huawei — Next-Gen Voice Virtual Agents for AICC (MWC 2026) | [링크](https://www.huawei.com/en/news/2026/3/mwc-voice-interaction-aicc) | IR/발표 | 2026-03-02 | [A] |
| <a id="ref-g-16"></a>G-16 | Deepgram — Best Speech-to-Text APIs in 2026 (Flux) | [링크](https://deepgram.com/learn/best-speech-to-text-apis-2026) | blog | 2026 | [B] |
| <a id="ref-g-17"></a>G-17 | BluTrumpet — Grok Voice Mode March 2026 Update | [링크](https://www.blutrumpet.com/post/grok-voice-mode-update-march-2026) | news | 2026-03 | [C] |
| <a id="ref-g-18"></a>G-18 | GlobeNewsWire — CrescitAI AI Voice Agents Launch | [링크](https://www.globenewswire.com/news-release/2026/03/20/3259880/0/en/CrescitAI-Unveils-Revolutionary-AI-Voice-Agents-That-Never-Miss-a-Call.html) | press | 2026-03-20 | [B] |
| <a id="ref-g-19"></a>G-19 | TechCrunch — LiveKit $100M Series C, $1B valuation | [링크](https://techcrunch.com/2026/01/22/voice-ai-engine-and-openai-partner-livekit-hits-1b-valuation/) | news | 2026-01-22 | [B] |
| <a id="ref-g-20"></a>G-20 | Synthflow — $20M Series A for AI voice agents | [링크](https://synthflow.ai/news/synthflow-raises-20m-series-a) | press | 2026 | [B] |
| <a id="ref-g-21"></a>G-21 | SiliconANGLE — Newo $25M Series A, AI receptionists | [링크](https://siliconangle.com/2026/02/10/newo-lands-25m-bring-production-ready-ai-receptionists-small-businesses/) | news | 2026-02-10 | [B] |
| <a id="ref-g-22"></a>G-22 | Hamming AI Blog — $3.8M seed for voice agent testing | [링크](https://hamming.ai/blog/hamming-ai-seed-funding-to-make-voice-agents-more-reliable) | blog | 2026 | [B] |
| <a id="ref-g-23"></a>G-23 | ElevenLabs — Japan customer harassment emotional AI solution | [링크](https://elevenlabs.io/blog) | blog | 2026-03 | [B] |
| <a id="ref-g-24"></a>G-24 | WHO — Towards responsible AI for mental health and well-being | [링크](https://www.who.int/news/item/20-03-2026-towards-responsible-ai-for-mental-health-and-well-being--experts-chart-a-way-forward) | report | 2026-03-20 | [A] |
| <a id="ref-g-25"></a>G-25 | EU AI Act — Article 50 Transparency Obligations | [링크](https://artificialintelligenceact.eu/article/50/) | regulation | 2024 | [A] |
| <a id="ref-e-01"></a>E-01 | SKT 뉴스룸 — 에이닷 오토 차세대 차량용 AI 에이전트 | [링크](https://news.sktelecom.com/219242) | IR/발표 | 2026-01 | [A] |
| <a id="ref-e-02"></a>E-02 | WithNews — 통신사 AI 인프라 전쟁 MWC 2026 | [링크](https://car.withnews.kr/economy/telecom-companies-ai-infrastructure-war-mwc-2026) | news | 2026-03 | [B] |
| <a id="ref-e-03"></a>E-03 | 디지털투데이 — KT AI 보이스피싱 탐지 서비스 2.0 | [링크](https://www.digitaltoday.co.kr/news/articleView.html?idxno=580815) | news | 2025-07 | [B] |
| <a id="ref-p-01"></a>P-01 | Ray et al. — τ-Voice: Benchmarking Full-Duplex Voice Agents (arXiv 2603.13686) | [링크](https://arxiv.org/abs/2603.13686) | paper | 2026-03 | [A] |
| <a id="ref-p-02"></a>P-02 | VoxEmo: Benchmarking SER with Speech LLMs (arXiv 2603.08936) | [링크](https://arxiv.org/abs/2603.08936) | paper | 2026-03-09 | [A] |
| <a id="ref-p-03"></a>P-03 | How Attention Shapes Emotion: SER Attention Mechanisms (arXiv 2603.15120) | [링크](https://arxiv.org/abs/2603.15120) | paper | 2026-03 | [A] |
