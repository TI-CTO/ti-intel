---
type: weekly-deep-research
topic: voice-cloning
date: 2026-03-24
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
parent: 2026-03-24_weekly-voice-ai.md
note: intel-store MCP 미사용 (VSCode 확장 환경 제약) — WebSearch 전량 대체
---

# Deep 리서치: Voice Cloning (2026-W13)

## 이전 대비 변화

- **전주 (W12, 2026-03-17)**: ElevenLabs SXSW "1M Voices" 이니셔티브($1B 현물 투자), Iconic Marketplace(28명 유명인 라이선스), YouTube 딥페이크 탐지 확대, OpenAI Voice Engine 2년째 일반 배포 지연, Hume AI 핵심팀 Google DeepMind 합류
- **금주 (W13, 2026-03-24)**: Fortune·연구자 "구별 불가능 임계점(indistinguishable threshold)" 공식 선언, LiveKit $100M/$1B 유니콘 확정(1월 발표 후 업계 파급 지속), Pindrop–Zoom 실시간 딥페이크 탐지 통합(3월 12일), ElevenLabs Eleven v3 일반 공개(GA), UN·INTERPOL 글로벌 프로드 서밋(비엔나)에서 음성 클로닝 악용 경고, EU AI Act 8월 전면 시행 임박
- **변화 방향**: 기술 성숙도가 "구별 불가 임계점"을 넘어서며 생성·탐지의 비대칭성이 전면화됨. 투자 자본은 생성 플랫폼(LiveKit, Synthflow, Beside 등)과 탐지 인프라(Pindrop)로 동시 유입. EU·UN 수준의 다자 규제 기틀이 2026년 하반기 본격 집행 예정.

---

## 기술 동향

1. **"구별 불가능 임계점" 공식 선언 — 수초 오디오로 완전 복제, 탐지 인간 정확도 54% 수준.**
   Fortune(2025-12-27 게재, 2026 전반 확산)은 딥페이크 전문가 Siwei Lyu(SUNY Buffalo) 인용으로 음성 클로닝이 "indistinguishable threshold"를 넘었다고 선언했다. 자연스러운 억양·리듬·감정·숨소리까지 복제하는 데 수초 샘플만으로 충분하며, 인간이 딥페이크 음성을 탐지하는 정확도는 54%에 불과하다(우연 수준). 온라인 딥페이크 볼륨은 2023년 50만 건에서 2025년 800만 건으로 900% 이상 성장했다. [[G-01]](#ref-g-01) [[G-02]](#ref-g-02)

2. **ElevenLabs Eleven v3 일반 공개(GA) — 70개 언어, 멀티 스피커 대화, 감정 오디오 태그 지원.**
   ElevenLabs의 flagship 모델 eleven_v3가 알파를 졸업해 일반 공개(GA) 전환됐다. 70개 언어 지원, 멀티 스피커 대화(Multi-speaker Dialogue API 신규), `[excited]` `[whispers]` `[sighs]` 등 오디오 태그로 감정 세밀 제어가 가능하다. 실시간 사용 사례(대화형 에이전트)에는 v2.5 Turbo·Flash 유지를 권장하며, v3 실시간 버전은 개발 중이다. Studio 3.0(음성·영상·음악 통합 제작 환경)과 결합해 단일 브라우저 환경에서 엔드투엔드 콘텐츠 제작이 가능해졌다. [[G-03]](#ref-g-03) [[G-04]](#ref-g-04)

3. **OpenAI gpt-realtime 프로덕션 모델 출시 — 지시 추종 30.5%, 함수 호출 66.5%, 신규 음성 2종.**
   OpenAI가 gpt-realtime을 프로덕션 지향 음성 에이전트 모델로 공식 출시했다. MultiChallenge 오디오 벤치마크 기준 지시 추종 정확도 30.5%(이전 모델 20.6%), ComplexFuncBench 기준 함수 호출 66.5%(이전 49.7%)로 대폭 개선됐다. 신규 음성 Marin·Cedar 추가, 텍스트-음성 변환 파이프라인 없이 단일 모델에서 오디오를 직접 처리해 지연 시간을 단축했다. Voice Engine(커스텀 음성 클로닝)은 여전히 선정 파트너 제한 배포 중이다. [[G-05]](#ref-g-05) [[E-01]](#ref-e-01)

4. **Google Gemini 2.5 TTS GA 출시 + AI Studio 음성 클로닝 베타 준비 — 30개 스피커, 80개 로케일.**
   Google이 Gemini 2.5 Flash·Pro TTS를 GA로 출시, 30개 스피커·80개 이상 로케일 지원, 자연어 프롬프트로 스타일·억양·속도·감정을 세밀하게 제어할 수 있다. AI Studio에서는 "Create Your Voice" 기능이 UI에 노출됐으나 아직 비활성 상태로, Gemini 3 Flash에 네이티브 음성 클로닝이 내장될 가능성을 시사한다. Chirp 3 Instant Custom Voice는 EU·미국 리전 클로닝 키 생성을 지원하며, Zero Audio Retention 정책으로 프라이버시 리스크를 완화했다. [[G-06]](#ref-g-06) [[G-07]](#ref-g-07) [[E-02]](#ref-e-02)

5. **딥페이크 탐지 일반화 실패 — 실험실 vs. 실제 통화 채널 간 성능 격차 확인, 개선 가이드라인으로 57% 향상 가능.**
   PMC 게재 리뷰 논문(2026)은 기존 딥페이크 탐지 데이터셋이 실제 통신 채널(전화) 노이즈를 반영하지 못해 실세계 일반화에 실패한다는 증거를 제시했다. 원본 딥페이크 오디오와 통신 채널을 통과한 딥페이크 오디오 간의 특성 차이가 탐지 성능을 크게 저하시킨다. 개선된 데이터셋 가이드라인 적용 시 실험실 정확도 39%, 실세계 벤치마크 정확도 57% 향상이 가능하다고 밝혔다. [[P-01]](#ref-p-01)

6. **Targeted Speaker Poisoning 프레임워크 (arXiv 2603.07551) — 특정 화자 생성 차단, 15명까지 효과적.**
   USC·UCSF 연구팀이 제로샷 TTS 모델에서 특정 화자의 음성 생성을 차단하는 Speech Generation Speaker Poisoning(SGSP) 프레임워크를 제안했다(2026-03-08 제출). 기존 머신 언러닝은 제로샷 TTS가 참조 프롬프트만으로 화자를 동적으로 재현하기 때문에 무효화된다는 점을 지적하고, Encoder-Guided Poisoning(EGP) + triplet-loss로 모델 파라미터를 직접 수정하는 방식을 채택했다. 1~15명 화자 삭제에서 높은 프라이버시 보호를 달성했으나, 100명 이상에서는 화자 정체성 겹침으로 한계를 보였다. [[P-02]](#ref-p-02)

7. **Pindrop–Zoom 실시간 딥페이크 탐지 통합(2026-03-12) — 접촉 센터 2초 내 탐지, 정확도 99%.**
   Pindrop이 Zoom Contact Center에 실시간 딥페이크 탐지 및 음성 인증을 통합했다. 15억 건 이상의 실세계 인터랙션으로 훈련된 모델을 기반으로 2초 내에 합성 음성을 탐지하며 정확도 99%를 주장한다. 금융·의료·보험·통신·정부 분야를 타깃으로 하며, 300개 이상 특허로 보호된다. Gartner는 2026년까지 기업의 30%가 딥페이크로 인해 단일 신원 검증 솔루션을 신뢰하지 않게 될 것이라고 전망했다. [[G-08]](#ref-g-08) [[G-09]](#ref-g-09)

8. **UN·INTERPOL 글로벌 프로드 서밋(비엔나, 2026-03) — 음성 클로닝 조직 사기 주범으로 지목.**
   UN 마약범죄사무소(UNODC)와 INTERPOL이 비엔나·방콕 이중 서밋에서 동남아시아 기반 사기 조직이 음성 클로닝·딥페이크를 조직 범죄 인프라로 활용하고 있다고 경고했다. 다크웹 마켓플레이스에서 수초 음성·영상으로 신원 복제 가능한 툴이 서비스형 사이버범죄(CaaS)로 판매 중이다. 미국의 2024년 대상 피해액만 $10B로 집계됐으며, AI 주도 사기는 2025년 1,210% 급증했다. [[G-10]](#ref-g-10) [[G-11]](#ref-g-11)

9. **EU AI Act Article 50 전면 시행 D-130 — 음성 클로닝 콘텐츠 공시 의무, 위반 시 매출의 7%.**
   EU AI Act Article 50은 딥페이크 및 합성 오디오/음성에 대한 투명성 의무를 규정하며 2026년 8월 2일 전면 시행된다. AI 생성 음성 콘텐츠에 대한 레이블링·워터마킹·메타데이터 의무가 부과되며, 비준수 시 연간 글로벌 매출의 7% 또는 €1,500만 중 높은 금액의 과징금이 부과된다. 콘텐츠 투명성 코드 오브 프랙티스는 2026년 5~6월 확정 예정이다. [[G-12]](#ref-g-12) [[G-13]](#ref-g-13)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| ElevenLabs | Eleven v3 GA 전환(70개 언어, 오디오 태그, Multi-speaker Dialogue API). Studio 3.0으로 음성·영상·음악 통합 제작 환경 완성. $500M Series D($11B 밸류에이션) 조달 후 플랫폼 확장 가속. Iconic Voice Marketplace 유지·확대 예정. | [[G-03]](#ref-g-03), [[G-04]](#ref-g-04), [[G-14]](#ref-g-14) |
| OpenAI | gpt-realtime 프로덕션 모델 출시(지시 추종 +48%, 함수 호출 +34%). 오디오 팀 통합, 차세대 오디오 모델·스크린리스 디바이스 개발 중. Voice Engine 커스텀 클로닝은 선정 파트너 제한 배포 지속. | [[G-05]](#ref-g-05), [[E-01]](#ref-e-01), [[G-15]](#ref-g-15) |
| Google | Gemini 2.5 TTS(Flash/Pro) GA 출시, 30개 스피커·80개 로케일. AI Studio에 음성 클로닝 UI 노출(비활성). Chirp 3 Instant Custom Voice EU·미국 리전 지원. Hume AI 핵심팀 DeepMind 합류(1월)로 감성 음성 AI 역량 내부화. | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07), [[E-02]](#ref-e-02) |
| LiveKit | 2026-01-22 Series C $100M($1B 밸류에이션) 완료. Index Ventures·Salesforce Ventures 주도. OpenAI 음성 인프라 공급사. Tesla·Agentforce 등 대형 고객 확보. 실시간 음성·영상·AI 개발자 플랫폼으로 포지셔닝. | [[G-16]](#ref-g-16), [[G-17]](#ref-g-17) |
| Meta | PlayAI 2025-07 인수 완료(팀 35명 흡수). 기술이 내부 AI Characters·Meta AI·Wearables에 통합됨. PlayAI 서비스는 2025-12-31 종료. | [[G-18]](#ref-g-18), [[G-19]](#ref-g-19) |
| Resemble AI | Play.ht 공백 이후 보안 중심 음성 클로닝 플랫폼으로 포지셔닝 강화. 딥페이크 탐지(PerTh Watermarking) 겸업. | [[G-20]](#ref-g-20) |
| Pindrop | Zoom Contact Center 실시간 딥페이크 탐지 통합(2026-03-12). 15억 건 인터랙션 기반 모델, 2초 탐지, 정확도 99% 주장. 300개+ 특허 보유. | [[G-08]](#ref-g-08), [[G-09]](#ref-g-09) |
| SKT / Naver | SKT, 한국 주권 AI 프로그램 1라운드 통과(A.X 4.0 성능 GPT-4o 수준 주장). Naver Cloud는 모델 독창성 문제로 1라운드 탈락. 음성 클로닝 전용 공시 없음. | [[G-21]](#ref-g-21), [[G-22]](#ref-g-22) |
| Synthflow AI | $20M Series A(Accel 리드) 조달. 기업 대상 노코드 음성 에이전트 플랫폼. 누적 조달 $30M. | [[G-23]](#ref-g-23) |

---

## 시장 시그널

- LiveKit Series C $100M(밸류에이션 $1B) 완료(2026-01-22). OpenAI·Tesla·Salesforce Agentforce가 핵심 고객으로 실시간 음성 AI 인프라 수요를 방증한다. [[G-16]](#ref-g-16)
- ElevenLabs $500M Series D($11B 밸류에이션) 조달로 누적 조달액 규모화. 경쟁사 대비 압도적 밸류에이션 격차가 형성됐다. [[G-14]](#ref-g-14)
- Synthflow AI $20M Series A(Accel 리드), Beside $20M Series A(EQT Ventures 리드)가 1월 내 동시 클로즈됐다. 기업용 음성 에이전트 분야로 투자 흐름이 집중되는 신호다. [[G-23]](#ref-g-23)
- Deepgram Series C $130M, Decagon Series D $250M도 동기간 조달 완료. Voice AI 전반에 대형 라운드가 집중된 1~2월이었다. [[G-24]](#ref-g-24)
- Meta의 PlayAI 인수(2025-07)로 독립 음성 클로닝 플랫폼 하나가 시장에서 소멸. 빅테크의 스타트업 흡수가 독립 공급사 생태계를 압박하고 있다. [[G-18]](#ref-g-18)
- Pindrop–Zoom 통합으로 엔터프라이즈 접촉 센터 내 탐지 기술 상용화가 가속화됐다. 탐지 시장이 독립 플레이어(Pindrop)와 플랫폼 번들 모델로 분기되는 중이다. [[G-08]](#ref-g-08)
- 한국: SKT·Naver가 주권 AI 프로그램에서 격차를 보이며, 글로벌 음성 AI 플레이어 대비 독자 클로닝 기술 공시가 부재하다. 통신사 자체 음성 AI 역량 구축 또는 글로벌 API 의존 선택이 임박했다. [[G-21]](#ref-g-21)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead (PMC, 2026) | 탐지 시스템의 실세계 일반화 실패 진단, 통신 채널 노이즈 반영 가이드라인으로 57% 정확도 향상 가능 | [[P-01]](#ref-p-01) |
| Targeted Speaker Poisoning Framework in Zero-Shot TTS (Trachu et al., 2026) | SGSP 프레임워크 제안 — EGP+triplet-loss로 15명까지 특정 화자 생성 차단, 100명+ 한계 확인 | [[P-02]](#ref-p-02) |
| Warning: Humans Cannot Reliably Detect Speech Deepfakes (Kawa et al., PMC 2023, 2026 재확인) | 인간의 딥페이크 음성 탐지 정확도 54%, 사전 훈련으로도 개선 미미 | [[P-03]](#ref-p-03) |
| AudioFakeNet: Reliable Speaker Verification in Deepfake Audio (MDPI Algorithms, 2025) | 딥페이크 탐지와 포렌식 화자 인증을 통합하는 모델, 법과학적 활용 기반 제시 | [[P-04]](#ref-p-04) |
| High Fidelity Zero Shot Speaker Adaptation via Denoising Diffusion GAN (Nature Scientific Reports, 2025) | 노이즈 강인성 제로샷 화자 적응에 Denoising Diffusion GAN 적용, WER·화자 유사도 SOTA | [[P-05]](#ref-p-05) |

---

## 전략적 시사점

**기회**

- **탐지 인프라 선제 구축**: Pindrop–Zoom 통합 사례처럼 통신사 접촉 센터(고객 서비스, 인증 IVR)에 실시간 딥페이크 탐지를 번들링하면 규제 압박(EU AI Act 8월)을 조기 선점할 수 있다. 탐지 정확도 99% 주장 솔루션과 통신 트래픽 분석 역량을 결합한 차별화가 가능하다.
- **동의 기반 음성 라이선스 B2B 플랫폼**: ElevenLabs Iconic Marketplace 모델처럼, 통신사가 보유한 콘텐츠 파트너(방송·미디어·연예)와 연계해 한국어 음성 라이선스 마켓플레이스를 구축할 수 있다. EU AI Act 투명성 요건을 충족하는 구조로 설계하면 규제 리스크 헤지도 된다.
- **음성 에이전트 인프라 투자**: LiveKit($1B 유니콘) 사례가 보여주듯, 실시간 음성 AI 인프라가 독립 유니콘을 만들어내는 시장이 됐다. 통신사의 실시간 통신 자산(RTP, WebRTC, 저지연 네트워크)은 음성 에이전트 인프라와 시너지가 크다.
- **한국어 특화 클로닝 API**: 글로벌 플레이어들이 80개 로케일을 커버하지만, 한국어 TTS 품질·방언·비즈니스 도메인 적합성에서 여전히 격차가 있다. SKT A.X 기반 한국어 음성 클로닝 API를 B2B 서비스로 제공하는 기회가 존재한다.

**위협**

- **구별 불가능 임계점 돌파로 음성 인증 신뢰 붕괴**: 음성 기반 본인 확인(ARS 인증, 콜센터 ID 검증)이 클로닝 공격에 취약해졌다. 단일 음성 인증 솔루션만으로는 Gartner 예측대로 2026년 기업 신뢰도 저하가 불가피하다.
- **EU AI Act 8월 시행 컴플라이언스 부담**: 합성 음성 콘텐츠 레이블링·워터마킹 의무를 위반하면 전 세계 매출의 7% 과징금 리스크가 현실화된다. 국내 통신사가 유럽 시장 진출 또는 EU 고객 대상 서비스를 운영하는 경우 즉각 대응이 필요하다.
- **빅테크 M&A로 독립 공급사 생태계 압박**: Meta의 PlayAI 인수처럼 유망 음성 클로닝 스타트업이 빅테크에 흡수되면 독립 API 공급사 선택지가 좁아진다. 파트너십 의존 전략은 단기간에 공급망 리스크로 전환될 수 있다.
- **사기 인프라의 무기화**: UN·INTERPOL 보고대로 음성 클로닝이 사이버범죄 서비스(CaaS)로 표준화됐다. AI 주도 사기 1,210% 급증은 통신사 네트워크를 통한 보이싱(vishing) 공격 급증으로 직결되며, 브랜드 신뢰도 훼손 및 고객 피해 배상 리스크를 수반한다.
- **탐지 기술의 일반화 실패**: 실험실 정확도 높은 탐지 모델이 실제 통화 채널에서 성능이 급락한다는 학술 증거가 누적됐다. 탐지 솔루션 도입 시 통신 채널 시뮬레이션 기반 검증이 필수적이나, 업계 표준이 부재한 상황이다.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Fortune — Voice cloning has crossed the 'indistinguishable threshold' | [링크](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/) | news | 2025-12-27 | [B] |
| <a id="ref-g-02"></a>G-02 | University at Buffalo — Deepfakes leveled up in 2025: Here's what's coming next | [링크](https://www.buffalo.edu/home/story-repository.host.html/content/shared/university/news/ub-reporter-articles/stories/2026/01/lyu-conversation-deep-fakes-2026.detail.html) | news | 2026-01 | [B] |
| <a id="ref-g-03"></a>G-03 | ElevenLabs — Eleven v3: Most Expressive AI TTS Model Launched | [링크](https://elevenlabs.io/blog/eleven-v3) | blog | 2026-02 | [A] |
| <a id="ref-g-04"></a>G-04 | UnifiedTTS — ElevenLabs eleven_v3 Flagship Model Released: 70+ Languages | [링크](http://unifiedtts.com/en/news/2026-02-12-elevenlabs-v3-model) | news | 2026-02-12 | [B] |
| <a id="ref-g-05"></a>G-05 | OpenAI — Introducing gpt-realtime and Realtime API updates for production voice agents | [링크](https://openai.com/index/introducing-gpt-realtime/) | blog | 2026 | [A] |
| <a id="ref-g-06"></a>G-06 | Google Blog — Gemini 2.5 Text-to-Speech model updates | [링크](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-2-5-text-to-speech/) | blog | 2025-12 | [A] |
| <a id="ref-g-07"></a>G-07 | WinBuzzer — Google Tests Voice Cloning With Google Gemini | [링크](https://winbuzzer.com/2026/01/30/google-tests-voice-cloning-ai-studio-gemini-xcxwbn/) | news | 2026-01-30 | [B] |
| <a id="ref-g-08"></a>G-08 | Globe Newswire — Pindrop Zoom Integration Embeds Real-Time Deepfake Detection | [링크](https://www.globenewswire.com/news-release/2026/03/12/3254709/0/en/Pindrop-Zoom-Integration-Embeds-Real-Time-Deepfake-Detection-and-Identity-Verification-in-Zoom-Contact-Center.html) | news | 2026-03-12 | [A] |
| <a id="ref-g-09"></a>G-09 | Pindrop — Detect Deepfake Audio with Pindrop Pulse | [링크](https://www.pindrop.com/product/pindrop-pulse/) | blog | 2026 | [B] |
| <a id="ref-g-10"></a>G-10 | UN News — Deepfakes, voice cloning and weaponised AI: Global wake-up call to organised fraud | [링크](https://news.un.org/en/story/2026/03/1167144) | news | 2026-03 | [A] |
| <a id="ref-g-11"></a>G-11 | RIT Cyber Self-Defense — The Rise of AI Voice Cloning Scams | [링크](https://ritcyberselfdefense.wordpress.com/2026/03/22/the-rise-of-ai-voice-cloning-scams-a-new-frontier-in-consumer-protection/) | blog | 2026-03-22 | [C] |
| <a id="ref-g-12"></a>G-12 | AI Tribune — AI Voice Cloning Regulation in 2026: What's Legal, What's Risky | [링크](https://aitribune.net/2026/02/24/ai-voice-cloning-regulation-in-2026/) | blog | 2026-02-24 | [B] |
| <a id="ref-g-13"></a>G-13 | EU Digital Strategy — Commission launches work on code of practice on marking AI-generated content | [링크](https://digital-strategy.ec.europa.eu/en/news/commission-launches-work-code-practice-marking-and-labelling-ai-generated-content) | news | 2026 | [A] |
| <a id="ref-g-14"></a>G-14 | Newcomer — Investors Go Hard for Voice AI With a String of Big January Deals | [링크](https://www.newcomer.co/p/investors-go-hard-for-voice-ai-with) | news | 2026-01 | [B] |
| <a id="ref-g-15"></a>G-15 | TechCrunch — OpenAI bets big on audio as Silicon Valley declares war on screens | [링크](https://techcrunch.com/2026/01/01/openai-bets-big-on-audio-as-silicon-valley-declares-war-on-screens/) | news | 2026-01-01 | [B] |
| <a id="ref-g-16"></a>G-16 | TechCrunch — Voice AI engine and OpenAI partner LiveKit hits $1B valuation | [링크](https://techcrunch.com/2026/01/22/voice-ai-engine-and-openai-partner-livekit-hits-1b-valuation/) | news | 2026-01-22 | [B] |
| <a id="ref-g-17"></a>G-17 | SiliconANGLE — LiveKit raises $100M at $1B valuation to scale real-time AI and media platform | [링크](https://siliconangle.com/2026/01/22/livekit-raises-100m-1b-valuation-scale-real-time-ai-media-platform/) | news | 2026-01-22 | [B] |
| <a id="ref-g-18"></a>G-18 | TechCrunch — Meta acquires voice startup Play AI | [링크](https://techcrunch.com/2025/07/13/meta-acquires-voice-startup-play-ai/) | news | 2025-07-13 | [B] |
| <a id="ref-g-19"></a>G-19 | Bloomberg — Meta Acquires Voice AI Startup PlayAI, Continuing to Add Talent | [링크](https://www.bloomberg.com/news/articles/2025-07-11/meta-acquires-voice-ai-startup-playai-continuing-to-add-talent) | news | 2025-07-11 | [B] |
| <a id="ref-g-20"></a>G-20 | Resemble AI — Best Open Source AI Voice Cloning Tools in 2026 | [링크](https://www.resemble.ai/best-open-source-ai-voice-cloning-tools/) | blog | 2026 | [C] |
| <a id="ref-g-21"></a>G-21 | Korea Herald — LG, SKT, Upstage advance in Korea's sovereign AI project | [링크](https://www.koreaherald.com/article/10656367) | news | 2026-01 | [B] |
| <a id="ref-g-22"></a>G-22 | The Investor — LG, SKT, Upstage advance; Naver, NC dropped in 1st round | [링크](https://m.theinvestor.co.kr/article/10656530) | news | 2026-01 | [B] |
| <a id="ref-g-23"></a>G-23 | Tech Funding News — Enterprise voice AI startup Synthflow raises $20M | [링크](https://techfundingnews.com/enterprise-voice-ai-synthflow-raises-20m-series-a/) | news | 2026-01 | [B] |
| <a id="ref-g-24"></a>G-24 | Tracxn — Artificial Intelligence in Voice AI: 2026 Market & Investment Trends | [링크](https://tracxn.com/d/artificial-intelligence/ai-startups-in-voice-ai/__s7thq7EI12tPI5Mmcnok_quhhCDTJRpxZqAJ5VexoGc) | blog | 2026 | [C] |
| <a id="ref-e-01"></a>E-01 | OpenAI — Updates for developers building with voice | [링크](https://developers.openai.com/blog/updates-audio-models/) | IR/발표 | 2026 | [A] |
| <a id="ref-e-02"></a>E-02 | Google Cloud Docs — Gemini-TTS release notes | [링크](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts) | IR/발표 | 2026 | [A] |
| <a id="ref-p-01"></a>P-01 | PMC — Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/) | paper | 2026 | [A] |
| <a id="ref-p-02"></a>P-02 | Trachu et al. — Targeted Speaker Poisoning Framework in Zero-Shot Text-to-Speech (arXiv:2603.07551) | [링크](https://arxiv.org/abs/2603.07551) | paper | 2026-03-08 | [A] |
| <a id="ref-p-03"></a>P-03 | Kawa et al. — Warning: Humans cannot reliably detect speech deepfakes (PMC) | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC10395974/) | paper | 2023 | [A] |
| <a id="ref-p-04"></a>P-04 | MDPI Algorithms — AudioFakeNet: A Model for Reliable Speaker Verification in Deepfake Audio | [링크](https://www.mdpi.com/1999-4893/18/11/716) | paper | 2025 | [A] |
| <a id="ref-p-05"></a>P-05 | Nature Scientific Reports — High fidelity zero shot speaker adaptation via denoising diffusion GAN | [링크](https://www.nature.com/articles/s41598-025-90507-0) | paper | 2025 | [A] |
