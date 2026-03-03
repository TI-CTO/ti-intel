---
topic: Secure AI - B2C Voice Call Security (v3 — validator 이슈 해소)
date: 2026-02-26
agent: research-deep
version: v3 (validator UNCERTAIN 해소 전용)
confidence: high
status: completed
sources_used: [websearch, webfetch, prior_reports]
mcp_status: "MCP 도구 미작동 (VSCode 확장 환경 제약) — WebSearch + WebFetch + 내부 문서 폴백. v2 대비 개선: validator UNCERTAIN 이슈 5건 전면 해소. 신규 출처 14개 추가 확보."
prior_reports:
  - path: /Users/ctoti/Project/ClaudeCode/outputs/reports/2026-02-26_wtis-proposal-secure-ai-research-v2.md
    verdict: Conditional Go (통과)
    validator_status: UNCERTAIN (고아 인용 5건, 수치-소스 불일치 2건, 연도 혼선 1건)
---

# Research Report: Secure AI — B2C 통화 보안 (v3)

## Executive Summary (경영진 요약)

> 본 보고서(v3)는 validator v3가 UNCERTAIN 판정으로 지적한 7개 이슈를 전면 해소하는 데 집중한다. 핵심 발견: (1) 2024년 보이스피싱 피해액 8,545억 원은 2023년 4,472억 원 대비 **+91% 증가**이며, "+335%"는 2023년 금감원 기준(1,965억)→경찰청 2024년 기준(8,545억) 간 집계 기준 차이에서 발생한 오류 수치로 본문에서 삭제 필요하다. (2) "1인당 5,290만원"은 2025년 1~10월 경찰청 발표 수치로 공식 확인되었다. (3) 고아 인용 5건(G-17~G-19, G-21, G-23) 모두 본문에서 직접 활용 가능한 맥락을 부여했다. (4) 삼성 갤럭시 S26 보이스피싱 탐지는 한국어 기준 경찰청·국과수 데이터 학습 기반 온디바이스 탐지(자체 기능)와 Gemini 기반 탐지(영어 미국 한정)의 두 레이어로 구성됨을 확인했다. (5) Zama TFHE GPU 부트스트래핑이 <1ms(H100 기준)를 달성했으나, 64비트 암호화 곱셈이 32ms(8xH100 기준)로 실음성 스트림 처리에는 여전히 현실적이지 않다. 전략적 신뢰도: 핵심 기술 판단 [A], 시장 수치 [B] 수준.

---

## 연구 질문

> validator v3가 UNCERTAIN으로 판정한 이슈 7건의 전면 해소를 목표로: (Q1) "+335%" 수치의 정확한 출처 및 산출 근거 확인, (Q2) "1인당 5,290만원" 공식 출처 확정, (Q3) N-04/N-10 연도 불일치 해소, (Q4) G-17~G-19(시장 규모), G-21(MSIT 무선회선), G-23(Cisco 지연) 고아 인용 5건의 본문 활용 맥락 부여, (Q5) 삼성 S26 탐지 기능 한국 사양 확인, (Q6) FHE/TFHE 최신 성능 개선 동향 확인, (Q7) 정부 공동대응 플랫폼 최신 진행 현황. 이전 분석(I-02)의 핵심 발견은 유지하며, 신규 독립 출처 최소 10개 추가 확보.

---

## 이전 분석 대비 변화

| 항목 | 이전 (v2) | 현재 (v3) | 변화 |
|------|---------|---------|------|
| "+335% 폭증" 수치 근거 | N-03 (세계일보 Q1 기사) — 소스 불일치 [D] | 경찰청 집계 기준 상이 확인. 2023→2024 YoY는 +91% (4,472→8,545억). "+335%"는 금감원-경찰청 기준 혼용 오류로 삭제 권고 | 수치 수정 |
| "1인당 5,290만원" 출처 | N-04, N-10 파생 계산 추정 [C] | 더시사법률(경찰청 국수본 인용): 2025년 1~10월 기준 5,290만원 공식 확인 [B→A] | 출처 확정 |
| N-04/N-10 연도 혼선 | N-04(2025년) vs N-10(2024년) — "1조 2,578억" 연도 불일치 | N-10 요약 오기 확인: N-10 기사(뉴시스/2025.11.24)는 2024년 연간 1조 2,578억을 기재했으나 실제 피해액 1조 2,578억은 2025년 연간 수치(헤럴드경제 N-04 기준). 2024년 연간은 8,545억. | 연도 명확화 |
| G-17 (DataIntelo 콜센터 시장) | References만 존재, 본문 미인용 — 고아 인용 | 섹션 2.2에서 콜센터 사기 탐지 AI 시장 세그먼트 데이터로 직접 인용 | 고아 인용 해소 |
| G-18 (MRF 음성 분석 시장) | References만 존재, 본문 미인용 — 고아 인용 | 섹션 2.2에서 광의 Voice Analytics 시장 데이터로 직접 인용 | 고아 인용 해소 |
| G-19 (Allied MR 음성 분석 시장) | References만 존재, 본문 미인용 — 고아 인용 | 섹션 2.2에서 Allied MR 2023→2032 예측으로 직접 인용, MnM 수치와 교차 검증 | 고아 인용 해소 |
| G-21 (MSIT 전체 무선회선 9,079만) | References만 존재, 본문 미인용 — 고아 인용 | 섹션 2.3에서 G-20(휴대폰 5,724만)과 G-21(전체 무선 9,079만)의 구분 논거 명시 | 고아 인용 해소 |
| G-23 (Cisco 지연 기준) | References만 존재, 본문 미인용 — 고아 인용 | 섹션 1.1에서 ITU-T G.114와 함께 HE 실시간 불가 판정의 이중 기준으로 직접 인용 | 고아 인용 해소 |
| 삼성 S26 탐지 사양 | 영어 미국 한정(Gemini 기반) 단일 설명 | 한국어 기반 자체 온디바이스 탐지(경찰청·국과수 데이터)와 Gemini 기반 탐지(영어·미국) 분리 확인 | 사양 정확화 |
| TFHE 최신 성능 | ~13ms per binary gate (CPU, 2020년) | Zama TFHE-rs v1.4: H100 GPU 기준 <1ms bootstrapping. 그러나 64비트 암호화 곱셈 32ms(8xH100) — 실음성 처리 여전히 비현실적 | 성능 업데이트 |
| LGU+ 익시오 최신 성과 | 5,500건 탐지 (2025 상반기), KB국민은행 1,720억 예방 | 익시오 프로(MWC 2026 공개): 월 2,000건 탐지, 악성 앱 서버 800개 추적, 고객 3만 3,000명 경찰 전달. 향후 HE 적용 계획 언급 | 성과 업데이트 |

---

## 1. 기술 현황

### 1.1 동형암호 (Homomorphic Encryption) — V4 검증 [Critical Risk 유지]

**결론: 최신 GPU 가속으로 단일 bootstrapping <1ms 달성. 그러나 실음성 스트림 처리에는 여전히 현실적이지 않음. "불가" 판정은 유지.**

**최신 Zama TFHE-rs v1.4 (2025년 9월) 성능 [G-24]:**

| 연산 | H100 GPU 1개 | 8xH100 노드 | CPU 대비 개선 |
|------|------------|-----------|-------------|
| 4비트 bootstrapping | ~945µs (< 1ms) | - | 56배 향상 (53ms → 945µs) |
| Boolean bootstrapping | ~796µs | - | 24배 향상 |
| 64비트 암호화 덧셈 | - | 8.7ms | 230배 향상 |
| 64비트 암호화 곱셈 | - | 32ms | 406배 향상 |

**통화 실시간 요건 대비 재평가:**

ITU-T G.114 권장 기준: 편도 **150ms** (0~150ms 고품질, 150~400ms 허용) [G-22].
Cisco 실무 기준: 200ms 적정, 250ms 한계 — 지연 분해: 코덱 2.5~10ms, 패킷화 20~30ms, 네트워크 가변 [G-23].

GPU 가속 최신 성능(8xH100)에서도 64비트 암호화 곱셈이 **32ms**이며, 이는 단일 연산 기준이다. 실제 음성 스트림(16kHz 샘플링, 연속 처리)에 HE 적용 시 수백~수천 연산이 필요하므로 누적 지연은 수십 초 이상으로 ITU-T G.114 기준 150ms [G-22]나 Cisco 실무 기준 250ms [G-23]를 모두 초과한다. 또한 H100 GPU는 단말 탑재가 불가능한 서버급 하드웨어다.

**추가 확인: LGU+ 익시오 프로 HE 적용 계획 [N-16]:**
LGU+는 MWC 2026에서 익시오 프로를 공개하며 "향후 동형암호를 익시오에 적용해 데이터 유출을 원천 차단할 계획"을 명시했다. 이는 현재 실시간 통화 적용이 아닌 **데이터 저장·처리 단계의 비실시간 HE 적용**을 의미하며, 본 보고서의 "실시간 통화 HE 불가" 판정과 충돌하지 않는다.

**TRL 판정 (B2C 통화 보안 맥락, v3 업데이트):**
- HE 알고리즘 (GPU 가속): TRL 5~6 (실험실-파일럿. GPU 서버 기반)
- 실시간 통화 HE 적용 (단말): TRL 2~3 (개념 증명 단계 — H100 GPU조차 32ms로 불가)
- 비실시간 데이터 분석 HE (클라우드): TRL 4~5 (전용 프로토콜 필요 [P-04])

---

### 1.2 온디바이스 AI 보이스피싱 탐지 — V5 검증 [TRL 7~8, 확인 유지]

**결론: v2 판정 유지. 삼성 S26의 한국어 기반 자체 온디바이스 탐지(자체 딥러닝)와 Gemini 기반 스캠 탐지(영어·미국 한정)가 별도 레이어로 확인됨.**

**삼성 갤럭시 S26 탐지 기능 — 한국 사양 [E-01, N-06]:**

| 레이어 | 기술 방식 | 언어/지역 | 특징 |
|--------|---------|---------|------|
| 자체 딥러닝 탐지 | 경찰청·국과수 보이스피싱 데이터 3만건 학습, 온디바이스 AI | **한국어 지원** | Phone 앱 기본 탑재, One UI 8.0+ 전 갤럭시 |
| Gemini 기반 스캠 탐지 | 온디바이스 Gemini 모델 로컬 실행, 통화 중 대화 패턴 분석 | **영어, 미국 한정** | Galaxy S26 시리즈에서 먼저 출시 |

**핵심 시사점:** 국내 한국어 사용자 대상으로는 **경찰청·국과수 데이터 학습 기반 자체 탐지**가 작동한다. 이는 국내 보이스피싱 패턴에 특화된 탐지로, 통신사 앱과 병렬 지원된다 [E-01]. Gemini 기반 탐지는 현재 영어·미국 한정이므로 한국어 사용 맥락에서의 위협은 자체 탐지 레이어가 주된 경쟁 요소다.

**Apple iOS 26 Call Screening — v3 업데이트 [N-17]:**
- 완전 온디바이스 처리: 모든 오디오·전사본 iPhone 내 저장, 서버 전송 없음
- 미지 번호 자동 응대: AI가 발신자 이름·목적 확인 후 사용자에게 전달
- 설정 옵션 3가지: Never / Ask Reason for Calling / Silence
- iPhone 11 이상 호환 (iOS 26 설치 시)
- 현재 iOS 26 Call Screening은 한국 출시 여부 미확인 — 언어 지원 범위 추가 확인 필요 [D]

---

### 1.3 양자내성암호 (PQC) — V3 검증 [TRL 5~6, 확인 유지]

**결론: v2 판정 유지. NIST ML-KEM 표준 배포 진행 중, 3GPP·IETF 프로토콜 통합 작업 중.**

**2025~2026년 PQC 배포 현황 [G-25]:**
- X25519MLKEM768 (X25519+ML-KEM-768 하이브리드): 널리 배포 중, TLS·IPsec에 Hybrid 방식으로 적용
- IETF: TLS, IPSec 등 핵심 프로토콜 PQC 알고리즘 지원을 위한 개정 진행 중
- 3GPP: 5G-Advanced/6G PQC 통합 표준화 진행 중 (공식 배포 전 Hybrid 방식 사용)
- NIST: PQC 인증서 최초 상업 배포는 **2026년** 예상, 전체 신뢰 체계 확립은 **2027년 이후**
- GSMA PQ.03 v2.0: VoLTE/VoNR IMS 적용 시 SIP 시그널링 + 미디어 보안(SRTP) 모두 PQC 전환 필요 — 단말 통합은 여전히 벤더 의존 [G-08]

**TRL 판정 (v3 유지):**
- PQC 알고리즘: TRL 7~8
- 5G/VoLTE 실제 통합: TRL 5~6 (파일럿)
- 단말-네트워크 E2E PQC 암호화: TRL 4~5

---

## 2. 시장 동향

### 2.1 국내 보이스피싱 피해 통계 — V1, Q1, Q2, Q3 완전 해소

**핵심 수정 사항: "+335%" 수치는 집계 기준 차이에서 발생한 오류이며 삭제 권고. "1인당 5,290만원"은 공식 확인.**

**연도별 피해 통계 확정 (집계 기관별 구분):**

| 연도 | 피해액 | 전년 대비 | 1인당 피해 | 발생 건수 | 집계 기관 | 신뢰도 |
|------|--------|---------|---------|---------|---------|--------|
| 2021 | 7,744억 원 | - | 2,498만 원 | - | 경찰청 국수본 | [A] |
| 2022 | 1,451억 원 | - | - | - | 금감원 | [A] |
| 2023 (금감원 기준) | 1,965억 원 | +35.4% | 1,710만 원 | - | 금감원 | [A] [N-11] |
| 2023 (경찰청 기준) | 4,472억 원 | - | - | - | 경찰청 국수본 | [A] [N-20] |
| 2024 | **8,545억 원** | +91% (경찰청 2023년 대비) | 2,498만 원→상승 | 18,902건 | 경찰청 국수본 | [A] [N-20] |
| 2025 (1~10월) | 1조 566억 원 | 2024 연간 대비 24%↑ | **5,290만 원** | 19,972건 | 경찰청 국수본 | [A] [N-18] |
| 2025 (연간 확정) | **1조 2,578억 원** | +47.2% (2024 연간 대비) | - | 20,893건 | 경찰청 국수본 | [A] [N-04] |
| 2025 Q1 | 3,116억 원 | 2024 동기 대비 +2.2배 | 5,384만 원 | 5,878건 | 경찰청 국수본 | [A] [N-03] |

**"1인당 5,290만원" 출처 확정 [N-18]:**
더시사법률(경찰청 국수본 공식 자료 인용): "1인당 평균 피해액 5,290만원"은 **2025년 1~10월** 기준 경찰청 국수본 공식 발표 수치다. 이는 2021년 1인당 2,498만원 대비 약 2배 증가한 수치다.

**"+335% 폭증" 수치 확정 해소:**

세계일보(N-03) Q1 2025 기사의 "+335%" 수치 원문 확인 불가. 계산 검증:
- 금감원 집계: 2022년 1,451억→2023년 1,965억 (+35.4%)
- 경찰청 집계: 2023년 4,472억→2024년 8,545억 (+91%)
- 다른 경로: 2021년 7,744억→2022년 1,451억 (-81% 감소), 2022년→2024년 8,545억 = 2022년 대비 +489%

"+335%"는 어떤 연도 조합에서도 정확히 일치하지 않는다. 금감원-경찰청 집계 기준 혼용(금감원 2023년 1,965억 대비 경찰청 2024년 8,545억 = +335.3%)으로 발생한 수치로 추정되며, **동일 집계 기관 기준의 YoY 비교가 아님**. 본문에서 이 수치를 삭제하고, 경찰청 집계 기준 "+91% (2023→2024)"로 교체 권고.

**N-04/N-10 연도 불일치 해소:**

| 소스 | 발행일 | 수치 | 기준 연도 |
|------|--------|------|---------|
| N-04 (헤럴드경제) | 2026.01 | 1조 2,578억 원 | **2025년** 연간 확정 |
| N-10 (뉴시스) | 2025.11.24 | 1조 566억 원 (1~10월), "2024년 연간 1조 2,578억 원" | **오기** — 2024년 연간은 8,545억원. 뉴시스 N-10은 2025년 1~10월 통계를 발표했으며, N-10 References 요약에 "2024년 연간 1조 2,578억원"으로 기재된 것은 요약 오류다. |

**판정: 1조 2,578억 원은 2025년 연간 최종 확정 수치(N-04 기준 [A]). N-10은 2025년 1~10월 중간 통계(1조 566억 원)를 제공. 두 소스가 다른 집계 기간을 다루며 동일 수치를 가리키지 않는다.**

---

### 2.2 통화 보안 시장 규모 — G-17, G-18, G-19 고아 인용 해소

**글로벌 관련 시장 세그먼트 비교 (4개 독립 기관 교차 검증):**

| 시장 구분 | 2023/2024 규모 | 예측 규모 | CAGR | 기관 | 코드 | 신뢰도 |
|----------|--------------|---------|------|------|------|--------|
| **AI 음성 사기 탐지** | $2.36B (2024) | $12.16B (2033) | 18.7% | DataIntelo | [G-16] | [B] |
| **콜센터 사기 탐지 AI** | $1.92B (2024) | $8.60B (2033) | **19.7%** | DataIntelo | [G-17] | [B] |
| **Voice Analytics (광의)** | $3.69B (2024) | $13.73B (2035) | 12.68% | Market Research Future | [G-18] | [B] |
| **Voice Analytics (Allied)** | $1.3B (2023) | $6.7B (2032) | **19.6%** | Allied Market Research | [G-19] | [B] |
| **Voice Analytics (MnM)** | $1.6B (2024 est.) | - | 19.4% | MarketsandMarkets | [G-26] | [B] |
| Fraud Analytics 국제음성 | $1.87B (2024) | $5.49B (2033) | 14.2% | GrowthMarketReports | [G-14] | [C] |
| Fraud Detection & Prevention (전체) | $33.1B (2024) | $90.1B (2030) | 18.7% | Grand View Research | [G-27] | [B] |

**교차 검증 결과:**

1. **콜센터 사기 탐지 AI 시장(G-17: $1.92B, CAGR 19.7%)**: DataIntelo 단일 소스이나, Allied MR Voice Analytics CAGR(19.6% [G-19])과 MnM CAGR(19.4% [G-26])이 유사 범위. 성장률 방향성 확인 [B]. 시장 규모 절대값은 시장 정의 범위에 따라 편차 존재.

2. **Voice Analytics 시장(G-18: $3.69B, CAGR 12.68%)**: MRF는 광의 정의(고객 서비스·마케팅 포함). Allied MR($1.3B, CAGR 19.6% [G-19])과 MnM($1.6B, CAGR 19.4% [G-26])은 협의 정의. 광의-협의 차이로 규모 차이가 발생하지만 성장 방향성(12~20% CAGR)은 일관 [B].

3. **LGU+ 관련 TAM**: 국내 B2C 통화 보안 서비스 독립 시장 규모 공개 리서치 부재. 공개 정보 없음 — "공개 정보 없음" 처리 유지.

---

### 2.3 국내 이동통신 가입자 TAM — G-20/G-21 구분 논거 확정

**MSIT 공식 통계 기준 TAM 산정 [G-20, G-21]:**

| 지표 | 수치 | 기준 | 출처 |
|------|------|------|------|
| **이동통신 휴대폰 회선** | **5,724만 회선** | 2025년 5월 기준 | MSIT [G-20] |
| SKT 점유율 | 2,249.9만 (39.3%) | 동일 | [G-20] |
| KT 점유율 | 1,361.1만 (23.8%) | 동일 | [G-20] |
| LGU+ 점유율 | 1,113.1만 (19.5%) | 동일 | [G-20] |
| MVNO 점유율 | 999.8만 (17.5%) | 동일 | [G-20] |
| **전체 무선회선 (IoT 포함)** | **9,079만 회선** | 2025년 7월 기준 | MSIT [G-21] |

**TAM 산정 논거:**

보이스피싱 탐지 서비스의 실질적 TAM은 **이동통신 휴대폰 회선 5,724만** [G-20]이다. 전체 무선회선 9,079만 [G-21]은 스마트워치·태블릿·자동차 통신 모듈·IoT 센서 등을 포함하며, 이들 기기는 보이스피싱 탐지 서비스의 실질적 수요자가 아니다. 따라서:
- **TAM(전체 시장)**: 5,724만 휴대폰 회선 [G-20]
- LGU+ SAM: 약 1,113만 회선 (19.5% 점유율 [G-20])
- 9,079만 [G-21]은 MVNO 포함 무선 인프라 현황 파악 용도로, 서비스 시장 규모 산정에는 적합하지 않음

---

## 3. 경쟁사 동향

### 3.1 삼성전자 갤럭시 S26 — 최신 사양 확정 [E-01, N-06, N-17]

**한국 출시 기준 보이스피싱 탐지 기능:**

| 구분 | 기술 방식 | 언어/지역 | 출처 |
|------|---------|---------|------|
| 보이스피싱 의심 전화 알림 (한국) | 경찰청·국과수 데이터 3만건 딥러닝 학습, 온디바이스 | **한국어 지원** | [E-01] |
| Gemini 기반 스캠 탐지 | 온디바이스 Gemini 로컬 실행, 통화·문자 패턴 분석 | **영어, 미국 한정** (2026.03 기준) | [N-06] |
| 탐지 알림 방식 | '의심' / '경고' 2단계 알림 (팝업 + 햅틱) | - | [E-01] |
| 배포 범위 | Galaxy S26 시리즈 (2026.03.11 출시), One UI 8.0+ 업데이트 시 구형 갤럭시도 적용 | - | [E-01] |

**과기정통부 공동 플랫폼 최신 현황 [N-19]:**
- 과기정통부 AI 민생 10대 프로젝트: 'AI 기반 보이스피싱 통신서비스 공동대응 플랫폼' 구축 (2026~2027년)
- 경찰청·한국인터넷진흥원 등과 데이터 실시간 수집·분석·공유 체계 구축 계획
- 2026년 2월 현재: 삼성전자+SKT+KT+LGU+ 4사 온디바이스 AI 탐지 서비스 병렬 운영 중
- 규제 특례(규제샌드박스) 적용으로 상용화 지원

---

### 3.2 SKT 스캠뱅가드 — 2025~2026 최신 성과 [E-02]

**2025년 연간 성과 (공식 발표):**
- 통신 사기 시도 총 **11억 건 차단** (전년 대비 +35%) [E-02]
- 음성 스팸·보이스피싱 통화: 전년 대비 +119%, **2억 5천만 건 차단** [E-02]
- 스팸 문자: 전년 대비 +22%, 8억 5천만 건 차단

**2026년 계획:**
- 스팸·피싱 차단 전 과정에 AI 기술 단계적 확대 적용 예고
- IBK기업은행 AI 보이스피싱 탐지 기술 이전(B2B 파트너십 확대) [E-02]

**공개 스펙:** 탐지율 공개 정보 없음 / 지연 공개 정보 없음 / 가격 공개 정보 없음

---

### 3.3 KT AI 보이스피싱 탐지 2.0 — 최신 성과 [E-03]

**2025년 상반기~하반기 성과:**

| 지표 | 수치 | 기간 |
|------|------|------|
| 탐지 정확도 | 91.6% (H1 평균) | 2025년 상반기 |
| 분석 통화량 | 1,460만 건 | 2025년 H1 |
| 피해 예방액 | **약 1,300억 원** | 2025년 연간 |
| 2.0 목표 탐지율 | 95%+ | 2026년 목표 |
| 2.0 피해 예방 목표 | 2,000억 원+/년 | 2026년 목표 |

**2025년 7월 2.0 출시 신규 기능:** 화자인식(국과수 '그놈목소리' 성문 데이터) + 딥보이스 탐지 통합. 온디바이스, 통화 내용 서버 미저장.

---

### 3.4 LGU+ 익시오 / 익시오 프로 — 최신 성과 [E-04, N-16]

**익시오 현황 (2025~2026.02):**

| 지표 | 수치 | 비고 |
|------|------|------|
| 월 탐지 건수 | 약 2,000건 | 2025년 월 평균 |
| 누적 탐지 총건 | 5,500건 (2025 H1) → 추가 누적 중 | [E-04] |
| 악성 앱 서버 추적 | 800개 (2025년) | [N-16] |
| 피해 예방 고객 | 3만 3,000명 (경찰 전달) | [N-16] |
| 금융연계 피해 예방 | 1,720억 원 (KB국민은행 협력) | [E-04] |
| 악성 앱 추적 기여 | 전체 보이스피싱 신고 중 23% | [N-16] |

**익시오 프로 (MWC 2026, 2026.02.23 공개) [N-16]:**
- 기존 익시오: 사용자 호출 대응형 → 익시오 프로: 선제적 정보 제공형 (AI 콜 에이전트)
- 통화·문자·일정 통합 분석, 맥락 기반 선제 안내
- 보이스피싱 탐지 유지: 통화 중 의심 패턴, 악성 앱, 위험 URL 실시간 감지 → 금융사 공유
- **동형암호 적용 계획**: "향후 익시오에 HE 적용해 복호화 없이 데이터 활용 예정" — 비실시간 데이터 보호 목적 [N-16]
- 확장 비전: 스마트폰 → 집·오피스·차량·로봇 등 보이스 기반 슈퍼 에이전트

**MWC 2026 LGU+ AI·양자 기반 보안 기술 공개 [N-21]:**
- PQC 기반 통화 암호화 기술 시연
- 익시오 프로 + KB국민은행 연계 실시간 대응 체계 시연

---

### 3.5 Pindrop — 글로벌 기준선 [G-09, N-08]

- 탐지율 최대 80%, FP <0.5%, 1,300개 음향 피처 [G-09]
- BT 엔터프라이즈와 딥페이크 탐지 통합 파트너십 (2025.11) [N-08]
- B2B Contact Center 특화 — 국내 B2C 직접 경쟁 아님

---

## 4. 제품/서비스 스펙 비교

| 기업 | 탐지율 | 지연시간 | 가격(정책) | 종합평가 | 발표/출시 | 출처 |
|------|--------|---------|-----------|---------|---------|------|
| KT AI 보이스피싱 탐지 2.0 | 91.6% (H1), 목표 95%+ | 공개 정보 없음 | 공개 정보 없음 (무료 추정) | 화자인식+딥보이스 통합, 규제샌드박스 승인, 1,300억 예방 | 2025.07 | [E-03] |
| SKT 스캠뱅가드 + 에이닷 | 공개 정보 없음 | 공개 정보 없음 | 공개 정보 없음 (에이닷 무료) | 11억 건/년 차단, CES·MWC 수상 | 2024~2025 | [E-02] |
| LGU+ 익시오 프로 | 공개 정보 없음 | 5초 내 탐지 목표 | 공개 정보 없음 (무료 포함) | 악성 서버 800개 추적, 금융 연계 1,720억 예방, 익시오 프로 MWC 2026 | 2024.11 출시, 2026.02 프로 공개 | [E-04, N-16] |
| 삼성 갤럭시 S26 (한국어 자체 탐지) | 공개 정보 없음 | 공개 정보 없음 | **무료** (기본 탑재) | 국과수 데이터 3만건 학습, One UI 8.0+ 전 갤럭시, 2단계 알림 | 2026.03.11 출시 | [E-01] |
| 삼성 갤럭시 S26 (Gemini 스캠 탐지) | 공개 정보 없음 | 공개 정보 없음 | **무료** (기본 탑재) | 영어·미국 한정, 온디바이스 Gemini 로컬 | 2026.03.11 | [N-06] |
| Apple iOS 26 Call Screening | 공개 정보 없음 | 공개 정보 없음 | **무료** (OS 기본) | 완전 온디바이스, 발신자 AI 대리 응대, 한국 지원 여부 미확인 | 2025.09 출시 | [N-17] |
| Pindrop (B2B Contact Center) | 최대 80%, FP <0.5% | 공개 정보 없음 | 엔터프라이즈 계약 | 1,300개 음향 피처, BT 파트너십 | 2025 | [G-09] |

> **주:** 국내 통신 3사 모두 탐지율·지연 공개 없음. LGU+ 익시오의 "5초 내 탐지"는 목표 수치이며 공식 실측치 아님.

---

## 5. 학술 동향 (v3 신규 확인)

### 5.1 FHE 최신 성능 — Zama TFHE-rs v1.4 [G-24]

**v3 신규:** Zama TFHE-rs v1.4 (2025.09 발표) — H100 GPU 1개 기준 bootstrapping <1ms 달성.

- CPU 대비: Boolean 24배, 4비트 정수 56배 향상
- 8xH100 노드: 64비트 암호화 곱셈 32ms, 덧셈 8.7ms
- 2026.03 FHE.org 2026에서 "Sub-millisecond TFHE bootstrapping on GPU" 발표 예정
- **음성 처리 직접 적용 언급 없음** — 블록체인·정수 연산 특화

**평가:** GPU 가속으로 단일 연산은 <1ms 달성했으나, 음성 스트림(연속 수백~수천 연산)에는 여전히 비현실적. 단말 탑재 불가(H100 서버급). HE 불가 판정 유지.

### 5.2 PQC 배포 현황 — 2025~2026 [G-25]

- ML-KEM·ML-DSA·SLH-DSA FIPS 표준 확정
- HQC 추가 KEM 선정 (2025.03, NIST 4라운드)
- 5G·VoLTE 통합: 3GPP 표준화 진행 중 — 공식 배포 전 Hybrid 사용 권장
- 첫 상업용 PQC 인증서: **2026년** 예상, 광범위 신뢰 체계: **2027년 이후**

기존 학술 논문 (P-01~P-11) 판정 유지. v3에서는 FHE GPU 성능 업데이트와 PQC 배포 타임라인이 주요 신규 발견이다.

---

## 6. 특허 동향

T-01~T-05 판정 v2에서 확정, v3 유지. 추가 신규 특허 발견 없음.

**요약:**
- Wells Fargo [T-03], Bank of America [T-04]: 금융사 독자 합성 음성 탐지 특허 트렌드 확인
- Google [T-01]: 보이스피싱 실시간 탐지 핵심 특허 보유
- Samsung [T-02]: HE 가속 반도체 특허 — 장기 단말 HE 가능성 시사

---

## 7. 기업 발언 & 보도자료

**LGU+ (2026.02.23, MWC 2026 익시오 프로 공개):** [N-16]
> "익시오 프로는 대화의 흐름과 관계 맥락을 이해해 필요한 정보를 먼저 제시한다. 보이스피싱 탐지 기능도 고도화해 통화 중 의심 패턴과 악성 앱 설치 여부를 실시간 감지하고 해당 정보를 금융사와 공유한다. 향후 동형암호 기술을 익시오에 적용해 데이터 유출을 원천 차단할 계획이다."

**LGU+ CISO 홍관희 (2025, 보안퍼스트 전략 발표):** [N-16]
> "보이스피싱 범죄에 통신사, 단말 제조사, 금융기관, 정부가 함께 대응하는 공·민간 사이버보안 협의체 구성을 제안한다."

**삼성전자 뉴스룸 (2026.02.25):** [E-01]
> "경찰청과 국립과학수사연구원에서 2024년부터 제공된 보이스피싱 데이터 약 3만 개를 기반으로 딥러닝 학습을 거쳐, 기기 내(On-Device) AI 기술로 보이스피싱 여부를 탐지하는 솔루션을 개발했다. One UI 8.0 이상 갤럭시 스마트폰에 기본 탑재되는 전화 앱에서 사용 가능하다."

**과기정통부 (2026.02.12):** [N-19]
> "보이스피싱 피해 방지를 위해 삼성전자, 이동통신 3사(SKT·KT·LGU+)가 제공하는 인공지능 기반 보이스피싱 탐지·알림 서비스를 이용해 주기를 바란다. 통화 내용 분석은 모두 외부 서버가 아닌 스마트폰 기기 자체의 인공지능(On-Device AI) 기반으로 이뤄진다."

**Google (2026.02, Galaxy S26 Scam Detection 발표):** [N-06]
> "Scam Detection analysis happens entirely on your device, and the feature is automatically off for anyone in your contacts. However, Scam Detection on the Galaxy S26 series is limited to English speakers in the US."

**KT (2025.12, 연간 성과 발표):** [E-03]
> "AI 보이스피싱 탐지 서비스를 통해 2025년 약 1300억원 규모의 보이스피싱 피해를 예방했다. 2.0 버전을 통해 2026년 연간 2,000억원 이상 피해 예방과 95% 이상 탐지율 달성을 목표로 한다."

**SKT (2026.01, 2025년 연간 실적 발표):** [E-02]
> "AI로 스팸·피싱 35% 더 잡았다. 지난해 음성 스팸·보이스피싱 통화 전년 대비 119% 증가한 2억 5천만 건 차단."

---

## 8. 전략적 시사점

*(데이터 정리 역할에 한정. 전략 권고는 SKILL-1 담당)*

**v3 핵심 데이터 확정 사항:**

1. **피해 규모 수치 재정립:** "+335%" 수치 삭제, 경찰청 기준 "+91% (2023→2024)" 사용. 1인당 5,290만원은 공식 [A] 확인.

2. **삼성 S26 한국 영향 명확화:** 한국어 기반 자체 탐지(경찰청·국과수 데이터, 무료, One UI 8.0+ 전 갤럭시)가 실질적 경쟁 요소. Gemini 기반 탐지는 현재 영어·미국 한정으로 한국 시장에 즉각적 영향 제한적.

3. **LGU+ 익시오 프로 MWC 2026:** 금융 연계 탐지 모델(통신→금융 즉각 대응) 공개. HE 도입은 비실시간 데이터 보호 목적으로 명시. 익시오 프로가 단순 보이스피싱 탐지를 넘어 AI 콜 에이전트 방향으로 확장.

4. **시장 세그먼트 구조화:** G-17(콜센터 사기 탐지 AI $1.92B), G-18(Voice Analytics $3.69B), G-19(Allied MR $1.3B)은 모두 글로벌 시장으로, 국내 B2C 독립 시장과 직접 매칭되지 않으나 성장 방향성(CAGR 12~20%)을 지지.

5. **정부 공동 플랫폼 2026~2027:** 구축 중으로 아직 운영 전. LGU+의 조기 참여 기회 존재.

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- 동형암호 실시간 통화 불가 판정: 복수 학술 논문 [P-01~P-05] + Zama GPU 64비트 곱셈 32ms [G-24] [A]
- 보이스피싱 피해 통계: 경찰청·금감원 공식 발표 [A] [N-18, N-20, N-11, N-04]
- 삼성 S26 한국어 온디바이스 탐지: 삼성 뉴스룸 공식 발표 + 과기정통부 [A] [E-01]
- ITU-T G.114 150ms 기준 + Cisco 200~250ms 기준 [A] [G-22, G-23]
- LGU+ 익시오 프로 MWC 2026 발표: 복수 언론 확인 [B] [N-16]
- KT 91.6% 탐지율: KT 뉴스룸 + 복수 언론 [B] [E-03]
- MSIT 5,724만 휴대폰 회선: 정부 공식 통계 [A] [G-20]
- PQC ML-KEM Hybrid 배포: Cloudflare, NIST 공식 [A] [G-25]

**추가 검증 필요 [C/D]:**
- Zama GPU bootstrapping <1ms: 공식 블로그 기반 [B], 음성 처리 적용 가능성은 [D]
- Voice Analytics 시장 규모($1.3~3.69B): 리서치 기관별 정의 차이 존재 [B~C]
- Apple iOS 26 한국 지원 여부: 영어권 기반 보도만 확인, 한국 출시 여부 [D]
- SKT 11억 건 차단: SKT 자사 발표 [B], 독립 검증 부재
- LGU+ HE 도입 계획 구체 일정: 공개 정보 없음 [D]

**데이터 공백 (v3 이후에도 미해소):**
- 국내 B2C 통화 보안 서비스 독립 TAM/SAM 리서치 보고서
- 국내 소비자 WTP(지불의사) 조사
- LGU+ 익시오 공식 탐지율 측정치
- 삼성/Apple 보이스피싱 탐지 오탐율(FP Rate) 공식 수치
- KIPRIS 기반 국내 통신 3사 보이스피싱 특허 포트폴리오
- Apple iOS 26 Call Screening 한국어·한국 지원 공식 발표

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 인용원문(한글) | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|----------|------|-------------|--------|--------|--------|-----|
| G-05 | Gizmochina / Time Magazine | 2025.12 / 2025 | 미디어 | Snapdragon 8 Gen 5 NPU / Honor On-Device AI | +46% AI 성능, 70+ TOPS; Honor 온디바이스 딥페이크 탐지 | 4 | 3 | 5 | https://www.gizmochina.com/2025/12/24/on-device-ai-snapdragon-8-gen-5-npu-explained/ |
| G-07 | postquantum.com | 2025 | 전문기관 | PQC Standardization 2025 Update | ML-KEM, ML-DSA FIPS 확정 | 4 | 4 | 5 | https://postquantum.com/post-quantum/cryptography-pqc-nist/ |
| G-08 | postquantum.com / GSMA PQ.03 v2.0 | 2025 / 2024 | 전문기관/업계 | Telecom's Quantum-Safe Imperative | VoLTE IMS 전환 벤더 의존, GSMA 가이드라인 v2.0 | 5 | 4 | 5 | https://postquantum.com/post-quantum/telecom-pqc-challenges/ |
| G-09 | Pindrop 공식 / PR Newswire | 2025 | 기업 | 2025 Voice Intelligence and Security Report | 딥페이크 +1300%, $12.5B 사기 피해, 탐지율 80%, FP <0.5% | 4 | 4 | 5 | https://www.pindrop.com/research/report/voice-intelligence-security-report/ |
| G-14 | GrowthMarketReports / Pindrop | 2024 / 2025 | 리서치/기업 | Fraud Analytics for International Voice Market | 2024 $1.87B → 2033 $5.49B, CAGR 14.2% | 4 | 3 | 4 | https://growthmarketreports.com/report/fraud-analytics-for-international-voice-market |
| G-15 | GlobeNewswire | 2026.02.23 | 리서치 | Post-Quantum Cryptography Industry Research Report 2026 | PQC가 연구 개념에서 핵심 사이버보안 축으로 전환 | 3 | 3 | 5 | https://www.globenewswire.com/news-release/2026/02/23/3242432/28124/en/Post-Quantum-Cryptography-Industry-Research-Report-2026.html |
| G-16 | DataIntelo | 2024 | 리서치 | AI-Powered Voice Fraud Detection Market | $2.36B(2024)→$12.16B(2033) CAGR 18.7% | 4 | 3 | 4 | https://dataintelo.com/report/ai-powered-voice-fraud-detection-market |
| **G-17** | DataIntelo | 2024 | 리서치 | Call Center Fraud Detection AI Market | **$1.92B(2024)→$8.60B(2033) CAGR 19.7%. 콜센터 사기 탐지 AI 세그먼트 — Voice Analytics(G-18·G-19) 대비 협의 정의. 성장률은 Allied MR 19.6%(G-19)·MnM 19.4%(G-26)와 일관.** | 4 | 3 | 4 | https://dataintelo.com/report/call-center-fraud-detection-ai-market |
| **G-18** | Market Research Future | 2024 | 리서치 | Voice Analytics Market | **$3.69B(2024)→$13.73B(2035) CAGR 12.68%. 고객서비스·마케팅 포함 광의 정의 — G-17·G-19보다 큰 시장 정의.** | 4 | 3 | 4 | https://www.marketresearchfuture.com/reports/voice-analytics-market-7979 |
| **G-19** | Allied Market Research | 2023 | 리서치 | Voice Analytics Market Size & Forecast | **$1.3B(2023)→$6.7B(2032) CAGR 19.6%. MnM CAGR 19.4%(G-26)와 교차 검증 완료. 협의 정의 기준 성장률 일관.** | 4 | 3 | 4 | https://www.alliedmarketresearch.com/voice-analytics-market-A12983 |
| G-20 | 서울신문 (MSIT 공식 통계 기반) | 2025.07.18 | 정부 통계 | SKT 시장 점유율 40% 무너졌다 | 이동통신 휴대폰: SKT 39.3%, KT 23.8%, LGU+ 19.5%, 합계 5,724만 회선 | 5 | 5 | 5 | https://www.seoul.co.kr/news/economy/2025/07/18/20250718500096 |
| **G-21** | MSIT 무선통신서비스 통계 | 2025.07 | 정부 | 무선통신서비스 가입자 현황 | **전체 무선회선(IoT 포함): 9,079만 회선. 스마트워치·태블릿·IoT 포함 수치 — 보이스피싱 서비스 TAM 산정에는 부적합하며, 휴대폰 회선(5,724만, G-20)이 실질적 TAM.** | 4 | 5 | 5 | https://www.msit.go.kr/stat/ |
| **G-22** | ITU-T Rec. G.114 (2003) | 2003 (현행 표준) | 국제표준 | One-way transmission time | **편도 지연 0~150ms 권장, 150~400ms 허용 — HE 불가 판정의 1차 기준선.** | 5 | 5 | 3 | https://www.itu.int/rec/T-REC-G.114 |
| **G-23** | Cisco — Understanding Delay in Packet Voice Networks | 2006 (현행 참조) | 기업 기술 문서 | VoIP Delay Analysis | **실무: 200ms 적정, 250ms 한계. 코덱 2.5~10ms + 패킷화 20~30ms + 네트워크 가변 — HE 불가 판정의 2차 실무 기준선. G-22(ITU 표준)와 G-23(Cisco 실무)의 이중 기준으로 HE 실시간 불가를 다각도 검증.** | 5 | 4 | 3 | https://www.cisco.com/c/en/us/support/docs/voice/voice-quality/14655-voip-delay-details.html |
| **G-24** | Zama 공식 블로그 | 2025.09 | 기업 (HE 전문) | Bootstrapping TFHE ciphertexts in less than one millisecond | **H100 GPU 1개: bootstrapping <1ms(4비트 945µs). 8xH100: 64비트 곱셈 32ms, 덧셈 8.7ms. CPU 대비 56배 향상. 음성 처리 직접 적용 언급 없음.** | 5 | 4 | 5 | https://www.zama.org/post/bootstrapping-tfhe-ciphertexts-in-less-than-one-millisecond |
| **G-25** | Cloudflare Blog (State of PQC 2025) | 2025 | 기업 기술 블로그 | State of the post-quantum Internet in 2025 | **X25519MLKEM768 널리 배포 중. TLS·IPsec PQC Hybrid 운영. 첫 상업용 PQC 인증서: 2026년 예상. 광범위 신뢰 체계: 2027년 이후.** | 4 | 4 | 5 | https://blog.cloudflare.com/pq-2025/ |
| **G-26** | MarketsandMarkets | 2024 | 리서치 | Voice Analytics Market (MnM) | **$1.6B(2024 est.), CAGR 19.4% — Allied MR 19.6%(G-19)와 교차 검증. 협의 정의 성장률 일관성 확인.** | 4 | 3 | 4 | https://www.marketsandmarkets.com/PressReleases/voice-analytics.asp |
| **G-27** | Grand View Research | 2024 | 리서치 | Fraud Detection and Prevention Market (전체) | **$33.1B(2024)→$90.1B(2030) CAGR 18.7%. 전체 사기 탐지 시장 최상위 프레임 — 음성 사기 탐지는 세부 세그먼트.** | 3 | 4 | 5 | https://www.grandviewresearch.com/press-release/global-fraud-detection-prevention-market |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약(한글) | URL |
|------|--------|-------|------|-----------|----------|-----|
| N-01 | 보안뉴스 | 2025.12 | SKT·KT·LGU+, AI로 보이스피싱 탐지 고도화 | SKT KT LGU 보이스피싱 AI | 3사 AI 탐지 현황, SKT 음성 스팸 +119%, 2억 5천만 건 차단 | https://news.nate.com/view/20251202n25936 |
| N-02 | 서울경제 | 2025.10.03 | 보이스피싱 예방 위한 통신사 서비스 살펴보니 | 통신사 보이스피싱 서비스 비교 | SKT·KT·LGU+ 3사 서비스 비교 | https://www.seoul.co.kr/news/economy/industry/2025/10/03/20251003500063 |
| N-03 | 세계일보 | 2025.04.27 | 2025년 1분기 보이스피싱 피해액 3116억원… 2024년 대비 2.2배 급증 | 보이스피싱 피해액 통계 2025 Q1 | Q1 3,116억 원, 5,878건, 건수 +17%, 피해액 2.2배, 1인당 5,384만원. (주: "+335%" 수치는 이 기사 원문에서 직접 확인되지 않음) | https://www.segye.com/newsView/20250427507459 |
| N-04 | 헤럴드경제 | 2026.01 | 악성 앱으로 휴대폰 장악…지난해 보이스피싱 피해 1.2조 '사상 최대' | 보이스피싱 피해액 2025 1조 | 2025년 연간 1조 2,578억 원 확정. 발생 건수 20,893건 | https://biz.heraldcorp.com/article/10661923 |
| N-05 | 스마트투데이 | 2025 | LGU+, '안티딥보이스' 위변조음성 5500건 탐지 | LGU+ Anti-DeepVoice 성과 | 위변조 음성 5,500건 탐지, 5초 내 탐지 | https://www.smarttoday.co.kr/news/articleView.html?idxno=87596 |
| N-06 | Sammy Fans | 2026.02.25 | Gemini-powered Scam Detection arrives on Galaxy S26 | Samsung Galaxy S26 Gemini scam | S26 온디바이스 Gemini 스캠 탐지: **영어·미국 한정**. 한국어 기반 자체 탐지(경찰청·국과수 데이터)와 별개 레이어 | https://www.sammyfans.com/2026/02/25/samsung-galaxy-s26-gemini-ai-scam-detection/ |
| N-07 | 9to5Mac | 2025.06.13 | Security Bite: Apple's new iOS 26 spam tools | Apple iOS 26 scam detection | iOS 26 Call Screening 출시 발표 | https://9to5mac.com/2025/06/13/security-bite-apples-new-ios-26-spam-tools-will-make-scammers-cry/ |
| N-08 | VoIP Review | 2025.11.18 | BT and Pindrop Team Up to Combat Voice Fraud | Pindrop telecom partnership | BT-Pindrop 딥페이크 탐지 통합 파트너십 | https://voip.review/2025/11/18/bt-pindrop-team-combat-voice-fraud-ai/ |
| N-09 | The Pickool | 2024.10 | KT Gains Regulatory Approval for AI-Powered Voice Phishing | KT regulatory sandbox 2024 | 과기정통부 ICT 규제샌드박스 실증특례 승인 — KT 국내 최초 | https://www.thepickool.com/kt-gains-regulatory-approval-for-ai-powered-voice-phishing-detection-service/ |
| N-10 | 뉴시스 (경찰청 통합대응단) | 2025.11.24 | 보이스피싱 피해 1조원 돌파 | 보이스피싱 피해 1조 2025 | 2025년 1~10월: 1조 566억 원(19,972건). (**주의: N-10 요약에 "2024년 연간 1조 2,578억원"으로 기재된 것은 오기. 2024년 연간은 8,545억원. 1조 2,578억원은 2025년 연간 확정치(N-04).** ) | https://www.newsis.com/view/?id=NISX20251124 |
| N-11 | 금감원 정책보고서 | 2024.03 발표 | 2023년 보이스피싱 피해현황 분석 | 보이스피싱 2023 금감원 통계 | 2023년: 1,965억 원(+35.4% YoY), 1인당 1,710만 원 — 금감원 집계 기준 | https://www.fss.or.kr/ |
| N-12 | 네이트 뉴스 | 2025.07.04 | SKT 5년 7,000억 투자 공식 발표 | SKT 보안 투자 2025 | SKT 유영상 대표: 5년간 7,000억 원 투자 공식 발표 | https://news.nate.com/ |
| N-13 | 보안뉴스 | 2025.07.04 | SKT 보안 투자 상세 | SKT 보안 | CISO CEO 직속 격상, 보안 인력 2배 확대 | https://www.boannews.com/ |
| N-14 | 네이트 뉴스 | 2025.07.15 | KT 5년 1조 투자 공식 발표 | KT 보안 투자 2025 | KT 5년간 1조 원 투자 공식 발표 | https://news.nate.com/ |
| N-15 | 서울경제 | 2025.07.15 | KT 보안 투자 상세 | KT 보안 | 보안 인력 162명→300명, AI 선제 보안 | https://www.seoul.co.kr/ |
| **N-16** | 이지경제 / 데일리시큐 / 아주경제 (복수 언론) | 2026.02.23 | LG유플러스, 'MWC 2026'서 '익시오 프로' 공개 | 익시오 프로 MWC 2026 | **익시오 프로 공개: 선제적 AI 콜 에이전트. 월 2,000건 탐지, 악성 서버 800개 추적, 고객 3.3만명 경찰 전달. 향후 HE 적용(비실시간 데이터 보호) 계획.** | https://www.ezyeconomy.com/news/articleView.html?idxno=232539 |
| **N-17** | TechRadar / Macworld / ghacks (복수 언론) | 2026.01 | Call Screening in iOS 26 | Apple iOS 26 call screening | **iOS 26 Call Screening: 완전 온디바이스, 미지 번호 AI 대리 응대, 모든 오디오 iPhone 내 저장. iPhone 11 이상 호환. 한국 지원 여부 미확인.** | https://www.techradar.com/phones/iphone/call-screening-in-ios-26 |
| **N-18** | 더시사법률 (경찰청 국수본 인용) | 2025.11 | 보이스피싱 피해액, 올해 첫 1조 원 돌파 | 보이스피싱 1인당 피해액 5290만원 | **1인당 평균 피해액 5,290만원 공식 확인 (2025년 1~10월 기준, 경찰청 국수본). 2021년 2,498만원 대비 약 2배.** | https://www.tsisalaw.com/mobile/article.html?no=26745 |
| **N-19** | 과기정통부 정책브리핑 / 전자신문 | 2026.02.12 | 과기정통부 "보이스피싱 피해 방지, AI 서비스 이용하세요" | 과기정통부 보이스피싱 공동대응 플랫폼 | **AI 기반 보이스피싱 통신서비스 공동대응 플랫폼 2026~2027년 구축 예정 (경찰청·KISA 포함). 규제특례 적용. 삼성+3사 온디바이스 AI 탐지 서비스 병렬 운영.** | https://www.korea.kr/news/policyNewsView.do?newsId=148959497 |
| **N-20** | 뉴데일리 / 뉴스핌 (경찰청 국수본 공식 발표 기반) | 2025.07.15 / 2025.07.18 | 지난해 보이스피싱 피해액 8545억 원, 경찰청 발표 | 보이스피싱 2024 8545억 경찰청 | **2024년 연간 피해액 8,545억 원 (역대 최대, 경찰청 집계). 발생 건수 18,902건. 경찰청 2023년 기준(4,472억) 대비 +91%.** | https://www.newdaily.co.kr/site/data/html/2025/07/15/2025071500048.html |
| **N-21** | 이지경제 (LGU+ 공식 발표 기반) | 2026.02.23 | LGU+, 'MWC 2026'서 AI·양자 기반 차세대 보안 기술 공개 | LGU+ MWC 2026 양자 보안 | **LGU+ MWC 2026: PQC 기반 통화 암호화 기술 시연, 익시오 프로 + KB국민은행 연계 실시간 대응 체계 시연.** | https://www.ezyeconomy.com/news/articleView.html?idxno=232696 |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약원문 |
|------|--------|-------|------|-----------|---------|
| E-01 | 삼성 뉴스룸 (한국) / 과기정통부 | 2026.02.25 / 2026.02.12 | 삼성전자 갤럭시 스마트폰, AI로 보이스피싱·스팸 한 번에 차단 | 삼성 갤럭시 S26 보이스피싱 | 한국어 기반 자체 온디바이스 탐지(경찰청·국과수 데이터 3만건), One UI 8.0+ 전 갤럭시, 2단계 알림. 통신 3사 협력, 공동 플랫폼 2026~2027 |
| E-02 | SK텔레콤 뉴스룸 | 2026.01 | AI로 스팸·피싱 35% 더 잡았다, 2025년 11억 건 차단 | SKT 스캠뱅가드 2025 성과 | 11억 건 차단, 음성 스팸 +119%, 2억 5천만 건. IBK기업은행 기술 이전. 에이닷 온디바이스 탐지 |
| E-03 | KT 공식 뉴스룸 / The Pickool / 전자신문 | 2025.07.29 / 2025.12 | KT, 'AI 보이스피싱 탐지 2.0' 출시 / AI 보이스피싱으로 1300억 피해 예방 | KT AI 보이스피싱 탐지 2.0 | 화자인식+딥보이스 통합. 91.6%(H1). 1,300억 예방. 목표 95%+, 2,000억+/년 |
| E-04 | 한국NGO신문 / EBN / 이지이코노미 | 2026.01~02 | KB국민은행-LG유플러스, AI 기반 보이스피싱 실시간 대응 체계 | LGU+ 익시오 KB국민은행 협력 | 익시오-KB국민은행 연동, 1,720억 원 피해 예방, MWC26 시연 |
| E-05 | Korea Herald / Korea Times | 2025.02 | LG Uplus to launch world's 1st on-device anti-deepvoice tech | LG U+ Anti-DeepVoice PQC MWC 2025 | MWC 2025 Exy Guardian: Anti-DeepVoice + PQC + On-Device SLM 통합 스위트 |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 학술지/컨퍼런스 | 인용수 | 핵심 인용 | DOI/URL |
|------|------|---------|------|----------------|--------|----------|---------|
| P-01 | Chillotti et al. / TFHE 팀 | 2020 / 2025 | TFHE: Fast FHE over the Torus / Refined TFHE Leveled HE | JACM / ACM CCS 2025 | - | binary gate당 ~13ms; refined 4.2~6.8ms (최적화 조건) | https://tfhe.github.io/tfhe/ |
| P-02 | Bae et al. | 2019 | Hardware Assisted HE in Real-Time VOIP | IEEE Xplore | - | FPGA 가속에도 ~150ms/operation — 실시간 통화 불가 | https://ieeexplore.ieee.org/document/8639492 |
| P-03 | ACM CCS 2025 저자 | 2025 | Refined TFHE Leveled Homomorphic Evaluation | ACM CCS 2025 | - | 특정 연산 4.2~6.8ms — 실시간 통화 요건 대비 불충분 | https://dl.acm.org/doi/10.1145/3719027.3744873 |
| P-04 | Boura et al. | 2023 | Scalable Cloud-Supported Audio Conferencing using E2E HE | ACM CCSW 2023 | - | 클라우드 지원 시 가능 — 전용 프로토콜 필요, 일반 VoIP 즉시 적용 불가 | https://dl.acm.org/doi/10.1145/3605763.3625245 |
| P-05 | arXiv 저자 | 2026.02 | On the Feasibility of Hybrid Homomorphic Encryption | arXiv | - | "prohibitive latency" — 실시간 음성 통신 HE 불가 명시 | https://arxiv.org/pdf/2602.02717 |
| P-06 | arXiv 저자 | 2025.12 | Physics-Guided Deepfake Detection for Voice Authentication Systems | arXiv | - | M4 Pro 기준 149ms/3초 세그먼트; ZKP 대안 제안 | https://arxiv.org/abs/2512.06040 |
| P-07 | arXiv 저자 | 2025.09 | On Deepfake Voice Detection — It's All in the Presentation | arXiv | - | 탐지 성능에 입력 presentation 방식이 핵심 영향 | https://arxiv.org/abs/2509.26471 |
| P-08 | Xinfeng Li et al. | 2024 | SafeEar: Content Privacy-Preserving Audio Deepfake Detection | ACM CCS 2024 | - | EER 2.02%; WER 93.93%+ (프라이버시 보존); acoustic 특성만으로 딥페이크 탐지 | https://arxiv.org/abs/2409.09272 |
| P-09 | K.A. Shahriar | 2026.01 | Lightweight Resolution-Aware Audio Deepfake Detection | arXiv | - | 159k parameters, <1 GFLOP/inference; EER 0.16%; AUC 0.98 | https://arxiv.org/abs/2601.06560 |
| P-10 | arXiv 저자 | 2025.12 | Toward Noise-Aware Audio Deepfake Detection: SNR-Benchmarks | arXiv | - | 실제 잡음 조건에서 탐지 성능 급락 — 실서비스 핵심 고려사항 | https://arxiv.org/abs/2512.13744 |
| P-11 | arXiv 저자 | 2026.01 | Audio Deepfake Detection in the Age of Advanced TTS | arXiv | - | 최신 TTS 딥페이크 탐지 어려움 심화; Generalization 문제 | https://arxiv.org/abs/2601.20510 |

### 특허 (T-xx)

| 번호 | 출원인 | 등록/출원일 | 특허번호 | 제목 | 핵심 청구항 | 관할 |
|------|--------|-----------|---------|------|-----------|------|
| T-01 | Google LLC | 2022.08.23 (등록) | US11423926B2 | Real-time voice phishing detection | 통신 네트워크 보이스피싱 탐지기 결과 단말 알림 전달 | USPTO |
| T-02 | Samsung Electronics | 2024 (등록) | US11652603B2 | AI Calculation Semiconductor Device | HE 연산 가속 반도체; multiply/accumulator + cyclic shift로 FHE 속도 향상 | USPTO |
| T-03 | Wells Fargo Bank | 2024.02.07 (출원) / 2025.02.19 (공개) | US20250252968A1 | Synthetic Voice Fraud Detection | (1) 실제 음성 수집·정규화, (2) 합성 클론 생성, (3) 실제·합성 페어 ML 학습, (4) 불일치 지표 탐지 | USPTO |
| T-04 | Bank of America | 2023.11.07 (출원) / 2025.05.08 (공개) | US20250148788 | Deepfake Detection System | 컴퓨팅 기기 딥페이크 분석 엔진이 콘텐츠 접근 모니터링 중 딥페이크 자동 탐지 | USPTO |
| T-05 | 발명인 미확인 | 2015 (선행특허) | US20150237019A1 | HE for Teleconferencing | additive HE로 음성 암호화 → 믹서가 암호화 상태 혼합 — VoIP HE 원조 개념특허 | USPTO |

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 페이지 | 인용내용 |
|------|--------|-------|--------|---------|
| I-01 | Secure AI 기술·시장·규제 동향 리서치 (초기) | 2026-02-25 | 전체 | HE TRL 4~5, PQC TRL 7~8, Anti-DeepVoice MWC 2025, SKT/KT 투자 비교 |
| I-02 | Research Report: Secure AI B2C v2 | 2026-02-26 | 전체 | HE 불가(TFHE 13ms/gate), 삼성 S26, 피해액 1조 2,578억, 경량 모델 159k params |
| I-03 | WTIS SKILL-1 v3 (Conditional Go 123/200) | 2026-02-26 | 전체 | HE Critical Risk, 3B 전략, 권고 KPI |
| I-04 | Validator v3 (UNCERTAIN) | 2026-02-26 | 전체 | 고아 인용 5건, 수치 불일치 2건, 연도 혼선 — v3 해소 대상 |
| I-05 | SKILL-0 v2 Analysis Brief | 2026-02-26 | 전체 | 검색 전략, 검증 항목 V1~V10 정의 |

---

## v3 validator 이슈 해소 체크리스트

| 이슈 | v3 조치 | 해소 여부 |
|------|---------|---------|
| G-17 고아 인용 | 섹션 2.2 시장 세그먼트 비교표에 직접 인용, DataIntelo 콜센터 사기 탐지 AI 시장으로 교차 검증 활용 | **해소** |
| G-18 고아 인용 | 섹션 2.2 시장 세그먼트 비교표에 직접 인용, MRF 광의 Voice Analytics 시장으로 활용 | **해소** |
| G-19 고아 인용 | 섹션 2.2 시장 세그먼트 비교표에 직접 인용, Allied MR 협의 정의로 MnM과 교차 검증 | **해소** |
| G-21 고아 인용 | 섹션 2.3 TAM 산정 논거에서 G-20(5,724만)과 G-21(9,079만) 구분 명시적 활용 | **해소** |
| G-23 고아 인용 | 섹션 1.1 HE 불가 판정에서 G-22(ITU-T 150ms)와 G-23(Cisco 200~250ms) 이중 기준으로 명시 인용 | **해소** |
| "+335% 폭증" 수치-소스 불일치 | 섹션 2.1에서 출처 불확인 및 집계 기준 오류 확정. 삭제하고 "+91% (경찰청 기준, 2023→2024)"로 교체 권고 | **해소 (삭제 권고)** |
| "1인당 5,290만원" 파생 계산 | N-18(더시사법률/경찰청 국수본)에서 공식 확인. 2025년 1~10월 기준 수치임을 명시 | **해소** |
| N-04/N-10 연도 혼선 | 섹션 2.1 주석에서 N-10 요약의 오기 명시. 1조 2,578억원은 2025년 연간(N-04), 2024년 연간은 8,545억원(N-20) | **해소** |
