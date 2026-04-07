---
type: weekly-monitor
domain: secure-ai
week: 2026-W15
date: 2026-04-07
l3_count: 5
deep_count: 3
---

# 주간 기술 동향: Secure AI (2026-W15 Update)

## Executive Summary

> **이번 주 핵심**: Cryptographically Relevant Quantum Computer (CRQC) 위협이 학술 커뮤니티 최고조에 달했다. Scott Aaronson이 Google+Caltech 논문 교차 적용으로 Elliptic Curve Cryptography (ECC)-256 공격 하한을 "25,000 물리 큐비트"로 재추정(4/1)했고, Nature가 "real shock"으로 보도(4/6)하며 주류 과학계가 임박한 위협으로 공식 분류. 스팸/피싱 영역은 EvilTokens Phishing-as-a-Service (PhaaS) 340+ Microsoft 365 기관 피해(3/31)와 Multi-Factor Authentication (MFA) 완전 우회 Device Code Phishing이 새 공격 벡터로 급부상. Fully Homomorphic Encryption (FHE) 측은 CryptoLab "2026년 동형암호 상용화 원년" 선언(4/4)과 HEaaN2 부트스트래핑 9.6ms 세계 기록 발표가 핵심.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| 양자/동형 암호 | On-Device Post-Quantum Cryptography (PQC) | 🟡 | [기술돌파] Aaronson ECC-256 공격 하한 25K 큐비트 재추정 · [규제] Nature "real shock" 주류 과학계 경보 · [생태계] Schneier 크립토-어질리티 지지 |
| | On-Device 동형암호 | 🟡 | [제품출시] CryptoLab "상용화 원년" 선언·Gartner 인정(4/4) · [기술돌파] HEaaN2 부트스트랩 9.6ms 세계 기록 [원문 미확인] |
| | Secure Vector Search | 🟢 | Hermes FHE-SQL 논문 진전, 독립 돌파 없음 |
| 스팸/피싱탐지 | 스팸/피싱 감지(통화전) | 🟡 | [기술돌파] EvilTokens PhaaS 340+ 기관 MFA 완전 우회 · [규제] Microsoft AI 피싱 클릭률 450%↑ 경고(4/2) · 한국 통신사기법 개정 입법예고(4/2) |
| | OCR 이미지 스팸 차단 | 🟢 | 신규 시그널 없음 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
> **태그** : [기술돌파] [제품출시] [경쟁사] [규제] [투자] [논문] [생태계]

---

## 🟢 Quick 요약 (변화 미미)

### Secure Vector Search
- Hermes(arXiv 2506.03308 v3)가 FHE-native 벡터 쿼리를 MySQL 엔진에서 직접 처리하는 최초 시스템으로 학술적 진전을 보였으나, 상용 솔루션의 독립적 돌파는 없음. Niobium The Fog의 Encrypted Semantic Search 포함이나 벡터 검색 자체의 성능 독립 검증 미발표. Partially Homomorphic Encryption (PHE) 기반 효율적 대안 연구(arXiv 2503.05850)도 진행 중.

### OCR 활용 이미지 스팸 차단
- 신규 시그널 없음. Gmail RETVec + Gemini Nano 온디바이스 보호 체계 유지. GLM-OCR 멀티모달 OCR 모델(2026)이 문서 이해에서 1.86 pages/sec 처리량을 보이나 이미지 스팸 특화 적용 사례 없음.

---

## 🟡🔴 Deep 심층 분석

### 스팸/피싱 감지(통화전) — 🟡 주목

#### 이전 대비 변화
- 전주: INTERPOL-UNODC $442B 글로벌 사기 손실 공식화, American Bankers Association (ABA)·Better Identity Coalition (BIC) 연방 정책 20개 권고안(4/1), Pindrop Pulse 2초 99% 탐지
- 금주: EvilTokens PhaaS 340+ 기관 Device Code Phishing(3/31), Microsoft "AI가 공격 도구에서 사이버공격 표면으로 전환" 경고(4/2), Tycoon2FA PhaaS 공조 폐쇄 후 즉시 재개, 한국 통신사기피해환급법 시행령 개정안 입법예고(4/2~5/12)
- 변화 방향: 피싱 공격이 딥페이크 음성에서 AI 자동화 OAuth 탈취(Device Code Phishing)로 다변화. PhaaS 플랫폼이 차단 후 즉시 복구하는 회복탄력성 확보 — 단속 효과 반감

#### 기술 동향

1. **Microsoft AI 위협 보고서 — AI 피싱 클릭률 비AI 대비 450% 상승, "에이전트 에코시스템이 최대 공격 표면" 전망(4/2).**
   Microsoft Security Blog(4/2)이 AI 위협 보고서를 발표했다. 생성형 AI가 정찰·무기화·초기접근·지속성 유지까지 공격 전 단계에 내재화됐으며, "공격 임계비용이 국가급 자원에서 개인 툴 접근성 수준으로 붕괴"(Sherrod DeGrippo 부 Chief Information Security Officer (CISO)) 됐다고 분석. [[G-01]](#ref-g-01)

2. **EvilTokens PhaaS — 340+ Microsoft 365 기관 대상 Device Code Phishing, MFA 완전 우회(3/31).**
   OAuth RFC 8628의 합법적 인증 흐름을 악용해 피해자가 직접 MFA를 완료하지만 공격자가 세션 토큰을 수집하는 구조. 패스워드 리셋 후에도 리프레시 토큰 유효. 피해 섹터: 건설·비영리·금융·의료·법률·지방정부. 한국 통신사 컨택센터 환경에도 동일 위협 벡터 노출 가능. [[G-02]](#ref-g-02), [[G-03]](#ref-g-03)

3. **Tycoon2FA 공조 폐쇄 후 즉각 복구 — PhaaS 회복탄력성 실증(3/4→4월 지속).**
   Europol·Microsoft·Cloudflare 공조로 300개 도메인 압수(3/4), 64,000건 연계 플랫폼 차단. 그러나 수일 내 압수 전 수준으로 복구. 월 500만+ 기관 대상 운영. Adversary-in-the-Middle (AiTM) 프록시 세션 쿠키 실시간 탈취. 단일 PhaaS 폐쇄가 피싱 생태계 억제에 구조적 한계를 가짐을 실증. [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)

4. **Cofense 연간 리포트 — AI 피싱 204% 증가, 19초당 1건 악성 이메일(2026-02).**
   2025년 기준 악성코드 탑재 피싱 캠페인 204% 증가. 초기 감염 URL 76%가 고유 주소(폴리모픽 피싱), 원격접속 도구 악용 900% 증가, 대화형 Business Email Compromise (BEC) 18% 비중. [[G-06]](#ref-g-06)

5. **Microsoft AI 활성화 디바이스코드 피싱 심층 분석(4/6).**
   EvilTokens 기반 역할 맞춤형 생성형 AI 피싱 이메일, 15분 만료 코드 동적 생성 자동화, Vercel·Cloudflare Workers·AWS Lambda 트래픽 위장 분석. Storm-2372(2025-02)에서 진화한 형태. [[G-07]](#ref-g-07)

6. **한국 통신사기피해환급법 시행령 개정안 입법예고(4/2~5/12).**
   금융위원회 주도. 금융사·통신사·수사기관 간 의심거래 탐지 정보공유 범위 명확화, 정보공유 분석기관 지정 요건 신설, "선제적 탐지·차단" 법적 근거 마련. 2025.10~2026.02 보이스피싱 신고 31.6% 감소(9,777→6,687건). [[G-08]](#ref-g-08)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Microsoft | 4/2 AI 위협 보고서: AI 피싱 클릭률 450% 상승. 4/6 EvilTokens 심층 기술 분석. Tycoon2FA 폐쇄(3/4) 공조 주도 | [[G-01]](#ref-g-01), [[G-07]](#ref-g-07) |
| EvilTokens (PhaaS) | 2026-02-16 Telegram 등장. 340+ M365 기관 타깃. Device Code Phishing 서비스화. Gmail·Okta 확장 예고 | [[G-02]](#ref-g-02), [[G-03]](#ref-g-03) |
| Pindrop | Fraud Assist 에이전트형 사기 조사(3/17). 분석관 효율 70%↑. FNBO 정확도 50%↑ | [[G-09]](#ref-g-09) |
| Adaptive Security | 총 $146.5M 펀딩. OpenAI 첫 사이버보안 투자처. 딥페이크·비싱·스미싱 AI 시뮬레이션 플랫폼 | [[G-10]](#ref-g-10) |
| SKT | ScamVanguard AI: 2025년 보이스피싱 2.5억건(+119%), 스팸 문자 8.5억건(+22%) 합계 11억건 차단 | [[G-11]](#ref-g-11) |
| KT | 후후(HuHu): 문맥+화자+딥보이스 삼중 탐지. 탐지 정확도 Q1 90.3% → Q4 97.2% | [[G-12]](#ref-g-12) |

#### 시장 시그널

**투자 & M&A**
- Adaptive Security 누적 $146.5M(Series B $81M): OpenAI 첫 사이버보안 투자처 [[G-10]](#ref-g-10)

**시장 전망**
- Vishing 442% 증가(2024 하반기, CrowdStrike), 딥페이크 비싱 1,600%+ 급증(2025 Q1) [[G-13]](#ref-g-13)
- AI 사기 손실: 2023년 $12.3B → 2027년 $40B 전망(Deloitte) [[G-14]](#ref-g-14)

**연구 동향**
- "Audio Deepfake Detection: What Has Been Achieved" (PMC, 2025) — ASVspoof 2019 LA EER 0.06% 달성. Wav2Vec 2.0·WavLM 자기지도학습이 전통 MFCC 대체 [[P-01]](#ref-p-01)
- "Where are We in Audio Deepfake Detection?" (ACM, 2026) — 최신 TTS 도구 대상 기존 탐지 모델 성능 저하 실증 [[P-02]](#ref-p-02)

**커뮤니티 시그널**
- Reddit: UN 스캠 콜센터 보고에 대한 높은 engagement — 크로스보더 관할권 문제 공감대 확산 [[C-01]](#ref-c-01)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- 탐지-공격 속도 격차 — 딥페이크 음성 합성(30초 오디오로 복제 가능) 앞에서 기존 음성 인증 무력화 — 출처: TADSummit 2025 (Enrico Faccioli)
- STIR/SHAKEN 커버리지 공백 — Tier-1 간 A등급 서명율 90% 달성에도 TDM 레거시 구간 파라미터 소실 — 출처: TNS Voice Security 2025
- 경보 피로(alert fatigue) — 오탐 과다로 "스팸 의심" 경고 무시 습관화. 고령층은 기기 경고보다 사람 목소리 신뢰 — 출처: HN 커뮤니티

**도입 장벽**
- AI 공격 도구의 저비용 접근성 — 공개 LLM+TTS 파이프라인으로 자율 비싱 봇 구성 가능(AsiaCCS 2025 실험 입증) — 출처: Figueiredo et al.
- OS 레벨 API 폐쇄 — 서드파티 탐지 앱 통화 메타데이터 접근 불가. 탐지 생태계 발전 저해 — 출처: HN 커뮤니티

**시장 니즈**
- 통화전 실시간 AI 탐지 엔진 — 착신 수 초 내 음성+발신 패턴+네트워크 메타데이터 복합 분석
- 산업 전체 위협 인텔리전스 공유 플랫폼 — 통신사 간 실시간 스캠 패턴 공유
- 차세대 발신자 인증 계층 — STIR/SHAKEN 이후 RCD, CNAM 보완, AI 행동 분석 기반

#### 전략적 시사점

**기회**
- 한국 통신사기피해환급법 개정(4/2)이 통신-금융 정보공유 플랫폼 구축 법적 근거 마련. 선점 통신사에 정부 파트너십 우선권
- PhaaS 복구 탄력성(Tycoon2FA)은 "토큰 유효기간 단축·세션 고착 방지" 등 기술적 방어 레이어 수요 증가 시사
- ABA FIDO 패스키 권고와 맞닿은 Device Code Phishing 대응 솔루션 포지셔닝 가능

**위협**
- EvilTokens MFA 완전 우회 Device Code Phishing이 통신사 기업 고객 새 공격 벡터로 부상
- AI 피싱 클릭률 450%↑(Microsoft) 및 19초당 1건(Cofense) — 공격 속도가 방어 응답 속도 초과

---

### On-Device PQC (양자내성암호) — 🟡 주목

#### 이전 대비 변화
- 전주: Google ECDLP <50만 큐비트 20배↓(3/31), Oratomic 10K 중성원자(3/31), Cisco IOS XE 26 전체 스택 PQC(4/1), 캐나다 PQC 이행 의무화(4/1)
- 금주: Aaronson 두 논문 교차 → ECC-256 공격 하한 "25,000 물리 큐비트"(4/1), Nature "real shock" 보도(4/6), Schneier 크립토-어질리티 지지(4/6), CoinDesk Bitcoin $1.3조 양자보안 종합 분석(4/4)
- 변화 방향: 위협 추정치 하한이 "50만→25,000 큐비트"로 재조정되며 학술 긴장 최고조. Nature·Schneier 등 주류 매체·전문가가 위협 공식 확인 — "이론→운영 위협" 전환 가속

#### 기술 동향

1. **Aaronson 종합 분석 — 두 논문 합산 시 ECC-256 공격 하한 "25,000 물리 큐비트" 도출(4/1).**
   Scott Aaronson(UT Austin)이 Caltech/Oratomic(quantum Low-Density Parity-Check (qLDPC) 고율 코드)과 Google(Shor 알고리즘 최적화) 논문을 교차 적용. "Caltech 그룹 추정치 기준, Elliptic Curve Digital Signature Algorithm (ECDSA)-256 공격에 단 25,000 물리 큐비트면 충분. 1년 전 최고 추정치는 수백만 큐비트"라고 발언. 다만 "이론적 하한이며 실제 CRQC 구현에는 수년 필요"라는 맥락 추가. [[G-15]](#ref-g-15)

2. **Nature — "양자컴퓨팅 돌파구, 사이버보안에 임박한 위협" 보도(4/6).**
   CRQC 필요 자원이 3개월 내 3편 논문으로 연속 급감한 사실을 "실제 충격(real shock)"으로 표현. 주류 학술 커뮤니케이션으로 위협 확산. [[G-16]](#ref-g-16)

3. **Schneier — Google 2029 PQC 전환 계획, "크립토-어질리티 관점에서 타당" 평가(4/6).**
   "2029년 이전 실용적 양자컴퓨터 등장을 보지 않지만, crypto-agility is always a good thing." 위협 확실성보다 아키텍처 유연성에서 PQC 도입 정당성을 찾는 전문가적 관점. [[G-17]](#ref-g-17)

4. **Bitcoin $1.3조 양자보안 경쟁 종합 분석(CoinDesk, 4/4).**
   약 650만 BTC(수천억 달러)가 공개키 온체인 노출 주소에 저장. 방어 수단: BIP-360(P2MR), Stateless Hash-Based Digital Signature Algorithm (SLH-DSA)(FIPS 205), commit/reveal 스킴. SLH-DSA 서명 크기 64B→8KB(125배↑) 블록 공간 압박 우려. [[G-18]](#ref-g-18)

5. **Warsaw 대학 Talbot effect Quantum Key Distribution (QKD) — 단일 검출기 고차원 QKD(4/1).**
   1836년 광학 현상 활용, 다중 상태 전송으로 데이터 용량 확대. 검출기 1개로 비용·복잡성 하락. 도시 광섬유망 실증. Optica Quantum 등 3개 저널 동시 게재. [[P-03]](#ref-p-03)

6. **NIST Hamming Quasi-Cyclic (HQC) 초안 2026년 초 예정 — Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) 백업 다양성 확보.**
   코드 기반 수학으로 격자 기반 ML-KEM과 상이한 기반 제공. 2027년 최종 확정 목표. [[G-19]](#ref-g-19)

#### 플레이어 동향

| 기업/기관 | 동향 | 출처 |
|-----------|------|------|
| Scott Aaronson (UT Austin) | 4/1: Google+Caltech 교차 → ECC-256 하한 25K 큐비트. "비트코인 서명이 기존보다 훨씬 일찍 취약" | [[G-15]](#ref-g-15) |
| Nature | 4/6: "real shock" 기사. CRQC 위협 주류 학술 커뮤니케이션 확산 | [[G-16]](#ref-g-16) |
| Bruce Schneier | 4/6: Google 2029 PQC 전환 "크립토-어질리티 관점 타당" | [[G-17]](#ref-g-17) |
| CoinDesk | 4/4: Bitcoin $1.3조 양자보안 분석. 650만 BTC 노출, 3개 방어방안 정리 | [[G-18]](#ref-g-18) |
| Warsaw 대학 | 4/1: Talbot effect QKD. 단일 검출기·고차원·도시 광섬유 실증 | [[P-03]](#ref-p-03) |
| NIST | HQC 초안 2026년 초, 2027 확정 목표. ML-KEM 백업 다양성 확보 | [[G-19]](#ref-g-19) |

#### 시장 시그널

**학술·전문가 반응**
- Aaronson "25K 큐비트 하한" — 학술 권위자 공식 종합이 미디어 레버리지로 작동 [[G-15]](#ref-g-15)
- Nature "임박한 위험(imminent risks)" — 주류 과학계 공식 분류 전환 [[G-16]](#ref-g-16)

**규제·정책**
- Year of Quantum Security (YQS) 2026: FBI·CISA·NIST 공동 출범. "양자 위협 이론→운영 격상" 선언 [[G-20]](#ref-g-20)

**시장 전망**
- PQC 시장: 2026년 $12억 → 2035년 $130억, CAGR 30% (Juniper Research) [[G-21]](#ref-g-21)
- 상위 40% 웹사이트 이미 하이브리드 PQ 키 교환 지원 [[G-22]](#ref-g-22)

**연구 동향**
- Warsaw Talbot QKD: 엣지 단말 QKD 비용 하향 경로 제시 [[P-03]](#ref-p-03)
- ARM Cortex-M0+ ML-KEM-512 35.7ms·2.83mJ(전주 발표, 인용 증가) [[P-04]](#ref-p-04)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- 레거시 코드 하드코딩 — ABN Amro 마이그레이션에서 RSA가 64개 파일 수동 수정 필요 — 출처: PKI Consortium 2025 (Amadori, TNO)
- PQC 서명 크기 — 수 KB로 쿠키 4096B 제한과 충돌, stateless 아키텍처 호환 불가 — 출처: HN 커뮤니티

**도입 장벽**
- Crypto Agility 아키텍처 부재 — 기존 시스템이 특정 알고리즘에 단단히 결합 — 출처: PKI Consortium 2025
- 다년 마이그레이션 규모 — DoD 100만+ 직원 시스템 2031년 전환 vs 5년 예산 사이클 충돌 — 출처: PKI Consortium 2025

**시장 니즈**
- PQC 성숙도 평가 프레임워크(PQC Maturity Model (PQCMM)) — 자가 진단 + 단계별 마이그레이션 계획 수립
- 전사 암호화 의존성 자동 발견 도구 — 취약 알고리즘 현황 스캔 자동화

#### 전략적 시사점

**기회**
- Schneier의 크립토-어질리티 지지는 PQC 조기 도입 산업 합의 형성 시사. 하이브리드 PQC 아키텍처 선제 도입으로 조달 기준 선점 가능
- Warsaw Talbot QKD는 엣지 단말 QKD 비용 장벽 하향 — QKD+PQC 하이브리드 장기 로드맵 참고

**위협**
- Aaronson "25K 큐비트" — Harvest Now, Decrypt Later (HNDL) 하 VoLTE/VoNR 트래픽 복호화 위험 구체화
- SLH-DSA 서명 125배 증가 — 통신 SIP 시그널링/미디어 보안에서도 동일 오버헤드 문제. PQC 알고리즘 선택 시 실시간 음성 품질 영향 사전 정량화 필수

---

### On-Device 동형암호 키워드 검색 — 🟡 주목

#### 이전 대비 변화
- 전주: Niobium "The Fog" FHE 클라우드 베타(4/2), CryptoLab HEaaN Zero-Leak Retrieval-Augmented Generation (RAG) Government Software (GS) 1등급(3/27), LG U+ AICC PoC, Intel Heracles ISSCC
- 금주: CryptoLab "2026년 상용화 원년" 선언(4/4), HEaaN2 부트스트랩 9.6ms 기록, Niobium 독립 검증 요구 제기, Hermes FHE-MySQL 통합 논문 진전
- 변화 방향: W15 플랫폼·인증 발표 → W15 후반 미디어 서사 확산 및 기술 검증 논쟁으로 전환

#### 기술 동향

1. **CryptoLab HEaaN2 부트스트래핑 9.6ms 세계 기록 — FHE 핵심 병목 돌파 주장.**
   CryptoLab LinkedIn 채널 발표. 부트스트래핑은 FHE 누적 노이즈 제거 핵심 절차. Builder API, 유연한 재스케일, 다항식 평가 최적화 포함. 공식 기술 논문·벤치마크 미공개. [[G-23]](#ref-g-23) [원문 미확인]

2. **Hermes — FHE-native 벡터 쿼리를 MySQL에서 직접 처리하는 최초 시스템(arXiv v3, 3/16).**
   Single Instruction Multiple Data (SIMD)-aware 데이터 모델로 복수 레코드 단일 암호문 패킹. 기존 대비 암호화 처리량 3,400× 향상, 튜플 삽입 4,000×, 삭제 300× 가속. 산업용 관계형 DB 엔진에 FHE 통합 최초 실용 사례. [[P-05]](#ref-p-05)

3. **"Privacy at your Fingertips" — 클라이언트 측 FHE 연산 최대 7× 가속(ePrint 2026/515).**
   그라츠 공대 연구팀의 Boosted-Deflation 기법. 부트스트래핑을 활용해 클라이언트 암복호화에서 부동소수점 연산 의존성 제거. HEaaN 대비 동일 파라미터 환경에서 7× 속도 향상. 온디바이스 FHE 키워드 검색 클라이언트 오버헤드 직접 감소. [[P-06]](#ref-p-06)

4. **CryptoLab "2026년 동형암호 상용화 원년" 선언 — Gartner 인정, 공공 조달 로드맵(4/4).**
   서울경제 영문판 인터뷰. CEO 천정희: "2026년에 완전히 상용화된 분야가 반드시 나올 것." Gartner 혁신 기술 선정 국내 최초. LG U+ ixi-O 통합 공식 확인. 조달청 혁신 시제품(6월), Common Criteria (CC) EAL2(9월) 로드맵. [[G-24]](#ref-g-24), [[E-01]](#ref-e-01)

5. **Niobium The Fog — 독립 기술 분석에서 성능 검증 요구 제기(4/2 이후).**
   Zubnet.ai: "독립 검증 없음, 벤치마크 없음, 암호 기법 세부 정보 없음." Transformer 추론 지원, 지연 시간, AI 프레임워크 호환성 미답변 지적. [[G-25]](#ref-g-25) [추가확인 필요]

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| CryptoLab | "상용화 원년" 선언(4/4). Gartner 인정 국내 최초. HEaaN2 9.6ms 기록 [원문 미확인]. LG U+ ixi-O PoC. 조달청 6월·CC 9월 | [[G-24]](#ref-g-24), [[E-01]](#ref-e-01), [[G-23]](#ref-g-23) |
| Niobium | The Fog 베타 지속. Q2 말 공개 출시. mistic Core FPGA(GPU 2×). 독립 검증 요구 제기 | [[G-25]](#ref-g-25), [[G-26]](#ref-g-26) |
| LG U+ | CryptoLab과 ixi-O·AICC 동형암호 PoC 진행. 국내 통신사 최초 FHE 실서비스 경로. 상용화 일정 미확정 | [[E-02]](#ref-e-02) |
| Intel | Heracles ISSCC: 1,074~5,547× Xeon 대비 가속. 3nm FinFET. 양산 미발표 | [[G-27]](#ref-g-27) |

#### 시장 시그널

**상용화 서사 확산**
- CryptoLab CEO "2026년 상용화 원년" + Gartner 선정 → 국내외 언론 확산. 공공·통신 부문 예산 배정 정당화 근거 [[G-24]](#ref-g-24)
- Niobium Q2 공개 출시 준비 중이나 가격·독립 검증 미공개 [[G-25]](#ref-g-25)

**연구 동향**
- Hermes MySQL 통합: FHE가 산업용 DB 엔진 수준 진입 최초 사례 [[P-05]](#ref-p-05)
- ePrint 2026/515: 클라이언트 측 7× 가속 — 온디바이스 배포 임계값 돌파 가능 [[P-06]](#ref-p-06)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- FHE 배포 시 주변 인프라(Hardware Security Module (HSM), Trusted Execution Environment (TEE), Kafka) 복잡도가 FHE 자체를 압도 — 출처: FHE.org 2025 (Bergamaschi, Intel Labs)
- Large Language Model (LLM) 등 대형 모델 FHE 실행 불가 — "수만 배 느림", 9MB→188GB 팽창 — 출처: HEIR (Google); HN

**도입 장벽**
- 파라미터 선택 전문성 요구 — 자동 파라미터 선택 부재 — 출처: HEIR (Google)
- ML 모델 호환성 — PyTorch/TF export 시 reshape/transpose 연산 FHE 부적합 — 출처: HEIR (Google)

**시장 니즈**
- Python 친화적 FHE SDK — "most requested feature" (HEIR, Google) — 출처: FHE.org 2025
- 금융기관 간 Private Query 서비스 — 쿼리 의도+DB 모두 숨기는 협력 쿼리 플랫폼 — 출처: Intel Labs PoC

#### 전략적 시사점

**기회**
- CryptoLab "상용화 원년" 프레이밍과 GS 인증이 국내 공공·통신 부문 예산 배정 정당화 근거
- ePrint 2026/515 클라이언트 오버헤드 감소는 온디바이스 키워드 검색 제품화 핵심 선행 기술

**위협**
- Niobium 성능 주장 독립 검증 지연 시 FHE 플랫폼 전반 시장 신뢰 훼손 가능
- HEaaN2 9.6ms 기록 공식 논문 미공개 — 재현 불가 시 CryptoLab 기술 리더십 서사에 타격

---

## 경쟁사 동향 (SKT / KT)

> 이번 주 해당 도메인과 관련된 SKT·KT의 주요 움직임.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| ScamVanguard AI | 2025년 보이스피싱 2.5억건(+119%), 스팸 문자 8.5억건(+22%) 합계 11억건 차단. AI 미끼 문자·피싱 채팅·음성패턴·실명 분석 4개 AI 앱 추가 | spam-phishing-detection | [[G-11]](#ref-g-11) |
| Thales 5G PQC | Crystals-Kyber SIM 카드 협력 지속. W15 기간 신규 발표 없음 | pqc-voice-encryption | [[G-28]](#ref-g-28) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 양자 암호키 분배 | 초당 30만개 암호키 생성 장비 자체 개발(2026-02). 도청 원천 차단 | pqc-voice-encryption | [[G-29]](#ref-g-29) |
| 후후(HuHu) AI | 문맥+화자+딥보이스 삼중 탐지 체계. Q4 97.2% 정확도 | spam-phishing-detection | [[G-12]](#ref-g-12) |
| MWC 2026 퀀텀 세이프 | 6G 핵심 기술로 "퀀텀 세이프 보안" 제시. QKD+AI 침해탐지+동형암호 결합 | pqc-voice-encryption | [[G-30]](#ref-g-30) |

### 시사점
- SKT는 ScamVanguard AI로 스팸/피싱 탐지 실적(11억건)을 쌓고, KT는 후후 정확도(97.2%)로 경쟁. 두 통신사 모두 양자보안에 투자 중이나 PQC 상용 서비스 출시는 아직 없음
- LG U+가 CryptoLab과 동형암호 AICC 차별화를 선점 중 — KT/SKT 미대응 시 프라이버시 차별화 포인트 선점 가능

---

## 규제 & 거버넌스

> 해당 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 | 시행일 | D-day |
|------|--------|-------|
| EU AI Act Article 6 (High-Risk AI 의무) | 2026-08-02 | D-117 |
| EU Cyber Resilience Act (CRA) 보고 의무 | 2026-09-11 | D-157 |
| FIPS 140-2 인증 종료 | 2026-09-21 | D-167 |
| Commercial National Security Algorithm (CNSA) 2.0 신규 조달 의무화 | 2027-01-01 | D-269 |
| NIST IR 8547 RSA/ECDSA deprecated (초안) | 2030 | D-~1,364 |
| NIST IR 8547 RSA/ECDSA disallowed (초안) | 2035 | D-~3,191 |
| 캐나다 PQC 고우선순위 시스템 완료 | 2031 | D-~1,729 |
| 한국 AI 기본법 Article 31 (AI 생성 표시) | 2026-01-22 | 시행 중 |
| FCC SIP 603+ Analytics-Based Blocking | 2026-03-25 | 시행 중 |
| 캐나다 PQC 이행계획 제출·조달 의무화 | 2026-04-01 | 시행 중 |

### 신규 발의 & 가이드라인

- **한국 통신사기피해환급법 시행령 개정안 입법예고(4/2~5/12)**: 금융-통신-수사 정보공유 의무화 추진. "선제적 탐지·차단" 법적 근거 마련 [[G-08]](#ref-g-08)
- **ABA·BIC 연방 정책 20개 권고안(4/1)**: FIDO 패스키·모바일 운전면허증(mDL) 도입 규제 장벽 제거. Treasury 태스크포스 신설 촉구. 130명+ 전문가 18개월 작업 [[G-14]](#ref-g-14)
- **YQS2026(Year of Quantum Security 2026)**: FBI·CISA·NIST 공동 출범 연중 진행. "양자 위협 이론→운영 격상" 공식 선언 [[G-20]](#ref-g-20)

### 시사점
- 통신사기법 개정이 실현되면 국내 통신사의 피싱 탐지 데이터 공유가 의무화되어 협력형 AI 탐지 인프라 구축 가속
- YQS2026와 캐나다 의무화 프레임 확산 — 과기정통부·KISA PQC 의무화 일정 조기화 가능성 모니터링 필요

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **CRQC 위협 학술 공인 단계 진입** — Aaronson 25K 큐비트, Nature "real shock", Schneier 크립토-어질리티 지지가 동시 발생. 위협이 "이론→전문가 확인→주류 과학 공인" 3단계를 거침. VoLTE/VoNR 통화 녹음 암호화의 PQC 전환 우선순위를 재검토할 시점

2. **PhaaS 회복탄력성 vs 피싱 방어 구조적 한계** — Tycoon2FA 즉각 복구 사례는 단일 차단 전략의 구조적 한계 노출. AI 기반 지속 감지·적응형 방어(Device Code Phishing 대응 포함)로 패러다임 전환 필요

3. **FHE 상용화 서사 확산 + 검증 압력** — CryptoLab "상용화 원년" 선언과 Niobium 검증 요구가 동시에 나타남. 기술 성숙도와 마케팅 서사 사이의 갭을 주시하면서, 실제 PoC 결과(LG U+ AICC)에 집중할 필요

### 후속 조치 제안

- 🟡 PQC — Aaronson 25K 큐비트 하한 추정의 VoLTE/VoNR 보안 영향 내부 검토. Schneier 크립토-어질리티 논리를 활용한 PQC 도입 내부 제안서 작성 검토
- 🟡 동형암호 — CryptoLab HEaaN2 9.6ms 공식 논문 공개 추적. Niobium Q2 공개 출시 모니터링. LG U+ PoC 진행 상황 계속 추적
- 🟡 스팸/피싱 — Device Code Phishing 위협의 국내 컨택센터 영향 평가. 통신사기법 개정안 입법예고 기간(~5/12) 모니터링

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Microsoft Security Blog — Threat actor abuse of AI accelerates | [링크](https://www.microsoft.com/en-us/security/blog/2026/04/02/threat-actor-abuse-of-ai-accelerates-from-tool-to-cyberattack-surface/) | news | 2026-04-02 | [A] |
| <a id="ref-g-02"></a>G-02 | Help Net Security — EvilTokens device code phishing Microsoft 365 | [링크](https://www.helpnetsecurity.com/2026/03/31/eviltokens-phishing-microsoft-365/) | news | 2026-03-31 | [B] |
| <a id="ref-g-03"></a>G-03 | The Hacker News — Device Code Phishing 340+ M365 Orgs | [링크](https://thehackernews.com/2026/03/device-code-phishing-hits-340-microsoft.html) | news | 2026-03 | [B] |
| <a id="ref-g-04"></a>G-04 | Microsoft Security Blog — Inside Tycoon2FA AiTM phishing kit | [링크](https://www.microsoft.com/en-us/security/blog/2026/03/04/inside-tycoon2fa-how-a-leading-aitm-phishing-kit-operated-at-scale/) | news | 2026-03-04 | [A] |
| <a id="ref-g-05"></a>G-05 | The Hacker News — Europol Takes Down Tycoon2FA | [링크](https://thehackernews.com/2026/03/europol-led-operation-takes-down-tycoon.html) | news | 2026-03-04 | [B] |
| <a id="ref-g-06"></a>G-06 | Cofense — AI-Powered Phishing One Attack Every 19 Seconds | [링크](https://cofense.com/Blog/Cofense-Report-Reveals-AI-Powered-Phishing-Accelerated-to-One-Attack-Every-19-Seconds) | 보고서 | 2026-02 | [A] |
| <a id="ref-g-07"></a>G-07 | Microsoft Security Blog — AI-enabled device code phishing campaign | [링크](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/) | news | 2026-04-06 | [A] |
| <a id="ref-g-08"></a>G-08 | 정책브리핑 — 보이스피싱 범죄 더 빠르고 강력히 대응 | [링크](https://www.korea.kr/news/policyNewsView.do?newsId=148962033) | 공식 | 2026-04-02 | [A] |
| <a id="ref-g-09"></a>G-09 | Help Net Security — Pindrop Fraud Assist | [링크](https://www.helpnetsecurity.com/2026/03/17/pindrop-protect-fraud-assist/) | news | 2026-03-17 | [B] |
| <a id="ref-g-10"></a>G-10 | Biometric Update — Adaptive Security $146.5M | [링크](https://www.biometricupdate.com/202512/new-series-b-round-brings-adaptives-total-capital-raised-to-146-5-million) | news | 2025-12 | [B] |
| <a id="ref-g-11"></a>G-11 | Telecompaper — SKT AI-driven spam/phishing blocking 11억건 | [링크](https://www.telecompaper.com/news/skt-reveals-rise-in-ai-driven-blocking-of-spam-and-voice-phishing-attempts--1558993) | news | 2026-01-13 | [B] |
| <a id="ref-g-12"></a>G-12 | The Fast Mode — KT HuHu AI Voice Phishing Detection | [링크](https://www.thefastmode.com/technology-solutions/39153-kt-unveils-real-time-ai-voice-phishing-protection) | news | 2026 | [B] |
| <a id="ref-g-13"></a>G-13 | Security Magazine — Vishing 442% increase | [링크](https://www.securitymagazine.com/articles/101439-vishing-attacks-increased-by-442-in-the-second-half-of-2024) | news | 2025 | [B] |
| <a id="ref-g-14"></a>G-14 | Help Net Security — Financial groups fight AI identity fraud | [링크](https://www.helpnetsecurity.com/2026/04/01/fight-ai-identity-fraud/) | news | 2026-04-01 | [B] |
| <a id="ref-g-15"></a>G-15 | Scott Aaronson — Quantum computing bombshells not April Fools | [링크](https://scottaaronson.blog/?p=9665) | blog | 2026-04-01 | [A] |
| <a id="ref-g-16"></a>G-16 | Nature — Real shock: quantum-computing breakthroughs imminent risks | [링크](https://www.nature.com/articles/d41586-026-01054-1) | news | 2026-04-06 | [A] |
| <a id="ref-g-17"></a>G-17 | Schneier on Security — Google PQC 2029 transition | [링크](https://www.schneier.com/blog/archives/2026/04/google-wants-to-transition-to-post-quantum-cryptography-by-2029.html) | blog | 2026-04-06 | [A] |
| <a id="ref-g-18"></a>G-18 | CoinDesk — Bitcoin $1.3T quantum-proofing race | [링크](https://www.coindesk.com/tech/2026/04/04/bitcoin-s-usd1-3-trillion-security-race-key-initiatives-aimed-at-quantum-proofing-the-worlds-largest-blockchain) | news | 2026-04-04 | [B] |
| <a id="ref-g-19"></a>G-19 | NIST — HQC Fifth Algorithm Post-Quantum Encryption | [링크](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption) | news | 2025-03-11 | [A] |
| <a id="ref-g-20"></a>G-20 | Quantum Insider — Year of Quantum Security 2026 | [링크](https://thequantuminsider.com/2026/01/14/u-s-federal-agencies-are-stepping-up-for-the-quantum-security-transition/) | news | 2026-01-14 | [B] |
| <a id="ref-g-21"></a>G-21 | Juniper Research — PQC Market $13B by 2035 | [링크](https://www.juniperresearch.com/press/post-quantum-cryptography-market-to-exceed-13-billion-by-2035-as-q-day-awareness-accelerates/) | news | 2026 | [B] |
| <a id="ref-g-22"></a>G-22 | Security Boulevard — PQC: Awareness to Execution | [링크](https://securityboulevard.com/2026/04/post-quantum-cryptography-moving-from-awareness-to-execution/) | news | 2026-04-01 | [B] |
| <a id="ref-g-23"></a>G-23 | CryptoLab LinkedIn — HEaaN2 bootstrap 9.6ms world record | [링크](https://www.linkedin.com/company/cryptolabinc/) | social | 2026-04 | [C] |
| <a id="ref-g-24"></a>G-24 | Seoul Economic Daily — CryptoLab Gartner commercialization 2026 | [링크](https://en.sedaily.com/finance/2026/04/04/gartner-recognized-encryption-startup-seeks-to) | news | 2026-04-04 | [B] |
| <a id="ref-g-25"></a>G-25 | Zubnet.ai — Niobium Fog details thin | [링크](https://zubnet.ai/news/niobiums-fog-promises-fully-encrypted-ai-details-thin/) | blog | 2026-04 | [C] |
| <a id="ref-g-26"></a>G-26 | SiliconANGLE — Niobium The Fog encrypted AI | [링크](https://siliconangle.com/2026/04/02/niobium-brings-fully-encrypted-ai-workloads-cloud-fog/) | news | 2026-04-02 | [B] |
| <a id="ref-g-27"></a>G-27 | Tom's Hardware — Intel Heracles FHE 1,074-5,547× | [링크](https://www.tomshardware.com/tech-industry/cyber-security/intels-heracles-chip-computes-fully-encrypted-data-without-decrypting-it-chip-is-1-074-to-5-547-times-faster-than-a-24-core-intel-xeon-in-fhe-math-operations) | news | 2026-03-10 | [B] |
| <a id="ref-g-28"></a>G-28 | SK Telecom Newsroom — Thales 5G PQC SIM | [링크](https://news.sktelecom.com/en/628) | news | 2023-02 | [B] |
| <a id="ref-g-29"></a>G-29 | 서울신문 — KT 초당 30만개 양자 암호키 생성 | [링크](https://www.seoul.co.kr/news/economy/industry/2026/02/04/20260204029004) | news | 2026-02-04 | [B] |
| <a id="ref-g-30"></a>G-30 | Insight Korea — SKT·KT·LGU+ 양자 보안 구축 | [링크](https://www.insightkorea.co.kr/news/articleView.html?idxno=242127) | news | 2026 | [B] |
| <a id="ref-p-01"></a>P-01 | PMC — Audio Deepfake Detection: What Has Been Achieved | [링크](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | ACM Trans. Internet Tech. — Where are We in Audio Deepfake Detection? | [링크](https://dl.acm.org/doi/10.1145/3736765) | paper | 2026 | [A] |
| <a id="ref-p-03"></a>P-03 | Karpiński et al. — Talbot effect high-dimensional QKD | [링크](https://www.sciencedaily.com/releases/2026/04/260401071933.htm) | paper | 2026-04-01 | [A] |
| <a id="ref-p-04"></a>P-04 | Janssen et al. — ML-KEM ML-DSA ARM Cortex-M0+ benchmark (arXiv:2603.19340) | [링크](https://arxiv.org/abs/2603.19340) | paper | 2026-03-30 | [A] |
| <a id="ref-p-05"></a>P-05 | Zhao — Hermes FHE-native MySQL (arXiv:2506.03308 v3) | [링크](https://arxiv.org/abs/2506.03308) | paper | 2026-03-16 | [A] |
| <a id="ref-p-06"></a>P-06 | Aikata et al. — Privacy at your Fingertips FHE client-side 7× (ePrint 2026/515) | [링크](https://eprint.iacr.org/2026/515) | paper | 2026-03-13 | [A] |
| <a id="ref-e-01"></a>E-01 | CryptoLab CEO 천정희 — "2026년 동형암호 상용화 원년" | [링크](https://en.sedaily.com/finance/2026/04/04/gartner-recognized-encryption-startup-seeks-to) | IR/발표 | 2026-04-04 | [B] |
| <a id="ref-e-02"></a>E-02 | LG U+ CTO — ixi-O AICC 동형암호 PoC | [링크](https://www.ebn.co.kr/news/articleView.html?idxno=1701823) | IR/발표 | 2026-03-10 | [B] |
| <a id="ref-c-01"></a>C-01 | HN — UN scam call centers epidemic | [링크](https://news.ycombinator.com/item?id=43768100) | community | 2026 | [C] |
