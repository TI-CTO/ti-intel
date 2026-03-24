---
type: weekly-deep-research
topic: voice-synthesis
date: 2026-03-24
parent: 2026-03-24_weekly-voice-ai.md
agent: research-deep
confidence: high
sources_used: [websearch, webfetch]
---

# Deep 리서치: Voice Synthesis (2026-W13)

## 이전 대비 변화

- **전주 (W12, 2026-03-17)**: Big Tech 반격 — Google Gemini 2.5 Text-to-Speech (TTS) 멀티스피커+실시간 번역(70언어), OpenAI gpt-4o-mini-tts Word Error Rate (WER) 35% 감소, Anthropic ElevenLabs TTS Original Equipment Manufacturer (OEM) 채택, Cartesia Sonic 3 Amazon Web Services (AWS) SageMaker 통합, Inworld TTS-1.5-Max ELO 1위(1,160점).
- **금주 (W13, 2026-03-24)**: 플랫폼 전환 완성 단계 — Hume Octave 2 감정 TTS 정식 출시(11언어, 200ms 이하, Octave 1 대비 50% 가격 인하), ElevenLabs 11.ai MCP 음성 비서 알파 공개(Conversational AI + Model Context Protocol (MCP) 통합), Eleven v3 General Availability (GA) 확정(2026-03-14, 70+ 언어, Audio Tags, 오류율 68% 감소), Gemini 2.5 TTS Flash+Pro 업그레이드 버전 출시(Native Audio 개선), Microsoft Azure Dragon HD Omni 프리뷰(700+ 음성, 150+ 언어). 오픈소스 측에서는 Kitten TTS v0.8(15M~80M 파라미터 CPU 실행)이 에지 디바이스 시장 공략.
- **변화 방향**: "모델 성능 경쟁"에서 "플랫폼·에이전트 통합 경쟁"으로 완전 전환. TTS 기능이 AI 어시스턴트·음성 에이전트의 내장 레이어로 흡수되는 구조적 변화 가속. 감정 표현력과 멀티스피커 제어가 차세대 차별화 요소로 부상.

---

## 기술 동향

1. **Hume Octave 2 — 감정 인지 TTS 2세대, 200ms 이하 멀티링궐 출시.**
   Hume AI가 Octave 2를 정식 출시했다. 1세대 대비 40% 빠른 200ms 미만 레이턴시, 11개 언어 지원(아랍어·영어·프랑스어·독일어·힌디어·이탈리아어·일본어·한국어·포르투갈어·러시아어·스페인어), 가격 50% 인하를 동시 달성했다. 기술적 차별점은 스크립트의 서사적 맥락을 읽어 속삭임·큰 외침·침착한 설명 등 발화 방식을 자동 추론하는 감정 이해 레이어다. 신규 기능으로 Voice Conversion(음성 변환)과 직접 음소 편집(Phoneme Editing)이 추가됐다. 향후 20개 이상 언어 확대 계획이 공개됐다. [[G-01]](#ref-g-01) [[G-02]](#ref-g-02)

2. **ElevenLabs 11.ai 알파 — MCP 통합 음성 우선 AI 어시스턴트 공개.**
   ElevenLabs가 11.ai를 알파 버전으로 무료 공개했다. Conversational AI 엔진 위에 MCP를 결합해 Salesforce·HubSpot·Gmail·Zapier·Slack·Google Calendar 등 외부 서비스를 음성 명령으로 제어한다. 기존 음성 비서와의 차별점은 멀티턴 맥락 유지 능력으로, 이전 발화에서 얻은 정보를 이후 태스크에 연속 적용한다. 사용자 정의 MCP 서버 연결도 지원한다. 현재는 피드백 수집 목적의 개념 증명(Proof of Concept) 단계다. [[G-03]](#ref-g-03) [[G-04]](#ref-g-04)

3. **Eleven v3 GA 확정 — 70+ 언어, Audio Tags, 오류율 4.9%로 감소.**
   ElevenLabs의 Eleven v3가 2026년 3월 14일 정식 GA 전환됐다. 핵심 개선점은 세 가지다. (1) Audio Tags: `[excited]`, `[whispers]`, `[sighs]`, `[clapping]`, `[American accent]` 등 대괄호 태그로 감정·음향 효과·억양 전환을 직접 지시. (2) Text to Dialogue Application Programming Interface (API): JSON 배열로 화자 교체 구조를 입력하면 자연스러운 오버래핑 대화를 자동 생성. (3) 정확도: 테스트에서 이전 알파 대비 72% 선호, 오류율 15.3% → 4.9%로 68% 감소. 에이전트용 Conversational v3 모델도 추가됐다. [[G-05]](#ref-g-05) [[G-06]](#ref-g-06)

4. **Gemini 2.5 TTS Native Audio 업그레이드 — 멀티턴 대화·실시간 번역 확대.**
   Google이 Gemini 2.5 Flash Native Audio 업그레이드 버전을 출시했다. 핵심 변화는 멀티턴 맥락 유지(이전 대화 컨텍스트 참조)와 Function Calling 정확도 향상이다. TTS 측면에서는 Flash TTS·Pro TTS 모델의 표현력·페이싱 정밀도·멀티스피커 일관성이 개선됐다. Gemini Live와 Search Live로의 통합도 시작됐다. 별도로 실시간 Speech-to-Speech 번역은 Google Translate 앱(Android)에서 베타 제공 중이며, iOS 확대 및 Gemini API 노출은 2026년 중 예정이다. [[G-07]](#ref-g-07) [[G-08]](#ref-g-08)

5. **Microsoft Azure Dragon HD Omni 프리뷰 — 통합 모델로 700+ 음성 제공.**
   Microsoft가 Azure Speech의 신규 음성 유형 Dragon HD Omni를 2026년 1월 12일 프리뷰 출시했다. 기존 다중 모델 구조를 단일 통합 모델로 전환해 700개 이상의 고품질 음성, 150개 이상 언어·로케일을 하나의 모델에서 제공한다. 개발자 측면에서는 SSML 튜닝 부담 절감이 핵심 소구점이다. 기존 Azure Neural TTS 600+ 음성 포트폴리오를 Dragon HD Omni로 통합 마이그레이션하는 경로도 공개됐다. [[G-09]](#ref-g-09)

6. **Kitten TTS v0.8 — 15M~80M 파라미터 오픈소스 에지 TTS, CPU 실행.**
   KittenML이 2026년 3월 19일 Kitten TTS v0.8을 오픈소스로 공개했다. 세 가지 모델(15M·40M·80M 파라미터)이 CPU에서 실시간 실행 가능하도록 설계됐다. 이는 Kyutai Pocket TTS(100M, 2026-01)에 이어 초경량 에지 TTS 경쟁이 심화되고 있음을 보여준다. 상용 TTS API의 대역폭 비용 없이 온디바이스 음성 합성을 가능케 하는 기술 트렌드다. [[G-10]](#ref-g-10) [[G-11]](#ref-g-11)

7. **Inworld TTS-1.5-Max — 벤치마크 1위 유지, 실시간 에이전트 스택 공식화.**
   Inworld이 2026년 TTS API 벤치마크 리포트를 발표했다. Artificial Analysis Speech Arena에서 ELO 1,160으로 1위를 유지하고 있으며, Time-to-First-Audio P90 레이턴시 250ms 이하, Inworld 기준 ElevenLabs 대비 20배 저렴한 $10/1M chars를 강조한다. 실시간 음성 에이전트용 TTS 스택 가이드라인도 공개했으며, 음성 에이전트 레이턴시 허용치로 TTFB 100~200ms 이하를 업계 표준으로 제시하고 있다. [[G-12]](#ref-g-12) [[G-13]](#ref-g-13)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| **Hume AI** | Octave 2 정식 출시. 11언어, 200ms 이하 레이턴시, Octave 1 대비 50% 가격 인하. Voice Conversion·Phoneme Editing 신규 기능 추가. 향후 20개 이상 언어 확대 예정. | [[G-01]](#ref-g-01) [[G-02]](#ref-g-02) |
| **ElevenLabs** | 11.ai MCP 음성 비서 알파 공개(무료). Eleven v3 GA(2026-03-14): 70+ 언어, Audio Tags, 오류율 68% 감소. 일본 법인 ElevenLabs G.K. 설립, 81PRODUCE와 파트너십(성우 AI 음성 보존·29개 언어 로컬라이제이션). $500M Series D(2026-02-04), 기업 가치 $11B. | [[G-03]](#ref-g-03) [[G-05]](#ref-g-05) [[G-06]](#ref-g-06) [[G-14]](#ref-g-14) [[G-15]](#ref-g-15) [[G-16]](#ref-g-16) |
| **Google** | Gemini 2.5 Flash Native Audio 업그레이드(멀티턴 맥락, Function Calling 개선). Flash TTS/Pro TTS 표현력·멀티스피커 개선. Gemini Live·Search Live 통합 시작. 실시간 Speech-to-Speech 번역 Google Translate 베타(Android). | [[G-07]](#ref-g-07) [[G-08]](#ref-g-08) |
| **Microsoft** | Azure Dragon HD Omni 프리뷰(2026-01-12). 단일 통합 모델로 700+ 음성·150+ 언어 제공. SSML 튜닝 부담 대폭 절감. GitHub VibeVoice 오픈소스 프론티어 음성 AI 프로젝트 공개. | [[G-09]](#ref-g-09) |
| **Inworld** | TTS-1.5-Max ELO 1,160 1위 유지. TTFB P90 250ms 이하. $10/1M chars 가격 정책 유지. WaveSpeed AI를 통한 Max·Mini 버전 제공. | [[G-12]](#ref-g-12) [[G-13]](#ref-g-13) |
| **Cartesia** | Sonic 3 AWS SageMaker JumpStart 통합(2026-02). Sonic Turbo TTFB 40ms, 표준 Sonic 3 TTFB 90ms. 42개 언어, 15초 레퍼런스로 화자 복제. 자연 웃음·감정 포함 실시간 동작. | [[G-17]](#ref-g-17) |
| **Deepgram** | Aura-2 다국어 확장(네덜란드어·프랑스어·독일어·이탈리아어·일본어 추가). TTFB P90 200ms 이하 유지. $0.030/1,000자. 엔터프라이즈 온프레미스 배포 옵션 제공. | [[G-18]](#ref-g-18) |
| **KittenML** | Kitten TTS v0.8 오픈소스 공개(2026-03-19). 15M~80M 파라미터, CPU 실행 가능. 에지 디바이스 음성 합성 시장 공략. | [[G-10]](#ref-g-10) |
| **Meta** | PlayAI 인수(2025-07) 이후 음성 AI 팀 내재화 완료. 팀 전체(35명) Meta Superintelligence Lab 편입. Ray-Ban 스마트글래스·Meta AI·Quest VR 음성 통합 가속화 목적. | [[G-19]](#ref-g-19) |

---

## 시장 시그널

- ElevenLabs가 2026년 2월 4일 Sequoia Capital 주도 $500M Series D를 마감했다. 기업 가치 $11B으로 전년 대비 3배 이상 상승, 누적 조달액 $781M. ARR(연간 반복 매출) $330M(2025년 말 기준)이며, 자금은 감정형 대화 모델·더빙·Audio General Intelligence 연구에 집중 투입된다 [[G-15]](#ref-g-15) [[G-16]](#ref-g-16).
- Meta가 2025년 7월 PlayAI를 인수해 음성 AI 역량을 내재화했다. 인수 규모 비공개. PlayAI 팀 35명 전원 Meta Superintelligence Lab 합류 [[G-19]](#ref-g-19).
- PolyAI가 2025년 12월 $86M Series D를 마감해 총 조달액 $200M+ 달성, 기업 가치 $750M으로 음성 에이전트 특화 플레이어 중 최대 규모 [[G-20]](#ref-g-20).
- 글로벌 AI 기반 음성 에이전트 시장 규모: 2024년 $2.4B → 2034년 $47.5B 전망(CAGR ~35%). TTS 단독 시장은 2030년 $20.4B 예상 [[G-20]](#ref-g-20).
- Voice AI 전체 섹션 2026년 1~3월 신규 에퀴티 조달액이 이미 2024년 연간 수준($371M)에 도달 [[G-20]](#ref-g-20).
- ElevenLabs 일본 법인(ElevenLabs G.K.) 설립 및 음성 탤런트 에이전시 81PRODUCE와 파트너십 체결로 일본 시장 본격 진출. Spark+와 콜센터 특화 일본어 음성 AI 공동 개발 [[G-14]](#ref-g-14).
- Deepgram이 $130M Series C를 조달해 엔터프라이즈 TTS·STT 스택 확장을 가속 [[G-20]](#ref-g-20).

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "Towards Controllable Speech Synthesis in the Era of Large Language Models: A Survey" (익명 외, 2024) | Large Language Model (LLM) 시대의 음성 합성 제어 가능성 서베이. 피치·에너지·속도·운율·음색·감정·스타일 등 제어 파라미터별 최신 방법론 체계화. | [[P-01]](#ref-p-01) |
| "TTS-Transducer: End-to-End Speech Synthesis with Neural Transducer" (익명 외, 2025) | 오디오 코덱 모델과 Neural Transducer를 결합한 end-to-end TTS 신규 아키텍처 제안. 기존 두 단계 파이프라인(음향 모델+보코더) 대비 레이턴시·품질 균형 개선. | [[P-02]](#ref-p-02) |
| "Toward Low-Latency End-to-End Voice Agents for Telecommunications Using Streaming ASR, Quantized LLMs, and Real-Time TTS" (익명 외, 2025) | 통신 분야 음성 에이전트 구현 위한 스트리밍 Automatic Speech Recognition (ASR) + 양자화 LLM + 실시간 TTS 통합 파이프라인 연구. 엔드투엔드 레이턴시 최소화 방법론 제시. | [[P-03]](#ref-p-03) |

---

## 전략적 시사점

**기술 트렌드**
- TTS 기술의 기능 차별화는 음질/레이턴시에서 감정 표현·멀티스피커·맥락 인식으로 이동 중이다. Hume Octave 2와 ElevenLabs Eleven v3 모두 감정/음향 제어 레이어가 핵심 차별화 요소다.
- 오픈소스 초경량 TTS(Kitten TTS 15M, Kyutai Pocket TTS 100M)의 CPU 실행 가능화로 온디바이스·에지 음성 합성이 현실화됐다. 상용 API 의존도 낮추는 전략적 대안이 등장한 것이다.
- MCP 프로토콜이 음성 에이전트의 외부 서비스 통합 표준으로 빠르게 자리 잡고 있다. ElevenLabs 11.ai가 선례를 만들면서, TTS가 단순 발화 레이어에서 에이전트 제어 레이어로 확장됐다.

**기회**
- ElevenLabs 일본 법인 설립과 한국어를 포함한 Octave 2 11개 언어 지원은, 아시아 통신사가 로컬 음성 AI 서비스에 글로벌 플레이어 솔루션을 OEM 채택하는 시나리오를 현실화한다.
- 실시간 Speech-to-Speech 번역(Google 70언어)은 통신사 국제 로밍/통화 서비스에 적용 가능한 킬러 피처다. 통신 인프라와의 통합이 선점 기회.
- Azure Dragon HD Omni의 단일 통합 모델 접근법은 엔터프라이즈 고객의 SSML 튜닝 비용을 낮추는 방향으로, 기업용 음성 서비스 구축 비용이 대폭 감소하는 시점이 도래하고 있다.

**위협**
- ElevenLabs $500M, Inworld·Deepgram·PolyAI 등 대규모 자금 조달이 집중되면서 글로벌 플레이어의 가격 압박과 기능 고도화 속도가 국내 음성 AI 플레이어에게 구조적 위협이 되고 있다.
- Meta의 PlayAI 인수, Anthropic의 ElevenLabs OEM 채택 등 빅테크가 음성 AI를 직접 내재화하거나 포섭하는 움직임이 독립 TTS 스타트업의 생존 공간을 좁히고 있다.
- Kitten TTS·Kyutai Pocket TTS 등 오픈소스 초경량 모델의 품질이 상용 수준에 근접하면서, API 과금 모델 기반 수익 구조의 지속 가능성에 중장기 위협이 되고 있다.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Hume AI — Octave 2 launch blog | [링크](https://www.hume.ai/blog/octave-2-launch) | blog | 2025-10-01 | [B] |
| <a id="ref-g-02"></a>G-02 | Hume AI on X — Octave 2 announcement | [링크](https://x.com/hume_ai/status/1973450822840152455) | news | 2026-03 | [B] |
| <a id="ref-g-03"></a>G-03 | ElevenLabs — Introducing 11.ai | [링크](https://elevenlabs.io/blog/introducing-11ai) | blog | 2026-03 | [A] |
| <a id="ref-g-04"></a>G-04 | The Decoder — ElevenLabs launches 11ai with MCP integration | [링크](https://the-decoder.com/elevenlabs-launches-11ai-a-voice-assistant-that-uses-mcp-to-integrate-with-digital-workflow-tools/) | news | 2026-03 | [B] |
| <a id="ref-g-05"></a>G-05 | ElevenLabs — Eleven v3 is Now Generally Available | [링크](https://elevenlabs.io/blog/eleven-v3-is-now-generally-available) | blog | 2026-03-14 | [A] |
| <a id="ref-g-06"></a>G-06 | ElevenLabs — What are Eleven v3 Audio Tags | [링크](https://elevenlabs.io/blog/v3-audiotags) | blog | 2026-03 | [A] |
| <a id="ref-g-07"></a>G-07 | Google Blog — Gemini 2.5 Native Audio upgrade, plus text-to-speech model updates | [링크](https://blog.google/products/gemini/gemini-audio-model-updates/) | blog | 2026-03 | [A] |
| <a id="ref-g-08"></a>G-08 | TechFinitive — Google's Gemini in fine voice with new speech-to-speech translation | [링크](https://www.techfinitive.com/googles-gemini-in-fine-voice-with-new-speech-to-speech-translation-and-native-audio-refresh/) | news | 2026-03 | [B] |
| <a id="ref-g-09"></a>G-09 | Microsoft Community Hub — Introducing Dragon HD Omni: Azure Speech New Voice Type | [링크](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-dragon-hd-omni-azure-speech-new-voice-type-now-in-preview-via-micros/4481288) | blog | 2026-01-12 | [A] |
| <a id="ref-g-10"></a>G-10 | Sesame Disk — Kitten TTS: Open-Source Voice Synthesis for Edge Devices | [링크](https://sesamedisk.com/kitten-tts-open-source-voice-synthesis/) | news | 2026-03-19 | [C] |
| <a id="ref-g-11"></a>G-11 | Conzit — Introducing Kitten TTS v0.8: Compact, Efficient Voice Synthesis | [링크](https://conzit.com/post/introducing-kitten-tts-v08-compact-efficient-voice-synthesis) | news | 2026-03-19 | [C] |
| <a id="ref-g-12"></a>G-12 | Inworld — Best TTS APIs for Real-Time Voice Agents (2026 Benchmarks) | [링크](https://inworld.ai/resources/best-voice-ai-tts-apis-for-real-time-voice-agents-2026-benchmarks) | blog | 2026 | [B] |
| <a id="ref-g-13"></a>G-13 | Inworld — Inworld TTS-1.5 blog | [링크](https://inworld.ai/blog/introducing-inworld-tts-1-5) | blog | 2026 | [A] |
| <a id="ref-g-14"></a>G-14 | ElevenLabs — ElevenLabs establishes Japanese Subsidiary ElevenLabs G.K. | [링크](https://elevenlabs.io/blog/elevenlabs-establishes-japanese-subsidiary-elevenlabs-gk) | blog | 2026-03 | [A] |
| <a id="ref-g-15"></a>G-15 | ElevenLabs — ElevenLabs raises $500M Series D | [링크](https://elevenlabs.io/blog/series-d) | blog | 2026-02-04 | [A] |
| <a id="ref-g-16"></a>G-16 | TechCrunch — ElevenLabs raises $500M from Sequoia at $11 billion valuation | [링크](https://techcrunch.com/2026/02/04/elevenlabs-raises-500m-from-sequioia-at-a-11-billion-valuation/) | news | 2026-02-04 | [B] |
| <a id="ref-g-17"></a>G-17 | AWS — Cartesia Sonic 3 now available on Amazon SageMaker JumpStart | [링크](https://aws.amazon.com/about-aws/whats-new/2026/02/cartesia-sonic-3-on-sagemaker-jumpstart/) | blog | 2026-02 | [A] |
| <a id="ref-g-18"></a>G-18 | Deepgram — Aura-2 now speaks Dutch, French, German, Italian, and Japanese | [링크](https://deepgram.com/learn/aura-2-now-speaks-dutch-french-german-italian-japanese) | blog | 2026 | [A] |
| <a id="ref-g-19"></a>G-19 | TechCrunch — Meta acquires voice startup Play AI | [링크](https://techcrunch.com/2025/07/13/meta-acquires-voice-startup-play-ai/) | news | 2025-07-13 | [B] |
| <a id="ref-g-20"></a>G-20 | AssemblyAI — Voice AI in 2026: Inside the companies and investments | [링크](https://www.assemblyai.com/blog/voice-ai-in-2026-series-1) | blog | 2026 | [B] |
| <a id="ref-p-01"></a>P-01 | 익명 외 — Towards Controllable Speech Synthesis in the Era of LLMs: A Survey | [링크](https://arxiv.org/html/2412.06602v1/) | paper | 2024-12 | [A] |
| <a id="ref-p-02"></a>P-02 | 익명 외 — TTS-Transducer: End-to-End Speech Synthesis with Neural Transducer | [링크](https://arxiv.org/html/2501.06320) | paper | 2025-01 | [A] |
| <a id="ref-p-03"></a>P-03 | 익명 외 — Toward Low-Latency End-to-End Voice Agents for Telecommunications | [링크](https://arxiv.org/html/2508.04721v1) | paper | 2025 | [A] |
