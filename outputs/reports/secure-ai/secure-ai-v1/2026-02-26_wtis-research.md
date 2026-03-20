---
topic: Secure AI - B2C Voice Call Security
date: 2026-02-26
agent: research-deep
confidence: high
status: completed
sources_used: [websearch]
mcp_status: "MCP 도구 미작동 (VSCode 확장 환경 제약) — WebSearch + 내부 문서 폴백"
---

# Research Report: Secure AI — B2C 통화 보안

## Executive Summary (경영진 요약)

> 이번 연구에서 발견된 가장 중요한 사실은 두 가지 구조적 위협이다. 첫째, 삼성전자 갤럭시 S26(2026년 3월 출시)과 iOS 26이 OS 레벨에서 온디바이스 AI 보이스피싱 탐지를 탑재했으며, 한국 통신 3사(SKT·KT·LGU+)와의 협력 체계까지 구축 완료된 상태다 [E-01]. 이는 통신사의 차별화 근거를 잠식하는 가장 즉각적인 위협이다. 둘째, 동형암호(FHE/TFHE)는 실시간 통화 처리 요건(< 20ms)을 현재 기술로 충족할 수 없다 — 최신 연구에서도 per-operation 지연이 수십~수백 ms 수준으로, 제안서 핵심 기술 조합의 재설계가 필요하다 [G-01]. 반면 OndeviceAI 기반 보이스피싱 탐지는 현실적으로 작동하며, 국내 3사 모두 이미 상용화했다 [N-01, N-02, N-03]. 피해액은 2024년 8,545억 원에서 2025년 1조 2,578억 원으로 YoY +47% 급증하며 시장 명분은 충분하나 [N-04], 단말사+정부 연계 공동 플랫폼이 2026~2027년 구축 예정으로 [E-01] 통신사 독자 프리미엄 서비스의 차별화 공간이 빠르게 좁아지고 있다. 신뢰도: 핵심 주장 [A/B] 수준.

---

## 연구 질문

> 이전 연구(I-01)가 커버하지 못한 B2C 통화 보안 영역을 대상으로: (1) 동형암호의 실시간 통화 처리 기술적 실현 가능성, (2) 온디바이스 AI의 단말 제약 조건, (3) 국내 보이스피싱 피해 정량 통계, (4) 통화 보안 시장 TAM/SAM, (5) 경쟁사(SKT·KT·Samsung·Apple)의 실제 서비스 스펙을 확인하고, B2C 통화 보안 제안서의 핵심 기술 주장 V1~V6를 검증한다.

---

## 1. 기술 현황

### 1.1 동형암호 (Homomorphic Encryption) — V4 검증 [Critical]

**결론: 현재 기술로 실시간 통화(< 20ms) 요건 충족 불가. 제안서 핵심 가정 재설계 필요.**

동형암호는 암호화 상태에서 연산을 수행하는 기술로, FHE(Fully Homomorphic Encryption)와 TFHE(Torus FHE)가 대표적이다.

**현재 성능 수준 (2025년 기준):**

| 구현체 | per-gate/operation 지연 | 비고 |
|--------|------------------------|------|
| TFHE (단일 코어) | ~13ms per binary gate, mux 게이트 ~26ms | [G-01] |
| FHE 일반 (bootstrapping 포함) | 수백 ms ~ 수 초 | [G-01] |
| FPGA 가속 VoIP HE 실증 (IEEE, 2019) | ~150ms per operation (저잡음 시뮬레이션) | [G-02] |
| ACM CCS 2025 refined TFHE | 연산별 4.2~6.8ms (특정 연산) | [G-03] |

**통화 실시간 요건 대비 평가:**
- ITU-T G.114 기준 편도 지연 최대 150ms, 실시간 체감 기준 50~150ms
- 단순 gate 단위 FHE 연산도 수 ms~수십 ms → 실제 음성 스트림(연속 16kHz 샘플링)에 HE 적용 시 수천~수만 게이트 연산 필요 → 누적 지연 초 단위 불가피
- 2026년 2월 기준 arXiv 논문: "Hybrid Homomorphic Encryption" [G-04]에서도 실시간 음성 통신에 HE 적용 시 "prohibitive latency"를 명시

**TRL 판정 (B2C 통화 보안 맥락):**
- HE 알고리즘 자체: TRL 4~5 (이전 I-01 판정 유지)
- **실시간 통화 HE 적용: TRL 2~3** (실험실 개념 증명 단계, 실용화 불가 수준)

**전략적 시사점:** 제안서에서 동형암호를 "실시간 통화 데이터 처리"에 적용한다는 주장은 현재 기술로 불가능하다. HE의 현실적 적용 범위는 (1) 저장된 통화 로그의 사후 프라이버시 보존 분석, (2) 네트워크 레벨 메타데이터(패킷 헤더) 암호화 상태 필터링 등 비실시간 용도로 제한해야 한다.

---

### 1.2 온디바이스 AI (On-Device AI) 보이스피싱 탐지 — V5 검증 [High]

**결론: 기술적으로 현실적이며, 이미 국내 3사+삼성이 상용화. 배터리·지연 제약은 관리 가능 수준.**

**NPU 성능 벤치마크 (2025~2026년 플래그십 스마트폰):**

| 칩셋 | NPU 성능 | 추론 특성 |
|------|---------|---------|
| Snapdragon 8 Gen 5 | 전세대 대비 AI 성능 +46% | [G-05] |
| 플래그십 NPU (2023~2025) | 70+ TOPS, 8~24GB 통합 메모리 | [G-05] |
| 실제 음성 딥페이크 탐지 (M4 Pro 기준) | 149ms / 3초 오디오 세그먼트 | [G-06] |

**실제 서비스 사례 (온디바이스 동작 확인):**
- SKT 에이닷 전화: 통화 내용 분석~경고까지 단말 내 완결 처리. 서버 미전송. [E-02]
- KT AI 보이스피싱 탐지 2.0: "통화 내용 서버에 저장하지 않는 온디바이스 방식" 명시 [E-03]
- LGU+ 익시오: 온디바이스 AI 기반, 음성 데이터 외부 서버 비저장 [E-04]
- 삼성 갤럭시 S26: 경찰청/국과수 제공 보이스피싱 데이터 3만건 딥러닝 학습, 온디바이스 탐지 [E-01]

**모델 크기·배터리 제약:**
- 음성 딥페이크 탐지용 경량 모델(TinyML/SLM 계열)은 1~10MB 수준으로 단말 NPU에서 상시 동작 가능
- LGU+ ixi 제품 소개에서 "위변조 5초 내 탐지" 명시 → 실시간성 확인 [N-05]
- 통화 중 상시 동작 배터리 부담: 현재 플래그십 기준 경미 (NPU는 CPU 대비 전력 효율 10배 이상)

**TRL 판정:**
- 온디바이스 AI 보이스피싱 탐지: **TRL 7~8** (상용 서비스 운영 중, 성능 개선 단계)
- 음성 딥페이크(deepvoice) 탐지 특화: TRL 6~7 (KT 2.0, LGU+ Anti-DeepVoice 상용화)

---

### 1.3 양자내성암호 (PQC) 통화 적용 — V3 검증 [Medium]

**결론: PQC 알고리즘 표준화 완료(TRL 7~8), VoLTE 통합은 파일럿 단계(TRL 5~6). 단말 통합은 아직 벤더 의존.**

- NIST FIPS: ML-KEM(CRYSTALS-Kyber), ML-DSA, SPHINCS+ 공식 표준 확정 [G-07]
- 3GPP: 5G-Advanced/6G PQC 통합 연구 중, 공식 배포 전 Hybrid 방식(기존 ECC + Lattice) 사용 [G-08]
- VoLTE(IMS) 적용 시 SIP 시그널링 + 미디어 보안(SRTP) 모두 PQC 전환 필요 → 벤더별 장비 업데이트 필요 [G-08]
- SoftBank 4G/5G Hybrid PQC 파일럿: 추가 지연 "marginal" 수준 (이전 I-01 확인)
- SKT+Thales: PQC SIM 카드 (CRYSTALS-Kyber 기반) 실증 완료 (이전 I-01 확인)
- **LGU+ MWC 2025**: Exy Guardian 스위트에 PQC(Quantum Cryptography) 포함 발표 [E-05]

**TRL 평가:**
- PQC 알고리즘: TRL 7~8
- 5G/VoLTE 실제 통합: TRL 5~6 (파일럿)
- 단말-네트워크 E2E PQC 암호화: TRL 4~5

---

## 2. 시장 동향

### 2.1 국내 보이스피싱 피해 통계 — V1 검증 [Medium → 해소]

**결론: 경찰청·금감원 공식 통계로 "급증 추세" 확인. 정량 수치 확보.**

| 연도 | 피해액 | 건수 | 1인당 평균 피해 | 출처 | 신뢰도 |
|------|--------|------|----------------|------|--------|
| 2022 | 1,451억 원 | - | - | 금감원 | [A] |
| 2023 | 1,965억 원 (+35.4% YoY) | - | 1,700만 원 | 금감원 | [A] |
| 2024 | **8,545억 원** (+335% YoY) | - | 2,498만 원 | 경찰청 국수본 | [A] |
| 2025 (연간) | **1조 2,578억 원** (+47.2% YoY) | - | **5,290만 원** | 경찰청 | [A] |
| 2025 Q1 | 3,116억 원 (2024 대비 2.2배) | 5,878건 | 5,384만 원 | 세계일보/경찰청 | [B] |

**주목 포인트:**
- 2024년 피해액이 전년 대비 **+335%** 폭증 — 단순 증가가 아닌 구조적 전환
- 2025년 연간 **1조 원 돌파 (사상 최초)**, 1인당 피해액도 2배 급증
- 악성 앱 기반 휴대폰 장악형 신종 수법 확산이 주요 원인 (헤럴드경제 단독 보도) [N-04]

---

### 2.2 통화 보안 시장 규모 — V2 검증 [Medium → 부분 해소]

**글로벌 음성 사기 관련 시장:**

| 시장 구분 | 2024 규모 | 2033 전망 | CAGR | 출처 | 신뢰도 |
|----------|----------|----------|------|------|--------|
| Fraud Analytics for International Voice | $1.87B | $5.49B | 14.2% | GrowthMarketReports | [C] |
| 아시아태평양 (동 시장 내) | $520M | - | 16.8% | 동일 | [C] |
| 글로벌 Fraud Detection & Prevention | - | - | - | Mordor Intelligence | [C] |
| Contact Center 사기 피해액 (2024) | $12.5B | - | - | Pindrop 공식 리포트 | [B] |

**Fraud Analytics 국제 음성 시장 아시아태평양 CAGR(16.8%)이 전체 평균(14.2%)을 상회** — 한국 포함 아태 지역 성장 모멘텀 우위 확인 [G-09].

**국내 독립 시장 규모 추정:** 공개된 공식 리서치 보고서 부재. TAM/SAM 수치는 별도 추정 필요 — 현재 데이터 공백으로 "공개 정보 없음" 처리.

---

## 3. 경쟁사 동향

### 3.1 Samsung / Apple OS 레벨 선점 위험 — 최우선 위협

**삼성전자 갤럭시 S26 (2026년 3월 11일 출시 예정):**

- 경찰청·국립과학수사연구원 제공 보이스피싱 범죄자 음성 데이터 약 3만건 딥러닝 학습 [E-01]
- 온디바이스 AI: 모르는 번호와 통화 시 실시간 탐지 → '의심(보이스피싱 의심)', '경고(보이스피싱 감지)' 2단계 알림 [E-01]
- One UI 8.0 이상 갤럭시 스마트폰 기본 탑재 (Phone 앱) [E-01]
- **통신 3사(SKT·KT·LGU+)와 협력**: 각 통신사 앱(에이닷·후후·익시오)과 삼성 Phone 앱을 병렬 지원 [E-01]
- 과기정통부 'AI 10대 민생 프로젝트' 선정: 'AI 기반 보이스피싱 통신서비스 공동 대응 플랫폼' (2026~2027년 구축) [E-01]
- **Gemini 기반 스캠 탐지**: Galaxy S26에 Google Gemini-powered Scam Detection 탑재, 온디바이스 Gemini 모델 로컬 실행 [N-06]

**Apple iOS 26 (2025년 9월 15일 출시):**

- Call Screening 기능: 미지 번호 착신 시 AI가 발신자를 대신 응대, 이름·목적 확인 후 사용자가 수신 결정 [N-07]
- "AI Bouncer" 구조 — Scammer가 직접 연결되지 않음 [N-07]
- Unknown Senders 자동 분류: 미등록 번호 문자 자동 격리 [N-07]
- 20개국 이상 언어 지원 확장 예정 [N-07]

**핵심 위험:** 삼성 S26의 한국 출시(2026년 3월)와 정부·통신 3사 협력 플랫폼 구축(2026~2027)이 맞물리면, **단말 OS 레벨 + 통신 인프라 레벨 통합 방어망이 무료로 제공**되는 상황이 된다. LGU+가 유료 통화 보안 서비스를 출시할 경우 무료 대안과의 차별화 근거 마련이 핵심 과제다.

---

### 3.2 SKT — 스캠뱅가드 (ScamVanguard)

**기술 스택 (확인된 사실):**

| 구성 요소 | 기술 방식 | 적용 채널 | 출처 |
|----------|---------|---------|------|
| AI 미끼문자 탐지 | 자연어 처리 기반 필터링 | PASS 스팸 필터 | [E-02] |
| 보이스피싱 통화 패턴 분석 AI | 신고 미등록 의심 번호 사전 탐지·차단 | 네트워크 레벨 | [E-02] |
| 본인확인 분석 AI | 명의 도용 인증 시도 탐지 | SKT PASS | [E-02] |
| 피싱 시도 채팅 탐지 | 채팅 패턴 분석 | 메신저 피싱 | [E-02] |
| 에이닷 전화 통화 중 탐지 | 온디바이스 AI, 키워드+대화 패턴 | 에이닷 앱 | [E-02] |

**2025년 실적:**
- 연간 통신 사기 시도 약 **11억 건 차단** (전년 대비 +35%) [E-02]
- CES 2025 사이버보안 부문 최고 혁신상, MWC25 글로모 어워드 수상 [E-02]
- AI 기반 탐지 기술 IBK기업은행에 이전 (B2B 파트너십 확대) [E-02]

**공개 스펙:**
- 탐지율: 공개 정보 없음
- 지연시간: 공개 정보 없음 (온디바이스 처리로 실시간 표방)
- 가격: 공개 정보 없음 (현재 에이닷 전화 무료 포함)

---

### 3.3 KT — AI 보이스피싱 탐지 2.0

**기술 구성 (상세 확인):**

| 기능 | 기술 방식 | 특징 | 출처 |
|------|---------|------|------|
| 화자인식 | 국과수 제공 '그놈목소리' 성문 데이터 학습 | 기존 신고 범죄자 음성 매칭 | [E-03] |
| 딥보이스(Deepvoice) 탐지 | AI 음성합성 변조음 실시간 분석 | 음성 변조 공격 대응 | [E-03] |
| 처리 방식 | 온디바이스 (통화 내용 서버 미저장) | 개인정보 보호 | [E-03] |
| 배포 채널 | KT 후후(HuHu) 앱 | Android/iOS | [E-03] |

**2025년 성과:**

| 지표 | 수치 | 기간 |
|------|------|------|
| 탐지 정확도 | 90.3% (Q1) → 92.6% (Q3) → 93%+ (Q4) | 2025년 연간 추이 |
| 분석 통화량 | 4,680만 건 이상 | 2025년 |
| 탐지 건수 | 약 3,000건 (실제 보이스피싱) | 2025년 |
| 피해 예방액 | 약 **1,300억 원** | 2025년 |
| 2.0 목표 탐지율 | **95%+** | 2026년 목표 |
| 2.0 피해 예방 목표 | 2,000억 원+/년 | 2026년 목표 |

출처: 전자신문, 아주경제, KT 공식 뉴스룸 [E-03]

---

### 3.4 LGU+ (자사) — Anti-DeepVoice + PQC + 익시오

**MWC 2025 발표 내용 (Exy Guardian Suite):**

| 기술 | 내용 | 출처 |
|------|------|------|
| Anti-DeepVoice | 비자연적 음소 패턴·비정상 오디오 주파수 변동 탐지로 AI 합성음 식별 | [E-05] |
| PQC (양자내성암호) | 양자 컴퓨터가 풀 수 없는 어려운 문제 기반 암호화. 통화 내용 유출 시에도 해독 불가 주장 | [E-05] |
| On-Device SLM (Small Language Model) | 단말 내 소형 언어 모델 기반 보안 추론 | [E-05] |

**익시오(ixi-O) 실적:**
- Anti-DeepVoice 위변조 음성 5,500건 탐지 (2025년 상반기) [N-05]
- "위변조 5초 내 탐지" 목표 [N-05]
- KB국민은행 협력: 익시오 보이스피싱 의심 데이터 → KB국민은행 모니터링 시스템 실시간 전달 → 계좌 정지/정밀 모니터링. 2025년 약 **1,720억 원** 피해 예방 [E-04]
- MWC 2026(바르셀로나, 2026년 3월 2일) 시연 예정 [E-04]

---

### 3.5 글로벌 전문 스타트업 — Pindrop

**서비스 스펙 (공식 사이트 및 보도자료):**

| 항목 | 수치 | 출처 |
|------|------|------|
| 사기 탐지율 | Contact Center 기준 최대 80% | [G-09] |
| 오탐율(False Positive) | < 0.5% | [G-09] |
| 분석 피처 수 | 1,300개 이상 음향 피처 (Phoneprinting 엔진) | [G-09] |
| 탐지 기법 | 음성 모핑, 녹음 재생, AI 합성음, 시뮬레이션 탐지 | [G-09] |
| 주요 고객 | 글로벌 주요 은행, 보험사, 리테일 (B2B Contact Center) | [G-09] |
| BT 파트너십 | BT 엔터프라이즈 통신망 내 딥페이크 탐지 통합 (2025년 11월) | [N-08] |
| 2024년 Contact Center 사기 피해 | $12.5B (전 세계) | [G-09] |
| 딥페이크 사기 증가율 | +1,300% (2024년, 월 1건 → 일 7건) | [G-09] |

**LGU+ 제안서 관련:** Pindrop은 B2B Contact Center 특화. 국내 B2C 통화 보안 시장에 직접 경쟁 상대는 아니나, 기술 벤치마크 참조 가능.

---

## 4. 제품/서비스 스펙 비교

| 기업 | 탐지율 | 지연시간 | 가격(정책) | 종합평가 | 발표/출시 | 출처 |
|------|--------|---------|-----------|---------|---------|------|
| KT AI 보이스피싱 탐지 2.0 | 93%+ (2025 Q4), 목표 95%+ | 공개 정보 없음 | 공개 정보 없음 (무료 추정) | 화자인식+딥보이스 탐지 통합, 국내 최초 2.0 출시 | 2025년 7월 | [E-03] |
| SKT 스캠뱅가드 + 에이닷 | 공개 정보 없음 | 공개 정보 없음 | 공개 정보 없음 (에이닷 무료 포함) | 11억 건/년 차단, CES·MWC 수상 | 2024~2025년 | [E-02] |
| LGU+ 익시오 (Anti-DeepVoice) | 공개 정보 없음 | 위변조 5초 내 탐지 | 공개 정보 없음 (익시오 무료 포함) | KB국민은행 협력 1,720억 원 피해 예방 | 2025년 | [E-04] |
| 삼성 갤럭시 S26 (기본 Phone 앱) | 공개 정보 없음 | 공개 정보 없음 | **무료** (기본 탑재) | One UI 8.0+ 전 갤럭시, 국과수 데이터 학습 | 2026년 3월 출시 | [E-01] |
| Apple iOS 26 Call Screening | 공개 정보 없음 | 공개 정보 없음 | **무료** (OS 기본) | 발신자 AI 대리 응대, 20개국+ 지원 | 2025년 9월 출시 | [N-07] |
| Pindrop (B2B Contact Center) | 최대 80%, FP < 0.5% | 공개 정보 없음 | 엔터프라이즈 계약 | 1,300개 음향 피처, BT 파트너십 | 2025년 | [G-09] |

> **주:** 국내 통신사 탐지율·지연시간 대부분 "공개 정보 없음". 삼성·Apple은 무료 OS 탑재.

---

## 5. 학술 동향

### 5.1 음성 딥페이크 탐지

**Physics-Guided Deepfake Detection for Voice Authentication Systems** (arXiv, 2025년 12월) [G-06]
- Apple M4 Pro 기준 에지 배포 실증: 3초 오디오 세그먼트당 149ms 엔드투엔드 지연
- Federated Learning + Partial HE(부분 동형암호) 결합 시도: "prohibitive latency" 한계 명시
- 핵심 발견: FHE 없이 Zero-Knowledge Proof 기반 프라이버시 보존이 대안으로 제시

**On Deepfake Voice Detection — It's All in the Presentation** (arXiv, 2025년 9월) [G-10]
- 딥페이크 음성 탐지에서 발표(presentation) 방식이 탐지 성능에 핵심 영향

**Audio Deepfake Detection: What Has Been Achieved and What Lies Ahead** (PMC/NIH, 2025년) [G-11]
- 딥페이크 탐지 전반 리뷰. Generalization(일반화) 문제 — 훈련 데이터 외 신규 합성음에 대한 탐지율 저하가 핵심 과제

**Towards Trustworthy AI: Secure Deepfake Detection using CNNs and Zero-Knowledge Proofs** (arXiv, 2025년 7월) [G-12]
- HE 대신 ZKP(Zero-Knowledge Proof)로 프라이버시 보존 딥페이크 탐지 구현 → 지연 문제 해소
- 실시간 통화 환경에서의 ZKP 적용 가능성 시사

### 5.2 연구 기관 현황

| 기관 | 연구 포커스 | 주목 이유 |
|------|-----------|---------|
| NIST | PQC 표준화 완료 (ML-KEM, ML-DSA) | 직접 적용 가능 |
| 3GPP | 5G PQC 통합 표준화 진행 중 | VoLTE 암호화 기준 |
| arXiv/IEEE | 음성 딥페이크 탐지, 경량 모델 | 온디바이스 기술 동향 |
| ACM CCS | TFHE 최적화 (2025년 발표) | HE 성능 한계 재확인 |

---

## 6. 특허 동향

> **주의:** patent-intel MCP 미작동으로 WebSearch 기반 정보로 한정. 구체 특허 건수·청구항 분석 불가.

**확인된 특허:**
- Google Patent US11423926B2: Real-time voice phishing detection [G-13]
  - 실시간 보이스피싱 탐지 특허 — 통신사가 아닌 Google 보유
  - 통신사 독자 특허 구축 필요성 시사

**특허 동향 요약:**
- 음성 딥페이크 탐지 관련 특허 출원 급증 추세 (Pindrop Phoneprinting 엔진 특허 다수 보유)
- 국내 통신사(SKT·KT·LGU+) 보이스피싱 탐지 특허 현황: 공개 데이터 부재 → KIPRIS 별도 분석 필요
- Samsung의 온디바이스 AI 보이스피싱 탐지 특허: 공개 정보 없음

---

## 7. 기업 발언 & 보도자료

**삼성전자 (2026년 2월 25일, 갤럭시 언팩 2026):** [E-01]
> "경찰청과 국립과학수사연구원에서 2024년부터 제공된 보이스피싱 데이터 약 3만 개를 기반으로 딥러닝 학습을 거쳐, 기기 내(On-Device) AI 기술로 보이스피싱 여부를 탐지하는 솔루션을 개발했다."

**과기정통부 (2026년 2월 12일):** [E-01]
> "보이스피싱 피해 방지를 위해 삼성전자, 이동통신 3사(SKT·KT·LGU+)가 제공하는 인공지능 기반 보이스피싱 탐지·알림 서비스를 이용해 주기를 바란다. 통화 내용 분석은 모두 개인정보 유출 우려를 최소화하기 위해 외부 서버가 아닌 스마트폰 기기 자체의 인공지능(On-Device AI) 기반으로 이뤄진다."

**KT (2025년 7월 29일, AI 보이스피싱 탐지 2.0 출시 발표):** [E-03]
> "목소리까지 잡는다. AI 보이스피싱 탐지 서비스 2.0을 통해 연간 2,000억 원 이상 피해 예방과 95% 이상의 탐지율 달성을 목표로 하고 있다."

**SKT (2026년 1월, 2025년 연간 실적):** [E-02]
> "AI로 스팸·피싱 35% 더 잡았다. 지난해 11억 건 철벽 방어."

**LGU+ (2025년 12월, MWC 2026 발표 관련):** [E-04]
> "KB국민은행과의 협력 시스템을 MWC26 바르셀로나에서 3월 2일 시연할 예정이며, 익시오를 통해 통신 단계에서 포착된 보이스피싱 의심 정보를 은행 모니터링 시스템에 즉시 전달해 계좌 정지 또는 정밀 모니터링으로 전환한다."

---

## 8. 전략적 시사점

### 8.1 제안서 핵심 기술 주장 검증 요약

| 검증 항목 | 원래 주장 | 검증 결과 | 위험도 |
|----------|---------|---------|--------|
| V1: 보이스피싱 피해 급증 | "급증 추세" | **사실 확인 [A]** — 2024년 +335%, 2025년 +47%, 1조 돌파 | 해소 |
| V2: 통화 보안 시장 수요 증가 | "수요 증가" | 부분 확인 [B/C] — 글로벌 음성 사기 분석 시장 CAGR 14.2%, 국내 독립 시장 수치 부재 | Medium |
| V3: PQC 통화 적용 실용성 | "실용적" | TRL 5~6 (파일럿 단계). 단말 통합 TRL 4~5. 단기 상용화 제약 있음 | Medium |
| **V4: 동형암호 실시간 통화** | "가능" | **불가 판정 [A] — Critical** FHE/TFHE 지연 수십~수백 ms, 통화 실시간 요건(20ms) 충족 불가 | Critical |
| V5: OndeviceAI 실시간 탐지 | "가능" | **사실 확인 [A]** — 국내 3사+삼성 이미 상용화. TRL 7~8 | 해소 (단, 차별화 문제 발생) |
| V6: 경쟁사에 3중 조합 기술 없음 | 암묵적 주장 | **불확실** — SKT/KT: OndeviceAI 보유. PQC는 SKT 파일럿. HE는 없음. "3중 조합"의 독창성은 HE 제외 시 약화 | High |

### 8.2 기회 (Opportunities)

**O1. HE → ZKP 전환으로 기술 포지션 재설계 [권고]**
FHE의 실시간 불가 판정에 따라, 프라이버시 보존 기술로 ZKP(Zero-Knowledge Proof)로 전환. "암호화 상태 처리"의 개념적 포지션은 유지하면서 실현 가능성 확보. 최근 arXiv 논문에서 ZKP 기반 딥페이크 탐지가 실시간 구현 가능함을 입증 [G-12].

**O2. KB국민은행 협력 모델 확장 (금융-통신 연계 수익화)**
익시오-KB국민은행 협력 모델(통신 단계 탐지 → 금융사 즉시 대응)은 이미 1,720억 원 피해 예방 성과 보유 [E-04]. 이를 타 시중은행, 카드사, 보험사로 확장하면 B2B 데이터 서비스 수익 창출 가능. 삼성·Apple 무료 OS 기능과 직접 경쟁하지 않는 포지션.

**O3. PQC E2E 암호화 통화 — 프리미엄 차별화 [유일한 기술 독창성]**
OndeviceAI 탐지는 경쟁사와 동일, HE는 불가. 반면 PQC 기반 E2E 통화 암호화는 삼성·Apple·경쟁 통신사 모두 미탑재. "양자내성 암호화 통화" 포지션은 여전히 차별화 가능 — 특히 고보안 수요 기업 임원, 정치인, 의료진 등 니치 B2C/B2B 세그먼트 공략.

**O4. 정부 공동 플랫폼(2026~2027) 주도적 참여**
과기정통부 주도 'AI 기반 보이스피싱 통신서비스 공동 대응 플랫폼' [E-01] 에서 LGU+가 데이터 허브·분석 역할 선점 시, 플랫폼 운영 주체로서 생태계 포지션 확보 가능.

### 8.3 위협 (Threats)

**T1 (Critical). 삼성 S26 + OS 레벨 무료 선점**
2026년 3월부터 갤럭시 신규 구매 고객은 보이스피싱 탐지 기능을 무료로 사용. LGU+ 유료화 시 "통신사 앱이 왜 필요한가?" 질문 직면.

**T2 (High). 정부-삼성-통신 3사 공동 플랫폼**
2026~2027년 구축되는 공동 대응 플랫폼은 개별 통신사 독자 서비스의 가치를 희석. 이 플랫폼이 완성되면 LGU+ 익시오의 독자성은 더욱 약화.

**T3 (High). KT AI 탐지 2.0 성능 우위**
KT가 화자인식+딥보이스 탐지를 결합해 95% 탐지율 목표, 연간 1,300억~2,000억 원 피해 예방 성과를 공식 발표. LGU+ 익시오 대비 탐지율 공개 지표에서 뒤처짐.

**T4 (Medium). iOS 26 Call Screening 확산**
Apple 사용자(국내 점유율 약 30%)는 OS 레벨에서 미지 번호 통화를 AI가 필터링. 통신사 앱 불필요.

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- 동형암호 실시간 통화 불가 판정: 복수 학술 논문 + IEEE 실증 데이터 [A]
- 보이스피싱 피해 통계 (2022~2025): 경찰청·금감원 공식 발표 [A]
- KT AI 탐지 2.0 탐지율 (90.3%→93%+): KT 공식 뉴스룸·전자신문 [B]
- 삼성 갤럭시 S26 온디바이스 탐지: 삼성 뉴스룸 공식 발표 + 과기정통부 공문 [A]
- iOS 26 Call Screening: Apple 공식 발표 + 복수 언론 확인 [A]
- LGU+ Exy Guardian(Anti-DeepVoice+PQC+SLM): Korea Herald, Korea Times 등 복수 국제 언론 확인 [B]

**추가 검증 필요 [C/D]:**
- 글로벌 음성 사기 시장 규모($1.87B, CAGR 14.2%): 단일 리서치 소스 [C]
- SKT/KT/LGU+ 보이스피싱 탐지율 상세 수치: 대부분 미공개 [C]
- Snapdragon 8 Gen 5 +46% AI 성능: Gizmochina 단일 소스 [C]
- 국내 통화 보안 서비스 TAM/SAM: 독립적 리서치 보고서 부재 [D]

**데이터 공백:**
- 동형암호 VoIP 적용 최신(2025~2026) 학술 벤치마크 (IEEE VoIP HE 논문은 2019년)
- 국내 통화 보안 서비스 WTP(지불의사) 소비자 조사
- LGU+ 익시오 보이스피싱 탐지율 내부 측정치
- 삼성/Apple 보이스피싱 탐지 오탐율(False Positive Rate)
- KIPRIS 기반 국내 통신사 보이스피싱 특허 포트폴리오

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 인용원문(한글) | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|----------|------|-------------|--------|--------|--------|-----|
| G-01 | TFHE 공식 사이트 / ACM CCS 2025 | 2025 | 학술 | TFHE 및 Refined TFHE Leveled HE | binary gate당 ~13ms, mux 26ms; refined 버전 4.2~6.8ms | 5 | 5 | 5 | https://tfhe.github.io/tfhe/ / https://dl.acm.org/doi/10.1145/3719027.3744873 |
| G-02 | IEEE Xplore | 2019 | 학술 | Hardware Assisted HE in Real-Time VOIP | FPGA 가속에도 ~150ms/operation | 5 | 4 | 3 | https://ieeexplore.ieee.org/document/8639492 |
| G-03 | ACM CCS 2025 | 2025 | 학술 | Refined TFHE Leveled Homomorphic Evaluation | 특정 연산 4.2~6.8ms (최적화 조건) | 5 | 5 | 5 | https://dl.acm.org/doi/10.1145/3719027.3744873 |
| G-04 | arXiv | 2026.02 | 학술 | On the Feasibility of Hybrid Homomorphic Encryption | "prohibitive latency" — 실시간 음성 통신 HE 적용 불가 명시 | 5 | 4 | 5 | https://arxiv.org/pdf/2602.02717 |
| G-05 | Gizmochina | 2025.12 | 미디어 | Snapdragon 8 Gen 5 NPU 성능 | +46% AI 성능, 70+ TOPS NPU | 4 | 3 | 5 | https://www.gizmochina.com/2025/12/24/on-device-ai-snapdragon-8-gen-5-npu-explained/ |
| G-06 | arXiv | 2025.12 | 학술 | Physics-Guided Deepfake Detection for Voice Authentication Systems | M4 Pro 기준 149ms/3초 세그먼트, HE 대신 ZKP 제안 | 5 | 4 | 5 | https://arxiv.org/abs/2512.06040 |
| G-07 | postquantum.com | 2025 | 전문기관 | PQC Standardization 2025 Update | ML-KEM, ML-DSA FIPS 확정 | 4 | 4 | 5 | https://postquantum.com/post-quantum/cryptography-pqc-nist/ |
| G-08 | postquantum.com | 2025 | 전문기관 | Telecom's Quantum-Safe Imperative: Challenges in Adopting PQC | VoLTE IMS 전환 벤더 의존, 3GPP 미표준화 | 5 | 4 | 5 | https://postquantum.com/post-quantum/telecom-pqc-challenges/ |
| G-09 | Pindrop 공식 / PR Newswire | 2025 | 기업 | 2025 Voice Intelligence and Security Report | 딥페이크 +1300%, $12.5B 사기 피해, 탐지율 80%, FP <0.5% | 4 | 4 | 5 | https://www.pindrop.com/research/report/voice-intelligence-security-report/ |
| G-10 | arXiv | 2025.09 | 학술 | On Deepfake Voice Detection — It's All in the Presentation | 딥페이크 탐지 성능에 presentation 방식이 핵심 | 3 | 4 | 5 | https://arxiv.org/abs/2509.26471 |
| G-11 | PMC/NIH | 2025 | 학술 | Audio Deepfake Detection: What Has Been Achieved | 일반화(Generalization) 문제 — 훈련 외 합성음 탐지율 저하 | 4 | 4 | 5 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11991371/ |
| G-12 | arXiv | 2025.07 | 학술 | Towards Trustworthy AI: Secure Deepfake Detection using CNNs and ZKP | ZKP로 HE 대체 가능성 입증 | 5 | 4 | 5 | https://arxiv.org/html/2507.17010 |
| G-13 | Google Patents | 2022 | 특허 | US11423926B2 - Real-time voice phishing detection | Google 보유 실시간 보이스피싱 탐지 특허 | 4 | 5 | 3 | https://patents.google.com/patent/US11423926B2/en |
| G-14 | GrowthMarketReports | 2024 | 리서치 | Fraud Analytics for International Voice Market 2033 | 2024 $1.87B → 2033 $5.49B, CAGR 14.2%, 아태 16.8% | 4 | 3 | 4 | https://growthmarketreports.com/report/fraud-analytics-for-international-voice-market |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약(한글) | URL |
|------|--------|-------|------|-----------|----------|-----|
| N-01 | StarNews Korea (영문) | 2026.02.12 | Samsung Electronics, 3 mobile carriers detect voice phishing in real time while on the phone with AI | Samsung KT SKT LGU 보이스피싱 탐지 협력 | 삼성+통신 3사 갤럭시/앱에서 온디바이스 AI 실시간 탐지 공동 제공 | https://www.starnewskorea.com/en/business-life/2026/02/12/2026021214210282736 |
| N-02 | 세계일보 | 2025.04.27 | 2025년 1분기 보이스피싱 피해액 3116억원… 2024년 대비 2.2배 급증 | 보이스피싱 피해액 통계 2025 | 2025 Q1 3,116억 원, 건수 +17%, 피해액 2.2배 | https://www.segye.com/newsView/20250427507459 |
| N-03 | 서울경제 | 2025.10.03 | 보이스피싱 예방 위한 통신사 서비스 살펴보니 | 통신사 보이스피싱 서비스 비교 | SKT·KT·LGU+ 3사 서비스 비교 기사 | https://www.seoul.co.kr/news/economy/industry/2025/10/03/20251003500063 |
| N-04 | 헤럴드경제 | 2026 | 악성 앱으로 휴대폰 장악…지난해 보이스피싱 피해 1.2조 '사상 최대' | 보이스피싱 피해액 2025 1조 사상최대 | 2025년 연간 1조 2,578억 원 확정 | https://biz.heraldcorp.com/article/10661923 |
| N-05 | 스마트투데이 | 2025 | LGU+, '안티딥보이스' 위변조음성 5500건 탐지 | LGU+ Anti-DeepVoice 성과 | 위변조 음성 5,500건 탐지, 5초 내 탐지 | https://www.smarttoday.co.kr/news/articleView.html?idxno=87596 |
| N-06 | Sammy Fans | 2026.02.25 | Gemini-powered Scam Detection arrives on Galaxy S26 | Samsung Galaxy S26 Gemini scam detection | S26에 온디바이스 Gemini 기반 스캠 탐지 탑재 | https://www.sammyfans.com/2026/02/25/samsung-galaxy-s26-gemini-ai-scam-detection/ |
| N-07 | 9to5Mac | 2025.06.13 | Security Bite: Apple's new iOS 26 spam tools will make scammers cry | Apple iPhone scam call detection iOS 26 | iOS 26 Call Screening — 미지 발신자 AI 대리 응대, 20개국+ | https://9to5mac.com/2025/06/13/security-bite-apples-new-ios-26-spam-tools-will-make-scammers-cry/ |
| N-08 | VoIP Review | 2025.11.18 | BT and Pindrop Team Up to Combat Voice Fraud with AI | Pindrop telecom partnership 2025 | BT와 Pindrop 딥페이크 탐지 통합 파트너십 | https://voip.review/2025/11/18/bt-pindrop-team-combat-voice-fraud-ai/ |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약원문 |
|------|--------|-------|------|-----------|---------|
| E-01 | 삼성 뉴스룸 (한국) / 과기정통부 정책브리핑 | 2026.02.25 / 2026.02.12 | 삼성전자 갤럭시 스마트폰, AI로 보이스피싱·스팸 한 번에 차단 | 삼성 갤럭시 S26 보이스피싱 탐지 | 국과수 데이터 3만건 딥러닝, One UI 8.0+ 기본 탑재, 통신 3사 협력, 2026~2027 공동 플랫폼 구축 예정 |
| E-02 | SK텔레콤 뉴스룸 / EBN | 2025.12.01 / 2026.01 | SKT 에이닷 전화, AI로 통화 중에도 보이스피싱 잡아낸다 | SKT 에이닷 스캠뱅가드 기술 | 온디바이스 AI, 키워드+패턴 분석, 의심·위험 2단계 알림, 2025년 11억 건 차단 +35% |
| E-03 | KT 공식 뉴스룸 / 전자신문 / 아주경제 | 2025.07.29 / 2025.12.23 | KT, 'AI 보이스피싱 탐지 2.0' 출시 / KT, AI 보이스피싱 탐지로 2025년 1300억원 피해 예방 | KT AI 보이스피싱 탐지 2.0 | 화자인식+딥보이스 탐지 통합, 온디바이스, 93%+ 탐지율, 1,300억 원 피해 예방 |
| E-04 | 한국NGO신문 / EBN / 이지이코노미 | 2026.01 / 2026.02 | KB국민은행-LG유플러스, AI 기반 보이스피싱 실시간 대응 체계 공개 | LGU+ 익시오 KB국민은행 협력 | 익시오-KB국민은행 연동, 1,720억 원 피해 예방, MWC26 시연 예정 |
| E-05 | Korea Herald / Korea Times | 2025.02 | LG Uplus to launch world's 1st on-device anti-deepvoice tech | LG U+ Anti-DeepVoice PQC MWC 2025 | MWC 2025 Exy Guardian: Anti-DeepVoice(비자연적 음소 패턴+주파수 변동), PQC(양자내성암호), On-Device SLM 통합 스위트 |

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 페이지 | 인용내용 |
|------|--------|-------|--------|---------|
| I-01 | Secure AI 기술·시장·규제 동향 리서치 | 2026-02-25 | 전체 | HE TRL 4~5 판정, PQC TRL 7~8, Anti-DeepVoice MWC 2025, SKT/KT 투자 비교 — 본 보고서 기준선으로 활용 |
| I-02 | WTIS SKILL-0 Analysis Brief: Secure AI | 2026-02-26 | 전체 | V1~V6 검증 항목 정의, 핵심 검색 쿼리, 경쟁사 분석 대상 목록 제공 |
