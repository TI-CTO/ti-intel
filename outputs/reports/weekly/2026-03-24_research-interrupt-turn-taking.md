---
type: weekly-deep-research
topic: interrupt-turn-taking
date: 2026-03-24
parent: 2026-03-24_weekly-voice-ai.md
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
---

# Deep 리서치: Interrupt & Turn-Taking (2026-W13)

> **조사 범위**: 2026-03-17 ~ 2026-03-24 / 기술·시장·경쟁 동향 종합
> **MCP 상태**: intel-store MCP 미호출 (VSCode 확장 환경 제약) — WebSearch 전량 대체. 수집 품질 [B] 이상.
> **추적 키워드**: ElevenLabs, LiveKit, Deepgram, AssemblyAI, NVIDIA, Google, OpenAI, τ-Voice, turn-taking, barge-in, full-duplex

---

## 이전 대비 변화

- **전주 (W12, 2026-03-17)**: Full-Duplex-Bench 수치 공개 (Gemini Live TOR 0.255 vs Moshi 0.265s Turn-Taking Latency), OpenAI gpt-realtime 정식 출시 (Semantic VAD), LiveKit turn-detector v0.4.1-intl 한국어 포함 14개 언어 지원 + 오탐 39.23% 추가 감소, Magic Data 한국어 full-duplex 데이터셋 공개, NVIDIA PersonaPlex-7B 실측 0.170s Smooth Turn-Taking latency 확인.
- **금주 (W13, 2026-03-24)**: ElevenLabs Conversational AI 2.0 출시 — 독자 턴테이킹 신경망 모델 + 인터럽트 감지 정확도 95% 주장. 음성 에이전트 인프라 투자 폭증 확인 (LiveKit $100M/$1B, ElevenLabs $500M/$11B, Synthflow $20M, Newo.ai $25M, Hamming.ai $3.8M — 복수 라운드 합산). τ-Voice 벤치마크 (arXiv 2603.13686) 발표로 full-duplex 평가 표준화 가속. SKT A.auto 차량 내 AI 에이전트 출시 (음성 기반).
- **변화 방향**: 평가·인프라 표준화가 시장 구조 재편을 촉진하는 방향. ElevenLabs가 단순 TTS 기업에서 엔터프라이즈 음성 에이전트 플랫폼으로 포지셔닝 전환. 인프라 레이어(LiveKit·Deepgram·AssemblyAI)와 애플리케이션 레이어(Synthflow·Newo·Retell AI) 간 투자 양극화가 뚜렷해지고 있음. 한국 통신사 음성 에이전트 본격 경쟁 신호 포착 (SKT).

---

## 기술 동향

1. **ElevenLabs Conversational AI 2.0 — 독자 턴테이킹 신경망 + 인터럽트 제어 3단계.**
   2025년 5월 출시된 Conversational AI 2.0은 기존 VAD(음성 활동 감지) 기반에서 벗어나 필러 워드(um, ah), 운율, 발화 리듬, 미세 정지를 분석하는 하이브리드 신경망 턴테이킹 모델을 탑재했다. 인터럽트 감지 정확도 95% 이상을 자사 벤치마크 기준 주장한다. 전환 민첩성(Turn Eagerness)을 Eager·Normal·Patient 3단계로 설정 가능하며, Turn Timeout은 1~30초 조정 가능하다. 기업 기능으로는 HIPAA 준수, EU 데이터 레지던시, 멀티모달, 배치 통화, 내장 RAG가 포함됐다 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[E-01]](#ref-e-01).

2. **τ-Voice — Full-Duplex 음성 에이전트 벤치마크의 새 표준 제안.**
   arXiv 2603.13686 (2026-03-14 제출)은 음성 에이전트를 실세계 복잡도가 있는 과제 기반으로 평가하는 τ-Voice 벤치마크를 발표했다. τ²-bench를 음성 도메인으로 확장하여 복잡한 멀티턴 대화, 도메인 정책 준수, 실시간 환경 상호작용을 평가 항목으로 포함한다. 현실적인 음성 시뮬레이터는 다양한 억양, 실내외 배경 소음, 채널 열화(프레임 드롭·먹먹함), 자연스러운 턴테이킹 행동(인터럽트·백채널링·발화 틱)을 재현한다. W12에서 확인한 Full-Duplex-Bench(arXiv 2503.04721)와 함께 평가 인프라가 복수 표준으로 확장되는 흐름이다 [[P-01]](#ref-p-01).

3. **Deepgram Flux — 세계 최초 대화 전용 음성 인식(CSR) 모델, 엔드포인트 감지 통합.**
   2025년 10월 VapiCon에서 발표된 Flux는 기존 ASR(자동 음성 인식)이 전사(transcription) 목적으로 설계된 것과 달리, 실시간 음성 에이전트의 턴 역학을 이해하도록 훈련된 최초의 대화 전용 음성 인식(CSR, Conversational Speech Recognition) 모델이다. VAD·엔드포인팅 트리거·맥락 인식 턴 감지를 단일 모델에 통합하여 엔드오브턴(End-of-Turn) 감지 레이턴시 ~260ms를 달성했다. GPU당 100+ 스트림 병렬 처리, Nova-3 수준 정확도를 유지하며, Voiceflow에도 통합 완료됐다. 엔드포인팅 설정 최솟값(500ms)으로 프로덕션 환경에서 오탐의 90%를 필터링한다 [[G-03]](#ref-g-03), [[E-02]](#ref-e-02).

4. **LiveKit 턴 감지 모델 — 한국어 포함 14개 언어, 의미적 완전성 기반 예측.**
   LiveKit은 VAD 전용·STT 엔드포인팅·모델 기반 감지 3가지 방식을 지원하며, 고유의 오픈 웨이트 턴 감지 모델을 개발했다. Qwen2.5 7B 교사 → 0.5B 학생 모델 지식 증류로 RAM ~400MB, 추론 ~25ms를 실현한다. 정확도는 진양성률(TPR, True Positive Rate) 85%로, 단순 침묵이 아닌 의미적 완전성을 판단 신호로 사용하여 사용자가 말을 마치지 않았을 때의 조기 인터럽트를 방지한다. 지원 언어에 영어, 프랑스어, 스페인어, 독일어, 이탈리아어, 포르투갈어, 네덜란드어, 중국어, 일본어, **한국어**, 인도네시아어, 러시아어, 터키어, 힌디어가 포함됐다 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05).

5. **AssemblyAI Universal-Streaming — 음향+의미 통합 엔드포인팅, ~150ms P50 레이턴시.**
   AssemblyAI의 Universal-Streaming은 음향 특성과 의미적 특성을 결합한 지능형 엔드포인팅을 내장하여 전통적 침묵 기반 방식의 폴백 안전성을 유지하면서도 정확도를 향상시켰다. 최신 모델인 Universal-3 Pro Streaming은 VAD 엔드포인트 감지 후 ~150ms P50 레이턴시, 영어 도메인 WER(단어 오류율) 8.14%를 달성한다. 2026년 3월 기준 멀티링구얼 Universal-Streaming 출시로 글로벌 언어 지원도 확장됐다 [[G-06]](#ref-g-06), [[G-07]](#ref-g-07).

6. **Retell AI — 턴테이킹 모델 업데이트로 레이턴시 150ms 추가 감소.**
   2026년 1월 Retell AI는 턴테이킹 모델을 업데이트하여 전체 레이턴시를 150ms 추가 절감했다. 현재 전체 플랫폼 레이턴시 ~600ms를 달성했으며, 수익이 $40M ARR을 돌파했다. 독자적 턴테이킹 모델은 사용자 발화 완료 여부를 의미 기반으로 판단하며, 조기 응답과 과도한 대기 사이의 균형을 핵심 과제로 설계됐다 [[G-08]](#ref-g-08), [[E-03]](#ref-e-03).

7. **Google Gemini Live API — Proactive Audio(프로액티브 오디오) 기능으로 침묵 판단 지능화.**
   Gemini Live API는 WebSocket 기반 full-duplex 연결로 실시간 스트리밍을 처리한다. 기본 서버사이드 VAD 턴 감지 외에, 프리뷰 기능인 Proactive Audio는 에이전트가 수동 청취가 적절한 맥락에서 불필요한 인터럽트를 스스로 방지하도록 한다. Gemini 2.5 Flash Native Audio는 향상된 함수 호출과 지시 준수 능력을 갖추며, 2026-03-19에 구형 모델(gemini-live-2.5-flash-preview-native-audio-09-2025)이 지원 종료됐다 [[G-09]](#ref-g-09), [[E-04]](#ref-e-04).

8. **노이즈 강건 턴테이킹 로봇 — 쇼핑몰 현장 실험으로 응답 레이턴시 단축 실증.**
   arXiv 2503.06241 (IROS 2025 채택)은 Transformer 기반 잡음 강건 VAP(음성 활동 투영, Voice Activity Projection) 모델을 실세계 쇼핑몰 환경에서 검증한 현장 실험을 보고했다. 기존 클라우드 기반 음성 인식 시스템 대비 응답 레이턴시가 유의미하게 단축됐으며, 로봇과 사용자 양측 모두 더 빠르게 응답하는 더 자연스러운 대화가 관찰됐다. 배경 소음이 풍부한 실세계 환경에서의 턴테이킹 강건성을 직접 입증한 최초 현장 실험 중 하나다 [[P-02]](#ref-p-02).

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | Conversational AI 2.0 출시 (2025-05). 독자 신경망 턴테이킹 모델, 인터럽트 감지 정확도 95% 주장. 동시에 $500M Series D ($11B 밸류에이션) 조달로 음성 에이전트 플랫폼 전환 확인. Deutsche Telekom·Revolut 엔터프라이즈 고객 확보, $330M ARR. | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01), [[G-10]](#ref-g-10) |
| LiveKit | $100M Series C 조달, 밸류에이션 $1B (유니콘). Index Ventures·Salesforce Ventures 주도. ChatGPT Advanced Voice Mode, xAI, Meta, Spotify에 인프라 제공. 턴 감지 모델 한국어 포함 14개 언어 지원, ~25ms 추론. | [[G-11]](#ref-g-11), [[G-04]](#ref-g-04) |
| Deepgram | Flux CSR 모델(2025-10) GA — 세계 최초 대화 전용 음성 인식. ~260ms 엔드오브턴 감지, GPU당 100+ 스트림. Voice Agent API 정식 출시로 STT·TTS·오케스트레이션 단일 API 제공. | [[G-03]](#ref-g-03), [[E-02]](#ref-e-02) |
| AssemblyAI | Universal-3 Pro Streaming: ~150ms P50 레이턴시, WER 8.14%. 음향+의미 통합 엔드포인팅 출시. 멀티링구얼 Universal-Streaming 확장. | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07) |
| NVIDIA | PersonaPlex-7B-v1 (arXiv 2602.06053, ICASSP 2026). Moshi 아키텍처 기반 full-duplex, Smooth Turn-Taking 0.170s. 멀티롤·음성 클로닝 full-duplex 모델로 고객 서비스 시나리오 검증. | [[P-03]](#ref-p-03) |
| Retell AI | 턴테이킹 모델 업데이트로 전체 레이턴시 150ms 절감, ~600ms 달성. $40M ARR 돌파(2026-01). 음성·채팅·이메일·SMS 통합 멀티채널 플랫폼 전환. | [[G-08]](#ref-g-08), [[E-03]](#ref-e-03) |
| Google | Gemini Live API Proactive Audio 기능 추가. gemini-live-2.5-flash-preview 구형 모델 2026-03-19 지원 종료. Gemini 2.5 Flash Native Audio로 함수 호출·지시 준수 개선. | [[G-09]](#ref-g-09), [[E-04]](#ref-e-04) |
| SKT | A.auto 인카 AI 에이전트 2026-01-14 출시 (르노코리아 필란테 탑재). A.X 4.0 LLM 기반, T-map·FLO·전화·뉴스 음성 제어. MWC 2026에서 AI Native 전략 발표, 1GW AIDC 구축 및 1T 파라미터 멀티모달 모델 업그레이드 계획. | [[G-12]](#ref-g-12), [[E-05]](#ref-e-05) |
| Synthflow AI | $20M Series A (Accel 주도, 2025-06). 노코드 음성 에이전트 플랫폼, 5M+ 시간 절감·35% 통화 응답률 향상 보고. 200+ CRM/캘린더/전화 시스템 통합. 총 $30M 조달. | [[G-13]](#ref-g-13), [[E-06]](#ref-e-06) |
| Newo.ai | $25M Series A (2026-02-10, Ratmir Timashev 주도). SMB 대상 AI 리셉셔니스트, Zero-Hallucination Architecture. 15,000+ 에이전트 생성, 2025년 12월 이후 매출 2배 성장. | [[G-14]](#ref-g-14) |
| Hamming.ai | $3.8M 시드 (Mischief·YCombinator, 2026-03-05). 음성 에이전트 자동화 테스트·거버넌스 플랫폼. 4M+ 통화 스트레스 테스트, 기존 대비 20배 빠르고 10배 저렴한 테스트 클레임. | [[G-15]](#ref-g-15) |

---

## 시장 시그널

- LiveKit, $100M Series C 조달로 밸류에이션 $1B 달성 (유니콘). Index Ventures·Salesforce Ventures 주도. ChatGPT Advanced Voice Mode 포함 수십억 건/년 통화 인프라 운영 [[G-11]](#ref-g-11).
- ElevenLabs, $500M Series D (Sequoia 주도, 2026-02) 조달, 밸류에이션 $11B. 전 라운드($3.3B) 대비 3배 이상 상승. 총 조달액 $781M. $330M ARR 기반 엔터프라이즈 플랫폼 포지셔닝 [[G-10]](#ref-g-10), [[E-01]](#ref-e-01).
- Synthflow AI, $20M Series A (Accel·Atlantic Labs·Singular, 2025-06). 총 $30M 조달. 엔터프라이즈 노코드 음성 에이전트 시장 가속 [[G-13]](#ref-g-13).
- Newo.ai, $25M Series A (2026-02-10). SMB 프런트데스크 AI 음성 에이전트, 15,000+ 에이전트 플랫폼으로 성장 [[G-14]](#ref-g-14).
- Hamming.ai, $3.8M 시드 (2026-03-05). 음성 에이전트 신뢰성·테스트 자동화 전문 스타트업 — 인프라 품질보증(QA) 세부 시장 형성 신호 [[G-15]](#ref-g-15).
- 대화형 AI 시장 규모: 2025년 $14.29B 추정, 2030년 $41.39B (CAGR 23.7%) 전망 [[G-16]](#ref-g-16). [단일 소스, [C] 수준 신뢰도]
- 음성 에이전트 빌더 87.5%가 연구 단계가 아닌 실제 구축 중이라는 조사 결과 (2026 Voice Agent Report) [[G-16]](#ref-g-16). [단일 소스]

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| τ-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains (Ray et al., 2026) | full-duplex 음성 에이전트를 실세계 과제 기반으로 평가하는 벤치마크. 인터럽트·백채널링·노이즈·억양 다양성을 포함한 현실 시뮬레이터. τ²-bench의 음성 확장. | [[P-01]](#ref-p-01) |
| A Noise-Robust Turn-Taking System for Real-World Dialogue Robots: A Field Experiment (Inoue et al., 2025) | Transformer 기반 잡음 강건 VAP 모델, 쇼핑몰 현장 실험에서 응답 레이턴시 유의미하게 단축. IROS 2025 채택. | [[P-02]](#ref-p-02) |
| PersonaPlex: Voice and Role Control for Full Duplex Conversational Speech Models (NVIDIA, 2026) | Moshi 아키텍처 기반 full-duplex 모델. 역할+음성 동시 조건화, Smooth Turn-Taking 0.170s, ICASSP 2026 게재. | [[P-03]](#ref-p-03) |
| Full-Duplex-Bench: A Benchmark to Evaluate Full-Duplex Spoken Dialogue Models on Turn-Taking Capabilities (Iwamoto et al., 2025) | Pause Handling·Backchanneling·Smooth Turn-Taking·User Interruption 4축 평가. Gemini Live TOR 0.255, Moshi 0.265s 레이턴시. | [[P-04]](#ref-p-04) |
| Real-time and Continuous Turn-taking Prediction Using Voice Activity Projection (Ekstedt et al., 2024) | VAP(음성 활동 투영) 모델로 스테레오 오디오에서 미래 발화 활동 실시간 예측. 멀티링구얼 확장판 별도 발표됨. | [[P-05]](#ref-p-05) |

---

## 전략적 시사점

**기회**

- ElevenLabs·LiveKit·Deepgram이 음성 에이전트 인프라 레이어를 선점하는 동안, 국내 통신사가 한국어 특화 턴테이킹 모델 독자 개발 또는 전략적 파트너십을 체결할 시간이 제한적임. LiveKit의 한국어 공식 지원(v0.4.1-intl)은 최소 기술 기반을 낮추는 긍정 신호이나, ElevenLabs가 서울 사무소 설립 및 Deutsche Telekom 파트너십을 통해 통신사 직접 공략 의도를 명확히 함.
- τ-Voice 벤치마크, Full-Duplex-Bench 등 표준 평가 지표가 수립되면서 국내 기업의 객관적 기술 격차 측정이 가능해짐. 이를 활용한 WTIS 분석 정밀화 기회.
- Hamming.ai의 음성 에이전트 테스트 자동화 세부 시장(4M+ 통화 스트레스 테스트) 출현은 통신사 내부 음성 에이전트 품질관리 체계 고도화 수요와 직결됨.
- 차량 내 음성 에이전트 (SKT A.auto) 영역에서 통신사 고유 데이터(운전 패턴, 맥락 정보)를 활용한 턴테이킹 개인화 모델 구축 가능성.

**위협**

- ElevenLabs의 $330M ARR + $11B 밸류에이션은 통신사가 독자적으로 경쟁하기 어려운 생태계 잠금 효과(lock-in)를 형성 중. Deutsche Telekom 같은 글로벌 통신사가 이미 ElevenLabs 에이전트 플랫폼에 종속 예정.
- 음성 에이전트 인프라 레이어(LiveKit·Deepgram·AssemblyAI)가 모두 영미권 기업으로 집중. 한국어 지원이 추가됐으나 훈련 데이터 다양성·오류율 편차가 여전히 과제.
- Synthflow·Newo.ai 등 노코드 플랫폼이 중소기업(SMB) 시장을 빠르게 잠식하면서, 통신사 ARS/컨택센터 사업 기반이 중기적으로 위협받을 가능성.
- Retell AI $40M ARR 달성 — 음성 에이전트 플랫폼 시장에서 수익 모델이 이미 검증됐음. 국내 플레이어의 진입 기회가 좁아지는 속도 빠름.
- Google Gemini Live API의 Proactive Audio 기능과 모델 교체 주기(2026-03-19 구형 모델 지원 종료) 빠른 교체 주기는 의존 기업의 통합 비용 반복 발생을 의미.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | VentureBeat — ElevenLabs Conversational AI 2.0 turn-taking | [링크](https://venturebeat.com/ai/elevenlabs-debuts-conversational-ai-2-0-voice-assistants-that-understand-when-to-pause-speak-and-take-turns-talking) | news | 2025-05-30 | [B] |
| <a id="ref-g-02"></a>G-02 | blockchain.news — ElevenLabs Conversational AI 2.0 enterprise features | [링크](https://blockchain.news/ainews/elevenlabs-launches-conversational-ai-2-0-with-advanced-turn-taking-model-and-enterprise-features) | news | 2025-05-30 | [B] |
| <a id="ref-g-03"></a>G-03 | Deepgram — Introducing Flux: Conversational Speech Recognition | [링크](https://deepgram.com/learn/introducing-flux-conversational-speech-recognition) | blog | 2025-10-02 | [B] |
| <a id="ref-g-04"></a>G-04 | LiveKit — Turn Detection: VAD, Endpointing, and Model-Based Detection | [링크](https://livekit.com/blog/turn-detection-voice-agents-vad-endpointing-model-based-detection) | blog | 2025-12 | [B] |
| <a id="ref-g-05"></a>G-05 | LiveKit Docs — Turn detector plugin (multilingual) | [링크](https://docs.livekit.io/agents/logic/turns/turn-detector/) | docs | 2025-12 | [A] |
| <a id="ref-g-06"></a>G-06 | AssemblyAI — Introducing Multilingual Universal-Streaming | [링크](https://www.assemblyai.com/blog/introducing-multilingual-universal-streaming) | blog | 2026-03 | [B] |
| <a id="ref-g-07"></a>G-07 | AssemblyAI — How intelligent turn detection (endpointing) solves the biggest challenge | [링크](https://www.assemblyai.com/blog/turn-detection-endpointing-voice-agent) | blog | 2026 | [B] |
| <a id="ref-g-08"></a>G-08 | RetellAI Changelog — Updated turn-taking model, 150ms latency reduction | [링크](https://www.retellai.com/changelog) | docs | 2026-01 | [B] |
| <a id="ref-g-09"></a>G-09 | Google AI — Gemini Live API capabilities guide | [링크](https://ai.google.dev/gemini-api/docs/live-guide) | docs | 2026-03 | [A] |
| <a id="ref-g-10"></a>G-10 | TechCrunch — ElevenLabs raises $500M from Sequoia at $11B valuation | [링크](https://techcrunch.com/2026/02/04/elevenlabs-raises-500m-from-sequioia-at-a-11-billion-valuation/) | news | 2026-02-04 | [B] |
| <a id="ref-g-11"></a>G-11 | SiliconANGLE — LiveKit raises $100M at $1B valuation | [링크](https://siliconangle.com/2026/01/22/livekit-raises-100m-1b-valuation-scale-real-time-ai-media-platform/) | news | 2026-01-22 | [B] |
| <a id="ref-g-12"></a>G-12 | RCRWireless — SK Telecom debuts A.auto in-car AI | [링크](https://www.rcrwireless.com/20260115/ai/sk-telecom-a-dot-auto-ai) | news | 2026-01-15 | [B] |
| <a id="ref-g-13"></a>G-13 | TechCrunch — How Synthflow AI is cutting through the noise | [링크](https://techcrunch.com/2025/06/24/how-synthflow-ai-is-cutting-through-the-noise-in-a-loud-ai-voice-category/) | news | 2025-06-24 | [B] |
| <a id="ref-g-14"></a>G-14 | SiliconANGLE — Newo lands $25M to bring production-ready AI receptionists | [링크](https://siliconangle.com/2026/02/10/newo-lands-25m-bring-production-ready-ai-receptionists-small-businesses/) | news | 2026-02-10 | [B] |
| <a id="ref-g-15"></a>G-15 | TFN — Hamming.ai $3.8M seed funding voice agent reliability | [링크](https://techfundingnews.com/hamming-ai-voice-agent-reliability-funding/) | news | 2026-03-05 | [B] |
| <a id="ref-g-16"></a>G-16 | AssemblyAI — Voice AI in 2026: Inside the companies and investments | [링크](https://www.assemblyai.com/blog/voice-ai-in-2026-series-1) | blog | 2026-03 | [B] |
| <a id="ref-p-01"></a>P-01 | Ray et al. — τ-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains | [링크](https://arxiv.org/abs/2603.13686) | paper | 2026-03-14 | [A] |
| <a id="ref-p-02"></a>P-02 | Inoue et al. — A Noise-Robust Turn-Taking System for Real-World Dialogue Robots: A Field Experiment | [링크](https://arxiv.org/abs/2503.06241) | paper | 2025-03 | [A] |
| <a id="ref-p-03"></a>P-03 | NVIDIA — PersonaPlex: Voice and Role Control for Full Duplex Conversational Speech Models | [링크](https://arxiv.org/abs/2602.06053) | paper | 2026-02 | [A] |
| <a id="ref-p-04"></a>P-04 | Iwamoto et al. — Full-Duplex-Bench: A Benchmark to Evaluate Full-Duplex Spoken Dialogue Models | [링크](https://arxiv.org/abs/2503.04721) | paper | 2025-03 | [A] |
| <a id="ref-p-05"></a>P-05 | Ekstedt et al. — Real-time and Continuous Turn-taking Prediction Using Voice Activity Projection | [링크](https://arxiv.org/abs/2401.04868) | paper | 2024-01 | [A] |
| <a id="ref-e-01"></a>E-01 | ElevenLabs — Conversational AI 2.0 공식 블로그 | [링크](https://elevenlabs.io/blog/conversational-ai-2-0) | IR/발표 | 2025-05-30 | [A] |
| <a id="ref-e-02"></a>E-02 | Deepgram (BusinessWire) — Deepgram Launches Flux — The World's First Conversational Speech Recognition Model | [링크](https://www.businesswire.com/news/home/20251002758871/en/Deepgram-Launches-Flux---The-Worlds-First-Conversational-Speech-Recognition-Model) | IR/발표 | 2025-10-02 | [A] |
| <a id="ref-e-03"></a>E-03 | Retell AI (GlobeNewswire) — Revenue Exceeds $40M ARR, Updated Platform | [링크](https://www.globenewswire.com/news-release/2026/01/29/3228780/0/en/Upgraded-Retell-AI-Voice-Platform-Enables-Corporate-Call-Centers-to-Deploy-Infinite-AI-Sales-and-Support-Agents-Across-Voice-Chat-Email-and-SMS-Company-Revenue-Now-Exceeds-40M-ARR.html) | IR/발표 | 2026-01-29 | [A] |
| <a id="ref-e-04"></a>E-04 | Google Cloud Blog — Build voice-driven applications with Live API | [링크](https://cloud.google.com/blog/products/ai-machine-learning/build-voice-driven-applications-with-live-api) | IR/발표 | 2026-03 | [A] |
| <a id="ref-e-05"></a>E-05 | SKT (PRNewswire) — CEO Unveils AI Native Strategy at MWC26 | [링크](https://www.prnewswire.com/news-releases/sk-telecom-ceo-unveils-ai-native-strategy-at-mwc26-driving-koreas-leap-in-ai-innovation-302700470.html) | IR/발표 | 2026-03-01 | [A] |
| <a id="ref-e-06"></a>E-06 | Synthflow AI (BusinessWire) — Raises $20M to Transform the $168B Global Conversational AI Market | [링크](https://www.businesswire.com/news/home/20250624442670/en/Synthflow-AI-Raises-$20M-to-Transform-the-$168B-Global-Conversational-AI-Market-With-Enterprise-AI-Voice-Agents) | IR/발표 | 2025-06-24 | [A] |
