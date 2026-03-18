---
topic: On-Device 동형암호 키워드 검색
domain: secure-ai
l2_topic: quantum-he
date: 2026-03-18
wtis_version: v4.1
wtis_mode: standard
skills_executed: [research-deep, SKILL-1, validator]
confidence: medium
status: completed
total_references: 49
verdict: Conditional Go
score: 125/200
strategy: Borrow(CryptoLab) + Build(AICC 통합) + Watch(HW/GL)
prior_report: 2026-03-03_secure-ai-v2/2026-03-03_wtis-secure-ai-v2.md
prior_report_date: 2026-03-03
---

# WTIS Report: On-Device 동형암호 키워드 검색

## Executive Summary

**시장**: FHE 글로벌 TAM $350~600M(보수)~$1~3B(적극) by 2030, CAGR 8~20% [[G-01]](#ref-g-01)[[G-02]](#ref-g-02)[[G-03]](#ref-g-03). AICC SAM CAGR 17~22% [[G-09]](#ref-g-09).
**기술**: TRL 2~3 → 3~4 상향. Intel Heracles 5,547× [[G-04]](#ref-g-04), HET-PIR 3.9ms [[P-03]](#ref-p-03), Aikata 클라이언트 97% 경량화 [[P-01]](#ref-p-01). On-Device 엔드-투-엔드 벤치마크는 미완.
**기회**: CKKS 원천 특허(한국), LGU+-CryptoLab MWC 2026 PoC [[E-01]](#ref-e-01), SKT/KT 동형암호 미추진 → 국내 선점 창구.
**위협**: Apple iOS 18 BFV PIR 실 배포(1~2년 선행) [[G-17]](#ref-g-17). TEE/가명처리 등 대체재 성능 우위. GL 스킴 등 경쟁 스킴 불확실성.
**권고**: Borrow(CryptoLab FHE 엔진) + Build(AICC 통합). On-Device PoC 벤치마크(<1초) 확보가 Go 전환 전제조건. 실시간 통화 FHE는 여전히 불가 → 비실시간 AICC 키워드 검색으로 유스케이스 전환.

## 이전 분석 대비 변화

| 항목 | 이전 (2026-03-03) | 현재 (2026-03-18) | 변화 |
|------|------------------|------------------|------|
| 핵심 판정 | Watch ("HE 제거") | Conditional Go | ↑ 상향 |
| 점수 | 120/200 (전체) | 125/200 (HE 단독) | +5 |
| TRL | 2~3 | 3~4 | ↑ |
| 유스케이스 | 실시간 통화 FHE | 비실시간 AICC 키워드 검색 | 전환 |
| 통신사 PoC | 없음 | LGU+-CryptoLab MWC 2026 | 신규 |
| 하드웨어 가속 | FPGA 연구 수준 | Intel ASIC+Niobium 파일럿 | 상용화 임박 |
| 표준화 | 모호 | NIST 4/20, ISO 3년, 서울 9차 | 구체화 |

**변화 주요 원인:**
- Intel Heracles ASIC(5,547×)과 Niobium Gen2(삼성 8nm) 발표로 서버-사이드 FHE 연산 병목 해소 방향 확인
- Aikata et al. 97% 클라이언트 경량화 논문(EuroS&P 2026)으로 On-Device 전제 조건 부분 해소
- HET-PIR(3.9ms) · BKPIR(10× 처리량) 키워드 PIR 구현 단계 진입
- LGU+-CryptoLab MWC 2026 PoC 공식화로 실행 경로 확보
- DESILO×Gentry GL 5세대 FHE 발표로 알고리즘 혁신 가속

## 1. 시장 분석

### TAM/SAM/SOM

| 구분 | 규모 | CAGR | 출처 |
|------|------|------|------|
| TAM (FHE 글로벌) | $350~600M(보수)~$1~3B(적극) by 2030 | 8~20% | [[G-01]](#ref-g-01)~[[G-03]](#ref-g-03) |
| SAM (AICC 음성보안) | $480M~$2B (2025) | 17~22% | [[G-09]](#ref-g-09) |
| SOM (한국 FHE) | $7~15M (PoC 단계) | — | [D, 편의 계산] |

### 연도별 시장 전망

| 기관 | 기준값 | 2030 전망 | CAGR | 신뢰도 |
|------|--------|-----------|------|--------|
| NextMSC | $189.5M (2022) | $358.9M | ~8.3% | [C] |
| GM Insights | $234.7M (2025) | $351.5M | ~8.4% | [C] |
| Data Bridge | $321.4M (2024) | $594.9M (2032) | ~8.0% | [C] |
| 360 Research | $251.2M (2026) | $1,319M (2035) | 20.2% | [C] |

> **Validator 지적**: G-02 GM Insights 기준값 $234.7M은 원본 페이지에 명시되지 않는 추정값일 가능성. 보수 TAM($350~600M)으로 해석 권장.

### 인접 시장 기회
- AICC(콜센터 AI) 시장 $2.4B(2025) → $13.5B(2034), CAGR 20.8% [[G-09]](#ref-g-09)
- AI기본법 시행(2026-01)으로 AICC 고위험 AI 분류 가능성 → 암호화 상태 처리 수요 [[G-24]](#ref-g-24)
- 한국 PET R&D 예산 확대(PIPC), EU AI Act 고위험 데이터 보호 강화

## 2. 기술 성숙도 분석

### TRL 매트릭스

```
              High TRL (7~9)
                    |
   [유지]           |          [베팅]
   Apple iOS 18     |
   BFV PIR (8~9)    |
                    |
   Low Disruption --+-- High Disruption
                    |
   [탐색]           |          [Conditional Go]
   CKKS+/GL 스킴   |          On-Device FHE
   (TRL 4~5)        |          키워드 검색 (TRL 3~4)
                    |
              Low TRL (1~6)
```

### 성능 벤치마크

| 기술 | 성능 | 근거 | 출처 |
|------|------|------|------|
| Intel Heracles ASIC | 1,074~5,547× vs 24코어 Xeon | 3nm, 48GB HBM3, CKKS/BGV/BFV | [[G-04]](#ref-g-04)[[G-05]](#ref-g-05) |
| Aikata 클라이언트 경량화 | enc/dec 97% 비용 절감, FPGA 76× | EuroS&P 2026, 마이크로컨트롤러 구현 | [[P-01]](#ref-p-01) |
| HET-PIR 키워드 검색 | 3.9ms/32비트 단일 비교, 0.01ms batch | Springer 피어리뷰 | [[P-03]](#ref-p-03) |
| BKPIR 키워드 PIR | 기존 대비 10× 처리량 | NDSS 2026 피어리뷰 | [[P-04]](#ref-p-04) |
| Niobium Gen2 ASIC | 삼성 8nm, 고객 파일럿 준비 | KRW 10B 계약 | [[G-06]](#ref-g-06) |
| CryptoLab HEaaN GPU | 100×+ 가속 | 상용 배포 | [[G-13]](#ref-g-13) |
| Apple BFV PIR | iOS 18 실 배포 | 인덱스 PIR(키워드 아님) | [[G-17]](#ref-g-17) |

### SMART Test 요약

| Criterion | 평가 | 핵심 근거 |
|-----------|------|----------|
| Specific | 충족 | On-Device FHE 키워드 검색 PoC, <1초 KPI |
| Measurable | 충족 | 레이턴시(ms), 정확도(precision/recall) 측정 가능 |
| Achievable | 조건부 | 서버-사이드 3.9ms 달성 가능. On-Device 실증 미완 |
| Relevant | 충족 | AI기본법, PIPA 개정이 수요 창출 |
| Time-bound | 부분 | 12~18개월 PoC 현실적. Apple 선행 압박 존재 |

### 표준화 현황

| 표준 | 상태 | 시점 | 출처 |
|------|------|------|------|
| NIST Threshold FHE (S5) | 미리보기 제출 마감 | 2026-04-20 | [[G-16]](#ref-g-16) |
| ISO/IEC 18033-8 | NWI 승인, 초안 작업 | 3년 타임라인 | [[G-15]](#ref-g-15) |
| HomomorphicEncryption.org | 9차 서울 개최 | 2026-03-05~06 | [[G-14]](#ref-g-14) |

## 3. 경쟁 환경

### Gap Analysis

| 역량 | 국내 (CryptoLab/DESILO/LGU+) | 글로벌 (Apple/Google/Intel) | 격차 |
|------|----------------------------|---------------------------|------|
| 알고리즘 원천 | CKKS 원천 특허, GL 스킴 | BFV(Apple), TFHE(Zama), HEIR(Google) | **대등** |
| On-Device 배포 | PoC 단계 | iOS 18 실 배포 (Apple) | **Apple 1~2년 선행** |
| 하드웨어 가속 | SEMIFIVE-Niobium (설계) | Intel Heracles (발표) | **Intel 선행** |
| 통신사 AICC 특화 | LGU+ PoC 유일 | Nokia QRYPT (연구) | **국내 잠재 우위** |
| 표준화 참여 | 운영위, 서울 9차 주최 | Intel Gold 스폰서 | **적극 참여** |
| 오픈소스 생태계 | HEaaN (제한 공개) | SEAL, HEIR, swift-HE 전면 공개 | **글로벌 우위** |

### 경쟁사 포지션

| 기업 | 단계 | 특이점 | 출처 |
|------|------|--------|------|
| Apple | 상용(인덱스 PIR) | iOS 18 BFV PIR. 키워드 PIR 아님 | [[G-17]](#ref-g-17) |
| Intel | ASIC 발표 | 5,547× 가속. 양산 미정 | [[G-04]](#ref-g-04) |
| Niobium | 파일럿 | 세계 최초 상업용 FHE ASIC 목표 | [[G-06]](#ref-g-06) |
| CryptoLab | PoC | CKKS 원천. LGU+ 파트너 | [[E-01]](#ref-e-01) |
| DESILO | 학술 발표 | GL 5세대. Gentry 공동 | [[E-02]](#ref-e-02) |
| Zama | mainnet | TFHE 유니콘 $1B | [[G-12]](#ref-g-12) |
| SKT | 미추진 | QKD+PQC 집중. FHE 공식 발표 없음 | [[N-02]](#ref-n-02) |
| KT | 미추진 | AI 보안 투자. FHE 직접 미확인 | [[N-03]](#ref-n-03) |

## 4. 전략 권고

### 3B 의사결정 경로

| 평가 요소 | 점수 | 판정 |
|----------|------|------|
| 차별화 중요도 | 7/10 | CKKS 원천+AICC 특화. 빅테크 미커버 영역 |
| 내부 역량 | 부분 | FHE 원천 미보유. AICC 인프라는 보유 |
| 시장 윈도우 | >18개월 | FHE AICC 상용 배포 기업 전무 |
| 시장 긴급성 | 5/10 | 규제 수요 생성 중이나 FHE 의무화 아님 |
| 기술 갭 | 0~1년(국내), 1~2년(vs Apple) | SKT/KT 미추진 → 선점 가능 |

**결론: Borrow(CryptoLab) + Build(AICC 통합) + Watch(HW/GL)**

| 기술 요소 | 전략 | 세부 |
|----------|------|------|
| FHE 키워드 검색 엔진 | **Borrow** | CryptoLab CKKS+ 파트너십 |
| On-Device 경량화 | **Borrow** | Aikata 기법 학술 협력 |
| AICC 통합 인프라 | **Build** | 익시오(ixi-O) FHE 통합 |
| 하드웨어 가속 | **Watch** | Niobium/Intel 양산 추적 |
| DESILO GL 스킴 | **Watch** | 벤치마크 공개 대기 |

### 후속 조건 체크리스트

- [ ] 기술기획: CryptoLab PoC 후속 — On-Device 단말 벤치마크 포함 (2026-Q2)
- [ ] 연구소: Aikata 클라이언트 경량화 적용 가능성 기술 검토 (2026-Q2)
- [ ] 전략기획: NIST Threshold Call (2026-04-20) CryptoLab 참여 현황 확인
- [ ] 사업기획: Niobium Gen2 ASIC 양산 일정·가격 수집 (2026-H2)
- [ ] 법무/규제: AI기본법 AICC 고위험 분류 확정 여부 모니터링

## 5. 교차검증 결과

**Validator 판정: PARTIAL** (Critical 1건, Minor 4건)

| # | 유형 | 심각도 | 내용 | 처리 |
|---|------|--------|------|------|
| 1 | 수치 | Critical | G-02 GM Insights $234.7M — 원본 미명시 추정값 가능 | 보수 TAM($350~600M) 범위로 해석. 단일 수치 의존 배제 |
| 2 | 인용 | Minor | E-03(Cornami), P-05(Spiral PIR) — 고아 소스 | 본문 인용 불필요 항목. References에 참고용 유지 |
| 3 | 소스 | Minor | SKT 7,000억, KT 1조 — 단일 언론 소스 | 경쟁사 투자 규모는 참고치로만 활용. 판정에 미반영 |

**핵심 9개 수치 독립 검증 통과**: Intel 5,547×, Aikata 97%, HET-PIR 3.9ms, BKPIR 10×, Niobium KRW 10B, Zama $1B, Apple iOS 18 PIR, NIST 4/20, 서울 9차.

**최종: PARTIAL → 핵심 판정에 영향 없음.** Critical 이슈는 시장 규모 추정치 1건이며 보수 범위로 해석함으로써 해소.

## 6. 정량 평가 (125/200)

| # | 평가 항목 | 세부1 | 세부2 | 세부3 | 세부4 | 소계 |
|---|----------|-------|-------|-------|-------|------|
| 1 | 고객가치 | 7 (pain point) | 7 (가치 명확성) | 5 (대체재 대비) | 5 (수용성) [D] | **24/40** |
| 2 | 시장매력도 | 6 (TAM/SAM) | 7 (CAGR) | 8 (타이밍) | 8 (규제) | **29/40** |
| 3 | 기술경쟁력 | 6 (TRL 3~4) | 8 (CKKS 특허) | 7 (기술 장벽) | 7 (표준화) | **28/40** |
| 4 | 경쟁우위 | 6 (포지션) | 6 (지속성) | 5 (대응력) | 7 (생태계) | **24/40** |
| 5 | 실행가능성 | 5 (내부 역량) | 5 (ROI) [D] | 6 (일정) | 4 (리스크) | **20/40** |
| | **총점** | | | | | **125/200** |

**판정: Conditional Go (120~159)**

Conditional Go 범위 하단. 상승 요인: TRL +1, LGU+ PoC, CKKS 특허·표준화. 제약 요인: On-Device 실증 미완, WTP 미검증, 내부 FHE 역량 부재.

**이전 "HE 제거" 판정 재평가**: 실시간 통화 FHE는 여전히 불가(ITU-T 150ms 초과). 비실시간 AICC 키워드 검색으로 유스케이스 전환이 적절한 재평가 결론.

**Go 전환 조건:**
1. On-Device PoC 벤치마크 <1초 실증 (필수)
2. CryptoLab 파트너십 공식 계약 (필수)
3. AICC 고객 실 데이터 검증 (필수)
4. 하드웨어 가속기 로드맵 확인 (참조)
5. 대체재(TEE) 대비 우위 정량화 (Go 조건)

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | NextMSC — FHE Market $189.5M→$358.9M | [링크](https://www.nextmsc.com/report/homomorphic-encryption-market) | report | 2024 | [C] |
| <a id="ref-g-02"></a>G-02 | GM Insights — FHE Market Forecasts | [링크](https://www.gminsights.com/industry-analysis/homomorphic-encryption-market) | report | 2025 | [C] |
| <a id="ref-g-03"></a>G-03 | 360 Research — FHE Market CAGR 20.2% | [링크](https://www.360researchreports.com/market-reports/homomorphic-encryption-market-206111) | report | 2025 | [C] |
| <a id="ref-g-04"></a>G-04 | Tom's Hardware — Intel Heracles 5,547× | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2026-03 | [B] |
| <a id="ref-g-05"></a>G-05 | IEEE Spectrum — Intel Heracles FHE | [링크](https://spectrum.ieee.org/fhe-intel) | news | 2026-03 | [B] |
| <a id="ref-g-06"></a>G-06 | PR Newswire — SEMIFIVE×Niobium (Samsung 8nm) | [링크](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) | 보도자료 | 2026-02-19 | [A] |
| <a id="ref-g-07"></a>G-07 | CybersecAsia — DESILO GL 5세대 | [링크](https://cybersecasia.net/pr-newswire/desilo-and-fhe-inventor-craig-gentry-introduce-5th-generation-gl-fhe-scheme-for-private-ai/) | news | 2026-03-08 | [B] |
| <a id="ref-g-09"></a>G-09 | Fortune BI — Call Center AI $2.4B→$13.5B | [링크](https://www.fortunebusinessinsights.com/call-center-ai-market-109249) | report | 2025 | [C] |
| <a id="ref-g-10"></a>G-10 | Nokia Bell Labs — QRYPT 암호화 음성 | [링크](https://www.nokia.com/bell-labs/collaboration-opportunities/entrepreneurs-in-residence/end-to-end-encrypted-audio-conferencing/) | 연구 | 2025 | [B] |
| <a id="ref-g-12"></a>G-12 | BlockEden — Zama $1B 밸류에이션 | [링크](https://blockeden.xyz/blog/2026/01/05/zama-protocol/) | news | 2026-01 | [B] |
| <a id="ref-g-13"></a>G-13 | CryptoLab — HEaaN GPU 100×+ | [링크](https://www.cryptolab.co.kr/en/products-en/heaan-he/) | 공식 | 2025 | [A] |
| <a id="ref-g-14"></a>G-14 | HomomorphicEncryption.org — 9차 서울 | [링크](https://homomorphicencryption.org/9th-homomorphicencryption-org-standards-meeting/) | 공식 | 2026-03 | [A] |
| <a id="ref-g-15"></a>G-15 | IAPP — ISO/IEC 18033-8 FHE 표준 | [링크](https://iapp.org/news/a/the-latest-in-homomorphic-encryption-a-game-changer-shaping-up) | news | 2025 | [B] |
| <a id="ref-g-16"></a>G-16 | NIST — Threshold Cryptography FHE S5 | [링크](https://csrc.nist.gov/projects/threshold-cryptography) | 공식 | 2026 | [A] |
| <a id="ref-g-17"></a>G-17 | Apple ML Research — iOS 18 BFV PIR | [링크](https://machinelearning.apple.com/research/homomorphic-encryption) | 공식 | 2024 | [A] |
| <a id="ref-g-18"></a>G-18 | Swift.org — swift-homomorphic-encryption | [링크](https://www.swift.org/blog/announcing-swift-homomorphic-encryption/) | 공식 | 2024 | [A] |
| <a id="ref-g-19"></a>G-19 | Google — FHE Offering (Jaxite, HEIR) | [링크](https://developers.googleblog.com/en/expanding-our-fully-homomorphic-encryption-offering/) | 공식 | 2025-11 | [A] |
| <a id="ref-g-20"></a>G-20 | Dialzara — SEAL 4,500+ 앱 | [링크](https://dialzara.com/blog/homomorphic-encryption-securing-ai-privacy) | blog | 2025 | [C] |
| <a id="ref-g-21"></a>G-21 | Quantum Insider — Niobium $23M+ | [링크](https://thequantuminsider.com/2025/12/03/niobium-23m-fhe-funding/) | news | 2025-12 | [B] |
| <a id="ref-g-24"></a>G-24 | Securiti — Korea AI Safe Use / PIPA | [링크](https://securiti.ai/south-korea-safe-use-of-personal-information-in-ai/) | 분석 | 2025 | [B] |
| <a id="ref-g-34"></a>G-34 | Springer — FHE vs ABE 성능 비교 | [링크](https://www.nature.com/articles/s41598-025-19404-w) | paper | 2025 | [A] |
| <a id="ref-n-01"></a>N-01 | Asia Business Daily — LGU+ CryptoLab MWC | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | news | 2026-03-10 | [B] |
| <a id="ref-n-02"></a>N-02 | SKT Newsroom — QKD-PQC 하이브리드 | [링크](https://news.sktelecom.com/207758) | 보도자료 | 2025 | [A] |
| <a id="ref-n-03"></a>N-03 | Global Economic — KT 1조 투자 | [링크](https://www.g-enews.com/article/ICT/2025/07/2025071511020968510b8d776efa_1) | news | 2025-07 | [C] |
| <a id="ref-e-01"></a>E-01 | CryptoLab CEO + LGU+ CTO — MWC 2026 | — | IR/발표 | 2026-03 | [B] |
| <a id="ref-e-02"></a>E-02 | DESILO — GL 5세대 FHE (Gentry 공동) | [링크](https://www.prnewswire.com/news-releases/desilo-and-fhe-inventor-craig-gentry-introduce-5th-generation-gl-fhe-scheme-for-private-ai-302707060.html) | 보도자료 | 2026-03-08 | [A] |
| <a id="ref-e-03"></a>E-03 | Cornami×DESILO — FHE LLM 플랫폼 | [링크](https://www.prnewswire.com/news-releases/cornami-and-desilo-bring-encrypted-ai-to-scale-with-deployable-fhe-based-llm-302557181.html) | 보도자료 | 2025-09 | [A] |
| <a id="ref-e-04"></a>E-04 | SEMIFIVE — Niobium ASIC 파트너십 | [링크](https://www.prnewswire.com/news-releases/semifive-partners-with-niobium-to-develop-fhe-accelerator-driving-us-market-expansion-302692312.html) | 보도자료 | 2026-02 | [A] |
| <a id="ref-p-01"></a>P-01 | Aikata et al. — Client-Side FHE 97% (EuroS&P) | [링크](https://eprint.iacr.org/2026/515) | paper | 2026-03 | [A] |
| <a id="ref-p-03"></a>P-03 | HET-PIR — Keyword PIR 3.9ms (Springer) | [링크](https://link.springer.com/article/10.1186/s42400-025-00506-x) | paper | 2026 | [A] |
| <a id="ref-p-04"></a>P-04 | BKPIR — Keyword PIR 10× (NDSS 2026) | [링크](https://www.ndss-symposium.org/ndss-paper/bkpir-keyword-pir-for-private-boolean-retrieval/) | paper | 2026-02 | [A] |
| <a id="ref-p-05"></a>P-05 | Faster Spiral PIR (MDPI) | [링크](https://www.mdpi.com/2410-387X/9/1/13) | paper | 2025-02 | [A] |
