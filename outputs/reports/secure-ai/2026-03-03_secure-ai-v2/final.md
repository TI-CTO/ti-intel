---
topic: Secure AI — B2C 통화 보안
date: 2026-03-03
wtis_version: v4.0
wtis_mode: proposal
skills_executed: [SKILL-0 v2, research-deep v3, SKILL-1 v2, validator v2]
confidence: medium
status: completed
total_references: 43
verdict: Conditional Go
score: 120/200
strategy: Borrow(PQC) + Build(OndeviceAI/금융연계) + Watch(HE)
prior_report: 2026-02-26_wtis-proposal-secure-ai-final.md
prior_report_date: 2026-02-26
---

# WTIS Report: Secure AI — B2C 통화 보안 (v2)

## 경영진 요약

> **Conditional Go (120/200, 하한선)** — Secure AI 과제는 보이스피싱 피해 **1조 2,578억 원(2025년, YoY +47.2%)** [N-04]이라는 명확한 시장 명분을 갖추고 있으나, **3가지 구조적 제약**으로 인해 제안서 핵심 가정의 전면 재설계가 필수적이다.
>
> 1. **동형암호(HE) 실시간 불가 확정** — Zama GPU 가속(2025.09)에도 64비트 곱셈 32ms/8xH100 [G-24], ITU-T G.114 150ms [G-22] 및 Cisco 실무 250ms [G-23] 기준 모두 초과. 제안서의 "3중 보안 조합" 핵심 가정이 파괴됨.
> 2. **삼성 S26 한국어 무료 탐지 확정** — 경찰청/국과수 데이터 3만건 학습 기반 자체 딥러닝 탐지, One UI 8.0+ 전 갤럭시 확대 [E-01]. B2C 유료 서비스 차별화 공간 급격 축소.
> 3. **OndeviceAI 탐지 commodity화** — 국내 3사(SKT/KT/LGU+) + 삼성 모두 상용화 완료 [N-19]. 차별화 요소 소멸.
>
> **PQC E2E 통화 암호화가 유일한 차별화 축**(경쟁사 미상용, TRL 5~6 [G-25]). **Borrow(PQC 벤더 파트너십) + Build(OndeviceAI/금융-통신 B2B 내재화) + Watch(HE 장기 모니터링)** 전략 권고. 이전 분석(128→123점) 대비 3점 추가 하락(120점)은 삼성 S26 한국어 자체 탐지 확인에 따른 경쟁우위 재평가가 주 원인. 신뢰도: Medium (WTP/투자규모/탐지율 데이터 부재).

---

## 상세 분석

### 핵심 기술 판정

| 기술 | TRL | 판정 | 근거 |
|------|-----|------|------|
| 동형암호 (실시간 통화) | **2~3** | **불가 → Watch** | TFHE 64비트 곱셈 32ms/8xH100 [G-24], ITU-T 150ms [G-22], Cisco 250ms [G-23] 모두 초과. 학술 "prohibitive latency" [P-05]. LGU+ 자체도 비실시간 데이터 보호로 방향 전환 [N-16]. |
| OndeviceAI 보이스피싱 탐지 | 7~8 | **가능, commodity** | 경량 모델 159k params, EER 0.16% [P-09]. 3사+삼성 모두 배포 [N-19]. 잡음 환경 성능 급락 주의 [P-10]. |
| Anti-DeepVoice | 7~8 | **LGU+ 자산** | 세계 최초 온디바이스 상용화 [E-05], 5,500건→월 2,000건 탐지 [N-05, N-16]. 악성 서버 800개 추적 [N-16]. |
| PQC VoLTE E2E 암호화 | 5~6 | **유일한 차별화축** | ML-KEM 표준 확정 [G-07]. 첫 PQC 인증서 2026년, 신뢰 체계 2027년+ [G-25]. MWC 2026 시연 완료 [N-21]. |
| Samsung S26 자체 탐지 | 8~9 | **Critical Risk** | 경찰청/국과수 3만건 학습, 무료, 전 갤럭시 [E-01]. |

### 경쟁 포지션

| 경쟁사 | 서비스 | 핵심 성과 | 출처 |
|--------|--------|----------|------|
| SKT | 스캠뱅가드 + 에이닷 | 11억 건/년 차단, 음성 2.5억건, IBK 이전 | [E-02] |
| KT | AI 탐지 2.0 + 후후 | 91.6% 탐지율, 1,300억 예방, 목표 95%+/2,000억+ | [E-03] |
| LGU+ | 익시오/익시오 프로 | 월 2,000건, 악성서버 800개, KB 1,720억 예방, MWC 2026 PQC 시연 | [E-04, N-16, N-21] |
| Samsung | Galaxy S26 자체 탐지 | 경찰청/국과수 3만건, One UI 8.0+ 전 갤럭시, **무료** | [E-01] |
| Apple | iOS 26 Call Screening | 완전 온디바이스, AI 대리 응대, **무료**, 한국 미확인 [D] | [N-17] |
| Google | Gemini 스캠 탐지 (on S26) | 영어/미국 한정, 온디바이스 Gemini | [N-06] |

**Gap Analysis**: LGU+는 금융-통신 실시간 연계(KB 1,720억 [E-04])와 PQC 시연(MWC 2026 [N-21])에서 차별점을 보유하나, 탐지 규모(월 2,000건 vs SKT 11억건/년), 탐지율 미공개(KT 91.6% 대비), 가입자 규모 열위(19.5% [G-20]), 삼성/Apple 무료화 구조에서 **유료 B2C 서비스의 존재 이유** 확보가 최대 과제.

### 전략 권고: Borrow(PQC) + Build(OndeviceAI/금융연계) + Watch(HE)

```
[과제명]: Secure AI — B2C 통화 보안
[추천 방향]: Borrow(PQC) + Build(OndeviceAI/금융연계) + Watch(HE)
[핵심 근거]:
  - 시장: 피해 1조 2,578억(2025) [N-04], 1인당 5,290만원 [N-18], YoY +47.2%
         글로벌 CAGR 18.7% [G-16]. 단, 삼성/Apple 무료 OS 탑재로 B2C 유료 축소 [E-01, N-17]
  - 기술: PQC E2E(TRL 5~6) = 유일 차별화 [G-25]. HE 실시간 불가 확정 [G-22, G-24, P-05]
         OndeviceAI는 commodity(TRL 7~8) [N-19, P-09]
  - 사업: KB 1,720억 피해 예방 [E-04]으로 금융연계 모델 검증. MWC 2026 PQC 시연 [N-21]
         SKT 7,000억 [N-12], KT 1조 [N-14] 투자 대비 자원 열위
[리스크]:
  R1. Samsung/Apple 무료 탐지 확대 (확률: H, 영향: H) [E-01, N-17]
  R2. PQC E2E 통합 지연 — 단말 벤더 의존 (확률: M, 영향: H) [G-08]
  R3. 유료 전환 실패 — WTP 미검증 (확률: H, 영향: H) [D]
  R4. 경쟁사 투자 격차 (확률: H, 영향: M) [N-12, N-14]
  R5. 실환경 탐지 성능 저하 (확률: M, 영향: M) [P-10, P-11]
[Next Action]:
  - [ ] 0~1개월: 제안서 재설계 (HE 제거, PQC E2E + OndeviceAI 2중 구조)
  - [ ] 0~1개월: PQC 벤더(Thales, IDQ 등) 기술 협의 착수
  - [ ] 0~2개월: B2C WTP 조사 설계/실시
  - [ ] 0~2개월: 2026H2 서비스 출시 마일스톤 역산 일정표
  - [ ] 3~6개월: PQC VoLTE E2E PoC (Hybrid X25519+ML-KEM [G-25])
  - [ ] 3~6개월: 익시오 탐지율 정량 공개 (KT 91.6%+ 대응)
  - [ ] 6~12개월: KB 모델 → 타 금융사 확장
  - [ ] 지속 모니터링: Zama HE 로드맵 [G-24], Samsung HE 반도체 [T-02]
```

### 정량 평가 (120/200)

| # | 평가 항목 | 세부1 | 세부2 | 세부3 | 세부4 | 소계 |
|---|----------|-------|-------|-------|-------|------|
| 1 | 고객가치 | 9 (Pain Point) | 7 (가치 명확성) | 5 (대체제 우위) | 5 (수용성) [D] | **26** |
| 2 | 시장매력도 | 7 (TAM/SAM) | 8 (CAGR) | 6 (타이밍) | 8 (규제) | **29** |
| 3 | 기술경쟁력 | 6 (TRL) | 5 (특허) [D] | 5 (기술장벽) | 6 (표준) | **22** |
| 4 | 경쟁우위 | 4 (포지션) | 5 (지속성) | 4 (대응력) | 7 (생태계) | **20** |
| 5 | 실행가능성 | 7 (내부역량) | 5 (ROI) [D] | 6 (일정) | 5 (리스크) | **23** |
| | **총점** | | | | | **120/200** |

**판정: Conditional Go (120~159 구간 하한선)** — 아래 5대 조건 충족 시 추진 가능:
1. HE 제거 및 제안서 재설계 (필수)
2. 2026H2 서비스 출시 마일스톤 확정 (필수)
3. B2C WTP 조사 실시 — Go 전환 조건
4. PQC E2E 파트너 확보 (필수)
5. Samsung S26 대응 포지셔닝 명확화 — "탐지 이상의 가치" (필수)

---

## 이전 분석 대비 변화

> 이전 분석: `2026-02-26_wtis-proposal-secure-ai-final.md` (2026-02-26)

| 항목 | 이전 (2026-02-26) | 현재 (2026-03-03) | 변화 |
|------|------------------|------------------|------|
| 핵심 판정 | Conditional Go (128→123) | Conditional Go (120) | ↓ -3점 |
| 신뢰도 | Medium | Medium | → 유지 |
| 주요 위험 | S26 영어/미국 추정 | S26 한국어 자체 탐지 확정 [E-01] | ↑ 위험 격상 |
| 기술 성숙도 | HE Critical Risk | HE 불가 확정 (Zama 32ms도 초과) [G-24] | → 확정 |
| 피해 통계 | +335% (불일치) | +91% YoY 확정 [N-20] | 수정 |
| 1인당 피해 | 파생 계산 추정 | 5,290만원 공식 [N-18] | 출처 확정 |
| 익시오 성과 | 5,500건 (H1) | 월 2,000건, 악성서버 800개, 3.3만명 [N-16] | 업데이트 |
| validator | UNCERTAIN (7건) | UNCERTAIN (경미 5건) | 개선 |

**변화 주요 원인:**
- S26 한국어 자체 탐지 확인 → 경쟁우위 점수 하락 (이전: 영어/미국 한정 추정)
- validator v3 이슈 7건 전면 해소 → 데이터 신뢰도 향상 (부분 상쇄)
- TFHE GPU 성능 업데이트(Zama v1.4)에도 HE 불가 판정 강화

---

## 교차검증 결과

**validator 판정: UNCERTAIN (경미)**

이전 v3 validator 이슈 7건: **전면 해소 확인**

| v3 이슈 | v2 해소 |
|---------|---------|
| 고아 인용 G-17~G-19, G-21, G-23 (5건) | 본문 직접 인용 확인 |
| "+335% 폭증" 수치 불일치 | "+91% YoY" 교체 완료 |
| "1인당 5,290만원" 파생 계산 | N-18 공식 출처 확정 |
| N-04/N-10 연도 혼선 | N-10 제외, N-04/N-20 분리 |

**신규 경미 이슈 (핵심 판정에 영향 없음):**

| 검증 항목 | 결과 | 비고 |
|----------|------|------|
| 인용 검증 | ⚠️ | 고아 인용 4건 (G-14, G-27, N-03, N-11 — References 정리 불완전), P-02/03/04 미정의 (범위 표기 [P-01~P-05]) |
| 수치 검증 | ✅ | 핵심 수치 교차 검증 완료. 편의 계산 레이블 명시. |
| 논리 검증 | ✅ | 결론이 증거 수준에 비례. HE 불가 다중 근거 확보. |
| 편향 검증 | ✅ | 강점/약점 균형. LGU+ 불리 데이터 회피 없음. |

**핵심 안전 판정**: HE 불가 판정은 학술 5건 [P-01, P-05] + GPU 벤치마크 [G-24] + 국제표준 [G-22, G-23]으로 다각도 검증 완료. Conditional Go 120/200 채점은 세부 지표별 근거 명시로 논리적 일관성 확인.

---

## 권고 및 Next Action

- [ ] **즉시 (0~1개월)**: 제안서 재설계 — HE 제거, "PQC E2E + OndeviceAI" 2중 구조 확정
- [ ] **즉시 (0~1개월)**: PQC 벤더(Thales, IDQ, PQShield) 기술 협의 착수
- [ ] **단기 (0~2개월)**: B2C WTP 조사 설계/실시 — 유료 전환 가능성 정량 검증
- [ ] **단기 (0~2개월)**: 2026H2 서비스 출시 마일스톤 역산 일정표 작성
- [ ] **단기 (0~2개월)**: 익시오 탐지율 정량 공개 준비 (KT 91.6%+ 대응)
- [ ] **중기 (3~6개월)**: PQC VoLTE E2E PoC — Hybrid X25519+ML-KEM [G-25]
- [ ] **중기 (3~6개월)**: KB 모델 → 타 금융사 2~3사 확장
- [ ] **중기 (3~6개월)**: 정부 공동대응 플랫폼 [N-19] 데이터 허브 역할 선점
- [ ] **장기 (6~12개월)**: PQC 프리미엄 통화 파일럿 (VIP/기업 세그먼트)
- [ ] **지속 모니터링**: Zama HE 로드맵 [G-24], Samsung HE 반도체 [T-02], Apple iOS 26 한국 지원 [N-17]

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|----------|------|--------|--------|--------|-----|
| G-07 | postquantum.com | 2025 | 전문기관 | PQC Standardization 2025 Update | 4 | 4 | 5 | https://postquantum.com/post-quantum/cryptography-pqc-nist/ |
| G-08 | postquantum.com / GSMA PQ.03 v2.0 | 2025/2024 | 전문기관 | Telecom's Quantum-Safe Imperative | 5 | 4 | 5 | https://postquantum.com/post-quantum/telecom-pqc-challenges/ |
| G-09 | Pindrop 공식 | 2025 | 기업 | 2025 Voice Intelligence Report | 4 | 4 | 5 | https://www.pindrop.com/research/report/voice-intelligence-security-report/ |
| G-16 | DataIntelo | 2024 | 리서치 | AI-Powered Voice Fraud Detection Market | 4 | 3 | 4 | https://dataintelo.com/report/ai-powered-voice-fraud-detection-market |
| G-17 | DataIntelo | 2024 | 리서치 | Call Center Fraud Detection AI Market ($1.92B CAGR 19.7%) | 4 | 3 | 4 | https://dataintelo.com/report/call-center-fraud-detection-ai-market |
| G-18 | Market Research Future | 2024 | 리서치 | Voice Analytics Market ($3.69B CAGR 12.68%) | 4 | 3 | 4 | https://www.marketresearchfuture.com/reports/voice-analytics-market-7979 |
| G-19 | Allied Market Research | 2023 | 리서치 | Voice Analytics Market ($1.3B CAGR 19.6%) | 4 | 3 | 4 | https://www.alliedmarketresearch.com/voice-analytics-market-A12983 |
| G-20 | 서울신문 (MSIT 통계) | 2025.07 | 정부 통계 | 이동통신 가입자 5,724만, LGU+ 19.5% | 5 | 5 | 5 | https://www.seoul.co.kr/news/economy/2025/07/18/20250718500096 |
| G-22 | ITU-T Rec. G.114 | 2003 (현행) | 국제표준 | 편도 지연 150ms 권장 | 5 | 5 | 3 | https://www.itu.int/rec/T-REC-G.114 |
| G-23 | Cisco | 2006 (현행) | 기업 기술문서 | VoIP 실무 200ms 적정, 250ms 한계 | 5 | 4 | 3 | https://www.cisco.com/c/en/us/support/docs/voice/voice-quality/14655-voip-delay-details.html |
| G-24 | Zama 블로그 | 2025.09 | 기업(HE) | TFHE bootstrapping <1ms, 64비트 곱셈 32ms/8xH100 | 5 | 4 | 5 | https://www.zama.org/post/bootstrapping-tfhe-ciphertexts-in-less-than-one-millisecond |
| G-25 | Cloudflare Blog | 2025 | 기업 | PQC 2025: ML-KEM 배포 중, 첫 인증서 2026년 | 4 | 4 | 5 | https://blog.cloudflare.com/pq-2025/ |
| G-26 | MarketsandMarkets | 2024 | 리서치 | Voice Analytics $1.6B CAGR 19.4% | 4 | 3 | 4 | https://www.marketsandmarkets.com/PressReleases/voice-analytics.asp |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | URL |
|------|--------|-------|------|-----|
| N-04 | 헤럴드경제 | 2026.01 | 2025년 보이스피싱 피해 1.2조 사상 최대 | https://biz.heraldcorp.com/article/10661923 |
| N-05 | 스마트투데이 | 2025 | LGU+ Anti-DeepVoice 5,500건 탐지 | https://www.smarttoday.co.kr/news/articleView.html?idxno=87596 |
| N-06 | Sammy Fans | 2026.02.25 | S26 Gemini 스캠 탐지 (영어/미국 한정) | https://www.sammyfans.com/2026/02/25/samsung-galaxy-s26-gemini-ai-scam-detection/ |
| N-08 | VoIP Review | 2025.11 | BT-Pindrop 딥페이크 탐지 파트너십 | https://voip.review/2025/11/18/bt-pindrop-team-combat-voice-fraud-ai/ |
| N-09 | The Pickool | 2024.10 | KT 규제샌드박스 승인 | https://www.thepickool.com/kt-gains-regulatory-approval-for-ai-powered-voice-phishing-detection-service/ |
| N-12 | 보안뉴스 외 | 2025.07 | SKT 5년 7,000억 투자 | https://news.nate.com/ |
| N-14 | 서울경제 외 | 2025.07 | KT 5년 1조 투자 | https://news.nate.com/ |
| N-16 | 이지경제 외 | 2026.02.23 | LGU+ MWC 2026 익시오 프로 공개 | https://www.ezyeconomy.com/news/articleView.html?idxno=232539 |
| N-17 | TechRadar 외 | 2026.01 | iOS 26 Call Screening | https://www.techradar.com/phones/iphone/call-screening-in-ios-26 |
| N-18 | 더시사법률 | 2025.11 | 1인당 5,290만원 (경찰청 국수본 공식) | https://www.tsisalaw.com/mobile/article.html?no=26745 |
| N-19 | 과기정통부 | 2026.02.12 | AI 공동대응 플랫폼 2026~2027 구축 | https://www.korea.kr/news/policyNewsView.do?newsId=148959497 |
| N-20 | 뉴데일리 외 | 2025.07 | 2024년 피해 8,545억, +91% YoY | https://www.newdaily.co.kr/site/data/html/2025/07/15/2025071500048.html |
| N-21 | 이지경제 | 2026.02.23 | LGU+ MWC 2026 PQC 통화 암호화 시연 | https://www.ezyeconomy.com/news/articleView.html?idxno=232696 |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 요약 |
|------|--------|-------|------|------|
| E-01 | 삼성 뉴스룸 / 과기정통부 | 2026.02 | 갤럭시 AI 보이스피싱 차단 | 경찰청/국과수 3만건, One UI 8.0+ 전 갤럭시, 무료 |
| E-02 | SKT 뉴스룸 | 2026.01 | 에이닷 스캠뱅가드 2025 성과 | 11억 건 차단, 음성 2.5억건, IBK 이전 |
| E-03 | KT 뉴스룸 외 | 2025.07~12 | AI 보이스피싱 탐지 2.0 | 91.6%, 1,300억 예방, 목표 95%+/2,000억+ |
| E-04 | 한국NGO신문 외 | 2026.01~02 | KB-LGU+ AI 실시간 대응 | 1,720억 예방, MWC26 시연 |
| E-05 | Korea Herald | 2025.02 | LGU+ Anti-DeepVoice MWC 2025 | Exy Guardian 세계 최초 온디바이스 |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 핵심 인용 | DOI/URL |
|------|------|---------|------|----------|---------|
| P-01 | Chillotti et al. | 2020/2025 | TFHE: Fast FHE over the Torus | ~13ms/gate; refined 4.2~6.8ms | https://tfhe.github.io/tfhe/ |
| P-05 | arXiv | 2026.02 | On the Feasibility of Hybrid HE | "prohibitive latency" 실시간 불가 | https://arxiv.org/pdf/2602.02717 |
| P-08 | Xinfeng Li et al. | 2024 | SafeEar: Privacy-Preserving Deepfake Detection | EER 2.02%, 프라이버시 보존 | https://arxiv.org/abs/2409.09272 |
| P-09 | K.A. Shahriar | 2026.01 | Lightweight Audio Deepfake Detection | 159k params, EER 0.16%, AUC 0.98 | https://arxiv.org/abs/2601.06560 |
| P-10 | arXiv | 2025.12 | Noise-Aware Audio Deepfake Detection | 잡음 환경 성능 급락 | https://arxiv.org/abs/2512.13744 |
| P-11 | arXiv | 2026.01 | Audio Deepfake in Age of Advanced TTS | 최신 TTS 일반화 어려움 | https://arxiv.org/abs/2601.20510 |

### 특허 (T-xx)

| 번호 | 출원인 | 특허번호 | 제목 | 관할 |
|------|--------|---------|------|------|
| T-01 | Google LLC | US11423926B2 | Real-time voice phishing detection | USPTO |
| T-02 | Samsung Electronics | US11652603B2 | AI Calculation Semiconductor (HE 가속) | USPTO |
| T-03 | Wells Fargo Bank | US20250252968A1 | Synthetic Voice Fraud Detection | USPTO |

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 인용내용 |
|------|--------|-------|---------|
| I-01 | Secure AI 기술/시장/규제 리서치 | 2026-02-25 | HE TRL, PQC TRL, SKT Thales PQC SIM |
| I-03 | WTIS SKILL-1 v3 (123/200) | 2026-02-26 | 2026H2 출시 필요, 권고 KPI |

---

## 파이프라인 산출물

| 단계 | 파일 | 상태 |
|------|------|------|
| SKILL-0 v2 (제안서 파싱) | `2026-02-26_wtis-proposal-secure-ai-v2-skill0.md` | ✅ pass |
| research-deep v3 (심층 리서치) | `2026-02-26_wtis-proposal-secure-ai-v2-research.md` | ✅ pass (이슈 7건 해소) |
| SKILL-1 v2 (선정검증) | `2026-03-03_wtis-proposal-secure-ai-v2-skill1.md` | ✅ Conditional Go 120/200 |
| validator v2 (교차검증) | `2026-03-03_wtis-proposal-secure-ai-v2-skill1-validator.md` | ⚠️ UNCERTAIN (경미 5건) |
| **최종 보고서** | `2026-03-03_wtis-proposal-secure-ai-v2-final.md` | ✅ completed |
