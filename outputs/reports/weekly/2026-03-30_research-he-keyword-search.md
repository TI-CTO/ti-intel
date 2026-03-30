---
type: weekly-deep-research
topic: he-keyword-search
date: 2026-03-30
period: 2026-03-23 ~ 2026-03-30
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
parent: 2026-03-30_weekly-secure-ai.md
prior_report: 2026-03-25_research-he-keyword-search.md
---

# Deep 리서치: On-Device 동형암호 (2026-W14)

> 기간: 2026-03-23 ~ 2026-03-30

## 이전 대비 변화

- **전주 (W13)**: Intel Heracles 일반 미디어 확산(Privacy Guides 3/19), UTS FHE 기반 딥강화학습(Deep Reinforcement Learning, DRL) 세계 최초 실증(Nature MI, 3/18), IACR Vaikuntanathan IACR Fellows 선정(3/23), LGU+·CryptoLab ixi-O AICC 동형암호 협력(MWC 2026)
- **금주 (W14)**: Zama + T-REX Network 제도금융 기관급 완전 동형암호(Fully Homomorphic Encryption, FHE) 인프라 출시(3/26), Intel Heracles 기술 사양 상세 확산 지속, CAT GPU-가속 프레임워크 arXiv 공개(3/28), "Privacy at your Fingertips" 클라이언트 측 연산 최적화 논문 발표(EuroS&P 2026)
- **변화 방향**: 하드웨어 단계(ASIC 발표·확산)에서 **생태계 확장** 단계로 이동 중. Zama가 FHE를 $32억 규모 토큰화 자산 인프라에 통합하며 금융 부문 실증을 선도. 클라이언트 측 암호화·복호화 오버헤드 97% 감소 논문은 온디바이스 키워드 검색 실용성을 직접적으로 높이는 성과.

---

## 기술 동향

1. **"Privacy at your Fingertips" — 클라이언트 측 FHE 연산 최적화, enc/dec 오버헤드 97% 감소 (EuroS&P 2026).**
   Aikata, Krieger, Sinha Roy가 제11회 IEEE 유럽 보안·프라이버시 심포지엄(EuroS&P 2026)에 발표한 "Boosted-Deflation" 기법은 FHE 클라이언트 측의 두 가지 핵심 병목—느린 암호화·복호화와 대용량 암호문 팽창(ciphertext expansion)—을 동시에 해결한다. IACR ePrint 2026/515로 3월 15일 공개됐다. 클라이언트가 수행하는 근사 숫자(approximate numbers) FHE의 부동소수점 산술 요구를 제거하고, 부트스트래핑을 활용해 통신 오버헤드를 서버 및 클라이언트 모두에서 줄인다. 소프트웨어·하드웨어 플랫폼 모두 호환되는 구조로 선행 연구 대비 최대 76× 속도 향상을 달성했다. 이 성과는 온디바이스 키워드 검색 시 스마트폰 등 저전력 클라이언트의 실용성을 직접적으로 높인다. [[G-01]](#ref-g-01), [[P-01]](#ref-p-01)

2. **CAT — GPU 가속 FHE 프레임워크, CKKS 기반 프라이빗 데이터셋 쿼리 33× 가속 (arXiv, 3/28).**
   Cipher-Acceleration-Textile(CAT) 프레임워크가 2026년 3월 28일 arXiv(2503.22227)에 공개됐다. 3계층 아키텍처(핵심 수학 연산 → 사전 연산 요소 및 결합 연산 → FHE 연산자 API)를 채택해 CKKS, BFV, BGV 세 가지 주요 FHE 체계를 통합 지원한다. Nvidia RTX 4090에서 CPU 대비 최대 2,173× 가속, 최신 GPU 가속 연구 대비 1.25× 성능을 달성했다. CKKS 기반 프라이빗 데이터베이스 쿼리 시나리오에서 CPU 대비 33× 가속, 단일 GPU로 1초 내에 10³행 데이터셋 쿼리가 가능하다. 키워드 검색용 암호화 쿼리 처리에 직접 적용 가능한 결과다. [[G-02]](#ref-g-02), [[P-02]](#ref-p-02)

3. **Intel Heracles 기술 사양 상세 — ISSCC 데모 성과 지속 확산.**
   3월 23일~30일 기간에도 Intel Heracles 관련 기술 분석이 지속됐다. 핵심 수치: 1.2 GHz, 197mm², 176W TDP, Intel 3 공정, 29.5 TOPS(butterfly), 9.8 TOPS(모듈러 산술), 48GB HBM(819 GB/s 대역폭), 9.6 TB/s 타일 간 인터커넥트. 암호화된 유권자 데이터베이스 익명 쿼리 실증에서 Intel Xeon(15ms) 대비 Heracles(14μs)로 1,071× 가속. 1억 건 투표 검증 기준 23분(vs. 17일). BGV, BFV, CKKS 다중 FHE 스킴 지원 및 파라미터 세트 프로그래밍 가능. 양산 일정은 미발표 상태이나 PCIe 가속기 카드 형태로 서버와 병치 운용. [[G-03]](#ref-g-03), [[G-04]](#ref-g-04), [[E-01]](#ref-e-01)

4. **FHECore — GPU FHE 전용 마이크로아키텍처 커버리지 지속 (BU/Northeastern/KAIST/Murcia).**
   arXiv 2602.22229로 2월 발표된 FHECore 논문이 이번 주도 Semi Engineering 등 기술 미디어에서 지속 인용됐다. 수치 이론 변환(Number Theoretic Transform, NTT)과 기저 변환(Base Conversion)을 동일 wide-precision 모듈 곱산 누산(WMAC) 유닛으로 처리하는 접근이다. CKKS 기본 연산에서 동적 명령어 수 기하평균 2.41× 감소, 엔드투엔드 최대 2.12× 향상, 부트스트래핑 50% 감소, 면적 오버헤드 2.4%. [[G-05]](#ref-g-05), [[P-03]](#ref-p-03)

5. **OpenFHE 1.5.0 개발 버전 출시 (2026-02-26), 오픈소스 생태계 확장.**
   오픈소스 FHE 라이브러리 OpenFHE의 개발 버전 1.5.0이 2월 26일 GitHub에 출시됐다. 현재 안정 버전은 1.4.2(2025-10-20)이며, 1.5.0은 개발 브랜치로 운용 중이다. FIDESlib(Murcia 대학 팀)과의 서버 측 CKKS GPU 가속 상호운용성이 설계된 라이브러리로, 온디바이스 HE 키워드 검색 프로토타입 개발의 기반 플랫폼으로 활용된다. [[G-06]](#ref-g-06)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Intel (미국) | Heracles FHE ASIC, ISSCC 2026 데모 성과 지속 확산. 1,074~5,547× Xeon 대비 가속. 29.5 TOPS butterfly. 양산 일정 미발표. DARPA DRIVE 프로그램 기원 | [[G-03]](#ref-g-03), [[G-04]](#ref-g-04), [[E-01]](#ref-e-01) |
| Zama (프랑스) | T-REX Network와 FHE 기반 기관급 기밀 인프라 출시(3/26). ERC-3643 표준 $32억 토큰화 자산에 FHE 기밀성 레이어 통합. FHE.org 2026 컨퍼런스(3/8 타이페이)에서 8편 기여. Apple·AWS·Google 후원 확보. 유니콘($1B+ 밸류에이션) 지위 유지 | [[G-07]](#ref-g-07), [[G-08]](#ref-g-08), [[E-02]](#ref-e-02) |
| CryptoLab (한국) | LGU+ ixi-O 에이전트·AICC 동형암호 적용 PoC 진행 중(MWC 2026 발표). CKKS 4세대 원천특허 보유. UClone과 Encrypted Vector Search(ES2) RAG 통합. 국내 통신사 대상 암호화 AI 서비스 상용화 선도 | [[G-09]](#ref-g-09), [[E-03]](#ref-e-03) |
| Niobium + SemiFive (미국·한국) | Samsung Foundry 8nm 8LPU 공정 FHE ASIC 개발 진행(2/19 계약 100억 원). 세계 최초 상용 FHE 가속기 목표. 설계 단계 진행 중 | [[G-10]](#ref-g-10) |
| T-REX Network (글로벌) | Zama와 협력해 T-REX Ledger의 기본 기밀성 레이어로 FHE 채택(3/26). Apex Group $3.5조 자산 서비스 기반. 2027년 6월까지 $1,000억 토큰화 자산 목표 | [[G-07]](#ref-g-07), [[E-04]](#ref-e-04) |
| LG유플러스 (한국) | MWC 2026에서 '인간 중심 AI' 비전 발표. CryptoLab과 AI 에이전트 ixi-O 및 AICC에 동형암호 탑재 PoC 추진. 해킹·유출 시에도 개인정보 암호화 유지 목표 | [[G-09]](#ref-g-09), [[E-03]](#ref-e-03) |
| Boston Univ./KAIST 등 공동팀 | FHECore(arXiv 2602.22229) 이번 주도 기술 미디어 인용 지속. GPU SM에 FHE 전용 연산 유닛 통합 제안 | [[G-05]](#ref-g-05), [[P-03]](#ref-p-03) |

---

## 시장 시그널

**파트너십 & 제휴**

- Zama + T-REX Network: FHE를 T-REX Ledger 기본 기밀성 레이어로 통합(3/26). 실물 자산(Real World Asset, RWA) 토큰화 기관 인프라에 FHE가 최초 실사용 규모로 진입 [[G-07]](#ref-g-07), [[E-04]](#ref-e-04)
- LGU+ + CryptoLab: AICC·ixi-O AI 에이전트 동형암호 탑재 개념 증명(Proof of Concept, PoC) 진행 중. 국내 통신사 최초 암호화 AI 고객센터 상용화 경로 확보 [[G-09]](#ref-g-09), [[E-03]](#ref-e-03)
- CryptoLab + Niobium: CryptoLab-Niobium 파트너십(선행 발표). CryptoLab HEaaN 라이브러리와 Niobium ASIC 간 소프트웨어·하드웨어 통합 스택 구성 목표 [[G-10]](#ref-g-10)

**연구 동향**

- EuroS&P 2026: "Privacy at your Fingertips" — 클라이언트 측 FHE enc/dec 오버헤드 97% 감소. 온디바이스 키워드 검색의 실용성 임계점에 근접 [[P-01]](#ref-p-01)
- arXiv 2503.22227 (3/28): CAT GPU 가속 FHE 프레임워크. CKKS 프라이빗 DB 쿼리 CPU 대비 33×. 1초 내 10³행 쿼리 가능 [[P-02]](#ref-p-02)
- FHE.org 2026(타이페이, 3/8): 10편 구두 발표·23편 포스터. Apple·AWS·Google 후원. TFHE 부트스트래핑 GPU 가속, 암호화 해시 함수, 행렬 곱 SNARG 등 발표 [[G-08]](#ref-g-08)

**시장 전망**

- FHE 스타트업 8개사 누적 투자금 $2억 7,890만(평균 사당 $3,490만). 데이터 기준 2026-03-24 [[G-11]](#ref-g-11) [추가확인 필요]
- Zama 유니콘 달성($1B+ 밸류에이션), 총 투자 $1.5억+ (Series A+B 합산). FHE 단일 기업 최고 밸류에이션 [[G-12]](#ref-g-12)

**도입 사례**

- T-REX Ledger: $32억 ERC-3643 토큰화 자산에 Zama FHE 기밀성 레이어 통합(3/26 공식 발표). FHE 사상 최초 기관 금융 인프라 수준 실도입 [[G-07]](#ref-g-07), [[E-04]](#ref-e-04)
- LGU+ AICC: 고객 개인정보·상담 이력 암호화 상태 비교·분석. PoC 진행 중 (상용화 시점 미발표) [[G-09]](#ref-g-09)

**커뮤니티 시그널**

- Slashdot "Intel Demos Chip To Compute With Encrypted Data" 게시(3/10)에 수백 건 댓글. 주류 기술 커뮤니티로 FHE 인지도 확산. 기술 실현 가능성 회의론과 기대감 혼재 [C-01] [추가확인 필요]
- FHE.org Digest #38(3/8): Apple·AWS·Google 후원으로 FHE 커뮤니티에서 "빅테크 진입" 신호로 해석. 생태계 자금 유입 기대감 고조 [[G-08]](#ref-g-08)

---

## 전략적 시사점

**기회**

- **온디바이스 키워드 검색 실용화 임계점 접근**: "Privacy at your Fingertips" 논문의 클라이언트 측 enc/dec 97% 감소는 스마트폰급 기기에서 FHE 기반 키워드 검색이 가능해지는 전환점. 향후 12~18개월 내 상용 데모 가능성 높음
- **통신사 AICC 암호화 차별화**: LGU+·CryptoLab 협력이 성공할 경우, KT/SKT도 동형암호 기반 AICC를 고객 프라이버시 차별화 포인트로 도입할 압박을 받을 가능성
- **FHE 하드웨어 가속기 공급망**: Niobium(Samsung 8nm) + Intel(Intel 3 공정) 두 축이 병행 진행 중. 국내 팹리스 기업 협력 기회 존재(SemiFive 설계 승리 사례 참고)
- **금융·공공 암호화 DB 쿼리**: T-REX RWA 인프라 사례가 금융·공공 부문의 레퍼런스로 확산될 경우, 암호화 키워드 검색 솔루션에 대한 B2B 수요 증가 예상

**위협**

- **Intel Heracles 양산 일정 불확실성**: ISSCC 데모 수준에서 PCIe 카드 양산까지 일정이 미공개 상태. 하드웨어 가속 없이는 소프트웨어 FHE 키워드 검색의 지연(latency) 문제가 지속됨
- **글로벌 빅테크 생태계 선점 리스크**: Apple·AWS·Google이 FHE.org 2026 후원에 진입. 자체 클라우드 인프라와 통합된 FHE 키워드 검색 서비스 출시 시 국내 솔루션 시장 잠식 가능
- **소비자급 엣지 기기 호환성 제약**: CUDA 벤치마크 결과(MDPI), Jetson Nano 등 저전력 임베디드 GPU는 FHE 연산에 부적합 판정. 온디바이스 적용 범위가 스마트폰 상위 티어 이상으로 제한될 가능성

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | IACR ePrint 2026/515 — Privacy at your Fingertips (발표 소식) | [링크](https://iacr.org/news/item/27993) | news | 2026-03-15 | [A] |
| <a id="ref-g-02"></a>G-02 | arXiv 2503.22227 — CAT GPU-Accelerated FHE Framework | [링크](https://arxiv.org/abs/2503.22227) | paper | 2026-03-28 | [A] |
| <a id="ref-g-03"></a>G-03 | Tom's Hardware — Intel Heracles 1,074~5,547× Xeon 가속 | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2026-03-19 | [B] |
| <a id="ref-g-04"></a>G-04 | IEEE Spectrum — Intel Heracles Chip Speeds Up FHE Computing | [링크](https://spectrum.ieee.org/fhe-intel) | news | 2026-03-10 | [B] |
| <a id="ref-g-05"></a>G-05 | Semi Engineering — A GPU Microarchitecture Optimized for FHE | [링크](https://semiengineering.com/a-gpu-microarchitecture-optimized-for-fully-homomorphic-encryption/) | news | 2026-03 | [B] |
| <a id="ref-g-06"></a>G-06 | GitHub — openfheorg/openfhe-development v1.5.0 (2026-02-26) | [링크](https://github.com/openfheorg/openfhe-development) | blog | 2026-02-26 | [B] |
| <a id="ref-g-07"></a>G-07 | Benzinga — T-REX Network and Zama Launch Institutional-Grade Confidentiality Infrastructure | [링크](https://www.benzinga.com/pressreleases/26/03/51479524/t-rex-network-and-zama-launch-institutional-grade-confidentiality-infrastructure-for-rwa-tokenizati) | news | 2026-03-26 | [B] |
| <a id="ref-g-08"></a>G-08 | FHE.org Digest #38 — 2026 Conference, Apple/AWS/Google 후원 | [링크](https://fheorg.substack.com/p/fheorg-digest-38-fheorg-2026-conference) | news | 2026-03 | [B] |
| <a id="ref-g-09"></a>G-09 | The Asia Business Daily — LG Uplus and Cryptolab MWC26 발표 | [링크](https://www.asiae.co.kr/en/article/2026031008212144575) | news | 2026-03-10 | [B] |
| <a id="ref-g-10"></a>G-10 | evertiq — SemiFive secures design win with Niobium for FHE accelerator | [링크](https://evertiq.com/design/2026-02-20-semifive-secures-design-win-with-niobium-for-fhe-accelerator) | news | 2026-02-20 | [B] |
| <a id="ref-g-11"></a>G-11 | SeedTable — 8 Best Homomorphic Encryption Startups (2026-03-24 기준) | [링크](https://www.seedtable.com/best-homomorphic-encryption-startups) | blog | 2026-03-24 | [C] |
| <a id="ref-g-12"></a>G-12 | MEXC Blog — What Is Zama FHE? The $1B Unicorn | [링크](https://blog.mexc.com/news/what-is-zama-fhe-the-1b-unicorn-bringing-private-smart-contracts-to-ethereum-and-shibarium-2026/) | blog | 2026 | [C] |
| <a id="ref-g-13"></a>G-13 | Privacy Guides — Intel's FHE Chip Could Revolutionize Privacy | [링크](https://www.privacyguides.org/news/2026/03/19/intels-fully-homomorphic-encryption-chip-could-revolutionize-privacy/) | news | 2026-03-19 | [B] |
| <a id="ref-g-14"></a>G-14 | Decrypt — T-REX Network and Zama Launch Institutional-Grade Confidentiality | [링크](https://decrypt.co/362436/t-rex-network-and-zama-launch-institutional-grade-confidentiality-infrastructure-for-rwa-tokenization) | news | 2026-03-26 | [B] |
| <a id="ref-g-15"></a>G-15 | FHE.org 2026 Conference Program (Taipei, 3/8) | [링크](https://fhe.org/conferences/conference-2026/program.html) | blog | 2026-03-08 | [A] |
| <a id="ref-p-01"></a>P-01 | Aikata, Krieger, Sinha Roy — Privacy at your Fingertips: Enabling Rapid Client-Side Operations in FHE (EuroS&P 2026) | [링크](https://eprint.iacr.org/2026/515) | paper | 2026-03-15 | [A] |
| <a id="ref-p-02"></a>P-02 | CAT: A GPU-Accelerated FHE Framework with Its Application to High-Precision Private Dataset Query (arXiv 2503.22227) | [링크](https://arxiv.org/abs/2503.22227) | paper | 2026-03-28 | [A] |
| <a id="ref-p-03"></a>P-03 | FHECore: Rethinking GPU Microarchitecture for Fully Homomorphic Encryption (arXiv 2602.22229) | [링크](https://arxiv.org/abs/2602.22229) | paper | 2026-02 | [A] |
| <a id="ref-e-01"></a>E-01 | Intel — Heracles ISSCC 2026 데모: 암호화 유권자 DB 쿼리 14μs (Xeon 15ms 대비) | [링크](https://spectrum.ieee.org/fhe-intel) | IR/발표 | 2026-03-10 | [A] |
| <a id="ref-e-02"></a>E-02 | Zama — Zama Becomes the Confidentiality Layer for the T-REX Ledger (공식 블로그) | [링크](https://www.zama.org/post/zama-becomes-the-confidentiality-layer-for-the-t-rex-ledger) | IR/발표 | 2026-03-26 | [A] |
| <a id="ref-e-03"></a>E-03 | Korea IT Times — LG Uplus 'Human-Centered AI' Vision at MWC 2026 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151339) | IR/발표 | 2026-03-10 | [B] |
| <a id="ref-e-04"></a>E-04 | Zama — More than 30% of $ZAMA staked, FHE.org receiving support from Apple, AWS, Google | [링크](https://www.zama.org/post/more-than-30-of-zama-circulating-supply-staked-the-zama-portfol--fhe-org-receiving-support-from-apple-aws-google-and-more) | IR/발표 | 2026-03 | [A] |
| <a id="ref-c-01"></a>C-01 | Slashdot — Intel Demos Chip To Compute With Encrypted Data (커뮤니티 반응) | [링크](https://it.slashdot.org/story/26/03/10/2022201/intel-demos-chip-to-compute-with-encrypted-data) | blog | 2026-03-10 | [C] |
