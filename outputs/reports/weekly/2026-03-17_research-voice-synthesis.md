---
type: weekly-research
topic: voice-synthesis
domain: voice-ai
date: 2026-03-17
agent: research-deep
confidence: high
sources_used: [websearch, websearch-fetch]
---

# Voice Synthesis — Deep 리서치 (W12)

> **조사 기간**: 2026-03-10 ~ 2026-03-17
> **핵심 발견**: 이번 주의 핵심 변화는 Big Tech 주도 이동이다. 지난 주 오픈소스 경량 모델 폭발에 이어, Google·OpenAI·Anthropic이 각각 플랫폼 통합·성능 고도화·생태계 포섭 전략으로 대응했다. Google은 Gemini 2.5 TTS 멀티스피커 및 실시간 speech-to-speech 번역을 Developer API에 추가했고, OpenAI는 gpt-4o-mini-tts에서 35% WER 감소를 확인했다. Anthropic은 자체 TTS 대신 ElevenLabs를 OEM 채택해 Claude Code 음성모드를 출시했다. ElevenLabs는 SXSW에서 1M Voices 접근성 이니셔티브로 브랜드 포지셔닝을 사회적 임팩트로 전환했다.

---

## 이전 대비 변화

- **전주 (W11, 2026-03-11)**: 오픈소스 TTS 빅뱅 — Qwen3-TTS(97ms), Kani-TTS-2(3GB VRAM), Orpheus(감정태그), Kyutai Pocket TTS(100M/CPU). 네이버 HyperCLOVA X Omni 한국어 MOS 4.22. Gemini 2.5 TTS GA 시작. ElevenLabs Eleven v3 Audio Tags 출시.
- **금주 (W12, 2026-03-17)**: Big Tech 반격 — Google Gemini 2.5 TTS 멀티스피커+실시간 번역 추가(24언어), OpenAI gpt-4o-mini-tts WER 35% 감소+Custom Voices 개선, Anthropic Claude Code 음성모드 출시(ElevenLabs TTS 채택), ElevenLabs 1M Voices 접근성 이니셔티브(SXSW), Cartesia Sonic 3 AWS SageMaker JumpStart 통합. 품질 벤치마크: Inworld TTS-1.5-Max ELO 1,160 1위.
- **변화 방향**: 기술 경쟁 축이 "모델 성능" → "플랫폼 통합+사용 생태계"로 이동. AI 어시스턴트(Claude, ChatGPT)의 음성모드 내장이 TTS 산업 구조를 재편하는 핵심 벡터로 부상. 오픈소스 경량 모델의 품질 추격으로 상용 API의 가격 경쟁 압력 가중.

---

## 기술 동향

1. **Google Gemini 2.5 TTS — 멀티스피커 + 실시간 Speech-to-Speech 번역 추가 (2026-03월).** Gemini 2.5 Flash TTS와 Pro TTS에 세 가지 업그레이드를 적용했다. (1) Enhanced Expressivity: 더 풍부한 톤 다양성과 스타일 프롬프트 준수도 향상. (2) Precision Pacing: 맥락 인식 자동 속도 조절과 지시 이행력 개선. (3) Multi-Speaker: 멀티 화자 시나리오에서 캐릭터 음성 일관성 유지. 24개 언어 지원. 별도로 Gemini의 Native Audio 기능을 통해 실시간 Speech-to-Speech 번역(70개 언어, 2,000개 언어쌍)이 Google Translate 앱에 적용되어, 헤드폰 사용 시 화자의 억양·속도·피치를 보존하며 실시간 번역. [[G-01]](#ref-g-01) [[G-02]](#ref-g-02) [[G-03]](#ref-g-03)

2. **OpenAI gpt-4o-mini-tts — WER 35% 감소, Custom Voices 정확도 향상 (2025-12-22 출시, 이번 주 확산 반영).** `gpt-4o-mini-tts-2025-12-15` 스냅샷 기준 Common Voice·FLEURS 벤치마크에서 약 35% 낮은 WER 달성. Multilingual LibriSpeech에서도 일관된 개선. Custom Voices에서 더 자연스러운 톤, 레퍼런스 샘플 충실도 향상, 방언 정확도 개선. 가격은 이전 스냅샷과 동일. 중국어·힌디어·벵갈어·일본어·인도네시아어·이탈리아어 특히 강화. [[G-04]](#ref-g-04) [[G-05]](#ref-g-05)

3. **Anthropic Claude Code 음성모드 — ElevenLabs TTS OEM 채택 (2026-03-03 출시, W12 가시화).** Anthropic은 자체 TTS 모델 개발 대신 ElevenLabs를 TTS 하청업체(subcontractor)로 이용약관에 명시했다. Claude Code 음성모드에서 Buttery·Airy·Mellow·Glassy·Rounded 5개 음성 선택 가능. 2026-03-03 점진적 출시(초기 5% 사용자 대상), 엔지니어 Thariq Shihipar가 X에 공개. 현재 영어 중심, 다국어 확장 계획 언급. [[G-06]](#ref-g-06) [[G-07]](#ref-g-07) [[G-08]](#ref-g-08)

4. **ElevenLabs '1 Million Voices' 이니셔티브 (SXSW 2026-03-11).** 영구 음성 손실 환자 100만 명에게 음성 복원 기술을 무료 제공하는 이니셔티브 발표($1B in-kind 가치). '11 Voices' 다큐시리즈(ALS, 뇌졸중, 뇌손상 환자 11인이 자신의 AI 복원 음성으로 직접 내레이션) SXSW 초연. 현재 7,000명 지원 완료, 800+ NPO·통신 파트너, 49개국 커버리지. 배우 Eric Dane(ALS, 작고)의 음성 복원 사례가 대표 스토리. [[G-09]](#ref-g-09) [[G-10]](#ref-g-10)

5. **Cartesia Sonic 3 — AWS SageMaker JumpStart 통합 (2026-02월).** State Space Model(SSM) 기반 Sonic 3가 Amazon SageMaker JumpStart에 통합되어 엔터프라이즈 배포 허들 낮아짐. Sonic Turbo는 TTFB 40ms로 업계 최저 지연, 표준 Sonic 3는 90ms. 42개 언어 지원, 15초 레퍼런스 오디오로 화자 복제. 자연스러운 웃음·감정 포함 상태에서도 실시간 동작. [[G-11]](#ref-g-11) [[G-12]](#ref-g-12)

6. **Inworld TTS — 품질 벤치마크 1위 (ELO 1,160).** Inworld TTS-1.5-Max가 Artificial Analysis Speech Arena 블라인드 비교 테스트에서 ELO 1,160으로 1위 확인(ElevenLabs Multilingual v2 ELO 1,105, OpenAI TTS-1 ELO 1,111 상회). HuggingFace TTS Arena에서는 Vocu V3.0(ELO 1,600)이 1위, Inworld TTS MAX가 ELO 1,576으로 2위. 가격 측면에서는 ElevenLabs 대비 20배 이상 저렴하다고 자사 주장. [[G-13]](#ref-g-13) [[G-14]](#ref-g-14)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| **Google** | Gemini 2.5 Flash/Pro TTS에 멀티스피커·Enhanced Expressivity·Precision Pacing 추가. 24언어 지원. Native Audio로 실시간 Speech-to-Speech 번역 70언어·2,000언어쌍 지원(Google Translate 앱 적용 중). | [[G-01]](#ref-g-01) [[G-02]](#ref-g-02) [[G-03]](#ref-g-03) |
| **OpenAI** | gpt-4o-mini-tts-2025-12-15 스냅샷: WER 35% 감소(Common Voice/FLEURS), Custom Voices 자연스러움·방언 정확도 향상. 가격 동결. Azure AI Foundry에서도 동일 모델 제공. | [[G-04]](#ref-g-04) [[G-05]](#ref-g-05) |
| **Anthropic** | Claude Code 음성모드 출시(2026-03-03). TTS는 ElevenLabs 기술 채택(자체 모델 없음). 초기 5% 사용자 대상 점진적 확대. 5개 음성 선택지 제공. | [[G-06]](#ref-g-06) [[G-07]](#ref-g-07) [[G-08]](#ref-g-08) |
| **ElevenLabs** | SXSW '1 Million Voices' 이니셔티브 발표(2026-03-11). $1B in-kind 투자, 100만 명 음성 복원 목표. 7,000명·800+ NPO 기지 확보. Eleven v3 Audio Tags 상업화 지속. Anthropic 파트너로서 AI 어시스턴트 TTS 생태계 내재화. | [[G-09]](#ref-g-09) [[G-10]](#ref-g-10) |
| **Cartesia** | Sonic 3 AWS SageMaker JumpStart 통합(2026-02월). TTFB 40ms(Turbo) 유지. 42언어, 15초 클로닝, SSM 아키텍처 차별화. 엔터프라이즈 채널 확대 중. | [[G-11]](#ref-g-11) [[G-12]](#ref-g-12) |
| **Inworld AI** | TTS-1.5-Max ELO 1,160으로 Artificial Analysis 벤치마크 1위. ElevenLabs 대비 20배 이상 저렴한 가격 정책. 실시간 음성 에이전트 특화 포지셔닝. | [[G-13]](#ref-g-13) [[G-14]](#ref-g-14) |
| **Microsoft Azure** | Azure AI Foundry에 OpenAI gpt-4o-mini-tts 포함 최신 오디오 모델 제공. 자체 Neural TTS 440+ 음성·140+ 언어 유지. 엔터프라이즈 Custom Neural Voice 독점적 강점. | [[G-04]](#ref-g-04) [[G-15]](#ref-g-15) |
| **Naver (CLOVA)** | HyperCLOVA X Omni 한국어 TTS MOS 4.22(전주 기록 유지). 이번 주 신규 발표 없음. CLOVA Voice API 엔터프라이즈 서비스 지속. | — |

---

## 시장 시그널

- AI 음성 생성기 시장: 2025년 $4.16B → 2031년 $20.71B 전망, CAGR 30.7% [단일 소스, [D]]
- ElevenLabs SXSW '1M Voices' 이니셔티브: TTS 기업이 기술 상용화 외 사회적 임팩트 내러티브를 전략적으로 채택하는 첫 대형 사례 — 브랜드 포지셔닝 차별화 신호 [[G-09]](#ref-g-09)
- Anthropic의 ElevenLabs TTS 채택은 "LLM 리더들이 TTS를 아웃소싱한다"는 구조적 시그널: 자체 TTS 개발 없이도 음성 기능을 제공하는 "TTS-as-Infrastructure" 모델 확산 [[G-06]](#ref-g-06) [[G-07]](#ref-g-07)
- Cartesia Sonic 3 AWS SageMaker 통합: 독립 TTS API 기업이 클라우드 메가플랫폼 마켓플레이스를 통한 엔터프라이즈 진입 전략 채택 [[G-11]](#ref-g-11)
- 벤치마크 파편화: Artificial Analysis(Inworld 1위 ELO 1,160) vs HuggingFace TTS Arena(Vocu V3 1위 ELO 1,600) 등 리더보드별 결과 불일치 — 기업들이 자사에 유리한 벤치마크를 선별 인용하는 현상 가속 [[G-13]](#ref-g-13)
- 규제 타임라인 재확인: EU AI Act Article 50(합성음 라벨링) 2026-08-02 발효, 미국 뉴욕주 합성 퍼포머 공시 의무 2026-06 시행 — 엔터프라이즈 TTS 도입 시 컴플라이언스 스택 요구 확대 [[G-16]](#ref-g-16) [[G-17]](#ref-g-17)
- 실시간 TTS 지연 벤치마크 표준화: Cartesia 40ms, ElevenLabs 75ms, Inworld <250ms, CosyVoice2 150ms — 음성 에이전트 요건 기준(800ms 이상 시 사용자 인지 지연)에서 상위권 모두 충분한 수준 도달 [[G-12]](#ref-g-12) [[G-18]](#ref-g-18)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Causal Prosody Mediation for TTS (Mohanty, 2026-03-12) | FastSpeech2에 인과 구조 모델 추가. 감정 조건화로 운율 조작 가능. MOS 및 감정 분류 정확도 향상. 반사실적 학습으로 운율 속성 분리 가능 | [[P-01]](#ref-p-01) |
| DS-TTS: Zero-Shot Speaker Style Adaptation (2026) | 단일 오디오 샘플만으로 화자 음성 합성. Dual-Style Encoding + Dynamic Generator 구조. VCTK에서 WER 및 화자 유사도 모두 SotA 초과 | [[P-02]](#ref-p-02) |
| DiffGAN-ZSTTS: High Fidelity Zero-Shot TTS (Nature, 2025) | FastSpeech2 기반 + 확산 디코더. 미등장 화자에 대한 제너럴라이제이션 향상. 고충실도 제로샷 화자 적응 달성 | [[P-03]](#ref-p-03) |
| CosyVoice 2 (FunAudioLLM, 2024-12) | Finite-scalar quantization + 사전학습 LLM 백본 + Causal Flow Matching. 스트리밍 150ms, 발음 오류 30~50% 감소, MOS 5.4→5.53 향상 | [[P-04]](#ref-p-04) |
| Towards Controllable Speech Synthesis in the Era of LLMs: Survey (2024-12) | 감정·운율·음색·길이 등 세밀 제어 방법론 종합 서베이. LLM 시대 제어 가능 TTS 아키텍처 분류 체계 제안 | [[P-05]](#ref-p-05) |

---

## 전략적 시사점

**기회**

- Anthropic의 ElevenLabs OEM 채택은 "LLM 기업에 TTS를 B2B로 납품"하는 새로운 수익 모델이 유효함을 검증. 한국 LLM 기업(Naver HyperCLOVA 등)에도 유사 파트너십 기회 존재
- Google Gemini Speech-to-Speech 번역(70언어·2,000쌍)이 Google Translate 앱에 통합되면 한국어 통·번역 제품에서 직접 경쟁 구도 형성 — 국내 플레이어에 위협이자 API 활용 기회
- 실시간 Voice Agent 시장(콜센터, 고객지원)에서 Cartesia·Inworld 등 저지연 특화 모델이 점유율 확보 중 — 음성 에이전트 솔루션 레이어에서의 차별화 포인트

**위협**

- Big Tech(Google, OpenAI, Microsoft)의 TTS 기능이 자사 플랫폼(Gemini API, Azure AI Foundry)에 번들로 통합됨에 따라 독립 TTS API 기업의 가격 경쟁력 및 고객 유지 위협 가중
- EU AI Act Article 50(2026-08) 및 미국 뉴욕주(2026-06) 합성음 라벨링 의무 시행 — 컴플라이언스 미비 시 B2B 엔터프라이즈 계약 리스크 발생
- 오픈소스 경량 TTS(Kyutai Pocket TTS 100M, Kokoro 82M, CosyVoice2-0.5B)의 품질이 상용 수준에 근접 — 온프레미스 배포 선호 엔터프라이즈 고객의 API 종속 탈피 가속화 우려

---

## 신뢰도 평가

- **높은 확신 [A/B]**: Google Gemini 2.5 TTS 업그레이드(공식 블로그), OpenAI gpt-4o-mini-tts WER 35% 감소(공식 개발자 블로그), Anthropic ElevenLabs 채택(TechCrunch+The Decoder 교차), ElevenLabs SXSW PR 뉴스와이어, Cartesia AWS SageMaker 통합(AWS 공식 발표)
- **추가 검증 필요 [C/D]**: 시장 규모($4.16B→$20.71B) — 단일 소스, Inworld '20배 저렴' 주장 — 자사 자료, HuggingFace TTS Arena ELO 수치 — 집계 시점 불명확
- **데이터 공백**: Claude Code 음성모드의 지원 언어 수(20개 언어 여부 미확인), Google 실시간 번역 API 공개 시점(현재 제품 내장, API는 2026년 중 예정), Naver W12 신규 동향(공개 발표 없음), Kakao TTS W12 동향(공개 발표 없음)

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Google Blog — Gemini 2.5 Native Audio upgrade, plus text-to-speech model updates | [링크](https://blog.google/products/gemini/gemini-audio-model-updates/) | blog | 2025-12-12 | [A] |
| <a id="ref-g-02"></a>G-02 | Google Blog — Gemini 2.5 Text-to-Speech model updates | [링크](https://blog.google/technology/developers/gemini-2-5-text-to-speech/) | blog | 2025-12-12 | [A] |
| <a id="ref-g-03"></a>G-03 | TechFinitive — Google's Gemini in fine voice with speech-to-speech translation | [링크](https://www.techfinitive.com/googles-gemini-in-fine-voice-with-new-speech-to-speech-translation-and-native-audio-refresh/) | news | 2025-12-12 | [B] |
| <a id="ref-g-04"></a>G-04 | OpenAI Developer Blog — Updates for developers building with voice | [링크](https://developers.openai.com/blog/updates-audio-models/) | blog | 2025-12-22 | [A] |
| <a id="ref-g-05"></a>G-05 | OpenAI — Introducing next-generation audio models in the API | [링크](https://openai.com/index/introducing-our-next-generation-audio-models/) | blog | 2025-12-22 | [A] |
| <a id="ref-g-06"></a>G-06 | TechCrunch — Claude Code rolls out a voice mode capability | [링크](https://techcrunch.com/2026/03/03/claude-code-rolls-out-a-voice-mode-capability/) | news | 2026-03-03 | [B] |
| <a id="ref-g-07"></a>G-07 | The Decoder — Anthropic's Claude uses ElevenLabs technology for speech features | [링크](https://the-decoder.com/anthropics-claude-uses-elevenlabs-technology-for-speech-features-rather-than-an-in-house-model/) | news | 2026-03-03 | [B] |
| <a id="ref-g-08"></a>G-08 | Dataconomy — Anthropic Rolls Out New Voice Mode For Claude Code Assistant | [링크](https://dataconomy.com/2026/03/04/anthropic-rolls-out-new-voice-mode-for-claude-code-assistant/) | news | 2026-03-04 | [B] |
| <a id="ref-g-09"></a>G-09 | PR Newswire — ElevenLabs debuts '11 Voices' docuseries at SXSW | [링크](https://www.prnewswire.com/news-releases/elevenlabs-debuts-11-voices-docuseries-at-sxsw-as-part-of-global-campaign-to-reach-1-million-people-with-voice-loss-302711275.html) | news | 2026-03-11 | [A] |
| <a id="ref-g-10"></a>G-10 | ElevenLabs — On a mission to help 1 million people reclaim their voices | [링크](https://elevenlabs.io/impact-program) | blog | 2026-03-11 | [A] |
| <a id="ref-g-11"></a>G-11 | AWS — Cartesia Sonic-3 on Amazon SageMaker JumpStart | [링크](https://aws.amazon.com/about-aws/whats-new/2026/02/cartesia-sonic-3-on-sagemaker-jumpstart/) | news | 2026-02 | [A] |
| <a id="ref-g-12"></a>G-12 | Inworld AI — Best TTS APIs for Real-Time Voice Agents (2026 Benchmarks) | [링크](https://inworld.ai/resources/best-voice-ai-tts-apis-for-real-time-voice-agents-2026-benchmarks) | blog | 2026 | [C] |
| <a id="ref-g-13"></a>G-13 | Artificial Analysis — Text to Speech Leaderboard | [링크](https://artificialanalysis.ai/text-to-speech/leaderboard) | tool | 2026-03 | [B] |
| <a id="ref-g-14"></a>G-14 | Inworld AI — Inworld vs ElevenLabs: 20x Cheaper, Higher-Quality TTS | [링크](https://inworld.ai/resources/inworld-vs-elevenlabs) | blog | 2026 | [C] |
| <a id="ref-g-15"></a>G-15 | Microsoft Azure — Azure AI Speech pricing | [링크](https://azure.microsoft.com/en-us/pricing/details/speech/) | doc | 2026 | [A] |
| <a id="ref-g-16"></a>G-16 | AI Tribune — AI Voice Cloning Regulation in 2026 | [링크](https://aitribune.net/2026/02/24/ai-voice-cloning-regulation-in-2026/) | blog | 2026-02-24 | [B] |
| <a id="ref-g-17"></a>G-17 | WeVenture — AI labeling requirement starting in 2026 | [링크](https://weventure.de/en/blog/ai-labeling) | blog | 2026 | [B] |
| <a id="ref-g-18"></a>G-18 | Camb.ai — Real-Time TTS API for Low-Latency Speech Streaming, 2026 Guide | [링크](https://www.camb.ai/blog-post/real-time-tts-api-for-low-latency-speech-streaming) | blog | 2026 | [C] |
| <a id="ref-g-19"></a>G-19 | Google DeepMind — Advanced audio dialog and generation with Gemini 2.5 | [링크](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-2-5-native-audio/) | blog | 2025-12-12 | [A] |
| <a id="ref-g-20"></a>G-20 | Cartesia — Sonic 3 model page | [링크](https://cartesia.ai/sonic) | doc | 2026 | [A] |
| <a id="ref-g-21"></a>G-21 | PyVideoTrans — Gemini 2.5 Adds Multi-Speaker TTS, Available for Free | [링크](https://pyvideotrans.com/en/blog/geminitts) | blog | 2026-03 | [C] |
| <a id="ref-g-22"></a>G-22 | TestingCatalog — Google expands Gemini TTS with 24 languages, lifelike voices | [링크](https://www.testingcatalog.com/google-expands-gemini-tts-with-24-languages-lifelike-voices/) | news | 2026 | [B] |
| <a id="ref-g-23"></a>G-23 | Kyutai Labs — Pocket TTS GitHub (100M parameter, CPU, MIT license) | [링크](https://github.com/kyutai-labs/pocket-tts) | code | 2026-01 | [A] |
| <a id="ref-p-01"></a>P-01 | Mohanty — Causal Prosody Mediation for Text-to-Speech: Counterfactual Training of Duration, Pitch, and Energy in FastSpeech2 | [링크](https://arxiv.org/abs/2603.11683) | paper | 2026-03-12 | [A] |
| <a id="ref-p-02"></a>P-02 | DS-TTS — Zero-Shot Speaker Style Adaptation from Voice Clips via Dynamic Dual-Style Feature Modulation | [링크](https://arxiv.org/html/2506.01020v1) | paper | 2026 | [A] |
| <a id="ref-p-03"></a>P-03 | Scientific Reports — High fidelity zero shot speaker adaptation in TTS with denoising diffusion GAN | [링크](https://www.nature.com/articles/s41598-025-90507-0) | paper | 2025 | [A] |
| <a id="ref-p-04"></a>P-04 | FunAudioLLM — CosyVoice 2: Scalable Streaming Speech Synthesis with Large Language Models | [링크](https://arxiv.org/abs/2412.10117) | paper | 2024-12 | [A] |
| <a id="ref-p-05"></a>P-05 | Towards Controllable Speech Synthesis in the Era of LLMs: A Survey | [링크](https://arxiv.org/html/2412.06602v1/) | paper | 2024-12 | [A] |
