---
type: weekly-deep-research
topic: voice-synthesis
date: 2026-03-30
parent: 2026-03-30_weekly-voice-ai.md
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
---

# Deep 리서치: Voice Synthesis (2026-W14)

## 이전 대비 변화

- **전주 (W13, 2026-03-24)**: 플랫폼 전환 완성 단계 — Hume TADA 오픈소스(RTF 0.09, 환각 제로), ElevenLabs 11.ai MCP 음성 비서 알파, Google Gemini 2.5 TTS GA, Microsoft Dragon HD Omni 700+ 음성, Kitten TTS 25MB 엣지.
- **금주 (W14, 2026-03-30)**: 오픈웨이트 + 기업 파트너십 2중 공세 — Mistral Voxtral TTS 4B 오픈웨이트 출시(ElevenLabs 대비 68.4% 승률), xAI Grok Voice Agent Application Programming Interface (API) 런칭($0.05/min, Big Bench Audio 1위), ElevenLabs-IBM watsonx 파트너십(엔터프라이즈 음성 에이전트), Amazon Polly 10개 생성형 음성 GA + Bidirectional Streaming API 출시.
- **변화 방향**: "오픈소스 vs. 클라우드 API" 구도가 선명해짐. Mistral·xAI 진입으로 TTS 시장 경쟁이 새 단계 진입. 음성 에이전트 플랫폼 통합(IBM watsonx, LiveKit)이 대형 기업 도입 경로의 핵심으로 부상.

---

## 기술 동향

1. **Mistral Voxtral TTS — 4B 오픈웨이트, ElevenLabs 대비 68.4% 승률, $0.016/1k chars.**
   Mistral AI가 2026년 3월 26일 첫 Text-to-Speech (TTS) 모델 Voxtral TTS를 공개했다. arXiv 논문(2603.25551)과 함께 모델 가중치를 공개한 오픈웨이트 방식이다. 아키텍처는 Ministral 3B 디코더를 백본으로 삼은 하이브리드 구조로, 자동회귀(auto-regressive) 방식으로 시맨틱 토큰을 생성하고 플로우 매칭(flow-matching)으로 음향 토큰을 디코딩한다. Voxtral Codec은 VQ-FSQ 하이브리드 양자화를 사용한다. 3초 레퍼런스 오디오로 제로샷 음성 복제를 수행하며 크로스링궐(cross-lingual) 적응도 지원한다(예: 프랑스어 억양의 영어 생성). 지원 언어는 영어·프랑스어·독일어·스페인어·네덜란드어·포르투갈어·이탈리아어·힌디어·아랍어 9개 언어다. API 레이턴시는 10초 샘플/500자 기준 70ms이며, Time-to-First-Audio (TTFA)는 90ms다. 가격은 $0.016/1k chars로 ElevenLabs($0.11~) 대비 약 87% 저렴하다. 라이선스는 CC BY-NC 4.0이며 vLLM-Omni를 통해 서빙된다. 인간 평가에서 ElevenLabs Flash v2.5 대비 68.4% 승률을 기록했다. [[G-01]](#ref-g-01) [[G-02]](#ref-g-02) [[G-03]](#ref-g-03) [[P-01]](#ref-p-01)

2. **xAI Grok Voice Agent API — $0.05/min, Big Bench Audio 1위, OpenAI Realtime API 호환.**
   xAI가 2026년 3월 16일 Grok Text-to-Speech (TTS) API를 공개하고, 이어 Grok Voice Agent API를 런칭했다. TTS API는 Ara·Eve·Leo·Rex·Sal 5개 음성과 20+ 언어를 지원하며, MP3·WAV·PCM·G.711 μ-law·G.711 A-law 등 다양한 오디오 포맷을 제공한다. Voice Agent API는 OpenAI Realtime API 스펙과 호환되어 기존 생태계 이전 비용을 낮췄다. TTFA는 1초 미만으로 "가장 가까운 경쟁사 대비 5배 빠르다"고 주장하며, Big Bench Audio(음성 에이전트 추론 벤치마크) 1위를 기록했다. 가격은 접속 시간당 $0.05/min(분 단위 과금)이다. LiveKit 플러그인도 공식 제공하여 실시간 음성 에이전트 구축 경로를 단순화했다. [[G-04]](#ref-g-04) [[G-05]](#ref-g-05) [[G-06]](#ref-g-06)

3. **ElevenLabs-IBM watsonx 파트너십 — 엔터프라이즈 음성 에이전트에 프리미엄 TTS/STT 통합.**
   ElevenLabs와 IBM이 2026년 3월 25일 IBM watsonx Orchestrate에 ElevenLabs TTS·Speech-to-Text (STT) 역량을 통합하는 파트너십을 발표했다. 10,000개 이상 음성 라이브러리, 70개 언어 지원, PCI 컴플라이언스, Zero Retention Mode(HIPAA 지원), 데이터 레지던시 등 엔터프라이즈 보안 요건을 포함한다. 활용 사례는 고객 지원·영업·직원 워크플로우·정부 서비스다. 같은 날 Deepgram 또한 IBM watsonx Orchestrate의 첫 전용 음성 파트너로 실시간 전사·다국어 지원·STT·TTS를 통합했다(2026-02-24 발표, 3월 확대). 동일 플랫폼에 두 경쟁사가 동시 진입한 특이한 구도다. [[G-07]](#ref-g-07) [[G-08]](#ref-g-08) [[G-09]](#ref-g-09)

4. **Amazon Polly Generative TTS — 10개 음성 GA + Bidirectional Streaming API 신규 출시.**
   AWS가 2026년 3월 Generative TTS 엔진에 10개 고품질 음성(Tiffany·Brian·Aria·Jasmine·Florian·Ambre·Lorenzo·Beatrice·Lennart·Sabrina)을 추가하여 8개 로케일에서 GA(General Availability) 전환했다. 함께 출시한 Bidirectional Streaming API는 Large Language Model (LLM) 출력을 TTS에 실시간으로 파이핑(piping)하여 챗봇·게임 캐릭터 등 실시간 응용에 적합한 구조를 완성했다. 지원 리전도 Europe(London)과 Canada(Central)로 확대됐다. [[G-10]](#ref-g-10)

5. **ElevenLabs v3 GA 전환 — 70+ 언어, Audio Tags, 오류율 4.9%로 안정화.**
   ElevenLabs Eleven v3가 2026년 3월 14일 알파를 종료하고 GA로 전환됐다. 핵심 기능은 (1) Audio Tags(`[excited]`, `[whispers]`, `[sighs]`, `[American accent]`), (2) Text-to-Dialogue API(JSON 배열 멀티스피커 자동 생성), (3) 에이전트용 `eleven_v3_conversational` 추가다. 알파 대비 오류율 15.3% → 4.9%로 68% 감소, 사용자 선호도 72% 우위를 달성했다. [[G-11]](#ref-g-11) [[G-12]](#ref-g-12)

6. **Gemini 2.5 TTS 업데이트 — 감정 제어 강화, Pro/Flash 이중 트랙 가격 공개.**
   Google이 Gemini 2.5 Flash TTS·Pro TTS 모델의 표현력·페이싱·멀티스피커 일관성 업그레이드를 발표했다. Flash TTS는 실시간 어시스턴트·고량 내레이션용, Pro TTS는 장문 콘텐츠·전문 내레이션·복잡한 크리에이티브 워크플로우용으로 포지셔닝을 이중화했다. 가격은 Pro TTS $1.00/1M input tokens + $20.00/1M output tokens, Flash TTS $0.50/$10.00(각 입/출력 per 1M tokens)이다. [[G-13]](#ref-g-13) [[G-14]](#ref-g-14)

7. **OpenAI 오디오 모델 업데이트 — Custom Voices 확대, WER 35% 감소 모델 안정화.**
   OpenAI가 gpt-4o-mini-tts-2025-12-15 기반으로 오디오 모델 스냅샷을 업데이트했다. Common Voice·FLEURS 기준 Word Error Rate (WER) 35% 이하, Multilingual LibriSpeech 전반적 개선을 확인했다. Custom Voices의 자연스러운 톤·샘플 충실도·방언 정확도가 향상됐으며, 프로덕션 앱에 대한 Custom Voices 접근이 확대됐다. [[G-15]](#ref-g-15)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Mistral AI | Voxtral TTS 4B 오픈웨이트 출시(3/26). 9언어, TTFA 90ms, $0.016/1k chars, ElevenLabs 대비 68.4% 승률. CC BY-NC 4.0 | [[G-01]](#ref-g-01), [[P-01]](#ref-p-01) |
| xAI | Grok TTS API(3/16) + Voice Agent API 런칭. $0.05/min, TTFA <1s, Big Bench Audio 1위, OpenAI Realtime API 호환, LiveKit 플러그인 제공 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| ElevenLabs | Eleven v3 GA(3/14). 70+ 언어, Audio Tags, 오류율 4.9%. IBM watsonx 파트너십(3/25). 11.ai 알파 MCP 음성 에이전트 공개 | [[G-07]](#ref-g-07), [[G-11]](#ref-g-11) |
| Google | Gemini 2.5 Flash/Pro TTS 표현력 업그레이드. Pro $20/1M output tokens, Flash $10/1M output tokens 가격 공시 | [[G-13]](#ref-g-13) |
| Amazon (AWS) | Polly Generative TTS 10개 음성 GA + Bidirectional Streaming API 출시(3월). 8개 로케일, 2개 신규 리전 | [[G-10]](#ref-g-10) |
| OpenAI | gpt-4o-mini-tts 스냅샷 업데이트. WER 35% 감소, Custom Voices 프로덕션 확대 | [[G-15]](#ref-g-15) |
| Microsoft | Azure Speech Dragon HD Omni 700+ 음성 프리뷰 상태 유지. 신규 발표 없음 (전주 시그널 지속) | [[G-16]](#ref-g-16) |
| IBM | watsonx Orchestrate에 ElevenLabs·Deepgram 동시 통합(3/25). 엔터프라이즈 음성 에이전트 플랫폼 전략 | [[G-07]](#ref-g-07), [[G-09]](#ref-g-09) |
| Deepgram | IBM watsonx 첫 전용 음성 파트너 선정(2/24 발표). Series C $130M/$1.3B 밸류에이션(1/13). Nova-3 의료 STT 출시 | [[G-09]](#ref-g-09), [[G-17]](#ref-g-17) |
| Hume AI | TADA(RTF 0.09, 환각 제로) 전주 오픈소스 공개 후 커뮤니티 채택 확산 중 | [[G-18]](#ref-g-18) |
| Kyutai | Pocket TTS(100M 파라미터, CPU 실행, sub-50ms) 오픈소스 공개(1월). 228개 기증 음성 통합 완료 | [[G-19]](#ref-g-19) |
| SKT | 에이닷 오토(르노코리아 필랑트 차량 탑재, 3/14), "1인 1 AI 에이전트" 전사 AX 전환 가속 발표 | [[G-20]](#ref-g-20) |

---

## 시장 시그널

**투자 & M&A**

- ElevenLabs Series D $500M 조달(2/4), 기업 가치 $11B 확정 [[G-17]](#ref-g-17)
- Deepgram Series C $130M 조달(1/13), 기업 가치 $1.3B. YC AI 스타트업 OfOne 동시 인수 [[G-17]](#ref-g-17)
- PolyAI Series D $86M(2025-12), NVIDIA VC·Citi Ventures·Zendesk Ventures 참여, 기업 가치 $750M [[G-21]](#ref-g-21)

**파트너십 & 제휴**

- ElevenLabs + IBM watsonx Orchestrate: 프리미엄 TTS/STT 엔터프라이즈 통합(3/25) [[G-07]](#ref-g-07)
- Deepgram + IBM watsonx Orchestrate: 첫 전용 음성 파트너(2/24 발표, 3월 확대) [[G-09]](#ref-g-09)
- xAI + LiveKit: Grok Voice Agent API 공식 플러그인 제공 [[G-05]](#ref-g-05)
- SKT + 르노코리아: 에이닷 오토 필랑트 차량 최초 탑재(3/14) [[G-20]](#ref-g-20)

**시장 전망**

- TTS 시장 규모: 2026년 $4.36B, 2031년 $7.92B(CAGR 12.66%) [[G-22]](#ref-g-22) [추가확인 필요]
- AI 보이스 제너레이터 시장: 2025년 $4.16B → 2031년 $20.71B(CAGR 30.7%) [[G-22]](#ref-g-22) [추가확인 필요]
- Voice AI 에이전트 시장: 2024년 $2.4B → 2034년 $47.5B(CAGR 34.8%) [[G-23]](#ref-g-23) [추가확인 필요]
- 음성 인식 시장: 2025년 $18.39B → 2031년 $61.71B(CAGR 22.38%) [[G-21]](#ref-g-21) [추가확인 필요]

> 시장 규모 수치는 복수 리서치 업체 추정치를 교차 인용한 것으로 정밀도에 차이가 있음.

**도입 사례**

- IBM watsonx Orchestrate: 고객 지원·영업·직원 워크플로우·정부 서비스에 ElevenLabs/Deepgram TTS 통합 [[G-07]](#ref-g-07)
- 르노코리아 필랑트: SKT 에이닷 오토 음성 에이전트 차량 내장 [[G-20]](#ref-g-20)
- 1,300개 이상 기업이 Deepgram API로 음성 AI 기능 구현 중 [[G-17]](#ref-g-17)

**연구 동향**

- Voxtral TTS 아키텍처(자동회귀 시맨틱 토큰 + 플로우 매칭 음향 토큰 하이브리드)가 고품질·저레이턴시 달성의 새 접근으로 주목됨 [[P-01]](#ref-p-01)
- Interspeech 2026 제출 논문군: CodecMOS-Accent(영어 억양별 MOS 벤치마크), 딥페이크 탐지, 음성 향상 등 품질 측정·보안 분야 활발 [[G-24]](#ref-g-24)
- 에지(edge) TTS 모델 경쟁: Kyutai Pocket TTS 100M(1월), Kitten TTS 15~80M(3월), Voxtral TTS 4B 온디바이스 가능 수준으로 경량화 트렌드 지속 [[G-19]](#ref-g-19), [[G-25]](#ref-g-25)

---

## 전략적 시사점

**기술 트렌드**

- 오픈웨이트 TTS의 품질이 상용 API 수준에 근접하며 진입 장벽 붕괴 중(Voxtral, TADA, Kyutai Pocket)
- 하이브리드 아키텍처(자동회귀 시맨틱 + 플로우 매칭 음향)가 품질과 레이턴시를 동시 달성하는 유력 구조로 수렴
- 음성 에이전트 API 표준이 OpenAI Realtime API 스펙으로 사실상 통합(xAI Grok, ElevenLabs 모두 호환)
- 엔터프라이즈 통합 경로: IBM watsonx Orchestrate 등 오케스트레이션 플랫폼이 TTS 도달 채널로 부상

**기회**

- 오픈웨이트 모델(Voxtral, TADA, Kyutai) 활용 시 TTS 비용을 상용 API 대비 80~90% 절감 가능
- 차량·헬스케어·오프라인 환경 등 프라이버시·레이턴시 민감 영역의 온디바이스 TTS 수요 급증
- IBM watsonx·LiveKit 등 플랫폼 통합 경로가 열리면서 대형 기업(금융·공공·통신) 도입 가속 가능
- 한국어 지원: Mistral Voxtral·Hume Octave 2·Google Gemini 2.5가 한국어 포함하여 국내 서비스 적용 가능성 확대

**위협**

- Mistral·xAI 진입으로 TTS API 가격 하락 압력 심화($0.016~$0.05 수준으로 저가 경쟁 격화)
- CC BY-NC 라이선스(Voxtral)의 상업적 제약으로 직접 활용 시 라이선스 위험 존재
- ElevenLabs·Deepgram이 IBM watsonx 같은 엔터프라이즈 플랫폼을 선점하면서 직접 계약 경로 축소 가능
- 딥페이크 음성 규제 리스크: 3초 음성 복제 기술 확산으로 인한 법·규제 환경 변화 주시 필요

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Mistral AI — Speaking of Voxtral | [링크](https://mistral.ai/news/voxtral-tts) | blog | 2026-03-26 | [A] |
| <a id="ref-g-02"></a>G-02 | TechCrunch — Mistral releases new open source model for speech generation | [링크](https://techcrunch.com/2026/03/26/mistral-releases-a-new-open-source-model-for-speech-generation/) | news | 2026-03-26 | [B] |
| <a id="ref-g-03"></a>G-03 | VentureBeat — Mistral AI just released a TTS model it says beats ElevenLabs | [링크](https://venturebeat.com/orchestration/mistral-ai-just-released-a-text-to-speech-model-it-says-beats-elevenlabs-and) | news | 2026-03-26 | [B] |
| <a id="ref-g-04"></a>G-04 | xAI — Grok Voice Agent API 공식 발표 | [링크](https://x.ai/news/grok-voice-agent-api) | blog | 2026-03-16 | [A] |
| <a id="ref-g-05"></a>G-05 | xAI Docs — Voice APIs | [링크](https://docs.x.ai/developers/model-capabilities/audio/voice) | blog | 2026-03-16 | [A] |
| <a id="ref-g-06"></a>G-06 | AIBase — xAI Launches Grok Voice Agent API at $0.05 Per Minute | [링크](https://news.aibase.com/news/23823) | news | 2026-03-16 | [B] |
| <a id="ref-g-07"></a>G-07 | IBM Newsroom — Enterprise AI Finds its Voice: ElevenLabs and IBM | [링크](https://newsroom.ibm.com/2026-03-25-enterprise-ai-finds-its-voice-elevenlabs-and-ibm-bring-premium-voice-capabilities-to-agentic-ai) | IR/발표 | 2026-03-25 | [A] |
| <a id="ref-g-08"></a>G-08 | ElevenLabs Blog — ElevenLabs partners with IBM | [링크](https://elevenlabs.io/blog/elevenlabs-partners-with-ibm-to-bring-premium-voice-to-watsonx-orchestrate) | blog | 2026-03-25 | [A] |
| <a id="ref-g-09"></a>G-09 | IBM Newsroom — Deepgram and IBM Introduce Advanced Voice Capabilities | [링크](https://newsroom.ibm.com/2026-02-24-deepgram-and-ibm-introduce-advanced-voice-capabilities-for-enterprise-ai) | IR/발표 | 2026-02-24 | [A] |
| <a id="ref-g-10"></a>G-10 | AWS — Amazon Polly expands Generative TTS engine with 10 new voices | [링크](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-polly-expands-TTS-new-voices-and-bidirectional-streaming/) | blog | 2026-03 | [A] |
| <a id="ref-g-11"></a>G-11 | ElevenLabs Blog — Eleven v3 is Now Generally Available | [링크](https://elevenlabs.io/blog/eleven-v3-is-now-generally-available) | blog | 2026-03-14 | [A] |
| <a id="ref-g-12"></a>G-12 | ElevenLabs Blog — Eleven v3: Most Expressive AI TTS Model Launched | [링크](https://elevenlabs.io/blog/eleven-v3) | blog | 2026-02-12 | [A] |
| <a id="ref-g-13"></a>G-13 | Google Blog — Gemini 2.5 Text-to-Speech model updates | [링크](https://blog.google/technology/developers/gemini-2-5-text-to-speech/) | blog | 2026-03 | [A] |
| <a id="ref-g-14"></a>G-14 | Google AI for Developers — Gemini 2.5 Pro TTS | [링크](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts) | blog | 2026-03 | [A] |
| <a id="ref-g-15"></a>G-15 | OpenAI Developers Blog — Updates for developers building with voice | [링크](https://developers.openai.com/blog/updates-audio-models) | blog | 2026-03 | [A] |
| <a id="ref-g-16"></a>G-16 | Microsoft Learn — What's new in Speech service | [링크](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/releasenotes) | blog | 2026-03 | [A] |
| <a id="ref-g-17"></a>G-17 | Deepgram — Raises $130M Series C at $1.3B Valuation | [링크](https://deepgram.com/learn/press-release-deepgram-raises-series-c) | IR/발표 | 2026-01-13 | [A] |
| <a id="ref-g-18"></a>G-18 | Hume AI Blog — Opensourcing TADA | [링크](https://www.hume.ai/blog/opensource-tada) | blog | 2026-03-10 | [A] |
| <a id="ref-g-19"></a>G-19 | Kyutai — Pocket TTS GitHub | [링크](https://github.com/kyutai-labs/pocket-tts) | blog | 2026-01 | [B] |
| <a id="ref-g-20"></a>G-20 | SKT 뉴스룸 — 에이닷 오토 르노코리아 필랑트 탑재 | [링크](https://news.sktelecom.com/219242) | IR/발표 | 2026-03-14 | [A] |
| <a id="ref-g-21"></a>G-21 | AssemblyAI — Voice AI in 2026: Inside the companies and investments | [링크](https://www.assemblyai.com/blog/voice-ai-in-2026-series-1) | news | 2026-03 | [B] |
| <a id="ref-g-22"></a>G-22 | Mordor Intelligence — Text to Speech Market Size, Trends Report 2031 | [링크](https://www.mordorintelligence.com/industry-reports/text-to-speech-market) | news | 2026 | [B] |
| <a id="ref-g-23"></a>G-23 | VoiceAIWrapper — Voice AI Market Analysis 2026 | [링크](https://voiceaiwrapper.com/insights/voice-ai-market-analysis-trends-growth-opportunities) | news | 2026 | [C] |
| <a id="ref-g-24"></a>G-24 | arXiv list — eess.AS Audio and Speech Processing (recent) | [링크](https://arxiv.org/list/eess.AS/recent) | paper | 2026-03 | [B] |
| <a id="ref-g-25"></a>G-25 | SiliconFlow — Best Voice Cloning Models For Edge Deployment In 2026 | [링크](https://www.siliconflow.com/articles/en/best-voice-cloning-models-for-edge-deployment) | news | 2026-03 | [C] |
| <a id="ref-g-26"></a>G-26 | MarkTechPost — Mistral AI Releases Voxtral TTS: 4B Open-Weight Streaming Speech Model | [링크](https://www.marktechpost.com/2026/03/28/mistral-ai-releases-voxtral-tts-a-4b-open-weight-streaming-speech-model-for-low-latency-multilingual-voice-generation/) | news | 2026-03-28 | [B] |
| <a id="ref-p-01"></a>P-01 | Mistral AI — Voxtral TTS (arXiv:2603.25551) | [링크](https://arxiv.org/abs/2603.25551) | paper | 2026-03-26 | [A] |
