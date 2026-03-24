---
type: weekly-monitor
domain: secure-ai
week: 2026-W13
date: 2026-03-24
l3_count: 5
deep_count: 2
---

# 주간 기술 동향: Secure AI (2026-W13)

## Executive Summary

> **이번 주 핵심**: 스팸/피싱 탐지는 SKT의 성문(voice-print) 기반 온디바이스 탐지 출시와 FCC SIP 603+ 의무화 마감(3/25)으로 통신사 보안의 제도화·고도화가 동시 진행. PQC는 중국의 독자 표준 3년 내 확정 선언(3/19)과 트럼프 행정부 사이버 전략(3/6)의 PQC 명시로 미·중 양대 축에서 표준화·규제 압박이 가속.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| 스팸/피싱탐지 | 스팸/피싱 감지(통화전) | 🟡 | SKT 에이닷 '위험 목소리 탐지' 성문 분석 추가(3/18), FCC SIP 603+ 마감(3/25), Adaptive Security $81M Series B |
| | OCR 활용 이미지 스팸 차단 | 🟢 | 구조적 변화 없음. Gmail RETVec/Gemini Nano 이미지 스팸 차단 지속 |
| 양자/동형 암호 | On-Device 양자암호(PQC) | 🟡 | 중국 PQC 독자 표준 3년 내 선언(3/19), 트럼프 사이버 전략 PQC 명시(3/6), SEALSQ 블록체인 PQC 배포(3/20) |
| | On-Device 동형암호 | 🟢 | Intel Heracles 후속 기사(3/19) 외 전주 대비 구조적 신규 발표 없음 |
| | Secure Vector Search | 🟢 | Hermes v2 논문 개정(3/16), PHE 대안 연구 외 상용 돌파 없음 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음

---

## 🟢 Quick 요약 (변화 미미)

### OCR 활용 이미지 스팸 차단
- Gmail TensorFlow 기반 이미지 스팸 탐지 일 1억건 추가 차단 지속. RETVec(Resilient & Efficient Text Vectorizer) 조작 텍스트 탐지 강화, Gemini Nano 온디바이스 보호 확대. 이번 주 구조적 변화 없음.

### On-Device 동형암호: 키워드 검색
- Intel Heracles FHE ASIC(Fully Homomorphic Encryption Application-Specific Integrated Circuit)이 Privacy Guides 등 미디어에서 지속 조명(3/19)되나 전주 ISSCC 2026 시연의 후속 보도이며 신규 기술 돌파 없음. GPU 기반 FHE 가속 연구(CUDA) 논문 게재(3/19). 전반적으로 전주 대비 소강 상태.

### Secure Vector Search: B2B AICC 동형암호 적용
- Hermes(FHE-native 벡터DB) v2 논문 개정(3/16): MySQL 네이티브 통합, 3,400× 암호화 처리량, 4,000× 삽입 속도 개선. PHE(Partially Homomorphic Encryption)가 엣지 기기 환경에서 FHE 대비 실용적 대안으로 연구 진행 중. 상용 돌파 없음.

---

## 🟡🔴 Deep 심층 분석

### 스팸/피싱 감지(통화전) — 🟡 주목

#### 이전 대비 변화
- 전주: P1 Vishing-as-a-Service($399/월) 실체 노출, Microsoft Teams Brand Impersonation Protection, Meta 전 플랫폼 AI 사기 탐지, KT 2.0 상용화
- 금주: SKT 에이닷 '위험 목소리 탐지' 성문 분석 추가(3/18), FCC SIP 603+ 의무화 마감(3/25), Adaptive Security $81M Series B, 온디바이스 AI 탐지 통신3사+삼성 전면 확산
- 변화 방향: 탐지 기술이 텍스트→성문(voice-print) 레이어로 확장. 규제(FCC 603+)가 analytics-based blocking 제도화. AI 딥페이크 방어 시장에 대형 VC 자금 유입

#### 기술 동향

1. **SKT 에이닷 '위험 목소리 탐지' — 온디바이스 성문 분석 추가 (3/18).**
   기존 텍스트 기반 통화 분석에 국립과학수사연구원(NFS) 보이스피싱 범죄자 성문(聲紋) 데이터와의 유사도 비교를 추가. 온디바이스 AI로 통화 데이터를 외부 전송 없이 단말 내 처리. 자체 평가 탐지 정확도 96%. ICT 규제 샌드박스 실증특례 승인으로 성문 민감정보 활용 근거 확보. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)

2. **FCC SIP 603+ 의무화 마감 — 2026년 3월 25일.**
   미국 FCC Eighth Report and Order에 따라 모든 통신사(Voice Service Provider)의 analytics-based call blocking에 SIP 603+("Network Blocked") 코드 사용 의무화. 기존 603/607/608 코드는 폐지. STIR/SHAKEN(Secure Telephone Identity Revisited / Signature-based Handling of Asserted information using toKENs)과 결합된 분석 기반 차단 투명성 제도화. 미국 Tier-1 사업자 간 서명 트래픽 85% 달성, 비Tier-1은 21%로 격차 존재. [[G-03]](#ref-g-03), [[G-04]](#ref-g-04)

3. **Adaptive Security $81M Series B — NVIDIA·OpenAI·a16z 투자.**
   Bain Capital Ventures 주도, NVentures(NVIDIA VC), OpenAI Startup Fund, Andreessen Horowitz(a16z), Citi Ventures, Capital One Ventures 참여. 누적 $146.5M. 500+ 엔터프라이즈 고객(PayPal, Bose, NHL, Xerox). AI 기반 딥페이크 음성·영상·문자 시뮬레이션으로 직원 교육 플랫폼 제공. 딥페이크 사고 17x 증가(2023→2024). [[G-05]](#ref-g-05)

4. **삼성전자·통신3사 온디바이스 보이스피싱 탐지 전면 확산.**
   삼성 Galaxy 본 전화앱 + SKT 에이닷 + KT 후후 + LGU+ 익시오(ixi-O)에서 온디바이스 AI 실시간 통화 분석 제공. 통화 데이터 외부 전송 없이 기기 내 처리로 프라이버시 보호. 과학기술정보통신부 'AI 기반 보이스피싱 공동 대응 플랫폼' 2026년 구축 착수. [[G-06]](#ref-g-06), [[G-07]](#ref-g-07)

5. **딥페이크 음성 위협 지표 악화 — 미국인 25% 수신 경험.**
   Hiya State of Call 2026: 미국인 1/4이 AI 생성 딥페이크 음성 통화 수신. 주당 9.9건 원치 않는 통화(+16% CAGR). 소비자 38%가 이통사 교체 의향. 딥페이크 비싱 2025 Q1에 전분기 대비 1,600% 급증. 음성 복제에 3초 오디오면 충분. [[G-08]](#ref-g-08)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| SKT | 에이닷 '위험 목소리 탐지' 3/18 출시. 국과수 성문DB+텍스트 분석 이중 체계. 정확도 96%. 규제 샌드박스 승인 | [[G-01]](#ref-g-01) |
| Samsung | Galaxy 본 전화앱에 온디바이스 AI 보이스피싱 탐지 내장. 통신3사와 협력 확대 | [[G-06]](#ref-g-06) |
| Adaptive Security | $81M Series B (NVIDIA·Bain·OpenAI). 500+ 기업 고객. 딥페이크 시뮬레이션 플랫폼 | [[G-05]](#ref-g-05) |
| FCC (미국) | SIP 603+ 의무화 3/25 시행. Analytics-based blocking 투명성 제도화 | [[G-03]](#ref-g-03) |
| 과기정통부 (한국) | AI 보이스피싱 공동 대응 플랫폼 2026년 구축 착수 | [[G-07]](#ref-g-07) |

#### 시장 시그널

**투자 & M&A**
- Adaptive Security $81M Series B (Bain·NVIDIA·OpenAI·a16z). 누적 $146.5M. AI 딥페이크 방어 시장 최대 규모 투자 중 하나 [[G-05]](#ref-g-05)

**시장 전망**
- 딥페이크 기반 사기 2027년 $40B 피해 전망. FTC 2024년 미국 사기 피해 $12.5B [[G-08]](#ref-g-08)
- 딥페이크 비싱 2025 Q1에 전분기 대비 1,600% 급증 (미국) [[G-08]](#ref-g-08)

**도입 사례**
- SKT 에이닷: 온디바이스 성문 분석 상용 서비스 — 통신사 최초 성문DB 기반 실시간 탐지 [[G-01]](#ref-g-01)
- FCC SIP 603+: 미국 전 통신사 analytics-based blocking 투명성 의무화 (3/25) [[G-03]](#ref-g-03)

#### 시장 수요 (voice-of-market)

이번 주 해당 기술 관련 컨퍼런스 영상에서 수요 시그널을 확인하지 못함.

#### 전략적 시사점

**기회**
- SKT 성문DB 기반 탐지의 ICT 규제 샌드박스 승인 선례 — 유사 기술 도입 시 규제 경로가 열린 상태
- FCC SIP 603+ 의무화는 analytics-based blocking의 글로벌 참조 모델 — 한국 통신 규제에도 유사 제도화 가능성
- 온디바이스 AI 탐지의 통신3사+삼성 전면 확산으로 "통화 보안"이 기본 기능으로 자리잡기 시작

**위협**
- Adaptive Security 등 SaaS 플랫폼이 기업 단위 딥페이크 방어를 직접 제공 — 통신사 부가서비스와 경쟁
- 딥페이크 음성 복제 진입장벽 극히 낮음(3초 오디오) — 공격 도구 진화 속도가 탐지 기술을 초과할 위험 지속

---

### On-Device 양자암호(PQC) — 🟡 주목

#### 이전 대비 변화
- 전주: Akamai TLS 전면 PQC 완료, Samsung Exynos 2600 HW-PQC 양산, QCi+Ciena 1.6Tb/s PQC+QKD OFC 시연
- 금주: 중국 PQC 독자 표준 3년 내 확정 선언(3/19), 트럼프 사이버 전략 PQC 명시(3/6), SEALSQ 블록체인 PQC 배포(3/20), HNDL 위협 경고 강화(3/23)
- 변화 방향: 기술 배포에서 규제·표준 제도화로 무게 중심 이동. 미·중 양대 축에서 PQC 표준화 동시 가속

#### 기술 동향

1. **중국, PQC 독자 표준 3년 내 확정 선언 (3/19).**
   중국 15차 5개년 계획에서 양자기술을 핵심 전략 산업으로 격상. 칭화대 왕샤오윈 교수(전인대 대표)가 "3~5년 내 PQC 산업 마이그레이션 폭발적 성장" 전망. NIST와 달리 "비구조 격자(structureless lattice)" 알고리즘(S-Cloud+) 중심으로 차별화. 금융·에너지 부문 우선 적용. [[G-09]](#ref-g-09), [[G-10]](#ref-g-10)

2. **트럼프 행정부 '사이버 전략 for America' — PQC 명시 (3/6).**
   6대 핵심 기둥에 Post-Quantum Cryptography(PQC) 포함: 연방 네트워크 현대화에서 "PQC, 제로 트러스트, 클라우드 전환" 명시. 핵심·신기술 부문에서 양자내성 암호화 지원 약속. 연방 기관의 PQC 마이그레이션에 공식 정책 근거 부여. [[G-11]](#ref-g-11), [[G-12]](#ref-g-12)

3. **SEALSQ, 블록체인·IoT 인프라에 PQC 배포 (3/20).**
   CRYSTALS-Kyber(Key Encapsulation Mechanism) + CRYSTALS-Dilithium(디지털 서명)을 시큐어 엘리먼트·TPM(Trusted Platform Module) 칩에 내장. WeCan(스위스 블록체인 금융) 협력으로 MPC(Secure Multi-Party Computation)+ZKP(Zero-Knowledge Proof)+HW 기반 ID 검증 통합. 위성 IoT에도 확대. [[G-13]](#ref-g-13)

4. **CISA PQC 제품 카테고리 리스트 발표 (1/23, 후속 영향 지속).**
   "Widely Available"(클라우드, 웹 브라우저, 엔드포인트 보안)과 "Transitioning"(네트워킹 HW/SW, 통신 장비, IAM) 2단계 분류. FIPS 203/204/205 구현 필수. 연방 조달의 PQC 우선 구매 기준. 통신 장비가 "Transitioning"에 포함되어 통신사 공급사의 PQC 대응 가속 예상. [[G-14]](#ref-g-14)

5. **HNDL 위협 경고 강화 — "양자 위협은 이미 활성 상태" (3/23).**
   Help Net Security: 적대국의 Harvest Now, Decrypt Later(HNDL) 데이터 수집이 현재 진행형. Crypto-agility(NIST CSWP 39, 2025-12 확정)가 필수 역량. 공급망 파트너의 암호화 취약점까지 점검 범위 확대 필요. [[G-15]](#ref-g-15)

6. **FIPS 140-2 종료 카운트다운 — D-181 (2026-09-21).**
   NIST CMVP(Cryptographic Module Validation Program)가 잔존 FIPS 140-2 인증 모듈을 Historical로 이전. 이후 신규 조달은 FIPS 140-3만 허용. [[G-16]](#ref-g-16)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| 중국 정부 | 15차 5개년 계획에서 양자기술 핵심 전략 산업 격상. 비구조 격자 PQC 독자 표준 3년 내 | [[G-09]](#ref-g-09) |
| 미국 백악관 | 사이버 전략 for America(3/6) PQC 명시. 연방 네트워크 현대화 포함 | [[G-11]](#ref-g-11) |
| CISA | PQC 제품 카테고리 리스트. 통신 장비 "Transitioning" 분류 | [[G-14]](#ref-g-14) |
| SEALSQ | 블록체인·IoT PQC 배포(3/20). CRYSTALS-Kyber/Dilithium TPM 내장 | [[G-13]](#ref-g-13) |

#### 시장 시그널

**시장 전망**
- PQC 시장 2025년 $10억 → 2035년 $450억(CAGR 43%) [[G-17]](#ref-g-17)
- "PQC 마이그레이션은 1조 달러 규모 과제" — GlobeNewswire [[G-18]](#ref-g-18)

**도입 사례**
- SEALSQ: CRYSTALS-Kyber/Dilithium을 TPM·시큐어 엘리먼트에 내장, 블록체인 금융 적용 (3/20) [[G-13]](#ref-g-13)
- CISA: 연방 조달에서 PQC 우선 구매 기준 제도화 [[G-14]](#ref-g-14)

#### 시장 수요 (voice-of-market)

이번 주 해당 기술 관련 컨퍼런스 영상에서 수요 시그널을 확인하지 못함.

#### 전략적 시사점

**기회**
- 미·중 동시 PQC 표준화 가속은 글로벌 마이그레이션 수요 폭발의 전조 — 한국 통신사의 PQC 서비스 차별화 시간 창 축소
- CISA "Transitioning"에 통신 장비 포함 — 통신사 장비 공급사의 PQC 대응이 가속될 것
- 트럼프 사이버 전략의 PQC 명시는 연방 고객 대상 PQC 서비스 시장 확대 신호

**위협**
- 중국 비구조 격자 표준이 NIST 표준과 비호환 시, 글로벌 통신 인프라의 이중 표준 부담
- FIPS 140-3 완전 PQC 인증 모듈 희소 → 규제 산업 조달 마찰 지속
- 3GPP PQC 표준화 지연(2027+)으로 VoLTE/VoNR 실시간 PQC는 at-rest 암호화에 우선 집중 필요

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 Secure AI 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 에이닷 '위험 목소리 탐지' 출시 | 국과수 성문DB 기반 화자 유사도 분석 추가. 텍스트+성문 이중 체계. 정확도 96%. ICT 규제 샌드박스 승인 | spam-phishing-detection | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |

### KT

이번 주 해당 도메인 관련 KT 신규 뉴스 없음. (전주: AI 보이스피싱 탐지 2.0 상용화, PQC+QKD 하이브리드 전략 공식화)

### 시사점
- SKT가 성문 분석 기반 온디바이스 탐지에서 선행. 규제 샌드박스 승인이라는 제도적 우위도 확보
- 다음 경쟁 포인트는 성문DB 규모·정확도 경쟁과 온디바이스 AI 모델 경량화 성능 차별화

---

## 규제 & 거버넌스

> Secure AI 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| FCC SIP 603+ Analytics-Based Blocking 의무화 (미국) | 2026-03-25 | D-1 |
| EU AI Act Article 6 (High-Risk AI 의무) | 2026-08-02 | D-131 |
| FIPS 140-2 인증 종료 (NIST CMVP Historical 이전) | 2026-09-21 | D-181 |
| 한국 AI 기본법 Article 31 (AI 생성 표시) | 2026-01-22 | 시행 중 |

### 신규 발의 & 가이드라인

- **트럼프 행정부 '사이버 전략 for America' (3/6)**: 연방 네트워크에 PQC·제로 트러스트·클라우드 전환 의무화. EO 14306 후속으로 PQC 마이그레이션 정책 근거 공식화 [[G-11]](#ref-g-11)
- **중국 15차 5개년 계획 — 양자기술 핵심 전략 산업 격상**: PQC 독자 표준 3년 내 확정 추진. 금융·에너지 우선 적용 [[G-09]](#ref-g-09)
- **NIST CSWP 39 (Crypto-Agility 가이드라인)**: 2025-12-19 확정. 암호 민첩성 성숙도 모델 제시. 조직의 PQC 전환 역량 자체 평가 프레임워크 [[G-15]](#ref-g-15)

### 시사점
- FCC 603+ 시행은 통신사 analytics-based blocking의 제도적 투명성 기준을 확립. 한국에도 유사 프레임워크 도입 논의가 발생할 가능성
- 미·중 양국의 PQC 표준화 동시 가속으로 글로벌 이중 표준 위험이 현실화. 통신 인프라 사업자의 crypto-agility(양쪽 표준 모두 대응) 역량이 핵심

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **온디바이스 AI의 이중 역할 — 탐지와 암호화**: 스팸/피싱 탐지(성문 분석)와 PQC(HW-PQC SoC)가 모두 온디바이스 기술에 의존하며, 통신사의 "스마트폰 보안" 포지셔닝이 두 축을 동시에 커버 가능

2. **규제 양면 가속**: FCC 603+(탐지 투명성)과 FIPS 140-2 종료(암호화 현대화)가 같은 시기에 진행. 통신사는 탐지와 암호화 양쪽에서 규제 대응이 동시에 필요

3. **미·중 PQC 표준 분열 위험**: 중국 비구조 격자 표준이 NIST 표준과 비호환 가능성 — 글로벌 통신 장비의 이중 표준 부담으로 이어질 수 있으며, crypto-agility 설계가 선택이 아닌 필수

### 후속 조치 제안

- 🟡 스팸/피싱 감지 — SKT 성문DB 탐지 성능 벤치마크 추적. FCC 603+ 모델의 한국 통신 규제 적용 가능성 모니터링
- 🟡 PQC — 중국 비구조 격자 표준의 NIST 호환성 추적. FIPS 140-2 종료(9/21) 대비 내부 인증 모듈 점검 지속. Crypto-agility 역량 자체 평가(CSWP 39) 검토
- 🟢 동형암호/Secure Vector Search — 전주 대비 소강. 다음 주 NIST Threshold Call 4/20 마감 전 FHE 표준화 진행 상황 모니터링

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | 전자신문 — SKT 에이닷 '위험 목소리 탐지' 적용 | [링크](https://www.etnews.com/20260318000294) | news | 2026-03-18 | [B] |
| <a id="ref-g-02"></a>G-02 | 뉴시스 — "검찰입니다" 그놈 말투 알아채는 AI | [링크](https://www.newsis.com/view/NISX20260318_0003553437) | news | 2026-03-18 | [B] |
| <a id="ref-g-03"></a>G-03 | ACA International — FCC Call Blocking Redress: Deadline March 25 | [링크](https://www.acainternational.org/news/fcc-call-blocking-redress-final-compliance-deadline-is-march-25/) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | TNS — 2026 Robocall Report: Going Further Than STIR/SHAKEN | [링크](https://tnsi.com/resource/com/tns-2026-robocall-report-going-further-than-stir-shaken-blog/) | report | 2026 | [B] |
| <a id="ref-g-05"></a>G-05 | PR Newswire — Adaptive Security $81M Series B | [링크](https://www.prnewswire.com/news-releases/adaptive-security-raises-81-million-series-b-to-stop-ai-powered-cyber-threats-302643174.html) | 보도자료 | 2026-01 | [A] |
| <a id="ref-g-06"></a>G-06 | HelloT — 통신3사·삼성전자 온디바이스 탐지 서비스 활성화 | [링크](https://www.hellot.net/news/article.html?no=110341) | news | 2026-02 | [B] |
| <a id="ref-g-07"></a>G-07 | 정책브리핑 — AI로 통화 중 보이스피싱 잡는다 | [링크](https://www.korea.kr/news/policyNewsView.do?newsId=148959497) | 공식 | 2026-03 | [A] |
| <a id="ref-g-08"></a>G-08 | Hiya / NatLawReview — State of the Call 2026 | [링크](https://natlawreview.com/press-releases/state-call-2026-ai-deepfake-voice-calls-hit-1-4-americans-consumers-say) | report | 2026-03-02 | [B] |
| <a id="ref-g-09"></a>G-09 | The Quantum Insider — China PQC Standards Within Three Years | [링크](https://thequantuminsider.com/2026/03/19/china-expects-post-quantum-cryptography-standards-within-three-years/) | news | 2026-03-19 | [B] |
| <a id="ref-g-10"></a>G-10 | QuantumZeitgeist — China Forecasts National PQC Standards | [링크](https://quantumzeitgeist.com/post-quantum-cryptography-china-forecasts/) | news | 2026-03-19 | [B] |
| <a id="ref-g-11"></a>G-11 | White House — President Trump's Cyber Strategy for America | [링크](https://www.whitehouse.gov/wp-content/uploads/2026/03/president-trumps-cyber-strategy-for-america.pdf) | 공식 | 2026-03-06 | [A] |
| <a id="ref-g-12"></a>G-12 | Sidley Data Matters — New Cyber Doctrine of the United States | [링크](https://datamatters.sidley.com/2026/03/10/the-new-cyber-doctrine-of-the-united-states/) | news | 2026-03-10 | [B] |
| <a id="ref-g-13"></a>G-13 | GlobeNewswire — SEALSQ PQC Blockchain Deployment | [링크](https://www.globenewswire.com/news-release/2026/03/20/3259796/0/en/SEALSQ-Deploys-Post-Quantum-Cryptography-to-Secure-Blockchain-and-Digital-Transaction-Infrastructures-Through-the-Deployment-of-Post-Quantum-Cryptographic-PQC-Technologies.html) | 보도자료 | 2026-03-20 | [A] |
| <a id="ref-g-14"></a>G-14 | CISA — PQC Product Categories List | [링크](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards) | 공식 | 2026-01-23 | [A] |
| <a id="ref-g-15"></a>G-15 | Help Net Security — Quantum Threats Active, Defense Fragmented | [링크](https://www.helpnetsecurity.com/2026/03/23/ciso-post-quantum-crypto-agility/) | news | 2026-03-23 | [B] |
| <a id="ref-g-16"></a>G-16 | SafeLogic — FIPS 140-2 September 21, 2026 | [링크](https://www.safelogic.com/blog/what-happens-on-september-21-2026) | blog | 2026 | [B] |
| <a id="ref-g-17"></a>G-17 | OpenPR — PQC Market Surge Toward Multi-Billion by 2035 | [링크](https://www.openpr.com/news/4433132/post-quantum-cryptography-market-poised-to-redefine-global) | report | 2026-03 | [C] |
| <a id="ref-g-18"></a>G-18 | GlobeNewswire — PQC Migration Trillion-Dollar Imperative | [링크](https://www.globenewswire.com/news-release/2026/02/19/3241234/0/en/Post-Quantum-Cryptography-Migration-Is-Now-a-Trillion-Dollar-Imperative.html) | news | 2026-02-19 | [B] |
| <a id="ref-e-01"></a>E-01 | SKT Newsroom — 에이닷 AI 보이스피싱 탐지 | [링크](https://news.sktelecom.com/217274) | 보도자료 | 2026-03-18 | [A] |
