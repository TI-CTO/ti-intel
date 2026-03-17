---
type: weekly-research
topic: voice-cloning
domain: voice-ai
date: 2026-03-17
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
note: intel-store MCP 미사용 (VSCode 확장 환경 제약) — WebSearch 전량 대체
---

# Voice Cloning — Deep 리서치 (W12)

> **조사 기간**: 2026-03-10 ~ 2026-03-17
> **추적 키워드**: voice cloning, zero-shot TTS, ElevenLabs, OpenAI, Google, Anthropic, deepfake regulation

---

## 이전 대비 변화

- **전주 (W11, 2026-03-11)**: ElevenLabs $500M Series D ($11B 밸류에이션), Deutsche Telekom 망 AI 통합(Magenta AI Call Assistant, 50언어), Qwen3-TTS·Chatterbox 오픈소스로 상용 API 단가 하방 압력, Google NotebookLM 보이스 소송, 11.ai MCP 개인 비서 알파, Play.ht 종료
- **금주 (W12, 2026-03-17)**: ElevenLabs가 SXSW 2026 무대에서 "1 Million Voices" 이니셔티브($1B 현물 투자) + "11 Voices" 다큐시리즈 프리미어로 소셜 임팩트 전략을 전면화. Iconic Voice Marketplace(28개 유명인 음성 라이선스)로 B2B 수익화 신규 축 확보. ElevenCreative 멀티모달 플랫폼 공식 런칭. Anthropic Claude Code가 ElevenLabs TTS를 음성 모드 공식 채택. YouTube, 정치인·언론인 대상 딥페이크 탐지 도구 확대. Hume AI 핵심 팀 Google DeepMind로 흡수.
- **변화 방향**: ElevenLabs가 기술 주도권을 넘어 접근성·브랜딩·엔터테인먼트 3방향으로 시장 지배력 확장. OpenAI 커스텀 보이스 API는 여전히 제한적 배포. 규제 압박(YouTube 정책 확대, EU AI Act 2026-08 시행 임박)이 탐지·투명성 기술 투자를 가속화. Hume AI 구인으로 Google DeepMind의 감성 음성 AI 역량이 급격히 강화됨.

---

## 기술 동향

1. **ElevenLabs "1 Million Voices" 이니셔티브 — 보이스 복원 소수 샘플 클로닝, $1B 현물 투자.** SXSW 2026(2026-03-11)에서 ElevenLabs는 ALS·뇌졸중·뇌손상 등 영구 음성 손실을 가진 100만 명에게 보이스 복원을 무상 제공하는 이니셔티브를 발표했다. 보이스메일·홈비디오 등 소량의 과거 녹음을 활용해 화자의 음성을 재건하고, 실시간 TTS 인터페이스에 탑재해 일상 소통에 사용하는 방식이다. 배우 Eric Dane(ALS 투병 중 사용)의 유산을 기리며 Rebecca Gayheart Dane이 캠페인 대사로 참여했다. 현재까지 7,000명 지원, 800개+ 비영리·통신 파트너 네트워크를 구축했다. [[G-01]](#ref-g-01) [[G-02]](#ref-g-02)

2. **ElevenLabs Iconic Voice Marketplace — 28개 유명인 음성 라이선스, 동의 기반 B2B 수익화 모델 정립.** ElevenLabs가 유명인·역사적 인물 AI 음성에 대한 법적 라이선스 마켓플레이스를 출시했다. Michael Caine, Liza Minnelli, Matthew McConaughey(투자자 겸 고객), Judy Garland, Maya Angelou, Mark Twain 등 28개 음성을 포함하며, CMG Worldwide와 파트너십으로 에스테이트 계약을 체계화했다. 동의(consent-only) 모델을 원칙으로 하며, 광고·나레이션·팟캐스트·게임·다국어 콘텐츠에 활용 가능. 70개 언어를 지원한다. [[G-03]](#ref-g-03) [[G-04]](#ref-g-04)

3. **ElevenCreative 플랫폼 공식 런칭 (2026-03-10) — 음성·음악·영상·이미지 통합 멀티모달 제작 환경.** ElevenLabs가 전문가·기업 대상 통합 멀티모달 콘텐츠 제작 플랫폼 ElevenCreative를 공식 출시했다. 보이스 클로닝, 70개 언어 팟캐스트 더빙, 음악 생성, 효과음, 이미지·영상 도구를 단일 플랫폼에 통합했다. 수백만 명의 크리에이터·마케터·미디어 기업을 대상으로 현지화·오디오 브랜딩·캠페인 제작을 효율화하는 포지셔닝이다. Conversational AI 플랫폼에는 텍스트·음성 동시 처리 멀티모달 기능도 추가됐다. [[G-05]](#ref-g-05) [[G-06]](#ref-g-06)

4. **Anthropic Claude Code — ElevenLabs TTS 공식 채택, 음성 모드 전체 구독자 확대 중.** Anthropic이 Claude Code AI 코딩 어시스턴트에 음성 모드를 탑재하며 ElevenLabs를 TTS 서브컨트랙터로 채택했다. 현재 약 5% 사용자에게 활성화됐으며 향후 전체 확대 예정이다. 5개 선택 가능한 음성, 스페이스바 홀드 방식 입력, `/voice` 토글 명령을 제공한다. Pro·Max·Team·Enterprise 구독자에게는 추가 비용 없이 제공되며, Claude Code의 2026년 초 기준 연환산 매출(run-rate)이 $2.5B를 돌파했다는 맥락에서 ElevenLabs TTS API의 규모 있는 채택이 확인된다. [[G-07]](#ref-g-07) [[G-08]](#ref-g-08)

5. **OpenAI gpt-4o-mini-tts 커스텀 보이스 — 프로덕션 확대 중이나 일반 공개는 여전히 제한적.** OpenAI의 gpt-4o-mini-tts는 "어떻게 말할지"까지 지시 가능한 steerable TTS 모델로, 13개 내장 보이스 외에 커스텀 보이스 기능을 기업 대상으로 제한 제공 중이다. 2024년 3월 Voice Engine 발표 이후 2년이 경과했으나 일반 배포는 안전성 검토를 이유로 지속 지연 중이다. 현재 선정된 파트너사 및 기업 고객(sales@openai.com 문의 경로)에게만 접근이 허용된다. [[G-09]](#ref-g-09) [[G-10]](#ref-g-10)

6. **Google Chirp 3 Instant Custom Voice — EU·미국 리전 확대, 일본어 포함 30개+ 로케일 지원.** Google Cloud TTS의 Chirp 3 Instant Custom Voice가 EU 및 미국 리전에서 음성 클로닝 키 생성을 지원하며, 일본어(ja-JP)를 포함해 30개 이상 로케일로 확대됐다. Google Meet의 AI 음성 번역 기능은 원화자의 톤·감정을 유지하는 "immersive voice"(보이스 클로닝 기반)를 영어→이탈리아어 등 유럽 언어에서 라이브 데모로 공개했다. 오디오 미보존(zero audio retention) 정책을 채택해 프라이버시 리스크를 완화했다. [[G-11]](#ref-g-11) [[G-12]](#ref-g-12)

7. **Hume AI 핵심 팀 Google DeepMind 합류 (2026-01-22) — 감성 음성 AI 역량 구글 내부화.** 감성 음성 AI 스타트업 Hume AI의 CEO Alan Cowen과 약 7명의 핵심 엔지니어가 Google DeepMind로 이동해 Gemini 음성 기능 개선에 투입됐다. Hume AI 본체는 기존 기술 라이선싱을 타 AI 기업에 계속 제공하나, 핵심 R&D 역량의 이탈로 독자 성장 전망이 불투명해졌다. Hume AI의 누적 조달액은 약 $80M이다. [[G-13]](#ref-g-13)

8. **IndexTTS2(Bilibili, 2025-09) — 감정·화자 정체성 분리 제어, 영상 더빙 특화 자동회귀 제로샷 TTS.** IndexTTS2는 Bilibili가 오픈소스로 공개한 자동회귀 제로샷 TTS로, 감정 표현과 화자 정체성을 분리 제어하는 disentanglement 구조를 채택했다. 영상 더빙에 필수적인 정밀 발화 지속 시간(duration) 제어를 지원하며, GPT 잠재 표현을 활용한 3단계 학습 패러다임으로 고감정 발화 명료도를 향상시켰다. WER·화자 유사도·감정 충실도에서 SOTA 대비 우위를 기록했다. [[G-14]](#ref-g-14)

9. **"Targeted Speaker Poisoning" 연구 (arXiv 2603.07551, 2026-03-08) — 제로샷 TTS의 특정 화자 학습 삭제(machine unlearning) 프레임워크.** 제로샷 TTS가 참조 프롬프트만으로 임의 화자를 복제할 수 있어 기존 머신 언러닝(학습 데이터 삭제)이 무효화된다는 문제를 지적하고, 모델 파라미터를 직접 수정해 특정 화자 생성을 차단하는 SGSP(Speech Generation Speaker Poisoning) 프레임워크를 제안했다. StyleTTS2에 적용한 Encoder-Guided Poisoning(EGP) + triplet-loss로 1~15명 화자 삭제는 효과적이나, 100명 이상에서는 화자 겹침으로 한계를 보였다. [[P-01]](#ref-p-01)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | SXSW 2026에서 "1 Million Voices" ($1B 현물 투자) 이니셔티브 발표 + "11 Voices" 다큐 프리미어. Iconic Voice Marketplace(28개 음성) 출시로 B2B 라이선싱 수익 축 확보. ElevenCreative 멀티모달 플랫폼 공식 런칭. Claude Code TTS 공식 채택으로 파트너 생태계 확장. 현재까지 음성 복원 7,000명 지원, 800개+ 파트너. | [[G-01]](#ref-g-01) [[G-03]](#ref-g-03) [[G-05]](#ref-g-05) [[G-07]](#ref-g-07) |
| Anthropic | Claude Code 음성 모드 출시(2026-03-03)에서 ElevenLabs TTS를 공식 채택. 5개 음성 선택, 추가 비용 없음. Claude Code run-rate 매출 $2.5B+ 돌파(2026년 초 기준). | [[G-07]](#ref-g-07) [[G-08]](#ref-g-08) |
| OpenAI | gpt-4o-mini-tts로 steerable 저지연 TTS 제공 중. 커스텀 보이스(Voice Engine)는 선정 파트너에게만 제한 제공. 2024-03 발표 이후 2년째 일반 배포 지연. | [[G-09]](#ref-g-09) [[G-10]](#ref-g-10) |
| Google | Chirp 3 Instant Custom Voice EU·미국 리전 확대(30개+ 로케일). Google Meet에 보이스 클로닝 기반 AI 음성 번역 라이브 데모. Hume AI 핵심팀(CEO + 7명) DeepMind 합류로 감성 음성 AI 역량 내부화. | [[G-11]](#ref-g-11) [[G-12]](#ref-g-12) [[G-13]](#ref-g-13) |
| Microsoft | Azure Personal Voice DragonV2.1Neural(2025-07 GA) 유지. VibeVoice-1.5B 모델 HuggingFace 공개. 100개 언어, 제로샷 TTS, Personal Voice v2.1 업그레이드(표현력 강화). | [[G-15]](#ref-g-15) |
| YouTube (Google) | 2026-03-10: AI 딥페이크 탐지 도구를 정치인·정부 관료·언론인으로 확대. 음성 인식 딥페이크 탐지도 향후 로드맵에 포함. 현재는 얼굴 유사도 탐지가 주. | [[G-16]](#ref-g-16) [[G-17]](#ref-g-17) |
| Hume AI | CEO Alan Cowen + 핵심 엔지니어 약 7명이 Google DeepMind로 이동. 회사는 존속하나 독자 개발 역량 약화. 누적 조달액 ~$80M. | [[G-13]](#ref-g-13) |
| Bilibili (IndexTTS2) | 2025-09 오픈소스 공개. 감정·화자 정체성 분리, 영상 더빙 특화 duration 제어. WER·화자 유사도·감정 충실도 SOTA 달성 주장. | [[G-14]](#ref-g-14) |
| Matthew McConaughey | ElevenLabs Iconic Marketplace 투자자 겸 고객으로 참여. AI 음성을 활용해 뉴스레터 "Lyrics of Livin'"의 스페인어판 제작. | [[G-04]](#ref-g-04) |

---

## 시장 시그널

- 글로벌 보이스 클로닝 시장: 2026년 추정 $1.1~4.1B(추산 기관별 방법론 차이 존재), 2030년 $9.6~10.8B, CAGR 23~26% [[G-18]](#ref-g-18)
- ElevenLabs "1 Million Voices"의 $1B 현물 투자는 보이스 AI가 단순 기술을 넘어 사회적 인프라로 포지셔닝하는 전략 전환을 의미 [[G-01]](#ref-g-01)
- Iconic Voice Marketplace 출시로 유명인 음성 라이선싱이 새로운 B2B 수익 모델로 제도화됨 — 미디어·엔터·광고 산업 내 AI 음성 채택 가속 [[G-03]](#ref-g-03)
- Anthropic Claude Code TTS 파트너십 확정 → ElevenLabs API가 개발자 도구 생태계에 사실상 표준(de facto standard)으로 자리 잡는 흐름
- Hume AI 핵심팀의 Google DeepMind 합류 → 감성 음성 AI 분야에서 스타트업 vs. 빅테크 인재 경쟁이 인수합병 대신 "acqui-hire 구조"로 전개
- OpenAI Voice Engine 일반 배포 2년 지연: 안전성 이슈가 커스텀 보이스 상용화의 병목으로 지속 [[G-09]](#ref-g-09)
- YouTube의 딥페이크 탐지 범위 확대(2026-03-10)는 플랫폼 레벨 음성 진위 검증 인프라 구축으로 이어질 전망 [[G-16]](#ref-g-16)
- EU AI Act 2026-08-02 전면 시행(Article 50): 합성 음성에 대한 투명성 표기 의무 — 규제 준수 비용 증가로 중소 사업자 진입장벽 상승 [[G-19]](#ref-g-19)
- 아시아태평양 CAGR 28.1%로 글로벌 평균 초과 성장 — 한국·일본·인도 시장이 주요 성장 거점 [[G-18]](#ref-g-18)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Targeted Speaker Poisoning Framework in Zero-Shot TTS (익명 et al., 2026-03-08) | 제로샷 TTS에서 특정 화자 정체성을 선택적으로 차단하는 SGSP 프레임워크 제안. EGP + triplet-loss로 15명까지 효과적 삭제, 100명 이상에서 한계. 보이스 클로닝 프라이버시 보호의 새로운 연구 방향. | [[P-01]](#ref-p-01) |
| Towards Lightweight and Stable Zero-shot TTS with Self-distilled Representation Disentanglement (익명 et al., 2025-01) | 2단계 자기증류(self-distillation)로 언어 콘텐츠와 화자를 분리. 경량화와 안정성을 동시에 달성하는 제로샷 TTS 프레임워크. | [[P-02]](#ref-p-02) |
| IndexTTS: Industrial-Level Controllable Efficient Zero-Shot TTS (Bilibili, 2025-02) | 산업 수준의 제로샷 TTS. 정밀 duration 제어로 영상 더빙 최적화. IndexTTS2의 전신이며 arXiv 공개 후 오픈소스로 전환. | [[P-03]](#ref-p-03) |
| Voice Cloning: Comprehensive Survey (익명 et al., 2025-05) | Few-shot·zero-shot·다국어·화자 적응 전 분야를 망라한 최신 서베이. representation disentanglement를 핵심 연구 동향으로 정의. | [[P-04]](#ref-p-04) |
| Fed-PISA: Federated Voice Cloning via Personalized Identity-Style Adaptation (익명 et al., 2025-09) | 연합학습(Federated Learning) 기반 보이스 클로닝. private ID-LoRA로 화자 음색 로컬 보존, style-LoRA만 서버 전송. 프라이버시-보존 분산 학습 구조 제안. | [[P-05]](#ref-p-05) |

---

## 전략적 시사점

**기회**
- ElevenLabs의 소셜 임팩트 전략("1 Million Voices")은 단순 기술 도구를 접근성 인프라로 격상시키며 규제 압박의 방어막 역할을 겸함. 국내에서도 언어 장애·실어증 환자 대상 음성 복원 사업을 공익 프레임으로 추진할 수 있는 가능성
- Iconic Voice Marketplace 모델은 국내 연예인·방송인 음성 라이선싱에 적용 가능. 한류 콘텐츠의 다국어 AI 더빙 수요와 맞물리면 빠른 시장 형성 기대
- Anthropic Claude Code의 ElevenLabs 채택 사례처럼, 개발자 도구·AI 에이전트 플랫폼에 음성 API를 번들 공급하는 B2B2D(Business-to-Developer) 모델이 고성장 채널로 부상 중
- IndexTTS2·Qwen3-TTS 등 오픈소스 모델 성숙으로 자체 모델 구축 비용 하락 → 한국어 특화 파인튜닝(감정·방언·방송 스타일) 차별화 여지 존재

**위협**
- EU AI Act 2026-08 Article 50 시행 임박: 합성 음성 투명성 표기 의무 불이행 시 글로벌 서비스 운영 리스크. 중소 사업자는 컴플라이언스 비용 부담으로 시장 퇴출 압력
- YouTube 딥페이크 탐지 확대(음성 탐지 로드맵 포함)와 플랫폼별 자체 규제 강화로 무단 보이스 클로닝 콘텐츠의 배포 창구가 점차 차단
- OpenAI Voice Engine의 지속적 배포 지연은 안전성 요건이 높다는 신호 — 동의 없는 보이스 클로닝 서비스는 향후 규제 표적이 될 가능성이 높음
- Hume AI 핵심팀 Google DeepMind 합류는 빅테크의 감성 음성 AI 역량 내부화 추세를 반영. 독립 스타트업이 차별화 기술 기반을 유지하기 어려워지는 환경

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | PR Newswire — ElevenLabs debuts '11 Voices' docuseries at SXSW, 1 Million Voices initiative | [링크](https://www.prnewswire.com/news-releases/elevenlabs-debuts-11-voices-docuseries-at-sxsw-as-part-of-global-campaign-to-reach-1-million-people-with-voice-loss-302711275.html) | press | 2026-03-11 | [A] |
| <a id="ref-g-02"></a>G-02 | ElevenLabs Blog — Honoring Eric Dane's Legacy at SXSW: Advancing 1 Million Voices | [링크](https://elevenlabs.io/blog/honoring-eric-danes-legacy-at-sxsw-advancing-1-million-voices) | blog | 2026-03-11 | [A] |
| <a id="ref-g-03"></a>G-03 | AdWeek — ElevenLabs Launches AI Voice Licensing Marketplace, Adds Matthew McConaughey as Investor | [링크](https://www.adweek.com/media/elevenlabs-ai-voice-marketplace-matthew-mcconaughey/) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | ElevenLabs Blog — Announcing Partnership with Sir Michael Caine to Iconic Marketplace | [링크](https://elevenlabs.io/blog/announcing-partnership-with-sir-michael-caine-to-newly-launched-iconic-marketplace) | blog | 2026-03 | [A] |
| <a id="ref-g-05"></a>G-05 | Blockchain.news — ElevenLabs Launches ElevenCreative Account: Multimodal AI | [링크](https://blockchain.news/ainews/elevenlabs-launches-elevencreative-account-multimodal-ai-for-voice-cloning-70-language-dubbing-and-music-generation-latest-2026-update) | news | 2026-03-10 | [B] |
| <a id="ref-g-06"></a>G-06 | ElevenLabs — ElevenCreative Platform Overview | [링크](https://elevenlabs.io/creative) | web | 2026-03 | [A] |
| <a id="ref-g-07"></a>G-07 | The Decoder — Anthropic's Claude uses ElevenLabs technology for speech features | [링크](https://the-decoder.com/anthropics-claude-uses-elevenlabs-technology-for-speech-features-rather-than-an-in-house-model/) | news | 2026-03 | [B] |
| <a id="ref-g-08"></a>G-08 | TechCrunch — Claude Code rolls out a voice mode capability | [링크](https://techcrunch.com/2026/03/03/claude-code-rolls-out-a-voice-mode-capability/) | news | 2026-03-03 | [B] |
| <a id="ref-g-09"></a>G-09 | TechCrunch — A year later, OpenAI still hasn't released its voice cloning tool | [링크](https://techcrunch.com/2025/03/06/a-year-later-openai-still-hasnt-released-its-voice-cloning-tool/) | news | 2025-03-06 | [B] |
| <a id="ref-g-10"></a>G-10 | OpenAI — Introducing next-generation audio models in the API | [링크](https://openai.com/index/introducing-our-next-generation-audio-models/) | blog | 2026 | [A] |
| <a id="ref-g-11"></a>G-11 | Google Cloud Docs — Chirp 3: Instant Custom Voice Release Notes | [링크](https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice) | web | 2026-03 | [A] |
| <a id="ref-g-12"></a>G-12 | News.oneboard.network — AI Voice Translation live Demo in Google Meet | [링크](https://news.oneboard.network/2026/03/ai-voice-translation-live-demo-in.html) | news | 2026-03 | [C] |
| <a id="ref-g-13"></a>G-13 | TechCrunch — Google snags team behind AI voice startup Hume AI | [링크](https://techcrunch.com/2026/01/22/google-reportedly-snags-up-team-behind-ai-voice-startup-hume-ai/) | news | 2026-01-22 | [B] |
| <a id="ref-g-14"></a>G-14 | AI Adoption Agency — IndexTeam Index TTS 2: Emotionally Expressive Voice Synthesis | [링크](https://aiadoptionagency.com/indexteam-index-tts-2-emotionally-expressive-voice-synthesis-revealed/) | blog | 2025-09 | [C] |
| <a id="ref-g-15"></a>G-15 | Microsoft Tech Community — Personal Voice upgraded to v2.1 in Azure AI Speech | [링크](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/personal-voice-upgraded-to-v2-1-in-azure-ai-speech-more-expressive-than-ever-bef/4435233) | blog | 2026 | [A] |
| <a id="ref-g-16"></a>G-16 | TechCrunch — YouTube expands AI deepfake detection to politicians, government officials, and journalists | [링크](https://techcrunch.com/2026/03/10/youtube-expands-ai-deepfake-detection-to-politicians-government-officials-and-journalists/) | news | 2026-03-10 | [B] |
| <a id="ref-g-17"></a>G-17 | The AI Insider — YouTube Expands AI Deepfake Detection Tools to Government Officials | [링크](https://theaiinsider.tech/2026/03/11/youtube-expands-ai-deepfake-detection-tools-to-government-officials-politicians-and-journalists/) | news | 2026-03-11 | [B] |
| <a id="ref-g-18"></a>G-18 | Business Research Company — Voice Cloning Market 2026, Size and Demand Forecast | [링크](https://www.thebusinessresearchcompany.com/report/voice-cloning-global-market-report) | report | 2026 | [B] |
| <a id="ref-g-19"></a>G-19 | AI Tribune — AI Voice Cloning Regulation in 2026 | [링크](https://aitribune.net/2026/02/24/ai-voice-cloning-regulation-in-2026/) | blog | 2026-02-24 | [C] |
| <a id="ref-g-20"></a>G-20 | Hollywood Reporter — Babe Ruth, Lana Turner, McConaughey — ElevenLabs Has the Voices | [링크](https://www.hollywoodreporter.com/business/digital/elevenlabs-ai-voices-babe-ruth-judy-garland-1236423582/) | news | 2026-03 | [B] |
| <a id="ref-g-21"></a>G-21 | Radio World — ElevenLabs Launches AI Voice Licensing Marketplace | [링크](https://www.radioworld.com/columns-and-views/guest-commentaries/elevenlabs-launches-ai-voice-licensing-marketplace) | news | 2026-03 | [B] |
| <a id="ref-g-22"></a>G-22 | Winbuzzer — Anthropic Rolls Out Voice Mode for Claude Code | [링크](https://winbuzzer.com/2026/03/04/anthropic-rolls-out-voice-mode-claude-code-xcxwbn/) | news | 2026-03-04 | [B] |
| <a id="ref-p-01"></a>P-01 | 익명 et al. — Targeted Speaker Poisoning Framework in Zero-Shot Text-to-Speech (arXiv 2603.07551) | [링크](https://arxiv.org/abs/2603.07551) | paper | 2026-03-08 | [A] |
| <a id="ref-p-02"></a>P-02 | 익명 et al. — Towards Lightweight and Stable Zero-shot TTS with Self-distilled Representation Disentanglement (arXiv 2501.08566) | [링크](https://arxiv.org/html/2501.08566) | paper | 2025-01 | [A] |
| <a id="ref-p-03"></a>P-03 | Bilibili/IndexTeam — IndexTTS: Industrial-Level Controllable Efficient Zero-Shot TTS (arXiv 2502.05512) | [링크](https://arxiv.org/abs/2502.05512) | paper | 2025-02 | [A] |
| <a id="ref-p-04"></a>P-04 | 익명 et al. — Voice Cloning: Comprehensive Survey (arXiv 2505.00579) | [링크](https://arxiv.org/abs/2505.00579) | paper | 2025-05 | [A] |
| <a id="ref-p-05"></a>P-05 | 익명 et al. — Fed-PISA: Federated Voice Cloning via Personalized Identity-Style Adaptation (arXiv 2509.16010) | [링크](https://arxiv.org/html/2509.16010v1) | paper | 2025-09 | [A] |
