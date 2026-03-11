---
type: deep-research
topic: voice-synthesis
date: 2026-03-11
parent: weekly-voice-ai
agent: research-deep
confidence: high
sources_used: [websearch, websearch-fetch]
---

# Deep Research: Voice Synthesis (2026-03-11)

> **조사 기간**: 2026-03-04 ~ 2026-03-11
> **핵심 발견**: 오픈소스 TTS 생태계가 폭발적으로 성장하며 상용 서비스 격차를 빠르게 좁히고 있음. 경량화(82M~400M 파라미터), 스트리밍 실시간 합성, 감정 표현 제어가 핵심 기술 방향으로 수렴. 네이버는 한국어 TTS MOS 4.22/5로 상업 수준 달성 확인. EU AI Act 합성음 라벨링 의무가 2026년 8월 발효 예정으로 규제 리스크 가시화.

---

## 기술 동향

1. **Qwen3-TTS (Alibaba, 2026-01-22) — Apache 2.0 오픈소스, 3초 클로닝, 97ms 스트리밍 지연.** Alibaba Cloud Qwen팀이 공개한 오픈소스 TTS 시리즈. 1.7B 파라미터 플래그십(Qwen3-TTS-12Hz-1.7B)과 0.6B 경량 버전 두 가지. Dual-Track hybrid streaming 아키텍처로 97ms 초저지연 스트리밍을 달성했으며, 자연어 지시로 억양·감정·발화 속도를 제어한다. 10개 언어(한국어 포함) 지원, Apache 2.0으로 상업 활용 자유. 3초 레퍼런스 오디오만으로 화자 복제 가능. [[G-01]](#ref-g-01) [[G-02]](#ref-g-02)

2. **Kani-TTS-2 (nineninesix.ai, 2026-02-15) — 400M 파라미터, 3GB VRAM, RTF 0.2.** LiquidAI의 LFM2(350M) 아키텍처 기반. NVIDIA NanoCodec으로 오디오를 언어 토큰처럼 처리. 10초 오디오를 2초에 생성(RTF=0.2), RTX 3060급 소비자 GPU에서 동작. 10,000시간 데이터로 H100 8장을 6시간만 사용해 학습 완료. Apache 2.0 라이선스. 영어·포르투갈어 버전 Hugging Face 공개. [[G-03]](#ref-g-03) [[G-04]](#ref-g-04)

3. **Orpheus TTS (Canopy AI, 2026-03-19 출시 예고) — Llama-3B 기반, 200ms 스트리밍 지연, 감정 태그.** 100,000+ 시간 영어 음성 데이터 학습. `<laugh>`, `<sigh>`, `<chuckle>` 등 감정 태그로 세밀한 표현 제어. 입력 스트리밍과 KV 캐싱 조합 시 25~50ms 지연 달성 가능. Zero-shot 화자 복제 지원. 오픈소스로 공개 예정(GitHub: canopyai/Orpheus-TTS). [[G-05]](#ref-g-05)

4. **Kokoro-82M — 82M 파라미터, 대형 모델 수준 품질, API 단가 $0.06/오디오시간.** StyleTTS2+ISTFTNet 기반으로 인코더·디퓨전 없이 고속 생성. Elo 방식 자연스러움 평가에서 Fish Speech(~100만 시간 학습) 등 대형 모델을 추월. 한국어·일본어·중국어·영어·프랑스어 지원. Together AI 통해 API 서빙, 100만 자 기준 $1 미만. Apache 2.0. [[G-06]](#ref-g-06)

5. **Dia2 (Nari Labs) — 스트리밍 대화형 TTS, 첫 토큰부터 합성 시작.** 전체 텍스트 수신 없이 첫 몇 단어 입력 즉시 오디오 생성 개시. 멀티턴 전환 지연 감소로 실시간 음성-음성 파이프라인에 최적화. 1B·2B 체크포인트 제공, [S1]/[S2] 태그로 화자 구분. 오디오 prefix conditioning으로 화자 일관성 유지. [[G-07]](#ref-g-07)

6. **Gemini 2.5 TTS Flash/Pro — 자연어 스타일 프롬프트, 24개 언어, 30개 화자.** Google이 Gemini 2.5 Flash TTS(저지연 최적화)와 Pro TTS(품질 최적화)를 GA 출시. 자연어 지시로 억양·속도·감정 제어, 복잡 콘텐츠에서 자동 속도 조절. 멀티 스피커 대화 합성 지원. Cloud TTS API와 Vertex AI API 양쪽으로 제공. [[G-08]](#ref-g-08) [[G-09]](#ref-g-09)

7. **ElevenLabs Eleven v3 — 70+ 언어, Audio Tags 감정 제어, 상업 GA.** Alpha에서 정식 상업 출시 완료. `[whispers]`, `[shouts]`, `[strong X accent]`, `[sings]` 등 오디오 태그로 감정·억양·노래 제어. 복잡 텍스트(화학식, 전화번호) 오류 68% 감소. Text to Dialogue API로 멀티 화자 자연스러운 대화 합성. 에이전트 플랫폼(ElevenAgents)·창작 스튜디오(ElevenCreative)·개발자 API(ElevenAPI) 3개 축으로 플랫폼 재편. [[G-10]](#ref-g-10) [[G-11]](#ref-g-11)

8. **HyperCLOVA X 8B Omni (Naver, 2026-01) — 한국어 TTS MOS 4.22/5, 옴니모달 단일 모델.** 텍스트·오디오·비전 입출력을 단일 모델로 통합. 30명 평가자 대상 MOS(1~5점) 평가에서 한국어 TTS 4.22 달성, 2위 대비 0.82점 우위. 한국 정부 기반모델 사업 일환으로 공개. HyperCLOVA X SEED 32B Think(음성 추가형)와 8B Omni(동시 멀티모달 학습형) 두 트랙. [[G-12]](#ref-g-12) [[G-13]](#ref-g-13)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| **ElevenLabs** | Eleven v3 GA 출시(2026-02-12). Audio Tags 감정 제어, 70+ 언어, 복잡 텍스트 오류 68% 감소. ElevenAgents/ElevenCreative/ElevenAPI 3개 축으로 플랫폼 확장. | [[G-10]](#ref-g-10) [[G-11]](#ref-g-11) |
| **Google** | Gemini 2.5 TTS Flash(저지연)·Pro(품질) GA. 자연어 스타일 프롬프트, 24언어 30화자 멀티스피커 지원. Cloud TTS 380+ 음성 50+ 언어 별도 유지. | [[G-08]](#ref-g-08) [[G-09]](#ref-g-09) |
| **Alibaba (Qwen팀)** | Qwen3-TTS 오픈소스 공개(Apache 2.0). 1.7B·0.6B 두 변형, 97ms 스트리밍, 10개 언어, 3초 클로닝. 상용 모델과 경쟁하는 수준 평가. | [[G-01]](#ref-g-01) [[G-02]](#ref-g-02) |
| **Naver** | HyperCLOVA X 8B Omni (2026-01) 공개. 한국어 TTS MOS 4.22/5(2위 대비 +0.82). 정부 기반모델 사업 연계. OmniServe 서빙 코드 GitHub 공개. | [[G-12]](#ref-g-12) [[G-13]](#ref-g-13) |
| **Nari Labs** | Dia2 스트리밍 대화 TTS 공개. 1B·2B 오픈소스, 멀티턴 실시간 화자 전환. | [[G-07]](#ref-g-07) |
| **nineninesix.ai** | Kani-TTS-2 출시(2026-02-15). 400M 파라미터, RTF 0.2, 3GB VRAM, Apache 2.0. | [[G-03]](#ref-g-03) [[G-04]](#ref-g-04) |
| **Canopy AI** | Orpheus TTS 개발(2026-03-19 예고). Llama-3B 기반, 100k+ 시간 학습, 200ms 이하 스트리밍. | [[G-05]](#ref-g-05) |
| **Play.ht** | 30초 레퍼런스 오디오 즉시 클로닝, 140+ 언어 800+ 음성 스타일, 감정 딜리버리 제어. | [[G-15]](#ref-g-15) |
| **Resemble AI** | 신경 워터마킹(Neural Watermarking) 탑재, 기업 API·보안 기능 강화 포지셔닝. | [[G-15]](#ref-g-15) |
| **Microsoft Azure** | Neural TTS 440+ 음성, 140+ 언어/변형. 48kHz 고품질, 멀티토커 대화. 최근 공개 발표 없음. | [[G-16]](#ref-g-16) |
| **Supertone (HYBE 자회사)** | K-pop 아이돌 목소리 합성, 한국어 자연스러움 강점. 2022년 HYBE가 $32M에 인수. SYNDI8 가상 걸그룹 운영 중. | [[G-17]](#ref-g-17) |

---

## 시장 시그널

- AI 보이스 제너레이터 시장은 2025년 $4.16B에서 2031년 $20.71B으로 성장 전망, CAGR 30.7% [[G-18]](#ref-g-18)
- Neural TTS 엔진·음성 합성 세그먼트가 2025년 전체 AI 음성 시장의 49.6% 비중 차지, 최대 단일 세그먼트 [[G-18]](#ref-g-18)
- 오픈소스 TTS 모델 출시 속도가 급등, 2026년 1~3월에만 Qwen3-TTS, Kani-TTS-2, Orpheus TTS, Kokoro-82M 등 다수 등장 — 상용 API 의존도 감소 압력 [[G-04]](#ref-g-04) [[G-06]](#ref-g-06)
- EU AI Act Article 50 합성 오디오 라벨링 의무가 2026년 8월 발효 예정. 2025년 12월 EU 집행위 1차 초안 공개 [[G-19]](#ref-g-19)
- 실시간 대화 에이전트 수요가 TTS 지연 요구를 100ms 이하로 당기고 있음 — Dia2·Orpheus가 해당 포지션 공략 [[G-07]](#ref-g-07)
- 한국 시장: Naver HyperCLOVA X Omni가 상업 수준 한국어 TTS 달성, Supertone은 K-pop·엔터 특화 영역 유지 [[G-12]](#ref-g-12)
- 멀티모달 통합 추세 — TTS가 독립 모듈에서 옴니모달 모델(HyperCLOVA X, Gemini) 내부 기능으로 흡수되는 방향 [[G-13]](#ref-g-13)
- 음성 워터마킹·딥페이크 탐지가 상용 제품 차별화 요소로 부상 (Resemble AI 신경 워터마킹, EU 규제 연계) [[G-19]](#ref-g-19)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| HyperCLOVA X 8B Omni (NAVER Cloud Team, 2026) | 텍스트·오디오·비전 any-to-any 단일 모델. 한국어 TTS MOS 4.22/5로 상업 수준 달성. | [[P-01]](#ref-p-01) |
| ARCHI-TTS: Flow-Matching-Based TTS with Self-supervised Semantic Aligner (2026-02) | 비자기회귀 플로우 매칭 디코더 + 의미 정렬기 조합. 디노이징 단계 간 인코더 특성 재사용으로 추론 가속. | [[P-02]](#ref-p-02) |
| Towards Controllable Speech Synthesis in the Era of LLMs: A Survey (Tan et al., 2024) | LLM 기반 제어 가능 음성 합성 체계 정리. 비자기회귀(NAR) vs 자기회귀(AR) 분류, 감정·스타일 제어 최신 동향. | [[P-03]](#ref-p-03) |
| VoiceCraft-X: Multilingual Voice-Cloning TTS and Speech Editing (EMNLP 2025) | 자기회귀 신경 코덱 언어 모델로 11개 언어 Zero-shot TTS + 음성 편집 통합. | [[P-04]](#ref-p-04) |

---

## 전략적 시사점

**기회**
- 오픈소스 경량 TTS(Kokoro 82M, Kani-TTS-2 400M)가 온디바이스·엣지 배포를 현실화, 클라우드 API 비용 없이 프라이버시 보장형 음성 합성 구현 가능
- Dia2·Orpheus 등 스트리밍 아키텍처가 실시간 음성 대화 에이전트 품질 임계점을 낮춤, 보이스 에이전트 서비스 진입 비용 감소
- HyperCLOVA X Omni가 한국어 TTS에서 상업 수준 달성 — 국내 고품질 한국어 음성 합성의 오픈소스 기반 확보 가능성

**위협**
- Qwen3-TTS(Apache 2.0) 등 대형 테크 기업 오픈소스 공개로 중소 상용 TTS API 업체의 가격 경쟁력 급격히 약화
- EU AI Act Article 50 합성 오디오 의무 라벨링(2026년 8월)이 모든 음성 합성 제품의 컴플라이언스 비용 추가
- 음성 딥페이크·보이스 피싱 악용이 규제 강화를 촉진하고, 한국 포함 아시아 시장에서도 유사 입법 가속될 가능성

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | QwenLM — Qwen3-TTS GitHub | [링크](https://github.com/QwenLM/Qwen3-TTS) | blog/repo | 2026-01-22 | [A] |
| <a id="ref-g-02"></a>G-02 | Qwen Blog — Qwen3-TTS Family is Now Open Sourced | [링크](https://qwen.ai/blog?id=qwen3tts-0115) | news | 2026-01-22 | [A] |
| <a id="ref-g-03"></a>G-03 | MarkTechPost — Kani-TTS-2 400M param open source TTS | [링크](https://www.marktechpost.com/2026/02/15/meet-kani-tts-2-a-400m-param-open-source-text-to-speech-model-that-runs-in-3gb-vram-with-voice-cloning-support/) | news | 2026-02-15 | [B] |
| <a id="ref-g-04"></a>G-04 | Hugging Face — nineninesix/kani-tts-2-en | [링크](https://huggingface.co/nineninesix/kani-tts-2-en) | repo | 2026-02-15 | [A] |
| <a id="ref-g-05"></a>G-05 | Communeify — Orpheus TTS emotional speech synthesis | [링크](https://www.communeify.com/en/blog/orpheus-tts-emotional-human-speech-synthesis/) | blog | 2026-03 | [C] |
| <a id="ref-g-06"></a>G-06 | Hugging Face — hexgrad/Kokoro-82M | [링크](https://huggingface.co/hexgrad/Kokoro-82M) | repo | 2025 | [A] |
| <a id="ref-g-07"></a>G-07 | GitHub — nari-labs/dia2 | [링크](https://github.com/nari-labs/dia2) | repo | 2026 | [A] |
| <a id="ref-g-08"></a>G-08 | Google Blog — Gemini 2.5 Text-to-Speech model updates | [링크](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-2-5-text-to-speech/) | news | 2026 | [A] |
| <a id="ref-g-09"></a>G-09 | Google Cloud Docs — Gemini-TTS | [링크](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts) | doc | 2026 | [A] |
| <a id="ref-g-10"></a>G-10 | ElevenLabs Blog — Eleven v3: Most Expressive AI TTS | [링크](https://elevenlabs.io/blog/eleven-v3) | news | 2026-02-12 | [A] |
| <a id="ref-g-11"></a>G-11 | Releasebot — Eleven Labs Release Notes March 2026 | [링크](https://releasebot.io/updates/eleven-labs) | news | 2026-03 | [B] |
| <a id="ref-g-12"></a>G-12 | NAVER Corp — Omnimodal HyperCLOVA X Press Release | [링크](https://www.navercorp.com/en/media/pressReleasesDetail?seq=34256) | news | 2026-01 | [A] |
| <a id="ref-g-13"></a>G-13 | CLOVA Tech Blog — HyperCLOVA X OMNI Omnimodality | [링크](https://clova.ai/en/tech-blog/hyperclova-x-omni-koreas-flagship-ai-on-the-road-to-omnimodality) | blog | 2026-01 | [A] |
| <a id="ref-g-14"></a>G-14 | BentoML — Best Open-Source TTS Models 2026 | [링크](https://www.bentoml.com/blog/exploring-the-world-of-open-source-text-to-speech-models) | blog | 2026 | [B] |
| <a id="ref-g-15"></a>G-15 | Resemble AI — Best AI Voice Generators 2026 | [링크](https://www.resemble.ai/best-ai-voice-generators-real-people/) | blog | 2026 | [C] |
| <a id="ref-g-16"></a>G-16 | Microsoft Learn — Azure TTS Overview | [링크](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech) | doc | 2026 | [A] |
| <a id="ref-g-17"></a>G-17 | Music Business Worldwide — Supertone SYNDI8 launch after HYBE acquisition | [링크](https://www.musicbusinessworldwide.com/hybe-owned-voice-cloning-startup-supertone-launches-ai-powered-virtual-pop-group-syndi81/) | news | 2024 | [B] |
| <a id="ref-g-18"></a>G-18 | MarketsandMarkets — AI Voice Generator Market $20.71B by 2031 | [링크](https://www.marketsandmarkets.com/PressReleases/ai-voice-generator.asp) | report | 2025 | [B] |
| <a id="ref-g-19"></a>G-19 | Jones Day — EU Commission Draft Code of Practice AI Labelling | [링크](https://www.jonesday.com/en/insights/2026/01/european-commission-publishes-draft-code-of-practice-on-ai-labelling-and-transparency) | legal | 2026-01 | [A] |
| <a id="ref-g-20"></a>G-20 | GitHub — canopyai/Orpheus-TTS | [링크](https://github.com/canopyai/Orpheus-TTS) | repo | 2026-03 | [A] |
| <a id="ref-p-01"></a>P-01 | NAVER Cloud HyperCLOVA X Team — HyperCLOVA X 8B Omni | [링크](https://arxiv.org/abs/2601.01792) | paper | 2026-01 | [A] |
| <a id="ref-p-02"></a>P-02 | ARCHI-TTS: Flow-Matching-Based TTS with Semantic Aligner | [링크](https://arxiv.org/abs/2602.05207) | paper | 2026-02 | [A] |
| <a id="ref-p-03"></a>P-03 | Tan et al. — Controllable Speech Synthesis in Era of LLMs: Survey | [링크](https://arxiv.org/html/2412.06602v1/) | paper | 2024-12 | [A] |
| <a id="ref-p-04"></a>P-04 | VoiceCraft-X: Multilingual Voice-Cloning TTS and Editing (EMNLP 2025) | [링크](https://aclanthology.org/2025.emnlp-main.137/) | paper | 2025 | [A] |
