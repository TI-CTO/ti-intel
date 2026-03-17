---
type: weekly-research
topic: interrupt-turn-taking
domain: voice-ai
date: 2026-03-17
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
---

# Interrupt & Turn-Taking — Deep 리서치 (W12)

> **조사 범위**: 2026-03-10 ~ 2026-03-17 / 기술·시장·경쟁 동향 종합
> **MCP 상태**: intel-store MCP 미호출 (VSCode 확장 환경 제약) — WebSearch 전량 대체. 수집 품질 [B] 이상.
> **추적 키워드**: OpenAI, Google, Anthropic, Meta SyncLLM, Full-Duplex-Bench, Edge AEC+VAD

---

## 이전 대비 변화

- **전주 (W11, 2026-03-11)**: Full-duplex 주류화 확인, ICASSP 2026 HumDial FDI 트랙 신설, NVIDIA PersonaPlex-7B 단일 Transformer 170ms 발표, LiveKit EOU 오탐 85% 감소, Deepgram Flux 동적 barge-in 제어, FireRedChat 오픈소스 공개. 한국어 시맨틱 턴 감지 미개척 상태 지속.
- **금주 (W12, 2026-03-17)**: Full-Duplex-Bench 공식 평가 수치 확보 (Gemini Live vs. Moshi 등 비교), LiveKit turn-detector v0.4.1-intl 한국어 포함 14개 언어 지원 + 오탐 39.23% 추가 감소, OpenAI gpt-realtime Realtime API 정식 출시(베타 졸업), OpenAI의 차세대 full-duplex 아키텍처 Q1 2026 완성 목표 보도, Magic Data 한국어 포함 다국어 full-duplex 대화 데이터셋 공개, Meta SyncLLM 기술 세부 재확인.
- **변화 방향**: 한국어 지원 공백이 **부분적으로 해소**되기 시작. LiveKit multilingual 모델이 한국어를 공식 지원 언어로 포함함으로써 W11에서 지적한 "영어 중심 격차" 상황이 변화. 동시에 평가 인프라(Full-Duplex-Bench)가 수치 기반 비교를 가능하게 하면서 경쟁 가시화. OpenAI가 full-duplex 전환을 공식화하는 방향으로 진행 중.

---

## 기술 동향

1. **Full-Duplex-Bench — 턴테이킹 평가의 정량적 표준이 확립됨.**
   arXiv 2503.04721 (2025-03-06 초판 → 2025-08-16 v2)이 full-duplex SDM을 4개 축으로 평가하는 공식 벤치마크를 제안했다. 4축은 Pause Handling(TOR ↓), Backchanneling(TOR ↓, Backchannel Frequency ↑, JSD ↓), Smooth Turn-Taking(TOR ↑, Response Latency ↓), User Interruption(TOR ↑, GPT-4o Score ↑, Latency After Interruption ↓)이다. 테스트 결과 Gemini Live가 Pause Handling에서 최우수(TOR 0.255), Moshi가 Turn-Taking Latency에서 최단(0.265s)를 기록했다. 상용 모델 중 Gemini Live의 Turn-Taking Latency는 1.301s로 오픈소스 대비 뒤처졌다 [[P-01]](#ref-p-01).

2. **OpenAI gpt-realtime — 베타 졸업 및 Semantic VAD 정식 지원.**
   OpenAI는 Realtime API를 베타에서 정식 프로덕션 등급으로 전환하고 `gpt-realtime` 모델을 출시했다. Semantic VAD(`turn_detection.type = semantic_vad`) 모드를 공식 지원: 발화 내용을 분류기로 점수화하여 "음..." 같은 사용자 일시 정지를 턴 종료로 오인하지 않도록 설계됐다. `interrupt_response` 파라미터로 인터럽트 동작을 세밀하게 제어할 수 있다. instruction-following 정확도 18.6%p, tool-calling 정확도 12.9%p 향상이 보고됐다 [[G-01]](#ref-g-01), [[G-02]](#ref-g-02).

3. **OpenAI — 차세대 Full-Duplex 아키텍처 Q1 2026 목표.**
   복수 보도에 따르면 OpenAI는 오디오 팀을 통합하고 "동시 발화(speaks while you speak)" 처리가 가능한 신규 아키텍처를 2026년 3월 목표로 개발 중이다. 현행 시스템의 순차적 턴 방식을 탈피하여 real-time 동시 발화, 인터럽트, 문장 중 수정을 처리하는 것이 목표다 [[G-03]](#ref-g-03), [[G-04]](#ref-g-04). 공식 발표는 이 보고서 작성 시점(2026-03-17) 기준 미확인.

4. **Google Gemini Live API — barge-in 개선 및 Proactive Audio 모드 추가.**
   Gemini Live API는 WebSocket 기반 full-duplex 연결로 마이크 스트리밍과 음성 응답 수신을 동시에 처리한다. 사용자 인터럽트 시 예정된 오디오를 즉시 폐기하고 청취 모드로 전환하는 barge-in이 시끄러운 환경에서도 안정적으로 동작하도록 개선됐다. Proactive Audio 기능으로 에이전트가 언제 응답하고 언제 침묵을 유지할지 지능적으로 판단한다(서버사이드 VAD + 중단 제어) [[G-05]](#ref-g-05), [[E-01]](#ref-e-01).

5. **LiveKit turn-detector v0.4.1-intl — 한국어 포함 14개 언어 지원, 오탐 39.23% 추가 감소.**
   W11에서 확인한 오탐 85% 감소(VAD 대비)에 더해, v0.4.1-intl 업데이트(2025-12월)는 이전 v0.3.0-intl 대비 오탐을 추가로 39.23% 상대적으로 감소시켰다. 지원 언어에 한국어가 공식 포함됐다. 7B Qwen2.5 교사 모델 → 0.5B 학생 모델 지식 증류 방식, RAM ~400MB, 추론 ~25ms. 구조화된 입력(이메일, 전화번호, 신용카드 번호 등)에서의 조기 인터럽트 오탐을 특히 개선했다 [[G-06]](#ref-g-06).

6. **NVIDIA PersonaPlex-7B — 실측 latency 및 FullDuplexBench 상세 수치 확보.**
   v1 실측: Smooth Turn-Taking latency 0.170s, User Interruption latency 0.240s. FullDuplexBench 기준 Smooth Turn-Taking TOR 0.908, User Interruption TOR 0.950. 단일 Transformer가 내부 상태를 스트리밍으로 갱신하면서 즉시 응답 스트리밍을 시작하는 방식으로 기존 파이프라인 지연을 제거했다. ICASSP 2026에 게재 승인됨 [[G-07]](#ref-g-07), [[G-08]](#ref-g-08).

7. **Edge AEC+VAD — sub-100ms가 표준 요구 사항으로 정착.**
   2026년 기준 edge 기반 full-duplex 에이전트는 AEC(Acoustic Echo Cancellation)+VAD를 sub-100ms로 동작시키는 것을 요구 사항으로 명시한다. 오디오 프레임 처리 주기는 10~20ms 수준이며, sub-2B 파라미터 모델과 효율적 코덱 조합이 on-device 또는 near-edge 추론의 현실적 스위트스팟으로 부상했다 [[G-09]](#ref-g-09), [[G-10]](#ref-g-10).

8. **Anthropic Claude Code Voice Mode — Push-to-talk 방식 제한적 출시.**
   2026-03-03 Claude Code에 Voice Mode가 출시(5% 롤아웃)됐다. Push-to-talk(스페이스바 홀드) 방식이며, full-duplex 혹은 자연스러운 턴테이킹 구현이 아닌 제어 기반 접근이다. 대화 중 자연스러운 인터럽트나 barge-in은 현재 지원하지 않는다 [[G-11]](#ref-g-11).

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| **OpenAI** | gpt-realtime 정식 출시(베타 졸업). Semantic VAD 공식 지원으로 시맨틱 턴 감지 상용 표준화. Q1 2026 동시 발화 처리 신규 아키텍처 개발 중(공식 미발표). | [[G-01]](#ref-g-01), [[G-03]](#ref-g-03) |
| **Google** | Gemini Live API Proactive Audio + 향상된 barge-in 지원. sub-300ms latency 예산 내 전환 관리. 서버사이드 VAD 인터럽트 즉시 처리. | [[G-05]](#ref-g-05), [[E-01]](#ref-e-01) |
| **Anthropic** | Claude Code Voice Mode 출시(2026-03-03, 5% 롤아웃). Push-to-talk 방식으로 full-duplex 아님. Claude 일반 채팅에도 Voice Mode 이미 제공 중. | [[G-11]](#ref-g-11) |
| **Meta** | SyncLLM — Llama-3-8B 기반 wall-clock synchronized full-duplex. 160~240ms 청크 단위 동기 처리. 212k시간 합성 데이터 + 2k시간 실제 대화 데이터 학습. EMNLP 2024 게재. | [[P-02]](#ref-p-02), [[G-12]](#ref-g-12) |
| **NVIDIA** | PersonaPlex-7B-v1: Smooth Turn-Taking 0.170s, Interruption 0.240s 실측. ICASSP 2026 채택. FullDuplexBench에서 오픈소스 SOTA 달성. | [[G-07]](#ref-g-07), [[G-08]](#ref-g-08) |
| **LiveKit** | turn-detector v0.4.1-intl: 한국어 포함 14개 언어 공식 지원. v0.3.0-intl 대비 오탐 39.23% 추가 감소. ~25ms 추론. LiveKit Agents Python 1.3.0 / JS 1.0.19에 통합. | [[G-06]](#ref-g-06) |
| **Deepgram** | Flux: Realtime API와 연동 가능한 mid-stream 동적 EOT 임계값 설정. ~260ms EOT 감지. Nova-3 수준 정확도. Telnyx 등 통신사 파트너사에 배포 확대 중. | [[G-13]](#ref-g-13) |
| **Huawei** | MWC 2026(2026-03-02): AICC용 차세대 Voice Virtual Agent 공개. Conversational Agent Engine(CAE) + 도메인 특화 LLM 결합. 자기해결률 20% 향상 주장. 인터럽트·턴 감지 세부 스펙 미공개. | [[E-02]](#ref-e-02) |
| **Magic Data** | 중국어·영어·일본어·한국어·스페인어 포함 다국어 full-duplex 대화 데이터셋 출시. 한국어 경어체·감정 종결어미·빠른 턴테이킹 반영. 독립 채널 분리(오버랩 발화 포함). 상업 라이선스 제공. | [[G-14]](#ref-g-14) |

---

## 시장 시그널

- **Full-Duplex-Bench 수치가 경쟁 비교의 기준점으로 부상**: Gemini Live TOR(Pause Handling) 0.255 vs. Moshi TOR 0.985 같은 수치가 공개되면서, 기업·연구팀 간 정량 경쟁이 시작됐다. Latency 수치(응답 1.301s vs. 0.265s)는 상용 제품의 실질적 취약점을 드러낸다 [[P-01]](#ref-p-01).
- **OpenAI Realtime API 베타 졸업**: 프로덕션 등급 전환은 인터럽트·턴 감지 기능을 기업 도입 가능 수준으로 공식화하는 신호다. Semantic VAD가 API 기본 기능이 된 것은 시장 표준화 진행을 의미한다 [[G-01]](#ref-g-01).
- **한국어 full-duplex 데이터 공백 해소 시작**: Magic Data 다국어 데이터셋과 LiveKit multilingual 모델의 한국어 지원으로, 한국어 시맨틱 턴 감지 모델 학습 인프라가 갖춰지기 시작했다. W11의 "한국어 미개척" 상태에서 "초기 인프라 구축" 단계로 전환 중이다 [[G-14]](#ref-g-14), [[G-06]](#ref-g-06).
- **Edge full-duplex 양산 임박**: sub-100ms AEC+VAD, sub-2B 파라미터 모델 조합이 on-device 배포의 현실적 기준으로 정립됐다. Whisper, DistilHuBERT 등 경량 모델이 모바일에서 100ms 이하 달성 사례가 등장하고 있다 [[G-09]](#ref-g-09).
- **통신사·엔터프라이즈 수요 확대**: Huawei AICC MWC 2026 발표, Deepgram-Telnyx 통신사 파트너십 확대 등 통신사 채널을 통한 voice AI 배포가 가속화되고 있다 [[E-02]](#ref-e-02), [[G-13]](#ref-g-13).
- **오픈소스 진영의 벤치마크 우위**: FullDuplexBench에서 오픈소스 Moshi(0.265s)가 상용 Gemini Live(1.301s)를 큰 폭으로 앞서는 결과는 오픈소스 모델이 빠른 반응성 측면에서 상용 클라우드 API를 추월하고 있음을 시사한다 [[P-01]](#ref-p-01).

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Full-Duplex-Bench: A Benchmark to Evaluate Full-duplex Spoken Dialogue Models on Turn-taking Capabilities (Gao et al., 2025) | Pause Handling·Backchanneling·Turn-Taking·Interruption 4축 정량 평가. Gemini Live TOR(Pause) 0.255, Turn-Taking Latency 1.301s. Moshi 0.265s 기록. | [[P-01]](#ref-p-01) |
| Beyond Turn-Based Interfaces: Synchronous LLMs as Full-Duplex Dialogue Agents — SyncLLM (Tu et al., 2024) | Llama-3-8B에 wall-clock 동기화 메커니즘 도입. 160~240ms 청크 단위. 212k시간 합성 데이터 학습. EMNLP 2024 채택. | [[P-02]](#ref-p-02) |
| PersonaPlex: Voice and Role Control for Full Duplex Conversational AI (NVIDIA, 2026) | 단일 Transformer로 ASR·LLM·TTS 통합. Smooth Turn-Taking 0.170s, Interruption 0.240s. FullDuplexBench + ServiceDuplexBench SOTA. ICASSP 2026 채택. | [[P-03]](#ref-p-03) |
| Full-Duplex-Bench-v2: A Multi-Turn Evaluation Framework for Duplex Dialogue Systems with an Automated Examiner (2025) | Fast/Slow 페이싱 2가지 설정, 4개 태스크 패밀리(daily, correction, entity tracking, safety). 다회전 명령 추종 및 안전성 평가 추가. | [[P-04]](#ref-p-04) |
| The ICASSP 2026 HumDial Challenge (ASLP-lab et al., 2026) | Full-Duplex Interaction 공식 경쟁 트랙 신설. 인터럽트·오버랩·실시간 턴 감지 평가 체계 정의. | [[P-05]](#ref-p-05) |
| FireRedChat: A Pluggable, Full-Duplex Voice Interaction System (Chen et al., 2025) | pVAD+EoT 기반 턴테이킹 컨트롤러. 캐스케이드/세미-캐스케이드 2가지 파이프라인. 셀프호스팅 오픈소스. | [[P-06]](#ref-p-06) |

---

## 전략적 시사점

**기회**
- LiveKit turn-detector v0.4.1-intl의 한국어 공식 지원으로 한국어 시맨틱 턴 감지 기반 구현의 즉시 가능성이 열렸다. 25ms 추론·400MB RAM으로 경량 배포가 가능하다.
- Magic Data 다국어 데이터셋이 한국어 full-duplex 모델 파인튜닝의 원자재를 제공한다. 경어체·감정 종결어미 반영 데이터는 범용 영어 모델의 한국어 적용 한계를 보완한다.
- Full-Duplex-Bench 수치가 공개되면서 정량적 성능 포지셔닝이 가능해졌다. Gemini Live의 Turn-Taking Latency 1.301s 대비 경쟁력 있는 수치를 목표로 제품 스펙을 수립할 수 있다.
- OpenAI Realtime API 베타 졸업 + Semantic VAD 정식 지원으로, 빠른 프로토타이핑 경로(API 직접 통합)가 확보됐다.

**위협**
- Full-Duplex-Bench에서 오픈소스 Moshi가 상용 Gemini Live를 응답 속도에서 5배 앞서는 결과는 클라우드 API 의존 전략의 품질 한계를 드러낸다.
- OpenAI Q1 2026 신규 아키텍처가 완성될 경우, 현재 Semantic VAD 기반 반이중 시스템과의 격차가 갑자기 벌어질 수 있다.
- NVIDIA PersonaPlex, Meta SyncLLM 같은 단일 Transformer 접근법이 성숙해지면, 기존 STT+LLM+TTS 파이프라인 구조로 구축된 시스템은 재설계 압박을 받는다.
- Huawei AICC가 MWC 2026에서 통신사 채널을 통해 엔터프라이즈 voice agent를 배포하는 방식은 국내 통신사(SKT·KT) 플랫폼 전략에 직접적 경쟁 변수다.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | OpenAI — Introducing gpt-realtime and Realtime API updates for production voice agents | [링크](https://community.openai.com/t/introducing-gpt-realtime-and-realtime-api-updates-for-production-voice-agents/1355039) | news | 2025-12-22 | [A] |
| <a id="ref-g-02"></a>G-02 | OpenAI — Voice Activity Detection (VAD) Guide | [링크](https://developers.openai.com/api/docs/guides/realtime-vad/) | blog | 2025 | [A] |
| <a id="ref-g-03"></a>G-03 | OpenAI merges audio teams, targets new voice architecture by March 2026 | [링크](https://www.implicator.ai/openai-merges-audio-teams-targets-new-voice-architecture-by-march-2026/) | news | 2026-01 | [B] |
| <a id="ref-g-04"></a>G-04 | OpenAI bets big on audio as Silicon Valley declares war on screens (TechCrunch) | [링크](https://techcrunch.com/2026/01/01/openai-bets-big-on-audio-as-silicon-valley-declares-war-on-screens/) | news | 2026-01-01 | [B] |
| <a id="ref-g-05"></a>G-05 | Gemini Live API: Build Low-Latency Voice AI Apps | [링크](https://i10x.ai/news/gemini-live-api-real-time-voice-conversations) | blog | 2026 | [B] |
| <a id="ref-g-06"></a>G-06 | LiveKit — Improved End-of-Turn Model Cuts Voice AI Interruptions 39% | [링크](https://blog.livekit.io/improved-end-of-turn-model-cuts-voice-ai-interruptions-39/) | blog | 2025-12 | [B] |
| <a id="ref-g-07"></a>G-07 | NVIDIA — PersonaPlex: Natural Conversational AI With Any Role and Voice | [링크](https://research.nvidia.com/labs/adlr/personaplex/) | news | 2026-01-15 | [A] |
| <a id="ref-g-08"></a>G-08 | MarkTechPost — NVIDIA Releases PersonaPlex-7B-v1 | [링크](https://www.marktechpost.com/2026/01/17/nvidia-releases-personaplex-7b-v1-a-real-time-speech-to-speech-model-designed-for-natural-and-full-duplex-conversations/) | news | 2026-01-17 | [B] |
| <a id="ref-g-09"></a>G-09 | Rethinking Voice AI At The Edge: A Practical Offline Pipeline (SemiEngineering) | [링크](https://semiengineering.com/rethinking-voice-ai-at-the-edge-a-practical-offline-pipeline/) | blog | 2026 | [B] |
| <a id="ref-g-10"></a>G-10 | Real-time Voice AI Latency: Hit Sub-100ms (Vogla) | [링크](https://vogla.com/real-time-voice-ai-latency-sub-100ms-production/) | blog | 2026 | [C] |
| <a id="ref-g-11"></a>G-11 | Anthropic — Claude Code rolls out a voice mode capability (TechCrunch) | [링크](https://techcrunch.com/2026/03/03/claude-code-rolls-out-a-voice-mode-capability/) | news | 2026-03-03 | [B] |
| <a id="ref-g-12"></a>G-12 | Meta AI — Beyond Turn-Based Interfaces: SyncLLM (공식 연구 페이지) | [링크](https://ai.meta.com/research/publications/beyond-turn-based-interfaces-synchronous-llms-as-full-duplex-dialogue-agents/) | news | 2024-11 | [A] |
| <a id="ref-g-13"></a>G-13 | Deepgram — Deepgram Flux now available in Telnyx Voice AI | [링크](https://telnyx.com/release-notes/deepgram-flux-voice-ai-release) | news | 2026 | [B] |
| <a id="ref-g-14"></a>G-14 | MagicHub — Large-Scale Multilingual Full-Duplex Conversational Speech Datasets | [링크](https://magichub.com/large-scale-multilingual-full-duplex-conversational-speech-datasets-accelerating-voice-ai-industrialization-with-magic-data/) | news | 2026 | [B] |
| <a id="ref-e-01"></a>E-01 | Google Cloud Blog — How to use Gemini Live API Native Audio in Vertex AI | [링크](https://cloud.google.com/blog/topics/developers-practitioners/how-to-use-gemini-live-api-native-audio-in-vertex-ai) | IR/발표 | 2026 | [A] |
| <a id="ref-e-02"></a>E-02 | Huawei — Next-Generation Voice Virtual Agents for AICC (MWC 2026 공식 발표) | [링크](https://www.huawei.com/en/news/2026/3/mwc-voice-interaction-aicc) | IR/발표 | 2026-03-02 | [A] |
| <a id="ref-p-01"></a>P-01 | Gao et al. — Full-Duplex-Bench: A Benchmark to Evaluate Full-duplex Spoken Dialogue Models on Turn-taking Capabilities | [링크](https://arxiv.org/abs/2503.04721) | paper | 2025-03-06 | [A] |
| <a id="ref-p-02"></a>P-02 | Tu et al. (Meta AI & UW) — Beyond Turn-Based Interfaces: Synchronous LLMs as Full-Duplex Dialogue Agents (SyncLLM) | [링크](https://arxiv.org/abs/2409.15594) | paper | 2024-09 | [A] |
| <a id="ref-p-03"></a>P-03 | NVIDIA ADLR — PersonaPlex: Voice and Role Control for Full Duplex Conversational AI | [링크](https://research.nvidia.com/labs/adlr/files/personaplex/personaplex_preprint.pdf) | paper | 2026-01 | [A] |
| <a id="ref-p-04"></a>P-04 | Full-Duplex-Bench-v2: A Multi-Turn Evaluation Framework for Duplex Dialogue Systems with an Automated Examiner | [링크](https://arxiv.org/abs/2510.07838) | paper | 2025-10 | [A] |
| <a id="ref-p-05"></a>P-05 | ASLP-lab et al. — The ICASSP 2026 HumDial Challenge: Benchmarking Human-like Spoken Dialogue Systems | [링크](https://arxiv.org/abs/2601.05564) | paper | 2026-02-04 | [A] |
| <a id="ref-p-06"></a>P-06 | Chen et al. (FireRedTeam) — FireRedChat: A Pluggable, Full-Duplex Voice Interaction System | [링크](https://arxiv.org/abs/2509.06502) | paper | 2025-09 | [A] |
