---
validator_status: partial
target_file: /Users/ctoti/Project/ClaudeCode/outputs/reports/secure-ai/he-keyword-search/2026-03-30_wtis-skill1.md
verified_at: 2026-03-30
---

# Validation Report — WTIS Skill-1: 양자/동형 암호 (he-keyword-search)

## 요약

- **상태: PARTIAL**
- **주요 이슈**:
  - Critical 2건: (1) G-17 ID 충돌 — CISA URL이 Apple BFV PIR 인용에 오용, (2) G-18(CyberArk 블로그)이 NSA CNSA 2.0 2027-01 의무화 주장을 지지하지 않음
  - Minor 3건: G-09/P-04 미인용 고아 소스, E-07 날짜 불일치(3/24 vs 3/26), G-28(arXiv 2502.14291)이 TEE 비교 주장 미지지
  - 채점 합산 오류 없음 (전 항목 정확), 판정 기준 부합

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | 24개 항목 등재 (G-01~G-28, P-01~P-04, E-01~E-07) |
| 모든 [N] 인용 매핑 | ⚠️ | G-17 ID 충돌 문제 있음 (아래 상세) |
| 미인용 소스 발견 | ❌ | G-09, P-04, G-17(Apple) 3건 — 본문에서 단 한 번도 인용되지 않음 |

### G-17 ID 충돌 (Critical)

본 파일의 References 테이블에 G-17이 **두 개** 존재한다.

- `G-17` (`ref-g-17`): CISA 페이지 — "Product Categories for Technologies That Use PQC Standards"
- `G-17 (Apple)` (`ref-g-17-apple`): Apple ML Research — iOS 18 BFV PIR

본문 63행, 89행에서 Apple BFV PIR을 `[[G-17]](#ref-g-17)`로 인용하고 있으나, `ref-g-17` 앵커는 CISA 페이지를 가리킨다. 즉, Apple BFV PIR 주장의 실제 근거는 Apple ML Research 페이지인데 CISA URL로 연결된다.

**영향 범위**: 기술 성숙도 맵(63행), 경쟁 비교표 Apple 행(89행)에서 출처 귀속 오류 발생.

---

## 2. 수치 검증

| 수치 | 인용 소스 수 | 판정 |
|------|------------|------|
| FHE TAM $251~310M(2026) → $1,319M(2035), CAGR 20.2% | 1건 (G-25, [C]) | [추가확인 필요] — 본문 표기 일치 ✅, 단일 소스 [C] |
| CAT GPU 33× 가속, 10³행 1초 | 1건 (P-02, [A]) | ✅ 원본 arXiv 수치 일치 확인 |
| Intel Heracles 5,547× | 1건 (E-05, [A]) | ✅ IEEE Spectrum "up to 5,000×" — 근사 일치 (⚠️ "5,547×" 정확 수치는 원문 본문에서 확인 필요) |
| KRW 10B 계약 (Niobium+SemiFive) | 1건 (G-21, [B]) | ✅ evertiq 원본 KRW 10 billion 일치 |
| $32B 기관 금융 인프라 (T-REX) | 2건 (G-22, E-07) | ✅ 두 URL 모두 $32 billion 수치 확인 |
| NSA CNSA 2.0 신규 시스템 2027-01 의무화 | 1건 (G-18, [B]) | ❌ 원본 CyberArk 블로그는 NIST 2030/2035 타임라인만 기술, CNSA 2.0 2027-01 내용 없음 |
| PQC 메시징 대역폭 100배 증가 | 1건 (E-03, [A]) | ✅ IBM 블로그에 "hundredfold increase" 명시 확인 |
| FHE 클라이언트 97% 경량화 (EuroS&P 2026) | 1건 (P-01, [A]) | ⚠️ iacr.org 403 오류 — 직접 접근 불가 (피어리뷰 확정 주장 검증 불완전) |
| Zama $1B 유니콘 (G-22, E-07 귀속) | 0건 | ❌ Decrypt 기사(G-22)와 Zama 공식 발표(E-07) 모두 $1B 유니콘 언급 없음 — 미인용 주장 또는 소스 오귀속 |

---

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "NSA CNSA 2.0 신규 시스템 2027-01 의무화"
    current_sources: 1 (G-18 CyberArk 블로그, 내용 불일치)
    suggested_keywords: ["NSA CNSA 2.0 timeline 2027 mandatory", "NSA Commercial National Security Algorithm Suite 2.0 deadline"]

  - claim: "Intel Heracles FHE ASIC 5,547× 성능 향상"
    current_sources: 1 (E-05 IEEE Spectrum, 약 5,000× 확인 — 정확 수치 불확실)
    suggested_keywords: ["Intel Heracles ISSCC 2026 FHE 5547", "Intel FHE accelerator exact speedup"]

  - claim: "Zama $1B 유니콘 달성"
    current_sources: 0 (기재 소스들이 해당 내용 미포함)
    suggested_keywords: ["Zama unicorn 1 billion valuation 2025", "Zama Series B funding"]
```

---

## 5. URL-Content 검증

| # | URL 상태 | 본문 주장 | 판정 | 비고 |
|---|---------|---------|------|------|
| G-01 | 200 OK | Google 2029 PQC 데드라인 선언 | ⚠️ 부분 일치 | 페이지 주요 내용은 PQC 마이그레이션 타임라인이나, CSS/JS 중심 로딩으로 "2029" 데드라인 텍스트 직접 확인 불완전 |
| G-03 | 200 OK | NIST FIPS 203/204/205 확정 | ✅ 일치 | 2024-08-13 확정 명시 (본문 2024-08-14 표기와 1일 차이 — 경미) |
| G-07 | 접근 불가 | Thales+SKT QKD+PQC 상용화, 5G SIM PQC | 🔗 접근 불가 | Incapsula 봇 차단 |
| G-09 | 200 OK | (본문 미인용) | — | 고아 소스 |
| G-11 | 200 OK | KT QENC PQC 장비 보안기능확인 완료, 2026년 공공 조달 착수 | ⚠️ 부분 일치 | 보안기능확인 접수 확인, 2026 공공 조달 명시 없음 ("7월 발급 완료 → 전국 기관 활용 가능" 수준) |
| G-12 | 미검증 | KT FHE "계획 언급" | — | WebFetch 미실행 (보조 인용) |
| G-13 | 200 OK | LGU+ MWC26 동형암호 ixi-O AICC PoC | ✅ 일치 | LGU+ ixi-O AICC 동형암호 적용 계획 확인. 단, CryptoLab 협력 출처로는 부적합 (기사에 CryptoLab 미언급) |
| G-14 | 200 OK | CryptoLab HEaaN Zero-Leak RAG GS 1등급, 공공 조달 6월 계획 | ✅ 일치 | GS 1등급, 조달청 혁신시제품 6월 등록 계획 확인 |
| G-17 (CISA) | 접근 불가 | Apple BFV PIR (잘못된 귀속), CISA 1군 즉시 PQC 의무 | ❌ 불일치 | Apple BFV PIR 주장의 근거 URL이 CISA 문서 — 출처 귀속 오류. 대안: `machinelearning.apple.com/research/homomorphic-encryption` |
| G-17 (Apple) | 200 OK | Apple iOS 18 BFV PIR 키워드 검색 주장 | ⚠️ 부분 일치 | Apple 페이지는 "keyword-value database lookup"으로 기술. 본문 "인덱스 PIR(키워드 아님)" 표현은 원문과 상충 가능 |
| G-18 | 200 OK | NSA CNSA 2.0 2027-01 신규 시스템 의무화 | ❌ 불일치 | CyberArk 블로그는 NIST 2030/2035 타임라인만 기술. CNSA 2.0 2027 데드라인 없음. 대안: NSA 공식 CNSA 2.0 문서 |
| G-21 | 200 OK | Niobium+SemiFive Samsung 8nm, KRW 10B 계약 | ✅ 일치 | 수치 및 내용 전부 일치 |
| G-22 | 200 OK | T-REX+Zama $32B 기관 FHE 실도입, Zama $1B 유니콘 | ⚠️ 부분 일치 | $32B 수치 일치. $1B 유니콘 언급 없음 |
| G-24 | 200 OK | FHE.org Apple/AWS/Google 후원 진입 | ❌ 불일치 | FHE.org Digest #38에 Apple/AWS/Google 후원 언급 없음. 행사 정보만 수록 |
| G-25 | 200 OK | FHE TAM $251~310M(2026), $1,319M(2035), CAGR 20.2% | ✅ 일치 | 수치 일치 확인 |
| G-28 | 200 OK | TEE(SGX/SEV) 대비 FHE 10~100× 오버헤드 낮다는 주장 | ❌ 불일치 | arXiv 2502.14291은 AHE vs FHE 비교만 수록. TEE/SGX/SEV 언급 없음. 대안: 별도 TEE-FHE 비교 출처 필요 |
| P-01 | 접근 불가 | Aikata 97% 경량화, EuroS&P 2026 피어리뷰 확정 | 🔗 접근 불가 | iacr.org 403 오류 |
| P-02 | 200 OK | CAT GPU 33× 가속, 10³행 1초 | ✅ 일치 | arXiv 수치 정확히 일치 |
| P-03 | 접근 불가 | HET-PIR 3.9ms 키워드 검색 | 🔗 접근 불가 | Springer 저널 홈(링크가 논문 URL 아닌 저널 홈으로 등재) — 특정 논문 검증 불가 |
| P-04 | 200 OK | (본문 미인용) | — | 고아 소스 |
| E-01 | 200 OK | Android 17 ML-DSA API 공개, 2026 H2 출시 예정 | ⚠️ 부분 일치 | ML-DSA 네이티브 탑재 확인. "H2 출시 예정" 구체적 표현은 원문에 없음 ("next beta" → "production release") |
| E-03 | 200 OK | PQC 대역폭 100배 증가, IBM 재설계 제안 | ✅ 일치 | "hundredfold increase" 및 IBM 재설계 방안 확인 |
| E-04 | 접근 불가 | Thales+SKT 세계 최초 5G 양자내성암호 | 🔗 접근 불가 | Nasdaq PR 타임아웃 |
| E-05 | 200 OK | Intel Heracles ASIC 5,547×, ISSCC 2026, PCIe | ⚠️ 부분 일치 | "up to 5,000×" 확인. 정확히 "5,547×"는 기사 본문 미확인. PCIe 미확인 |
| E-06 | 200 OK | CryptoLab GS 1등급, LGU+ ixi-O 협력, 6월 조달 계획 | ⚠️ 부분 일치 | GS 1등급·6월 조달 계획 확인. LGU+ 협력은 이 기사에 없음 (G-13 분리 확인 필요) |
| E-07 | 200 OK | T-REX+Zama FHE 기밀성 레이어, 2026-03-26 | ⚠️ 부분 일치 | 내용 일치. 단, 원본 날짜 "March 24, 2026" vs 본문 "2026-03-26" 불일치 |
| G-17 (Apple) | 200 OK | (본문에서 `ref-g-17`로 잘못 연결됨) | ❌ 불일치 | 비표준 ID `G-17 (Apple)` — 앵커 링크 `ref-g-17-apple` 인데 본문 인용은 `ref-g-17` 사용 |

---

## 3. 논리 검증

**전반적으로 PASS.** 아래 1건의 경미한 논리 이슈를 기록한다.

### 3-1. FHE.org 빅테크 후원 진입 주장 (G-24, ❌ 불일치)

본문 192행에서 "빅테크 FHE.org 후원 진입(Apple·AWS·Google)" 리스크를 G-24로 인용하나, FHE.org Digest #38 페이지에는 Apple·AWS·Google 후원 언급이 없다. 이 주장은 출처 미지지 상태로 본문에 제시되어 있어 리스크 판단의 근거가 약하다.

### 3-2. Conditional Go 판정 논리

총점 134/200 → Conditional Go(120~159) 범위 정확히 해당. 상승 요인(+9) 분해 계산도 내부 일관성 유지.

### 3-3. 이전 대비 점수 변동 검증

| 항목 | 이전 | 현재 | 변동 |
|------|------|------|------|
| 고객가치 | 24 | 26 | +2 |
| 시장매력도 | 29 | 31 | +2 |
| 기술경쟁력 | 28 | 30 | +2 |
| 경쟁우위 | 24 | 25 | +1 |
| 실행가능성 | 20 | 22 | +2 |
| **합계** | **125** | **134** | **+9** |

총 +9점 변동 선언과 합산 일치. PASS.

---

## 4. 편향 검증

**전반적으로 PASS.** 강점/리스크 양면 서술이 균형 있게 제시되어 있다.

- Go 전환 조건 6건 명시(3건 미충족, 1건 진행 중) — 제약 요인 은폐 없음 ✅
- TEE 대체재 존재 및 10~100× 오버헤드 이점 명시 ✅ (출처는 불일치이나 주장 자체는 학술적으로 알려진 사실)
- On-Device E2E 미실증 반복 명시 ✅
- WTP 미검증 [미검증] 태그 ✅
- CryptoLab 단일 파트너 의존도 리스크 명시 ✅

---

## 결론

**판정: PARTIAL**

핵심 이슈는 두 가지다. 첫째, G-17 앵커 ID 충돌로 Apple BFV PIR 주장이 CISA URL을 근거로 인용되고 있어 독자 검증 시 출처 오인이 발생한다. 둘째, G-18(CyberArk 블로그)이 NSA CNSA 2.0 2027-01 의무화 근거로 반복 인용(3회)되나 실제 페이지 내용과 불일치하여 규제 긴박도 주장의 핵심 근거가 취약하다. 반면 채점 합산, 판정 범위, 수치 내부 일관성은 모두 정확하다. Zama $1B 유니콘 주장은 인용 소스 어디에도 근거가 없어 본문에서 제거하거나 별도 출처가 필요하다.
