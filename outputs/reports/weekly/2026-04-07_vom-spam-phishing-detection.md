---
topic: spam-phishing-detection
date: 2026-04-07
agent: voice-of-market
videos_analyzed: 0
hn_threads_analyzed: 2
conference_sources: 4
---

## 시장 수요 시그널: 스팸/피싱 감지(통화전)

> **참고**: 2025년 이후 YouTube 컨퍼런스 트랜스크립트를 직접 추출 가능한 영상은 확인되지 않았다.
> TADSummit 2025 발표(Enrico Faccioli, vishr.ai)는 YouTube 링크가 공개되지 않은 상태이며,
> 학술/컨퍼런스 자료(AsiaCCS 2025, SIPNOC 2025, CFCA 2025)와 HN 커뮤니티 쓰레드에서
> 수요 시그널을 추출했다.

---

### 고객 페인포인트

- **탐지 기술이 공격 고도화 속도를 따라가지 못함** — 딥페이크 음성 합성이 30~60초 오디오만으로 가능해지면서, 기존 음성 인증/바이오메트릭 시스템이 AI 생성 음성을 실시간으로 걸러내지 못하는 격차가 발생하고 있다. 통화 전 탐지(pre-call screening) 보다 사후 대응에 머물러 있는 상태다. 출처: TADSummit 2025 (Enrico Faccioli, vishr.ai); MobileIDWorld 2025 보고

- **STIR/SHAKEN 인증 체계의 커버리지 공백** — Tier-1 통신사 간 A등급 서명율이 90%를 초과했음에도, 레거시 TDM 인프라를 사용하는 소형 통신사 구간에서 파라미터가 소실된다. 사기꾼이 이 공백 구간을 경유 경로로 활용하면서 인증 기반 탐지가 무력화된다. 출처: TNS Top Five Voice Security Takeaways 2025

- **다중 채널 복합 공격으로 단일 탐지 레이어가 우회됨** — 문자로 신뢰를 형성한 뒤 전화로 유인하는 멀티벡터 공격이 급증(2024년 하반기 vishing 442% 증가)했다. 통화 단독 분석만으로는 공격 의도를 사전에 파악하기 어렵다. 출처: TNS 2025; TADSummit Social Engineering 세션 (Matt Holland, vishr.ai, 2025-07)

- **경보 신뢰도 문제 — 사용자 무시(alert fatigue)** — 캐리어/OS 레벨의 "스팸 의심" 경고가 과도하게 발생하거나 정상 전화를 차단하는 오탐(false positive)으로 인해, 사용자들이 경고를 무시하는 습관이 형성됨. HN 실무자 댓글: "Do you trust Google saying 'this might be a scam' over a person on the phone assuring you there is some urgent need?" 특히 고령층은 기기 경고보다 사람 목소리를 신뢰한다. 출처: HN 쓰레드 (item#43768100, 2025)

- **발신번호 스푸핑 차단 불가** — 전화망 표준에서 "누구든 어떤 번호로도 발신자 표시 변조 가능"하며, 이를 근본적으로 차단하는 네트워크 수준 인증 인프라가 없다. 로컬 지역번호로 스푸핑된 번호에 대한 지리적 필터링도 무력화된다. 출처: HN 쓰레드 (item#43768100, 2025)

---

### 도입 장벽

- **소형 통신사의 인프라 현대화 비용** — SIP/IP 망 전환에 필요한 투자를 감당하지 못하는 Tier-2/3 통신사들이 TDM 레거시를 유지하면서 STIR/SHAKEN 커버리지 공백을 만들고 있다. 이 구간이 스팸/피싱 트래픽의 경유지로 악용된다. 출처: TNS Voice Security 2025

- **KYC(Know Your Customer) 집행 불균형** — 일부 통신사/MVNO가 느슨한 KYC를 유지하면서 사기 발신자가 합법적 번호 풀을 확보하는 온램프 역할을 한다. 산업 전체 집행 체계 부재. 출처: TNS Voice Security 2025

- **크로스보더 관할권 문제** — 스캠 콜센터가 동남아·동유럽에 집중되어 있어 국내 차단 조치가 실효성을 잃는다. UN 보고서(2025)는 글로벌 스캠 콜센터가 '전염병 수준'으로 확산 중이라 지적. 국가간 조약 수준의 공조 없이는 발신원 차단이 불가능하다. 출처: HN 쓰레드 (item#43768100 — UN scam call centers); TNS 2025

- **다계층 통합의 기술적 복잡도** — 디바이스 레벨 스크리닝 + 네트워크 레벨 탐지 + AI 분석 엔진을 동시에 연동해야 실효성 있는 통화전 탐지가 가능한데, 세 레이어의 인프라 투자와 실시간 연동 구현이 요구된다. 출처: MobileIDWorld 2025

- **AI 공격 도구의 저비용 접근성** — AsiaCCS 2025 발표(Sounds Vishy, Figueiredo et al.)에 따르면, 공개된 LLM + TTS 파이프라인만으로 자율 vishing 봇(ViKing) 구성이 가능하며 240명 피험자 대상 실험에서 상당수가 민감정보를 노출했다. 공격 도구의 접근성이 방어 도구보다 빠르게 낮아지고 있다. 출처: ACM AsiaCCS 2025 "Sounds Vishy" (Figueiredo et al., INESC-ID/IST Lisbon)

- **OS/플랫폼 간 탐지 격차** — iOS와 Android 간 스팸 탐지 성능 차이가 실무자 수준에서 명확히 인지됨. HN 댓글: "I just switched to iPhone from Google and I get way more spam now." 서드파티 앱이 OS 레벨 통화 데이터에 접근할 수 없어 보완 탐지 솔루션 개발도 제약된다. 출처: HN 쓰레드 (item#31070141)

---

### 시장 니즈

- **통화전(pre-call) 실시간 AI 탐지 엔진** — 착신 전 수 초 내에 음성 특징·발신 패턴·네트워크 메타데이터를 복합 분석하는 탐지 엔진 수요. Pindrop이 2016년 Black Hat에서 발표한 "초 단위 fingerprinting" 접근법이 기술 방향성을 제시하나, AI 생성 음성에 대한 대응은 별도 R&D가 필요하다. 출처: Black Hat "Call Me: Gathering Threat Intelligence on Telephony Scams" (Pindrop, 2016—기술 방향 참고); MobileIDWorld 2025

- **산업 전체 실시간 위협 인텔리전스 공유 플랫폼** — 개별 통신사가 탐지한 스캠 패턴을 업계 전반에 실시간 공유하는 협력 체계. 현재는 각 통신사가 독립적으로 운영하여 신규 공격 패턴 전파가 늦다. 출처: TNS Voice Security 2025; Fast Company 보도

- **STIR/SHAKEN 이후 차세대 인증 계층** — 서명율 90%를 달성한 이후에도 잔존하는 공백(TDM 구간, 소형 통신사)을 메울 Rich Call Data (RCD), CNAM 보완, 또는 AI 기반 발신자 행동 분석 등 대안 인증 레이어 수요. 출처: TNS Voice Security 2025; FCC FACT SHEET (2025-10, Call Branding FNPRM)

- **OS 레벨 API 개방** — 서드파티 스팸 탐지 앱이 통화 메타데이터에 접근할 수 있도록 OS 수준의 훅(hook) 제공 요구. 현재 iOS 등에서 서드파티 접근이 제한되어 탐지 생태계 발전을 저해. 출처: HN 쓰레드 (item#43768100)

- **vishing 시뮬레이션 및 임직원 교육 자동화** — 기업 환경에서 AI 음성 공격에 대한 실전형 훈련 수요 급증. 기존 동영상/퀴즈 방식 보안 교육은 "체크박스 문화"만 양산하며 실제 방어력 형성에 실패. 1:1 AI 코칭 기반의 실시간 시뮬레이션 플랫폼으로의 전환 요구. 출처: TADSummit 2025 (Enrico Faccioli, vishr.ai)

---

### 분석 소스

| 소스 | 제목 | 유형 | 날짜 |
|------|------|------|------|
| Enrico Faccioli (vishr.ai) | Cybersecurity Training in the Age of Voice AI | TADSummit 2025 컨퍼런스 | 2025-07 |
| Matt Holland & Enrico Faccioli (vishr.ai) | Social Engineering | TADSummit 2025 컨퍼런스 | 2025-07 |
| Figueiredo et al. (INESC-ID/IST) | Sounds Vishy: Automating Vishing Attacks with AI-Powered Systems | ACM AsiaCCS 2025 논문 | 2025-08 |
| TNS (Transaction Network Services) | Top Five Voice Security Takeaways in 2025 | 업계 보고서 | 2025 |
| MobileIDWorld | Phone Networks Deploy AI-Powered Scam Call Prevention Systems in 2025 | 업계 기사 | 2025 |
| HN 커뮤니티 | UN says scam call centers are epidemic (item#43768100) | HN 쓰레드 | 2025 |
| HN 커뮤니티 | Americans are drowning in spam (item#31070141) | HN 쓰레드 | 2022 |

---

### 참고: YouTube 영상 탐지 결과

2025년 이후 발행된 스팸/피싱 감지(통화전) 관련 컨퍼런스 YouTube 영상은 공개 색인에서 확인되지 않았다.

- TADSummit 2025 발표(Enrico Faccioli): 블로그 포스트만 공개, YouTube URL 미공개
- SIPNOC 2025 "Current Developments in AI for Spam Detection": YouTube 녹화본 미공개
- Black Hat telephony fraud 발표: 2016년 자료 (검색 결과에서 최신 것으로 오인)
- IEEE S&P 2025 robocall 연구: 학술 논문, 영상 미공개

향후 TADSummit YouTube 채널(youtube.com/@TADSummit) 또는 SIPNOC SIP Forum 채널에서 영상 공개 여부를 재확인하는 것을 권장한다.
