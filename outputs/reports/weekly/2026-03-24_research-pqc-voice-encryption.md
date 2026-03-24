---
type: research-deep
topic: pqc-voice-encryption
date: 2026-03-24
parent: 2026-03-24_weekly-secure-ai.md
---

# Deep 리서치: On-Device 양자암호(PQC) — 2026-W13

## 이전 대비 변화

- **전주**: Akamai TLS 전면 PQC 완료, Samsung Exynos 2600 HW-PQC 양산, QCi+Ciena 1.6Tb/s PQC+QKD OFC 시연, FIPS 140-2 종료 카운트다운
- **금주**: 중국 PQC 독자 표준 3년 내 확정 선언(3/19), 트럼프 행정부 사이버 전략(3/6) PQC 명시, SEALSQ 블록체인 PQC 배포(3/20), CISA PQC 제품 카테고리 리스트 발표, HNDL 위협 대응 긴급성 고조
- **변화 방향**: 미·중 양대 축에서 PQC 표준화·제도화가 동시 가속. 규제(FIPS 140-2 종료, CISA 리스트, 트럼프 전략)가 산업 전반의 마이그레이션 압박을 본격화

## 기술 동향

1. **중국, PQC 독자 표준 3년 내 확정 선언 (3/19).**
   중국 15차 5개년 계획에서 양자기술을 핵심 전략 산업으로 격상. 칭화대 왕샤오윈 교수(전인대 대표)가 "3~5년 내 PQC 산업 마이그레이션 폭발적 성장" 전망. NIST와 달리 "비구조 격자(structureless lattice)" 알고리즘(S-Cloud+) 중심으로 차별화. 금융·에너지 부문 우선 적용. NIST 표준과의 상호운용성 문제가 글로벌 분열 위험 요소. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02)

2. **트럼프 행정부 '사이버 전략 for America' — PQC 명시 (3/6).**
   6대 핵심 기둥에 PQC를 포함: (1) 연방 네트워크 현대화에서 "PQC, 제로 트러스트, 클라우드 전환" 명시, (2) 핵심·신기술 부문에서 양자내성 암호화 지원 약속. 미국 연방 기관의 PQC 마이그레이션에 공식 정책 근거 부여. [[G-03]](#ref-g-03), [[G-04]](#ref-g-04)

3. **CISA PQC 제품 카테고리 리스트 발표 (1/23).**
   EO 14306에 따라 PQC 기술 적용 제품군을 두 단계로 분류: "Widely Available"(클라우드, 웹 브라우저, 엔드포인트 보안 — 이미 상용 PQC 제품 존재)과 "Transitioning"(네트워킹 HW/SW, 통신 장비, IAM, 컨테이너 — PQC 성숙 중). FIPS 203/204/205 구현 필수. 연방 조달의 PQC 우선 구매 기준. [[G-05]](#ref-g-05), [[G-06]](#ref-g-06)

4. **SEALSQ, 블록체인·IoT 인프라에 PQC 배포 (3/20).**
   CRYSTALS-Kyber(KEM) + CRYSTALS-Dilithium(서명)을 시큐어 엘리먼트·TPM 칩에 내장. WeCan(스위스 블록체인 금융) 협력으로 MPC+ZKP+HW 기반 ID 검증 통합. 위성 IoT 인프라에도 적용 확대. [[G-07]](#ref-g-07)

5. **HNDL 위협 경고 강화 — "양자 위협은 이미 활성 상태" (3/23).**
   Help Net Security: 적대국이 현재 암호화 데이터를 수집 중이며, PQC 대응 속도가 조직 간 극심한 격차. Crypto-agility(NIST CSWP 39, 2025-12 확정)가 필수 역량으로 부상. 공급망 파트너의 암호화 취약점까지 점검 범위 확대 필요. [[G-08]](#ref-g-08), [[G-09]](#ref-g-09)

6. **FIPS 140-2 종료 카운트다운 — D-181 (2026-09-21).**
   NIST CMVP가 잔존 FIPS 140-2 인증 모듈을 Historical로 이전. 이후 신규 조달은 FIPS 140-3만 허용. 완전 CMVP PQC 인증 모듈이 희소하여 규제 산업 조달 마찰 예상. [[G-10]](#ref-g-10)

7. **MWC 2026 PQC Readiness 세미나 (3/3) — NIST·3GPP·IETF·ETSI 참여.**
   모바일 산업 PQC 준비 상태 점검. 3GPP PQC 도입 연구 착수 확인, VoLTE/VoNR PQC는 2027년 이후 현실적. [[G-11]](#ref-g-11)

## 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| 중국 정부 | 15차 5개년 계획에서 양자기술 핵심 전략 산업 격상. PQC 독자 표준 3년 내 확정. 비구조 격자 알고리즘 중심 | [[G-01]](#ref-g-01) |
| 미국 백악관 | 사이버 전략 for America(3/6)에서 PQC 명시. 연방 네트워크 현대화 6대 기둥 포함 | [[G-03]](#ref-g-03) |
| CISA | PQC 제품 카테고리 리스트(1/23). Widely Available vs Transitioning 2단계 분류 | [[G-05]](#ref-g-05) |
| SEALSQ | 블록체인·IoT PQC 배포(3/20). CRYSTALS-Kyber/Dilithium TPM 내장 | [[G-07]](#ref-g-07) |
| NIST | FIPS 140-2 종료 D-181. HQC 초안 표준 2026년 예정. CSWP 39 확정(2025-12) | [[G-10]](#ref-g-10) |

## 시장 시그널

**시장 전망**
- PQC 시장 2025년 $10억 → 2035년 $450억(CAGR 43%) — OpenPR 추정 [[G-12]](#ref-g-12)
- "PQC 마이그레이션은 1조 달러 규모 과제" — GlobeNewswire [[G-13]](#ref-g-13)

**도입 사례**
- SEALSQ: CRYSTALS-Kyber/Dilithium을 시큐어 엘리먼트·TPM에 내장, 블록체인 금융에 적용 (3/20) [[G-07]](#ref-g-07)
- CISA PQC 제품 카테고리: 연방 조달에서 PQC 우선 구매 기준 제도화 [[G-05]](#ref-g-05)

**연구 동향**
- MWC 2026 PQC Readiness Seminar (3/3): NIST·3GPP·IETF·ETSI 참여, 모바일 PQC 준비 상태 점검 [[G-11]](#ref-g-11)

## 시장 수요 (voice-of-market)

이번 주 해당 기술 관련 컨퍼런스 영상에서 수요 시그널을 확인하지 못함.

## 전략적 시사점

**기회**
- 미·중 동시 PQC 표준화 가속은 글로벌 마이그레이션 수요 폭발의 전조 — 한국 통신사의 PQC 서비스 차별화 시간 창(window) 축소
- CISA "Transitioning" 카테고리에 통신 장비 포함 — 통신사 장비 공급사(Ericsson, Nokia, Samsung Networks)의 PQC 대응이 가속될 것
- 트럼프 사이버 전략의 PQC 명시는 연방 고객 대상 PQC 서비스의 시장 확대 신호

**위협**
- 중국 비구조 격자 표준이 NIST 표준과 비호환 시, 글로벌 통신 인프라의 이중 표준 부담 발생
- FIPS 140-3 완전 PQC 인증 모듈 희소 → 규제 산업 조달 마찰 지속
- 3GPP PQC 표준화 지연(2027+)으로 VoLTE/VoNR 실시간 PQC는 at-rest 암호화에 우선 집중 필요

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | The Quantum Insider — China PQC Standards Within Three Years | [링크](https://thequantuminsider.com/2026/03/19/china-expects-post-quantum-cryptography-standards-within-three-years/) | news | 2026-03-19 | [B] |
| <a id="ref-g-02"></a>G-02 | QuantumZeitgeist — China Forecasts National PQC Standards | [링크](https://quantumzeitgeist.com/post-quantum-cryptography-china-forecasts/) | news | 2026-03-19 | [B] |
| <a id="ref-g-03"></a>G-03 | White House — President Trump's Cyber Strategy for America | [링크](https://www.whitehouse.gov/wp-content/uploads/2026/03/president-trumps-cyber-strategy-for-america.pdf) | 공식 | 2026-03-06 | [A] |
| <a id="ref-g-04"></a>G-04 | Sidley Data Matters — New Cyber Doctrine of the United States | [링크](https://datamatters.sidley.com/2026/03/10/the-new-cyber-doctrine-of-the-united-states/) | news | 2026-03-10 | [B] |
| <a id="ref-g-05"></a>G-05 | CISA — PQC Product Categories List | [링크](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards) | 공식 | 2026-01-23 | [A] |
| <a id="ref-g-06"></a>G-06 | Industrial Cyber — CISA PQC Categories Guide Adoption | [링크](https://industrialcyber.co/cisa/cisa-publishes-initial-list-of-hardware-and-software-categories-supporting-post-quantum-cryptography-to-guide-adoption/) | news | 2026-01 | [B] |
| <a id="ref-g-07"></a>G-07 | GlobeNewswire — SEALSQ PQC Blockchain Deployment | [링크](https://www.globenewswire.com/news-release/2026/03/20/3259796/0/en/SEALSQ-Deploys-Post-Quantum-Cryptography-to-Secure-Blockchain-and-Digital-Transaction-Infrastructures-Through-the-Deployment-of-Post-Quantum-Cryptographic-PQC-Technologies.html) | 보도자료 | 2026-03-20 | [A] |
| <a id="ref-g-08"></a>G-08 | Help Net Security — Quantum Threats Active, Defense Fragmented | [링크](https://www.helpnetsecurity.com/2026/03/23/ciso-post-quantum-crypto-agility/) | news | 2026-03-23 | [B] |
| <a id="ref-g-09"></a>G-09 | Federal News Network — Cryptographic Drift and PQC | [링크](https://federalnewsnetwork.com/commentary/2026/03/the-business-impact-of-cryptographic-drift-the-urgent-case-for-post-quantum-cryptography/) | news | 2026-03 | [B] |
| <a id="ref-g-10"></a>G-10 | SafeLogic — FIPS 140-2 September 21, 2026 | [링크](https://www.safelogic.com/blog/what-happens-on-september-21-2026) | blog | 2026 | [B] |
| <a id="ref-g-11"></a>G-11 | MWC Barcelona — PQC Readiness Standardisation and Migration | [링크](https://www.mwcbarcelona.com/agenda/sessions/5976-post-quantum-cryptography-readiness-standardisation-and-migration) | 공식 | 2026-03-03 | [A] |
| <a id="ref-g-12"></a>G-12 | OpenPR — PQC Market Surge Toward Multi-Billion by 2035 | [링크](https://www.openpr.com/news/4433132/post-quantum-cryptography-market-poised-to-redefine-global) | report | 2026-03 | [C] |
| <a id="ref-g-13"></a>G-13 | GlobeNewswire — PQC Migration Trillion-Dollar Imperative | [링크](https://www.globenewswire.com/news-release/2026/02/19/3241234/0/en/Post-Quantum-Cryptography-Migration-Is-Now-a-Trillion-Dollar-Imperative.html) | news | 2026-02-19 | [B] |
