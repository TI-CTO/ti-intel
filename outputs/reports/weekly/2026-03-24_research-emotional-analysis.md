---
type: weekly-deep-research
topic: emotional-analysis
date: 2026-03-24
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch]
parent: 2026-03-24_weekly-voice-ai.md
---

# Deep 리서치: Emotional Analysis (2026-W13)

## 이전 대비 변화

- **전주 (W12, 2026-03-17):** Foundation Model의 zero-shot 음성 감정 인식(Speech Emotion Recognition, SER) 능력이 Nature npj AI 논문으로 학술 공식화. MME-Emotion ICLR 2026 채택 — 최고 모델(Gemini-2.5-Pro) 39.3%라는 구조적 한계 수치 공개. Hume AI Empathic Voice Interface (EVI) 3 출시. SKT 멘탈비전(MentAl VISION) 사내 서비스 확인.
- **금주 (W13, 2026-03-24):** Hume AI Octave 2 다국어 감정 텍스트 음성 합성(Text-to-Speech, TTS) 출시(2025-10 출시, 이번 주 확인) — 11개 언어 지원·200ms 레이턴시·Octave 1 대비 50% 가격 인하. ElevenLabs Japan, 고객 괴롭힘(customer harassment) 대응 감정 표현 AI 보이스 솔루션 일본 시장 출시. VoxEmo 벤치마크(2026-03-09 arxiv) — 15개 언어·35개 감정 코퍼스 기반 Speech LLM SER 평가 체계 등장. EU AI 법(AI Act) 직장 내 감정 인식 금지 조항 2025-02 발효로 규제 리스크 가시화.
- **변화 방향:** "학술 벤치마크 정비 → 상용 제품 출시 가속"으로 전환. 특히 다국어·저지연 감정 표현 TTS 경쟁이 본격화되며 텔레콤 고객센터 응용이 즉각적인 전략 대상으로 부상. 동시에 EU AI Act 준수 리스크가 기업 도입 방어 요인으로 등장.

---

## 기술 동향

1. **Hume AI Octave 2 — 다국어 감정 표현 TTS, 200ms 레이턴시 달성.**
   Hume AI가 2025년 10월 출시한 Octave 2는 11개 언어(아랍어·영어·프랑스어·독일어·힌디어·이탈리아어·일본어·한국어·포르투갈어·러시아어·스페인어)를 지원하는 차세대 감정 표현 TTS 모델이다. 핵심 개선: Octave 1 대비 40% 속도 향상(200ms 이하 레이턴시), 가격 50% 인하(분당 1센트 이하 전용 배포 가능). 스크립트의 감정 맥락을 자율적으로 이해해 "겁에 질린 목소리로 속삭이기" "빈정거리는 톤" 등 상황별 음성 표현을 다국어에서 동일하게 구현한다. 추가 예정 기능: voice conversion(한 목소리를 다른 목소리로 변환하되 음소 특성 보존), phoneme 직접 편집. [[G-01]](#ref-g-01) [[E-01]](#ref-e-01)

2. **ElevenLabs Japan — 고객 괴롭힘 대응 감정 AI 보이스 솔루션 출시.**
   ElevenLabs Japan LLC가 일본 고객 서비스 시장의 'customer harassment'(카스하라) 문제 해결을 목적으로 감정 표현 AI 보이스 솔루션을 출시했다. AI 보이스가 1차 응대 "방파제" 역할을 담당해 인간 상담원을 언어폭력으로부터 보호하는 구조다. 핵심 기능: 아무리 거친 말을 들어도 지치지 않으며, 인간적 온기와 공감의 억양을 유지하면서 고객 발언을 분석·요약. 일본 특유의 장기 근무자 정신건강 문제와 AI의 감정 표현 능력을 결합한 응용 사례로, 통신사 고객센터 전환 참고 모델이 된다. [[G-02]](#ref-g-02) [[G-03]](#ref-g-03)

3. **VoxEmo — Speech LLM 기반 다국어 SER 벤치마크 발표(2026-03-09).**
   USC·셰필드대 공동 연구(Zhang, Chou, Narayanan, Hain)가 arxiv에 VoxEmo를 발표했다. 15개 언어·35개 감정 데이터셋을 아우르는 Speech LLM SER 종합 평가 프레임워크로, 단순 분류부터 언어학적 추론까지 다양한 프롬프트 복잡도를 표준화했다. 핵심 발견: zero-shot Speech LLM은 하드 레이블 정확도(단일 정답)에서 지도학습 모델에 뒤지지만, "인간의 주관적 감정 분포"와 일치성이 더 높다 — 즉 감정의 모호성·복잡성을 더 잘 반영한다. W12에 확인된 MME-Emotion(다중 모달)과 함께 평가 인프라가 빠르게 정비되고 있음을 보여준다. [[P-01]](#ref-p-01)

4. **EU AI Act 직장 내 감정 인식 금지 — 2025년 2월 발효, 기업 규제 리스크 현재화.**
   EU 인공지능 법(EU AI Act) Article 5가 2025년 2월 2일 발효되면서 직장 및 교육기관에서의 감정 인식 AI 사용이 명시적으로 금지됐다. 위반 시 최대 3,500만 유로 또는 연간 글로벌 매출의 7% 벌금이 부과된다(높은 금액 적용). 일리노이주 심리자원 복지법(Wellness and Oversight for Psychological Resources Act, 2025-08 발효)도 무허가 AI의 심리치료 제공 및 인간 검토 없는 감정 탐지를 제한한다. 한국 시장은 직접 적용 대상 아니나, 글로벌 B2B 고객사 대상 서비스 수출 시 컴플라이언스 고려가 필수. [[G-04]](#ref-g-04) [[G-05]](#ref-g-05)

5. **멀티모달 감정 인식 시장 — 2026~2035 CAGR 15.5%, 2030년 144억 달러 전망.**
   시장조사기관 Coherent Market Insights는 감정 AI 시장 규모를 2025년 19.5억 달러에서 2026년 41.5억 달러, 2034년 207.7억 달러로 전망한다(CAGR 22.29%). 멀티모달 감정 AI 세그먼트는 2026~2035년 CAGR 15.5%로 2030년 144.1억 달러 규모 예상. 음성 기반 세그먼트는 CAGR 37.1%로 세그먼트 내 최고 성장률을 보인다. 단, 시장 추정치는 조사기관마다 상이하므로 교차 검증 필요. [[G-06]](#ref-g-06) [[G-07]](#ref-g-07)

6. **Microsoft DragonHD — 감정 맥락 자동 감지·실시간 톤 조정 신규 신경망 음성 모델.**
   Microsoft Azure는 DragonHDLatestNeural 및 DragonHDOmniLatestNeural을 출시했다. 핵심 기능: 음성의 의미적 내용을 이해하고 감정적 단서를 자동 탐지해 말하는 스타일·톤을 실시간으로 맥락에 맞게 조정한다. 별도 감정 태그나 SSML 마크업 없이 텍스트 내용만으로 감정 톤을 추론하는 방식으로, 엔터프라이즈 고객센터 자동화에 직접 적용 가능. Google Chirp 3(고정밀 다국어 자동음성인식(Automatic Speech Recognition, ASR) 모델)과 함께 대형 클라우드의 감정 인식 내재화 흐름을 보여준다. [[G-08]](#ref-g-08) [[G-09]](#ref-g-09)

7. **ACII 2026 — 감정 컴퓨팅·지능 상호작용 국제 학회 일정 공개.**
   제14회 국제 감정 컴퓨팅·지능 상호작용 학술대회(Affective Computing and Intelligent Interaction 2026, ACII 2026)가 2026년 9월 7~10일 멕시코 푸에블라에서 개최된다. 이번 대회 주제는 "다문화 감정 컴퓨팅(multicultural affective computing)"으로, 문화 간 감정 AI 적용 방법론에 초점. 논문 등록 마감 2026년 8월 18일. 채택 논문은 IEEE Xplore 수록 및 IEEE Transactions on Affective Computing 확장판 투고 초청. [[G-10]](#ref-g-10)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Hume AI | Octave 2 출시: 11개 언어, 200ms 레이턴시, Octave 1 대비 50% 가격 인하. 분당 1센트 이하 전용 배포 가능. Voice conversion·phoneme 편집 기능 예고. EVI 3: 200K+ 목소리 커스터마이제이션, 300ms 이하 응답. GPT-4o 대비 공감·표현성·자연스러움에서 우위(블라인드 평가) | [[G-01]](#ref-g-01) [[E-01]](#ref-e-01) [[E-02]](#ref-e-02) |
| ElevenLabs | Japan LLC가 customer harassment 대응 감정 AI 보이스 솔루션 출시. 연중무휴 공감 대응, 상담원 보호 "방파제" 역할. 음성 에이전트 플랫폼 2026 개발자 트렌드 리포트 발표(음성 에이전트 채택 가속화) | [[G-02]](#ref-g-02) [[G-03]](#ref-g-03) |
| Microsoft | DragonHDLatestNeural·DragonHDOmniLatestNeural 출시: 감정 단서 자동 탐지, 실시간 톤 조정. Video Indexer: 텍스트+음성 톤 결합 4가지 감정 상태 탐지. Azure AI Language 감성 분석. Uniphore를 2026 Gartner Magic Quadrant 고객 데이터 플랫폼 리더로 인정 | [[G-08]](#ref-g-08) [[G-09]](#ref-g-09) |
| Google | Chirp 3 다국어 ASR 모델 출시(고정밀·고속). Gemini-2.5-Pro는 MME-Emotion 벤치마크에서 최고 39.3%·CoT 56.0%. 음성 에이전트가 Google Workspace에 내재화 진행 중 | [[G-09]](#ref-g-09) [[G-11]](#ref-g-11) |
| Deepgram | Voice Agent API: 300ms 이하 레이턴시 실시간 전사·감성 분석. 토큰 기반 과금($0.0003/1k input). 감정 탐지보다 실시간 음성 인프라 포지셔닝 | [[G-12]](#ref-g-12) |
| AssemblyAI | Audio Intelligence: 발화 문장별 긍·부정·중립 감성 분석 + 신뢰도 점수 제공. 기업 고객 감성 분석·개인식별정보(PII) 필터링 특화. 실시간 트랜스크립션 경쟁보다 "음성 이해" 포지셔닝 | [[G-12]](#ref-g-12) |
| Uniphore | 2026 Gartner Magic Quadrant 고객 데이터 플랫폼 리더 선정. Business AI Suite: 얼굴 표정·음성 톤·감성 분석 결합 실시간 감정 지능. 2025-06 Business AI Cloud 출시(에이전트형 AI). $610M 누적 투자 | [[E-03]](#ref-e-03) [[G-13]](#ref-g-13) |
| SKT | 멘탈비전(음성+얼굴 → 불안·우울 분석) 사내 운영 중. 보컬비전(VocAl VISION) 식약처 의료기기 허가 취득 — 후두질환·성대결절·후두암·연축성발성장애 음성 진단. 2026년 외부 서비스 확장 준비 | [[E-04]](#ref-e-04) [[G-14]](#ref-g-14) |
| KT | AI 보이스 스튜디오: 인간 수준 감정 표현 AI 음성. Rangtok AI 통화 리포트: 통화 결과 감정 분석·전사·요약·키워드 정리. AICC(AI Contact Center) 'A.sen Cloud'에 보이스봇 감정 응대 내재화 | [[G-15]](#ref-g-15) [[E-05]](#ref-e-05) |

---

## 시장 시그널

- **감정 AI 시장 규모(교차 검증 2건):** Coherent Market Insights는 2026년 41.5억 달러 → 2034년 207.7억 달러(CAGR 22.29%)로 추정 [[G-07]](#ref-g-07). Fortune Business Insights는 2025년 34억 달러 → 2034년 207.7억 달러(CAGR 22.29%)로 추정 [[G-16]](#ref-g-16). 두 소스 모두 CAGR 22%+ 일치하여 고신뢰도 방향성 확인.
- **음성 감정 분석 세그먼트:** 전체 어펙티브 컴퓨팅 시장 내 음성 인식 세그먼트 CAGR 37.1% — 세그먼트 최고 성장률. 실시간 고객 서비스·헬스케어 수요 집중 [[G-06]](#ref-g-06).
- **멀티모달 세그먼트:** 멀티모달 어펙티브 컴퓨팅 시장 2026~2035년 CAGR 15.5%, 2030년 144.1억 달러 전망 [[G-07]](#ref-g-07). 클라우드 기반 감정 분석 플랫폼 수요가 주요 성장 동력.
- **엔터프라이즈 투자 집중:** Uniphore $610M 누적 투자, 연간 반복 매출(Annual Recurring Revenue, ARR) $100M 이상으로 B2B 감정 AI 선두. 2026년 3월 미국 스타트업 투자 전반이 소폭 둔화됐으나 AI 분야는 지속 [[G-17]](#ref-g-17).
- **일본 시장 개척:** ElevenLabs Japan의 customer harassment 솔루션은 감정 AI 비즈니스 모델의 새 패턴 — "상담원 보호"를 전면에 내세운 B2B SaaS. 아시아 통신사 고객센터 전환 선례.
- **Kopernica(Neurologyca, 스페인):** 790개 신체 포인트 추적 + 음성 톤 + 행동 패턴 결합, 90개 감정 상태 식별. 2025년 5월 출시, 엣지 AI 멀티모달 감정 OS(운영 체제) 방향성 제시 [[G-18]](#ref-g-18).
- **WHO 정신건강 AI 성명(2026-03-20):** WHO(세계보건기구)가 "책임 있는 정신건강 AI" 전문가 로드맵을 발표 — 감정 AI 헬스케어 응용의 임상 근거 기준과 윤리 가이드라인 요구 [[G-19]](#ref-g-19).

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| VoxEmo: Benchmarking SER with Speech LLMs (Zhang et al., 2026) | 15개 언어·35개 데이터셋 Speech LLM SER 벤치마크. zero-shot 모델이 하드 레이블 정확도는 낮지만 인간 주관 분포와 일치성 더 높음 | [[P-01]](#ref-p-01) |
| Pioneering Multimodal Emotion Recognition: Closed Sets to Open Vocabularies (2025-12) | 개방형 어휘(Open-Vocabulary) 멀티모달 감정 인식(MER-OV) 최초 체계적 연구. 2단계(모달별 감정 단서 추출 → 융합 추론) 방법론, 오디오·비디오·텍스트 삼중 융합이 최적 | [[P-02]](#ref-p-02) |
| Speech Emotion Recognition Using Multimodal LLMs (Sciencedirect, 2025) | 이베리아어권 저자원 환경에서 멀티모달 LLM + 감정 TTS 데이터 증강으로 SER 성능 향상. 합성 데이터의 실제 데이터 대체 가능성 실증 | [[P-03]](#ref-p-03) |
| Multimodal Emotion Recognition in Conversations: A Survey (2025-05) | 텍스트·음성·영상 융합 대화 감정 인식(MERC) 방법론·트렌드·한계 종합 리뷰. 인간-컴퓨터 인터랙션 자연성 향상을 위한 MERC 연구 방향 제시 | [[P-04]](#ref-p-04) |
| EmoNet-Voice: Fine-Grained Expert-Verified Benchmark (2025) | 40개 세분 감정 카테고리·11개 목소리·4개 언어·5,000시간 전처리 데이터셋. EmoDB·RAVDESS에서 강한 일반화 성능 확인 | [[P-05]](#ref-p-05) |
| Ethics and Bias in Emotional AI (Frontiers in AI, 2026) | 감정 AI의 편향·고정관념 강화 위험 체계적 분석. 다양성 반영 훈련 데이터 및 감사 체계 필요성 제안 | [[P-06]](#ref-p-06) |

---

## 전략적 시사점

**기회**

- **저지연 감정 TTS 내재화:** Octave 2가 200ms·11개 언어·저가격 API를 제공함에 따라, 한국어 포함 아시아 언어 감정 표현 음성 생성 비용이 급감. 통신사 AICC(AI Contact Center)에 감정 TTS를 API 방식으로 빠르게 내재화하는 전략이 현실적 옵션이 됨.
- **일본 고객 괴롭힘 모델의 국내 복제:** ElevenLabs Japan의 customer harassment 솔루션은 국내 고객센터 과로·정신건강 문제와 직결되는 응용 모델. 상담원 보호 + 운영 효율 이중 가치 제안이 가능하며, SKT·KT 모두 자사 AICC에 즉각 적용 가능한 시나리오.
- **VoxEmo·MME-Emotion 기반 내부 벤치마크 구축:** 국내 감정 AI 서비스 품질을 글로벌 기준으로 측정할 수 있는 평가 인프라가 공개됐다. 한국어 감정 데이터셋이 VoxEmo에 포함될 경우 국내 기술 수준을 객관적으로 비교할 수 있음.
- **헬스케어 음성 바이오마커:** SKT 보컬비전의 식약처 허가 사례는 텔레콤 기업이 의료기기 인허가 경로로 진입 가능함을 실증. 정신건강(멘탈비전)→ 외부 서비스 확장 시 B2C·B2B 헬스케어 SaaS 진입 기회.

**위협**

- **EU AI Act 직장 내 감정 인식 금지:** 유럽 고객사 대상 서비스 수출이나 글로벌 기업에 납품 시 컴플라이언스 위험. Article 5가 2025년 2월 발효됐으며, 국내 규제도 유사 방향으로 수렴할 가능성이 있어 제품 설계 단계부터 "감정 추론 vs. 감성 분석" 구분이 필요.
- **Big Tech의 감정 AI 내재화:** Microsoft DragonHD, Google Chirp 3 + Gemini 통합, Amazon Alexa+ 등 클라우드 3사가 감정 인식·감정 표현 TTS를 기존 음성 API에 통합하고 있음. 독립 감정 AI 솔루션의 차별화 공간이 좁아지는 구조적 압력.
- **LLM 감정 지능의 구조적 한계:** MME-Emotion에서 최고 모델도 39.3%에 불과 — 현재 LLM 기반 감정 인식은 실제 복잡한 맥락에서 여전히 낮은 신뢰도. 이를 인지하지 않고 감정 AI 서비스를 운영하면 오인식 사고(false emotion detection) 위험.
- **한국어 감정 데이터 부족:** VoxEmo에 한국어가 포함됐으나, 감정 어노테이션된 한국어 음성 코퍼스의 절대적 규모는 여전히 부족. Foundation Model 기반 접근도 한국어 감정 표현 다양성을 충분히 반영하지 못할 가능성.

---

## 신뢰도 평가

- **높은 확신 [A/B]:** Hume AI Octave 2 출시 세부 사항(공식 블로그 [A]), ElevenLabs Japan customer harassment 솔루션(공식 보도 [B]), VoxEmo 논문 arxiv 제출(학술 [A]), EU AI Act Article 5 발효(공식 [A]), SKT 보컬비전 식약처 허가(공식 보도 [B]).
- **추가 검증 필요 [C/D]:** 시장 규모 수치(리서치사별 상이, 교차 검증 완료되나 예측 불확실성 내재 [C]). Microsoft DragonHD 출시 구체적 날짜 미확인 [C]. Naver·Kakao 감정 AI 구체 서비스 정보 부재 — 에이전트 AI에 집중, 감정 분석 독립 서비스 부재 확인 [C].
- **데이터 공백:** AssemblyAI·Deepgram의 2026년 3월 기준 신규 기능 공식 발표 없음. Amazon의 2026년 감정 AI 신규 발표 없음. KT Rangtok 감정 분석 서비스 상세 스펙 공개 정보 없음.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Hume AI — Octave 2: Next-Generation Multilingual Voice AI | [링크](https://www.hume.ai/blog/octave-2-launch) | news | 2025-10-01 | [A] |
| <a id="ref-g-02"></a>G-02 | IT Business Today — ElevenLabs Promotes AI Voice Agent for Customer Service | [링크](https://itbusinesstoday.com/martech/customer-experience/elevenlabs-promotes-ai-voice-agent-for-customer-service/) | news | 2026-03 | [B] |
| <a id="ref-g-03"></a>G-03 | ElevenLabs — AI Customer Support & Help Desk Solutions | [링크](https://elevenlabs.io/customer-service) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | Wolters Kluwer — Prohibition of AI Emotion Recognition in Workplace under the AI Act | [링크](https://legalblogs.wolterskluwer.com/global-workplace-law-and-policy/the-prohibition-of-ai-emotion-recognition-technologies-in-the-workplace-under-the-ai-act/) | news | 2025-02 | [A] |
| <a id="ref-g-05"></a>G-05 | EU AI Act — Article 5: Prohibited AI Practices | [링크](https://artificialintelligenceact.eu/article/5/) | news | 2025-02 | [A] |
| <a id="ref-g-06"></a>G-06 | ReportsandData — Affective Computing Market 2016-2026 | [링크](https://www.reportsanddata.com/report-detail/affective-computing-market) | news | 2026 | [C] |
| <a id="ref-g-07"></a>G-07 | WhatechMarkets — Multimodal Affective Computing Market Outlook 2026-2035 | [링크](https://whatech.com/og/markets-research/it/1012381-multimodal-affective-computing-market-outlook-2026-2035-key-trends-shaping-the-next-decade-of-growth.html) | news | 2026 | [C] |
| <a id="ref-g-08"></a>G-08 | Microsoft Learn — Language and Voice Support for Azure Speech | [링크](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support) | news | 2026 | [A] |
| <a id="ref-g-09"></a>G-09 | Skywork AI — The Complete 2026 Guide to Google's Voice AI Ecosystem | [링크](https://skywork.ai/skypage/en/google-voice-ai-ecosystem/2027618525524463616) | news | 2026 | [C] |
| <a id="ref-g-10"></a>G-10 | ACII 2026 — 14th International Conference on Affective Computing and Intelligent Interaction | [링크](https://acii-conf.net/) | news | 2026 | [A] |
| <a id="ref-g-11"></a>G-11 | Parloa — The 5 Voice AI Trends That Will Define 2026 | [링크](https://www.parloa.com/blog/ai-trends-2026/) | news | 2026 | [B] |
| <a id="ref-g-12"></a>G-12 | Gladia — AssemblyAI vs Deepgram: Best Speech-to-Text API 2026 | [링크](https://www.gladia.io/blog/assemblyai-vs-deepgram) | news | 2026 | [B] |
| <a id="ref-g-13"></a>G-13 | Uniphore — Emotion AI | [링크](https://www.uniphore.com/emotion-ai/) | news | 2026 | [B] |
| <a id="ref-g-14"></a>G-14 | SKT 뉴스룸 — SKT, '멘탈비전' AI 기술로 마음건강 지킨다 | [링크](https://news.sktelecom.com/214844) | news | 2025-09 | [A] |
| <a id="ref-g-15"></a>G-15 | 전자신문 — KT, 사람 감정 표현하는 'AI 보이스 스튜디오' 출시 | [링크](https://www.etnews.com/20220719000108) | news | 2022-07 | [B] |
| <a id="ref-g-16"></a>G-16 | Fortune Business Insights — Emotion AI Market Share, Size, Trends, Forecast 2034 | [링크](https://www.fortunebusinessinsights.com/emotion-ai-market-112136) | news | 2026 | [C] |
| <a id="ref-g-17"></a>G-17 | Crunchbase News — US Startup Funding Slows Sharply in March | [링크](https://news.crunchbase.com/business/us-startup-funding-slows-march-2026-data/) | news | 2026-03 | [B] |
| <a id="ref-g-18"></a>G-18 | AIMultiple — Affective Computing: In-Depth Guide to Emotion AI in 2026 | [링크](https://research.aimultiple.com/affective-computing/) | news | 2026 | [B] |
| <a id="ref-g-19"></a>G-19 | WHO — Towards Responsible AI for Mental Health and Well-Being | [링크](https://www.who.int/news/item/20-03-2026-towards-responsible-ai-for-mental-health-and-well-being--experts-chart-a-way-forward) | news | 2026-03-20 | [A] |
| <a id="ref-e-01"></a>E-01 | Hume AI — Introducing Octave 2 (공식 블로그) | [링크](https://www.hume.ai/blog/octave-2-launch) | IR/발표 | 2025-10-01 | [A] |
| <a id="ref-e-02"></a>E-02 | Hume AI — Introducing EVI 3: Most Realistic Speech-to-Speech Foundation Model | [링크](https://www.hume.ai/blog/introducing-evi-3) | IR/발표 | 2026-02 | [A] |
| <a id="ref-e-03"></a>E-03 | CMSWire — Tech Giants Back Uniphore's $260M Series F | [링크](https://www.cmswire.com/customer-experience/tech-giants-back-uniphores-260m-series-f-for-enterprise-ai-platform/) | IR/발표 | 2022 | [B] |
| <a id="ref-e-04"></a>E-04 | SKT 뉴스룸 — SKT 에이닷 전화, AI로 통화 중에도 보이스피싱 잡아낸다 | [링크](https://news.sktelecom.com/217274) | IR/발표 | 2026 | [A] |
| <a id="ref-e-05"></a>E-05 | KT 보도자료 — KT AI 보이스봇·챗봇 서비스 | [링크](https://corp.kt.com/html/promote/news/report_detail.html?rows=10&page=1&datNo=18036) | IR/발표 | 2026 | [A] |
| <a id="ref-p-01"></a>P-01 | Zhang et al. — VoxEmo: Benchmarking SER with Speech LLMs | [링크](https://arxiv.org/abs/2603.08936) | paper | 2026-03-09 | [A] |
| <a id="ref-p-02"></a>P-02 | (저자 미상) — Pioneering Multimodal Emotion Recognition: From Closed Sets to Open Vocabularies | [링크](https://arxiv.org/html/2512.20938v1) | paper | 2025-12 | [A] |
| <a id="ref-p-03"></a>P-03 | (저자 미상) — Speech Emotion Recognition Using Multimodal LLMs and TTS Data Augmentation for Iberian Languages | [링크](https://www.sciencedirect.com/science/article/pii/S0885230825001524) | paper | 2025 | [A] |
| <a id="ref-p-04"></a>P-04 | (저자 미상) — Multimodal Emotion Recognition in Conversations: A Survey | [링크](https://arxiv.org/abs/2505.20511) | paper | 2025-05 | [A] |
| <a id="ref-p-05"></a>P-05 | (저자 미상) — EmoNet-Voice: Fine-Grained Expert-Verified Benchmark for Speech Emotion Detection | [링크](https://arxiv.org/abs/2506.09827) | paper | 2025 | [A] |
| <a id="ref-p-06"></a>P-06 | Frontiers in AI — Ethics and Bias in Emotional AI | [링크](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1768696/abstract) | paper | 2026 | [A] |
