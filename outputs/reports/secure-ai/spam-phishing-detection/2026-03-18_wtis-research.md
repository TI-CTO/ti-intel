---
type: wtis-research
topic: spam-phishing-detection
domain: secure-ai
l2_topic: spam-phishing
date: 2026-03-18
parent: 2026-03-18_wtis-spam-phishing-detection
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, prior_reports]
mcp_status: "MCP 도구 미작동 (VSCode 확장 환경 제약) — WebSearch 폴백. 총 14회 검색, 45건 출처 확보."
prior_analysis:
  date: 2026-03-03
  score: 120/200
  verdict: Conditional Go
  key_risk: "Samsung S26 자체 탐지 — Critical Risk"
---

# WTIS 심층 리서치: 스팸/피싱 감지 (통화전)

## Executive Summary

> 이번 분석은 2026년 3월 기준으로 급격히 재편된 통화 보안 생태계를 다룬다. **핵심 발견 5가지**: (1) Scam-as-a-Service 진입장벽이 붕괴되었다 — Vishing-as-a-Service 플랫폼이 월 $399에 ElevenLabs TTS를 활용한 자동화된 보이스피싱을 제공하면서 공격 규모가 비선형적으로 확대된다 [[G-01]](#ref-g-01). (2) 플랫폼 거인들이 독립적으로 탐지 레이어를 구축하고 있다 — Meta (WhatsApp/FB/Messenger), Microsoft Teams, Samsung Galaxy S26이 3월 한 달 사이 동시 배포되었다 [[G-04]](#ref-g-04)[[G-05]](#ref-g-05)[[G-06]](#ref-g-06). (3) 국내 통신사 격차가 명확해졌다 — KT "Circuit Breaker" 시스템이 경찰청 연계로 1만 개 번호 차단 및 보이스피싱 신고 25% 감소를 달성하며 SKT를 기술 리더로 역전할 가능성을 보인다 [[G-08]](#ref-g-08). (4) 한국 보이스피싱 피해는 2025년 1~10월 1조 567억원을 돌파하며 사상 최초로 연간 1조원을 넘어섰다 [[G-14]](#ref-g-14). (5) 딥페이크 탐지 정확도는 실사용 환경에서 여전히 불안정하며, Hiya 조사 기준 미국인 25%가 딥페이크 통화를 수신했으나 통신사는 사기범 대비 2:1로 열세이다 [[G-16]](#ref-g-16). **전략적 함의**: 이전 분석(2026-03-03)의 "Samsung Critical Risk" 판단은 유효하나, 위협이 단말 제조사만이 아닌 플랫폼-통신사-규제 삼각축에서 동시에 압박해 오는 구조로 전환 중이다.

---

## 연구 질문

> 2026년 3월 기준 스팸/피싱 감지(통화전) 기술의 성숙도와 시장 환경은 어떻게 변화했는가? 특히 (Q1) Vishing-as-a-Service 등 신규 위협이 시장 구조에 미치는 영향, (Q2) Samsung Galaxy S26 · Meta · Microsoft Teams 동시 배포의 경쟁 지형 변화, (Q3) KT Circuit Breaker와 SKT ScamVanguard의 격차 현황, (Q4) 한국 보이스피싱 피해 최신 통계, (Q5) C2PA/STIR-SHAKEN 이후 규제 표준의 실질적 효과를 파악한다. 이전 분석(2026-03-03) 대비 달라진 것에 집중하며 동일 결론을 반복하지 않는다.

---

## 1. 시장 분석

### TAM/SAM/SOM

**글로벌 시장 규모 (복수 기관 교차 검증)**

| 시장 세그먼트 | 2025 추정 | 2030 예측 | CAGR | 출처 |
|-------------|-----------|-----------|------|------|
| Fraud Detection & Prevention (광의) | $32.0B | $65.7B | 15.5% | [[G-20]](#ref-g-20) |
| Fraud Detection & Prevention (협의) | $33.1B | $90.1B | 18.7% | [[G-21]](#ref-g-21) |
| Phishing Protection Market | $3.2B (2026) | $7.3B (2032) | 13.2% | [[G-22]](#ref-g-22) |
| Robocall Mitigation & Branded Calling | $5.6B | $21.1B (2035) | 14.2% | [[G-25]](#ref-g-25) |
| Mobile Phishing Protection | N/A | N/A | 19.6% | [[G-23]](#ref-g-23) |

> [B] 시장 규모 교차 검증: Fraud Detection 광의 시장 $32~33B (2개 기관 일치, 오차 3% 이내), Phishing Protection $3.2B (단일 기관). Robocall Mitigation $5.6B이 스팸/피싱 감지 SAM에 가장 근접한 세그먼트.

**한국 시장 추정 (SAM)**

- 한국 이동통신 가입자: 5,724만 회선 (휴대폰 기준) [[G-02]](#ref-g-02)
- 보이스피싱 피해 규모를 경제적 손실 TAM으로 보면: 2025년 연간 피해액 **1조 567억원 이상** [[G-14]](#ref-g-14) → 예방 시장의 기회비용
- 통신사 부가서비스 ARPU 프리미엄: 국내 통신사들은 보이스피싱 탐지 서비스를 현재 무료(앱 기반)로 제공 중. 유료 전환 시 월 1,000~3,000원 가정 시 연간 수백억 원 규모 [D, 자체 추정]

### 연도별 시장 전망

**Vishing 위협 증가 추이 [복수 출처 일치]:**
- 보이스피싱(vishing) 공격 건수: 전년 대비 **442% 증가** [[G-24]](#ref-g-24)
- SKT가 2025년 차단한 보이스피싱/스팸 시도: **11억 건** (+35% YoY) [[G-10]](#ref-g-10)
  - 이 중 음성 스팸·보이스피싱 통화 **+119% 증가, 2억 5천만 건** [[G-11]](#ref-g-11)
- Hiya 조사 (2026.03): 미국인 **25%** 가 딥페이크 음성 통화 수신 경험, **24%** 는 구분 불가 [[G-16]](#ref-g-16)

### 한국 보이스피싱 피해 통계

**2025년 최신 통계 [A/B급]:**

| 기간 | 피해액 | 비고 | 출처 |
|------|--------|------|------|
| 2024년 연간 | 8,545억원 | 2023년(4,472억) 대비 +91% | [[G-02]](#ref-g-02) |
| 2025년 Q1 | 3,116억원 | 전년 동기 대비 건수 +17%, 피해액 2배 이상 | [[G-15]](#ref-g-15) |
| 2025년 상반기 | 6,000억원+ | 전년 상반기(3,243억) 대비 급증 | [[G-14]](#ref-g-14) |
| 2025년 1~10월 | **1조 567억원** | 사상 최초 연간 1조 돌파 (10월까지) | [[G-14]](#ref-g-14) |
| 2025년 10월 이후 | 4개월 연속 감소 | 2025.08 정부 종합대책 효과 | [[G-26]](#ref-g-26) |
| 1인당 평균 피해액 | 5,290만원 | 2025년 1~10월 경찰청 국수본 기준 | [[G-02]](#ref-g-02) |

- 가상화폐 보이스피싱 7개월 간 **+660% 급증** [[G-14]](#ref-g-14)
- 2025년 10월부터 4개월 연속 감소: 2025.08 정부 종합대책 이후 AI 탐지 + 경찰-통신사 연계 효과로 분석 [[G-26]](#ref-g-26)

---

## 2. 기술 성숙도

### TRL 현황

**AI 기반 Pre-Call 스팸/피싱 탐지 TRL 매핑:**

| 기술 영역 | TRL | 근거 | 대표 사례 |
|----------|-----|------|---------|
| 번호 기반 스팸 필터링 (발신번호 블랙리스트) | TRL 9 | 상용 완성, 전국 적용 중 | SKT ScamVanguard, KT Circuit Breaker |
| AI 통화 패턴 분석 (Pre-Call) | TRL 7~8 | 국내 3사 상용화, 성능 검증 진행 중 | KT Who Who 2.0, SKT 에이닷 |
| 딥페이크 음성 탐지 (통화 중/전) | TRL 6~7 | 상용화 일부. 실사용 환경 정확도 불안정 | LGU+ Anti-DeepVoice, KT Deep Voice |
| On-Device AI 탐지 (스마트폰) | TRL 7~8 | Galaxy S26 등 다수 배포 시작 | Samsung Galaxy S26, Pixel 9 |
| VoIP Pre-Call 브랜드 가장 탐지 | TRL 7 | MS Teams 3월 배포. 초기 상용화 | Microsoft Teams BIP |
| C2PA 음성 프로비넌스 인증 | TRL 4~5 | 표준 확산 중, 전화 통화 적용은 초기 | C2PA 콘소시엄 |

> 이전 분석(2026-03-03) 대비 변화: On-Device AI 탐지가 Samsung Galaxy S26 배포로 TRL 7→8 상향 조정. VoIP Pre-Call 탐지가 MS Teams 배포로 신규 TRL 7 등재.

### 탐지 정확도 벤치마크

**주요 사업자 탐지 정확도 비교:**

| 사업자/제품 | 탐지 정확도 | 측정 조건 | 출처 |
|-----------|------------|---------|------|
| KT AI 탐지 서비스 v1 | 90.3% | 2025 Q1, 1,528건 중 의심 탐지 | [[G-08]](#ref-g-08) |
| KT AI 탐지 서비스 v2 | **97.2%** | 2025 Q4, 연속 업그레이드 후 | [[G-08]](#ref-g-08) |
| KT 2.0 목표 | 연간 95%+ | KT 공식 발표 목표 | [[G-09]](#ref-g-09) |
| McAfee Deepfake Detector | 96% | 내부 벤치마크, ~200,000 샘플 학습 | [[G-28]](#ref-g-28) |
| Aurigin Apollo | 97.7% (EER 2.3%) | 3초 오디오, <50ms 지연 | [[G-29]](#ref-g-29) |
| Samsung Galaxy S26 (영어) | ~95% | 데모 환경 비공식 측정 | [[G-06]](#ref-g-06) |
| SKT ScamVanguard | 공개 정보 없음 | 차단 건수는 공개, 정확도 미공개 | [[G-10]](#ref-g-10) |

> [C] 독립 제3자 벤치마크 부재. 모든 수치는 사업자 발표 또는 언론 보도 기반. 실사용 환경(통화 채널 압축, 배경소음) 성능은 연구실 대비 유의미하게 하락할 수 있다 [[G-29]](#ref-g-29).

**딥페이크 오디오 탐지 학술 한계 [A]:**
- 2025년 연구: 데이터셋의 비현실성으로 인한 shortcut learning 문제. 통화 채널 노이즈를 반영한 실환경 벤치마크는 연구실 대비 성능이 크게 하락 [[G-29]](#ref-g-29).
- 실시간 WebRTC 스트림 저지연 탐지 연구는 2025년 기준 극히 소수 [[G-29]](#ref-g-29).
- 딥페이크 오디오 탐지 정확도 개선: 현실적 데이터 가이드라인 적용 시 **실험실 +39%, 실환경 벤치마크 +57%** [[G-29]](#ref-g-29).

### 핵심 기술 진전 (이전 대비 변화)

**이전 분석(2026-03-03)으로부터의 Delta:**

| 항목 | 이전 (2026-03-03) | 현재 (2026-03-18) | 중요도 |
|------|-----------------|-----------------|--------|
| Samsung S26 탐지 범위 | 한국어 탐지 (국과수 데이터) + 영어 Gemini (미국) | 확인 유지. Call Screening 13개 언어(한국어 포함), Scam Detection은 영어-미국 한정 [[G-06]](#ref-g-06) | 유지 |
| Vishing-as-a-Service | 언급 없음 | $399/월 플랫폼 등장, ElevenLabs 음성 15종 제공 [[G-01]](#ref-g-01) | **신규 Critical** |
| VoIP Pre-Call 탐지 | 부재 | MS Teams BIP 3월 배포 완료 [[G-04]](#ref-g-04) | **신규 신호** |
| 플랫폼 AI 탐지 | Meta 계획 단계 | Meta 3사(WhatsApp/FB/Messenger) 동시 배포 [[G-05]](#ref-g-05) | **신규 신호** |
| KT 탐지 정확도 | 90.3% (v1) | 97.2% (v2, Q4 2025) [[G-08]](#ref-g-08) | 상향 |
| KT-경찰청 연계 | 미확인 | Circuit Breaker 가동, 1만 번호 차단, 신고 25% 감소 [[G-08]](#ref-g-08) | **신규** |
| C2PA 표준 | 논의 단계 | 2026년 주요 인프라로 부상. 단, 전화 채널 적용은 미검증 [[G-31]](#ref-g-31) | 진전 |
| LGU+ 익시오 | 5,500건 탐지 | 월 2,000건 탐지, 악성 앱 서버 800개, 3만 3천명 경찰 이관. MWC 2026 익시오 프로 발표 | 성과 확인 |

---

## 3. 경쟁 환경

### 국내 플레이어 (SKT/KT/LGU+/Samsung)

**국내 주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| SKT | ScamVanguard: 2025년 11억 건 차단 (+35% YoY), 음성 통화 250만건 (+119%). 4개 AI 기능: AI 미끼 문자 탐지, 피싱 채팅 탐지, 음성피싱 패턴 분석, 실명 분석 AI. 정확도는 공개 안 됨 | [[G-10]](#ref-g-10), [[G-11]](#ref-g-11) |
| KT | Who Who 2.0 + Circuit Breaker 가동(2026.01). 탐지 정확도 90.3%→97.2%. 경찰청 연계로 1만 번호 차단, 보이스피싱 신고 25% 감소. 국과수 성문DB + 딥보이스 3중 탐지. 피해 예방 목표 연 2,000억원 | [[G-08]](#ref-g-08), [[G-09]](#ref-g-09), [[G-18]](#ref-g-18) |
| LG U+ | 익시오(ixi-O) 프로: 세계 최초 온디바이스 Anti-DeepVoice 탑재. 3,000시간/200만 건 학습. 월 2,000건 탐지, 악성 앱 서버 800개 추적, KB국민은행 연계 이상거래 감지. MWC 2026 공개 | [[G-17]](#ref-g-17) |
| Samsung | Galaxy S26: Google Scam Detection(Gemini Nano, 영어·미국) + 자체 Call Screening(13개 언어, 한국어 포함). 경찰청·국과수 3만건 학습 데이터 활용 온디바이스 탐지. S26 이전 전 갤럭시 무료 제공 | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07) |

**Samsung 내장 탐지 위협 심화 분석:**

이전 분석(2026-03-03)에서 "Critical Risk"로 분류된 Samsung Galaxy S26 자체 탐지 위협은 이번 분석에서 **다층 위협으로 진화**했다:

1. **Gemini Nano 통합**: Google Scam Detection이 Samsung Phone 앱에 직접 통합. 별도 앱 불필요 [[G-06]](#ref-g-06).
2. **언어 범위**: Call Screening은 한국어 포함 13개 언어 지원. Gemini 기반은 영어 미국 한정 [[G-06]](#ref-g-06).
3. **기어링 확대 가능성**: 현재 영어-미국 한정인 Gemini Scam Detection이 한국어로 확장될 경우, 통신사 탐지 앱의 설치 유인이 대폭 감소.
4. **무료 제공**: 별도 과금 없음. 통신사 유료화 전략에 직접 위협 [[G-07]](#ref-g-07).

### 글로벌 플레이어

**글로벌 주요 플레이어 동향**

| 기업 | 동향 | 출처 |
|------|------|------|
| Microsoft | Teams BIP(Brand Impersonation Protection): 2026년 3월 중순 배포 완료. 외부 첫 연락 VoIP 통화에 대한 Pre-Call 브랜드 가장 탐지. 기본 활성화. | [[G-04]](#ref-g-04) |
| Meta | WhatsApp/Facebook/Messenger 동시 AI 스캠 탐지 배포(2026.03.11). 2025년 스캠 광고 1억 5,900만건 92% 선제 차단. 15만개 스캠 센터 계정 비활성화 | [[G-05]](#ref-g-05) |
| Hiya | State of the Call 2026(2026.03): 55,000만 사용자 보호. 통신사 2:1 열세. 소비자 38%가 MNO 대응 미흡 시 이탈 의향. | [[G-16]](#ref-g-16) |
| Adaptive Security | Series B $81M 조달(2024.12, Bain Capital Ventures). 누적 $136M. OpenAI Fund 투자. 딥페이크 음성 시뮬레이션 + 기업 보안 인식 훈련. 500+ 기업 고객(PayPal, Xerox 등) | [[G-30]](#ref-g-30) |
| McAfee | Deepfake Detector 96% 정확도. Lenovo AI PC 기본 탑재. 텍스트 스캠 탐지 >99% 정확도. 200,000 샘플 학습. 전체 Core Plan 포함 (추가 비용 없음) | [[G-28]](#ref-g-28) |
| Truecaller | 4.5억 사용자, 2025년 77억건 사기 통화 식별. 인도 CNAP 도입(2026.03)으로 경쟁 압박. EBITDA -49% YoY (2025 Q4), 광고 수익 -31% | [[G-32]](#ref-g-32) |

### Gap Analysis

**탐지 레이어별 커버리지 공백:**

| 탐지 레이어 | 현재 커버 주체 | 공백 |
|-----------|-------------|------|
| 번호 기반 Pre-Call 차단 | SKT, KT, LGU+, Hiya, Truecaller | 국가 간 로밍, VoIP 번호 스푸핑 |
| 딥페이크 음성 실시간 탐지 | LGU+ (온디바이스), KT (통화 중) | 3초 미만 초단시간 통화 탐지 |
| VoIP/메시지 Pre-Call 브랜드 가장 | MS Teams, Meta | 일반 PSTN 전화 미커버 |
| C2PA 음성 프로비넌스 | 파일럿 단계 | 실시간 통화에 미적용 |
| 고령자·취약계층 맞춤 보호 | 정부 공동 플랫폼 (2026-2027) | 서비스 설계·전달 방식 미성숙 |

---

## 4. 제품/서비스 스펙 비교

**국내 통신사 Pre-Call 탐지 스펙 비교**

| 기업 | 탐지 정확도 | 처리 방식 | 가격(정책) | 출처 |
|------|-----------|---------|-----------|------|
| SKT (ScamVanguard) | 공개 정보 없음 | 클라우드+온디바이스 혼합 | 무료 (에이닷 앱) | [[G-10]](#ref-g-10) |
| KT (Who Who 2.0) | 97.2% (Q4 2025) | 국과수 성문DB + 딥보이스 3중 | 무료 (Who Who 앱) | [[G-08]](#ref-g-08) |
| LG U+ (ixi-O) | 공개 정보 없음 | 온디바이스 우선 | 무료 (이용약관 동의 필요) | [[G-17]](#ref-g-17) |
| Samsung (Galaxy S26) | ~95% (비공식) | 온디바이스 (Gemini Nano) | 무료 (기본 탑재) | [[G-06]](#ref-g-06) |

---

## 5. 학술 동향

**주요 논문**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead" (PMC, 2025) | 기존 데이터셋이 비현실적이며 shortcut learning 문제 심각. 통화 채널 노이즈 반영 시 성능 대폭 하락. | [[G-29]](#ref-g-29) |
| "On Deepfake Voice Detection – It's All in the Presentation" (arXiv 2509.26471, 2025) | 발표 조건(통화 채널, 압축, 재생)이 탐지 성능에 결정적. 실환경 벤치마크 39~57% 개선 가능. | [[P-01]](#ref-p-01) |
| "Where are We in Audio Deepfake Detection?" (ACM TOIT, 2025) | 생성 모델과 탐지 모델 간의 Arms race 분석. 합성 음성 품질 향상 속도가 탐지 기술을 앞서는 추세. | [[P-02]](#ref-p-02) |
| "DeepDetection: Privacy-Enhanced Deep Voice Detection" (MDPI, 2022) | 온디바이스 딥보이스 탐지 + 사용자 인증 결합 프레임워크. LGU+ Anti-DeepVoice 설계 참조 가능성. | [[P-03]](#ref-p-03) |

---

## 6. 특허 동향

> [주의] MCP intel-store 특허 수집 도구 미작동 환경으로 WebSearch 기반 정보 제한적. 특허 세부 청구항 데이터 공백. 추후 intel-store 정상 환경에서 보완 필요.

**주요 특허 출원 동향 (공개 정보 기반):**

- **Samsung**: Galaxy 시리즈 온디바이스 AI 탐지 관련 특허 다수. 경찰청·국과수 학습 데이터 활용 방법론 특허화 가능성 높음 [D, 단일 소스].
- **SKT**: ScamVanguard 음성 패턴 분석 + 실명 분석 AI 관련 특허 출원 예상. 구체적 출원 번호 확인 불가 [D].
- **KT**: Circuit Breaker 시스템의 AI 기반 번호 자동 식별 방법론. Who Who 앱 화자인식 특허 [[G-09]](#ref-g-09).
- **Microsoft**: Teams BIP 관련 브랜드 가장 탐지 알고리즘 특허 (기존 M365 보안 특허 포트폴리오 확장) [C].

---

## 7. 기업 발언 & 보도자료

**E-xx 기업 발언 직접 인용**

- **SKT (2026.01.13, 아시아경제)**: "SK텔레콤은 지난해 AI로 110억 건 이상의 통신 사기 시도를 최초 필터링했다. 전년 대비 35% 증가한 수치" [[E-01]](#ref-e-01)

- **KT (2026.03.16, 서울경제)**: "KT와 경찰청 통합신고대응팀이 함께 운영하는 'Circuit Breaker' 시스템을 통해 의심 피싱 번호 1만개를 차단했고, 보이스피싱 신고가 25% 감소했다" [[E-02]](#ref-e-02)

- **KT AI 탐지 서비스 2.0 출시 발언 (2025.07.29, Financial News)**: "KT는 AI 음성 피싱 탐지 서비스 2.0을 통해 연간 탐지 정확도 95% 이상, 피해 2,000억원 이상 예방을 목표로 한다. 서비스 2.0은 국과수 성문 DB를 활용해 범죄 음성을 식별하고 딥보이스 탐지 기술을 3중으로 적용한다" [[E-03]](#ref-e-03)

- **Hiya (2026.03.02, Martech Series)**: "State of the Call 2026에 따르면 소비자의 38%가 MNO들이 AI 사기에 충분히 대응하지 못할 경우 통신사를 전환할 의향이 있다고 답했다. 통신사는 사기범 대비 2대 1로 열세" [[E-04]](#ref-e-04)

- **Meta (2026.03.11, about.fb.com)**: "Meta는 WhatsApp, Facebook, Messenger에 새로운 AI 기반 스캠 탐지 도구를 배포한다. 2025년 정책 위반 스캠 광고 1억 5,900만건을 삭제했으며 92%는 신고 전에 선제 차단했다" [[E-05]](#ref-e-05)

- **Microsoft (2026.03, BleepingComputer)**: "Teams 브랜드 가장 방지 기능(BIP)은 3월 중순부터 배포를 시작해 3월 말 완료 예정이다. 외부 발신자가 신뢰받는 조직으로 위장하는 소셜 엔지니어링 공격을 차단하며 기본 활성화된다" [[E-06]](#ref-e-06)

- **Mirage Security (2026.03.11, Help Net Security)**: "Vishing-as-a-Service 플랫폼 'p1bot'이 ElevenLabs TTS를 오용해 'press 1' 스캠을 자동화한다. 영어 15종, 프랑스어·스페인어 각 4종의 음성 ID가 하드코딩되어 있으며, 월 $399부터 시작하는 구독 모델로 운영된다" [[E-07]](#ref-e-07)

---

## 8. 규제·정책 동향

### 미국 규제

**FCC AI 음성 로보콜 TCPA 규정 [A]:**
- FCC (2024.02): AI 생성 음성을 사용한 로보콜이 TCPA (Telephone Consumer Protection Act) 상 "인공 또는 사전 녹음 음성"에 해당한다고 명시적 선언 [[G-33]](#ref-g-33).
- AI 클론 음성·딥페이크 음성도 TCPA 적용 대상. 사전 동의 없는 AI 음성 로보콜 금지 [[G-33]](#ref-g-33).
- 위반 시 과태료, 금지 명령, 손해배상 소송 가능. FCC는 대응하지 않는 통신사에 대한 제재도 가능 [[G-33]](#ref-g-33).

**STIR/SHAKEN 한계 [B]:**
- 발신번호 스푸핑 방지에 효과적이나 딥페이크 음성 자체는 탐지 불가 [[G-31]](#ref-g-31).
- 국제 통화, VoIP 구형 인프라 환경에서 한계 명확 [[G-31]](#ref-g-31).

### 한국 규제

**보이스피싱 방지 정부 종합대책 (2025.08) [B]:**
- 2025년 8월 정부 종합대책 수립 이후 4개월 연속 피해 감소 [[G-26]](#ref-g-26).
- AI 기반 음성피싱 통신서비스 공동대응 플랫폼 구축 사업 발주 (2026~2027년): 경찰청 + KISA 협력, 실시간 데이터 수집·분석·공유 [[G-34]](#ref-g-34).

**AI 법 & 콘텐츠 레이블링 [B]:**
- 한국 AI 법: 2026년 1월 시행. AI 생성 콘텐츠 레이블링 의무화 포함. 음성 딥페이크 콘텐츠 식별 기반 마련 [[G-35]](#ref-g-35).

### C2PA 콘텐츠 인증 표준 [B]

- C2PA (Coalition for Content Provenance and Authenticity) 표준이 2026년 미디어 검증 인프라로 부상 [[G-31]](#ref-g-31).
- 합법적 오디오 스트림에 암호화 서명 삽입 → "인증된 인간" 배지 표시 가능.
- 단, 실시간 전화 통화 채널에 C2PA 적용은 기술·표준 측면 모두 미성숙 단계 [C].

---

## 9. 전략적 시사점

### 이전 분석 대비 핵심 변화

**신규 위협 (2026-03-18 기준 이전 분석 부재):**

- **Vishing-as-a-Service 진입장벽 붕괴**: 월 $399로 누구나 대규모 보이스피싱 캠페인 실행 가능. 공격 규모의 비선형적 확대 예상 [[E-07]](#ref-e-07).
- **플랫폼 독자 보안 레이어**: Meta(3개 플랫폼), Microsoft Teams가 독자적 탐지 시스템 배포. 이제 위협은 단말 제조사(Samsung)만이 아닌 플랫폼-단말-통신사 3중 압박.
- **KT Circuit Breaker**: 경찰청 연계 실시간 번호 차단이 의미 있는 효과(신고 25% 감소)를 보이며 SKT 대비 KT의 기술 포지셔닝이 역전 가능성 시사.

**지속 위협 (이전 분석 확인):**

- Samsung Galaxy S26 무료 탑재 위협: 유지 (Critical Risk 등급).
- 딥페이크 탐지 Arms Race: 탐지 속도 vs. 합성 음성 고도화 속도, 합성 측이 앞서는 추세 [[P-02]](#ref-p-02).

### 기회

- **통신사-경찰청 데이터 연계의 우위**: KT Circuit Breaker 사례처럼 정부 DB와 결합한 탐지 시스템은 단말 또는 플랫폼 독자 솔루션이 복제하기 어려운 강점.
- **고령자·취약계층 특화**: 플랫폼 AI 탐지(Meta, MS)는 디지털 채널에 집중. PSTN 기반 고령자 대상 탐지는 여전히 통신사만이 커버 가능.
- **가상화폐 보이스피싱 급증 대응**: +660% 증가한 가상화폐 관련 피싱은 은행 연계 이상거래 감지와 통화 탐지를 결합한 크로스 채널 솔루션 수요를 창출.

### 위협

- **공격 규모 폭증**: Vishing-as-a-Service로 공격 자동화→탐지 시스템의 False Negative 절대량 증가 [[E-07]](#ref-e-07).
- **플랫폼 내재화**: Meta·Microsoft·Samsung이 독자 탐지를 강화할수록 통신사 솔루션의 차별화 포인트 축소.
- **딥페이크 품질 향상**: 탐지 정확도(97%) 개선 속도를 딥페이크 합성 품질이 앞지르는 Arms Race 구조 [[P-02]](#ref-p-02).
- **개인정보보호 규제**: 온디바이스 처리는 강점이나, 클라우드 기반 분석 고도화 시 개인정보 이슈.

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- 한국 보이스피싱 피해 통계 (경찰청/금감원, 복수 언론 확인)
- KT 탐지 정확도 수치 (기업 공식 발표 + 언론)
- FCC TCPA AI 음성 규정 (공식 규정 문서)
- SKT 차단 건수 1.1억건 (기업 보도자료)
- Meta/MS Teams 배포 사실 (공식 발표 + 다수 언론)

**추가 검증 필요 [C/D]:**
- Samsung Galaxy S26 탐지 정확도 "~95%" (데모 환경, 독립 벤치마크 없음) [C]
- 통신사 부가서비스 ARPU 프리미엄 추정 (자체 추정) [D]
- Vishing-as-a-Service "$399/월" 가격 (단일 보안 연구 소스) [C]
- 특허 동향 전반 (MCP 미작동으로 공개 정보 제한적) [D]

**데이터 공백:**
- SKT ScamVanguard 탐지 정확도 (미공개)
- 국내 통신사 보이스피싱 탐지 서비스 유료화 가능성 및 ARPU 영향
- C2PA 전화 채널 적용 로드맵
- MCP intel-store 특허 데이터 (환경 제약으로 수집 불가)

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Mirage Security — Vishing-as-a-Service p1bot 플랫폼 발견 | [링크](https://www.helpnetsecurity.com/2026/03/11/researchers-uncover-ai-powered-vishing-platform/) | news | 2026-03-11 | [B] |
| <a id="ref-g-02"></a>G-02 | 더시사법률/경찰청 — 2025 보이스피싱 통계(1인당 5,290만원) | [링크](https://www.koreaherald.com/article/10631333) | news | 2025-11 | [B] |
| <a id="ref-g-03"></a>G-03 | Korea Herald — 2025 보이스피싱 피해 1조원 돌파 | [링크](https://www.koreaherald.com/article/10631333) | news | 2025-11 | [B] |
| <a id="ref-g-04"></a>G-04 | BleepingComputer — Microsoft Teams BIP 배포 | [링크](https://www.bleepingcomputer.com/news/microsoft/microsoft-teams-to-add-brand-impersonation-warnings-to-calls/) | news | 2026-03 | [B] |
| <a id="ref-g-05"></a>G-05 | TechCrunch — Meta AI 스캠 탐지 배포 | [링크](https://techcrunch.com/2026/03/11/meta-rolls-out-new-scam-detection-tools-to-facebook-whatsapp-and-messenger/) | news | 2026-03-11 | [B] |
| <a id="ref-g-06"></a>G-06 | Android Authority — Samsung Galaxy S26 Google Scam Detection | [링크](https://www.androidauthority.com/google-scam-detection-samsung-galaxy-s26-3643942/) | news | 2026-02 | [B] |
| <a id="ref-g-07"></a>G-07 | Tom's Guide — Samsung Galaxy S26 스캠 탐지 기능 설명 | [링크](https://www.tomsguide.com/phones/samsung-phones/samsung-galaxy-s26-just-got-a-new-tool-to-protect-you-from-scam-calls-and-texts-heres-how-it-works) | news | 2026-02 | [B] |
| <a id="ref-g-08"></a>G-08 | Seoul Economic Daily — KT 경찰청 Circuit Breaker 1만 번호 차단 | [링크](https://en.sedaily.com/technology/2026/03/16/kt-police-launch-ai-powered-phishing-detection-system-block) | news | 2026-03-16 | [B] |
| <a id="ref-g-09"></a>G-09 | Financial News — KT AI 음성피싱 탐지 서비스 2.0 출시 | [링크](https://en.fnnews.com/news/202507290951429524) | news | 2025-07-29 | [B] |
| <a id="ref-g-10"></a>G-10 | Asiae.co.kr (영문) — SKT 2025년 11억건 통신 사기 차단 | [링크](https://cm.asiae.co.kr/en/article/2026011309053028674) | news | 2026-01-13 | [B] |
| <a id="ref-g-11"></a>G-11 | Telecompaper — SKT AI 기반 스팸·음성피싱 차단 +35% | [링크](https://www.telecompaper.com/news/skt-reveals-rise-in-ai-driven-blocking-of-spam-and-voice-phishing-attempts--1558993) | news | 2026-01 | [B] |
| <a id="ref-g-12"></a>G-12 | The Fast Mode — KT AI 음성피싱 탐지 서비스 상용화 | [링크](https://www.thefastmode.com/technology-solutions/39153-kt-unveils-real-time-ai-voice-phishing-protection) | news | 2025-07 | [B] |
| <a id="ref-g-13"></a>G-13 | StarNews Korea — 삼성전자·이통 3사 통화 중 AI 보이스피싱 탐지 | [링크](https://www.starnewskorea.com/en/business-life/2026/02/12/2026021214210282736) | news | 2026-02-12 | [B] |
| <a id="ref-g-14"></a>G-14 | AJU Press — 2025년 Q1 보이스피싱 피해 3,116억, +17% | [링크](https://www.ajupress.com/view/20250427102250032) | news | 2025-04 | [B] |
| <a id="ref-g-15"></a>G-15 | Korea Times — 2025년 보이스피싱 피해 1조원 돌파 상반기 | [링크](https://www.koreatimes.co.kr/business/tech-science/20250602/ai-takes-lead-in-fight-against-voice-phishing-in-wake-of-sk-telecom-hack) | news | 2025-06-02 | [B] |
| <a id="ref-g-16"></a>G-16 | Martech Series — Hiya State of the Call 2026 | [링크](https://martechseries.com/predictive-ai/ai-platforms-machine-learning/state-of-the-call-2026-ai-deepfake-voice-calls-hit-1-in-4-americans-as-consumers-say-scammers-are-beating-mobile-network-operators-2-to-1/) | news | 2026-03-02 | [B] |
| <a id="ref-g-17"></a>G-17 | Korea Tech Today — LGU+ 세계 최초 온디바이스 Anti-DeepVoice | [링크](https://koreatechtoday.com/lg-uplus-launches-worlds-first-on-device-ai-to-fight-deepfake-voice-scams/) | news | 2025 | [B] |
| <a id="ref-g-18"></a>G-18 | Digital Today — KT-경찰청 AI 피싱 대응 신고 25% 감소 | [링크](https://www.digitaltoday.co.kr/en/view/39233/kt-steps-up-ai-based-phishing-response-with-national-police-agency-reports-down-25-percent) | news | 2026-03 | [B] |
| <a id="ref-g-19"></a>G-19 | Sammyguru — Galaxy 폰 KT AI 보이스피싱 탐지 서비스 탑재 | [링크](https://sammyguru.com/galaxy-phones-get-kts-new-ai-voice-phishing-detection-system-in-south-korea/) | news | 2025-07 | [B] |
| <a id="ref-g-20"></a>G-20 | MarketsandMarkets — Fraud Detection & Prevention Market $65.7B by 2030 | [링크](https://www.marketsandmarkets.com/PressReleases/fraud-detection-prevention.asp) | report | 2025 | [B] |
| <a id="ref-g-21"></a>G-21 | Grand View Research — Fraud Detection Market $90.1B by 2030 | [링크](https://www.grandviewresearch.com/industry-analysis/fraud-detection-prevention-market) | report | 2025 | [B] |
| <a id="ref-g-22"></a>G-22 | Persistence Market Research — Phishing Protection Market $7.3B by 2032 | [링크](https://www.persistencemarketresearch.com/market-research/phishing-protection-market.asp) | report | 2025 | [B] |
| <a id="ref-g-23"></a>G-23 | Market.us — Mobile Phishing Protection CAGR 19.6% | [링크](https://market.us/report/mobile-phishing-protection-market/) | report | 2025 | [C] |
| <a id="ref-g-24"></a>G-24 | Programs.com — Vishing Statistics 2026: 442% 증가, $40B 피해 | [링크](https://programs.com/resources/voice-phishing-stats/) | report | 2026 | [C] |
| <a id="ref-g-25"></a>G-25 | Market Research Future — Robocall Mitigation Market $21.1B by 2035 | [링크](https://www.marketresearchfuture.com/reports/robocall-mitigation-market-37870) | report | 2025 | [B] |
| <a id="ref-g-26"></a>G-26 | Digital Today — 보이스피싱 4개월 연속 감소 | [링크](https://www.digitaltoday.co.kr/en/view/5033/voice-phishing-incidents-losses-fall-for-fourth-straight-month) | news | 2026 | [B] |
| <a id="ref-g-27"></a>G-27 | Unbox Future — AI Voice Scam Epidemic, 1 in 4 Americans Fooled | [링크](https://www.unboxfuture.com/2026/03/the-ai-voice-scam-epidemic-Fooled-by-Deepfakes.html) | blog | 2026-03 | [C] |
| <a id="ref-g-28"></a>G-28 | McAfee Blog — Deepfake Detector 96% 정확도 | [링크](https://www.mcafee.com/blogs/internet-security/mcafee-deepfake-detector-with-lenovo/) | blog | 2024 | [B] |
| <a id="ref-g-29"></a>G-29 | PMC / arXiv — Audio Deepfake Detection 성능 벤치마크 리뷰 | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/) | paper | 2025 | [A] |
| <a id="ref-g-30"></a>G-30 | Bank Info Security — Adaptive Security Series B $81M | [링크](https://www.bankinfosecurity.com/adaptive-security-gets-81m-series-b-for-ai-deepfake-defense-a-30332) | news | 2025-12 | [B] |
| <a id="ref-g-31"></a>G-31 | TechBuzz AI — C2PA Authentication Standard 현황 | [링크](https://www.techbuzz.ai/articles/c2pa-authentication-standard-crumbles-as-reality-war-intensifies) | blog | 2026 | [C] |
| <a id="ref-g-32"></a>G-32 | TechCrunch — Truecaller founders step down, 사업 현황 | [링크](https://techcrunch.com/2024/11/06/truecaller-founders-step-down-as-spam-blocker-regains-momentum/) | news | 2024-11 | [B] |
| <a id="ref-g-33"></a>G-33 | FCC 공식 문서 — AI 음성 로보콜 TCPA 적용 선언 | [링크](https://www.fcc.gov/document/fcc-makes-ai-generated-voices-robocalls-illegal) | official | 2024-02 | [A] |
| <a id="ref-g-34"></a>G-34 | 정책브리핑 — AI 기반 음성피싱 공동대응 플랫폼 사업 | [링크](https://www.korea.kr/news/policyNewsView.do?newsId=148959497) | official | 2025 | [A] |
| <a id="ref-g-35"></a>G-35 | Digital Watch Observatory — 한국 AI 생성 콘텐츠 공시 규정 | [링크](https://dig.watch/updates/ai-generated-ads-face-new-disclosure-rules-in-south-korea) | news | 2026 | [B] |
| <a id="ref-g-36"></a>G-36 | SC Media — Microsoft Teams BIP 보안 강화 | [링크](https://www.scworld.com/brief/microsoft-teams-enhances-call-security-with-brand-impersonation-protection) | news | 2026-03 | [B] |
| <a id="ref-g-37"></a>G-37 | Sammyfans — Samsung Galaxy S26 Gemini AI Scam Detection | [링크](https://www.sammyfans.com/2026/02/25/samsung-galaxy-s26-gemini-ai-scam-detection/) | blog | 2026-02-25 | [C] |
| <a id="ref-g-38"></a>G-38 | Korea Herald — LGU+ Anti-Deepvoice 세계 최초 온디바이스 | [링크](https://www.koreaherald.com/article/10518436) | news | 2025 | [B] |
| <a id="ref-g-39"></a>G-39 | Globe Newswire — Robocall Mitigation 시장 경쟁자 리더보드 2025~2030 | [링크](https://www.globenewswire.com/news-release/2025/07/22/3119606/28124/en/Robocall-Mitigation-Branded-Calling-Market-Competitor-Leaderboard-Report-2025-2030.html) | report | 2025-07 | [B] |
| <a id="ref-g-40"></a>G-40 | Biometric Update — Aurigin Apollo 97.7% 정확도 실시간 통화 탐지 | [링크](https://www.biometricupdate.com/202509/aurigins-real-time-audio-deepfake-detection-defends-against-phone-video-call-fraud) | news | 2025-09 | [B] |
| <a id="ref-g-41"></a>G-41 | Help Net Security — Meta AI 스캠 탐지 기술 분석 | [링크](https://www.helpnetsecurity.com/2026/03/11/meta-ai-scam-protection-tools/) | news | 2026-03-11 | [B] |
| <a id="ref-g-42"></a>G-42 | ValidSoft — STIR/SHAKEN 한계 기술 노트 | [링크](https://www.validsoft.com/stir/shaken-limitations/) | blog | 2025 | [B] |
| <a id="ref-g-43"></a>G-43 | GASA — 한국 스캠 현황 보고서 2025 | [링크](https://www.gasa.org/post/state-of-scams-in-south-korea-report-2025) | report | 2025 | [B] |
| <a id="ref-g-44"></a>G-44 | SammMobile — Galaxy S26 Call Screening 13개 언어 지원 | [링크](https://www.sammobile.com/news/galaxy-s26-call-screening-explained-how-does-samsung-filter-spam-calls/) | blog | 2026-02 | [C] |
| <a id="ref-p-01"></a>P-01 | Donahue et al. — "On Deepfake Voice Detection: It's All in the Presentation" (arXiv:2509.26471, 2025) | [링크](https://arxiv.org/html/2509.26471v1) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | ACM TOIT — "Where are We in Audio Deepfake Detection?" (ACM Transactions on Internet Technology, 2025) | [링크](https://dl.acm.org/doi/10.1145/3736765) | paper | 2025 | [A] |
| <a id="ref-p-03"></a>P-03 | MDPI Applied Sciences — "DeepDetection: Privacy-Enhanced Deep Voice Detection and User Authentication" (2022) | [링크](https://www.mdpi.com/2076-3417/12/21/11109) | paper | 2022 | [A] |
| <a id="ref-e-01"></a>E-01 | SKT (아시아경제 보도자료) — 2025년 AI 필터링 11억건 차단 발표 | [링크](https://cm.asiae.co.kr/en/article/2026011309053028674) | IR/발표 | 2026-01-13 | [A] |
| <a id="ref-e-02"></a>E-02 | KT (서울경제 보도) — Circuit Breaker 1만 번호 차단, 신고 25% 감소 | [링크](https://en.sedaily.com/technology/2026/03/16/kt-police-launch-ai-powered-phishing-detection-system-block) | IR/발표 | 2026-03-16 | [A] |
| <a id="ref-e-03"></a>E-03 | KT (Financial News 보도) — AI 음성피싱 탐지 2.0 출시, 95%+ 정확도 목표 | [링크](https://en.fnnews.com/news/202507290951429524) | IR/발표 | 2025-07-29 | [A] |
| <a id="ref-e-04"></a>E-04 | Hiya (PR Newswire) — State of the Call 2026 공식 발표 | [링크](https://natlawreview.com/press-releases/state-call-2026-ai-deepfake-voice-calls-hit-1-4-americans-consumers-say) | IR/발표 | 2026-03-02 | [A] |
| <a id="ref-e-05"></a>E-05 | Meta (about.fb.com 공식 블로그) — Anti-Scam Tools 배포 발표 | [링크](https://about.fb.com/news/2026/03/meta-launches-new-anti-scam-tools-deploys-ai-technology-to-fight-scammers-and-protect-people/) | IR/발표 | 2026-03-11 | [A] |
| <a id="ref-e-06"></a>E-06 | Microsoft (BleepingComputer 보도) — Teams BIP 3월 배포 완료 발표 | [링크](https://www.bleepingcomputer.com/news/microsoft/microsoft-teams-to-add-brand-impersonation-warnings-to-calls/) | IR/발표 | 2026-03 | [A] |
| <a id="ref-e-07"></a>E-07 | Mirage Security / Help Net Security — Vishing-as-a-Service p1bot 연구 발표 | [링크](https://www.helpnetsecurity.com/2026/03/11/researchers-uncover-ai-powered-vishing-platform/) | IR/발표 | 2026-03-11 | [B] |
