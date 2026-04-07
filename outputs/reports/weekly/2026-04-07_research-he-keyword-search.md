---
type: weekly-deep-research
topic: he-keyword-search
l3_name: "On-Device 동형암호: 키워드 검색"
date: 2026-04-07
week: 2026-W16
parent_domain: secure-ai
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
prior_report: 2026-04-06_research-he-keyword-search.md
---

# 심층 분석: On-Device 동형암호 — 키워드 검색 (2026-W16)

> 기간: 2026-03-31 ~ 2026-04-07

## 이전 대비 변화

- **전주 (W15)**: Niobium "The Fog" 완전 동형암호(Fully Homomorphic Encryption, FHE) 클라우드 플랫폼 프라이빗 베타 공개(4/2), CryptoLab HEaaN Zero-Leak RAG 정부소프트웨어(Government Software, GS) 1등급 획득(3/27), LG U+ ixi-O·인공지능 컨택센터(AI Contact Center, AICC) 동형암호 개념검증(Proof of Concept, PoC) 진행 확인, Intel Heracles 1,074~5,547× 가속 ISSCC 보도 확산
- **금주 (W16)**: CryptoLab 서울경제 인터뷰(4/4)로 Gartner 선정·"2026년 동형암호 상용화 원년" 선언 국내외 확산, HEaaN2 부트스트래핑(bootstrapping) 9.6ms 세계 기록 LinkedIn 발표 [원문 미확인], Hermes FHE-native MySQL 통합 논문 v3 개정판 확인(3/16), Niobium The Fog 독립 기술 분석 기사 등장 — 검증 요구 여론 형성
- **변화 방향**: W15의 플랫폼·인증 발표가 W16에서 **미디어 서사(narrative) 확산 및 기술 검증 논쟁**으로 전환. "2026년 상용화 원년" 프레이밍이 국내외 언론에 확산되는 한편, Niobium 성능 주장에 대한 독립 검증 요구가 제기됨.

---

## 기술 동향

1. **CryptoLab HEaaN2 부트스트래핑 9.6ms 세계 기록 — FHE 핵심 병목 돌파 주장.**
   CryptoLab LinkedIn 채널이 HEaaN2가 부트스트래핑 9.6ms 세계 기록을 달성했다고 발표했다. 부트스트래핑은 FHE에서 누적된 연산 노이즈를 제거해 추가 연산을 가능하게 하는 핵심 절차로, 기존 구현체 대비 속도가 FHE 실용화의 최대 병목이었다. HEaaN2는 Builder 애플리케이션 프로그래밍 인터페이스(Application Programming Interface, API), 유연한 재스케일(flexible rescale), 다항식 평가(polynomial evaluation) 최적화, 배치 연산(batched operations) 기능을 함께 제공한다. 이 발표는 소셜 미디어 채널을 통한 것으로, 공식 기술 논문이나 벤치마크 리포트는 현재까지 공개되지 않았다 [[G-01]](#ref-g-01) [원문 미확인].

2. **Hermes — FHE-native 벡터 쿼리를 MySQL 표준 SQL 엔진 내에서 직접 처리하는 최초 시스템 (논문 v3, 2026-03-16).**
   Dongfang Zhao의 arXiv 논문(2506.03308)이 3월 16일 v3로 개정됐다. Hermes는 관계형 데이터베이스(relational database)와 FHE 암호 연산의 추상화를 통합해 MySQL의 적재 가능 함수(loadable functions)로 구현했다. 핵심 기여는 복수 레코드를 단일 암호문(ciphertext)에 패킹하는 단일 명령 다중 데이터(Single Instruction Multiple Data, SIMD)-aware 데이터 모델, 회전 없는 집계(rotation-free aggregation)를 위한 사전 계산 집계 통계 임베딩, 슬롯 마스킹(slot masking)·시프팅(shifting) 기반 데이터-비노출 알고리즘이다. 성능: 기존 스칼라 FHE 구현 대비 암호화 처리량 3,400× 향상, 튜플 삽입 4,000× 가속, 삭제 300× 가속. 산업용 관계형 데이터베이스 엔진에 FHE를 통합한 최초 실용 사례로 주목된다 [[P-01]](#ref-p-01).

3. **"Privacy at your Fingertips" — 클라이언트 측 FHE 연산 최대 7× 가속, Boosted-Deflation 기법 (eprint 2026/515, 3/13 접수).**
   Aikata Aikata, Florian Krieger, Sujoy Sinha Roy(그라츠 공대(Graz University of Technology))의 논문이 IACR ePrint에 공개됐다. 기존 FHE의 두 가지 실용화 장벽인 클라이언트 측 암복호화 속도와 암호문 팽창(ciphertext expansion) 문제를 Boosted-Deflation 기법으로 해결했다. 핵심은 부트스트래핑을 활용해 인코딩·디코딩 절차를 클라이언트에서 제거함으로써 부동소수점(floating-point) 연산 의존성을 없앤 것이다. 동일 파라미터·플랫폼 환경에서 HEaaN 대비 최대 7× 속도 향상을 달성했다. 온디바이스 FHE 키워드 검색에서 클라이언트 오버헤드를 직접 줄이는 기술로, L3 토픽과 직결된다 [[P-02]](#ref-p-02).

4. **OpenFHE v1.5.0 릴리스(2026-02-26) — FHE 오픈소스 생태계 업데이트.**
   오픈소스 FHE 라이브러리 OpenFHE가 개발 버전 1.5.0을 릴리스했다. CKKS, 바텐버그-제네비에브-비욘드(BGV), 브라케르스키-팬-레인(BFV), 쓰레스홀드 FHE(Threshold FHE, TFHE) 등 주요 스킴을 통합 지원하며, 학술·상업 FHE 구현의 공통 기반으로 활용된다. Hermes가 OpenFHE v1.2.4를 기반으로 구현됐음을 고려하면, 최신 릴리스 채택 시 추가 성능 향상 가능성이 있다 [[G-02]](#ref-g-02).

5. **Niobium The Fog — 독립 기술 분석 기사에서 성능 검증 요구 제기 (4/2 이후).**
   Niobium의 The Fog 발표(4/2) 직후 Zubnet.ai 기술 분석 기사가 "독립 검증 없음, 성능 벤치마크 없음, 사용 중인 암호 기법 세부 정보 없음"이라는 비판을 제기했다. 기사는 FHE 스타트업의 반복되는 과장 주장 패턴을 지적하며, 트랜스포머(Transformer) 추론 지원 여부, 지연 시간 영향, AI 프레임워크 호환성에 대한 답변이 없다고 지적했다. 이는 시장 진입 단계에서 예상되는 기술 신뢰성 검증 수요를 반영한다 [[G-03]](#ref-g-03).

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| CryptoLab (한국) | 서울경제 인터뷰(4/4): "2026년 동형암호 상용화 원년" 선언. Gartner 혁신 기술 선정 국내 최초 동형암호 기업. LG U+ ixi-O·AICC PoC 공식 확인. HEaaN2 부트스트래핑 9.6ms 세계 기록 LinkedIn 발표 [원문 미확인]. enVector 제품으로 음성·이미지·언어 AI 벡터 데이터 암호화 처리. 조달청 혁신 시제품(6월), CC EAL2 인증(9월) 로드맵 | [[G-04]](#ref-g-04), [[E-01]](#ref-e-01), [[E-02]](#ref-e-02) |
| Niobium (미국) | The Fog 프라이빗 베타 지속 운영. Q2 말 공개 출시 목표. mistic Core FPGA(GPU 대비 2×). 독립 기술 분석 기사에서 성능 주장 독립 검증 요구 제기. SEMIFIVE·Samsung Foundry ASIC 개발 진행 중(8nm LPU). CEO Kevin Yoder: "The Fog eliminates that tradeoff." | [[G-03]](#ref-g-03), [[E-03]](#ref-e-03), [[G-05]](#ref-g-05) |
| LG U+ (한국) | CryptoLab과 ixi-O·AICC 동형암호 PoC 진행 확인(3/10 발표). 통화 데이터 암호화 저장·복호화 없는 키워드 검색 구현 목표. LG U+ 최고기술책임자(CTO) 장재현: "LG U+만의 기술 장벽 구축 출발점". 상용화 일정 미확정 | [[E-02]](#ref-e-02), [[G-06]](#ref-g-06) |
| Intel (미국) | Heracles ISSCC 발표(3/10) 보도 지속. 1,074~5,547× Xeon 대비 가속. 양산 일정 미발표. 서버 측 가속기 카드(PCIe) 형태로 온디바이스와 구분 | [[G-07]](#ref-g-07) |
| OpenFHE 컨소시엄 | OpenFHE v1.5.0 릴리스(2026-02-26). CKKS·BGV·BFV·TFHE 통합 지원. 오픈소스 FHE 생태계 기반 라이브러리. Hermes·FHE-SQL 등 연구 시스템이 OpenFHE 기반으로 구현 | [[G-02]](#ref-g-02) |

---

## 시장 시그널

**상용화 서사(narrative) 확산**

- CryptoLab CEO 천정희의 "2026년 동형암호 상용화 원년" 발언이 4월 4일 서울경제 영문판에 보도되면서 국내외 언론으로 확산. Gartner 혁신 기술 선정이 글로벌 신뢰도 지표로 활용됨 [[G-04]](#ref-g-04), [[E-01]](#ref-e-01)
- LG U+ PoC는 아직 상용화 일정 미확정이나, 국내 통신사 최초 FHE 실제 서비스 경로로 지속 언급 [[E-02]](#ref-e-02), [[G-06]](#ref-g-06)
- Niobium The Fog Q2 공개 출시 준비 중이나, 가격 정책·독립 성능 검증 미공개 상태 [[G-03]](#ref-g-03), [[E-03]](#ref-e-03)

**기술 성숙도 시그널**

- Hermes MySQL 통합: FHE가 학술 프로토타입에서 **산업용 데이터베이스 엔진** 수준으로 진입하는 첫 사례. 암호화 상태에서 SQL 질의 처리 가능성 실증 [[P-01]](#ref-p-01)
- eprint 2026/515: 클라이언트 측 FHE 오버헤드 감소는 온디바이스 키워드 검색 실용화의 직접적 선행 조건. 7× 가속이 독립 검증될 경우 온디바이스 배포 임계값 돌파 가능 [[P-02]](#ref-p-02)
- OpenFHE v1.5.0: 오픈소스 FHE 생태계 안정화. 기업 채택 진입 장벽 지속 하락 [[G-02]](#ref-g-02)

**비판 및 리스크**

- Niobium 성능 주장(GPU 대비 2×)에 대한 독립 검증 부재 지적. 구체적 암호 기법·파라미터 미공개 [[G-03]](#ref-g-03) [추가확인 필요]
- CryptoLab HEaaN2 9.6ms 기록 원문(공식 논문·벤치마크) 미공개. LinkedIn 채널 단독 발표 [[G-01]](#ref-g-01) [원문 미확인]

---

## 전략적 시사점

**기회**

- CryptoLab의 "2026년 상용화 원년" 프레이밍과 Gartner 선정이 국내 공공·통신 부문 예산 배정의 정당화 근거로 활용 가능
- Hermes MySQL 통합은 기존 관계형 데이터베이스 기반 엔터프라이즈 고객이 FHE를 전체 시스템 교체 없이 도입할 수 있는 경로를 제시
- eprint 2026/515의 클라이언트 오버헤드 감소 기술은 온디바이스 키워드 검색 제품화를 앞당기는 핵심 기반 기술

**위협**

- Niobium The Fog 성능 주장 독립 검증 지연 시, FHE 플랫폼 전반에 대한 시장 신뢰 훼손 가능
- HEaaN2 9.6ms 기록이 공식 논문으로 재현 불가능할 경우 CryptoLab의 기술 리더십 서사에 타격
- FHE 부트스트래핑 속도 경쟁: Zama의 TFHE GPU 서브밀리초 달성 등 복수 기법이 병렬 경쟁 중으로, CKKS 계열 단독 우위 지속 불확실

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | CryptoLab Inc. LinkedIn — HEaaN2 bootstrap 9.6ms world record announcement | [링크](https://www.linkedin.com/company/cryptolabinc/) | social | 2026-04 | [C] |
| <a id="ref-g-02"></a>G-02 | OpenFHE GitHub — v1.5.0 release (development branch) | [링크](https://github.com/openfheorg/openfhe-development) | software | 2026-02-26 | [A] |
| <a id="ref-g-03"></a>G-03 | Zubnet.ai — "Niobium's Fog Promises Fully Encrypted AI — But Details Are Thin" | [링크](https://zubnet.ai/news/niobiums-fog-promises-fully-encrypted-ai-details-thin/) | blog | 2026-04 | [C] |
| <a id="ref-g-04"></a>G-04 | Seoul Economic Daily (영문) — "Gartner-Recognized Encryption Startup Seeks to Commercialize Korea's Homomorphic Security Tech" | [링크](https://en.sedaily.com/finance/2026/04/04/gartner-recognized-encryption-startup-seeks-to) | news | 2026-04-04 | [B] |
| <a id="ref-g-05"></a>G-05 | PR Newswire — "Niobium Introduces The Fog, a New Encrypted Cloud Platform for Private AI and Data Processing" | [링크](https://prnewswire.com/news-releases/niobium-introduces-the-fog-a-new-encrypted-cloud-platform-for-private-ai-and-data-processing-302732387.html) | press | 2026-04-02 | [A] |
| <a id="ref-g-06"></a>G-06 | EBN 뉴스 — "[Telecom & Now] LGU+, 동형암호 기반 AI 보안 실증" | [링크](https://www.ebn.co.kr/news/articleView.html?idxno=1701823) | news | 2026-03-10 | [B] |
| <a id="ref-g-07"></a>G-07 | Tom's Hardware — "Intel's Heracles chip computes fully-encrypted data without decrypting it — 1,074 to 5,547 times faster than a 24-core Intel Xeon" | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2026-03-10 | [B] |
| <a id="ref-p-01"></a>P-01 | Zhao — "Hermes: Bridging Relational and Algebraic Abstractions in Homomorphically Encrypted Databases" (arXiv 2506.03308 v3) | [링크](https://arxiv.org/abs/2506.03308) | paper | 2026-03-16 | [A] |
| <a id="ref-p-02"></a>P-02 | Aikata et al. — "Privacy at your Fingertips: Enabling Rapid Client-Side Operations in Fully Homomorphic Encryption" (IACR eprint 2026/515) | [링크](https://eprint.iacr.org/2026/515) | paper | 2026-03-13 | [A] |
| <a id="ref-e-01"></a>E-01 | CryptoLab CEO 천정희 — "2026년 동형암호 상용화 원년" (서울경제 인터뷰, 4/4) | [링크](https://en.sedaily.com/finance/2026/04/04/gartner-recognized-encryption-startup-seeks-to) | IR/발표 | 2026-04-04 | [B] |
| <a id="ref-e-02"></a>E-02 | LG U+ CTO 장재현 — "LG U+만의 기술 장벽 구축 출발점" (헤럴드경제 MWC26 인터뷰, 3/10) | [링크](https://biz.heraldcorp.com/article/10688970) | IR/발표 | 2026-03-10 | [B] |
| <a id="ref-e-03"></a>E-03 | Niobium CEO Kevin Yoder — "The Fog eliminates that tradeoff. Our goal is to make encrypted computing practical, scalable and accessible." (PR Newswire, 4/2) | [링크](https://prnewswire.com/news-releases/niobium-introduces-the-fog-a-new-encrypted-cloud-platform-for-private-ai-and-data-processing-302732387.html) | IR/발표 | 2026-04-02 | [A] |
| <a id="ref-e-04"></a>E-04 | CryptoLab CEO 천정희 — "4.5세대 동형암호로 대용량 데이터 밀리초 처리, 실시간 지연 없음" (헤럴드경제 MWC26, 3/10) | [링크](https://biz.heraldcorp.com/article/10688970) | IR/발표 | 2026-03-10 | [B] |
| <a id="ref-e-05"></a>E-05 | SiliconANGLE — "Niobium brings fully encrypted AI workloads to the cloud with The Fog" | [링크](https://siliconangle.com/2026/04/02/niobium-brings-fully-encrypted-ai-workloads-cloud-fog/) | news | 2026-04-02 | [B] |
