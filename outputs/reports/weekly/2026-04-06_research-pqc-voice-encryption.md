---
type: weekly-deep-research
topic: pqc-voice-encryption
date: 2026-04-06
agent: research-deep
confidence: high
status: completed
sources_used: [websearch, webfetch]
parent: 2026-04-06_weekly-secure-ai.md
prev_report: outputs/reports/weekly/2026-03-30_research-pqc-voice-encryption.md
---

# Deep Research: On-Device PQC (양자내성암호) (2026-W15)

> 기간: 2026-03-30 ~ 2026-04-06
> 이전 대비: W14에서 Google 2029 Post-Quantum Cryptography (PQC) 데드라인 선언(3/25), Android 17 Module-Lattice-Based Digital Signature Algorithm (ML-DSA) 4계층 통합(3/26), IBM+Signal+Threema ML-DSA 대역폭 100배 증가 정량화, PQShield 5KB RAM 임베디드 PQC, QuSecure SEC PQFIF 금융 레퍼런스, CISA 협업도구 즉시 PQC 의무 분류 이후 금주 주요 변화 추적

---

## 이전 대비 변화

- **전주 (W14, 2026-03-30)**: Google 2029 PQC 마이그레이션 데드라인 선언(3/25), Android 17 ML-DSA 4계층 통합 발표(3/26), IBM·Signal·Threema 양자안전 그룹 메시징 대역폭 100배 문제 정량화, PQShield PQMicroLib-Core 5KB RAM 임베디드 PQC 출시, QuSecure SEC PQFIF 금융권 공식 레퍼런스 인용, CISA 협업도구 즉시 PQC 의무 분류 공식화
- **금주 (W15, 2026-04-06)**: Google Quantum AI가 Cryptographically Relevant Quantum Computer (CRQC) 구축에 필요한 물리 큐비트를 20배 줄인 Elliptic Curve Discrete Logarithm Problem (ECDLP)-256 논문 공개(3/31, <50만 큐비트); Oratomic이 Caltech 협력으로 10,000 중성원자 큐비트로 Shor's 알고리즘 실행 가능함을 제시(3/31); 캐나다 연방정부 PQC 이행계획 제출 마감(4/1)·2031 고우선순위·2035 완료 체계 확정; Naoris Protocol ML-DSA 기반 양자내성 블록체인 메인넷 출시(4/1); Cisco가 IOS XE 26에 전체 스택 PQC 아키텍처 발표(4/1); Quantum XChange Phio TX 2026 사이버보안 우수상 금상 수상(3/26)
- **변화 방향**: 위협 측에서 CRQC 도달 필요 자원 추정치가 연이어 하향 조정되며(9M → 1M → 100K → 10K~500K 큐비트 수준으로 수렴) 업계 긴장감이 최고조. 방어 측에서는 네트워크 장비(Cisco IOS XE 26), 암호화폐(Naoris Protocol), 정부(캐나다 연방)가 동시에 구체적인 PQC 구현·마감을 공식화하며 "선언"에서 "실행" 국면으로 전환이 가속화

---

## 기술 동향

1. **Google·Oratomic 동시 발표 — ECDLP 공격 자원 추정치 20배 하락, Shor's 알고리즘 10,000 큐비트 실현 가능성 제시.**
   Google Quantum AI는 2026-03-31 "Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities: Resource Estimates and Mitigations" 논문(arXiv:2603.28846)을 공개했다. 세팅별 2개 회로: (a) 1,200 논리 큐비트·9,000만 Toffoli 게이트, (b) 1,450 논리 큐비트·7,000만 Toffoli 게이트. 표면 코드 기반 초전도체 아키텍처(물리적 에러율 10⁻³)에서 **<50만 물리 큐비트**로 secp256k1 ECDLP-256 해독 가능하며, 공개키 노출 후 약 9분 내 개인키 복원이 가능하다는 것이 핵심 주장이다. 이는 Litinski 2023 추정치 ~900만 큐비트 대비 약 20배 감소다. 동일 시점(3/31), Oratomic(Caltech 협력)이 10,000 중성원자 큐비트로 Shor's 알고리즘을 구동할 수 있는 고율 양자 Low-Density Parity-Check (qLDPC) 코드 아키텍처를 발표했다. PQShield는 두 논문을 "물리 큐비트 → 논리 큐비트 → 암호 알고리즘 → 실세계 공격의 4단계 중 서로 다른 계층을 각각 해결하는 상호보완 연구"로 평가했다. [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-03]](#ref-g-03), [[E-01]](#ref-e-01)

2. **캐나다 연방정부 PQC 이행계획 제출 마감(4/1) — 2031 고우선순위·2035 전면 완료 법적 의무화.**
   캐나다 사이버보안센터(CCCS) ITSM.40.001 문서에 따라 4/1 마감으로 연방 각 부처·기관이 초기 PQC 이행계획을 제출해야 했다. 계획서 의무 포함 항목: 전 IT 인프라(네트워크·운영체제·애플리케이션·클라우드·물리 자산) 암호화 현황 인벤토리, 역할·예산·인력 교육 계획, 조달 정책 개정. 4/1 이후 체결하는 디지털 요소 포함 계약에는 PQC 조달 조항이 의무화됐다. 2031년까지 고우선순위 시스템 이행 완료, 2035년까지 전체 시스템 완료가 법적 마감이다. 미국 NSA·영국 NCSC와 Five Eyes 협력 틀 안에서 조율된 일정이다. [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)

3. **NIST IR 8547(초안) — RSA/ECDSA 2030 deprecated, 2035 disallowed 기준 재확인.**
   NIST IR 8547은 2024-11-12 초기 공개 초안(Initial Public Draft)으로 배포됐으며 2025-01-10 의견 수렴이 마감된 후 아직 최종본이 발행되지 않은 상태다. 핵심 타임라인: 112비트 이하 보안강도 레거시 알고리즘(RSA-2048, ECC P-256 포함)은 **2030년 후 신규 시스템 사용 deprecated**, **2035년 후 전면 disallowed**. FIPS 203(ML-KEM), FIPS 204(ML-DSA), FIPS 205(Stateless Hash-Based Digital Signature Algorithm, SLH-DSA)를 핵심 대체 표준으로 지정하며 "지금 즉시 도입해야 한다"고 권고하고 있다. [[G-06]](#ref-g-06)

4. **Cisco IOS XE 26 전체 스택 PQC 아키텍처 — 네트워크 장비 계층의 NIST 표준 통합.**
   Cisco는 2026-04-01 Amsterdam Cisco Live에서 IOS XE 26을 발표했다. "업계 최초 전체 스택 PQC 아키텍처"로 소개된 이 프레임워크는 부팅 보안(Cisco C9000 Smart Switch Secure Boot), 이미지 무결성, 네트워크 트래픽(IPsec 터널·MACsec), 관리 세션의 4개 계층을 모두 NIST 승인 알고리즘으로 보호한다. 구체적 알고리즘명은 공식 블로그에 명시되지 않았으나 ML-KEM·ML-DSA 기반임을 시사했다. 엔터프라이즈 AI 인프라 보호를 위한 장기 암호화 통신 보안이 주요 적용 시나리오다. [[G-07]](#ref-g-07), [[E-02]](#ref-e-02)

5. **Naoris Protocol ML-DSA 메인넷 출시(4/1) — 최초 NIST 승인 PQC 기반 레이어1 블록체인.**
   Naoris Protocol이 2026-04-01 양자내성 레이어1 블록체인 메인넷을 출시했다. FIPS 204(ML-DSA) 알고리즘을 모든 트랜잭션 서명에 사용하며, 테스트 기간 중 1억 600만 건 트랜잭션 처리·6억 300만 건 보안 위협 차단을 검증했다. 출시 당시 $NAORIS 토큰 시가총액은 3,600만 달러. 한번 양자내성 키를 채택한 사용자는 이후 전통 암호화 서명으로 되돌아갈 수 없도록 프로토콜 수준에서 차단된다. [[G-08]](#ref-g-08)

6. **arXiv:2603.19340 — ARM Cortex-M0+ 기반 ML-KEM·ML-DSA 최초 체계적 벤치마크, IoT PQC 실용성 입증.**
   "Benchmarking NIST-Standardised ML-KEM and ML-DSA on ARM Cortex-M0+" 논문(2026-03-19 제출, 3/30 최종 버전)은 가장 제약된 32비트 임베디드 프로세서 클래스인 ARM Cortex-M0+에서 FIPS 203·204 표준의 첫 체계적 벤치마크를 제시했다. 핵심 결과: ML-KEM-512 완전 키 교환 35.7ms·2.83mJ(ECDH P-256 동일 하드웨어 대비 17배 빠름). 반면 ML-DSA 서명은 rejection sampling으로 인한 고분산(변동계수 66~73%, 99퍼센타일 최대 1,125ms)이 관측됐다 — 실시간 보이스 암호화 프로토콜 설계에서 ML-DSA 서명 지연 버스트를 고려해야 함을 시사한다. [[P-01]](#ref-p-01)

7. **Quantum XChange Phio TX, 2026 사이버보안 우수상 PQC 부문 금상 수상(3/26).**
   Quantum XChange의 Phio TX 플랫폼이 2026 Cybersecurity Excellence Awards PQC 카테고리 금상을 수상했다. 평가 근거는 기존 인프라 교체 없이 오버레이 방식으로 PQC를 도입하는 크립토-어질리티(Crypto-agility) 아키텍처—암호키 전달 경로와 데이터 전송 경로를 분리해 키 탈취 위험을 줄이고, 신규 PQC 알고리즘을 운용 중단 없이 교체 가능하게 한다. 같은 기간 Globee Award for Cybersecurity 혁신 네트워크 보안 솔루션 최고 등급도 획득했다. [[G-09]](#ref-g-09)

8. **BIP-360 비트코인 테스트넷 최초 구현(3/20) — P2MR(Pay-to-Merkle-Root) 운용 검증.**
   BTQ Technologies가 Bitcoin Quantum Testnet v0.3.0에 BIP-360 첫 실구현을 배포했다(2026-03-20). Pay-to-Taproot (P2TR)의 내부 공개키 노출 취약점을 제거한 P2MR 합의, SegWit 버전2 출력, 5개 Dilithium 서명 opcode 활성화. 마이너 50+명·블록 100,000개 이상·기여자 100+명 규모로 운용 중이다. BIP-360 공동 저자는 "비트코인이 완전한 양자내성 전환에 7년이 걸릴 수 있다"고 경고했다. [[G-10]](#ref-g-10), [[G-11]](#ref-g-11)

---

## 플레이어 동향

**주요 플레이어**

| 기업 | 동향 | 출처 |
|------|------|------|
| Google Quantum AI | 2026-03-31: ECDLP-256 논문 공개 — <50만 물리 큐비트·~9분 ECDSA-256 해독 주장. Google Blog "Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly" 게재. 자체 2029 PQC 마감 재확인. Ethereum Foundation·Stanford 공동 저자 | [[G-01]](#ref-g-01), [[E-01]](#ref-e-01) |
| Oratomic (Caltech 협력) | 2026-03-31: 중성원자 기반 10,000 큐비트로 Shor's 알고리즘 실행 가능한 qLDPC 코드 아키텍처 발표. 창업팀: Dolev Bluvstein(CEO)·John Preskill·Manuel Endres(Caltech·Berkeley·Harvard·Google·Amazon 출신). 2020년대 말 실용 규모 양자컴퓨터 구축 목표 | [[G-02]](#ref-g-02), [[G-03]](#ref-g-03) |
| Cisco | 2026-04-01(Cisco Live Amsterdam): IOS XE 26 전체 스택 PQC 아키텍처 발표. C9000 Smart Switch Secure Boot·IPsec·MACsec 전 계층 NIST 승인 알고리즘 적용. "업계 최초 전체 스택 PQC" 포지셔닝 | [[G-07]](#ref-g-07), [[E-02]](#ref-e-02) |
| Naoris Protocol | 2026-04-01: ML-DSA(FIPS 204) 기반 레이어1 블록체인 메인넷 출시. 테스트 1억600만 트랜잭션·6억300만 위협 차단 검증. NIST 승인 PQC만을 사용하는 최초 퍼블릭 블록체인 주장. 초대 전용 단계로 시작 | [[G-08]](#ref-g-08) |
| Quantum XChange | 2026-03-26: 2026 Cybersecurity Excellence Awards PQC 부문 금상·Globee Award 혁신 네트워크 보안 최고 등급 수상. Phio TX 크립토-어질리티 플랫폼: 키 전달·데이터 전송 경로 분리, 오버레이 방식 PQC 전환 | [[G-09]](#ref-g-09) |
| BTQ Technologies | 2026-03-20: BIP-360 Bitcoin Quantum Testnet v0.3.0 출시. P2MR 합의·Dilithium 서명 opcode 구현. 마이너 50+·블록 100K+ 운용. BIP-360 공동 저자 "7년 전환 소요" 경고 | [[G-10]](#ref-g-10), [[G-11]](#ref-g-11) |
| PQShield | W14(3/10) 출시 PQMicroLib-Core 이어 이번 주 Google·Oratomic 논문 공식 분석 리포트 발표. "4단계 PQC 공격 프레임워크" 제시 — 두 논문이 상호보완적으로 CRQC 구현 경로를 완성시킨다고 평가 | [[E-03]](#ref-e-03) |
| 캐나다 연방정부(CCCS) | 2026-04-01: 연방 부처 PQC 이행계획 제출 마감. 2031 고우선순위 완료·2035 전면 완료 법적 의무화. 4/1 이후 계약 전체에 PQC 조달 조항 의무화. Five Eyes 파트너(미 NSA·영 NCSC)와 조율된 일정 | [[G-04]](#ref-g-04), [[G-05]](#ref-g-05) |

---

## 시장 시그널

**투자 & M&A**

- Oratomic, Caltech 협력 논문 발표 직후 스텔스 상태에서 공식 런칭 — 구체적 투자 규모 미공개 [원문 미확인] [[G-02]](#ref-g-02)
- Juniper Research: 글로벌 PQC 시장 2026년 $12억 → 2035년 $130억(CAGR 30%) 전망 [[G-12]](#ref-g-12)
- 양자내성 토큰(Naoris Protocol 등) Google 논문 발표 직후 일부 50%+ 급등 [[G-13]](#ref-g-13)

**파트너십 & 제휴**

- Google Quantum AI + Ethereum Foundation + Stanford 대학: ECDLP-256 논문 공동 저술 — 빅테크·학계·암호화폐 생태계 3자 협력으로 위협 연구 이해관계 공유 [[G-01]](#ref-g-01)
- PQShield + 산업계: Google·Oratomic 논문 공식 분석 리포트 신속 발표 — PQC 솔루션 공급사의 위협 연구 대응 속도 가속 [[E-03]](#ref-e-03)
- BTQ Technologies + 오픈소스 커뮤니티: BIP-360 테스트넷에 100+명 기여자 합류 [[G-10]](#ref-g-10)

**시장 전망**

- PQC 시장: 2026년 $12억 → 2035년 $130억(Juniper Research, CAGR 30%) [[G-12]](#ref-g-12)
- 2026 Entrust/Ponemon 조사: 조직의 40%가 PQC 전환 진행 중이라고 응답, 그러나 실제 배포 완료 비율은 5%(DigiCert 2025 조사 기준) — 계획-실행 격차가 35%p [[G-14]](#ref-g-14) [추가확인 필요]
- 2026년은 퓨어 PQC보다 Classical+PQC 하이브리드 접근이 지배. 상위 40% 웹사이트가 이미 하이브리드 PQ 키 교환을 지원 [[G-14]](#ref-g-14)
- CRQC 조기 출현 시나리오 강화: 자원 추정치가 3개월 내 3편 논문으로 연속 하향(2025-05: RSA-2048 <100만 큐비트 → 2026-02: <10만 큐비트 → 2026-03: ECDLP <50만 큐비트·10K 중성원자) [[G-15]](#ref-g-15)

**도입 사례**

- Cisco IOS XE 26: C9000·8000·8100 플랫폼 전 계층 PQC 적용 — 엔터프라이즈 스위칭 인프라의 첫 전체 스택 PQC 상용화 [[G-07]](#ref-g-07)
- 캐나다 연방정부: 4/1부로 신규 계약 전체에 PQC 조달 조항 의무화 — 정부 조달 시장 PQC 요건 진입 [[G-04]](#ref-g-04)
- Naoris Protocol: ML-DSA 단독 트랜잭션 서명으로 레거시 알고리즘 일체 배제 — 블록체인 부문 강제 PQC 전환 첫 사례 [[G-08]](#ref-g-08)

**연구 동향**

- arXiv 2603.19340: ARM Cortex-M0+에서 ML-KEM-512 키 교환 35.7ms·2.83mJ (ECDH P-256 대비 17배 빠름), ML-DSA 99퍼센타일 서명 지연 1,125ms — IoT·보이스단말 PQC 설계에 직접 적용 가능한 정량 데이터 [[P-01]](#ref-p-01)
- PQShield 분석: Google·Oratomic 논문이 CRQC 구현 4단계(물리 큐비트 → 논리 큐비트 → 암호알고리즘 → 실세계 공격)를 각각 "2단계"와 "3단계"에서 동시 진전시킨 것으로 평가 [[E-03]](#ref-e-03)
- Bitcoin BIP-360 공동 저자: 비트코인 완전 양자내성 전환에 7년 소요 경고 — 2026년 시작 기준 2033년까지 마감, NIST 2030 데드라인과 충돌 [[G-11]](#ref-g-11)

**커뮤니티 시그널**

- Ethereum 연구자 Justin Drake(논문 공동 저자): "양자컴퓨팅과 암호학에서 기념비적인 날"이라고 X에 코멘트 [[G-13]](#ref-g-13)
- Binance 창립자 CZ: "패닉할 필요는 없으나 마이그레이션 도전은 실재한다"며 진정 요청 [[G-13]](#ref-g-13)
- Starknet 창립자 Eli Ben-Sasson: 비트코인 커뮤니티에 BIP-360 가속화 촉구 [[G-13]](#ref-g-13)
- Adam Back: 2026-04-05 X에서 "기존 Taproot 방어가 충분하다"며 단계적 양자 업그레이드 주장 [[G-16]](#ref-g-16)

---

## 전략적 시사점

**기회**

- Cisco IOS XE 26의 전체 스택 PQC 아키텍처 상용화는 통신사의 코어 네트워크 인프라 조달 기준이 PQC 지원으로 이동했음을 의미한다. 국내 통신사 스위칭·라우팅 장비 교체 로드맵에서 PQC 지원 여부를 핵심 조달 기준으로 반영할 시점
- arXiv 2603.19340 벤치마크 결과(ML-KEM-512 35.7ms, 2.83mJ)는 온디바이스 보이스 단말의 키 교환이 기술적으로 실용 수준임을 정량적으로 확인시켜 준다. 보이스 암호화 프로토콜 설계 시 ML-KEM 키 교환 성능 데이터를 직접 참조 가능
- 캐나다 연방정부 4/1 마감·미국 NIST 2030 데드라인이 동시에 구체화됨으로써 정부 조달 시장에서 PQC 솔루션 수요가 빠르게 법적 의무 수요로 전환. 국내 공공기관 대상 PQC 솔루션·컨설팅 시장 선점 기회

**위협**

- Google·Oratomic 논문의 CRQC 필요 자원 추정치 연속 하향 조정은 "Store-Now-Decrypt-Later (SNDL)"이 현재 기록되고 있는 트래픽에도 이미 적용되고 있음을 의미한다. 현재 국내 통신 네트워크에서 VoLTE (Voice over Long-Term Evolution)/VoNR (Voice over New Radio) 트래픽을 ECDSA/ECDH 기반으로 보호하는 경우, 오늘 캡처된 트래픽이 CRQC 등장 이후 복호화될 위험이 실재
- ML-DSA 서명의 99퍼센타일 지연이 최대 1,125ms로 측정됨 — 실시간 보이스 통화 연결 수립(SIP INVITE/200 OK) 과정에서 서명 검증 지연이 체감 품질을 저하시킬 수 있다. 하이브리드 방식에서도 PQC 서명 지연이 Classical 방식 대비 가장 큰 성능 병목
- 비트코인 BIP-360 공동 저자의 "7년 전환" 경고는 암호화폐 생태계에 국한되지 않는다. 분산 합의 구조를 갖지 않는 통신 시스템도 레거시 알고리즘 교체에 수년이 소요되는 공급망 복잡성을 공유하며, 2026년 시작 기준 NIST 2030 데드라인 달성이 빠듯하다는 점은 통신사에도 동일하게 적용

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Google Research Blog — Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly | [링크](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) | news | 2026-03-31 | [A] |
| <a id="ref-g-02"></a>G-02 | The Quantum Insider — Oratomic Launches to Build Utility-Scale Quantum Computers | [링크](https://thequantuminsider.com/2026/03/31/oratomic-launches-to-build-utility-scale-quantum-computers/) | news | 2026-03-31 | [B] |
| <a id="ref-g-03"></a>G-03 | Quantum Computing Report — The Decryption Threshold: Re-estimating the Quantum Threat | [링크](https://quantumcomputingreport.com/the-decryption-threshold-re-estimating-the-quantum-threat-to-blockchain-infrastructure/) | news | 2026-03-31 | [B] |
| <a id="ref-g-04"></a>G-04 | PQShield — Canada publishes new PQC migration roadmap | [링크](https://pqshield.com/canada-publishes-new-pqc-migration-roadmap/) | news | 2026-04-01 | [B] |
| <a id="ref-g-05"></a>G-05 | Quantum Computing Report — EU and Canada Detail Roadmaps for PQC Transition | [링크](https://quantumcomputingreport.com/european-union-and-government-of-canada-detail-roadmaps-for-post-quantum-cryptography-transition/) | news | 2026-04-01 | [B] |
| <a id="ref-g-06"></a>G-06 | NIST CSRC — IR 8547 Transition to Post-Quantum Cryptography Standards (IPD) | [링크](https://csrc.nist.gov/pubs/ir/8547/ipd) | news | 2024-11-12 | [A] |
| <a id="ref-g-07"></a>G-07 | Security Boulevard — Post-Quantum Cryptography: Moving From Awareness to Execution (Cisco IOS XE 26) | [링크](https://securityboulevard.com/2026/04/post-quantum-cryptography-moving-from-awareness-to-execution/) | news | 2026-04-01 | [B] |
| <a id="ref-g-08"></a>G-08 | The Quantum Insider — Naoris Protocol Launches Mainnet, Introducing Post-Quantum Layer 1 Blockchain | [링크](https://thequantuminsider.com/2026/04/01/naoris-protocol-launches-mainnet-introducing-post-quantum-layer-1-blockchain/) | news | 2026-04-01 | [B] |
| <a id="ref-g-09"></a>G-09 | National Law Review — Quantum XChange Wins Gold for PQC in 2026 Cybersecurity Excellence Awards | [링크](https://natlawreview.com/press-releases/quantum-xchange-wins-gold-post-quantum-cryptography-2026-cybersecurity) | news | 2026-03-26 | [B] |
| <a id="ref-g-10"></a>G-10 | The Quantum Insider — BTQ Technologies Implements BIP-360 Quantum-Resistant Bitcoin Transactions on Testnet | [링크](https://thequantuminsider.com/2026/03/20/btq-technologies-implements-bip-360-quantum-resistant-bitcoin-transactions-testnet/) | news | 2026-03-20 | [B] |
| <a id="ref-g-11"></a>G-11 | CoinTelegraph — Bitcoin may take 7 years to upgrade to post-quantum: BIP-360 co-author | [링크](https://cointelegraph.com/magazine/bitcoin-7-years-upgrade-post-quantum-bip-360-co-author/) | news | 2026-04-01 | [B] |
| <a id="ref-g-12"></a>G-12 | Juniper Research — Post-quantum Cryptography Market to Exceed $13 Billion by 2035 | [링크](https://www.juniperresearch.com/press/post-quantum-cryptography-market-to-exceed-13-billion-by-2035-as-q-day-awareness-accelerates/) | news | 2026 | [B] |
| <a id="ref-g-13"></a>G-13 | CoinDesk — 'Bitcoin cracked in 9 minutes': BTC bulls scramble for post-quantum protection | [링크](https://www.coindesk.com/tech/2026/03/31/bitcoin-bulls-scramble-for-post-quantum-protection-as-google-drops-bombshell-paper) | news | 2026-03-31 | [B] |
| <a id="ref-g-14"></a>G-14 | Security Boulevard — PQC: Moving From Awareness to Execution (enterprise adoption stats) | [링크](https://securityboulevard.com/2026/04/post-quantum-cryptography-moving-from-awareness-to-execution/) | news | 2026-04-01 | [B] |
| <a id="ref-g-15"></a>G-15 | The Quantum Insider — Q-Day Just Got Closer: Three Papers in Three Months | [링크](https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/) | news | 2026-03-31 | [B] |
| <a id="ref-g-16"></a>G-16 | Coin Alert News — Adam Back Advocates Phased Quantum Upgrade for Bitcoin | [링크](https://coinalertnews.com/news/2026/04/05/adam-back-bitcoin-quantum-upgrade-plan) | news | 2026-04-05 | [C] |
| <a id="ref-p-01"></a>P-01 | Janssen et al. — Benchmarking NIST-Standardised ML-KEM and ML-DSA on ARM Cortex-M0+ (arXiv:2603.19340) | [링크](https://arxiv.org/abs/2603.19340) | paper | 2026-03-30 | [A] |
| <a id="ref-e-01"></a>E-01 | Google Quantum AI — Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities (arXiv:2603.28846 백서) | [링크](https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf) | IR/발표 | 2026-03-31 | [A] |
| <a id="ref-e-02"></a>E-02 | Cisco Blogs — Why full-stack post-quantum cryptography cannot wait (Han Lee, Cisco Live EMEA) | [링크](https://blogs.cisco.com/networking/why-full-stack-post-quantum-cryptography-cannot-wait) | IR/발표 | 2026-04-01 | [A] |
| <a id="ref-e-03"></a>E-03 | PQShield — Improved Quantum Attacks on Elliptic Curves: Is the PQC Transition Moving Fast Enough? | [링크](https://pqshield.com/improved-quantum-attacks-on-elliptic-curves-is-the-pqc-transition-moving-fast-enough/) | IR/발표 | 2026-04-01 | [A] |
| <a id="ref-e-04"></a>E-04 | Canadian Centre for Cyber Security — ITSM.40.001 Roadmap for Migration to PQC (공식 문서) | [링크](https://www.cyber.gc.ca/en/guidance/roadmap-migration-post-quantum-cryptography-government-canada-itsm40001) | IR/발표 | 2026-04-01 | [A] |
| <a id="ref-e-05"></a>E-05 | Oratomic — Launch Announcement: Utility-Scale Quantum Computers (공식 보도자료) | [링크](https://www.oratomic.com/news/launch-announcement) | IR/발표 | 2026-03-31 | [A] |
