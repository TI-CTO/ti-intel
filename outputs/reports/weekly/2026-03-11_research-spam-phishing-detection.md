---
topic: spam-phishing-detection
date: 2026-03-11
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
domain: secure-ai
l3_topic: 스팸피싱감지(통화전)
period: 2026-03-04 ~ 2026-03-11
previous_report: 2026-03-05_research-spam-phishing-detection.md
---

# 스팸피싱감지(통화전) — 심층 리서치

> 기간: 2026-03-04 ~ 2026-03-11

---

## 기술 동향

- **LG Uplus, 세계 최초 온디바이스 Anti-DeepVoice 상용화**: MWC 2026(2026-03-02~03-05)에서 ixi-O AI 에이전트 서비스에 통화 시작 수 초 내 딥보이스(조작·합성 음성) 실시간 감지 기능을 공개했다. 음성 데이터를 클라우드로 전송하지 않고 단말 내에서만 처리(On-Device)하여 개인정보 유출 위험을 차단한다. [[G-01]](#ref-g-01)

- **KT Who Who 탐지 정확도 Q4 2025 최신치 확인**: 2025년 4분기 기준 97.2%로 상향(Q1 2025 기준 90.3%)되었음이 이번 주 복수 외신 보도에서 확인됐다. KT는 AI 문맥 탐지 + 화자인식 + 딥보이스 탐지 3중 체계를 유지하며, 연간 2,000억원 상당 피해 예방을 목표로 제시했다. [[G-02]](#ref-g-02), [[G-03]](#ref-g-03)

- **Samsung Galaxy One UI 8 + 이통3사 협력 서비스 구조 상세 확인**: Samsung Phone 앱(One UI 8.0 이상)에 내장된 '보이스피싱 의심 통화 알림'은 경찰청 및 국립과학수사연구소로부터 제공받은 3만 건 이상의 보이스피싱 녹취 데이터로 딥러닝 학습한 온디바이스 모델을 사용한다. 경보는 '의심(노란 팝업)' / '위험(빨간 팝업)' 2단계로 출력된다. 현재 한국 전용, 모르는 번호 발신 전용(수신 통화는 미지원). [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)

- **Hiya, 실시간 딥페이크 스캠 차단 AI Call Assistant 출시**: 통화 전 스팸 탐지(Pre-Call)에 더해, 통화 중 라이브 및 딥페이크 스캠을 실시간으로 차단하는 AI Call Assistant를 출시했다. 기존 Adaptive AI 기반 번호 평판 분석(Enterprise Caller Scoring)과 통합 운영된다. [[G-06]](#ref-g-06)

- **Virgin Media O2 + Hiya: Call Defence, 10억 건 스캠 탐지 도달**: 2026-03-10 발표. Adaptive AI로 번호 행동 패턴을 분석하며 월 7,000만 건 이상을 플래그 처리한다. 화면에 통화 수신 전 경고를 표시하는 Pre-Call 방식. 2026년 가장 많은 사기 유형은 Amazon 사칭, HMRC 사칭, 은행 사칭 순. [[G-07]](#ref-g-07)

- **VoIP Review(2026-03-09): 통신사 AI 네트워크 임베딩 확산 보고**: 통신사들이 AI를 망 레이어에 직접 내장하여 발신번호 데이터·음성 특성·오디오 신호를 분석해 음성 지문을 생성하고 합성 음성의 고유 특성을 식별하는 추세가 확산 중이라고 보고했다. [[G-08]](#ref-g-08)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| LG Uplus | MWC 2026에서 ixi-O Anti-DeepVoice(세계 최초 온디바이스 딥보이스 탐지) 공개; GSMA GLOMO 2026 CTO Choice 수상; KB Kookmin Bank 이상거래 모니터링 연동 | [[G-01]](#ref-g-01), [[G-09]](#ref-g-09) |
| KT | Who Who 앱 탐지 정확도 90.3%→97.2%(2025 Q1→Q4); AI 3중 체계(문맥+화자인식+딥보이스); 연간 2,000억원 피해 예방 목표 | [[G-02]](#ref-g-02), [[G-03]](#ref-g-03) |
| SKT | 2025년 보이스피싱+스팸 차단 11억 건(전년比 음성 스팸 119% 증가 차단); Aida Phone 앱 통화 중 AI 탐지 '의심/위험' 2단계 알림 | [[G-10]](#ref-g-10), [[G-11]](#ref-g-11) |
| Samsung | One UI 8.0 이상 Galaxy에 경찰청 3만+ 녹취 학습 온디바이스 AI 내장; 이통3사와 협력 체계; 한국 전용, 모르는 번호 발신 전용 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| Hiya | AI Call Assistant(실시간 딥페이크 스캠 차단) 출시; Virgin Media O2와 Call Defence로 10억 건 탐지 달성(월 7,000만 건); Enterprise Caller Scoring으로 번호 로테이션 우회 차단 | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07) |
| Virgin Media O2 | Hiya와 Call Defence 서비스로 10억 건 스캠·스팸 플래그 달성; 무료 제공; 2026년 상위 사기 유형(Amazon/HMRC/은행 사칭) 공개 | [[G-07]](#ref-g-07) |
| McAfee | Deepfake Detector 96% 정확도, 3초 내 판별; Lenovo/AMD/Intel NPU 기반 온디바이스 처리; 약 20만 건 샘플 학습 | [[G-12]](#ref-g-12) |
| FCC | AI 생성 음성 로보콜을 TCPA상 'artificial voice'로 규정하여 불법화; 2026-02-05 Robocall Mitigation Database 강화 규정 발효 | [[G-13]](#ref-g-13) |

---

## 시장 시그널

- Hiya 'State of the Call 2026' 보고서(12,000명 설문, 미국·영국·캐나다·프랑스·독일·스페인): 미국인 4명 중 1명이 지난 12개월 내 딥페이크 음성 통화를 수신했으며, 추가 24%는 구분 불가능하다고 응답 — 사실상 미국 성인 절반이 AI 음성 사기에 노출. [[G-14]](#ref-g-14)

- 같은 보고서: 구독자의 38%가 AI 스캠으로부터 보호받지 못한다고 느끼면 이통사를 교체할 의향이 있다고 응답. 72%는 강력한 정부 규제를 지지. 67%는 이통사가 스캠 손실의 일부 책임을 져야 한다고 주장. [[G-14]](#ref-g-14)

- 딥페이크 지원 사기 손실 규모: 2027년까지 $40B(약 55조원) 달성 예상. 55세 이상 시니어 피해 평균 $1,298(약 180만원)/건으로 젊은 연령대의 3배. [[G-15]](#ref-g-15)

- AI 생성 피싱 이메일의 클릭률은 기존 대비 4배. 2025년 2~9월 사이 분석된 피싱 이메일의 82.6%가 AI 포함(KnowBe4 보고서). [[G-16]](#ref-g-16)

- Fortune/연구자 발언(2025-12-27): 음성 클로닝이 '구별 불가 임계점(indistinguishable threshold)'을 넘었다 — 수 초의 오디오만으로 자연스러운 억양·리듬·감정·호흡까지 재현 가능. [[G-17]](#ref-g-17)

- 소비자 신뢰 붕괴: "소비자는 스캐머가 이통사보다 2:1로 앞선다"고 인식(Hiya). 통신이 안전망에서 불안 원천으로 변화 중이라는 진단. [[G-14]](#ref-g-14)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead" (PMC, 2025-03) | ASVspoof 2019~2025 챌린지 기반 최신 딥페이크 오디오 탐지 연구 현황 종합 서베이; 향후 과제 제시 | [[P-01]](#ref-p-01) |
| "AudioFakeNet: A Model for Reliable Speaker Verification in Deepfake Audio" (MDPI Algorithms, 2025-11-13) | CNN(공간·스펙트럼 피처) + LSTM(시간 의존성) + Multi-Head Attention(핵심 구간 집중) 하이브리드 아키텍처; MFCC 기반 학습; EER 기준 SOTA 달성 | [[P-02]](#ref-p-02) |
| "Where Are We in Audio Deepfake Detection?" (ACM TOIT, 2025) | 생성 모델과 탐지 모델 간 군비경쟁 구도 체계적 분석; 크로스-데이터셋 일반화 한계 지적 | [[P-03]](#ref-p-03) |
| "On Deepfake Voice Detection — It's All in the Presentation" (arXiv 2509.26471, 2025-09) | 탐지 성능이 입력 표현 방식(스펙트로그램 vs MFCC 등)에 크게 의존함을 실증 | [[P-04]](#ref-p-04) |
| "VoiceRadar: Voice Deepfake Detection" (NDSS 2025) | 실제 환경에서의 딥보이스 탐지를 위한 레이더 방식 프레임워크 제안; 실시간성 강조 | [[P-05]](#ref-p-05) |

---

## 이전 대비 변화

**2026-03-05 리포트 대비 주요 delta:**

- **신규**: LG Uplus Anti-DeepVoice 세계 최초 온디바이스 상용화 확인 (MWC 2026 공개). 이전 리포트에서 ixi-O는 기능 소개 수준이었으나 이번에 GLOMO CTO Choice 수상과 함께 공식 상용 서비스로 격상.

- **수치 갱신**: KT Who Who 탐지 정확도 최신치 97.2%(이전: Q4 2025 93%+ 수준). 복수 외신에서 97.2%로 구체화.

- **신규**: Virgin Media O2 + Hiya Call Defence 10억 건 달성(2026-03-10 발표). 글로벌 Pre-Call 탐지의 실효성을 보여주는 벤치마크 사례로 신규 포착.

- **신규**: Hiya 'State of the Call 2026' 보고서 발간(2026-03-02). 미국인 25%가 딥페이크 음성 통화 수신 경험이라는 정량 수치 추가.

- **신규**: FCC Robocall Mitigation Database 강화 규정 발효(2026-02-05). 이전 리포트의 STIR/SHAKEN 수준에서 DB 제출 의무 강화로 진전.

- **유지**: SKT 에이닷 전화 기능 구조(의심/위험 2단계)는 이전과 동일. 11억 건 2025 차단 실적 수치 재확인.

- **유지**: Samsung One UI 8 보이스피싱 탐지 구조 동일(경찰청 데이터 3만 건, 2단계 경보). 이번 주 추가 업데이트 없음.

---

## 전략적 시사점

**기회**

- LG Uplus의 GLOMO 수상은 On-Device Anti-DeepVoice가 글로벌 표준 기술로 인정받는 시그널. 국내 통신사 기술이 글로벌 시장 진출 가능한 레퍼런스로 부상.
- Virgin Media O2 + Hiya의 10억 건 탐지 마일스톤은 통신사-플랫폼 파트너십 모델의 실효성을 입증. 국내 3사도 유사한 네트워크 레이어 협력 확대 여지가 있음.
- KT 97.2% 정확도는 사용자 신뢰 구축 및 마케팅 차별화에 활용 가능한 수준. "월 2,000억원 피해 예방" 주장은 가입자 유지 명분으로 활용될 수 있음.
- 학술 분야의 멀티모달 융합(CNN+LSTM+Attention) 모델이 성숙 단계에 진입 — 상용 서비스 품질 격상을 위한 R&D 내재화 기회.

**위협**

- Hiya 보고서: 소비자 38%가 보호 불충분시 이통사 교체 의향 — 탐지 품질 격차가 가입자 이탈 리스크로 직결.
- 음성 클로닝의 '구별 불가 임계점' 도달 — 기존 키워드·패턴 기반 탐지 모델의 한계가 가속화되고 있으며, 딥보이스 탐지 모듈 없이는 탐지율 급락 가능.
- McAfee(96%), Hiya AI Call Assistant 등 독립 보안 플랫폼이 통신사 앱 없이도 동등한 탐지 기능을 제공 — 앱 기반 고객 락인 전략의 희석.
- ACM TOIT 논문이 지적한 "크로스-데이터셋 일반화 한계": 특정 TTS/음성 클론 툴에 최적화된 모델이 새 생성 모델 출현 시 탐지율 급락 위험. 재학습 파이프라인 부재 시 대응 지연.
- 딥페이크 피해 2027년 $40B 예상 — 피해 규모가 빠르게 증가할수록 규제 당국의 통신사 책임 강화 압력도 증가(67%가 통신사 책임 인정 필요 응답).

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Korea IT Times — LG Uplus Unveils Ambient AI Vision with ixi-O at MWC26 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151439) | news | 2026-03-03 | [B] |
| <a id="ref-g-02"></a>G-02 | The Fast Mode — KT Brings AI Voice Phishing Detection Service to Market | [링크](https://www.thefastmode.com/technology-solutions/39153-kt-unveils-real-time-ai-voice-phishing-protection) | news | 2026-03 | [B] |
| <a id="ref-g-03"></a>G-03 | The Pickool — KT Gains Regulatory Approval for AI-Powered Voice Phishing Detection | [링크](https://www.thepickool.com/kt-gains-regulatory-approval-for-ai-powered-voice-phishing-detection-service/) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | Android Police — Samsung Galaxy phones get on-device AI voice phishing detection in Korea | [링크](https://www.androidpolice.com/samsung-ai-voice-phishing-scam-detection/) | news | 2026-02 | [B] |
| <a id="ref-g-05"></a>G-05 | SamMobile — Samsung details how Galaxy phones protect people from voice phishing | [링크](https://www.sammobile.com/news/samsung-details-voice-phishing-protection-galaxy-phones/) | news | 2026-02 | [B] |
| <a id="ref-g-06"></a>G-06 | Hiya Newsroom — Hiya Launches First AI Call Assistant That Stops Live and Deepfake Scams in Real-Time | [링크](https://www.hiya.com/en-ca/newsroom/press-releases/hiya-launches-first-ai-call-assistant-that-stops-live-and-deepfake-scams-in-real-time) | 보도자료 | 2025 | [A] |
| <a id="ref-g-07"></a>G-07 | Virgin Media O2 — AI helps detect and flag 1 billion suspected scam and spam calls | [링크](https://news.virginmediao2.co.uk/ai-helps-virgin-media-o2-detect-and-flag-1-billion-suspected-scam-and-spam-calls-to-customers/) | 보도자료 | 2026-03-10 | [A] |
| <a id="ref-g-08"></a>G-08 | VoIP Review — AI Empowers Telecoms in the Battle Against Voice Scams | [링크](https://voip.review/2026/03/09/ai-empowers-telecoms-battle-against-voice-scams/) | news | 2026-03-09 | [B] |
| <a id="ref-g-09"></a>G-09 | Digital Today — LG Uplus wins three GLOMO awards including CTO Choice | [링크](https://www.digitaltoday.co.kr/en/view/18425/mwc26-lg-uplus-wins-three-glomo-awards-including-cto-choice) | news | 2026-03 | [B] |
| <a id="ref-g-10"></a>G-10 | Telecompaper — SKT reveals rise in AI-driven blocking of spam and voice phishing attempts | [링크](https://www.telecompaper.com/news/skt-reveals-rise-in-ai-driven-blocking-of-spam-and-voice-phishing-attempts--1558993) | news | 2026-03 | [B] |
| <a id="ref-g-11"></a>G-11 | StarNews Korea — Samsung Electronics, 3 mobile carriers detect voice phishing in real time | [링크](https://www.starnewskorea.com/en/business-life/2026/02/12/2026021214210282736) | news | 2026-02-12 | [B] |
| <a id="ref-g-12"></a>G-12 | McAfee — Deepfake Detector: AI Audio and Video Detection | [링크](https://www.mcafee.com/ai/deepfake-detector/) | 제품 공식 | 2024~2026 | [A] |
| <a id="ref-g-13"></a>G-13 | FCC — FCC Makes AI-Generated Voices in Robocalls Illegal | [링크](https://www.fcc.gov/document/fcc-makes-ai-generated-voices-robocalls-illegal) | 규제 공시 | 2024-02 | [A] |
| <a id="ref-g-14"></a>G-14 | Hiya — State of the Call 2026: AI Deepfake Voice Calls Hit 1 in 4 Americans | [링크](https://natlawreview.com/press-releases/state-call-2026-ai-deepfake-voice-calls-hit-1-4-americans-consumers-say) | 리포트 | 2026-03-02 | [B] |
| <a id="ref-g-15"></a>G-15 | CX Today — The Voice Trust Collapse: Deepfake Voice Fraud 2026 | [링크](https://www.cxtoday.com/security-privacy-compliance/the-voice-trust-collapse-and-deepfake-voice-fraud/) | news | 2026-03 | [B] |
| <a id="ref-g-16"></a>G-16 | StrongestLayer — AI-Generated Phishing: The Top Enterprise Threat of 2026 | [링크](https://www.strongestlayer.com/blog/ai-generated-phishing-enterprise-threat) | blog | 2026-03 | [C] |
| <a id="ref-g-17"></a>G-17 | Fortune — 2026 will be the year you get fooled by a deepfake | [링크](https://fortune.com/2025/12/27/2026-deepfakes-outlook-forecast/) | news | 2025-12-27 | [B] |
| <a id="ref-p-01"></a>P-01 | PMC — Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/) | paper | 2025-03 | [A] |
| <a id="ref-p-02"></a>P-02 | Boucherit et al. — AudioFakeNet: A Model for Reliable Speaker Verification in Deepfake Audio (MDPI Algorithms) | [링크](https://www.mdpi.com/1999-4893/18/11/716) | paper | 2025-11-13 | [A] |
| <a id="ref-p-03"></a>P-03 | ACM TOIT — Where are We in Audio Deepfake Detection? A Systematic Analysis | [링크](https://dl.acm.org/doi/10.1145/3736765) | paper | 2025 | [A] |
| <a id="ref-p-04"></a>P-04 | arXiv 2509.26471 — On Deepfake Voice Detection: It's All in the Presentation | [링크](https://arxiv.org/abs/2509.26471) | paper | 2025-09 | [B] |
| <a id="ref-p-05"></a>P-05 | NDSS 2025 — VoiceRadar: Voice Deepfake Detection | [링크](https://www.ndss-symposium.org/wp-content/uploads/2025-3389-paper.pdf) | paper | 2025 | [A] |
