---
type: weekly-monitor
domain: voice-ai
week: 2026-W11
date: 2026-03-11
l3_count: 8
deep_count: 4
---

# 주간 기술 동향: Voice AI (2026-W11)

## Executive Summary

| 세부기술 | 신호 | 핵심 내용 | 분석 |
|----------|------|----------|------|
| Voice Cloning | 🔴 | ElevenLabs $500M Series D ($11B), Deutsche Telekom 망 AI 통합, Qwen3-TTS 오픈소스 경쟁 | Deep |
| Voice Synthesis | 🔴 | 오픈소스 TTS 폭발 (Qwen3-TTS, Kani-TTS-2, Orpheus), 네이버 한국어 MOS 4.22/5 — 자체 구축 전략 재검토 필요 | Deep |
| Emotional Analysis | 🟡 | Google DeepMind Hume AI acqui-hire, 마고 CES 2026 감정인식 데모 | Deep |
| Interrupt & Turn-Taking | 🟡 | Full-duplex 주류화, NVIDIA PersonaPlex 170ms 단일 Transformer, 시맨틱 턴 감지 확산 | Deep |
| Context Recognition | 🟢 | LLM 멀티턴 대화 연구 지속, 특이 돌파구 없음 | Quick |
| Persona Plugin | 🟢 | PersonaKG/PersonaAgent 점진 발전 | Quick |
| Relationship Graph | 🟢 | GraphRAG 트렌드 지속 | Quick |
| Context Action Recommendation | 🟢 | 프로액티브 AI 트렌드 확산, 특별한 돌파 없음 | Quick |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
>
> **분석** : Deep = 심층 리서치 수행 | Quick = 1줄 요약만

※ Voice AI 첫 실행 — 이전 주 비교 데이터 없음.

---

## 🟢 Quick 요약 (변화 미미)

### Context Recognition
- LLM 기반 멀티턴 대화 시스템 연구 지속. ACM Computing Surveys에 LLM Multi-turn Dialogue 서베이 게재.
- 70% 고객 서비스 상호작용이 멀티턴 필요 (Sendbird 조사). 장문 컨텍스트에서 모델 성능 저하 문제는 여전한 과제.

### Persona Plugin
- 전주 스냅샷: PersonaKG(상식 지식그래프) + PersonaAgent(GraphRAG 기반 개인화) 프레임워크 진전.
- 이번 주 추가 시그널 없음. AI 페르소나의 실시간 업데이트·동적 적응이 2026년 핵심 트렌드로 유지.

### Relationship Graph
- GraphRAG가 2026년 AI 워크플로우의 핵심 인프라로 자리매김. Knowledge Graph Conference 2026 (Cornell Tech, NYC) 개최 예정.
- Neo4j, PuppyGraph 등 그래프 DB 플랫폼이 AI-native 지식 시스템 백본으로 포지셔닝.

### Context Action Recommendation
- Lenovo Qira 개인 AI 에이전트(CES 2026) — 디바이스 간 컨텍스트 인식 지원.
- 프로액티브 AI가 "프롬프트 너머"로 이동하는 트렌드 확산. Google Project Astra 연구 지속.

---

## 🔴 Deep 심층 분석

### Voice Cloning — 🔴 긴급

#### 기술 동향

1. **Qwen3-TTS 오픈소스 공개 — 3초 보이스 클로닝, Apache 2.0, ElevenLabs 능가 주장.**
   Alibaba Cloud Qwen팀이 0.6B~1.7B 파라미터 TTS 시리즈를 Apache 2.0으로 공개. 97ms 초저지연 이중 트랙 스트리밍, 10개 언어(한국어 포함) 지원. 블라인드 평가에서 MiniMax·ElevenLabs·SeedTTS 대비 음성 품질·화자 유사도 우위 주장. [[G-01]](#ref-g-01)

2. **Resemble AI Chatterbox 오픈소스 — MIT 라이선스, 감정 과장 제어, 100만 다운로드.**
   오픈소스 TTS 최초 감정 과장(emotion exaggeration) 제어 탑재. 23개 언어, 내장 워터마킹으로 AI 생성 음성 식별. HuggingFace 100만 다운로드·GitHub 11,000+ 스타. [[G-02]](#ref-g-02)

3. **ElevenLabs Conversational AI 2.0 — 자연스러운 턴테이킹 + HIPAA 준수.**
   최신 턴테이킹 모델로 망설임·필러 단어 실시간 분석. RAG 내장, 배치 콜, 멀티모달 처리 지원. HIPAA 준수 및 EU 데이터 레지던시로 엔터프라이즈 시장 정조준. [[G-03]](#ref-g-03)

4. **ElevenLabs 11.ai 알파 — MCP 기반 음성 우선 AI 개인 비서.**
   Model Context Protocol로 Google Calendar·Slack·Salesforce 등 외부 도구 실시간 연동. 5,000개 이상 사전 제작 음성 + 커스텀 클로닝. [[G-04]](#ref-g-04)

5. **Microsoft Azure Personal Voice DragonV2.1Neural — 100개 언어 제로샷 TTS.**
   수 초 샘플만으로 보이스 복제, 100개 언어 생성. 강화된 운율 안정성, 2025-07 GA. [[G-05]](#ref-g-05)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | Series D $500M ($11B 밸류에이션, Sequoia 리드). ARR $330M+. Conversational AI 2.0, 11.ai, Deutsche Telekom 파트너십 동시 진행 | [[G-06]](#ref-g-06) |
| Deutsche Telekom | MWC 2026 "Magenta AI Call Assistant" 세계 최초 공개. 50개 언어 실시간 통역, 앱 없이 "Hey Magenta" 호출 | [[G-07]](#ref-g-07), [[G-08]](#ref-g-08) |
| Alibaba (Qwen) | Qwen3-TTS Apache 2.0 오픈소스. 0.6B~1.7B, 3초 클로닝, 97ms 지연 | [[G-01]](#ref-g-01) |
| Resemble AI | Chatterbox MIT 오픈소스. 감정 제어, 23개 언어, 워터마킹 내장 | [[G-02]](#ref-g-02) |
| Google | NotebookLM 보이스 클로닝 소송 피소 (NPR David Greene). 법의학 53~60% 신뢰도 일치 | [[G-09]](#ref-g-09) |
| Amazon | Alexa+ 미국 전역 무료 공개 (2026-02). 보이스 클로닝 기능은 미출시 | [[G-10]](#ref-g-10) |
| 마고(MAGO) | Audion 플랫폼 — STT·화자분리·감정분석 미들웨어. 보이스 클로닝보다 실시간 감정인식에 집중 | [[G-11]](#ref-g-11) |
| 네이버 | CLOVA TTS Premium 운영. HyperCLOVA X 멀티모달 확장 계획. 한국어 보이스 클로닝 제품화 미확인 | [[G-12]](#ref-g-12) |
| Play.ht | 2025-12-31 서비스 종료. 경쟁 압박으로 시장 재편 진행 | [[G-13]](#ref-g-13) |

#### 시장 시그널
- 글로벌 보이스 클로닝 시장: 2024년 $2.7B → 2030년 $10.8B, CAGR 26.2%. 아태 CAGR 28.1% 최고 성장 [[G-14]](#ref-g-14)
- ElevenLabs Series D $500M — 총 조달 $781M, 음성 AI 단일 기업 최대 규모 [[G-06]](#ref-g-06)
- Deutsche Telekom–ElevenLabs: 통신망 레벨 AI 음성 통합이라는 새로운 사업 모델 등장 [[G-07]](#ref-g-07)
- Qwen3-TTS·Chatterbox 오픈소스 공세 → 상용 API 단가 하방 압력 가속화
- Play.ht 서비스 종료 — 중간 규모 사업자 구축 경쟁 심화

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Voice Cloning: Comprehensive Survey (2025) | 보이스 클로닝 전반(few-shot, zero-shot, 다국어) 체계적 서베이 | [[P-01]](#ref-p-01) |
| DiffGAN-ZSTTS (2025) | FastSpeech2 + Diffusion decoder 제로샷 화자 적응 | [[P-02]](#ref-p-02) |
| Zero-Shot Voice Cloning for Dysphonia (2024) | 음성 장애 화자 대상 제로샷 TTS — 의료 접근성 확장 | [[P-03]](#ref-p-03) |

#### 전략적 시사점

**기회**
- Deutsche Telekom 파트너십은 통신사가 보이스 AI를 망 레벨에서 내재화하는 새 모델 — 국내 통신사 유사 파트너십 검토 여지
- Qwen3-TTS(Apache 2.0) 오픈소스로 자체 솔루션 구축 비용 장벽 대폭 하락. 한국어 파인튜닝이 차별화 포인트
- 아태 CAGR 28.1% — 한국어 특화 보이스 클로닝 시장 진입 타이밍

**위협**
- Google NotebookLM 소송 — 무동의 보이스 클로닝 법적 리스크 전면화
- EU AI Act 2026-08 (Article 50: 합성 음성 투명성 의무) + 미국 NO FAKES Act 입법 추진
- 오픈소스 모델 확산으로 딥페이크 음성 사기·보이스피싱 위협 고도화

---

### Voice Synthesis — 🔴 긴급

#### 기술 동향

1. **Qwen3-TTS — Apache 2.0, 97ms 스트리밍, 10개 언어.**
   Alibaba Qwen팀의 오픈소스 TTS. 1.7B 플래그십 + 0.6B 경량 버전. Dual-Track 스트리밍, 자연어 지시로 억양·감정·속도 제어. 한국어 포함 10개 언어. [[G-01]](#ref-g-01)

2. **Kani-TTS-2 — 400M 파라미터, 3GB VRAM, RTF 0.2.**
   LiquidAI LFM2 기반, NVIDIA NanoCodec. 10초 오디오를 2초에 생성. RTX 3060급 소비자 GPU 동작. H100 8장 × 6시간 학습. Apache 2.0. [[G-36]](#ref-g-36)

3. **Orpheus TTS — Llama-3B 기반, 200ms 스트리밍, 감정 태그.**
   100,000+ 시간 영어 데이터 학습. `<laugh>`, `<sigh>` 등 태그 제어. KV 캐싱 시 25~50ms 달성 가능. 오픈소스 공개 예정. [[G-37]](#ref-g-37)

4. **Kokoro-82M — 82M 파라미터로 대형 모델 수준 품질.**
   StyleTTS2+ISTFTNet 기반. Elo 방식 평가에서 대형 모델 추월. 한국어·영어 등 지원. API $0.06/오디오시간. Apache 2.0. [[G-38]](#ref-g-38)

5. **Gemini 2.5 TTS Flash/Pro — 자연어 스타일 프롬프트, 24개 언어.**
   Google이 Flash(저지연)·Pro(품질) GA 출시. 자연어 억양·감정 제어, 멀티스피커 대화 합성. [[G-39]](#ref-g-39)

6. **ElevenLabs Eleven v3 — 70+ 언어, Audio Tags 감정 제어.**
   복잡 텍스트(화학식, 전화번호) 오류 68% 감소. Text to Dialogue API로 멀티화자 합성. ElevenAgents/Creative/API 3축 플랫폼 재편. [[G-22]](#ref-g-22)

7. **HyperCLOVA X 8B Omni — 한국어 TTS MOS 4.22/5, 옴니모달 단일 모델.**
   네이버가 텍스트·오디오·비전 입출력 단일 모델 공개. 한국어 TTS MOS 4.22 (2위 대비 +0.82). 정부 기반모델 사업 연계. [[G-40]](#ref-g-40), [[G-41]](#ref-g-41)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | Eleven v3 GA. Audio Tags, 70+ 언어, 복잡 텍스트 오류 68%↓ | [[G-22]](#ref-g-22) |
| Google | Gemini 2.5 TTS Flash/Pro GA. 자연어 스타일, 24언어 30화자 | [[G-39]](#ref-g-39) |
| Alibaba (Qwen) | Qwen3-TTS Apache 2.0. 1.7B/0.6B, 97ms, 10언어 | [[G-01]](#ref-g-01) |
| 네이버 | HyperCLOVA X 8B Omni — 한국어 MOS 4.22/5, 옴니모달 | [[G-40]](#ref-g-40) |
| Supertone (HYBE) | K-pop 아이돌 음성 합성, SYNDI8 가상 걸그룹 운영 | [[G-42]](#ref-g-42) |

#### 시장 시그널
- AI 보이스 제너레이터 시장: 2025년 $4.16B → 2031년 $20.71B, CAGR 30.7% [[G-43]](#ref-g-43)
- Neural TTS 세그먼트가 2025년 전체 AI 음성 시장 49.6% 차지 [[G-43]](#ref-g-43)
- 2026년 1~3월 오픈소스 TTS 러시: Qwen3-TTS, Kani-TTS-2, Orpheus, Kokoro — 상용 API 의존도 감소
- EU AI Act Article 50 합성 오디오 라벨링 의무 2026-08 발효 예정 [[G-44]](#ref-g-44)
- TTS가 독립 모듈에서 옴니모달 모델(HyperCLOVA X, Gemini) 내부 기능으로 흡수 추세

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| HyperCLOVA X 8B Omni (NAVER, 2026) | 한국어 TTS MOS 4.22/5, any-to-any 옴니모달 | [[P-10]](#ref-p-10) |
| ARCHI-TTS (2026-02) | 플로우 매칭 + 의미 정렬기, 추론 가속 | [[P-11]](#ref-p-11) |
| VoiceCraft-X (EMNLP 2025) | 11개 언어 Zero-shot TTS + 음성 편집 통합 | [[P-12]](#ref-p-12) |

#### 전략적 시사점

**기회**
- 오픈소스 경량 TTS(Kokoro 82M, Kani-TTS-2 400M)가 온디바이스·엣지 배포 현실화
- HyperCLOVA X Omni가 한국어 TTS 상업 수준 달성 — 오픈소스 기반 한국어 고품질 TTS 확보 가능
- Dia2·Orpheus 스트리밍 아키텍처가 음성 대화 에이전트 진입 비용 감소

**위협**
- Qwen3-TTS 등 대형 테크 오픈소스 공개로 중소 상용 TTS API 업체 가격 경쟁력 급격 약화
- EU AI Act Article 50 합성 오디오 라벨링 의무(2026-08) — 모든 제품 컴플라이언스 비용 추가
- 보이스 딥페이크·피싱 악용이 규제 강화 촉진, 아시아 유사 입법 가속 가능성

---

### Emotional Analysis — 🟡 주목

#### 기술 동향

1. **Google DeepMind — Hume AI acqui-hire로 감정 음성 AI 주도권 강화.**
   CEO Alan Cowen(감정과학 PhD) + 엔지니어 7명 영입. 비독점 라이선스 구조로 규제 심사 우회. Hume AI의 EVI(Empathic Voice Interface)가 Gemini 음성에 통합 예정. [[G-15]](#ref-g-15)

2. **On-device 음성 감정 처리 — 프라이버시 우선 아키텍처.**
   Sensory가 Snapdragon Wear Elite용 Ultra-Low Power 음성 처리 엔진 최적화. HIPAA 준수를 위한 온디바이스 처리 수요 급증. 클라우드-온디바이스 하이브리드 아키텍처가 2026년 표준화. [[G-16]](#ref-g-16)

3. **음성 바이오마커 — 헬스케어 조기 진단 임상 적용 가속.**
   파킨슨병 음성 AI 진단 정확도 98.0%, ROC-AUC 0.991 달성 (Nature Scientific Reports). Canary Speech + Intermountain Ventures 임상 연구 런칭 (2026-02). [[G-17]](#ref-g-17), [[G-18]](#ref-g-18)

4. **Multimodal Transformer 기반 감정 인식 — 학계 주류.**
   2022년 이후 논문 40%+가 트리모달(audio-visual-text) 트랜스포머 채택. edge-cloud 협력형 경량 이중 스트림 네트워크 연구 진행. [[G-19]](#ref-g-19)

5. **마고(MAGO) — 한국 B2B 음성 감정 AI, CES 2026 발표.**
   Audion 플랫폼: 음성 신호 기반 7가지 감정 분석 API/SDK. 한국어 음성인식 99.1%, 감정 분석 85%. '말하는' → '이해하는' 에이전트 전환 방향 제시. [[G-11]](#ref-g-11), [[G-20]](#ref-g-20)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Google DeepMind | Hume AI CEO + 7명 acqui-hire. EVI 비독점 라이선스 취득, Gemini 감정 인식 통합 | [[G-15]](#ref-g-15) |
| Hume AI | Andrew Ettinger 신임 CEO. EVI·Octave(TTS)·Expression Measurement API 3개 제품 유지 | [[G-21]](#ref-g-21) |
| ElevenLabs | Eleven v3 Audio Tags — [sigh], [excited] 등 감정 맥락 TTS. 70+ 언어 | [[G-22]](#ref-g-22) |
| 마고(MAGO) | CES 2026 Audion: 7감정 인식, 다국어, B2B API/SDK | [[G-11]](#ref-g-11) |
| SKT | AI 멘탈케어 — 음성 심리상태 분석 개발. 멘탈케어 전문기업 MOU. A.X K1 기술 보고서 공개 | [[G-23]](#ref-g-23) |
| 네이버 | HyperCLOVA X 기반 Tugboat에 감정지능(AEI) 데이터 적용. CLOVA Voice 감정 TTS 파라미터 제공 | [[G-24]](#ref-g-24) |
| Canary Speech | 음성 바이오마커 우울증(UAR 0.71)·불안장애(UAR 0.66) 탐지. Intermountain Ventures 임상 연구 | [[G-18]](#ref-g-18) |

#### 시장 시그널
- 감정 AI 시장: 2024년 $2.74B → 2030년 $9.01B, CAGR 21.9% [[G-25]](#ref-g-25)
- 감정 탐지·인식 넓은 시장: 2025년 $42.83B → 2032년 $113.32B, CAGR 14.91% [[G-25]](#ref-g-25)
- Google Hume AI acqui-hire — 라이선싱 딜+인재 영입 방식의 새로운 인수 패턴
- KT-Microsoft 5년 파트너십 ₩2.4조 — 한국형 AI 모델 2026 상반기 출시 예정 [[G-26]](#ref-g-26)
- EU AI Act → 공공장소 실시간 감정 인식 제한, 헬스케어·B2B 영역으로 적용 범위 이동

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Explainable AI for early Parkinson's (Kim et al., 2025) | 파킨슨 조기 진단 98.0%, ROC-AUC 0.991 | [[P-04]](#ref-p-04) |
| Multimodal Emotion Recognition Survey (Dzedzickis et al., 2025) | 2022년 후 40%+ 트리모달 트랜스포머 채택 | [[P-05]](#ref-p-05) |
| Behavioral Health via Vocal Biomarkers (Canary Speech, 2026) | MDD UAR 0.71, GAD UAR 0.66 | [[P-06]](#ref-p-06) |

#### 전략적 시사점

**기회**
- Google DeepMind의 Hume AI 영입으로 감정 AI가 빅테크 핵심 인프라로 격상 — 산업 전반 도입 가속화
- 헬스케어 음성 바이오마커: HIPAA 플랫폼 통합으로 B2B SaaS 수익화 모델 명확화
- 마고 B2B 미들웨어 포지셔닝: 글로벌 빅테크가 소비자 시장 집중하는 사이 국내 엔터프라이즈 틈새 공략 가능

**위협**
- Google DeepMind + Hume AI의 Gemini 통합 — 감정 인식이 OS/플랫폼 수준 내재화 시 독립 API 사업자 잠식
- EU AI Act 공공 공간 실시간 감정 인식 제한 — 컴플라이언스 비용 증가
- 감정 인식 정확도 편향 문제: 문화·인종·성별 편향 학습 데이터 이슈 지속

---

### Interrupt & Turn-Taking — 🟡 주목

#### 기술 동향

1. **Full-Duplex 아키텍처 주류화 — 동시 듣기+말하기가 새 기준점.**
   ICASSP 2026 HumDial Challenge가 Full-Duplex Interaction 트랙을 독립 신설하면서 학계 평가 기준 공식화. ElevenLabs, Deepgram, LiveKit이 상용 full-duplex 솔루션 출시. [[G-27]](#ref-g-27)

2. **Semantic End-of-Turn Detection — VAD를 넘어 언어 이해 기반 턴 판단.**
   LiveKit EOU 모델(135M Transformer)이 VAD 대비 인터럽트 오탐 85% 감소, ~50ms 추론. Speechmatics도 SLM 기반 시맨틱 턴 감지 공개. [[G-28]](#ref-g-28), [[G-29]](#ref-g-29)

3. **NVIDIA PersonaPlex — ASR→LLM→TTS 파이프라인을 단일 Transformer로 통합.**
   PersonaPlex-7B (2026-01-15): 170ms 응답, 인터럽트·백채널·오버랩 동시 처리. HuggingFace 오픈 웨이트 공개. 아키텍처 패러다임 전환 신호. [[G-30]](#ref-g-30)

4. **Barge-in 동적 제어 — 맥락 기반 실시간 임계값 조정.**
   Deepgram Flux: `eot_threshold`, `eager_eot_threshold` 등 mid-stream 실시간 변경 (2026-02-27). 제품 차별화 요소로 부상. [[G-31]](#ref-g-31)

5. **FireRedChat — 완전 셀프호스팅 Full-duplex 오픈소스.**
   샤오홍슈(小紅書) 팀 개발. pVAD+EoT 조합 턴테이킹 컨트롤러. 캐스케이드·세미-캐스케이드 2가지 파이프라인. [[G-32]](#ref-g-32)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | Conversational AI 2.0 — 고유 턴테이킹 모델, 인터럽트 감지 95%+, HIPAA 준수 | [[G-33]](#ref-g-33) |
| LiveKit | EOU Transformer 오픈소스. VAD 대비 오탐 85% 감소, 월 100만+ 다운로드 | [[G-28]](#ref-g-28) |
| Deepgram | Flux — End-of-Turn 감지 + mid-stream 동적 설정. Voice Agent API 내장 | [[G-31]](#ref-g-31) |
| NVIDIA | PersonaPlex-7B — 단일 Transformer, 170ms 응답, 오픈 웨이트 | [[G-30]](#ref-g-30) |
| AssemblyAI | Universal-Streaming 시맨틱 엔드포인팅. 300ms 불변 트랜스크립트 | [[G-34]](#ref-g-34) |
| SKT | MWC 2026 A.X "AI Native" 전략. A. 서비스 MAU 1,000만. 턴 감지 세부 기술 미공개 | [[G-35]](#ref-g-35) |
| 마고(MAGO) | Audion — 화자분리·의도분석 API 보유. 턴테이킹 세부 스펙 미공개 | [[G-11]](#ref-g-11) |

#### 시장 시그널
- ICASSP 2026 HumDial Challenge — Full-Duplex Interaction 벤치마크 공식화 [[G-27]](#ref-g-27)
- 오픈소스 확산: FireRedChat, PersonaPlex-7B, LiveKit EOU — 진입 장벽 급격 하락
- SKT A. 서비스 MAU 1,000만 + 멀티모달 확장 → 턴 감지 기술의 B2C 스케일 적용 임박 [[G-35]](#ref-g-35)

#### 학술 동향 (주요 논문)

| 논문 | 핵심 | 출처 |
|------|------|------|
| Full-Duplex-Bench (Gao et al., 2025) | Full-duplex SDM 턴 전환 능력 최초 정량 벤치마크 | [[P-07]](#ref-p-07) |
| ICASSP 2026 HumDial Challenge (2026) | Full-Duplex Interaction 공식 챌린지 트랙 정의 | [[P-08]](#ref-p-08) |
| FireRedChat (2025) | pVAD+EoT 턴테이킹 컨트롤러, 셀프호스팅 오픈소스 | [[P-09]](#ref-p-09) |
| PersonaPlex (NVIDIA, 2026) | 단일 Transformer로 인터럽트·백채널 동시 처리, 170ms | [[G-30]](#ref-g-30) |

#### 전략적 시사점

**기회**
- 시맨틱 턴 감지가 오픈소스·상용 API 양 방향에서 빠르게 상용화 — 국내 빠른 채택 가능
- 한국어 특화 시맨틱 턴 감지는 미개척 영역 — 마고 Audion의 화자분리+의도분석과 결합 시 차별화 가능
- ICASSP HumDial 벤치마크 참여로 기술 가시성 확보 기회

**위협**
- LiveKit·Deepgram·AssemblyAI 등 글로벌 플랫폼의 성숙한 API — 국내 독자 개발 비용 대비 효용 재검토 필요
- NVIDIA PersonaPlex 같은 단일 아키텍처가 기존 파이프라인 비즈니스 대체 가능성

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 Voice AI 관련 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| MWC 2026 "AI Native" 전략 | A.X 모델 기반 AI Native 플랫폼 전략 발표. A. 서비스 MAU 1,000만 돌파 | (L3 밖) | [[G-35]](#ref-g-35) |
| 멀티모달 확장 계획 | 음성·이미지·영상 처리 2026 상반기 확장 예정 | voice-synthesis | [[G-35]](#ref-g-35) |
| AI 멘탈케어 기술 개발 | 음성 심리상태(불안·우울) 분석 AI 개발, 멘탈케어 기업 MOU | emotional-analysis | [[G-23]](#ref-g-23) |
| A.X K1 기술 보고서 | Supertone(HYBE) 협력 음성 합성 기술 포함 | voice-synthesis | [[G-23]](#ref-g-23) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| AI 보이스피싱 탐지 2.0 | 화자인식+딥보이스(AI 변조음성) 탐지 통합 실시간 서비스 상용화 | voice-cloning | [[G-45]](#ref-g-45) |
| Microsoft 5년 파트너십 | AI·클라우드·IT 공동 투자 ₩2.4조. 한국형 AI 모델 2026 상반기 출시 | (L3 밖) | [[G-26]](#ref-g-26) |
| AICC 보이스봇 | KT 전용 클라우드 콜 인프라 + 음성인식·대화처리·음성합성 통합 | voice-synthesis | [[G-46]](#ref-g-46) |

### 시사점
- SKT는 A.X 플랫폼 중심으로 멀티모달 확장 + 멘탈케어(음성 감정) 영역에 투자. ElevenLabs–Deutsche Telekom 모델과 유사한 통신망 AI 음성 통합 접근 가능성
- KT는 보이스피싱 탐지에서 음성 AI 기술(화자인식, 딥보이스 탐지)을 실전 적용 중. Microsoft 파트너십으로 TTS/STT 역량 보강 예상
- 두 회사 모두 턴테이킹·보이스 클로닝 세부 기술은 공개 정보 부족 — Deutsche Telekom 사례처럼 글로벌 음성 AI 업체와의 전략 파트너십이 빠른 추격 경로가 될 수 있음

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **오픈소스 TTS 빅뱅이 Voice AI 전 영역에 파급.** Qwen3-TTS·Chatterbox·Kani-TTS-2·Kokoro의 동시 등장은 Voice Cloning과 Voice Synthesis 모두에서 상용 API 의존도를 낮추고 있다. 이는 Interrupt & Turn-Taking의 실시간 음성 에이전트 구축 비용도 동반 하락시킨다.

2. **감정 인식이 '분석'에서 '생성'으로 양방향 확장.** Google의 Hume AI acqui-hire(분석)와 ElevenLabs Audio Tags(생성)가 동시에 진행되면서, "감정을 읽고 + 감정을 담아 말하는" 풀스택 감정 음성 AI가 가시화되고 있다. 이는 Emotional Analysis와 Voice Synthesis/Cloning의 기술적 수렴점이다.

3. **통신사 = Voice AI 플랫폼 가설 강화.** Deutsche Telekom–ElevenLabs의 망 레벨 AI 음성 통합은 통신사가 단순 인프라 제공자를 넘어 Voice AI 플랫폼 사업자가 될 수 있음을 입증했다. SKT(MAU 1,000만)와 KT(AICC) 모두 유사 궤적에 있다.

4. **규제가 산업 구조를 재편.** EU AI Act Article 50(합성 음성 라벨링), Google NotebookLM 보이스 소송, NO FAKES Act 입법 추진이 동시에 진행되면서 "안전한 음성 AI"가 차별화 요소에서 필수 요건으로 전환 중이다.

### 후속 조치 제안

- 🔴 Voice Cloning 긴급 — ElevenLabs-Deutsche Telekom 모델을 국내 통신사 적용 가능성 검토. 필요 시 `/wtis standard` 검증 제안
- 네이버 HyperCLOVA X Omni 한국어 TTS 성과 추적 — 오픈소스 공개 시 즉시 활용 가능성 평가
- EU AI Act Article 50 발효(2026-08) 전 국내 컴플라이언스 영향 분석 필요

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Qwen.ai — Qwen3-TTS Family Open Sourced | [링크](https://qwen.ai/blog?id=qwen3tts-0115) | blog | 2026-01-22 | [A] |
| <a id="ref-g-02"></a>G-02 | Resemble AI — Chatterbox (GitHub) | [링크](https://github.com/resemble-ai/chatterbox) | repo | 2026 | [A] |
| <a id="ref-g-03"></a>G-03 | ElevenLabs — Conversational AI 2.0 | [링크](https://elevenlabs.io/blog/conversational-ai-2-0) | blog | 2026 | [A] |
| <a id="ref-g-04"></a>G-04 | ElevenLabs — Introducing 11.ai | [링크](https://elevenlabs.io/blog/introducing-11ai) | blog | 2026-03 | [A] |
| <a id="ref-g-05"></a>G-05 | The Register — Azure AI Speech Personal Voice | [링크](https://www.theregister.com/2025/07/31/microsoft_updates_azure_ai_speech/) | news | 2025-07-31 | [B] |
| <a id="ref-g-06"></a>G-06 | TechCrunch — ElevenLabs raises $500M at $11B | [링크](https://techcrunch.com/2026/02/04/elevenlabs-raises-500m-from-sequioia-at-a-11-billion-valuation/) | news | 2026-02-04 | [B] |
| <a id="ref-g-07"></a>G-07 | ElevenLabs — Deutsche Telekom AI Call Assistant | [링크](https://elevenlabs.io/blog/deutsche-telekom-ai-call-assistant) | blog | 2026-03-02 | [A] |
| <a id="ref-g-08"></a>G-08 | Deutsche Telekom — MWC 2026 AI Call Assistant | [링크](https://www.telekom.com/en/media/media-information/archive/deutsche-telekom-reimagines-phone-calls-with-ai-embedded-in-the-network-1102890) | press | 2026-03-02 | [A] |
| <a id="ref-g-09"></a>G-09 | TechCrunch — NPR host sues Google over NotebookLM voice | [링크](https://techcrunch.com/2026/02/15/longtime-npr-host-david-greene-sues-google-over-notebooklm-voice/) | news | 2026-02-15 | [B] |
| <a id="ref-g-10"></a>G-10 | TechCrunch — Alexa+ available to everyone in US | [링크](https://techcrunch.com/2026/02/04/alexa-amazons-ai-assistant-is-now-available-to-everyone-in-the-u-s/) | news | 2026-02-04 | [B] |
| <a id="ref-g-11"></a>G-11 | MAGO — Next Generation Voice Recognition AI | [링크](https://www.holamago.com/en/) | web | 2026 | [A] |
| <a id="ref-g-12"></a>G-12 | Naver CLOVA — TTS Premium API | [링크](https://api.ncloud-docs.com/docs/en/ai-naver-clovavoice-ttspremium) | doc | 2026 | [A] |
| <a id="ref-g-13"></a>G-13 | Gaga.art — PlayHT Service Shutdown | [링크](https://gaga.art/blog/playht/) | blog | 2026 | [C] |
| <a id="ref-g-14"></a>G-14 | Grand View Research — AI Voice Cloning Market 2030 | [링크](https://www.grandviewresearch.com/industry-analysis/ai-voice-cloning-market-report) | report | 2026 | [B] |
| <a id="ref-g-15"></a>G-15 | TechCrunch — Google snags Hume AI team | [링크](https://techcrunch.com/2026/01/22/google-reportedly-snags-up-team-behind-ai-voice-startup-hume-ai/) | news | 2026-01-22 | [B] |
| <a id="ref-g-16"></a>G-16 | Sensory — Edge AI 2026 Predictions | [링크](https://sensory.com/edge-ai-2026/) | blog | 2026 | [B] |
| <a id="ref-g-17"></a>G-17 | Canary Speech — 5 Vocal Biomarker Trends 2026 | [링크](https://canaryspeech.com/blog/5-trends-in-2026/) | blog | 2026 | [C] |
| <a id="ref-g-18"></a>G-18 | Utah Business — Canary Speech + Intermountain Study | [링크](https://www.utahbusiness.com/press-releases/2026/02/13/canary-speech-intermountain-ventures-launch-groundbreaking-study-sclerosis/) | news | 2026-02-13 | [B] |
| <a id="ref-g-19"></a>G-19 | PMC — Multimodal Emotion Recognition Review | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC12292624/) | paper | 2025 | [A] |
| <a id="ref-g-20"></a>G-20 | 시사저널e — K-음성 AI 진화 | [링크](https://www.sisajournal-e.com/news/articleView.html?idxno=415319) | news | 2026 | [B] |
| <a id="ref-g-21"></a>G-21 | Hume AI — EVI Product | [링크](https://www.hume.ai/empathic-voice-interface) | product | 2026 | [A] |
| <a id="ref-g-22"></a>G-22 | ElevenLabs — Eleven v3 Audio Tags | [링크](https://elevenlabs.io/blog/eleven-v3) | blog | 2026-02-12 | [A] |
| <a id="ref-g-23"></a>G-23 | SKT 뉴스룸 — AI 멘탈케어 / A.X K1 | [링크](https://news.sktelecom.com/218112) | IR | 2026-03 | [A] |
| <a id="ref-g-24"></a>G-24 | CLOVA Tech Blog — 감정 이해 AI | [링크](https://clova.ai/tech-blog/%EC%9D%8C%EC%84%B1%EC%9C%BC%EB%A1%9C-%EC%86%8C%ED%86%B5%ED%95%98%EB%8A%94-ai-%EC%82%AC%EB%9E%8C%EC%9D%98-%EA%B0%90%EC%A0%95%EA%B9%8C%EC%A7%80-%EC%9D%B4%ED%95%B4%ED%95%98%EB%8B%A4) | blog | 2025 | [B] |
| <a id="ref-g-25"></a>G-25 | GlobeNewswire — Emotion AI Market 2025-2035 | [링크](https://www.globenewswire.com/news-release/2026/01/20/3221854/28124/en/Emotion-AI-Market-Trends-and-Global-Forecasts-Report-2025-2035-Opportunities-in-Enhancing-Customer-Experiences-and-Mental-Health-Monitoring-Driven-by-Advancements-in-ML-and-NLP.html) | report | 2026-01-20 | [B] |
| <a id="ref-g-26"></a>G-26 | Straightnews — SK·KT·LG AI 삼국지 | [링크](https://www.straightnews.co.kr/news/articleView.html?idxno=296616) | news | 2026 | [B] |
| <a id="ref-g-27"></a>G-27 | ICASSP 2026 HumDial Challenge | [링크](https://aslp-lab.github.io/HumDial-Challenge/) | news | 2026-02-04 | [A] |
| <a id="ref-g-28"></a>G-28 | LiveKit — Transformer End-of-Turn Detection | [링크](https://livekit.com/blog/using-a-transformer-to-improve-end-of-turn-detection/) | blog | 2025 | [B] |
| <a id="ref-g-29"></a>G-29 | Speechmatics — Semantic Turn Detection | [링크](https://blog.speechmatics.com/semantic-turn-detection) | blog | 2025 | [B] |
| <a id="ref-g-30"></a>G-30 | NVIDIA Research — PersonaPlex | [링크](https://research.nvidia.com/labs/adlr/personaplex/) | news | 2026-01-15 | [A] |
| <a id="ref-g-31"></a>G-31 | Deepgram — Introducing Flux | [링크](https://deepgram.com/learn/introducing-flux-conversational-speech-recognition) | news | 2026-02-27 | [B] |
| <a id="ref-g-32"></a>G-32 | GitHub — FireRedChat | [링크](https://github.com/FireRedTeam/FireRedChat) | repo | 2025 | [B] |
| <a id="ref-g-33"></a>G-33 | VentureBeat — ElevenLabs Conversational AI 2.0 | [링크](https://venturebeat.com/ai/elevenlabs-debuts-conversational-ai-2-0-voice-assistants-that-understand-when-to-pause-speak-and-take-turns-talking) | news | 2025-05-30 | [B] |
| <a id="ref-g-34"></a>G-34 | AssemblyAI — Turn Detection Endpointing | [링크](https://www.assemblyai.com/blog/turn-detection-endpointing-voice-agent) | blog | 2025 | [B] |
| <a id="ref-g-35"></a>G-35 | AI News — MWC 2026 SK Telecom AI Native | [링크](https://www.artificialintelligence-news.com/news/mwc-2026-sk-telecom-lays-out-plan-to-rebuild-its-core-around-ai/) | news | 2026-03-02 | [B] |
| <a id="ref-g-36"></a>G-36 | MarkTechPost — Kani-TTS-2 | [링크](https://www.marktechpost.com/2026/02/15/meet-kani-tts-2-a-400m-param-open-source-text-to-speech-model-that-runs-in-3gb-vram-with-voice-cloning-support/) | news | 2026-02-15 | [B] |
| <a id="ref-g-37"></a>G-37 | Communeify — Orpheus TTS | [링크](https://www.communeify.com/en/blog/orpheus-tts-emotional-human-speech-synthesis/) | blog | 2026-03 | [C] |
| <a id="ref-g-38"></a>G-38 | HuggingFace — Kokoro-82M | [링크](https://huggingface.co/hexgrad/Kokoro-82M) | repo | 2025 | [A] |
| <a id="ref-g-39"></a>G-39 | Google Blog — Gemini 2.5 TTS | [링크](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-2-5-text-to-speech/) | news | 2026 | [A] |
| <a id="ref-g-40"></a>G-40 | NAVER Corp — HyperCLOVA X Omni | [링크](https://www.navercorp.com/en/media/pressReleasesDetail?seq=34256) | press | 2026-01 | [A] |
| <a id="ref-g-41"></a>G-41 | CLOVA Tech Blog — HyperCLOVA X OMNI | [링크](https://clova.ai/en/tech-blog/hyperclova-x-omni-koreas-flagship-ai-on-the-road-to-omnimodality) | blog | 2026-01 | [A] |
| <a id="ref-g-42"></a>G-42 | MBW — Supertone SYNDI8 (HYBE) | [링크](https://www.musicbusinessworldwide.com/hybe-owned-voice-cloning-startup-supertone-launches-ai-powered-virtual-pop-group-syndi81/) | news | 2024 | [B] |
| <a id="ref-g-43"></a>G-43 | MarketsandMarkets — AI Voice Generator Market $20.71B by 2031 | [링크](https://www.marketsandmarkets.com/PressReleases/ai-voice-generator.asp) | report | 2025 | [B] |
| <a id="ref-g-44"></a>G-44 | Jones Day — EU AI Act Labelling Code of Practice | [링크](https://www.jonesday.com/en/insights/2026/01/european-commission-publishes-draft-code-of-practice-on-ai-labelling-and-transparency) | legal | 2026-01 | [A] |
| <a id="ref-g-45"></a>G-45 | Digital Today — KT AI 보이스피싱 탐지 2.0 | [링크](https://www.digitaltoday.co.kr/news/articleView.html?idxno=580815) | news | 2026 | [B] |
| <a id="ref-g-46"></a>G-46 | KT AICC — 보이스봇 | [링크](https://www.kt-aicc.com/user/voiceBot) | product | 2026 | [A] |
| <a id="ref-p-01"></a>P-01 | Voice Cloning: Comprehensive Survey (2025) | [링크](https://arxiv.org/html/2505.00579v1) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | DiffGAN-ZSTTS: Zero-Shot Speaker Adaptation (Nature SR, 2025) | [링크](https://www.nature.com/articles/s41598-025-90507-0) | paper | 2025 | [A] |
| <a id="ref-p-03"></a>P-03 | Zero-Shot Voice Cloning for Dysphonia (IEEE, 2024) | [링크](https://ieeexplore.ieee.org/document/10517609/) | paper | 2024 | [A] |
| <a id="ref-p-04"></a>P-04 | Kim et al. — Explainable AI Parkinson's via Voice (Nature SR, 2025) | [링크](https://www.nature.com/articles/s41598-025-96575-6) | paper | 2025 | [A] |
| <a id="ref-p-05"></a>P-05 | Dzedzickis et al. — Multimodal Emotion Recognition Survey (PMC, 2025) | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC12292624/) | paper | 2025 | [A] |
| <a id="ref-p-06"></a>P-06 | Canary Speech — Behavioral Health Vocal Biomarkers (2026) | [링크](https://canaryspeech.com/wp-content/uploads/2025/04/canary-behavioralhealth-technicalreport-2026.pdf) | paper | 2026 | [B] |
| <a id="ref-p-07"></a>P-07 | Gao et al. — Full-Duplex-Bench (arXiv, 2025) | [링크](https://arxiv.org/abs/2503.04721) | paper | 2025-03 | [A] |
| <a id="ref-p-08"></a>P-08 | ICASSP 2026 HumDial Challenge Paper | [링크](https://arxiv.org/abs/2601.05564) | paper | 2026-02 | [A] |
| <a id="ref-p-09"></a>P-09 | FireRedChat: Full-Duplex Voice Interaction (arXiv, 2025) | [링크](https://arxiv.org/abs/2509.06502) | paper | 2025-09 | [A] |
| <a id="ref-p-10"></a>P-10 | HyperCLOVA X 8B Omni (NAVER, arXiv 2026) | [링크](https://arxiv.org/abs/2601.01792) | paper | 2026-01 | [A] |
| <a id="ref-p-11"></a>P-11 | ARCHI-TTS: Flow-Matching TTS (arXiv, 2026) | [링크](https://arxiv.org/abs/2602.05207) | paper | 2026-02 | [A] |
| <a id="ref-p-12"></a>P-12 | VoiceCraft-X: Multilingual TTS (EMNLP 2025) | [링크](https://aclanthology.org/2025.emnlp-main.137/) | paper | 2025 | [A] |
