---
type: deep-research
topic: spam-phishing-detection
date: 2026-03-18
parent: 2026-03-18_weekly-secure-ai
period: 2026-03-11 ~ 2026-03-18
previous_report: 2026-03-11_research-spam-phishing-detection.md
---

# Deep 리서치: 스팸/피싱 감지(통화전) (2026-W12)

> 기간: 2026-03-11 ~ 2026-03-18

---

## 기술 동향

1. **P1 Vishing-as-a-Service 플랫폼 노출 — ElevenLabs TTS 남용한 자동화 사기 인프라 확인.**
   Mirage Security 연구진이 2026-03-11 'P1 (p1bot.io)' 플랫폼의 비난독화 클라이언트 측 JavaScript를 분석해 전모를 공개했다. P1은 월 $399(암호화폐 결제)로 스캐머에게 전화번호 스푸핑, ElevenLabs TTS 기반 AI 음성 생성, WebRTC 발신, DTMF 캡처, 통화 녹음 기능을 제공한다. 하드코딩된 ElevenLabs 음성 카탈로그(영어 15개, 프랑스어 4개, 스페인어 4개)를 탑재해 금융기관·정부기관 사칭 "Press 1" 스캠을 완전 자동화한다. ElevenLabs는 보고 즉시 악용 계정을 차단했으나, 서비스형 사기(Scam-as-a-Service) 인프라의 존재가 공식 확인됐다는 점이 핵심이다. [[G-01]](#ref-g-01)

2. **Microsoft Teams, Brand Impersonation Protection 통화 차단 기능 3월 출시 — VoIP 플랫폼에 Pre-Call 보안 확산.**
   2026년 3월 중순 Targeted Release 배포를 시작, 4월 말 GA 예정. 미지의 외부 연락처로부터 수신되는 VoIP 통화를 자동 분석해 신뢰 기관 사칭 패턴 감지 시 수신 전 경고를 표시한다. 관리자 설정 불필요(자동 활성화), 은행·정부기관·IT 지원 사칭 유형에 특화. Microsoft 365 Message Center(MC1219793)를 통해 공식 공지됐다. 통신사 망 레이어가 아닌 기업 커뮤니케이션 플랫폼이 Pre-Call 탐지를 독자 구현한 첫 주요 사례다. [[G-02]](#ref-g-02), [[G-03]](#ref-g-03)

3. **Meta, WhatsApp·Facebook·Messenger 전 플랫폼 AI 사기 탐지 도구 3월 출시.**
   2026-03-11~12 발표. Messenger: 신규 연락처와의 채팅에서 사기 패턴(허위 취업 제안 등) 감지 시 사용자에게 AI 사기 리뷰 공유 여부를 질의하고, AI가 사기로 판단하면 수법 설명 및 차단/신고 옵션을 제시. WhatsApp: 기기 연결 요청의 행동 신호 이상 탐지로 계정 탈취(QR 코드 피싱) 방어. Facebook: 의심 친구 요청 시 계정 생성일·공통 친구 수·지역 불일치 여부를 표시. 법집행 공조로 동남아 스캠센터 관련 계정 15만+ 건 비활성화. [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)

4. **KT, 'AI 보이스피싱 탐지 서비스 2.0' 상용화 — 화자인식 + 딥보이스 탐지 국내 최초 통합.**
   화자인식 기능에 국립과학수사연구원 제공 '그놈목소리' 음성 데이터베이스를 적용하며 개인정보보호위원회 규제 심사·승인을 거쳐 상용화했다. 기존 문맥 탐지(v1.0)에 범죄자 성문 매칭과 AI 합성음성 식별을 추가한 3중 체계다. 삼성 갤럭시 S23 이상 단말기 지원, 이통사 무관 '후후(WhoWho)' 앱으로 이용 가능. 2025년 약 1,300억원 피해 예방 실적 공개. [[G-06]](#ref-g-06), [[G-07]](#ref-g-07)

5. **C2PA 콘텐츠 진본성 표준, 2026년 미디어·AI 플랫폼 전반으로 확산 — 음성 인증 기반으로 발전 가능성.**
   OpenAI가 2025년 11월 DALL-E 3, GPT-image-1, SORA 2 생성 콘텐츠에 C2PA Content Credentials를 자동 적용 시작. 2026년 BBC, Publicis, Reuters, Springer Nature 등이 채택하며 표준이 실제 적용 단계에 진입했다. Content Authenticity Initiative는 현재 회원 6,000개+ 조직에 달한다. 통신사의 Pre-Call 음성 출처 인증(누가 생성했는지, AI인지 사람인지)에 적용 시 딥페이크 통화 차단 인프라의 새로운 레이어가 될 수 있다. 현재 통신사 직접 채택 사례는 확인되지 않음. [[G-08]](#ref-g-08), [[G-09]](#ref-g-09)

6. **AI 교육·인식이 음성 사기 대응의 핵심 변수로 부상 — 기술만으로 불충분하다는 연구 결론.**
   TechXplore(2026-03) 보도에 따르면, 음성 사기에 맞서는 가장 실효적 대응은 AI 기술 탐지가 아닌 사용자 교육이라는 연구 결론이 제시됐다. 딥페이크 음성이 '구별 불가 임계점'을 넘은 현재, 순수 기술 탐지의 한계가 가속화되고 있어 탐지 도구와 사용자 인식 교육의 이중 접근이 필요하다는 논거다. [[G-10]](#ref-g-10)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| SKT | 2025년 통신 사기 차단 11억 건(전년比 +35%), ScamVanguard를 PASS 스팸 필터링·에이닷 전화 AI Safe Block에 적용; 통화패턴 AI 모델로 미신고 보이스피싱 번호 선제 탐지 — 음성 스팸·피싱 250억 건(+119% YoY) 차단 | [[G-11]](#ref-g-11), [[G-12]](#ref-g-12) |
| KT | AI 보이스피싱 탐지 서비스 2.0 상용화: 문맥 탐지 + 화자인식(국과수 성문 DB) + 딥보이스 탐지 3중 체계; 2025년 약 1,300억원 피해 예방; 탐지 정확도 97.2%(2025 Q4); 경찰청 공조 피해 25% 감소 | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07), [[G-13]](#ref-g-13) |
| Microsoft | Teams Brand Impersonation Protection 3월 중순 Targeted Release 배포 시작, 4월 말 GA; 미지 외부 연락처 VoIP 통화 수신 전 자동 경고; 관리자 설정 불필요 | [[G-02]](#ref-g-02), [[G-03]](#ref-g-03) |
| Meta | WhatsApp·Facebook·Messenger 전 플랫폼 AI 사기 탐지 3월 동시 출시; 스캠센터 계정 15만+ 비활성화; 동남아 법집행 공조 21명 검거 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| Hiya | State of the Call 2026 발표(12,000명 설문): 미국인 25% 딥페이크 음성 통화 수신, 소비자 38% 보호 불충분 시 이통사 교체 의향; AI Call Assistant(실시간 딥페이크 차단) 운영 중 | [[G-14]](#ref-g-14) |
| Mirage Security | P1 vishing-as-a-service 플랫폼 노출(ElevenLabs TTS 남용, 월 $399); ElevenLabs 즉시 악용 계정 차단 협력 | [[G-01]](#ref-g-01) |
| ElevenLabs | P1 플랫폼에 TTS API 남용 사실 확인; 보고 즉시 악용 계정 조치 및 추적성 기능 운영 중 강조 | [[G-01]](#ref-g-01) |

---

## 시장 시그널

- Hiya 'State of the Call 2026'(12,000명 설문): 미국인 주당 평균 9.9건 원치 않는 통화 수신(+16% CAGR since 2023); 전체 조사국 평균 7.4건. [[G-14]](#ref-g-14)
- 소비자 2:1 인식 격차: 미국 소비자들이 "스캐머가 통신사보다 2:1 앞선다"고 응답. 72%는 강력한 정부 규제 지지. [[G-14]](#ref-g-14)
- FTC, 2024년 미국 사기 피해액 $12.5B(약 17조원) 발표. 딥페이크 지원 사기는 2027년까지 $40B 달성 예상(별도 추정치). [[G-15]](#ref-g-15), [[G-16]](#ref-g-16)
- Vishing 증가율: CrowdStrike 기록 기준 2024년 하반기 vishing 사건이 상반기 대비 442% 급증(12월 93건 vs 1월 2건). [[G-17]](#ref-g-17)
- Scam-as-a-Service 가격화: P1 플랫폼 월 $399 구독료 공개 — AI 음성 사기 진입장벽이 실질적으로 붕괴됐음을 정량적으로 확인. [[G-01]](#ref-g-01)
- KT, 경찰청 공조 결과 2025년 보이스피싱 피해 25% 감소 발표. [[G-13]](#ref-g-13)

---

## 학술 동향 (주요 논문)

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "AI Powered Deepfake Voice and Scam Call Detector for Secure Communication" (Saxena et al., ICSIAIML 2025, 게재 2026-01) | CNN + RNN 기반 딥러닝 시스템으로 AI 생성 음성과 조작 음성을 통합 탐지; Pre-Call 스캠 탐지 특화 | [[P-01]](#ref-p-01) |
| "Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead" (PMC, 2025-03) | ASVspoof 2019~2025 챌린지 기반 최신 딥페이크 오디오 탐지 연구 현황 종합 서베이; 향후 과제 제시 | [[P-02]](#ref-p-02) |
| "AudioFakeNet: A Model for Reliable Speaker Verification in Deepfake Audio" (Boucherit et al., MDPI Algorithms, 2025-11) | CNN(공간·스펙트럼) + LSTM(시간 의존성) + Multi-Head Attention 하이브리드; MFCC 기반; EER 기준 SOTA | [[P-03]](#ref-p-03) |
| "Where Are We in Audio Deepfake Detection?" (ACM TOIT, 2025) | 생성 모델-탐지 모델 간 군비경쟁 체계적 분석; 크로스-데이터셋 일반화 한계 지적 | [[P-04]](#ref-p-04) |
| "VoiceRadar: Voice Deepfake Detection" (NDSS 2025) | 마이크로-주파수 및 구성 분석 기반 레이더 방식 실시간 딥보이스 탐지 프레임워크 | [[P-05]](#ref-p-05) |

---

## 이전 대비 변화 (W11 → W12 Delta)

**신규 포착:**
- P1 Vishing-as-a-Service 플랫폼 공개(ElevenLabs TTS 남용, $399/월) — Scam-as-a-Service 인프라 구체적 실체 최초 확인
- Microsoft Teams Brand Impersonation Protection 3월 배포 시작 — 통신사 외 VoIP 플랫폼의 Pre-Call 보안 자체 구현 첫 사례
- Meta 전 플랫폼 AI 사기 탐지 도구 동시 출시 — 메시징 플랫폼이 통신사와 병렬로 독자 사기 방어망 구축

**수치 갱신:**
- KT 2025년 피해 예방 실적: 1,300억원(이전: 2,000억원 목표치 → 이번에 달성치 확인)
- SKT 2025년 차단: 11억 건(이전 보고서에서 이미 확인, 3월 이후 신규 수치 없음)
- 미국 vishing 442% 증가(2024 H1→H2), CrowdStrike 데이터 신규 확인

**유지:**
- Hiya State of the Call 2026 핵심 수치(25%, 38%, 2:1) — 이전 주에 이미 포착, 이번 주 추가 세부 데이터(9.9건/주, +16% CAGR) 보완
- C2PA 채택 확산 흐름 — 통신사 직접 적용은 여전히 미확인

---

## 전략적 시사점

**기회**

- P1 플랫폼 노출로 "사기 자동화 인프라" 실체가 공개됐다. 이는 탐지 측에서도 동일한 AI TTS 패턴(ElevenLabs 음성 ID 등)을 역이용한 음성 지문 탐지(voice fingerprinting) 고도화 기회를 제공한다.
- Microsoft Teams·Meta의 Pre-Call·인-메시지 탐지 독자 구현은 통신사 망 레이어 탐지가 플랫폼 레이어와 경쟁하는 구도를 형성했다. 통신사는 망 레이어의 고유 우위(메타데이터·STIR/SHAKEN 신호)를 결합한 차별화 포지셔닝이 가능하다.
- KT의 국과수 성문 DB 기반 화자인식 상용화는 규제 당국(개인정보보호위원회) 승인을 득한 적법 모델로, 유사 기술 도입 시 규제 허들의 선례가 된다.
- C2PA Content Credentials의 AI 생성 콘텐츠 자동 표시 기능을 통신사 망 레이어에 통합하면, 발신 전 "AI 음성 여부" 메타데이터 제공이 가능한 새 서비스 레이어로 발전 가능하다.

**위협**

- Scam-as-a-Service 진입장벽 붕괴($399/월): 전문 지식 없이 AI 음성 사기를 운용 가능한 플랫폼이 이미 텔레그램으로 유통 중이며, 탐지 측의 대응 속도보다 사기 도구의 확산 속도가 빠른 구조가 고착화되고 있다.
- Microsoft·Meta의 자체 탐지 레이어 구축은 통신사 앱 기반 고객 접점 전략을 희석시킨다. 사용자가 별도 앱(후후, 에이닷) 설치 없이 플랫폼 수준에서 보호받는다면, 통신사의 부가 서비스 가치가 약화될 수 있다.
- ACM TOIT 논문이 지적한 크로스-데이터셋 일반화 한계: 새로운 TTS/음성 클론 모델 출현 시 기존 탐지 모델의 정확도 급락 위험이 지속 존재. P1 플랫폼이 ElevenLabs 음성을 빈번히 교체하면 패턴 기반 탐지 우회 가능.
- 사용자 교육의 중요성 재부각: 순수 기술 탐지만으로는 불충분하다는 연구 결론은, 서비스 품질 지표(탐지율)만으로 소비자 신뢰를 확보하기 어렵다는 마케팅·UX 과제를 시사한다.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Help Net Security — Researchers uncover AI-powered vishing platform | [링크](https://www.helpnetsecurity.com/2026/03/11/researchers-uncover-ai-powered-vishing-platform/) | news | 2026-03-11 | [B] |
| <a id="ref-g-02"></a>G-02 | BleepingComputer — Microsoft Teams to add brand impersonation warnings to calls | [링크](https://www.bleepingcomputer.com/news/microsoft/microsoft-teams-to-add-brand-impersonation-warnings-to-calls/) | news | 2026-03 | [B] |
| <a id="ref-g-03"></a>G-03 | SC Media — Microsoft Teams enhances call security with Brand Impersonation Protection | [링크](https://www.scworld.com/brief/microsoft-teams-enhances-call-security-with-brand-impersonation-protection) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | Meta Newsroom — Fighting Scammers and Protecting People with New Technology and Partnerships | [링크](https://about.fb.com/news/2026/03/fighting-scammers-protecting-people-with-new-technology-and-partnerships/) | 보도자료 | 2026-03 | [A] |
| <a id="ref-g-05"></a>G-05 | Malwarebytes — Meta rolls out anti-scam tools across WhatsApp, Facebook, and Messenger | [링크](https://www.malwarebytes.com/blog/news/2026/03/meta-rolls-out-anti-scam-tools-across-whatsapp-facebook-and-messenger) | news | 2026-03 | [B] |
| <a id="ref-g-06"></a>G-06 | BusinessPost — KT, 'AI 보이스피싱 탐지 서비스 2.0' 출시, 보이스피싱범 목소리와 합성음성까지 식별 | [링크](https://www.businesspost.co.kr/BP?command=article_view&num=405398) | news | 2026-03 | [B] |
| <a id="ref-g-07"></a>G-07 | Digital Today — "목소리까지 잡는다"…KT, 'AI 보이스피싱 탐지 서비스 2.0' 출시 | [링크](https://www.digitaltoday.co.kr/news/articleView.html?idxno=580815) | news | 2026-03 | [B] |
| <a id="ref-g-08"></a>G-08 | Content Authenticity Initiative — The State of Content Authenticity in 2026 | [링크](https://contentauthenticity.org/blog/the-state-of-content-authenticity-in-2026) | blog | 2026 | [B] |
| <a id="ref-g-09"></a>G-09 | C2PA — Content Credentials White Paper (2025-10) | [링크](https://c2pa.org/wp-content/uploads/sites/33/2025/10/content_credentials_wp_0925.pdf) | 공식문서 | 2025-10 | [A] |
| <a id="ref-g-10"></a>G-10 | TechXplore — AI education could be crucial in tackling rising voice scams | [링크](https://techxplore.com/news/2026-03-ai-crucial-tackling-voice-scams.html) | news | 2026-03 | [B] |
| <a id="ref-g-11"></a>G-11 | Telecompaper — SKT reveals rise in AI-driven blocking of spam and voice phishing attempts | [링크](https://www.telecompaper.com/news/skt-reveals-rise-in-ai-driven-blocking-of-spam-and-voice-phishing-attempts--1558993) | news | 2026-01 | [B] |
| <a id="ref-g-12"></a>G-12 | The Readable — SK Telecom ScamVanguard: Transforming mobile scam prevention with AI | [링크](https://thereadable.co/sk-telecom-scamvanguard-transforming-mobile-scam-prevention-with-ai/) | news | 2026-01 | [B] |
| <a id="ref-g-13"></a>G-13 | Herald Economy — 보이스피싱 잡는 'AI'…KT·경찰 공조로 피해 25%↓ | [링크](https://biz.heraldcorp.com/article/10694780) | news | 2026-03 | [B] |
| <a id="ref-g-14"></a>G-14 | Hiya / NatLawReview — State of the Call 2026: AI Deepfake Voice Calls Hit 1 in 4 Americans | [링크](https://natlawreview.com/press-releases/state-call-2026-ai-deepfake-voice-calls-hit-1-4-americans-consumers-say) | 리포트 | 2026-03-02 | [B] |
| <a id="ref-g-15"></a>G-15 | Webster First / FTC — FTC reports $12.5B in scam losses (2024 scam trends) | [링크](https://www.websterfirst.com/blog/what-the-2024-ftc-data-tells-us-about-scam-trends/) | news | 2025 | [B] |
| <a id="ref-g-16"></a>G-16 | DeepStrike — Vishing Statistics 2025: AI Deepfakes & the $40B Voice Scam Surge | [링크](https://deepstrike.io/blog/vishing-statistics-2025) | blog | 2025 | [C] |
| <a id="ref-g-17"></a>G-17 | Vishing Attacks 2026: How Voice Scams Are Outsmarting | [링크](https://tvm.offensoacademy.com/vishing-attacks-2026-voice-scams-beating/) | blog | 2026 | [C] |
| <a id="ref-p-01"></a>P-01 | Saxena et al. — AI Powered Deepfake Voice and Scam Call Detector for Secure Communication (Atlantis Press, ICSIAIML 2025) | [링크](https://www.atlantis-press.com/proceedings/icsiaiml-25/126021219) | paper | 2026-01 | [A] |
| <a id="ref-p-02"></a>P-02 | PMC — Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/) | paper | 2025-03 | [A] |
| <a id="ref-p-03"></a>P-03 | Boucherit et al. — AudioFakeNet: A Model for Reliable Speaker Verification in Deepfake Audio (MDPI Algorithms) | [링크](https://www.mdpi.com/1999-4893/18/11/716) | paper | 2025-11 | [A] |
| <a id="ref-p-04"></a>P-04 | ACM TOIT — Where Are We in Audio Deepfake Detection? A Systematic Analysis | [링크](https://dl.acm.org/doi/10.1145/3736765) | paper | 2025 | [A] |
| <a id="ref-p-05"></a>P-05 | NDSS 2025 — VoiceRadar: Voice Deepfake Detection | [링크](https://www.ndss-symposium.org/wp-content/uploads/2025-3389-paper.pdf) | paper | 2025 | [A] |
