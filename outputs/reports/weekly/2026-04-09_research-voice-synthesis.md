---
topic: voice-synthesis
week: 2026-W15-W16
date: 2026-04-09
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
---

# Deep 리서치: Voice Synthesis (W16, 2026-04-02 ~ 2026-04-09)

## 이전 대비 변화

- **전주 (W15, 2026-04-06)**: 플랫폼 확장 + 오픈소스 가속 — ElevenLabs 에이전트 플랫폼 대규모 업데이트(Model Context Protocol, MCP Tool Scoping·Video-to-Music), Cartesia Sonic-3 Amazon Web Services (AWS) SageMaker 배포, Miravoice $6.3M Seed, Nari Labs Dia2 커뮤니티 확산, OmniVoice 600+ 언어 논문 발표.
- **금주 (W16, 2026-04-09)**: 음악·모빌리티·오픈소스 3중 확장 — ElevenLabs가 iOS 음악 생성 앱 ElevenMusic을 출시하며 음악 시장 직접 공략. OpenAI는 ChatGPT Advanced Voice Mode를 CarPlay에 통합하며 모빌리티 채널로 확장. 오픈소스 진영에서 Sopro Text-to-Speech (TTS) 169M(CPU 실시간, $100 학습비)과 Fish Audio S2(Dual-Autoregressive, Reinforcement Learning 정렬, 80+ 언어)가 커뮤니티 주목을 받았다. Hume AI Octave 2(감정 지능 TTS, 11언어, 40% 성능 향상)와 Google Gemini 2.5 TTS(24언어, 감정 표현 강화)도 이 기간 주요 시그널로 확인됐다.
- **변화 방향**: TTS 품질 경쟁이 사실상 완료 단계에 진입했다. MOS 기준으로 오픈소스 최고 모델(4.6~4.7)과 상용 최고 모델(4.8) 간 격차가 0.1~0.2 수준으로 수렴했다 [[G-14]](#ref-g-14). 이에 따라 차별화 축이 (1) **플랫폼 생태계**(ElevenLabs의 음악·에이전트 확장), (2) **멀티모달·모빌리티 통합**(OpenAI CarPlay, Google Gemini 멀티스피커), (3) **초경량·온디바이스**(Sopro, Kokoro) 세 방향으로 분기하고 있다.

---

## 기술 동향

### 1. ElevenLabs ElevenMusic — iOS 음악 생성 앱 출시 (4/1)

ElevenLabs가 2026년 4월 1일 iOS 앱 ElevenMusic을 출시하며 Voice AI에서 Music AI로 영역을 확장했다 [[G-01]](#ref-g-01). 자연어 프롬프트로 음악을 생성·리믹스하며, 기존 스트리밍 앱과 유사한 발견(Discovery) 레이어(무드별 큐레이션 스테이션, 차트, 신곡)를 탑재했다. 가격 구조: 무료 티어 7곡/일, 프로 구독 $9.99/월 또는 $95.90/년(월 500트랙, 500GB+ 스토리지). 경쟁사인 Suno·Udio가 저작권 소송 이후 레이블과 사후 합의한 것과 달리, ElevenLabs는 출시 전 Merlin(독립 레이블 디지털 라이선싱 조직)과 Kobalt Music 출판사와 사전 라이선스 계약을 체결했다 [[G-02]](#ref-g-02). CEO Mati Staniszewski는 "AI 오디오 회사로서 음악 확장은 자연스러운 진화"라고 밝혔다 [[E-01]](#ref-e-01). 플랫폼 출시 이후 누적 1,400만 곡 생성, 음성 크리에이터에게 $1,100만 이상 지급 이력도 공개했다 [[G-02]](#ref-g-02).

**기술적 의미**: 단일 TTS 기업에서 종합 Audio AI 플랫폼으로 포지션 전환을 명시적으로 선언. 배경음악 생성·음악 크리에이터 생태계 구축을 통해 기업가치 재평가(현재 $11B) 근거를 다각화하는 전략이다.

### 2. Google Gemini 2.5 TTS 업데이트 — 24언어, 감정 표현 강화

Google이 Gemini 2.5 Flash/Pro TTS 프리뷰 모델을 업데이트했다. 세 가지 개선축: (1) **향상된 표현력** — 스타일 프롬프트("쾌활하고 낙관적인" → "엄숙하고 진지한" 등) 지시 준수율 대폭 향상; (2) **컨텍스트 기반 속도 제어** — 흥분 시 가속, 강조 시 감속, 다중 화자 대화에서 캐릭터별 일관된 음성 유지; (3) **24개 언어 지원** — 다국어 환경에서도 각 언어의 억양·음높이·스타일 보존 [[G-03]](#ref-g-03). Gemini 2.5 Flash TTS(저지연 최적화)와 Pro TTS(품질 최적화)는 Google AI Studio와 Gemini API를 통해 접근 가능하다.

**기술적 의미**: Google이 기존 Cloud Text-to-Speech (TTS)와 별개로 LLM 네이티브 TTS 경로를 구축하고 있으며, 다중 화자·다국어 시나리오에서 강점을 확보 중.

### 3. OpenAI ChatGPT CarPlay 통합 — 모빌리티 채널 확장 (3/31)

OpenAI가 2026년 3월 31일 ChatGPT Advanced Voice Mode의 Apple CarPlay 통합을 발표했다 [[G-04]](#ref-g-04). iOS 26.4 이상이 탑재된 iPhone과 CarPlay 지원 차량에서 사용 가능. Apple CarPlay 제약상 Wake Word 미지원(수동 실행 필요), 차량 기능 제어 불가(Siri 별도 사용 필요), 내비게이션·실시간 위치 데이터 미접근. ChatGPT의 음성은 이미 subtler intonation(미묘한 억양), realistic cadence(자연스러운 속도), 공감·풍자 등 감정 표현력이 강화된 상태다 [[G-05]](#ref-g-05).

**기술적 의미**: AI 음성 에이전트가 스마트폰에서 자동차 인포테인먼트 시스템으로 배포 채널을 확장. Siri의 주요 사용 사례(운전 중 질의·정보 검색) 직접 대체를 노린 포지셔닝.

### 4. Sopro TTS 169M — CPU 실시간, $100 학습비, HN 트렌딩

오픈소스 경량 TTS 모델 Sopro(개발자: samuel-vitorino)가 Hacker News (HN)에서 높은 관심을 끌었다 [[C-01]](#ref-c-01). 169M 파라미터(Mimi 코덱 제외), WaveNet 스타일 팽창 컨볼루션(Dilated Convolution) + 경량 크로스-어텐션 아키텍처로 Transformer를 미채용. 핵심 스펙: CPU Real-Time Factor (RTF) 0.05(M3 기준, 32초 오디오를 1.77초에 생성), 스트리밍 Time-To-First-Audio (TTFA) 250ms, 제로샷 음성 복제(3~12초 참조 오디오). 학습 비용 약 $100(L40S GPU), Apache 2.0 라이선스 [[G-06]](#ref-g-06). v1.5(2026-02-04)에서 135M으로 경량화·안정화됨. HN 커뮤니티에서는 품질에 대한 엇갈린 평가("완전히 사용 불가" vs. "CPU 성능 인상적")와 함께 Kokoro 82M, Chatterbox-TTS와 비교 논의가 활발했다 [[C-01]](#ref-c-01).

**기술적 의미**: 온디바이스·엣지 TTS의 진입 장벽이 $100 수준까지 하락. 인프라 접근이 어려운 개발자·연구자에게 실용적인 제로샷 클로닝 경로 제공.

### 5. Fish Audio S2 오픈소스 — Dual-AR + RL, 80언어, 81.88% EmergentTTS 승률

Fish Audio가 2026년 3월 9일 S2를 오픈소스로 공개했다(GitHub/HuggingFace) [[G-07]](#ref-g-07). 기술 아키텍처: **Dual-Autoregressive (Dual-AR)** — Slow AR(4B 파라미터, 시간축 의미 코드북 예측)과 Fast AR(400M 파라미터, 잔여 코드북 생성)의 비대칭 처리. **Reinforcement Learning (RL) 정렬** — Group Relative Policy Optimization (GRPO) 기반 학습 후 정렬로, 데이터 필터링·어노테이션에 사용한 동일 모델을 보상 모델로 재활용해 분포 불일치 제거. 학습 데이터 1,000만 시간+, 80개 언어 지원, 자연어 인라인 태그([whisper in small voice], [professional broadcast tone])로 단어 단위 감정 제어. 성능: Seed-TTS Eval WER(Word Error Rate) 0.54%(중국어)/0.99%(영어), EmergentTTS-Eval 81.88% 승률, RTF 0.195(H200 단일 GPU), Time-To-First-Audio (TTFA) 100ms 미만 [[G-07]](#ref-g-07).

**기술적 의미**: 오픈소스 모델이 처음으로 폐쇄형 시스템(Seed-TTS) 대비 WER·자연도 양면에서 우위를 기록. RL 정렬 기법이 TTS 품질 상한을 견인하는 핵심 기술 요소로 부상.

### 6. Hume AI Octave 2 — 감정 지능 TTS, 11언어, 40% 성능 향상

Hume AI가 2025년 10월 출시한 Octave 2는 LLM 기반 TTS의 새로운 기준을 제시했다 [[G-08]](#ref-g-08). 핵심 차별화: Octave는 텍스트를 "읽는" 것이 아닌 "이해"하는 모델로 설계됐다. 맥락에서 감정을 추론해 풍자적 발언은 풍자적으로, 긴박한 문장은 급박하게 발화. 기술 스펙: 11개 언어(아랍어, 영어, 프랑스어, 독일어, 힌디어, 이탈리아어, 일본어, 한국어, 포르투갈어, 러시아어, 스페인어), Time-To-First-Byte (TTFB) 200ms 미만(전작 대비 40% 향상), 15초 참조 오디오로 음성 복제, Sambanova 전용 칩 배포로 가격 Octave 1의 절반 수준, 전용 배포 시 분당 1센트 미만 가능 [[G-08]](#ref-g-08). 음성 변환(Voice Conversion), 포넘 직접 편집(Phoneme Editing) 기능 추가 예정.

**기술적 의미**: 감정 추론 기반 TTS가 상용화 단계 진입. 연기 지시(Acting Instructions)를 자연어로 받아들이는 모델이 AI 더빙·오디오북·대화형 캐릭터 시장의 새로운 표준이 될 가능성.

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | 4/1 iOS 앱 ElevenMusic 출시(무료 7곡/일, Pro $9.99/월). Merlin·Kobalt 사전 라이선스 체결로 Suno·Udio와 차별화. 누적 1,400만 곡, 크리에이터 $1,100만 지급. 2026-02 Series D $500M(Sequoia 주도, $11B 밸류에이션), ARR $330M+ | [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[E-01]](#ref-e-01), [[G-09]](#ref-g-09) |
| OpenAI | 3/31 ChatGPT Advanced Voice Mode → Apple CarPlay 통합(iOS 26.4+). 억양·속도·공감·풍자 감정 표현 강화 업데이트. CarPlay에서 차량 제어·Wake Word 미지원(Apple 제약) | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| Google | Gemini 2.5 Flash/Pro TTS 업데이트: 24언어, 감정 표현 강화, 컨텍스트 기반 속도 제어, 다중 화자 일관성 개선. Gemini API/AI Studio 제공 | [[G-03]](#ref-g-03) |
| Hume AI | Octave 2(2025-10 출시): LLM 기반 감정 추론 TTS, 11언어, TTFB 200ms 미만, 전작 대비 40% 성능 향상, 가격 절반. 20개 언어로 확장 예정. Sambanova 파트너십 | [[G-08]](#ref-g-08) |
| Fish Audio | S2 Pro 오픈소스(2026-03-09): Dual-AR + GRPO RL, 80언어, 1,000만 시간 학습, EmergentTTS-Eval 81.88% 승률, 오픈소스 최초 Seed-TTS 초과 WER 달성 | [[G-07]](#ref-g-07), [[P-01]](#ref-p-01) |
| Sopro (samuel-vitorino) | 169M 파라미터, CPU RTF 0.05, TTFA 250ms, 제로샷 클로닝, $100 학습비, Apache 2.0. HN 트렌딩. 품질 논란 있으나 초경량 카테고리 주목 | [[G-06]](#ref-g-06), [[C-01]](#ref-c-01) |
| Cartesia | Sonic-3(SSM 아키텍처) AWS SageMaker JumpStart 통합 유지. 42언어, 모델 딜레이 90ms. ServiceNow·Cresta·Decagon 엔터프라이즈 고객. $100M 펀딩(Kleiner Perkins·NVIDIA 참여) | [[G-10]](#ref-g-10) |
| Nari Labs | Dia2 오픈소스 스트리밍 TTS 커뮤니티 확산 지속(전주 대비 신규 발표 없음). 1B/2B 체크포인트, Apache 2.0 | [[G-11]](#ref-g-11) |
| Alibaba (Qwen) | Qwen3-TTS 오픈소스(2026-01, Apache 2.0): 10개 언어, 500만 시간 학습, 97ms 스트리밍 레이턴시, WER 1.835%(10개 언어 평균). ElevenLabs·MiniMax 대비 우위 주장 | [[G-12]](#ref-g-12) |
| Sesame AI | Conversational Speech Model (CSM) 기반 초사실적 대화 음성 유지. 이미지 인터랙션 추가. 20개 언어 확장 예정 발표. 최근 Fala AI로 리브랜딩 | [[G-13]](#ref-g-13) |
| Mistral AI | Voxtral TTS 4B(W14, arXiv 2026-04-06 갱신): ElevenLabs Flash v2.5 대비 68.4% 승률, CC BY-NC 라이선스. 신규 발표 없음 | [[P-02]](#ref-p-02) |

---

## 시장 시그널

**투자 & M&A**

- **ElevenLabs Series D $500M**: 2026년 2월 Sequoia 주도, $11B 밸류에이션(전년 대비 3배+). Andreessen Horowitz 지분 4배 확대, ICONIQ Capital 3배 증액. 2025년 ARR $330M+ 달성, IPO 준비 선언 [[G-09]](#ref-g-09).
- **PolyAI Series D $86M**: 2025년 12월 Georgian·Hedosophia·Khosla Ventures 공동 주도, NVentures(NVIDIA VC)·Citi Ventures·Zendesk Ventures 참여. 누적 $200M+, 기업가치 $750M [[G-15]](#ref-g-15).
- **Voice AI 섹터 2025년 $2.1B 유치**: 주요 TTS/음성 에이전트 스타트업 대상 총 VC 유입. 시장 성장 기대감이 지속적인 투자 모멘텀 제공 [[G-15]](#ref-g-15).

**파트너십 & 제휴**

- **ElevenLabs + Merlin/Kobalt**: ElevenMusic 출시 전 독립 레이블(Merlin)·Kobalt Music 출판사와 사전 라이선스 체결. 법적 분쟁 없이 음악 AI 시장 진입하는 새로운 모델 제시 [[G-02]](#ref-g-02).
- **OpenAI + Apple CarPlay**: iOS 26.4 CarPlay 특별 엔타이틀먼트 통해 ChatGPT Voice 모빌리티 채널 확보. Apple이 제3자 대화 AI 앱을 CarPlay에 허용한 첫 사례 [[G-04]](#ref-g-04).
- **Hume AI + Sambanova**: Octave 2를 Sambanova 전용 추론 칩에 배포, 가격 50% 절감 및 분당 1센트 미만 달성 [[G-08]](#ref-g-08).

**시장 전망**

- **Voice AI 시장 규모**: AI 음성 및 언어 인텔리전스 시장 2026년 $24.49B → 2035년 $145.03B 전망. AI Voice Agents 세그먼트 2024년 $2.4B → 2034년 $47.5B(연평균성장률 Compound Annual Growth Rate, CAGR 34.8%) [[G-16]](#ref-g-16). [추가확인 필요: 단일 시장조사 출처]
- **음성·음성인식 시장 전체**: 2024년 $15.46B → 2032년 $81.59B(CAGR 23.1%) [[G-15]](#ref-g-15).
- **TTS 품질 격차 수렴**: 오픈소스 최고 모델(Sesame CSM 4.7 MOS, Orpheus 4.6 MOS)과 상용 최고 모델(ElevenLabs Turbo v2.5 4.8 MOS) 간 격차 0.1~0.2로 축소. 2023년 ~1.0 대비 급격한 수렴 [[G-14]](#ref-g-14).

**연구 동향**

- **Dual-AR + RL 정렬**: Fish Audio S2가 Dual-AR + GRPO RL 조합으로 오픈소스 TTS 품질 상한을 끌어올린 것이 주목. 동일 모델을 데이터 필터링·보상 모델로 동시 활용하는 방식이 학계에서 관심을 끌고 있다.
- **확산-언어 모델 융합**: OmniVoice(600+ 언어, 전주 발표)의 Diffusion Language Model 기반 비자기회귀(Non-Autoregressive) 아키텍처가 대규모 다국어 TTS의 새로운 방향으로 주목.
- **LLM 네이티브 TTS**: Hume AI Octave·Google Gemini TTS가 TTS를 독립 모듈이 아닌 LLM 추론 파이프라인에 통합하는 트렌드를 이끌고 있다.

**커뮤니티 시그널**

- Sopro TTS HN 트렌딩(#1): "CPU에서 실시간 동작하는 제로샷 클로닝 모델"이라는 주제가 AI/오픈소스 커뮤니티의 높은 관심을 받음. 품질보다 접근성·비용이 부각되는 새로운 사용자 세그먼트 존재 확인 [[C-01]](#ref-c-01).
- ElevenLabs Music Marketplace: 음성 크리에이터 에코시스템($1,100만 지급)에서 음악 크리에이터로 확장. 커뮤니티 반응은 "Suno·Udio 대비 라이선싱 포지션이 차별화 요소"로 평가 [[G-02]](#ref-g-02).
- Fish Audio S2 ComfyUI 통합 노드 등장: 오픈소스 커뮤니티에서 S2를 이미지 생성 워크플로우와 결합하는 실험 활발 [[G-07]](#ref-g-07).

---

## 학술 동향

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Fish Audio S2 Technical Report (Liao et al., 2026) | Dual-AR + GRPO RL, 80언어, EmergentTTS-Eval 81.88% 승률. 오픈소스 최초 Seed-TTS 초과 WER 달성 | [[P-01]](#ref-p-01) |
| Voxtral TTS (Mistral AI, 2026) | 4B 파라미터, 하이브리드 자기회귀+플로우매칭, ElevenLabs 대비 68.4% 승률. CC BY-NC 오픈웨이트 | [[P-02]](#ref-p-02) |
| OmniVoice: Towards Omnilingual Zero-Shot TTS (Zhu et al., 2026) | 600+ 언어, Diffusion Language Model 비자기회귀 아키텍처, 오픈소스 58.1만 시간 학습 | [[P-03]](#ref-p-03) |

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | TechCrunch — ElevenLabs releases a new AI-powered music-generation app | [링크](https://techcrunch.com/2026/04/02/elevenlabs-releases-a-new-ai-powered-music-generation-app/) | news | 2026-04-02 | [B] |
| <a id="ref-g-02"></a>G-02 | Music Business Worldwide — ElevenLabs launches ElevenMusic iOS app, taking on Suno and Udio on mobile | [링크](https://www.musicbusinessworldwide.com/elevenlabs-launches-elevenmusic-ios-app-taking-on-suno-and-udio-on-mobile/) | news | 2026-04-01 | [B] |
| <a id="ref-g-03"></a>G-03 | Toolnavs — Google upgrades Gemini 2.5 Flash and Pro TTS to improve emotional expression | [링크](https://toolnavs.com/en/article/940-google-upgrades-gemini-25-flash-and-pro-tts-to-improve-emotional-expression-and) | news | 2026-04 | [B] |
| <a id="ref-g-04"></a>G-04 | MacRumors — OpenAI Brings ChatGPT to CarPlay for Hands-Free Voice Conversations | [링크](https://www.macrumors.com/2026/03/31/openai-chatgpt-carplay/) | news | 2026-03-31 | [B] |
| <a id="ref-g-05"></a>G-05 | TechCrunch — OpenAI updates ChatGPT's voice mode with more natural-sounding speech | [링크](https://techcrunch.com/2025/06/09/openai-updates-chatgpts-voice-mode-with-more-natural-sounding-speech/) | news | 2025-06-09 | [B] |
| <a id="ref-g-06"></a>G-06 | GitHub — samuel-vitorino/sopro | [링크](https://github.com/samuel-vitorino/sopro) | blog | 2026-02-04 | [B] |
| <a id="ref-g-07"></a>G-07 | Fish Audio Blog — Fish Audio Open-Sources S2: Fine-Grained Control Meets Production Streaming | [링크](https://fish.audio/blog/fish-audio-open-sources-s2/) | blog | 2026-03-09 | [B] |
| <a id="ref-g-08"></a>G-08 | Hume AI Blog — Octave 2: next-generation multilingual voice AI | [링크](https://www.hume.ai/blog/octave-2-launch) | blog | 2025-10-01 | [A] |
| <a id="ref-g-09"></a>G-09 | TechCrunch — ElevenLabs raises $500M from Sequoia at an $11 billion valuation | [링크](https://techcrunch.com/2026/02/04/elevenlabs-raises-500m-from-sequioia-at-a-11-billion-valuation/) | news | 2026-02-04 | [B] |
| <a id="ref-g-10"></a>G-10 | Fish Audio — S2 Product Page | [링크](https://fish.audio/s2/) | blog | 2026-03 | [B] |
| <a id="ref-g-11"></a>G-11 | GitHub — Nari Labs / dia (Dia2) | [링크](https://github.com/nari-labs/dia) | blog | 2026-04 | [B] |
| <a id="ref-g-12"></a>G-12 | Alibaba Cloud Community — Qwen3-TTS Family is Now Open Sourced | [링크](https://www.alibabacloud.com/blog/602826) | blog | 2026-01 | [B] |
| <a id="ref-g-13"></a>G-13 | TechCrunch — Sesame, the startup behind the viral virtual assistant Maya, releases its base AI model | [링크](https://techcrunch.com/2025/03/13/sesame-the-startup-behind-the-viral-virtual-assistant-maya-releases-its-base-ai-model/) | news | 2025-03-13 | [B] |
| <a id="ref-g-14"></a>G-14 | CodeSOTA — Speech AI Benchmarks 2026: STT & TTS Leaderboard | [링크](https://www.codesota.com/speech) | blog | 2026-04 | [C] |
| <a id="ref-g-15"></a>G-15 | AssemblyAI Blog — Voice AI in 2026: Inside the companies and investments shaping the future of speech | [링크](https://www.assemblyai.com/blog/voice-ai-in-2026-series-1) | news | 2026 | [B] |
| <a id="ref-g-16"></a>G-16 | VoiceAIWrapper — Voice AI Market Analysis 2026 | [링크](https://voiceaiwrapper.com/insights/voice-ai-market-analysis-trends-growth-opportunities) | blog | 2026 | [C] |
| <a id="ref-e-01"></a>E-01 | ElevenLabs CEO Mati Staniszewski — "As an AI audio company, expanding into music was a natural progression" (Music Business Worldwide 인용) | [링크](https://www.musicbusinessworldwide.com/elevenlabs-launches-elevenmusic-ios-app-taking-on-suno-and-udio-on-mobile/) | IR/발표 | 2026-04-01 | [B] |
| <a id="ref-p-01"></a>P-01 | Liao et al. — Fish Audio S2 Technical Report | [링크](https://arxiv.org/abs/2603.08823) | paper | 2026-03-09 | [A] |
| <a id="ref-p-02"></a>P-02 | Mistral AI — Voxtral TTS | [링크](https://arxiv.org/abs/2603.25551) | paper | 2026-04-06 | [A] |
| <a id="ref-p-03"></a>P-03 | Zhu et al. — OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models | [링크](https://arxiv.org/abs/2604.00688) | paper | 2026-04-01 | [A] |
| <a id="ref-c-01"></a>C-01 | Hacker News — Sopro TTS: A 169M model with zero-shot voice cloning that runs on the CPU | [링크](https://news.ycombinator.com/item?id=46546113) | community | 2026-04 | [B] |
