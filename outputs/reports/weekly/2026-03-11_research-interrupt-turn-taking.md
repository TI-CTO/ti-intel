---
type: deep-research
topic: interrupt-turn-taking
date: 2026-03-11
parent: weekly-voice-ai
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
---

# Deep Research: Interrupt & Turn-Taking (2026-03-11)

> **조사 범위**: 2026-03-04 ~ 2026-03-11 / 기술·시장·경쟁 동향 종합
> **MCP 상태**: intel-store MCP 미호출 (VSCode 확장 환경 제약) — WebSearch로 전량 대체. 수집 품질 [B] 이상.

---

## 기술 동향

1. **Full-Duplex 아키텍처의 주류화 — 동시 듣기+말하기가 새로운 기준점으로 부상.**
   반이중(half-duplex) 방식은 한 번에 한 방향만 처리하며 인터럽트를 구조적으로 막는다. Full-duplex 시스템은 ASR·TTS·LLM을 병렬 처리하여 자연스러운 끊기 없는 대화 흐름을 구현한다. ICASSP 2026 HumDial Challenge(2026-02-04 arXiv 등록)가 Full-Duplex Interaction을 독립 트랙으로 신설하면서 학계 평가 기준이 공식화되었다 [[G-01]](#ref-g-01). 상용 플랫폼에서는 ElevenLabs, Deepgram, LiveKit이 잇달아 자체 full-duplex 솔루션을 출시하며 인프라 수준의 기능으로 정착하고 있다.

2. **Semantic End-of-Turn Detection — VAD의 한계를 언어 이해로 극복.**
   전통적인 VAD(Voice Activity Detection)는 무음 구간을 발화 종료로 판단하지만, "음..." "잠깐만..." 등 일시적 침묵과 실제 턴 종료를 구분하지 못한다. 시맨틱 턴 감지는 소형 언어 모델(SLM)로 발화 맥락을 실시간 분석하여 발화자가 턴을 넘길 의도인지 파악한다. LiveKit의 EOU(End of Utterance) 모델은 135M 파라미터 Transformer(SmolLM v2 기반)로 VAD 대비 인터럽트 오탐 85% 감소, ~50ms 추론 속도를 달성했다 [[G-02]](#ref-g-02). Speechmatics도 자체 SLM 기반 시맨틱 턴 감지를 블로그를 통해 상세 공개했다 [[G-03]](#ref-g-03).

3. **Personalized VAD(pVAD) — 배경 소음과 비주화자 발화 필터링.**
   다화자 환경에서 주화자의 barge-in만 정확히 감지하는 pVAD가 핵심 구성요소로 부각됐다. FireRedChat(샤오홍슈/小紅書 Intelligent Audio Team 개발)은 pVAD + End-of-Turn(EoT) 모듈을 결합한 턴테이킹 컨트롤러를 오픈소스로 공개했다. 캐스케이드(FireRedASR + Qwen2.5 + FireRedTTS-1s)와 세미-캐스케이드(AudioLLM + FireRedTTS-2) 두 파이프라인을 지원한다 [[G-04]](#ref-g-04).

4. **단일 Transformer 아키텍처의 부상 — ASR→LLM→TTS 파이프라인 해체.**
   NVIDIA PersonaPlex(2026-01-15 발표)는 ASR·LLM·TTS를 하나의 Transformer에 통합하여 170ms 응답 시간을 달성했다. 별도 파이프라인 없이 인터럽트·백채널·오버랩을 동시 처리한다. 7B 파라미터 모델(personaplex-7b-v1)을 HuggingFace에 공개했다 [[G-05]](#ref-g-05).

5. **Barge-in 허용 vs. 억제의 동적 제어 — 설정 가능성이 제품 차별화 요소.**
   단순 barge-in 허용을 넘어, 대화 맥락·신뢰도·사용자 프로파일에 따라 barge-in 임계값을 동적으로 조정하는 기능이 등장했다. Deepgram Flux는 `eot_threshold`, `eager_eot_threshold`, `eot_timeout_ms` 파라미터를 mid-stream에서 실시간 변경하는 Configure 메시지를 2026-02-27 추가했다 [[G-06]](#ref-g-06). Microsoft Copilot Studio도 DTMF·음성 기반 barge-in 온/오프 설정을 지원한다 [[G-07]](#ref-g-07).

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| **ElevenLabs** | Conversational AI 2.0 (2025-05-30 출시). 고유 턴테이킹 모델이 "um", "ah" 등 주저 표현을 실시간 분석해 인터럽트 타이밍 판단. 인터럽트 감지 정확도 95%+ 주장. HIPAA 준수·EU 데이터 레지던시 추가로 엔터프라이즈 대응. | [[G-08]](#ref-g-08) |
| **LiveKit** | EOU Transformer 플러그인 오픈소스 공개. VAD 대비 오탐 85% 감소, 50ms 추론 달성. 월 100만+ 다운로드 프레임워크(LiveKit Agents)에 기본 통합. 향후 멀티언어·오디오 기반 EOU 모델 개발 예정. | [[G-02]](#ref-g-02) |
| **Deepgram** | Flux 모델: 대화 흐름 이해 기반 End-of-Turn 감지, Nova-3 수준 정확도. 2026-02-27 mid-stream 동적 설정 변경 기능 추가. Voice Agent API에 barge-in 감지·턴 예측 내장. | [[G-06]](#ref-g-06) |
| **Speechmatics** | 시맨틱 턴 감지 기술 블로그 공개. VAD+SLM 하이브리드 방식으로 일시적 침묵과 실제 턴 종료 구분. ~250ms 신호→최종 트랜스크립트 처리. | [[G-03]](#ref-g-03) |
| **AssemblyAI** | Universal-Streaming 기반 시맨틱 엔드포인팅. 신경망 턴 감지기로 300ms 불변 트랜스크립트 제공. `end_of_turn_confidence_threshold` + VAD 침묵 결합 방식. | [[G-09]](#ref-g-09) |
| **NVIDIA** | PersonaPlex-7B-v1 (2026-01-15). 단일 Transformer 아키텍처, 170ms 응답. 인터럽트·백채널·오버랩 발화 동시 처리. HuggingFace 오픈 웨이트 공개. | [[G-05]](#ref-g-05) |
| **Microsoft** | M365 Copilot Voice 실시간 대화 기능 2025-09월(모바일)~2026-03월(데스크톱/웹) 순차 출시. Copilot Studio에서 barge-in 온/오프 설정 지원. | [[G-07]](#ref-g-07) |
| **FireRedTeam (샤오홍슈)** | FireRedChat 오픈소스 공개. pVAD+EoT 조합 턴테이킹 컨트롤러. 캐스케이드·세미-캐스케이드 2가지 파이프라인 선택 가능. 완전 셀프호스팅 지원. | [[G-04]](#ref-g-04) |
| **SKT** | MWC 2026에서 A.X 모델 기반 "AI Native" 전략 발표. A. 서비스 MAU 1,000만 돌파. 멀티모달(음성·이미지·영상) 처리로 상반기 내 확장 계획. 음성 턴 감지 세부 기술은 공개 정보 없음. | [[G-10]](#ref-g-10) |
| **MAGO (마고)** | Audion 플랫폼으로 STT·화자 분리·의도·감정 분석 API/SDK 제공. CES 2026 및 LG U+ Shift 발표에서 "'말하는' 에이전트에서 '이해하는' 에이전트로" 전환 방향 제시. 턴테이킹 기술 세부 스펙은 공개 정보 없음. | [[G-11]](#ref-g-11) |

---

## 시장 시그널

- **평가 표준화 가속**: ICASSP 2026 HumDial Challenge가 Full-Duplex Interaction을 공식 경쟁 트랙으로 채택하면서, 인터럽트 처리·오버랩 발화·실시간 턴 감지가 학계 벤치마크 항목으로 편입됐다 [[G-01]](#ref-g-01).
- **Full-Duplex-Bench 등장**: arXiv 2503.04721 (2025-03-06 초판, 2025-08-16 최신판)이 full-duplex SDM 평가 프레임워크를 제안. 반이중 방식 대비 full-duplex SDM의 턴 전환 능력을 정량 비교하는 공식 벤치마크로 자리잡는 중 [[P-01]](#ref-p-01).
- **오픈소스 확산**: FireRedChat, PersonaPlex-7B, LiveKit EOU 플러그인 등 핵심 컴포넌트가 오픈소스·오픈 웨이트로 공개되며 진입 장벽이 급격히 낮아지고 있다.
- **상용 API 경쟁 심화**: Deepgram, AssemblyAI, Speechmatics, ElevenLabs가 모두 시맨틱 턴 감지를 API 수준에서 제공하며, 가격·정확도·지연시간이 실질적 차별화 기준이 됐다.
- **통신사 플랫폼 편입 가능성**: SKT A. 서비스 MAU 1,000만 돌파와 멀티모달 확장 계획은 턴 감지·인터럽트 기술이 B2C 스케일로 적용되는 시점이 임박했음을 시사한다 [[G-10]](#ref-g-10).
- **엔터프라이즈 컴플라이언스 요구**: HIPAA·EU 데이터 레지던시 등 규제 요건이 음성 AI 플랫폼 선택 기준으로 부상. ElevenLabs가 선제 대응 중 [[G-08]](#ref-g-08).

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Full-Duplex-Bench: A Benchmark to Evaluate Full-duplex Spoken Dialogue Models on Turn-taking Capabilities (Gao et al., 2025) | Full-duplex SDM의 턴 전환 능력을 정량 평가하는 최초 공식 벤치마크. 반이중 모델 대비 성능 격차 정량화. | [[P-01]](#ref-p-01) |
| From Turn-Taking to Synchronous Dialogue: A Survey of Full-Duplex Spoken Language Models (2025) | 2024~2025 full-duplex 시스템 서베이. 인터럽트·백채널 모델링 미성숙, 컴포넌트 ablation 부재를 공개 과제로 지목. | [[P-02]](#ref-p-02) |
| TurnGuide: Enhancing Meaningful Full Duplex Spoken Interactions via Dynamic Turn-Level Text-Speech Interleaving (2025) | 턴 수준 텍스트-음성 인터리빙 생성으로 SOTA 턴 전환 성능 달성. 2026-01-20 업데이트. | [[P-03]](#ref-p-03) |
| SALM-Duplex: Efficient and Direct Duplex Modeling for Speech-to-Speech Language Model (2025) | 사용자·에이전트 스트림 동시 모델링하는 채널 퓨전 아키텍처 제안. Ultra-low latency 목표. | [[P-04]](#ref-p-04) |
| The ICASSP 2026 HumDial Challenge: Benchmarking Human-like Spoken Dialogue Systems in the LLM Era (2026) | ICASSP 2026 공식 챌린지 논문. Full-Duplex Interaction 트랙: 인터럽트·오버랩·실시간 턴 감지 평가 체계 정의. | [[P-05]](#ref-p-05) |
| FireRedChat: A Pluggable, Full-Duplex Voice Interaction System with Cascaded and Semi-Cascaded Implementations (2025) | pVAD+EoT 기반 턴테이킹 컨트롤러 설계. 오픈소스 완전 셀프호스팅 구조. | [[P-06]](#ref-p-06) |

---

## 전략적 시사점

**기회**
- 시맨틱 턴 감지는 오픈소스(LiveKit EOU, PersonaPlex)와 상용 API(Deepgram Flux, AssemblyAI) 양 방향에서 빠르게 상용화 중 — 국내 플랫폼의 빠른 채택이 가능하다.
- ICASSP HumDial 벤치마크 공식화로 성능 비교 기준이 명확해졌다 — 국내 연구기관·기업이 해당 벤치마크에 참여하면 기술 가시성을 높일 수 있다.
- 마고(MAGO) Audion은 화자 분리·의도 분석 API를 이미 보유 — 이를 시맨틱 EoT와 연결하면 한국어 특화 턴 감지 솔루션 공백을 메울 수 있다.
- SKT A. 서비스의 대규모 B2C 배포 계획은 자연스러운 턴테이킹 수요를 대규모로 검증할 기회다.

**위협**
- LiveKit·Deepgram·AssemblyAI 등 글로벌 플랫폼이 이미 성숙한 API를 제공 중 — 국내 독자 개발의 비용 대비 효용을 재검토해야 한다.
- NVIDIA PersonaPlex 같은 단일 아키텍처 모델이 기존 파이프라인 비즈니스를 대체할 가능성이 있다.
- 영어 중심 시맨틱 턴 감지 모델(LiveKit EOU는 현재 영어만 지원)의 한국어 성능 격차가 여전히 존재하며, 이는 글로벌 플랫폼의 국내 시장 침투를 일시적으로 제한하는 동시에 국내 솔루션의 차별화 창문이기도 하다.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | ICASSP 2026 HumDial Challenge 공식 사이트 | [링크](https://aslp-lab.github.io/HumDial-Challenge/) | news | 2026-02-04 | [A] |
| <a id="ref-g-02"></a>G-02 | LiveKit — Using a Transformer to Improve End-of-Turn Detection | [링크](https://livekit.com/blog/using-a-transformer-to-improve-end-of-turn-detection/) | blog | 2025 | [B] |
| <a id="ref-g-03"></a>G-03 | Speechmatics — How to build smarter turn detection for Voice AI | [링크](https://blog.speechmatics.com/semantic-turn-detection) | blog | 2025 | [B] |
| <a id="ref-g-04"></a>G-04 | GitHub — FireRedTeam/FireRedChat | [링크](https://github.com/FireRedTeam/FireRedChat) | blog | 2025 | [B] |
| <a id="ref-g-05"></a>G-05 | NVIDIA Research — PersonaPlex | [링크](https://research.nvidia.com/labs/adlr/personaplex/) | news | 2026-01-15 | [A] |
| <a id="ref-g-06"></a>G-06 | Deepgram — Introducing Flux: Conversational Speech Recognition | [링크](https://deepgram.com/learn/introducing-flux-conversational-speech-recognition) | news | 2026-02-27 | [B] |
| <a id="ref-g-07"></a>G-07 | Microsoft — Real-time voice conversation coming to M365 Copilot | [링크](https://supersimple365.com/realtime-voice-conversation-with-m365-copilot/) | news | 2025 | [B] |
| <a id="ref-g-08"></a>G-08 | ElevenLabs — Conversational AI 2.0 (VentureBeat 보도) | [링크](https://venturebeat.com/ai/elevenlabs-debuts-conversational-ai-2-0-voice-assistants-that-understand-when-to-pause-speak-and-take-turns-talking) | news | 2025-05-30 | [B] |
| <a id="ref-g-09"></a>G-09 | AssemblyAI — How intelligent turn detection (endpointing) solves voice agent challenges | [링크](https://www.assemblyai.com/blog/turn-detection-endpointing-voice-agent) | blog | 2025 | [B] |
| <a id="ref-g-10"></a>G-10 | AI News — MWC 2026: SK Telecom lays out plan to rebuild its core around AI | [링크](https://www.artificialintelligence-news.com/news/mwc-2026-sk-telecom-lays-out-plan-to-rebuild-its-core-around-ai/) | news | 2026-03-02 | [B] |
| <a id="ref-g-11"></a>G-11 | MAGO — From speaking to understanding voice conversation agent | [링크](https://www.holamago.com/en/blog/%EB%8C%80%ED%99%94%EB%A5%BC-%EC%B2%98%EB%A6%AC-%ED%95%98%EB%8A%94-%EC%9D%8C%EC%84%B1-%EB%8C%80%ED%99%94-%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8%EC%97%90%EC%84%9C-%E2%80%98%EC%9D%B4%ED%95%B4%E2%80%99%ED%95%98%EB%8A%94-%EC%9D%8C%EC%84%B1-%EB%8C%80%ED%99%94-%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8%EB%A1%9C) | blog | 2026 | [C] |
| <a id="ref-g-12"></a>G-12 | Deepgram — Voice Agent API | [링크](https://deepgram.com/product/voice-agent-api) | blog | 2026 | [B] |
| <a id="ref-g-13"></a>G-13 | Speechmatics — Voice AI in 2026: 9 numbers that signal what's next | [링크](https://www.speechmatics.com/company/articles-and-news/voice-ai-in-2026-9-numbers-that-signal-whats-next) | news | 2026 | [B] |
| <a id="ref-g-14"></a>G-14 | ElevenLabs — X 발표 (Conversational AI 2.0) | [링크](https://x.com/elevenlabsio/status/1928527751956308004) | news | 2025-05-30 | [B] |
| <a id="ref-g-15"></a>G-15 | Medium — From Turn-Taking to Synchronous Dialogue: Building and Measuring True Full-Duplex Systems | [링크](https://medium.com/@brijeshrn/from-turn-taking-to-synchronous-dialogue-building-and-measuring-true-full-duplex-systems-794a07f3e59f) | blog | 2025 | [C] |
| <a id="ref-g-16"></a>G-16 | Korea Times — Naver and Kakao gear up for agentic AI era in 2026 | [링크](https://www.koreatimes.co.kr/amp/business/tech-science/20260102/naver-kakao-gear-up-for-agentic-ai-era-in-2026) | news | 2026-01-02 | [B] |
| <a id="ref-g-17"></a>G-17 | Notch.cx — Tackling Turn Detection in Voice AI: Overcoming Noise and Interruption Challenges | [링크](https://www.notch.cx/post/turn-detection-in-voice-ai) | blog | 2025 | [C] |
| <a id="ref-g-18"></a>G-18 | AssemblyAI — The voice AI stack for building agents in 2026 | [링크](https://www.assemblyai.com/blog/the-voice-ai-stack-for-building-agents) | blog | 2026 | [B] |
| <a id="ref-g-19"></a>G-19 | Sparkco — Optimizing Voice Agent Barge-in Detection for 2025 | [링크](https://sparkco.ai/blog/optimizing-voice-agent-barge-in-detection-for-2025) | blog | 2025 | [C] |
| <a id="ref-g-20"></a>G-20 | NVIDIA Medium — PersonaPlex: Realtime Voice AI that can listen and speak simultaneously | [링크](https://medium.com/data-science-in-your-pocket/nvidia-personaplex-realtime-voice-ai-that-can-listen-and-speak-simultaneously-0f5668a63901) | blog | 2026-01 | [B] |
| <a id="ref-p-01"></a>P-01 | Gao et al. — Full-Duplex-Bench: A Benchmark to Evaluate Full-duplex Spoken Dialogue Models on Turn-taking Capabilities | [링크](https://arxiv.org/abs/2503.04721) | paper | 2025-03-06 | [A] |
| <a id="ref-p-02"></a>P-02 | Survey — From Turn-Taking to Synchronous Dialogue: A Survey of Full-Duplex Spoken Language Models | [링크](https://arxiv.org/abs/2509.14515) | paper | 2025-09-18 | [A] |
| <a id="ref-p-03"></a>P-03 | TurnGuide — Enhancing Meaningful Full Duplex Spoken Interactions via Dynamic Turn-Level Text-Speech Interleaving | [링크](https://arxiv.org/abs/2508.07375) | paper | 2025-08 (2026-01-20 업데이트) | [A] |
| <a id="ref-p-04"></a>P-04 | SALM-Duplex — Efficient and Direct Duplex Modeling for Speech-to-Speech Language Model | [링크](https://arxiv.org/abs/2505.15670) | paper | 2025-05 | [A] |
| <a id="ref-p-05"></a>P-05 | ASLP-lab et al. — The ICASSP 2026 HumDial Challenge | [링크](https://arxiv.org/abs/2601.05564) | paper | 2026-02-04 | [A] |
| <a id="ref-p-06"></a>P-06 | FireRedTeam — FireRedChat: A Pluggable, Full-Duplex Voice Interaction System | [링크](https://arxiv.org/abs/2509.06502) | paper | 2025-09 | [A] |
