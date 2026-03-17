---
type: weekly-research
topic: emotional-analysis
domain: voice-ai
date: 2026-03-17
agent: research-deep
confidence: medium
status: completed
sources_used: [websearch]
---

# Emotional Analysis — Deep 리서치 (W12)

## 이전 대비 변화

- **전주 (W11, 2026-03-11):** Google DeepMind Hume AI acqui-hire (CEO Alan Cowen + 7명) 확인. 마고 CES 2026 7감정 인식 데모. 음성 바이오마커 헬스케어 임상 가속 (파킨슨 98% 정확도). On-device 감정 처리 트렌드. SKT 멘탈케어 MOU.
- **금주 (W12, 2026-03-17):** Foundation Model의 zero-shot 감정 분석 능력이 Nature npj AI 논문으로 학술적 공식화. MME-Emotion이 ICLR 2026 채택 논문으로 확정 — LLM 감정 지능의 체계적 벤치마크 최초 등장. Hume AI가 EVI 3 출시(이전 주 예고됐던 신모델). JMIR 음성 감정-정신건강 체계적 리뷰(85편 → 14편 최종 선정) 발표. SKT 멘탈비전 사내 서비스 출시 확인(2025-09).
- **변화 방향:** "특화 모델 vs. Foundation Model" 경쟁 구도가 핵심 축으로 부상. 정확도 경쟁(90%+)에서 벤치마크 표준화 단계로 이동. 헬스케어 임상 적용이 시범에서 실증으로 진전.

---

## 기술 동향

1. **Foundation Model의 zero-shot 감정 인식 — 학술 공식화.** Nature npj Artificial Intelligence에 게재된 "Affective computing has changed: the foundation model disruption" (Liang et al., 2025)이 이번 주 핵심 시그널이다. 핵심 주장: 감정 특화 어노테이션 데이터 없이 사전학습된 Foundation Model이 zero-shot 프롬프팅만으로 기존 SER SOTA 모델과 경쟁적 성능을 달성한다. SenseVoice-Small(FunAudioLLM, Alibaba)은 파인튜닝 없이 기존 최고 성능 SER 모델을 초과했다. 이는 데이터 수집·어노테이션 비용이 높았던 기존 SER 개발 패러다임을 근본적으로 흔드는 변화다. [[G-01]](#ref-g-01) [[P-01]](#ref-p-01)

2. **MME-Emotion — ICLR 2026 채택, LLM 감정 지능 첫 종합 벤치마크 등장.** FunAudioLLM이 개발한 MME-Emotion이 ICLR 2026 conference paper로 채택됐다. 6,500개 비디오 클립, 27개 시나리오 유형, 8가지 감정 태스크(실험실 감정인식·실세계 감정인식·노이즈 환경·세분화 감정·다중 레이블·감성 분석·의도 인식)로 구성된 최초 종합 벤치마크. **핵심 결과: 최고 성능 모델(Gemini-2.5-Pro)이 인식 점수 39.3%, CoT 점수 56.0%에 불과** — 현존 LLM의 감정 지능에 구조적 한계가 수치로 입증됐다. [[G-08]](#ref-g-08) [[P-02]](#ref-p-02)

3. **멀티모달 LLM 감정 인식 정확도 — 인간 초월 vs. 구조적 한계 공존.** 이중적 시그널이 동시에 나타나고 있다. GPT-4o는 안면 감정 인식에서 86% 정확도(NimStim 데이터셋, Cohen's κ=0.83)로 인간 수준 이상. 음성 기반 멀티모달 감정 인식은 일부 데이터셋에서 96~98% 달성. 그러나 MME-Emotion 야생 환경(ER-Wild) 벤치마크에서 최고 모델도 40% 미만 — 실제 복잡한 감정 맥락에서의 성능 격차가 정량화됐다. [[G-09]](#ref-g-09) [[P-02]](#ref-p-02)

4. **Hume AI EVI 3 출시 — Google acqui-hire 이후 독립 신제품.** Google DeepMind acqui-hire(2026-01) 이후 신임 CEO Andrew Ettinger 체제에서 EVI 3가 출시됐다. 주요 기능: 프롬프트 기반 200K+ 목소리 커스터마이제이션, 30초 오디오로 음색·리듬·성격까지 복제하는 voice cloning, 300ms 이하 응답 레이턴시. Claude 4, Gemini 2.5, Kimi K2 등 주요 LLM과 통합 지원. GPT-4o·Gemini 대비 감정 표현 정확도에서 우위 주장(사용자 평가 기준). [[G-05]](#ref-g-05) [[G-06]](#ref-g-06)

5. **JMIR 음성 감정-정신건강 체계적 리뷰 — 임상 근거 체계화.** JMIR Mental Health에 게재된 첫 SER-정신건강 체계적 리뷰(2025-09)는 3,648편 스크리닝 → 85편 → 14편 최종 선정. 우울·기분장애 연구가 53%로 가장 많고, 자살 위험 18%, 정신증 18%. 핵심 결론: SER이 치료 효과의 객관적 지표로서 임상 평가 보완 도구로서 가능성을 갖지만, 독립 진단 대체는 아직 미달. PHQ-9 수준(0.85 AUC) 달성을 위한 정확도 향상이 선결 과제. [[P-03]](#ref-p-03)

6. **SKT 멘탈비전 사내 서비스 정식 출시 (2025-09).** SKT가 2025년 9월 임직원 대상 '멘탈비전' 서비스를 공식 출시했다. 음성 4문장 낭독 + 얼굴 스캔 → 불안감·우울감 분석 → 맞춤형 건강 프로그램 추천. 별도로 보컬비전(VocAl VISION) 기술은 식약처 의료기기 허가 취득 — 후두질환·성대결절·후두암·연축성발성장애 음성 진단. 2026년 외부 서비스 확장 준비 중. [[G-03]](#ref-g-03) [[E-01]](#ref-e-01)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Google DeepMind | Hume AI CEO Alan Cowen + 7명 라이선싱 딜(2026-01) 이후 Gemini 음성 감정 통합 진행 중. EVI 기술 비독점 라이선스. $74M 투자 유치한 Hume AI는 독립 운영 유지, 2026년 $100M 매출 목표 | [[G-02]](#ref-g-02) [[G-04]](#ref-g-04) |
| Hume AI | Google acqui-hire 후 신임 CEO Andrew Ettinger 체제. EVI 3 출시: 200K+ 목소리 커스터마이제이션, voice cloning, LLM 통합(Claude 4, Gemini 2.5). GPT-4o·Gemini 대비 감정 표현 정확도 우위 주장 | [[G-05]](#ref-g-05) [[G-06]](#ref-g-06) |
| OpenAI | GPT-4o Advanced Voice Mode: 음성 톤·피치·속도에서 감정 인식 및 감정 적응형 응답. 232ms 평균 반응 속도. 안면 감정 인식 GPT-4o 정확도 86%(NimStim 데이터셋, Cohen's κ=0.83). MME-Emotion 벤치마크 상세 점수 미공개 | [[G-07]](#ref-g-07) [[G-09]](#ref-g-09) |
| Alibaba (FunAudioLLM) | SenseVoice-Small: 파인튜닝 없이 기존 SER SOTA 초과 달성. MME-Emotion 벤치마크 개발 및 ICLR 2026 채택. Gemini-2.5-Pro 39.3%라는 한계 수치를 공개 | [[G-01]](#ref-g-01) [[G-08]](#ref-g-08) |
| Microsoft Azure | Azure AI Video Indexer: 텍스트+음성 톤 결합 감정 탐지. Azure AI Language: 감성 분석·오피니언 마이닝. Gartner 예측 인용: 2026년 Conversational AI가 기업 앱에 내재화 전망 | [[G-10]](#ref-g-10) |
| Amazon AWS | Chime SDK 음성 톤 분석 모델(ASR 인코더-디코더 + 음향 특징 하이브리드). Amazon Comprehend 비정형 음성 데이터 감성 분석. 최신 독립 감정 AI 신규 발표 없음 — 기존 서비스 유지 | [[G-11]](#ref-g-11) |
| SKT | 멘탈비전 서비스 2025-09 사내 출시. 보컬비전 식약처 의료기기 허가 취득. 음성+얼굴 멀티모달 → 심리상태 분석 → 외부 서비스 확장 준비 중 | [[E-01]](#ref-e-01) [[G-03]](#ref-g-03) |
| Canary Speech | 음성 바이오마커 기반 MDD 탐지(UAR 0.71), GAD 탐지(UAR 0.66). 2026-02 Intermountain Ventures와 임상 연구 런칭. B2B 헬스케어 SaaS 포지셔닝 | [[G-12]](#ref-g-12) |

---

## 시장 시그널

- **감정 AI 시장 규모 (교차 검증 2건):** Roots Analysis 추정 $5.7B(2023) → $38.5B(2035), CAGR 20.9% [G-13]. MarketsandMarkets 추정 $9.01B(2030), CAGR 21.9% [G-13]. 두 소스 모두 20%+ CAGR 일치.
- **음성 세그먼트 성장:** 음성 기반 감정 분석 세그먼트는 2025~2034년 CAGR 22%+ 전망으로 전체 감정 AI 시장 내 최고 성장 세그먼트.
- **헬스케어 드라이버:** 정신건강 세그먼트 CAGR 23.44%. 치료사 부족(전 세계), 디지털 헬스 채택 가속화, HIPAA 플랫폼 통합 확대가 동시 작용.
- **Foundation Model 패러다임 전환 임박:** 특화 어노테이션 데이터 없이 zero-shot SER 가능 → 데이터 수집·레이블링 스타트업의 진입 장벽 하락. 반면 foundation model 자체 보유 기업(Google, OpenAI, Alibaba)의 경쟁 우위 강화.
- **벤치마크 표준화 시작:** MME-Emotion(ICLR 2026)이 LLM 감정 지능 첫 표준 벤치마크로 등장 — 향후 모델 선택·조달 의사결정에 기준점 제공.
- **ACII 2026 학회:** 9월 7~10일, 멕시코 Puebla. 주제 "Emotions beyond borders: Multicultural Affective Computing". 논문 마감 2026-03-27. IEEE Xplore 게재 확정.
- **Edge AI 수요:** 개발자 42%+가 LLM을 로컬 실행(2026 트렌드) — 프라이버시·레이턴시 이유. 감정 인식 on-device 처리 솔루션 수요 증가 뒷받침.
- **EU AI Act 규제 영향:** 공공 공간 실시간 감정 인식 제한 지속. B2B(콜센터·HR·의료) 및 동의 기반 개인 서비스로 적용 도메인 수렴.

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "Affective computing has changed: the foundation model disruption" (Liang et al. — npj AI, 2025) | Foundation Model이 감정 특화 학습 없이 zero-shot으로 SER SOTA 수준 달성. SenseVoice-Small 파인튜닝 없이 기존 최고 성능 초과. 어노테이션 데이터 패러다임 붕괴 선언. | [[P-01]](#ref-p-01) |
| "MME-Emotion: A Holistic Evaluation Benchmark for Emotional Intelligence in MLLMs" (FunAudioLLM et al. — ICLR 2026) | 6,500 비디오·27 시나리오·8 태스크 종합 벤치마크. Gemini-2.5-Pro 최고 성능 39.3% — 현존 MLLM 감정 지능의 구조적 한계 수치화. | [[P-02]](#ref-p-02) |
| "Speech Emotion Recognition in Mental Health: Systematic Review of Voice-Based Applications" (JMIR Mental Health, 2025-09) | 3,648편 스크리닝 → 14편 최종 선정. 우울·기분장애 53%, 자살 위험 18%, 정신증 18%. SER의 임상 보완 가능성 확인, 독립 진단 대체는 PHQ-9 수준(0.85 AUC) 미달. | [[P-03]](#ref-p-03) |
| "Evaluating general purpose LLMs in identifying human facial emotions" (npj Digital Medicine, 2025) | GPT-4o 86%, Gemini 2.0 84%, Claude 3.5 Sonnet 74% (NimStim 데이터셋 안면 감정 인식). GPT-4o·Gemini는 인간 수준 이상. | [[P-04]](#ref-p-04) |
| "A Comprehensive Review of Multimodal Emotion Recognition: Techniques, Challenges, Future Directions" (PMC, 2025) | 2022년 이후 논문 40%+가 트리모달(AVT) 또는 트랜스포머 크로스모달 퓨전 채택. 생체신호·아이트래킹 결합 연구 급증. | [[P-05]](#ref-p-05) |
| "Digital speech biomarkers can measure acute effects of levodopa in Parkinson's disease" (npj Parkinson's Disease, 2025) | 음성 바이오마커가 레보도파 치료 효과를 객관 측정. 임상 평가와 높은 상관(r=0.70). 치료 모니터링 도구로서 음성 활용 가능성 입증. | [[P-06]](#ref-p-06) |
| "Multimodal Emotion Recognition: Multi-Turn Emotion Understanding and Reasoning Benchmark" (arXiv, 2025) | 단발 인식 넘어 멀티턴 감정 이해·추론 벤치마크 제안. 장기 맥락에서 감정 추론 능력 평가 프레임워크. | [[P-07]](#ref-p-07) |

---

## 전략적 시사점

**기회**
- Foundation Model zero-shot SER의 부상은 어노테이션 데이터 조달 비용을 낮추는 동시에, 고품질 평가 데이터셋을 보유한 기업에 벤치마크 주도권 기회를 제공한다. MME-Emotion 사례처럼 벤치마크 설계자가 시장 표준을 주도한다.
- 헬스케어 SER: JMIR 리뷰가 임상 근거를 공식화함에 따라, FDA/식약처 인허가 경로가 명확해지는 시점. 보컬비전의 식약처 허가 선례가 국내 후발 기업에게도 경로 가시성을 제공한다.
- 멀티모달(음성+얼굴) 조합: 단일 모달 성능 한계를 보완하는 가장 확실한 경로. SKT 멘탈비전의 접근 방식이 학계 동향(AVT 40%+ 채택)과 일치한다.
- ACII 2026 논문 마감(2026-03-27)이 임박 — 연구 동향 선점 기회.

**위협**
- MME-Emotion 결과(최고 39.3%)는 감정 AI가 아직 성숙하지 않았음을 의미. 제품화 시 성능 과대 선전 리스크가 존재하며, 임상·B2B 고객의 신뢰 확보에 걸림돌.
- Gemini-2.5-Pro·GPT-4o가 Foundation Model 수준에서 감정 인식을 내재화하면, 독립 감정 AI API 사업자의 차별화 근거가 희박해진다. Hume AI 자신이 이 위협에 직면해 있다(EVI 3 출시로 대응 중).
- EU AI Act 및 국내 AI 기본법의 감정 인식 규제 범위가 헬스케어·HR로 확대될 경우, 임상 적용 경로가 제한될 수 있다.
- 음성 바이오마커 우울증 탐지(민감도 71.3%, 특이도 73.5%)는 PHQ-9 대비 성능 미달 — 독립 진단 도구로서의 시장 진입에 규제·임상 장벽 존재.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Nature npj AI — "Affective computing has changed: the foundation model disruption" | [링크](https://www.nature.com/articles/s44387-025-00061-3) | paper | 2025 | [A] |
| <a id="ref-g-02"></a>G-02 | TechCrunch — "Google reportedly snags up team behind AI voice startup Hume AI" | [링크](https://techcrunch.com/2026/01/22/google-reportedly-snags-up-team-behind-ai-voice-startup-hume-ai/) | news | 2026-01-22 | [B] |
| <a id="ref-g-03"></a>G-03 | SKT 뉴스룸 — "SKT, AI로 음성 분석해 마음건강 지키는 '멘탈비전' 출시" | [링크](https://news.sktelecom.com/214844) | news | 2025-09-04 | [B] |
| <a id="ref-g-04"></a>G-04 | Intellectia AI — "Google's DeepMind Signs Licensing Deal with Hume AI, CEO Joins Team" | [링크](https://intellectia.ai/news/stock/googles-deepmind-signs-licensing-deal-with-hume-ai-ceo-joins-team) | news | 2026-01 | [B] |
| <a id="ref-g-05"></a>G-05 | Hume AI Blog — "Introducing EVI 3: the world's most realistic and instructible speech-to-speech foundation model" | [링크](https://www.hume.ai/blog/introducing-evi-3) | blog | 2025 | [B] |
| <a id="ref-g-06"></a>G-06 | Hume AI Blog — "Announcing EVI 3 API: The most customizable speech-to-speech model" | [링크](https://www.hume.ai/blog/announcing-evi-3-api) | blog | 2025 | [B] |
| <a id="ref-g-07"></a>G-07 | OpenAI — "Hello GPT-4o" | [링크](https://openai.com/index/hello-gpt-4o/) | blog | 2024-05-13 | [A] |
| <a id="ref-g-08"></a>G-08 | MME-Emotion GitHub / OpenReview — "MME-Emotion: A Holistic Evaluation Benchmark for Emotional Intelligence in MLLMs" | [링크](https://openreview.net/forum?id=oSX9aenbea) | paper | 2026 | [A] |
| <a id="ref-g-09"></a>G-09 | PMC — "Evaluating the performance of general purpose LLMs in identifying human facial emotions" | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC12533101/) | paper | 2025 | [A] |
| <a id="ref-g-10"></a>G-10 | Microsoft Azure Blog — "Cross-channel emotion analysis in Microsoft Video Indexer" | [링크](https://azure.microsoft.com/en-us/blog/cross-channel-emotion-analysis-in-microsoft-video-indexer/) | blog | 2024 | [B] |
| <a id="ref-g-11"></a>G-11 | Amazon Science — "How Amazon Chime SDK's voice tone analysis works" | [링크](https://www.amazon.science/blog/how-amazon-chime-sdks-voice-tone-analysis-works) | blog | 2024 | [B] |
| <a id="ref-g-12"></a>G-12 | PubMed — "Evaluation of an AI-Based Voice Biomarker Tool to Detect Signals Consistent With Moderate to Severe Depression" | [링크](https://pubmed.ncbi.nlm.nih.gov/39805690/) | paper | 2025 | [A] |
| <a id="ref-g-13"></a>G-13 | GlobeNewswire — "Emotion AI Market Trends and Global Forecasts Report 2025-2035" | [링크](https://www.globenewswire.com/news-release/2026/01/20/3221854/28124/en/Emotion-AI-Market-Trends-and-Global-Forecasts-Report-2025-2035-Opportunities-in-Enhancing-Customer-Experiences-and-Mental-Health-Monitoring-Driven-by-Advancements-in-ML-and-NLP.html) | news | 2026-01-20 | [B] |
| <a id="ref-g-14"></a>G-14 | MarketsandMarkets — "Emotion AI Market worth $9.01 billion by 2030" | [링크](https://www.marketsandmarkets.com/PressReleases/emotion-ai.asp) | report | 2024 | [B] |
| <a id="ref-g-15"></a>G-15 | ACII 2026 공식 사이트 — "Call for Papers - ACII 2026" | [링크](https://acii-conf.net/2026/index.php/sample-page/) | conference | 2026 | [A] |
| <a id="ref-g-16"></a>G-16 | WikiCFP — "ACII 2026: Affective Computing and Intelligent Interaction" | [링크](http://www.wikicfp.com/cfp/servlet/event.showcfp?copyownerid=90704&eventid=191593) | conference | 2026 | [B] |
| <a id="ref-g-17"></a>G-17 | Sensory — "10 predictions for Edge AI in 2026: LLMs gain Efficiency" | [링크](https://sensory.com/edge-ai-2026/) | blog | 2026 | [C] |
| <a id="ref-g-18"></a>G-18 | ScienceDirect — "Exploring the prospects of multimodal LLMs for Automated Emotion Recognition in education: Insights from Gemini" | [링크](https://www.sciencedirect.com/science/article/abs/pii/S0360131525000752) | paper | 2025 | [A] |
| <a id="ref-p-01"></a>P-01 | Liang et al. — "Affective Computing Has Changed: The Foundation Model Disruption" | [링크](https://arxiv.org/abs/2409.08907) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | FunAudioLLM et al. — "MME-Emotion: A Holistic Evaluation Benchmark for Emotional Intelligence in MLLMs" | [링크](https://arxiv.org/abs/2508.09210) | paper | 2026 | [A] |
| <a id="ref-p-03"></a>P-03 | JMIR Mental Health — "Speech Emotion Recognition in Mental Health: Systematic Review of Voice-Based Applications" | [링크](https://mental.jmir.org/2025/1/e74260) | paper | 2025-09 | [A] |
| <a id="ref-p-04"></a>P-04 | npj Digital Medicine — "Evaluating the performance of general purpose LLMs in identifying human facial emotions" | [링크](https://www.nature.com/articles/s41746-025-01985-5) | paper | 2025 | [A] |
| <a id="ref-p-05"></a>P-05 | PMC — "A Comprehensive Review of Multimodal Emotion Recognition: Techniques, Challenges, and Future Directions" | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC12292624/) | paper | 2025 | [A] |
| <a id="ref-p-06"></a>P-06 | npj Parkinson's Disease — "Digital speech biomarkers can measure acute effects of levodopa in Parkinson's disease" | [링크](https://www.nature.com/articles/s41531-025-01045-5) | paper | 2025 | [A] |
| <a id="ref-p-07"></a>P-07 | arXiv — "Beyond Emotion Recognition: A Multi-Turn Multimodal Emotion Understanding and Reasoning Benchmark" | [링크](https://arxiv.org/html/2508.16859v1) | paper | 2025 | [B] |
| <a id="ref-e-01"></a>E-01 | SKT 뉴스룸 — "SKT, '멘탈비전' AI 기술로 마음건강 지킨다" | [링크](https://news.sktelecom.com/214844) | IR/발표 | 2025-09-04 | [A] |
| <a id="ref-e-02"></a>E-02 | SKT 전자신문 보도 — "SKT, AI 멘탈케어 기술 개발…표정·음성으로 정신건강 분석" | [링크](https://www.etnews.com/20240926000024) | news | 2024-09-26 | [B] |
| <a id="ref-e-03"></a>E-03 | Oreate AI Blog — "Google's Stealth Move: How Hume AI's Emotional Intelligence Is Supercharging Gemini" | [링크](https://www.oreateai.com/blog/googles-stealth-move-how-hume-ais-emotional-intelligence-is-supercharging-gemini/d8b38dad37895e29ba55b9a14f793fdb) | blog | 2026-01 | [C] |
