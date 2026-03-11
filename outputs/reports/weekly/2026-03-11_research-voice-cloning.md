---
type: deep-research
topic: voice-cloning
date: 2026-03-11
parent: weekly-voice-ai
agent: research-deep
confidence: high
sources_used: [websearch]
note: intel-store MCP 미사용 (VSCode 확장 환경 제약) — WebSearch 전량 대체
---

# Deep Research: Voice Cloning (2026-03-11)

> **조사 기간**: 2026-03-04 ~ 2026-03-11
> **핵심 키워드**: voice cloning, zero-shot TTS, speaker adaptation, ElevenLabs, Qwen3-TTS

---

## 기술 동향

1. **Qwen3-TTS 오픈소스 공개 (Alibaba Cloud, 2026-01-22) — 3초 보이스 클로닝, Apache 2.0, 상용 최강자 ElevenLabs 능가 주장.** Alibaba Cloud Qwen 팀이 공개한 Qwen3-TTS는 0.6B~1.7B 파라미터 시리즈로, 사용자가 3초 분량의 참조 오디오만 제공하면 보이스 클로닝이 가능하다. 97ms 초저지연 이중 트랙 스트리밍 아키텍처를 채택해 실시간 애플리케이션에 적합하며, 중국어·영어·일본어·한국어·독일어 등 10개 언어를 지원한다. 블라인드 평가에서 MiniMax, ElevenLabs, SeedTTS를 음성 품질과 화자 유사도 지표에서 앞선다는 평가를 받고 있다. Apache 2.0 라이선스로 상업적 활용이 완전히 자유로우며, HuggingFace와 GitHub에서 무료 다운로드가 가능하다. [[G-01]](#ref-g-01) [[G-02]](#ref-g-02)

2. **Resemble AI Chatterbox 오픈소스 TTS — MIT 라이선스, 감정 과장 제어 탑재, HuggingFace 100만 다운로드 돌파.** Resemble AI가 공개한 Chatterbox는 몇 초의 참조 오디오만으로 보이스 클로닝이 가능하고, 오픈소스 TTS 최초로 감정 과장(emotion exaggeration) 제어 기능을 탑재했다. 아랍어·중국어·한국어 등 23개 언어를 지원하는 Chatterbox Multilingual도 출시됐으며, 내장 워터마킹으로 AI 생성 음성 식별을 돕는다. MIT 라이선스라 수정 및 재배포가 자유롭고, 출시 수 주 만에 HuggingFace 100만 다운로드·GitHub 11,000+ 스타를 기록했다. [[G-03]](#ref-g-03)

3. **ElevenLabs Conversational AI 2.0 출시 — 자연스러운 대화 흐름 + 멀티모달 + 엔터프라이즈 HIPAA 준수.** ElevenLabs가 Conversational AI 2.0을 발표하면서 최신 턴-테이킹(turn-taking) 모델을 도입, 망설임·필러 단어 등 대화 신호를 실시간 분석해 자연스러운 발화 타이밍을 구현했다. 자동 언어 감지, 멀티 캐릭터 모드, RAG 내장, 배치 콜, 텍스트+음성 동시 멀티모달 처리를 지원한다. HIPAA 준수 및 EU 데이터 레지던시 옵션을 갖춰 헬스케어·금융권 엔터프라이즈 수요를 정조준했다. [[G-04]](#ref-g-04)

4. **ElevenLabs 11.ai 알파 출시 (2026-03 초) — MCP 기반 음성 우선 AI 개인 비서.** ElevenLabs가 자체 Conversational AI 기술을 기반으로 한 음성 우선 AI 비서 11.ai를 알파로 공개했다. Model Context Protocol(MCP)을 활용해 Google Calendar·Slack·Linear·Salesforce·Notion 등 외부 도구와 실시간 연동하며, 5,000개 이상의 사전 제작 음성과 커스텀 보이스 클로닝을 지원한다. 현재 피드백 수집을 위해 무료 제공 중이다. [[G-05]](#ref-g-05)

5. **Microsoft Azure Personal Voice DragonV2.1Neural — 100개 언어 지원 제로샷 TTS, 2025년 7월 GA.** Azure AI Speech의 Personal Voice 기능이 제로샷 TTS 모델 DragonV2.1Neural로 업그레이드됐다. 수 초의 샘플 음성만으로 보이스 복제가 가능하며, 100개 이상 언어로 음성을 생성한다. 강화된 운율 안정성과 발음 정확성을 특징으로 하며, 2025년 7월 기준 GA 상태다. [[G-06]](#ref-g-06)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | Series D $500M 조달 ($11B 밸류에이션, Sequoia 리드). 2025년 ARR $330M+. Conversational AI 2.0, 11.ai 알파, Deutsche Telekom 파트너십 동시 진행. 런던·도쿄·서울 등 글로벌 GTM 확대. | [[G-07]](#ref-g-07) [[G-08]](#ref-g-08) |
| Deutsche Telekom | MWC 2026에서 ElevenLabs와 공동 개발한 "Magenta AI Call Assistant" 세계 최초 공개. 50개 언어 실시간 통역·통화 요약 기능. 앱 없이 "Hey Magenta" 호출로 통신망에 AI가 내장. 독일 국내 출시 예정. | [[G-09]](#ref-g-09) [[G-10]](#ref-g-10) |
| Alibaba Cloud (Qwen) | Qwen3-TTS 시리즈 오픈소스 공개 (2026-01-22). Apache 2.0, 0.6B~1.7B 파라미터, 3초 보이스 클로닝, 97ms 지연. ElevenLabs 대비 우위 주장. | [[G-01]](#ref-g-01) [[G-02]](#ref-g-02) |
| Resemble AI | Chatterbox 오픈소스 TTS 공개 (MIT 라이선스). 감정 제어, 23개 언어, 내장 워터마킹. HuggingFace 100만 다운로드 돌파. | [[G-03]](#ref-g-03) |
| Google | NotebookLM Audio Overviews 기능이 NPR 전 진행자 David Greene의 목소리를 무단 복제했다는 주장으로 소송 피소 (2026-02-15). Google은 "유료 전문 성우 고용"이라 반박. 법의학 분석 53~60% 신뢰도로 Greene 목소리 일치 의견. | [[G-11]](#ref-g-11) [[G-12]](#ref-g-12) |
| Amazon | Alexa+ 전체 미국 무료 공개 (2026-02). 음성 커스터마이징 8가지 옵션 제공. 할머니 목소리 클로닝 데모(2022) 이후 공개 보이스 클로닝 기능은 미출시 상태. | [[G-13]](#ref-g-13) |
| Microsoft | Azure Personal Voice DragonV2.1Neural (2025-07 GA). 100개 언어, 제로샷 TTS, 수 초 음성 샘플 클로닝. | [[G-06]](#ref-g-06) |
| MAGO (한국) | STT·화자 분리·의도·감정 분석 기반 음성 AI 미들웨어 플랫폼 Audion 운영. 보이스 클로닝보다 실시간 음성 감정 인식·대화 AI에 집중. 기업용 API/SDK 형태 제공. | [[G-14]](#ref-g-14) |
| Naver | CLOVA TTS Premium을 통해 한국어 음성 합성 제공. HyperCLOVA X 멀티모달 확장 계획(이미지·오디오) 발표. 서울대와 음성 모델 코드·체크포인트 공개 협력 예정. 한국어 보이스 클로닝 제품화는 공개 정보 없음. | [[G-15]](#ref-g-15) |
| Play.ht | 2025-12-31 서비스 전체 종료. 일부 보도는 2026-02-09 YC Launch YC 재론칭을 언급하나 세부 내용 미확인. | [[G-16]](#ref-g-16) |

---

## 시장 시그널

- 글로벌 보이스 클로닝 시장 규모: 2024년 $2.7B → 2030년 $10.8B 전망, CAGR 26.2% [[G-17]](#ref-g-17)
- 단기 시장 추정치: 2025년 $3.28B → 2026년 $4.06B, 2030년 $9.56B (CAGR 23.9%) [[G-17]](#ref-g-17)
- 북미가 2024년 매출의 39% 점유. 아시아태평양 CAGR 28.1%로 가장 빠른 성장 전망 [[G-17]](#ref-g-17)
- ElevenLabs Series D $500M 조달 ($11B 밸류에이션) — 총 조달액 $781M, 2022년 창업 이후 최대 규모 [[G-07]](#ref-g-07)
- Deutsche Telekom–ElevenLabs 파트너십: 통신망 레벨 AI 음성 통합이라는 새로운 사업 모델 등장 [[G-09]](#ref-g-09)
- Play.ht 서비스 종료 — 스타트업 경쟁 압박으로 인한 시장 재편 진행 중 [[G-16]](#ref-g-16)
- Alibaba Qwen3-TTS, Resemble Chatterbox 오픈소스 공세 → 상용 API 단가 하방 압력 가속화
- Amazon Alexa+ 미국 전역 무료 출시 (2026-02) — 음성 AI 대중화 가속, 보이스 클로닝 선탑재 기대감 (미출시)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Voice Cloning: Comprehensive Survey (익명 et al., 2025) | 보이스 클로닝 전반(few-shot, zero-shot, 다국어, 화자 적응)을 체계적으로 정리한 서베이. 현재 기술 동향과 연구 방향 종합. | [[P-01]](#ref-p-01) |
| DiffGAN-ZSTTS: High Fidelity Zero-Shot Speaker Adaptation (익명 et al., 2025) | FastSpeech2 기반에 Diffusion decoder를 결합한 제로샷 화자 적응 모델. 미지 화자 일반화 능력 향상 입증. Scientific Reports 게재. | [[P-02]](#ref-p-02) |
| DS-TTS: Zero-Shot Speaker Style Adaptation via Dual-Style Feature Modulation (익명 et al., 2025) | Dual-Style Encoding Network(DuSEN)으로 미지 화자 스타일을 동적으로 모델링. 다양한 미지 화자 합성 성능 향상. | [[P-03]](#ref-p-03) |
| Zero-Shot Voice Cloning TTS for Dysphonia Disorder Speakers (익명 et al., 2024) | 음성 장애 화자 대상 제로샷 TTS 적용. 의료·접근성 분야 보이스 클로닝 확장 가능성 제시. IEEE Xplore 게재. | [[P-04]](#ref-p-04) |
| Google — Restoring Speaker Voices with Zero-Shot Cross-Lingual Voice Transfer (Google Research, 2025) | 교차 언어 제로샷 보이스 전이 기법으로 원래 화자의 목소리를 복원. 다국어 TTS에 적용. | [[P-05]](#ref-p-05) |

---

## 전략적 시사점

**기회**
- ElevenLabs $11B 밸류에이션과 Deutsche Telekom 파트너십은 통신사가 보이스 AI를 망 레벨에서 내재화하는 새로운 비즈니스 모델을 열었음. 국내 통신사(SKT/KT) 유사 파트너십 검토 여지 존재
- Qwen3-TTS(Apache 2.0)·Chatterbox(MIT) 오픈소스 공세로 자체 솔루션 구축 비용 장벽이 낮아짐. 국내 특화(한국어 고품질) 파인튜닝이 차별화 포인트가 될 수 있음
- 아시아태평양 CAGR 28.1% — 글로벌 평균 대비 가장 빠른 성장 시장. 한국어 특화 보이스 클로닝 제품의 시장 진입 타이밍으로 유리
- Resemble Chatterbox의 감정 제어·워터마킹 내장 — 안전하고 윤리적인 보이스 클로닝 솔루션 수요 대응 기술로 참조 가치

**위협**
- Google NotebookLM 소송 사례는 무동의 보이스 클로닝 법적 리스크를 전면화함. 학습 데이터 출처 투명성 확보 없이는 기업 서비스 운영 리스크 상존
- EU AI Act 2026-08 전면 적용(Article 50: 합성 음성 투명성 의무) 및 미국 NO FAKES Act 입법 추진 — 국제 규제 요건 충족 비용 증가
- Play.ht 서비스 종료 사례처럼, ElevenLabs·Qwen3-TTS 등 상위 플레이어의 오픈소스 전략이 중간 규모 사업자를 구축하는 경쟁 구도 심화
- 오픈소스 모델 확산으로 딥페이크 음성 사기·보이스피싱 위협 고도화. 탐지 기술(Resemble Detect 등)과의 병행 투자 필요

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Qwen.ai — Qwen3-TTS Family is Now Open Sourced | [링크](https://qwen.ai/blog?id=qwen3tts-0115) | blog | 2026-01-22 | [A] |
| <a id="ref-g-02"></a>G-02 | COEY — Qwen3-TTS Open Source: Streaming Voice Cloning in 3 Seconds | [링크](https://coey.com/resources/blog/2026/01/25/qwen3-tts-open-source-streaming-voice-cloning-in-3-seconds/) | blog | 2026-01-25 | [B] |
| <a id="ref-g-03"></a>G-03 | Resemble AI — Chatterbox SoTA Open-Source TTS (GitHub) | [링크](https://github.com/resemble-ai/chatterbox) | blog | 2026 | [A] |
| <a id="ref-g-04"></a>G-04 | ElevenLabs — Conversational AI 2.0 voice agents now live | [링크](https://elevenlabs.io/blog/conversational-ai-2-0) | blog | 2026 | [A] |
| <a id="ref-g-05"></a>G-05 | ElevenLabs — Introducing 11.ai Personal AI Voice Assistants | [링크](https://elevenlabs.io/blog/introducing-11ai) | blog | 2026-03 | [A] |
| <a id="ref-g-06"></a>G-06 | The Register — Azure AI Speech needs seconds of audio to clone voices | [링크](https://www.theregister.com/2025/07/31/microsoft_updates_azure_ai_speech/) | news | 2025-07-31 | [B] |
| <a id="ref-g-07"></a>G-07 | TechCrunch — ElevenLabs raises $500M from Sequoia at $11B valuation | [링크](https://techcrunch.com/2026/02/04/elevenlabs-raises-500m-from-sequioia-at-a-11-billion-valuation/) | news | 2026-02-04 | [B] |
| <a id="ref-g-08"></a>G-08 | ElevenLabs — Series D Official Blog | [링크](https://elevenlabs.io/blog/series-d) | blog | 2026-02 | [A] |
| <a id="ref-g-09"></a>G-09 | ElevenLabs — Deutsche Telekom AI Call Assistant | [링크](https://elevenlabs.io/blog/deutsche-telekom-ai-call-assistant) | blog | 2026-03-02 | [A] |
| <a id="ref-g-10"></a>G-10 | Deutsche Telekom — MWC 2026: World premiere of AI-powered call assistant | [링크](https://www.telekom.com/en/media/media-information/archive/mwc-2026-world-premiere-of-ai-powered-call-assistant-1102906) | press | 2026-03-02 | [A] |
| <a id="ref-g-11"></a>G-11 | TechCrunch — Longtime NPR host David Greene sues Google over NotebookLM voice | [링크](https://techcrunch.com/2026/02/15/longtime-npr-host-david-greene-sues-google-over-notebooklm-voice/) | news | 2026-02-15 | [B] |
| <a id="ref-g-12"></a>G-12 | NPR — Former Morning Edition host accuses Google of stealing his voice | [링크](https://www.npr.org/2026/02/17/nx-s1-5716055/former-morning-edition-host-accuses-google-of-stealing-his-voice-for-ai-product) | news | 2026-02-17 | [B] |
| <a id="ref-g-13"></a>G-13 | TechCrunch — Alexa+, Amazon's AI assistant, is now available to everyone in the US | [링크](https://techcrunch.com/2026/02/04/alexa-amazons-ai-assistant-is-now-available-to-everyone-in-the-u-s/) | news | 2026-02-04 | [B] |
| <a id="ref-g-14"></a>G-14 | MAGO — Next Generation Voice Recognition AI (공식 사이트) | [링크](https://www.holamago.com/en/) | web | 2026 | [A] |
| <a id="ref-g-15"></a>G-15 | Naver CLOVA — TTS Premium API Docs | [링크](https://api.ncloud-docs.com/docs/en/ai-naver-clovavoice-ttspremium) | web | 2026 | [A] |
| <a id="ref-g-16"></a>G-16 | Gaga.art — PlayHT Review: AI Voice Generation Platform 2026 | [링크](https://gaga.art/blog/playht/) | blog | 2026 | [C] |
| <a id="ref-g-17"></a>G-17 | Grand View Research — AI Voice Cloning Market Size & Outlook 2030 | [링크](https://www.grandviewresearch.com/industry-analysis/ai-voice-cloning-market-report) | report | 2026 | [B] |
| <a id="ref-g-18"></a>G-18 | Holonlaw — Synthetic Media & Voice Cloning Right of Publicity Risks 2026 | [링크](https://holonlaw.com/entertainment-law/synthetic-media-voice-cloning-and-the-new-right-of-publicity-risk-map-for-2026/) | web | 2026 | [B] |
| <a id="ref-g-19"></a>G-19 | AI Tribune — AI Voice Cloning Regulation in 2026 | [링크](https://aitribune.net/2026/02/24/ai-voice-cloning-regulation-in-2026/) | blog | 2026-02-24 | [C] |
| <a id="ref-g-20"></a>G-20 | The Decoder — ElevenLabs launches 11ai, a voice assistant that uses MCP | [링크](https://the-decoder.com/elevenlabs-launches-11ai-a-voice-assistant-that-uses-mcp-to-integrate-with-digital-workflow-tools/) | news | 2026-03 | [B] |
| <a id="ref-p-01"></a>P-01 | 익명 et al. — Voice Cloning: Comprehensive Survey | [링크](https://arxiv.org/html/2505.00579v1) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | 익명 et al. — High fidelity zero shot speaker adaptation in TTS with denoising diffusion GAN | [링크](https://www.nature.com/articles/s41598-025-90507-0) | paper | 2025 | [A] |
| <a id="ref-p-03"></a>P-03 | 익명 et al. — DS-TTS: Zero-Shot Speaker Style Adaptation via Dynamic Dual-Style Feature Modulation | [링크](https://arxiv.org/html/2506.01020v1) | paper | 2025 | [A] |
| <a id="ref-p-04"></a>P-04 | 익명 et al. — Zero-Shot Voice Cloning TTS for Dysphonia Disorder Speakers | [링크](https://ieeexplore.ieee.org/document/10517609/) | paper | 2024 | [A] |
| <a id="ref-p-05"></a>P-05 | Google Research — Restoring Speaker Voices with Zero-Shot Cross-Lingual Voice Transfer for TTS | [링크](https://research.google/blog/restoring-speaker-voices-with-zero-shot-cross-lingual-voice-transfer-for-tts/) | paper | 2025 | [A] |
