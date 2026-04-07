---
type: weekly-deep-research
topic: spam-phishing-detection
l3_name: "스팸/피싱 감지(통화전)"
date: 2026-04-07
week: 2026-W16
parent_domain: secure-ai
agent: research-deep
confidence: medium-high
status: completed
sources_used: [websearch, webfetch]
---

# 심층 분석: 스팸/피싱 감지(통화전) (2026-W16)

## 이전 대비 변화

- **전주 (W15)**: INTERPOL-UNODC $442B 글로벌 사기 손실 공식화, ABA·Better Identity Coalition (BIC) 연방 정책 20개 권고안(4/1), Pindrop Pulse 2초 99% 탐지, Agentic AI 사기 독립 위협 범주화
- **금주 (W16)**: EvilTokens PhaaS 340+ 기관 타깃 디바이스코드 피싱 급부상(3/31), Microsoft "AI가 공격 도구에서 사이버공격 표면으로 전환" 경고(4/2), Tycoon2FA PhaaS 공조 폐쇄 후 즉시 재개(3/4→4월 지속), 한국 통신사기피해환급법 시행령 개정안 입법예고(4/2~5/12)
- **변화 방향**: ① 피싱 공격이 단순 딥페이크 음성에서 AI 자동화 OAuth 탈취(Device Code Phishing)로 다변화. ② PhaaS(Phishing-as-a-Service) 플랫폼이 차단 후 즉시 복구하는 회복탄력성 확보 — 단속 효과 반감. ③ 한국 규제가 정보공유 의무화 방향으로 전환, 통신-금융-수사 삼각 협력 법제화 진입.

---

## 기술 동향

1. **Microsoft — AI가 피싱 클릭률 450% 상승, '공격 표면'으로 전환 (4/2)**
   Microsoft Security Blog(4/2) [[G-01]](#ref-g-01)이 AI 위협 보고서를 발표했다. WebFetch 원문 확인 결과 AI 활용 피싱의 클릭률이 비(非)AI 대비 450% 높으며, 생성형 AI가 정찰·무기화·초기접근·지속성 유지까지 공격 전 단계에 내재화됐다고 분석했다. 특히 "에이전트 에코시스템이 기업의 가장 집중 공격 표면이 될 것"이라는 전망이 주목된다. Sherrod DeGrippo 부 CISO(Microsoft) 발언: "공격 임계비용이 국가급 자원에서 개인 툴 접근성 수준으로 붕괴했다."

2. **EvilTokens — PhaaS 플랫폼, 340+ 기관 대상 Device Code Phishing (3/31)**
   2026-02-16 Telegram 첫 광고 이후 2026-03-31 기준 340개 이상 Microsoft 365 기관이 피해를 입었다 [[G-02]](#ref-g-02), [[G-03]](#ref-g-03). Device Code Phishing(디바이스 코드 피싱)은 OAuth RFC 8628의 합법적 인증 흐름을 악용해 MFA(Multi-Factor Authentication)를 완전 우회한다. 피해자가 직접 MFA를 완료하되 공격자가 세션 토큰을 수집하는 구조로, 패스워드 리셋 후에도 리프레시 토큰이 유효하다. 피해 섹터: 건설·비영리·금융·의료·법률·지방정부. 한국 통신사 컨택센터 환경에도 동일 위협 벡터 노출 가능성이 있다.

3. **Tycoon2FA 폐쇄 후 즉각 복구 — PhaaS 회복탄력성 확인 (3/4~4월)**
   Europol·Microsoft·Cloudflare 등 공조로 2026-03-04 Tycoon2FA 인프라 300개 도메인 압수, 64,000건 공격 연계 플랫폼 차단 [[G-04]](#ref-g-04), [[G-05]](#ref-g-05). 그러나 3/4~3/5 이틀간 25% 수준으로 급감한 캠페인 볼륨이 수일 내 압수 전 수준으로 복구됐다. Adversary-in-the-Middle (AiTM) 프록시로 세션 쿠키를 실시간 탈취하는 방식이며 월 500만+ 조직 대상 수천만 건 발송 규모로 운영됐다. 이 사례는 단일 PhaaS 폐쇄가 피싱 생태계 억제에 구조적 한계를 가짐을 실증한다.

4. **Cofense 연간 리포트 — AI 피싱 204% 급증, 19초당 1건 (2026-02)**
   Cofense 2025년 연간 피싱 위협 보고서 [[G-06]](#ref-g-06)에 따르면 악성코드 탑재 피싱 캠페인이 전년 대비 204% 증가했다. 2025년 기준 19초당 1건의 악성 이메일 발생(2024년 42초 대비 2배 이상 가속). 5가지 핵심 트렌드: ① 초기 감염 URL 76%가 고유 주소(폴리모픽 피싱), ② 동적 피싱 페이지(OS별 페이로드 분기), ③ 원격접속 도구 악용 900% 증가, ④ 대화형 BEC(Business Email Compromise) 18% 비중, ⑤ .es 도메인 크리덴셜 피싱 51배 급증.

5. **Microsoft AI 활성화 디바이스코드 피싱 심층 분석 (4/6)**
   Microsoft Defender Security Research Team(4/6) [[G-07]](#ref-g-07)이 AI 활성화 디바이스코드 피싱 캠페인을 분석했다. EvilToken PhaaS 기반으로 역할 맞춤형 생성형 AI 피싱 이메일(RFP, 인보이스, 제조 워크플로우 테마), 15분 만료 코드를 인터랙션 시점에 동적 생성하는 자동화, Vercel·Cloudflare Workers·AWS Lambda를 통한 트래픽 위장을 특징으로 한다. Storm-2372(2025-02)에서 진화한 형태다.

6. **한국 통신사기피해환급법(전기통신금융사기 피해 방지 및 피해금 환급에 관한 특별법) 시행령 개정안 입법예고 (4/2~5/12)**
   금융위원회 주도로 2026-04-02 입법예고가 개시됐다 [[G-08]](#ref-g-08). WebFetch 원문 확인: ① 금융사·통신사·수사기관 간 의심거래 탐지 정보공유 범위 명확화, ② 정보공유 분석기관 지정 요건·절차 신설, ③ "선제적 탐지·차단" 법적 근거 마련. 2025년 10월~2026년 2월 보이스피싱 신고 건수 31.6% 감소(9,777→6,687건), 피해금액 26.4% 감소를 달성한 상황에서 추가 제도화 입법이 추진된다.

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Microsoft | 4/2 AI 위협 보고서: AI 피싱 클릭률 450% 상승, 에이전트 에코시스템이 최대 공격 표면 예고. 4/6 EvilTokens 캠페인 심층 기술 분석 공개. Tycoon2FA 폐쇄(3/4) 공조 주도 | [[G-01]](#ref-g-01), [[G-07]](#ref-g-07) |
| EvilTokens (PhaaS) | 2026-02-16 Telegram 첫 등장. 340+ Microsoft 365 기관 타깃(미·캐·호·뉴질랜드·독일). AI 워크플로우·24/7 지원팀·Gmail·Okta 확장 예정. Device Code Phishing 서비스화 | [[G-02]](#ref-g-02), [[G-03]](#ref-g-03) |
| Tycoon2FA (PhaaS) | 3/4 Europol·Microsoft 공조 폐쇄(도메인 300개 압수). 이틀 내 복구. 월 500만+ 기관 대상 운영, Tycoon2FA 단독 Microsoft 차단 피싱의 62%(2025년 중반). AiTM 방식으로 모든 MFA 우회 가능 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |
| Pindrop | Fraud Assist(3/17 출시): 에이전트형 사기 조사·케이스 관리 솔루션. 분석관 효율 70% 향상(베타), FNBO 사기 케이스 처리 정확도 50% 향상. 연간 $1M 절감 효과 추정. Negative Voice ID로 번호·기기 변경해도 프로드 검출 | [[G-09]](#ref-g-09) |
| Adaptive Security | 총 $146.5M 누적 펀딩(Series A $55M + Series B $81M). OpenAI 첫 사이버보안 투자처. Bain Capital Ventures·NVIDIA·a16z 참여. 딥페이크·비싱·스미싱·GenAI 이메일 공격 대상 AI 시뮬레이션 플랫폼 | [[G-10]](#ref-g-10) |
| Cofense | 2025년 AI 피싱 위협 연간 보고서(2026-02): 204% 증가, 19초당 1건. 폴리모픽 피싱·동적 페이지·대화형 BEC 주요 추세 분석 | [[G-06]](#ref-g-06) |
| ABA / Better Identity Coalition | Financial Services Sector Coordinating Council (FSSCC) 공동 정책 문서(4/1): 130명+ 전문가 18개월 작업. 정책입안자 대상 20개 권고안 발표. FIDO 패스키·모바일 운전면허증(mDL) 도입 규제 장벽 제거 권고, Treasury 산하 태스크포스 신설 촉구 | [[G-11]](#ref-g-11) |
| SKT | ScamVanguard AI로 2025년 보이스피싱 2.5억 건(+배 이상), 스팸 문자 8.5억 건(+22%) 합계 11억 건 차단. AI 미끼 문자 탐지·피싱 시도 채팅 탐지·음성피싱 통화 패턴 분석·실명 분석 4개 AI 앱 추가 | [[G-12]](#ref-g-12) |
| KT | 후후(HuHu) 앱: 문맥 탐지+화자 인식+딥보이스 감지 삼중 체계. 2025년 4,680만 건 처리 중 3,000건 차단. 탐지 정확도 Q1 90.3% → Q4 97.2% | [[G-13]](#ref-g-13) |

---

## 시장 시그널

**투자 & M&A**
- Adaptive Security 누적 $146.5M 펀딩 완료(Series B $81M, 2025년 12월): OpenAI의 첫 사이버보안 투자처로 업계 상징성 [[G-10]](#ref-g-10)
- Tycoon2FA: Telegram 구독형 $120/10일, 월 약 2,000 고객 기반으로 추정 — PhaaS 상업화 규모 확인 [[G-05]](#ref-g-05)

**시장 전망**
- Vishing(음성 피싱) 공격: 2024년 하반기 상반기 대비 442% 증가 (CrowdStrike) [[G-14]](#ref-g-14)
- 딥페이크 기반 vishing: 2025년 Q1에 Q4 2024년 대비 1,600%+ 급증 [[G-14]](#ref-g-14)
- 미국 AI 사기 손실: 2023년 $12.3B → 2027년 $40B 전망 (Deloitte Center for Financial Services) [[G-11]](#ref-g-11)
- 글로벌 조직 사기 손실: $442B (Global Anti-Scam Alliance 추정) [[G-15]](#ref-g-15) [추가확인 필요]

**규제·정책 움직임**
- 한국 통신사기피해환급법 시행령 개정안 입법예고(4/2~5/12): 금융-통신-수사 정보공유 의무화 추진 [[G-08]](#ref-g-08)
- ABA·BIC 연방 정책 20개 권고안(4/1): FIDO 패스키·mDL 도입 규제 장벽 제거, Treasury 태스크포스 신설 [[G-11]](#ref-g-11)
- FSSCC 권고: "차세대 원격 신원 증명 시스템과 강력 인증, 국제 요건 조화, 신흥 위협 교육" 4대 이니셔티브 [[G-11]](#ref-g-11)

---

## 학술 동향

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead" (PMC, 2024/2025) | ASVspoof 2019 LA 데이터셋에서 EER 0.06% 달성. Wav2Vec 2.0·WavLM 등 자기지도학습 모델이 전통 MFCC 대체. 실세계 오디오 일반화가 여전히 핵심 과제 | [[P-01]](#ref-p-01) |
| "Where are We in Audio Deepfake Detection?" (ACM Transactions on Internet Technology, 2026) | 최신 TTS 도구(OpenAI Voice Engine 등) 대상 성능 저하 문제 실증. 최신 TTS 벤치마킹 우선 연구 필요성 제기 | [[P-02]](#ref-p-02) |

---

## 전략적 시사점

**기회**
- 한국 통신사기피해환급법 시행령 개정(입법예고 4/2)이 통신-금융 정보공유 플랫폼 구축의 법적 근거를 마련한다. 탐지 데이터 공유 인프라를 선점하는 통신사가 정부 파트너십 우선권 확보 가능
- PhaaS 복구 탄력성(Tycoon2FA 사례)은 단독 차단 대신 "토큰 유효기간 단축·세션 고착 방지" 등 기술적 방어 레이어 필요성을 보여준다. 이 영역의 솔루션 개발·도입이 시급
- AiTM Device Code Phishing 대응 솔루션(토큰 바인딩, FIDO 패스키)이 ABA·BIC 권고와 맞닿아 있어 글로벌 정책 흐름과 정렬된 제품 포지셔닝 가능

**위협**
- EvilTokens가 이미 340+ 기관을 타깃했고 Gmail·Okta 확장을 예고한다. MFA 완전 우회 가능한 Device Code Phishing이 통신사 기업 고객에 대한 새 공격 벡터로 부상
- Tycoon2FA 폐쇄 후 즉각 복구 사례: 국제 공조 단속도 PhaaS 생태계를 구조적으로 제거하지 못함. 방어 전략이 "차단"에서 "지속 감지·적응"으로 전환해야 함
- AI 피싱 클릭률 450% 상승(Microsoft 보고) 및 19초당 1건(Cofense) 지표는 이메일·통화 채널 모두에서 공격 속도가 방어 응답 속도를 앞서고 있음을 의미

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Microsoft Security Blog — Threat actor abuse of AI accelerates from tool to cyberattack surface | [링크](https://www.microsoft.com/en-us/security/blog/2026/04/02/threat-actor-abuse-of-ai-accelerates-from-tool-to-cyberattack-surface/) | news | 2026-04-02 | [A] |
| <a id="ref-g-02"></a>G-02 | Help Net Security — EvilTokens ramps up device code phishing targeting Microsoft 365 users | [링크](https://www.helpnetsecurity.com/2026/03/31/eviltokens-phishing-microsoft-365/) | news | 2026-03-31 | [B] |
| <a id="ref-g-03"></a>G-03 | The Hacker News — Device Code Phishing Hits 340+ Microsoft 365 Orgs Across Five Countries via OAuth Abuse | [링크](https://thehackernews.com/2026/03/device-code-phishing-hits-340-microsoft.html) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | Microsoft Security Blog — Inside Tycoon2FA: How a leading AiTM phishing kit operated at scale | [링크](https://www.microsoft.com/en-us/security/blog/2026/03/04/inside-tycoon2fa-how-a-leading-aitm-phishing-kit-operated-at-scale/) | news | 2026-03-04 | [A] |
| <a id="ref-g-05"></a>G-05 | The Hacker News — Europol-Led Operation Takes Down Tycoon 2FA Phishing-as-a-Service Linked to 64,000 Attacks | [링크](https://thehackernews.com/2026/03/europol-led-operation-takes-down-tycoon.html) | news | 2026-03-04 | [B] |
| <a id="ref-g-06"></a>G-06 | Cofense — Cofense Report Reveals AI-Powered Phishing Accelerated to One Attack Every 19 Seconds | [링크](https://cofense.com/Blog/Cofense-Report-Reveals-AI-Powered-Phishing-Accelerated-to-One-Attack-Every-19-Seconds) | 보고서 | 2026-02 | [A] |
| <a id="ref-g-07"></a>G-07 | Microsoft Security Blog — Inside an AI‑enabled device code phishing campaign | [링크](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/) | news | 2026-04-06 | [A] |
| <a id="ref-g-08"></a>G-08 | 정책브리핑 — 보이스피싱 범죄 더 빠르고, 더 강력히 대응합니다 | [링크](https://www.korea.kr/news/policyNewsView.do?newsId=148962033&call_from=rsslink) | 공식 | 2026-04-02 | [A] |
| <a id="ref-g-09"></a>G-09 | Help Net Security — Pindrop Fraud Assist uses AI to analyze calls and strengthen fraud prevention | [링크](https://www.helpnetsecurity.com/2026/03/17/pindrop-protect-fraud-assist/) | news | 2026-03-17 | [B] |
| <a id="ref-g-10"></a>G-10 | Biometric Update — New Series B round brings Adaptive's total capital raised to $146.5 million | [링크](https://www.biometricupdate.com/202512/new-series-b-round-brings-adaptives-total-capital-raised-to-146-5-million) | news | 2025-12 | [B] |
| <a id="ref-g-11"></a>G-11 | Help Net Security — Financial groups lay out a plan to fight AI identity attacks | [링크](https://www.helpnetsecurity.com/2026/04/01/fight-ai-identity-fraud/) | news | 2026-04-01 | [B] |
| <a id="ref-g-12"></a>G-12 | Telecompaper — SKT reveals rise in AI-driven blocking of spam and voice phishing attempts | [링크](https://www.telecompaper.com/news/skt-reveals-rise-in-ai-driven-blocking-of-spam-and-voice-phishing-attempts--1558993) | news | 2026-01-13 | [B] |
| <a id="ref-g-13"></a>G-13 | The Fast Mode — KT Brings AI Voice Phishing Detection Service to Market | [링크](https://www.thefastmode.com/technology-solutions/39153-kt-unveils-real-time-ai-voice-phishing-protection) | news | 2026 | [B] |
| <a id="ref-g-14"></a>G-14 | Security Magazine — Vishing attacks increased by 442% in the second half of 2024 | [링크](https://www.securitymagazine.com/articles/101439-vishing-attacks-increased-by-442-in-the-second-half-of-2024) | news | 2025 | [B] |
| <a id="ref-g-15"></a>G-15 | Programs.com — Vishing Statistics 2026: 442% More Incidents, $40B In Losses | [링크](https://programs.com/resources/voice-phishing-stats/) | 통계 | 2026 | [C] |
| <a id="ref-p-01"></a>P-01 | PMC (NIH) — Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead (PMC11991371) | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | ACM Transactions on Internet Technology — Where are We in Audio Deepfake Detection? | [링크](https://dl.acm.org/doi/10.1145/3736765) | paper | 2026 | [A] |
