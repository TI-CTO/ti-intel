---
type: weekly-deep-research
topic: pqc-voice-encryption
l3_name: "On-Device PQC (양자내성암호)"
date: 2026-04-07
week: 2026-W16
parent_domain: secure-ai
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
prev_report: outputs/reports/weekly/2026-04-06_research-pqc-voice-encryption.md
---

# 심층 분석: On-Device PQC (양자내성암호) (2026-W16)

> 기간: 2026-03-31 ~ 2026-04-07
> 이전 대비: W15에서 Google ECDLP-256 자원 추정치 20배↓(<50만 큐비트), Oratomic 10K 중성원자 qLDPC, Cisco IOS XE 26 전체 스택 Quantum-Resistant Cryptography (PQC) 발표, 캐나다 연방 PQC 의무화 4/1 마감, Naoris Module-Lattice-based Digital Signature Algorithm (ML-DSA) 메인넷, ARM Cortex-M0+ ML-KEM 35.7ms 벤치마크 이후 금주 추가 발전 추적

---

## 이전 대비 변화

- **전주 (W15)**: Google Quantum AI가 ECDLP-256 해독에 <50만 물리 큐비트면 충분하다고 발표(3/31), Oratomic이 10,000 중성원자 큐비트 qLDPC 아키텍처 공개, 캐나다 PQC 이행계획 제출 마감(4/1), Cisco IOS XE 26 전체 스택 PQC 발표, Naoris ML-DSA 메인넷 출시
- **금주 (W16)**: Scott Aaronson(UT Austin)이 두 논문을 종합하며 "Caltech 그룹 추정치 기준 25,000 물리 큐비트면 ECC-256 공격 가능"이라는 하한 추정치를 제시(4/1); Nature가 "양자컴퓨팅 돌파구가 사이버보안에 임박한 위협"이라고 보도(4/6); CoinDesk가 Bitcoin $1.3조 양자보안 경쟁 종합 분석(4/4); 브루스 슈나이어(Bruce Schneier)가 Google의 2029 PQC 전환 계획에 "크립토 어질리티 관점에서 타당"이라고 평가(4/6); Warsaw 대학 연구팀이 Talbot effect 기반 고차원 QKD(Quantum Key Distribution) 신기술 발표(4/1)
- **변화 방향**: 위협 추정치 하한이 W15의 "50만 큐비트" 에서 W16에 "25,000 큐비트(ECC-256)"로 재조정되며 학술 커뮤니티 긴장 최고조. 동시에 Nature·슈나이어 등 주류 매체·전문가가 위협을 공식 확인함으로써 "이론→운영 위협" 전환이 가속화됨

---

## 기술 동향

1. **Aaronson 종합 분석 — 두 논문 합산 시 ECC-256 공격 하한 "25,000 물리 큐비트" 도출.**
   Scott Aaronson(UT Austin, 양자컴퓨팅 이론 권위자)이 2026-04-01 블로그 "Quantum computing bombshells that are not April Fools"에서 Caltech/Oratomic 논문(qLDPC 고율 코드)과 Google 논문(Shor 알고리즘 최적화)을 교차 적용한 결과를 공개했다. Aaronson은 "Caltech 그룹 추정치 기준, ECC-256 공격에 단 25,000 물리 큐비트만으로 충분하다. 1년 전 최고 추정치는 수백만 큐비트였다"고 밝혔다. 두 논문의 상승 효과에 대해 그는 "이 두 결과를 합산할 때, 비트코인 서명은 기존에 알려진 것보다 훨씬 일찍 양자 공격에 취약하다"고 직접 발언했다. 다만 그는 "이는 이론적 하한이며 실제 CRQC(Cryptographically Relevant Quantum Computer) 구현에는 여전히 수년이 필요하다"고 맥락을 덧붙였다. [[G-01]](#ref-g-01)

2. **Nature 뉴스 — "양자컴퓨팅 돌파구, 사이버보안에 임박한 위협"(4/6) 주류 과학매체 합류.**
   Nature가 4월 6일 "It's a real shock: quantum-computing breakthroughs pose imminent risks to cybersecurity"를 게재하며 Google·Caltech 논문의 파급력을 주류 학술 커뮤니케이션으로 확산시켰다. 기사는 CRQC 필요 자원 추정치가 3개월 내 3편 논문으로 연속 급감한 사실을 "실제 충격(real shock)"으로 표현하고, 조속한 PQC 전환을 촉구했다. [[G-02]](#ref-g-02)

3. **슈나이어 분석(4/6) — Google 2029 PQC 전환 계획, "크립토-어질리티 관점에서 타당".**
   보안 전문가 Bruce Schneier가 2026-04-06 블로그에서 Google의 2029 PQC 전환 계획을 평가했다. 그는 "2029년 이전에 실용적 양자컴퓨터가 등장한다고 보지 않지만, 크립토-어질리티는 항상 좋은 것(crypto-agility is always a good thing)"이라며 지지 의사를 표명했다. 이 발언은 PQC 도입의 정당성을 위협 확실성보다 아키텍처 유연성에서 찾는 전문가적 관점을 대표한다. [[G-03]](#ref-g-03)

4. **Bitcoin $1.3조 양자보안 경쟁 종합 분석(CoinDesk, 4/4) — 현황 및 주요 이니셔티브.**
   CoinDesk가 4월 4일 Bitcoin 양자보안 경쟁을 심층 분석했다. 핵심 수치: 약 650만 BTC(수천억 달러 상당)가 공개키가 온체인 노출된 주소에 저장되어 있어 CRQC 직접 공격 대상이 된다. 제안된 방어 수단: (a) BIP-360(P2MR, 공개키 노출 제거), (b) SLH-DSA(SPHINCS+, FIPS 205 해시 기반 서명), (c) commit/reveal 스킴(멤풀 트랜잭션 보호). SLH-DSA 서명 크기는 현행 64바이트 대비 최소 8KB로 블록 공간 압박이 우려 사항으로 지적됐다. [[G-04]](#ref-g-04)

5. **Warsaw 대학 Talbot effect QKD — 단일 검출기로 고차원 QKD 구현(4/1).**
   폴란드 바르샤바 대학 물리학부 Michał Karpiński 팀이 1836년 광학 현상인 Talbot effect를 활용한 고차원 양자키 분배(QKD) 시스템을 발표했다. 기존 단일 광자 2상태 대비 다중 상태 전송으로 데이터 용량을 획기적으로 확대하고, 검출기를 1개로 줄여 비용·복잡성을 낮췄다. 도시 광섬유망 수km 거리에서 실증됐다. Optica Quantum 등 3개 저널 동시 게재. [[P-01]](#ref-p-01)

6. **NIST HQC 초안 2026년 초 예정 — ML-KEM 백업 다양성 확보 진행 중.**
   NIST가 2025년 3월 선정한 HQC 알고리즘의 초안 표준이 2026년 초 공개 의견 수렴 후 2027년 최종 확정 예정이다. HQC는 코드 기반(code-based) 수학으로 ML-KEM(격자 기반)과 상이한 수학적 기반을 제공하여, ML-KEM 취약점 발견 시 백업 역할을 한다. [[G-05]](#ref-g-05), [[E-01]](#ref-e-01)

---

## 플레이어 동향

**주요 플레이어**

| 기업/기관 | 동향 | 출처 |
|-----------|------|------|
| Scott Aaronson (UT Austin) | 2026-04-01: 블로그에서 Google+Caltech 논문 교차 적용 — ECC-256 공격 하한 25,000 물리 큐비트 도출. "비트코인 서명이 기존보다 훨씬 일찍 취약해 보인다" 직접 발언 | [[G-01]](#ref-g-01) |
| Nature | 2026-04-06: "It's a real shock" 기사 — CRQC 위협 주류 학술 커뮤니케이션으로 확산. 주류 과학저널 최초 종합 경보 | [[G-02]](#ref-g-02) |
| Bruce Schneier | 2026-04-06: Google 2029 PQC 전환 계획 "크립토-어질리티 관점에서 타당" 평가. 위협 확실성보다 아키텍처 유연성 강조 | [[G-03]](#ref-g-03) |
| CoinDesk | 2026-04-04: Bitcoin $1.3조 양자보안 종합 분석 — 650만 BTC 공개키 노출, BIP-360/SLH-DSA/commit-reveal 3개 방어 방안 정리 | [[G-04]](#ref-g-04) |
| University of Warsaw | 2026-04-01: Talbot effect 기반 고차원 QKD 발표. 단일 검출기·다중 상태·도시 광섬유망 실증. Optica Quantum 외 2개 저널 게재 | [[P-01]](#ref-p-01) |
| NIST | 2026년 초: HQC 초안 표준 공개 예정(선정 2025-03). 2027 최종 확정 목표. ML-KEM 백업 다양성 확보 | [[G-05]](#ref-g-05), [[E-01]](#ref-e-01) |
| Cisco (전주 연속) | 4/1 Cisco Live Amsterdam IOS XE 26 전체 스택 PQC 발표 후속 — 기업 고객 배포 문의 급증 보도. "업계 최초 전체 스택 PQC" 포지셔닝 유지 | [[G-06]](#ref-g-06) |
| SK Telecom | 기존 Thales와 5G PQC 협력 지속(Crystals-Kyber SIM 카드). W16 기간 신규 발표 없음 — 공개 정보 없음 | [[G-07]](#ref-g-07) |

---

## 시장 시그널

**학술·전문가 반응**

- Scott Aaronson(UT Austin): "25,000 큐비트 ECC-256 공격 하한" 발언 — 학술 권위자의 공식 종합이 미디어 레버리지로 작동 [[G-01]](#ref-g-01)
- Bruce Schneier: 크립토-어질리티 관점에서 PQC 전환 지지 — 위협 타임라인 불확실성에도 불구하고 조기 전환 정당성 확인 [[G-03]](#ref-g-03)
- Nature 게재: 주류 과학계가 CRQC 위협을 "임박한 위험(imminent risks)"으로 공식 분류 시작 [[G-02]](#ref-g-02)

**규제·정책**

- YQS2026 (Year of Quantum Security 2026): FBI·CISA·NIST 공동 출범(1월 개막, 연중 글로벌 서밋 진행 중). "양자 위협이 이론에서 운영 단계로 격상됐다"고 공식 선언 [[G-08]](#ref-g-08)
- 캐나다 CCCS ITSM.40.001: 4/1 마감 연방 PQC 이행계획 제출 완료 — 2031 고우선순위·2035 전면 완료 법적 의무 진행 중 [[E-02]](#ref-e-02)
- NIST IR 8547 초안: RSA/ECDSA 2030 deprecated·2035 disallowed 기준 재확인 중

**도입·시장**

- PQC 시장: Juniper Research 전망 2026년 $12억 → 2035년 $130억 (CAGR 30%) — W15 대비 변동 없음 [[G-09]](#ref-g-09)
- 상위 40% 웹사이트 이미 하이브리드 PQ 키 교환 지원 — PQC 인프라 확산 지표 [[G-06]](#ref-g-06)
- Bitcoin SLH-DSA 도입 시 서명 크기 64B → 8KB(125배↑) 블록 공간 압박 — 통신 시스템 PQC 패킷 오버헤드 문제와 구조적으로 동일한 과제 [[G-04]](#ref-g-04)

**연구 동향**

- Warsaw 대학 Talbot QKD: 고차원 단일 검출기 QKD로 비용·복잡성 하향 — 엣지 디바이스 QKD 실용화 경로 제시 [[P-01]](#ref-p-01)
- arXiv 2603.19340(P-01, 전주): ARM Cortex-M0+ ML-KEM-512 35.7ms·2.83mJ — IoT 보이스 단말 PQC 실용성 정량 근거 (전주 발표, 이번 주 인용 증가) [[P-02]](#ref-p-02)

---

## 전략적 시사점

**위협**

- Aaronson의 "25,000 큐비트 ECC-256 공격 하한" 발언은 CRQC 구현 자원 하한이 급격히 낮아지고 있음을 학술 권위자가 공식 확인한 것이다. "Harvest Now, Decrypt Later (HNDL)" 전략 하에 현재 수집 중인 VoLTE(Voice over Long-Term Evolution)/VoNR(Voice over New Radio) 트래픽이 향후 CRQC 등장 시 복호화될 실제 위험이 구체화되고 있다. 위협 시기가 이전 추정 대비 앞당겨질 가능성에 대비한 조기 대응이 필요하다
- Nature의 "real shock" 보도는 주류 과학계가 양자 위협을 임박한 위험으로 재분류했음을 의미한다. 이는 향후 국제 표준화 기구·규제 기관이 PQC 전환 일정을 앞당기는 압력으로 작용할 수 있다
- Bitcoin SLH-DSA 도입 시 서명 크기 125배 증가(64B → 8KB) 문제는 통신 시스템 SIP 신호 및 미디어 보안 레이어에서도 동일하게 발생한다. PQC 알고리즘 선택 시 패킷 오버헤드가 실시간 음성 품질에 미치는 영향을 사전 정량화해야 한다

**기회**

- Schneier의 "크립토-어질리티 지지" 발언은 위협 타임라인 불확실성에도 불구하고 PQC 조기 도입의 산업 합의가 형성됨을 시사한다. 통신사 보이스 암호화 인프라에 하이브리드 PQC(Classical + PQC) 아키텍처를 선제 도입하여 조달 기준 선점 가능
- Warsaw 대학의 Talbot effect QKD는 단일 검출기로 고차원 인코딩을 구현하여 엣지 단말 QKD 비용 장벽을 낮추는 방향을 제시했다. QKD와 PQC 하이브리드 아키텍처를 온디바이스 통화 암호화에 통합하는 장기 기술 로드맵 수립에 참고 가능
- YQS2026 정책 환경(FBI·CISA·NIST 공동)과 캐나다 의무화 프레임이 확산되는 가운데, 국내 과학기술정보통신부 및 KISA의 PQC 의무화 일정 조기화 가능성을 모니터링할 필요가 있다

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Scott Aaronson — Quantum computing bombshells that are not April Fools | [링크](https://scottaaronson.blog/?p=9665) | blog | 2026-04-01 | [A] |
| <a id="ref-g-02"></a>G-02 | Nature — It's a real shock: quantum-computing breakthroughs pose imminent risks to cybersecurity | [링크](https://www.nature.com/articles/d41586-026-01054-1) | news | 2026-04-06 | [A] |
| <a id="ref-g-03"></a>G-03 | Schneier on Security — Google Wants to Transition to Post-Quantum Cryptography by 2029 | [링크](https://www.schneier.com/blog/archives/2026/04/google-wants-to-transition-to-post-quantum-cryptography-by-2029.html) | blog | 2026-04-06 | [A] |
| <a id="ref-g-04"></a>G-04 | CoinDesk — Bitcoin's $1.3 trillion security race: Key initiatives aimed at quantum-proofing the world's largest blockchain | [링크](https://www.coindesk.com/tech/2026/04/04/bitcoin-s-usd1-3-trillion-security-race-key-initiatives-aimed-at-quantum-proofing-the-worlds-largest-blockchain) | news | 2026-04-04 | [B] |
| <a id="ref-g-05"></a>G-05 | NIST — NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption | [링크](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption) | news | 2025-03-11 | [A] |
| <a id="ref-g-06"></a>G-06 | Security Boulevard — Post-Quantum Cryptography: Moving From Awareness to Execution | [링크](https://securityboulevard.com/2026/04/post-quantum-cryptography-moving-from-awareness-to-execution/) | news | 2026-04-01 | [B] |
| <a id="ref-g-07"></a>G-07 | SK Telecom Newsroom — SK Telecom and Thales Collaborate on Post-Quantum Cryptography (5G PQC SIM) | [링크](https://news.sktelecom.com/en/628) | news | 2023-02 | [B] |
| <a id="ref-g-08"></a>G-08 | The Quantum Insider — U.S. Federal Agencies Are Stepping Up for the Quantum Security Transition (YQS2026) | [링크](https://thequantuminsider.com/2026/01/14/u-s-federal-agencies-are-stepping-up-for-the-quantum-security-transition/) | news | 2026-01-14 | [B] |
| <a id="ref-g-09"></a>G-09 | Juniper Research — Post-quantum Cryptography Market to Exceed $13 Billion by 2035 | [링크](https://www.juniperresearch.com/press/post-quantum-cryptography-market-to-exceed-13-billion-by-2035-as-q-day-awareness-accelerates/) | news | 2026 | [B] |
| <a id="ref-g-10"></a>G-10 | The Quantum Insider — Q-Day Just Got Closer: Three Papers in Three Months (CRQC 자원 추정치 비교) | [링크](https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/) | news | 2026-03-31 | [B] |
| <a id="ref-g-11"></a>G-11 | CoinDesk — Naoris Protocol's quantum-resistance blockchain goes live as Bitcoin and Ethereum face Q-Day threats | [링크](https://www.coindesk.com/markets/2026/04/03/naoris-protocol-s-quantum-resistance-blockchain-goes-live-as-bitcoin-and-ethereum-face-q-day-threats) | news | 2026-04-03 | [B] |
| <a id="ref-g-12"></a>G-12 | Quantum Computing Report — The Decryption Threshold: Re-estimating the Quantum Threat to Blockchain Infrastructure | [링크](https://quantumcomputingreport.com/the-decryption-threshold-re-estimating-the-quantum-threat-to-blockchain-infrastructure/) | news | 2026-03-31 | [B] |
| <a id="ref-g-13"></a>G-13 | Quantum Pirates (Substack) — RSA will die. Oratomic and Caltech, Google and Harvard, Quix — W16 주간 요약 | [링크](https://quantumpirates.substack.com/p/rsa-will-die-oratomic-and-caltech) | blog | 2026-04-06 | [B] |
| <a id="ref-p-01"></a>P-01 | Karpiński et al. (University of Warsaw) — Talbot effect-based high-dimensional QKD (Optica Quantum 외) | [링크](https://www.sciencedaily.com/releases/2026/04/260401071933.htm) | paper | 2026-04-01 | [A] |
| <a id="ref-p-02"></a>P-02 | Janssen et al. — Benchmarking NIST-Standardised ML-KEM and ML-DSA on ARM Cortex-M0+ (arXiv:2603.19340) | [링크](https://arxiv.org/abs/2603.19340) | paper | 2026-03-30 | [A] |
| <a id="ref-e-01"></a>E-01 | NIST CSRC — Post-Quantum Cryptography Standardization (HQC 선정 및 초안 일정) | [링크](https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization) | IR/발표 | 2025-03-11 | [A] |
| <a id="ref-e-02"></a>E-02 | Canadian Centre for Cyber Security — ITSM.40.001 Roadmap for Migration to Post-Quantum Cryptography | [링크](https://www.cyber.gc.ca/en/guidance/roadmap-migration-post-quantum-cryptography-government-canada-itsm40001) | IR/발표 | 2026-04-01 | [A] |
| <a id="ref-e-03"></a>E-03 | Google Research Blog — Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly | [링크](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) | IR/발표 | 2026-03-31 | [A] |
