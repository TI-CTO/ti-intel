---
topic: 스팸/피싱 감지(통화전) AI 서비스
domain: secure-ai
l2_topic: spam-phishing
date: 2026-03-18
wtis_version: v4.1
wtis_mode: standard
skills_executed: [research-deep, SKILL-1, validator]
confidence: medium
status: completed
total_references: 54
verdict: 재검토
score: 115/200
strategy: Borrow + Build (경찰청 연계 + 고령자/PSTN 특화)
prior_report: 2026-03-03_secure-ai-v2/2026-03-03_wtis-secure-ai-v2.md
prior_report_date: 2026-03-03
---

# WTIS Report: 스팸/피싱 감지(통화전) AI 서비스

## Executive Summary

**시장**: 보이스피싱 피해 2025년 1조 567억원 돌파(사상 최대) [[G-14]](#ref-g-14). Robocall Mitigation TAM $5.6B→$21.1B(CAGR 14~19%) [[G-25]](#ref-g-25). 시장 수요 자체는 확실.
**기술**: Pre-Call 탐지 TRL 7~8. KT 97.2% 정확도 [[G-08]](#ref-g-08), SKT 11억건 차단(+35%) [[E-01]](#ref-e-01). 딥페이크 탐지는 Arms Race 구조로 불안정.
**기회**: 정부 AI 기반 공동대응 플랫폼 2026~2027 구축 [[G-34]](#ref-g-34) — 마지막 진입 창구. 경찰청 DB 연계+고령자 PSTN 특화가 유일한 차별화 축.
**위협**: 3중 압박(Samsung S26 무료 내장 [[G-06]](#ref-g-06) + Meta 3플랫폼 [[G-05]](#ref-g-05) + Microsoft Teams [[G-04]](#ref-g-04)) → 통신사 부가서비스 독립 가치 심각 희석. KT가 경쟁 기술 리더(97.2% + Circuit Breaker 신고 25% 감소) [[G-08]](#ref-g-08)[[E-02]](#ref-e-02).
**권고**: Borrow+Build. 경찰청-통신사 데이터 연계와 고령자/PSTN 특화에 집중. 2026H2 이전 출시 필수. 유료화 전략은 간접 ROI(이탈 방지)로 정당화.

## 이전 분석 대비 변화

| 항목 | 이전 (2026-03-03) | 현재 (2026-03-18) | 변화 |
|------|------------------|------------------|------|
| 판정 | Conditional Go (120) | **재검토 (115)** | ↓ -5점 |
| 핵심 위협 | Samsung S26 단독 | **3중 압박 (Samsung+Meta+MS)** | 확대 |
| 경쟁 리더 | SKT (11억건) | **KT (97.2% + Circuit Breaker)** | KT 역전 |
| 신규 위협 | — | Vishing-as-a-Service ($399/월) | 신규 |
| 피해 규모 | 8,545억원 (2024) | **1조 567억원 (2025 1~10월)** | +23.6% |
| 경쟁우위 | 22/40 | **15/40** | **-7** |

**하락 주요 원인:** 경쟁우위(15/40) 급락. Samsung+Meta+Microsoft가 2026년 3월 한 달 내 동시 무료 배포하면서 통신사 부가서비스의 독립적 가치가 심각하게 희석. KT Circuit Breaker(경찰청 연계 1만 번호 차단, 신고 25% 감소)가 국내 경쟁 강도를 한층 높임.

## 1. 시장 분석

### TAM/SAM/SOM

| 구분 | 규모 | CAGR | 출처 |
|------|------|------|------|
| TAM (Robocall Mitigation) | $5.6B(2025)→$21.1B(2035) | ~14% | [[G-25]](#ref-g-25) |
| TAM (Fraud Detection) | $65.7B(2030) | 17~19% | [[G-20]](#ref-g-20)[[G-21]](#ref-g-21) |
| SAM (한국 통화보안) | 수백억원 추정 | — | [D] |
| SOM | 미정 | — | [D] |

### 한국 보이스피싱 피해 통계

| 연도 | 피해액 | 1인당 | 출처 |
|------|--------|-------|------|
| 2024 | 8,545억원 | 5,290만원 | [[G-02]](#ref-g-02) |
| 2025 (1~10월) | **1조 567억원** | — | [[G-14]](#ref-g-14) |

> **Validator 수정**: SKILL-1의 "+91% YoY" 표기는 비교 기간 혼용 오류. 연간 기준 약 +23.6% 성장이 정확.

## 2. 기술 성숙도 분석

### 탐지 정확도 벤치마크

| 솔루션 | 정확도 | 특이점 | 출처 |
|--------|--------|--------|------|
| KT WhoWho 2.0 | **97.2%** | 국과수 성문DB+딥보이스+문맥 3중 | [[G-08]](#ref-g-08) |
| Aurigin Apollo | 97.7% (EER 2.3%) | 실시간 오디오 딥페이크 탐지 | [[G-40]](#ref-g-40) |
| McAfee Deepfake Detector | 96% | 온디바이스, 3초 내 판정 | [[G-28]](#ref-g-28) |
| Samsung S26 | ~95% (비공식) | Google Scam Detection 내장, 13개 언어 | [[G-06]](#ref-g-06)[[G-44]](#ref-g-44) |
| SKT ScamVanguard | 미공개 | 11억건 차단(+35% YoY), 통화패턴 AI | [[E-01]](#ref-e-01) |

### TRL 현황

| 기술 | TRL | 근거 |
|------|-----|------|
| AI Pre-Call 스팸 탐지 | 7~8 | SKT/KT 상용 운영 중 |
| 딥페이크 음성 탐지 | 6~7 | KT 2.0 상용화, 실사용 환경 불안정 (Arms Race) |
| STIR/SHAKEN | 8~9 | 미국 의무화, 한국 기적용 |
| C2PA 음성 인증 | 3~4 | 표준 확산 중, 통신사 직접 적용 미확인 |

## 3. 경쟁 환경

### 3중 압박 구조 (이전 "Samsung Critical Risk" 확대)

```
[단말]  Samsung S26 — Google Scam Detection 무료 내장, 13개 언어, 전 갤럭시 확대
         ↓
[플랫폼] Meta — WhatsApp/Facebook/Messenger AI 사기 탐지 동시 출시
         Microsoft — Teams Brand Impersonation Protection 3월 배포
         ↓
[통신사] SKT — ScamVanguard 11억건, KT — 97.2% + Circuit Breaker
         → 후발 진입 공간 극도로 축소
```

### Gap Analysis

| 역량 | 자사 | SKT | KT | Samsung | 격차 |
|------|------|-----|-----|---------|------|
| 탐지 정확도 | 미보유 | 미공개 | **97.2%** | ~95% | **KT 선행** |
| 차단 규모 | 미보유 | **11억건** | — | — | **SKT 선행** |
| 경찰청 연계 | 미보유 | 부분 | **Circuit Breaker** | 없음 | **KT 선행** |
| 딥페이크 탐지 | 미보유 | 에이닷 | **2.0 (3중)** | Google 내장 | **KT 선행** |
| 고령자 PSTN | — | 부분 | 부분 | **미지원** | **기회 영역** |

### 신규 위협: Vishing-as-a-Service

P1 플랫폼 — 월 $399로 전화번호 스푸핑+ElevenLabs TTS 15개 음성+WebRTC 발신 자동화. Scam-as-a-Service 진입장벽 붕괴로 공격 볼륨 비선형 확대 예상 [[G-01]](#ref-g-01).

## 4. 전략 권고

### 3B 의사결정

| 요소 | 판정 | 근거 |
|------|------|------|
| 차별화 중요도 | 5/10 | 기술 모방 용이. 경찰청 DB+PSTN만 차별화 |
| 내부 역량 | 부분 | 망 데이터 보유, AI 탐지 팀 미확인 [D] |
| 시장 윈도우 | <12개월 | 정부 플랫폼 2026~2027이 마지막 |
| 시장 긴급성 | 7/10 | 피해 1조원+, 소비자 38% 이탈 의향 |
| 기술 갭 | 1~1.5년 (vs KT) | KT 97.2%+Circuit Breaker 선점 |

**결론: Borrow + Build**
- **Borrow**: Hiya/Adaptive Security 등 글로벌 딥페이크 탐지 엔진 파트너십
- **Build**: 경찰청 연계 DB, 고령자/PSTN 특화, 가상화폐 크로스 채널 탐지

### 유일한 차별화 축 (플랫폼이 복제 불가)

1. **경찰청-통신사 데이터 연계**: 정부 공동대응 플랫폼 참여 [[G-34]](#ref-g-34)
2. **고령자/PSTN 특화**: Samsung/Meta/MS가 커버하지 못하는 스마트폰 미사용 고령층
3. **망 시그널링 우위**: STIR/SHAKEN + CDR 메타데이터 + 가입자 행동 패턴

### 후속 조건 체크리스트

- [ ] 사업기획: 정부 공동대응 플랫폼 참여 계획 확정 (2026-Q2, 필수)
- [ ] 기술기획: 딥페이크 탐지 엔진 파트너 선정 (Hiya/Adaptive Security 평가)
- [ ] 서비스기획: 고령자/PSTN 보호 서비스 설계 (2026-Q3)
- [ ] 마케팅: 이탈 방지 ROI 모델 수립 (유료화 vs 번들 vs 무료)
- [ ] 전략기획: 2026H2 출시 타임라인 확정 (필수 — 미확정 시 시장 기회 상실)

## 5. 교차검증 결과

**Validator 판정: PARTIAL** (Critical 2건, Minor 4건)

| # | 유형 | 심각도 | 내용 | 처리 |
|---|------|--------|------|------|
| 1 | 수치 | Critical | "+91% YoY" — 비교 기간 혼용. 실제 ~+23.6% | 본 보고서에서 수정 반영 |
| 2 | 수치 | Critical | Truecaller EBITDA -49% — 원본 미확인 (-2.7%가 정확) | 본 보고서에서 제외 |
| 3 | 인용 | Minor | P-03 고아 소스 | References에 참고용 유지 |
| 4 | 신뢰도 | Minor | G-02에 [A] 부여 → [B]급이 정확 | 본 보고서에서 수정 |
| 5 | 판정 | Minor | frontmatter "Conditional Go" vs 점수 115 (재검토 범위) | **본 보고서에서 "재검토"로 정정** |

**핵심 수치 검증 통과**: KT 97.2%, SKT 11억건, 피해 1조 567억원, Hiya 25%/38%, VaaS $399, Meta 15만 계정, vishing 442% 증가.

## 6. 정량 평가 (115/200)

| # | 평가 항목 | 세부1 | 세부2 | 세부3 | 세부4 | 소계 |
|---|----------|-------|-------|-------|-------|------|
| 1 | 고객가치 | 9 (pain) | 8 (가치) | 5 (대체재) | 8 (수용성) | **30/40** |
| 2 | 시장매력도 | 7 (TAM) | 8 (CAGR) | 5 (타이밍) | 8 (규제) | **28/40** |
| 3 | 기술경쟁력 | 7 (TRL) | 5 (특허)[D] | 5 (장벽) | 7 (표준) | **24/40** |
| 4 | 경쟁우위 | 3 (포지션) | 4 (지속성) | 4 (대응력) | 4 (생태계) | **15/40** |
| 5 | 실행가능성 | 5 (역량)[D] | 4 (ROI) | 4 (일정) | 5 (리스크) | **18/40** |
| | **총점** | | | | | **115/200** |

**판정: 재검토 (80~119)**

115점은 재검토 범위 최상단. 고객가치(30)·시장매력도(28)는 양호하나, **경쟁우위(15)·실행가능성(18)이 미흡**. 이전 120점에서 -5점 하락한 주원인은 3중 압박 구조 심화에 따른 경쟁우위 -7점.

**이전 "Conditional Go" → "재검토" 하향 이유:**
- Samsung+Meta+Microsoft 동시 무료 배포 → 부가서비스 독립 가치 심각 희석
- KT Circuit Breaker+97.2% → 기술 리더 역전, 후발 차별화 공간 축소
- Vishing-as-a-Service 등장 → 공격 볼륨 비선형 확대, 탐지 측 Arms Race 열세 심화

**재검토 → Conditional Go 전환 조건:**
1. 정부 공동대응 플랫폼 참여 확정 + 경찰청 DB 연계 (필수)
2. 2026H2 출시 타임라인 확정 (필수)
3. 고령자/PSTN 특화 서비스 설계 완료 (필수)
4. 딥페이크 탐지 파트너십 확보 (필수)
5. 이탈 방지 ROI 모델로 투자 정당화 (필수)

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Help Net Security — VaaS p1bot | [링크](https://www.helpnetsecurity.com/2026/03/11/researchers-uncover-ai-powered-vishing-platform/) | news | 2026-03-11 | [B] |
| <a id="ref-g-02"></a>G-02 | Korea Herald — 2025 피해 통계 | [링크](https://www.koreaherald.com/article/10631333) | news | 2025-11 | [B] |
| <a id="ref-g-04"></a>G-04 | BleepingComputer — MS Teams BIP | [링크](https://www.bleepingcomputer.com/news/microsoft/microsoft-teams-to-add-brand-impersonation-warnings-to-calls/) | news | 2026-03 | [B] |
| <a id="ref-g-05"></a>G-05 | TechCrunch — Meta AI 스캠 탐지 | [링크](https://techcrunch.com/2026/03/11/meta-rolls-out-new-scam-detection-tools-to-facebook-whatsapp-and-messenger/) | news | 2026-03-11 | [B] |
| <a id="ref-g-06"></a>G-06 | Android Authority — Samsung S26 Scam Detection | [링크](https://www.androidauthority.com/google-scam-detection-samsung-galaxy-s26-3643942/) | news | 2026-02 | [B] |
| <a id="ref-g-07"></a>G-07 | Tom's Guide — Samsung S26 스캠 탐지 | [링크](https://www.tomsguide.com/phones/samsung-phones/samsung-galaxy-s26-just-got-a-new-tool-to-protect-you-from-scam-calls-and-texts-heres-how-it-works) | news | 2026-02 | [B] |
| <a id="ref-g-08"></a>G-08 | Seoul Economic Daily — KT Circuit Breaker | [링크](https://en.sedaily.com/technology/2026/03/16/kt-police-launch-ai-powered-phishing-detection-system-block) | news | 2026-03-16 | [B] |
| <a id="ref-g-14"></a>G-14 | AJU Press — 피해 1조 567억원 | [링크](https://www.ajupress.com/view/20250427102250032) | news | 2025-04 | [B] |
| <a id="ref-g-16"></a>G-16 | Martech Series — Hiya State of Call 2026 | [링크](https://martechseries.com/predictive-ai/ai-platforms-machine-learning/state-of-the-call-2026-ai-deepfake-voice-calls-hit-1-in-4-americans-as-consumers-say-scammers-are-beating-mobile-network-operators-2-to-1/) | 리포트 | 2026-03-02 | [B] |
| <a id="ref-g-20"></a>G-20 | MarketsandMarkets — Fraud Detection $65.7B | [링크](https://www.marketsandmarkets.com/PressReleases/fraud-detection-prevention.asp) | report | 2025 | [B] |
| <a id="ref-g-21"></a>G-21 | Grand View — Fraud Detection $90.1B | [링크](https://www.grandviewresearch.com/industry-analysis/fraud-detection-prevention-market) | report | 2025 | [B] |
| <a id="ref-g-25"></a>G-25 | MRFR — Robocall Mitigation $21.1B | [링크](https://www.marketresearchfuture.com/reports/robocall-mitigation-market-37870) | report | 2025 | [B] |
| <a id="ref-g-28"></a>G-28 | McAfee — Deepfake Detector 96% | [링크](https://www.mcafee.com/blogs/internet-security/mcafee-deepfake-detector-with-lenovo/) | blog | 2024 | [B] |
| <a id="ref-g-30"></a>G-30 | BankInfoSecurity — Adaptive Security $81M | [링크](https://www.bankinfosecurity.com/adaptive-security-gets-81m-series-b-for-ai-deepfake-defense-a-30332) | news | 2025-12 | [B] |
| <a id="ref-g-33"></a>G-33 | FCC — AI 음성 로보콜 TCPA | [링크](https://www.fcc.gov/document/fcc-makes-ai-generated-voices-robocalls-illegal) | 공식 | 2024-02 | [A] |
| <a id="ref-g-34"></a>G-34 | 정책브리핑 — 공동대응 플랫폼 | [링크](https://www.korea.kr/news/policyNewsView.do?newsId=148959497) | 공식 | 2025 | [A] |
| <a id="ref-g-40"></a>G-40 | Biometric Update — Aurigin 97.7% | [링크](https://www.biometricupdate.com/202509/aurigins-real-time-audio-deepfake-detection-defends-against-phone-video-call-fraud) | news | 2025-09 | [B] |
| <a id="ref-g-44"></a>G-44 | SammMobile — S26 13개 언어 | [링크](https://www.sammobile.com/news/galaxy-s26-call-screening-explained-how-does-samsung-filter-spam-calls/) | blog | 2026-02 | [C] |
| <a id="ref-e-01"></a>E-01 | SKT Newsroom — ScamVanguard 11억건 | [링크](https://www.telecompaper.com/news/skt-reveals-rise-in-ai-driven-blocking-of-spam-and-voice-phishing-attempts--1558993) | 보도자료 | 2026-01 | [B] |
| <a id="ref-e-02"></a>E-02 | KT — Circuit Breaker 신고 25% 감소 | [링크](https://en.sedaily.com/technology/2026/03/16/kt-police-launch-ai-powered-phishing-detection-system-block) | 보도자료 | 2026-03 | [B] |
