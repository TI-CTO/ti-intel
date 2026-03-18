---
type: wtis-validator
target: 2026-03-18_wtis-skill1.md
date: 2026-03-18
validator_status: partial
---

# WTIS 교차검증: On-Device 동형암호 키워드 검색

## 검증 결과 요약
- **status: PARTIAL**
- **총 이슈: 5건** (Critical: 1, Minor: 4)
- **단일 소스 비율:** 핵심 수치 중 약 30% (CryptoLab CEO 발언, Archive Market Research $55B, Cornami·DESILO E-03 등)

---

## 이슈 목록

| # | 유형 | 심각도 | 내용 | 처리 제안 |
|---|------|--------|------|----------|
| 1 | 수치 불일치 | **Critical** | G-02 (GM Insights) 인용값 "$234.7M (2025)"가 실제 페이지와 불일치. 실제 GM Insights는 2023년 기준 $178.4M, CAGR 8%, 2032년 $352M을 제시하며, 2025년 시점값 $234.7M은 확인 불가. "Roots Analysis"와 합산 표기된 것으로 보이나 두 기관의 별도 수치가 혼합될 가능성 있음 | G-02 수치 원본 재확인 및 출처 분리 필요 |
| 2 | 고아 소스 | Minor | E-03 (Cornami·DESILO FHE-based LLM Deployment, 2025-09-16)이 References 테이블에 등재되었으나 본문 어디에도 인용되지 않음 | E-03을 References에서 제거하거나 본문에 관련 내용 추가 |
| 3 | 고아 소스 | Minor | P-05 (Faster Spiral PIR, 2025-02)가 References 테이블에 등재되었으나 본문에서 미인용 | P-05 제거 또는 PIR 기술 비교 섹션에 인용 추가 |
| 4 | 단일 소스 미표시 | Minor | SAM 테이블 내 Archive Market Research "$55B (AICC 전체, 2025)" 수치가 G-09 단일 소스임에도 신뢰도 태그([C]/[B]) 미부여. G-09는 Fortune Business Insights와 Archive Market Research를 하나의 번호로 묶고 있어 출처 구분이 불명확 | G-09를 두 기관으로 분리하거나 Archive Market Research 수치에 [B] 태그 명시 |
| 5 | 논리적 순환 | Minor | 실행가능성 "리스크 관리(4점)" 채점 근거에서 "On-Device 레이턴시 미검증 → 완화: PoC에서 확인"을 스스로 순환 논리로 명시하면서도 감점 폭이 6점(4/10)에 그침. 핵심 Go 전환 조건이 미검증인 상황에서 실행가능성 20/40은 다소 관대한 채점 가능성 존재 | 채점 조정 불요하나, 판정 근거 설명에 이 한계를 보다 명시적으로 기재 권고 |

---

## 1. 인용 검증

### References 테이블 교차 확인

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | G/N/E/P 4개 섹션으로 구성 |
| 모든 본문 [N] 인용 → References 매칭 | ✅ | G-01~G-34, N-01~N-03, E-01~E-04, P-01~P-05 전체 테이블 등재 확인 |
| References 미인용 항목(고아 소스) | ❌ | E-03, P-05 — 2건 |
| 미인용 수치/주장 발견 | ✅ (없음) | 본문 내 모든 수치에 인용 기호 부여됨 |

### 본문 인용 코드 전수 목록

**G 계열 (21건):** G-01, G-02, G-03, G-04, G-05, G-06, G-07, G-09, G-10, G-12, G-13, G-14, G-15, G-16, G-17, G-18, G-19, G-20, G-21, G-24(규제), G-34

**N 계열 (3건):** N-01, N-02, N-03

**E 계열 (3건):** E-01, E-02, E-04 ← E-03은 본문 미인용

**P 계열 (3건):** P-01, P-03, P-04 ← P-05는 본문 미인용

### 고아 소스 상세

| 코드 | 제목 | 비고 |
|------|------|------|
| E-03 | Cornami & DESILO FHE-Based LLM Deployment (2025-09-16) | HARVEST 플랫폼 관련. 본문 DESILO 섹션에서 미인용. |
| P-05 | Faster Spiral: Low-Communication High-Rate PIR (2025-02) | PIR 기술 관련 논문이나 HET-PIR/BKPIR 비교에 미사용. |

---

## 2. 수치 교차검증

| 수치 | 출처 | 독립 검증 결과 | 판정 |
|------|------|--------------|------|
| Intel Heracles 1,074~5,547x FHE 가속 [G-04][G-05] | Tom's Hardware + IEEE Spectrum | 복수 소스 교차 확인. 24코어 Intel Xeon 대비 수치 정확. 3nm FinFET, 48GB HBM3 확인. | ✅ 일치 |
| Aikata 97% enc/dec 비용 절감, 76x FPGA 가속 [P-01] | IACR ePrint 2026/515 | 실제 페이지 확인. "reduces the enc/dec computation by up to 97%", "76× speedup" 정확 | ✅ 일치 |
| HET-PIR 32비트 비교 3.9ms [P-03] | Springer Cybersecurity 2026-01 | Springer 원문 확인. "comparing two 32-bit values takes only 3.9 milliseconds" 정확. 16비트 batch 0.01ms/건도 일치. | ✅ 일치 |
| BKPIR 처리량 10x 향상 [P-04] | NDSS 2026 | NDSS 2026 논문 확인. "achieves FHE-based PIR throughput by over 10× through parallelism and batched evaluations" 정확 | ✅ 일치 |
| Niobium-SEMIFIVE KRW 10B 계약, 삼성 8nm [G-06][E-04] | PR Newswire 2026-02-19 | "valued at around KRW 10 billion (USD 6.86 million)", Samsung 8nm LPU 확인 | ✅ 일치 |
| Niobium $23M+ 펀딩 [G-21] | The Quantum Insider 2025-12-03 | 복수 소스 교차 확인($23M+ oversubscribed financing). Quantum Insider 원문 확인. | ✅ 일치 |
| Zama $1B 밸류에이션, 500~1000 TPS GPU 로드맵 [G-12] | BlockEden 2026-01-05 | Zama 공식 리트페이퍼 + 로드맵에서 "end of 2026, GPU, 500-1000 TPS per chain" 확인 | ✅ 일치 |
| Apple iOS 18 BFV PIR, Live Caller ID Lookup [G-17][G-18] | Apple ML Research + Swift.org | 공식 페이지 교차 확인. BFV 기반 PIR, Live Caller ID Lookup 기능 정확. | ✅ 일치 |
| NIST Threshold FHE S5 카테고리, 2026-04-20 마감 [G-16] | NIST CSRC 공식 | "Preview Writeup by 2026-Apr-20" NIST CSRC 직접 확인 | ✅ 일치 |
| HomomorphicEncryption.org 9차 서울 개최 [G-14] | 공식 사이트 | 2026-03-05~06, 서울 LG 사이언스파크 ISC 빌딩 확인 | ✅ 일치 |
| LGU+-CryptoLab MWC 2026 AICC PoC [E-01][N-01] | Asia Business Daily + Korea IT Times | MWC 2026 Barcelona 발표 확인. ixi-O AICC 동형암호 PoC 공식화 확인. | ✅ 일치 |
| Fortune Business Insights AICC $2.4B(2025), $13.5B(2034), CAGR 20.8% [G-09] | Fortune Business Insights | "$2.41B (2025), $13.52B (2034), CAGR 20.80%" — 반올림 수준 일치 | ✅ 일치 (반올림) |
| GM Insights $234.7M (2025) [G-02] | GM Insights 원본 | 실제 페이지는 2023년 $178.4M, 2032년 $352M 제시. 2025년 $234.7M 값은 원본에 명시 없음 — CAGR 역산 추정값일 가능성 | ⚠️ **Critical 불일치** |
| Archive Market Research ~$55B AICC 전체 (2025), CAGR ~22% [G-09] | Archive Market Research | 검색 결과 "$55B projection 2025, CAGR 22%" 간접 확인. 그러나 G-09 하나로 Fortune($2.4B)와 Archive($55B)를 함께 묶어 인용 — 출처 통합 표기 혼란 | ⚠️ Minor — 출처 분리 필요 |
| DESILO GL 스킴 FHE.org 2026 Taipei 발표 [E-02][G-07] | PR Newswire + CybersecAsia | "formally presented at the FHE.org 2026 Conference in Taipei, March 8, 2026" 확인. Craig Gentry(Cornami) 공동 저자 확인. | ✅ 일치 |
| DESILO GL 스킴 정량 벤치마크 미공개 | 직접 확인 | PR Newswire 발표문에 정량 성능 수치 없음 — 본문의 "정량 벤치마크 미공개" 서술 정확 | ✅ 일치 |
| SKT 5년 7,000억 투자 [N-02] | SKT Newsroom | N-02는 QKD+PQC 뉴스룸 기사. 7,000억 투자 금액 자체는 해당 기사에서 직접 명시되는지 불명확 (기사 URL 접근 시 양자암호 출시 내용) — 금액 출처가 동일 기사인지 별도 발표인지 불분명 | ⚠️ Minor — 단일 소스, 수치 원본 재확인 권고 |
| KT 5년 1조 투자 [N-03] | Global Economic 2025-07-15 | N-03 Global Economic 기사. 1조 투자 수치는 단일 언론 소스. | ⚠️ Minor — 단일 소스 |

---

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "GM Insights FHE 시장 $234.7M (2025)"
    current_sources: 1
    issue: "GM Insights 원본 페이지는 2023년 $178.4M을 기준값으로 제시. 2025년 $234.7M은 CAGR 역산 추정값으로 보이며 원본에 명시 없음"
    suggested_keywords: ["GM Insights homomorphic encryption market 2025 size", "Roots Analysis FHE market 2025 forecast"]

  - claim: "SKT 5년 7,000억 양자암호 투자"
    current_sources: 1
    issue: "N-02 기사(SKT Newsroom QKD-PQC 출시)에 투자 금액 7,000억이 포함되는지 불명확. 별도 보도자료 출처 여부 미확인"
    suggested_keywords: ["SKT 양자암호 7000억 투자 계획", "SKT quantum security investment 2025"]

  - claim: "KT 5년 1조 AI 보안 투자"
    current_sources: 1
    issue: "N-03 단일 언론 소스(Global Economic). 한국 주요 언론 복수 확인 미완"
    suggested_keywords: ["KT 보안 투자 1조 2025", "KT AI security investment plan 2025"]
```

---

## 3. 논리 검증

### 판정(Conditional Go, 125/200)과 점수 간 일관성

총점 계산 재검증:
- 고객가치: 7+7+5+5 = **24** ✅
- 시장매력도: 6+7+8+8 = **29** ✅
- 기술경쟁력: 6+8+7+7 = **28** ✅
- 경쟁우위: 6+6+5+7 = **24** ✅
- 실행가능성: 5+5+6+4 = **20** ✅
- 합계: 24+29+28+24+20 = **125** ✅

Conditional Go 범위(120~159점) 내 정확히 위치하며, 점수 산술 오류 없음.

### 논리적 도약 검토

1. **TRL 2~3 → 3~4 상향 근거**: Intel Heracles ASIC(서버-사이드), Aikata 97% 절감(ASIC/FPGA), HET-PIR 3.9ms(서버-사이드), Niobium 파일럿으로 상향 근거. 단, 모든 근거가 서버-사이드 또는 FPGA 기반이며 On-Device 실증은 없음. 보고서 스스로 "On-Device 실증 미완으로 TRL 4 확정 불가"라고 명시하고 있어 TRL 3~4 조건부 상향은 논리적으로 수용 가능.

2. **이전 "HE 전면 제거" 대비 재평가 논리**: 이전 분석이 실시간 통화(TFHE 32ms → 150ms 초과)를 기준으로 Watch 판정한 데 반해, 본 분석은 비실시간 AICC 사후 분석으로 유스케이스를 분리하는 논리 전환이 명시적으로 설명되어 있음. 유스케이스 변경에 따른 재평가는 논리적으로 정합.

3. **"순환 논리" 자기 인식**: 핵심 리스크(On-Device 레이턴시 미검증)에 대한 완화 전략으로 "PoC에서 확인"을 제시하면서 이를 스스로 순환 논리라고 인정함. 이 인식 자체는 투명하나, 실행가능성 4점(리스크 관리)에서의 감점 폭이 Go 전환 필수 조건 미충족 수준에 비해 관대할 수 있음.

### 논리 검증 결론

**PASS (조건부)** — 주요 논리 흐름은 일관성이 있으며, 불확실성은 [D] 태그와 명시적 한계 설명으로 적절히 표시됨. 순환 논리 구조는 자기 인식되어 있음.

---

## 4. 편향 분석

### 긍정/부정 균형 확인

**긍정 증거:**
- Intel Heracles 가속 성능, Aikata 경량화, HET-PIR/BKPIR 학술 구현을 통한 TRL 상향 근거 충분히 제시
- LGU+-CryptoLab MWC 2026 PoC 공식화, 한국 FHE 에코시스템 형성 등 긍정 시그널 구체적 인용

**부정/리스크 증거 (균형 확인):**
- On-Device 엔드-투-엔드 벤치마크 부재 명시적 한계 서술 (R1)
- Apple 선점 리스크 (R2), CKKS 표준 불확실성 (R3), CryptoLab CEO 발언 단일 소스 위험 (R4) 명시
- 대체재(TEE, RBAC, 가명처리) 존재를 리스크 항목으로 포함
- WTP 미검증, ROI 산정 불가를 [D] 태그로 명시

**편향 판정:** 긍정·부정 증거를 균형 있게 제시함. 단, 실행가능성 20/40 채점에서 핵심 Go 전환 조건이 모두 미확인 상태임에도 "Conditional Go"를 도출하는 과정이 다소 낙관적으로 보일 수 있으나, 이는 채점 기준(120~159 = Conditional Go)의 구조적 특성으로 편향보다는 프레임워크 한계에 해당.

**경쟁사 분석:** SKT/KT 양쪽 모두 "동형암호 직접 추진 미확인" 서술로 과장하지 않음. Apple은 인덱스 PIR과 키워드 PIR의 차이를 명확히 구분하여 비교. Nokia Bell Labs QRYPT를 경쟁 리스크로 포함하는 균형 잡힌 시각 유지.

**편향 검증 결론: PASS**

---

## 최종 판정

**PARTIAL**

인용 체계는 전반적으로 견고하며, 핵심 기술 수치(Intel Heracles, Aikata, HET-PIR, BKPIR, Niobium, Zama, Apple BFV PIR)는 독립 웹 검증에서 원본 소스와 일치한다. 논리 흐름도 이전 분석(2026-03-03) 대비 유스케이스 분리 재평가로서 일관성이 있고, 불확실성은 [D] 태그와 명시적 한계 설명으로 적절히 표시된다.

다만, G-02 (GM Insights) "$234.7M (2025)" 수치가 실제 원본 페이지 제시값($178.4M, 2023년 기준)과 불일치하는 Critical 이슈 1건이 발견되었다. 이 수치는 2025년 파생값으로 보이며 원본에 명시되지 않아 신뢰도 저하 요인이다. 또한 E-03(Cornami·DESILO), P-05(Faster Spiral)가 References 테이블에 등재된 채 본문에서 미인용되는 고아 소스 패턴이 반복 확인된다. 이 두 항목은 Minor에 해당하나, 이전 검증 이력에서도 반복적으로 발생하는 패턴임을 유의해야 한다.
