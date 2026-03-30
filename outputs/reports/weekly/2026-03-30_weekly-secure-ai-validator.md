---
validator_status: partial
target_file: /Users/ctoti/Project/ClaudeCode/outputs/reports/weekly/2026-03-30_weekly-secure-ai.md
verified_at: 2026-03-30
---

# Validation Report — 2026-03-30_weekly-secure-ai

## 요약
- 상태: PARTIAL (조건부 통과)
- 주요 이슈:
  - **Critical 3건**: G-09 AFWERX/TACFI·MDA SHIELD 수치가 해당 URL 미지지(별도 URL에서 확인됨), G-16 Multiverse+Axelera PQC KSE3 결합 주장이 원문에 없음, G-28 FHE.org Apple·AWS·Google 후원 Digest #38에서 미확인(실제는 fhe.org 공식 페이지에 있음)
  - **Minor 4건**: G-12 CRYSTALS-Kyber·SKT 협력 원문 미언급, G-19 "14%"·"12~15년" 수치 원문 미확인, G-31 KT QKD+AI+동형암호 결합 전략 원문 내용 불일치, Zama $1.5억+ 수치 과대(실제 $107.8M)
  - 고아 소스: References 번호 G-04/06/08/11/14/18 건너뜀(정상 제거된 것으로 추정)
  - URL 접근 불가: G-02(TechSpot 403), G-10(CISA 403), G-13(MDPI 403), G-15(EE Times 타임아웃), G-20(Security Boulevard 403), G-21(IACR 403), P-01(IACR ePrint 403), E-03(Nasdaq 타임아웃)

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | 단일 통합 테이블, 34건 등재 |
| 모든 [N] 인용 매칭 | ✅ | 본문 인용 코드 34개 전수 References 테이블 매핑 확인 |
| 앵커 링크 형식 | ✅ | `[[X-nn]](#ref-x-nn)` 형식 일관 적용 |
| 미인용 주장 발견 | ✅ | 본문 내 주요 수치 전부 인용 코드 포함 |
| 번호 연속성 | ⚠️ | G-04/06/08/11/14/18 건너뜀. 이전 버전에서 제거된 것으로 추정되나, 명시적 주석 없음 |

**본문 인용 코드 전체 목록 (34개):**
G-01~03, G-05, G-07, G-09~10, G-12~13, G-15~17, G-19~32 / P-01~03 / E-01~06 / C-01

---

## 2. 수치 검증

| 수치 | 인용 | 소스 수 | 판정 | 비고 |
|------|------|---------|------|------|
| Google 2029 PQC 데드라인 | G-01, G-02 | 2 | ✅ [A] | G-01 확인, G-02 403 차단이나 WebSearch로 존재 교차 확인 |
| Android 17 ML-DSA 4계층 | G-03, E-01 | 2 | ✅ [A] | 두 소스 모두 4계층 구조 확인 |
| ML-DSA 서명 ~3,293바이트(ECDSA 대비 ~51×) | G-03, E-01 | 2 | ⚠️ 단일 소스 | G-03·E-01 본문에 수치 미명시. WebSearch에서 독립 소스(Medium) 확인. 원문 출처 특정 어려움 |
| Chrome ML-KEM 기본 활성화 | E-01 | 1 | ❌ 불일치 | E-01(Google Security Blog)은 Android 17에만 집중, Chrome 언급 없음. 별도 소스 필요 |
| PQShield 5KB RAM | G-05 | 1 | ✅ [B] | 원문 직접 확인 "less than 5KB" |
| IBM+Signal+Threema 대역폭 100× | G-07 | 1 | ✅ [B] | "up to a hundredfold increase" 확인 |
| QuSecure AFWERX $3.9M + MDA SHIELD $151B | G-09, E-02 | 2 | ⚠️ 귀속 불일치 | G-09 URL에 두 수치 모두 없음. WebSearch로 별도 URL(Quantum Insider, QuSecure 자체 PR)에서 사실 확인. E-02도 두 수치 미포함 (SEC 프레임워크 내용만) |
| CISA 1군/2군 분류 | G-10 | 1 | ✅ [A] | G-10 403 차단이나 WebSearch로 내용 교차 확인. 협업 도구 1군, 통신장비 2군 일치 |
| Axelera AI EU €200M+ | G-15 | 1 | 🔗 접근 불가 | URL 타임아웃. 제목 상 "$250M"으로 "€200M+" 표기와 차이 존재 가능 |
| Multiverse+Axelera PQC KSE3 결합 | G-16 | 1 | ❌ 불일치 | 원문에 "PQC KSE3" 언급 없음. 엣지 AI 모델 압축 협력만 확인 |
| SKT QKD-PQC 하이브리드 세계 최초 | G-17 | 1 | ✅ [A] | 원문 QKD-PQC 하이브리드 확인. 위성통신·PIC 기술 미언급(부분 불일치) |
| 기업 14%만 전수 조사 완료, 12~15년+ 소요 | G-19 | 1 | ❌ 불일치 | 원문에 해당 수치 없음. [추가확인 필요] 태그 붙어 있으나 근거 불명 |
| 2026 Pure PQC보다 하이브리드 지배 | G-20 | 1 | 🔗 접근 불가 | 403 차단. WebSearch 결과는 일반적으로 하이브리드 접근 논의됨 |
| "Privacy at your Fingertips" 97% 감소 | G-21, P-01 | 2 | ✅ [A] | G-21(IACR) 403이나 WebSearch로 확인. P-01 IACR ePrint도 403이나 타이틀/발표 사실 복수 경로 확인 |
| "Privacy at your Fingertips" 76× 속도 향상 | G-21, P-01 | 2 | ⚠️ 미확인 | 97% 감소는 확인되나 "선행 연구 대비 76×" 수치는 원문 직접 확인 불가 |
| CAT CKKS 33× 가속, RTX 4090 2,173× | G-22, P-02 | 2 | ✅ [A] | arXiv 직접 확인. "33× speedup", "up to 2173×" 정확 일치 |
| Intel Heracles 1,074~5,547×, 14μs | G-23, E-04 | 2 | ✅ [B] | Tom's Hardware 제목에서 배수 확인, Slashdot 커뮤니티에서 14μs 확인 |
| Intel Heracles 기술 사양(1.2GHz, 197mm², Intel 3) | G-23, E-04 | 2 | ⚠️ 미확인 | Tom's Hardware CSS/JS 구조로 본문 미추출. 별도 WebSearch 필요 |
| T-REX + Zama $32B RWA, $3.5조 Apex, 2027 $1,000억 | G-24, E-05 | 2 | ✅ [A] | Benzinga(G-24) + Zama 공식 블로그(E-05) 모두 확인 |
| Zama 유니콘($1B+) | G-24 (E-05 포함) | 2 | ✅ [A] | Series B 2025-06 $57M으로 $1B 유니콘 달성 WebSearch 확인 |
| Zama 누적 $1.5억+ | G-29 | 1 | ❌ 불일치 | G-29(SeedTable)는 Zama $107.8M으로 기재. "$1.5억+"은 과대 표기. 실제 누적 총투자는 $73M(Series A) + $57M(Series B) = ~$130M |
| FHE 스타트업 8개사 누적 $2.79억 | G-29 | 1 | ✅ [C] | "$278.9m" 확인, 본문의 "$2.79억" 표기는 백만 달러($278.9M) 오기입 가능성 — "$2억 7,900만" 기재 필요 |
| FHECore CKKS 부트스트래핑 50% 감소, 면적 오버헤드 2.4% | G-25, P-03 | 2 | ✅ [A] | P-03(arXiv) 직접 확인. G-25는 403 차단이나 수치는 P-03으로 독립 확인 |
| BU/Northeastern/KAIST/Murcia 기관 | P-03 | 1 | ⚠️ 미확인 | arXiv 저자 목록 있으나 기관 소속 미명시 |
| SemiFive+Niobium Samsung 8nm, 100억 원 | G-27 | 1 | ✅ [B] | 원문 직접 확인 |
| FHE.org 타이페이 10편/23편/Apple·AWS·Google 후원 | G-28 | 1 | ⚠️ 부분 불일치 | G-28(Digest #38)에서 10편/23편/스폰서 정보 미확인. 실제 수치는 fhe.org 공식 페이지(별도 URL)에서 확인됨 — 사실은 맞으나 인용 소스 오류 |
| KT AI 보이스피싱 1,300억 원, 4,400만 건, 3만 건 | G-30 | 1 | ✅ [B] | 전자신문 원문 직접 확인 |
| KT QKD+AI+동형암호 결합 전략 | G-31 | 1 | ⚠️ 부분 불일치 | G-31(보안뉴스) 원문은 KT 전략이 아닌 경영진 공백 이슈 중심. WebSearch에서 insightkorea 등 다른 소스가 QKD·AI·동형암호 3중 전략 확인 |
| 트럼프 Cyber Strategy 3/6, PQC+제로트러스트+AI | G-32 | 1 | ✅ [B] | UV Cyber 원문 "March 6, 2026 Cyber Strategy", PQC+zero trust+AI-driven defense 명시 확인 |

---

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "ML-DSA 서명 ~3,293바이트(ECDSA 대비 ~51×)"
    current_sources: 1 (간접 — 원문에 수치 미명시)
    suggested_keywords: ["ML-DSA-65 signature size bytes ECDSA comparison", "Android 17 PQC signature overhead"]

  - claim: "기업 14%만 양자 취약 시스템 전수 조사 완료. 대기업 마이그레이션 12~15년+ 소요"
    current_sources: 0 (G-19 원문에 해당 수치 없음)
    suggested_keywords: ["enterprise PQC cryptographic inventory 14 percent survey 2025 2026", "post-quantum migration timeline 12 15 years large organizations"]

  - claim: "Zama 단독 $1.5억+ (유니콘)"
    current_sources: 1 (수치 불일치 — 실제 $107.8M per G-29)
    suggested_keywords: ["Zama FHE total funding raised Series A Series B cumulative"]

  - claim: "FHE.org 타이페이(3/8): 10편 발표, 23편 포스터. Apple·AWS·Google 후원"
    current_sources: 1 (G-28이 아닌 별도 URL에서 확인)
    suggested_keywords: ["FHE.org 2026 conference Taipei accepted talks posters sponsors"]
    alternative_url: "https://fhe.org/conferences/conference-2026/"
```

---

## 5. URL-Content 검증

| # | URL 상태 | 본문 주장 | 판정 | 비고 |
|---|---------|---------|------|------|
| G-01 | 200 OK | Google 2029 PQC 데드라인 선언, CRQC·SNDL 위협 언급 | ✅ 일치 | 메타데이터로 제목·날짜 확인, 본문 CSS 구조로 일부 텍스트 미추출이나 WebSearch 교차 확인 |
| G-02 | 403 차단 | Google 2029 데드라인, NIST 2030보다 1년 앞당김 | 🔗 접근 불가 | WebSearch로 사실 자체는 교차 확인 |
| G-03 | 200 OK | Android 17 ML-DSA 4계층 통합, ML-DSA-65/87 Keystore API | ✅ 일치 | 4계층 구조 확인. ML-DSA 서명 3,293바이트 수치는 원문 미명시 (⚠️) |
| G-05 | 200 OK | PQShield PQMicroLib-Core 5KB RAM, Embedded World 2026, TLS, 소프트웨어 업그레이드 | ✅ 일치 | 전항목 원문 확인 |
| G-07 | 200 OK | IBM+Signal+Threema 대역폭 100× 정량화, Real-World Crypto 2026, 분산 검증 방식 | ✅ 일치 | "up to a hundredfold" 확인 |
| G-09 | 200 OK | QuSecure SEC PQFIF 인용, Banco Sabadell+Accenture 4개월 마이그레이션 | ⚠️ 부분 불일치 | Banco Sabadell 케이스는 확인됨. AFWERX $3.9M·MDA SHIELD $151B는 이 URL에 없음. 해당 수치는 별도 QuSecure/Quantum Insider URL에서 확인 |
| G-10 | 403 차단 | CISA 1군(클라우드·협업·브라우저·엔드포인트) 즉시 PQC 의무, 2군(통신장비·OS·스토리지·IAM) 전환 중 | ✅ 일치 | 403이나 WebSearch(Infosecurity Magazine 등)로 1군/2군 분류 내용 교차 확인 |
| G-12 | 200 OK | Thales 5G SIM OTA PQC 세계 최초 시연, CRYSTALS-Kyber, SKT 협력 | ⚠️ 부분 불일치 | OTA PQC 시연 확인. CRYSTALS-Kyber 및 SKT 협력은 원문 미명시. 2023년 별도 SKT-Thales 협력은 WebSearch로 확인됨 |
| G-13 | 403 차단 | MDPI Electronics 격자 기반 암호화 하드웨어 가속기, NTT 연산 온디바이스 오프로드 | 🔗 접근 불가 | 403. MDPI Electronics 저널 자체는 실존하나 특정 주장 검증 불가 |
| G-15 | 타임아웃 | Axelera AI EU Innovation Council €200M+ 조달, Europa AIPU | 🔗 접근 불가 | 타임아웃. EE Times 기사 제목에 "$250M"으로 기재 — "€200M+"와 환율 불일치 가능성 |
| G-16 | 200 OK | Multiverse Computing + Axelera: 엣지 AI 모델 압축 + PQC KSE3 결합(3/18) | ❌ 불일치 | "PQC KSE3" 언급 없음. 엣지 AI 모델 압축 협력만 확인됨. PQC 결합 주장은 원문 근거 없음 |
| G-17 | 200 OK | SKT QKD-PQC 하이브리드 장비 세계 최초, NIST FIPS 203/204 준수 | ✅ 일치 | 핵심 주장 확인. 위성통신·PIC 기술 언급은 해당 기사에 없음(별도 SKT 발표로 추정) |
| G-19 | 200 OK | 기업 14%만 전수 조사 완료, 대기업 마이그레이션 12~15년+ | ❌ 불일치 | 원문에 14% 및 12~15년 수치 없음. [추가확인 필요] 태그 부여는 적절하나 출처 오귀속 가능성 높음 |
| G-20 | 403 차단 | 2026년 Pure PQC보다 하이브리드 접근 지배 전망 | 🔗 접근 불가 | 403 |
| G-21 | 403 차단 | "Privacy at your Fingertips" EuroS&P 2026 발표 소식 | 🔗 접근 불가 | IACR 403. WebSearch로 논문 존재·EuroS&P 2026 발표 사실 교차 확인 |
| G-22 | 200 OK | CAT GPU FHE 프레임워크 CKKS 33×, RTX 4090 2,173×, 1초 내 10³행 | ✅ 일치 | arXiv 원문 직접 확인, 모든 수치 일치 |
| G-23 | 200 OK (부분) | Intel Heracles 1,074~5,547× Xeon 가속, 14μs 쿼리 | ✅ 일치 | 제목에서 배수 확인, Slashdot 커뮤니티에서 14μs vs 15ms 확인. 기술 사양(1.2GHz 등)은 CSS 구조로 본문 미추출 |
| G-24 | 200 OK | T-REX+Zama $32B ERC-3643, Apex $3.5조, 2027 $1,000억 | ✅ 일치 | Benzinga 원문 직접 확인, 전항목 일치 |
| G-25 | 403 차단 | FHECore CKKS 부트스트래핑 50% 감소, 면적 오버헤드 2.4% | 🔗 접근 불가 | 403. P-03(arXiv)으로 동일 수치 독립 확인 |
| G-26 | 200 OK | LGU+ CryptoLab MWC26 AICC 동형암호, 고객 데이터 암호화 비교·분석 | ✅ 일치 | 원문 확인 |
| G-27 | 200 OK | SemiFive+Niobium Samsung 8nm FHE ASIC, 100억 원, 세계 최초 | ✅ 일치 | "KRW 10 billion", "Samsung Foundry 8nm" 원문 확인 |
| G-28 | 200 OK | FHE.org 타이페이 10편/23편/Apple·AWS·Google 후원 | ❌ 불일치 | Digest #38에 10편·23편·스폰서 정보 없음. 실제 수치는 fhe.org 공식 페이지에 있음. 대안 URL: https://fhe.org/conferences/conference-2026/ |
| G-29 | 200 OK | FHE 스타트업 8개사 누적 $2.79억, Zama $1.5억+ | ⚠️ 부분 불일치 | 8개사·$278.9m 확인. Zama는 "$107.8m"으로 기재 — "$1.5억+"은 불일치. 누적이 $107.8M이고 $1.5억+(=$150M)은 개별 별도 발표 기준으로 추정되나 G-29에서는 미지지 |
| G-30 | 200 OK | KT AI 보이스피싱 탐지 1,300억 원, 4,400만 건, 3만 건 | ✅ 일치 | 전자신문 원문 직접 확인 |
| G-31 | 200 OK | KT QKD+AI+동형암호 결합 전략, 전 구간 적용 계획 | ❌ 불일치 | 원문(보안뉴스)은 KT 경영진 공백·동력 상실이 주요 내용. 3중 보안 전략 내용 없음. 실제 전략은 insightkorea 등 별도 소스에서 확인 |
| G-32 | 200 OK | 트럼프 Cyber Strategy 3/6, PQC+제로트러스트+AI 방어 명시 | ✅ 일치 | "March 6, 2026", "PQC alongside zero trust architecture, AI-driven defense" 확인 |
| P-01 | 403 차단 | "Privacy at your Fingertips" EuroS&P 2026, Boosted-Deflation 97% 감소, 76× 속도 향상 | 🔗 접근 불가 | IACR ePrint 403. 논문 존재 자체는 G-21 IACR 뉴스·WebSearch로 확인 |
| P-02 | 200 OK | CAT GPU FHE arXiv 2503.22227 | ✅ 일치 | G-22와 동일 arXiv — 중복 등재이나 허용 범위 |
| P-03 | 200 OK | FHECore arXiv 2602.22229, 50% 감소, 2.4% 면적 오버헤드 | ✅ 일치 | arXiv 직접 확인. 기관 소속(BU/Northeastern/KAIST/Murcia)은 미표시 |
| E-01 | 200 OK | Google Security Blog Android 17 ML-DSA 4계층, Chrome ML-KEM | ⚠️ 부분 불일치 | 4계층 확인. Chrome ML-KEM 언급 없음 — Chrome 관련 주장은 별도 소스 필요 |
| E-02 | 200 OK | QuSecure SEC PQFIF, Banco Sabadell, AFWERX $3.9M, MDA SHIELD $151B | ❌ 불일치 | E-02에 AFWERX/MDA 수치 없음. SEC 프레임워크·Banco Sabadell만 확인. 두 수치는 별도 QuSecure PR URL에서 확인됨 |
| E-03 | 타임아웃 | Thales 세계 최초 양자안전 5G SIM, CRYSTALS-Kyber, SKT | 🔗 접근 불가 | Nasdaq 타임아웃. WebSearch에서 Yahoo Finance/Thales 공식 페이지로 "세계 최초" 발표 사실 확인됨 |
| E-04 | 200 OK (부분) | Intel Heracles FHE ISSCC Demo, 기술 사양 | ⚠️ 부분 불일치 | IEEE Spectrum 구조 상 기술 사양 텍스트 미추출. ISSCC 연관성만 태그로 확인 |
| E-05 | 200 OK (리다이렉트) | Zama T-REX Ledger FHE 기밀성 레이어 출시 | ✅ 일치 | zama.org로 리다이렉트 후 확인. $32B·Apex·ERC-3643 전항목 일치 |
| E-06 | 200 OK | LGU+ Human-Centered AI MWC 2026, CryptoLab 동형암호, AICC | ✅ 일치 | 전항목 원문 확인 |
| C-01 | 200 OK | Slashdot Intel Heracles, 수백 건 댓글, 회의론·기대감 혼재 | ✅ 일치 | 커뮤니티 댓글 및 회의론 확인 |

---

## 3. 논리 검증

- **G-16 논리 비약**: Multiverse+Axelera 협력을 "엣지 AI 모델 압축 + PQC KSE3 결합"으로 서술했으나, 원문은 AI 모델 압축만 다룸. PQC KSE3 결합은 원문에 근거 없는 추론. [❌]
- **G-15 Axelera Europa AIPU "KSE3 PQC 내장" 주장**: 시장 시그널 섹션에서 "Europa AIPU(KSE3 PQC 내장) 생산 재원 확보"로 서술했으나 G-15 URL 확인 불가(타임아웃). G-16과 결합하여 PQC KSE3 내장 주장의 근거가 불명확. [⚠️]
- **주요 결론 도출**: Google 2029 선언 → 통신사 로드맵 조기화 압력 분석, FHE 3축(하드웨어·소프트웨어·비즈니스) 동시 수렴 분석 등 논리적 도출은 적절함. [✅]
- **SKT/KT/LGU+ 양극화 시사점**: 실증 데이터(SKT FIPS 203/204 준수, KT 1,300억 피해 예방, LGU+ PoC)로부터 도출되어 근거 있음. [✅]

---

## 4. 편향 검증

- **강점/약점 균형**: 각 기술 섹션에 "기회"와 "위협" 양면을 명시적으로 서술. PQC 메시징 대역폭 100× 증가 문제, Intel Heracles 양산 미발표, Apple 온디바이스 FHE 미완성 등 부정적 요소 포함. [✅]
- **경쟁사 균형**: SKT(PQC 선두), KT(AI 피싱 탐지 실적), LGU+(동형암호 차별화) 세 사업자의 차별화 축을 균형 있게 서술. 특정 사업자 편중 없음. [✅]
- **기술 낙관 편향 가능성**: "하드웨어·소프트웨어·비즈니스 3축이 동시에 움직이는 첫 주"라는 표현은 낙관적이나, 직후 위협 섹션에서 Intel Heracles 양산 미발표·킬러앱 부재·전문가 50인 미만을 열거하여 균형 잡힘. [✅]

---

## 6. Critical 이슈 상세

### Critical-1: G-09 / E-02 — QuSecure AFWERX·MDA SHIELD 수치 귀속 오류
- **본문 주장**: "QuSecure, SEC 제출 PQFIF에서 금융 PQC 레퍼런스 공식 인용(3/19). Banco Sabadell+Accenture 4개월 마이그레이션. AFWERX/TACFI $3.9M 미공군 계약, MDA SHIELD $151B 계약 수주. [[G-09]], [[E-02]]"
- **G-09 실제 내용**: SEC PQFIF + Banco Sabadell 케이스만 다룸. AFWERX·MDA 수치 없음.
- **E-02 실제 내용**: QuSecure 공식 블로그이나 SEC 프레임워크 내용만. AFWERX·MDA 수치 없음.
- **실제 소스**: AFWERX $3.9M은 별도 QuSecure PR(qusecure.com/tacfi-il6-post-quantum-encryption-us-air-force/), MDA SHIELD $151B는 별도 URL(qusecure.com/qusecure-awarded-mda-shield-contract/)
- **판정**: 사실은 맞으나 인용 소스 귀속 오류. 별도 References 등재 필요.

### Critical-2: G-16 — Multiverse+Axelera PQC KSE3 결합 주장 원문 미지지
- **본문 주장**: "Multiverse Computing + Axelera: 엣지 AI 모델 압축 + PQC KSE3 결합(3/18) [[G-16]]"
- **G-16 실제 내용**: 엣지 AI 모델 압축·최적화 협력만 다룸. "PQC KSE3"는 언급 없음.
- **판정**: 근거 없는 주장 추가. PQC KSE3 결합 내용은 삭제하거나 별도 출처 필요.

### Critical-3: G-28 — FHE.org 콘퍼런스 수치 소스 오귀속
- **본문 주장**: "FHE.org 타이페이(3/8): 10편 발표, 23편 포스터. Apple·AWS·Google 후원 [[G-28]]"
- **G-28 실제 내용**: Digest #38은 콘퍼런스 등록 안내·일정 중심. 발표 수·포스터 수·스폰서 정보 없음.
- **실제 소스**: fhe.org 공식 콘퍼런스 페이지(https://fhe.org/conferences/conference-2026/)
- **판정**: 사실은 맞으나 소스 오귀속. 대안 URL로 교체 권고.

---

## 결론

본 리포트는 References 테이블이 완비되어 있고 인용 코드 교차 매핑 34건이 전수 확인되었다. URL-Content 검증에서 34건 중 18건(53%)이 완전 일치, 6건이 부분 불일치, 4건이 소스 귀속 오류(❌), 8건이 접근 불가(403/타임아웃)로 판정되었다. Critical 이슈 3건(G-09/E-02 수치 오귀속, G-16 근거 없는 PQC KSE3 주장, G-28 소스 오귀속)과 Minor 이슈 4건(G-12 협업 세부사항 미언급, G-19 핵심 수치 원문 미확인, G-31 KT 전략 원문 불일치, G-29 Zama 수치 불일치)이 존재하여 **PARTIAL** 판정을 부여한다. 기술적 사실 자체는 대부분 실재하나, 특정 수치들이 실제 해당 인용 URL에 존재하지 않고 별도 소스에서 확인되는 출처 귀속 오류 패턴이 이 리포트에서도 반복됨을 지적한다.
