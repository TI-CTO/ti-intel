---
topic: quantum-crypto / pqc-migration
date: 2026-04-07
agent: voice-of-market
videos_analyzed: 3
hn_threads_analyzed: 2
---

## 시장 수요 시그널: 양자내성암호(PQC) 마이그레이션

### 고객 페인포인트

- **레거시 시스템의 하드코딩된 암호화 알고리즘** — 실제 은행(ABN Amro) 마이그레이션 프로젝트에서 RSA가 코드 전반에 하드코딩되어 있어 64개 파일을 수동으로 변경해야 했다. "It mostly boils down to two things: do not hardcode your cryptography or your cryptographic keys in the code." 출처: Migrating and Benchmarking a Banking Application (Alessandro Amadori, TNO / PKI Consortium PQC Conference Austin 2025)

- **암호화 라이브러리 문서화 부족** — BouncyCastle 등 Java 암호화 라이브러리에서 PQC 알고리즘 호출용 cipher string 이 문서에 명확히 기재되지 않아 개발자가 직접 탐색해야 한다. 출처: Migrating and Benchmarking a Banking Application (Alessandro Amadori, TNO)

- **큰 서명 크기로 인한 네트워크 오버헤드** — PQC 서명은 수 KB에 달해 쿠키 크기 제한(4096바이트)과 충돌하며, 매 API 요청마다 다중 패킷을 점유한다. 상태 비저장(stateless) 토큰 기반 아키텍처와 호환되지 않는다. 출처: Google's threat model for PQC (HN 쓰레드, 커뮤니티)

- **알고리즘별 성능 트레이드오프 불투명** — SLH-DSA는 보수적이지만 느리고 서명 크기가 크며(≥7.8KB), Dilithium은 빠르지만 구현 난도가 높다. FALCON은 부동소수점 연산 의존으로 하드웨어 제약이 있다. 실무 팀이 알고리즘 선택 기준을 정하기 어렵다. 출처: What Is Post-Quantum Cryptography (HN 쓰레드, user: less_less)

- **마이그레이션 타임라인 불확실성** — 양자 컴퓨터 등장 시점을 예측할 수 없어 투자 우선순위 결정이 어렵다. "We don't yet know when a cryptographically significant quantum computer will be developed." 출처: NIST Post-Quantum Cryptography Update (Bill Newhouse & Andrew Regenscheid, NIST / PKI Consortium Austin 2025)

### 도입 장벽

- **Crypto Agility(암호 민첩성) 아키텍처 부재** — 대부분 기업 시스템이 특정 알고리즘에 단단히 결합되어 있어(tight coupling), 교체 시 대규모 코드 수정이 필요하다. "Crypto agility is a thing not to be underestimated." 출처: Migrating and Benchmarking a Banking Application (Alessandro Amadori, TNO)

- **다년 프로젝트 규모** — 단일 은행 애플리케이션도 완전 마이그레이션에 다년이 소요된다. DoD(미국 국방부)는 100만 명 이상의 직원이 사용하는 시스템 전체를 2031년까지 전환해야 하며, 이는 5년 단위 예산 사이클과 충돌한다. "If our users can't meet security requirements for 10 years, that is our fault — we have picked the wrong standards." 출처: Transitioning National Security Systems (Morgan Stern, NSA / PKI Consortium Austin 2025)

- **규제 인증 요건** — FIPS 승인 알고리즘만 사용 가능한 규제 산업(금융, 국방, 의료)에서는 공식 표준화 이전 알고리즘 도입이 불가능하다. 인증 대기 시간이 신속한 도입을 막는다. 출처: What Is Post-Quantum Cryptography (HN 쓰레드, user: throw0101d)

- **서드파티 벤더 의존성** — ABN Amro 사례처럼 핵심 암호화 프로토콜이 외부 위탁(Outsource) 또는 특허 보호 상태여서 내부 마이그레이션 결정권이 없는 경우가 빈번하다. 출처: Migrating and Benchmarking a Banking Application (Alessandro Amadori, TNO)

- **발견/인벤토리 단계의 도구 부족** — NIST NCCoE는 암호화 의존성 검색(Discovery & Inventory) 도구가 아직 충분히 성숙하지 않았다고 인정했다. 기업이 어디에 RSA/ECC가 쓰이는지조차 파악하지 못한다. "We can only demonstrate [discovery] in a lab without any real threats, without any real traffic and data at a scale that's going to look great." 출처: NIST Post-Quantum Cryptography Update (Bill Newhouse, NIST NCCoE)

- **양자 위협 시간표 불신** — 일부 개발자/실무자는 위협 긴박성을 과장된 것으로 의심한다. "China's government views AES-256 as safe until 2100." 이는 기업 내 PQC 예산 확보를 어렵게 한다. 출처: What Is Post-Quantum Cryptography (HN 쓰레드, user: ilove196884)

### 시장 니즈

- **PQC 성숙도 평가 프레임워크** — PKI Consortium이 Post-Quantum Cryptography Maturity Model (PQCMM)을 공개했다. 정부·기업·인프라 운영자가 준비도를 자가 평가하고 단계적 마이그레이션 계획을 수립할 수 있는 실용적 도구에 대한 수요가 크다. 출처: PKI Consortium PQC Conference 2025 결산 보고 (pkic.org)

- **암호화 의존성 자동 발견(Discovery) 도구** — 기업 전체 시스템에서 취약 알고리즘 사용 현황을 자동으로 탐색하는 도구 필요. NIST NCCoE가 40개 이상의 민관 협력사(Wells Fargo, US Army PKI 등)와 공동으로 실증 중이다. 출처: NIST Post-Quantum Cryptography Update (Bill Newhouse, NIST NCCoE)

- **도메인별 마이그레이션 타임라인 명확화** — NSA는 2027년(신규 조달 PQC 역량 요구) → 2030년(하드웨어 기준선) → 2031년(PQC 활성화 완료)의 단계별 로드맵을 발표했다. 공급사들이 이에 맞는 제품 인증을 위한 명확한 요건 정의를 필요로 한다. 출처: Transitioning National Security Systems (Morgan Stern, NSA)

- **실제 마이그레이션 경험 사례 공유** — 차기 2026년 암스테르담 PKI Consortium 컨퍼런스 의제가 "practical migration experiences, real-world challenges, lessons learned"에 집중된다는 점에서 업계 전반의 실패/성공 사례 공유 플랫폼 수요가 확인된다. 출처: PKI Consortium PQC Conference 2025 결산 보고

- **하이브리드 키 교환(Hybrid Key Exchange) 가이던스** — 기존 알고리즘과 PQC 알고리즘을 병행 운영하는 전환 기간 동안의 표준화된 구현 가이드 부재. 개발자 커뮤니티에서 "convenient hybrid security for those with only classical computers"를 요구하는 목소리가 있다. 출처: What Is Post-Quantum Cryptography (HN 쓰레드)

### 분석 소스

| 소스 | 제목 | 유형 | 날짜 |
|------|------|------|------|
| Alessandro Amadori (TNO) | Migrating and Benchmarking a Banking Application | YouTube / PKI Consortium Austin | 2025-01 |
| Bill Newhouse & Andrew Regenscheid (NIST / NCCoE) | NIST Post-Quantum Cryptography Update | YouTube / PKI Consortium Austin | 2025-01 |
| Morgan Stern (NSA) | Transitioning National Security Systems to a Post-Quantum Future | YouTube / PKI Consortium Austin | 2025-01 |
| Hacker News 커뮤니티 | What Is Post-Quantum Cryptography – NIST (item 41383843) | HN 쓰레드 | 2024-08 |
| Hacker News 커뮤니티 | Google's threat model for post-quantum cryptography (item 39672583) | HN 쓰레드 | 2024-03 |
