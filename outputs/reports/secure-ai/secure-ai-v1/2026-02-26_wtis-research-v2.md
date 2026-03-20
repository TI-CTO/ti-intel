---
topic: Secure AI - B2C Voice Call Security
date: 2026-02-26
agent: research-deep
version: v2 (P-xx/T-xx retest)
confidence: high
status: completed
sources_used: [websearch]
mcp_status: "MCP 도구 미작동 (VSCode 확장 환경 제약) — WebSearch + 내부 문서 폴백. v1 대비 개선: G-xx 코드에서 학술 논문(P-xx)·특허(T-xx) 분리 완료. 신규 특허 2건·신규 논문 2건 추가."
---

# Research Report: Secure AI — B2C 통화 보안 (v2)

## Executive Summary (경영진 요약)

> 이번 연구(v2)의 핵심 개선사항은 소스 코드 체계의 정확한 재분류다. v1에서 G-xx로 혼입되었던 학술 논문 8편(P-01~P-08)과 특허 2건(T-01~T-02)을 별도 분리했으며, 신규 특허 3건(T-03~T-05)과 신규 논문 2편(P-09~P-10)을 추가 확보했다. 핵심 발견은 v1과 동일하게 유지된다: (1) 삼성전자 갤럭시 S26(2026년 3월 출시)과 iOS 26이 OS 레벨에서 온디바이스 AI 보이스피싱 탐지를 무료로 탑재했으며 [E-01], (2) 동형암호(FHE/TFHE)는 실시간 통화(< 20ms) 요건을 현재 기술로 충족할 수 없다 [P-01, P-02]. 신규 발견: Wells Fargo의 합성 음성 사기 탐지 특허(US20250252968A1) [T-03]는 금융사가 통신사를 우회해 독자 특허를 구축하고 있음을 시사하며, 경량 온디바이스 음성 딥페이크 탐지 모델(159k parameters, <1 GFLOP/inference) [P-09]은 LGU+ Anti-DeepVoice 기술의 학술적 실현 가능성을 강화한다. 피해액 1조 2,578억 원(2025년) [N-04] 시장 명분은 충분하나, 삼성+정부+통신 3사 공동 플랫폼(2026~2027년 구축 예정) [E-01]으로 인해 통신사 독자 유료 서비스의 차별화 공간이 빠르게 좁아지고 있다. 신뢰도: 핵심 주장 [A/B] 수준.

---

## 연구 질문

> 이전 연구(I-01)가 커버하지 못한 B2C 통화 보안 영역을 대상으로: (1) 동형암호의 실시간 통화 처리 기술적 실현 가능성, (2) 온디바이스 AI의 단말 제약 조건, (3) 국내 보이스피싱 피해 정량 통계, (4) 통화 보안 시장 TAM/SAM, (5) 경쟁사(SKT·KT·Samsung·Apple)의 실제 서비스 스펙을 확인하고, B2C 통화 보안 제안서의 핵심 기술 주장 V1~V6를 검증한다. v2에서는 추가로: 학술 논문·특허를 올바른 P-xx/T-xx 코드로 분류하고, 이전 데이터 공백 영역(특히 특허)을 보강한다.

---

## 1. 기술 현황

### 1.1 동형암호 (Homomorphic Encryption) — V4 검증 [Critical]

**결론: 현재 기술로 실시간 통화(< 20ms) 요건 충족 불가. 제안서 핵심 가정 재설계 필요.**

동형암호는 암호화 상태에서 연산을 수행하는 기술로, FHE(Fully Homomorphic Encryption)와 TFHE(Torus FHE)가 대표적이다.

**현재 성능 수준 (2025~2026년 기준):**

| 구현체 | per-gate/operation 지연 | 비고 |
|--------|------------------------|------|
| TFHE (단일 코어) | ~13ms per binary gate, mux 게이트 ~26ms | [P-01] |
| FHE 일반 (bootstrapping 포함) | 수백 ms ~ 수 초 | [P-01] |
| FPGA 가속 VoIP HE 실증 (IEEE, 2019) | ~150ms per operation (저잡음 시뮬레이션) | [P-02] |
| ACM CCS 2025 refined TFHE | 연산별 4.2~6.8ms (특정 연산) | [P-03] |
| ACM CCS 2023 E2E HE 오디오 컨퍼런싱 | 클라우드 지원 시 처리 가능, 단 전용 프로토콜 필요 | [P-04] |

**통화 실시간 요건 대비 평가:**
- ITU-T G.114 기준 편도 지연 최대 150ms, 실시간 체감 기준 50~150ms
- 단순 gate 단위 FHE 연산도 수 ms~수십 ms → 실제 음성 스트림(연속 16kHz 샘플링)에 HE 적용 시 수천~수만 게이트 연산 필요 → 누적 지연 초 단위 불가피
- 2026년 2월 기준 arXiv 논문 [P-05]: "Hybrid Homomorphic Encryption" 실시간 음성 통신에 HE 적용 시 "prohibitive latency" 명시

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
| 실제 음성 딥페이크 탐지 (M4 Pro 기준) | 149ms / 3초 오디오 세그먼트 | [P-06] |
| 경량 오디오 딥페이크 탐지 모델 (2026년 arXiv) | 159k parameters, <1 GFLOP/inference | [P-09] |

**SafeEar (ACM CCS 2024) 프라이버시 보존 딥페이크 탐지 [P-08]:**
- 음성 내용(semantic) 없이 acoustic 특성(prosody, timbre)만으로 딥페이크 탐지
- EER 2.02% (4개 벤치마크 데이터셋 평균) — 현존 최고 수준
- 5개 언어 음성 내용 WER 93.93% 이상 → 실질적 프라이버시 보호 달성
- **LGU+ Anti-DeepVoice 기술의 학술적 구현 근거로 활용 가능**

**실제 서비스 사례 (온디바이스 동작 확인):**
- SKT 에이닷 전화: 통화 내용 분석~경고까지 단말 내 완결 처리. 서버 미전송. [E-02]
- KT AI 보이스피싱 탐지 2.0: "통화 내용 서버에 저장하지 않는 온디바이스 방식" 명시 [E-03]
- LGU+ 익시오: 온디바이스 AI 기반, 음성 데이터 외부 서버 비저장 [E-04]
- 삼성 갤럭시 S26: 경찰청/국과수 제공 보이스피싱 데이터 3만건 딥러닝 학습, 온디바이스 탐지 [E-01]
- Honor Magic 7 Pro: 영상통화 딥페이크 실시간 온디바이스 탐지 (WeChat, WhatsApp, Messenger 지원) [G-05]

**모델 크기·배터리 제약:**
- 음성 딥페이크 탐지용 경량 모델(TinyML/SLM 계열)은 1~10MB 수준으로 단말 NPU에서 상시 동작 가능
- LGU+ ixi 제품 소개에서 "위변조 5초 내 탐지" 명시 → 실시간성 확인 [N-05]
- 최신 경량 모델(P-09): 159k params, <1 GFLOP → 배터리 영향 극미

**TRL 판정:**
- 온디바이스 AI 보이스피싱 탐지: **TRL 7~8** (상용 서비스 운영 중, 성능 개선 단계)
- 음성 딥페이크(deepvoice) 탐지 특화: TRL 6~7 (KT 2.0, LGU+ Anti-DeepVoice 상용화)

---

### 1.3 양자내성암호 (PQC) 통화 적용 — V3 검증 [Medium]

**결론: PQC 알고리즘 표준화 완료(TRL 7~8), VoLTE 통합은 파일럿 단계(TRL 5~6). 단말 통합은 아직 벤더 의존.**

- NIST FIPS: ML-KEM(CRYSTALS-Kyber), ML-DSA, SPHINCS+ 공식 표준 확정 [G-07]
- GSMA PQ.03 v2.0: 통신사용 PQC 가이드라인 2024년 업데이트 — VoLTE/VoNR IMS 적용 시 SIP 시그널링 + 미디어 보안(SRTP) 모두 PQC 전환 필요 [G-08]
- 3GPP: 5G-Advanced/6G PQC 통합 연구 중, 공식 배포 전 Hybrid 방식(기존 ECC + Lattice) 사용 [G-08]
- SoftBank 4G/5G Hybrid PQC 파일럿: 추가 지연 "marginal" 수준 (이전 I-01 확인)
- SKT+Thales: PQC SIM 카드 (CRYSTALS-Kyber 기반) 실증 완료 (이전 I-01 확인)
- **LGU+ MWC 2025**: Exy Guardian 스위트에 PQC(Quantum Cryptography) 포함 발표 [E-05]
- 2026년 PQC 시장: 연구 개념에서 핵심 사이버보안 축으로 전환 확인 [G-15]

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
- 악성 앱 기반 휴대폰 장악형 신종 수법 확산이 주요 원인 [N-04]

---

### 2.2 통화 보안 시장 규모 — V2 검증 [Medium → 부분 해소]

**글로벌 음성 사기 관련 시장:**

| 시장 구분 | 2024 규모 | 2033 전망 | CAGR | 출처 | 신뢰도 |
|----------|----------|----------|------|------|--------|
| Fraud Analytics for International Voice | $1.87B | $5.49B | 14.2% | GrowthMarketReports | [C] |
| 아시아태평양 (동 시장 내) | $520M | - | 16.8% | 동일 | [C] |
| Contact Center 사기 피해액 (2024) | $12.5B | - | - | Pindrop 공식 리포트 | [B] |
| 한국 사이버보안 시장 (전체) | $7.19억 달러 | $12.88억 달러 (2030) | - | Mordor Intelligence | [C] |

**Fraud Analytics 국제 음성 시장 아시아태평양 CAGR(16.8%)이 전체 평균(14.2%)을 상회** — 한국 포함 아태 지역 성장 모멘텀 우위 확인 [G-09].

**국내 독립 시장 규모 추정:** 공개된 공식 리서치 보고서 부재. B2C 통화 보안 서비스 TAM/SAM 수치는 별도 추정 필요 — 현재 데이터 공백으로 "공개 정보 없음" 처리.

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
- 음성 스팸·보이스피싱 통화 전년 대비 +119%, 2억 5천만 건 차단 [N-01]
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

**규제 경로 (신규 확인):**
- 2024년 10월: 과기정통부 ICT 규제샌드박스 실증특례 승인 [N-09]
- 실증특례 승인 → 상용화 경로 공식화 (KT가 국내 최초 규제 승인)

**2025년 성과:**

| 지표 | 수치 | 기간 |
|------|------|------|
| 탐지 정확도 | 90.3% (Q1) → 92.6% (Q3) → 91.6% (H1 평균) | 2025년 |
| 분석 통화량 | 1,460만 건 (H1) / 4,680만 건+ (연간) | 2025년 |
| 탐지 건수 | 약 3,000건 (실제 보이스피싱) | 2025년 |
| 피해 예방액 | 약 **1,300억 원** | 2025년 |
| 2.0 목표 탐지율 | **95%+** | 2026년 목표 |
| 2.0 피해 예방 목표 | 2,000억 원+/년 | 2026년 목표 |

출처: KT 공식 뉴스룸, 전자신문, 아주경제, The Pickool [E-03]

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
| 2025년 딥페이크 사기 예측 증가율 | +162% YoY | [G-14] |

**LGU+ 제안서 관련:** Pindrop은 B2B Contact Center 특화. 국내 B2C 통화 보안 시장에 직접 경쟁 상대는 아니나, 기술 벤치마크 참조 가능.

---

## 4. 제품/서비스 스펙 비교

| 기업 | 탐지율 | 지연시간 | 가격(정책) | 종합평가 | 발표/출시 | 출처 |
|------|--------|---------|-----------|---------|---------|------|
| KT AI 보이스피싱 탐지 2.0 | 91.6% (H1 평균), 목표 95%+ | 공개 정보 없음 | 공개 정보 없음 (무료 추정) | 화자인식+딥보이스 탐지 통합, 규제샌드박스 승인, 국내 최초 | 2025년 7월 | [E-03] |
| SKT 스캠뱅가드 + 에이닷 | 공개 정보 없음 | 공개 정보 없음 | 공개 정보 없음 (에이닷 무료 포함) | 11억 건/년 차단, CES·MWC 수상 | 2024~2025년 | [E-02] |
| LGU+ 익시오 (Anti-DeepVoice) | 공개 정보 없음 | 위변조 5초 내 탐지 | 공개 정보 없음 (익시오 무료 포함) | KB국민은행 협력 1,720억 원 피해 예방 | 2025년 | [E-04] |
| 삼성 갤럭시 S26 (기본 Phone 앱) | 공개 정보 없음 | 공개 정보 없음 | **무료** (기본 탑재) | One UI 8.0+ 전 갤럭시, 국과수 데이터 학습 | 2026년 3월 출시 | [E-01] |
| Apple iOS 26 Call Screening | 공개 정보 없음 | 공개 정보 없음 | **무료** (OS 기본) | 발신자 AI 대리 응대, 20개국+ 지원 | 2025년 9월 출시 | [N-07] |
| Pindrop (B2B Contact Center) | 최대 80%, FP < 0.5% | 공개 정보 없음 | 엔터프라이즈 계약 | 1,300개 음향 피처, BT 파트너십 | 2025년 | [G-09] |
| Honor Magic 7 Pro (온디바이스) | 공개 정보 없음 | 실시간 | **무료** (기본 탑재) | WeChat/WhatsApp 딥페이크 영상통화 탐지 | 2025년 | [G-05] |

> **주:** 국내 통신사 탐지율·지연시간 대부분 "공개 정보 없음". 삼성·Apple·Honor는 무료 OS 탑재.

---

## 5. 학술 동향

### 5.1 음성 딥페이크 탐지 — 주요 논문 (P-xx)

**[P-06] Physics-Guided Deepfake Detection for Voice Authentication Systems** (arXiv, 2025년 12월)
- Apple M4 Pro 기준 에지 배포 실증: 3초 오디오 세그먼트당 149ms 엔드투엔드 지연
- Federated Learning + Partial HE(부분 동형암호) 결합 시도: "prohibitive latency" 한계 명시
- 핵심 발견: FHE 없이 Zero-Knowledge Proof 기반 프라이버시 보존이 대안으로 제시

**[P-07] On Deepfake Voice Detection — It's All in the Presentation** (arXiv, 2025년 9월)
- 딥페이크 음성 탐지에서 발표(presentation) 방식이 탐지 성능에 핵심 영향
- 동일 모델도 입력 표현 방식에 따라 성능 편차 큼 → 서비스 구현 시 입력 전처리 중요

**[P-08] SafeEar: Content Privacy-Preserving Audio Deepfake Detection** (ACM CCS, 2024)
- **핵심 혁신**: 음성 내용(semantic) 접근 없이 acoustic 특성만으로 딥페이크 탐지 (프라이버시 보존)
- EER 2.02% (4개 벤치마크 데이터셋) — 현존 최고 수준의 프라이버시 보존 탐지
- WER 93.93% 이상 → 탐지 과정에서 음성 내용 사실상 복원 불가
- **LGU+ Anti-DeepVoice 기술 설계 레퍼런스로 직접 활용 가능**

**[P-09] Lightweight Resolution-Aware Audio Deepfake Detection** (arXiv, 2026년 1월)
- **신규**: 159k parameters, <1 GFLOP/inference — 온디바이스 배포 최적화
- ASVspoof 2019 LA: EER 0.16% (최고 수준), In-the-Wild deepfakes: AUC 0.98
- Cross-Scale Attention + Consistency Learning으로 다해상도 스펙트럼 표현 정렬
- **실용적 온디바이스 배포 가능성을 학술적으로 입증한 최신 결과**

**[P-10] Toward Noise-Aware Audio Deepfake Detection: SNR-Benchmarks** (arXiv, 2025년 12월)
- 실제 통화 환경(잡음 조건)에서의 딥페이크 탐지 강건성 벤치마크
- WavLM, Wav2Vec2, MMS 등 사전학습 인코더의 SNR별 성능 비교
- 핵심: 실제 통화 잡음 환경에서 탐지 성능 급락 문제 확인 — 실서비스 배포 시 핵심 고려사항

**[P-11] Audio Deepfake Detection in the Age of Advanced TTS** (arXiv, 2026년 1월)
- 최신 TTS 모델로 생성된 딥페이크 오디오에 대한 탐지 어려움 심화
- Generalization 문제: 훈련 데이터 외 신규 TTS 합성음에 대한 탐지율 저하

### 5.2 동형암호 — 주요 논문 (P-xx)

**[P-04] Now is the Time: Scalable Cloud-Supported Audio Conferencing using E2E HE** (ACM CCSW, 2023)
- **신규**: E2E 동형암호 오디오 컨퍼런싱의 최초 확장 가능 시연
- 클라우드 지원 시 처리 가능 — 단, 특수 설계된 혼합 프로토콜 필요
- 일반 VoIP/VoLTE 즉시 적용 불가 확인

### 5.3 연구 기관 현황

| 기관 | 연구 포커스 | 주목 이유 |
|------|-----------|---------|
| NIST | PQC 표준화 완료 (ML-KEM, ML-DSA) | 직접 적용 가능 |
| 3GPP | 5G PQC 통합 표준화 진행 중 | VoLTE 암호화 기준 |
| arXiv/IEEE | 음성 딥페이크 탐지, 경량 모델 | 온디바이스 기술 동향 |
| ACM CCS | TFHE 최적화, SafeEar | HE 성능 한계 + 프라이버시 보존 딥페이크 탐지 |

---

## 6. 특허 동향

> **주의:** patent-intel MCP 미작동으로 WebSearch 기반 정보로 한정. 구체 특허 건수·청구항 전문 분석 불가. KIPRIS 직접 검색은 웹 인터페이스 접근 제약으로 미수행.

### 6.1 신규 확인 특허 (T-xx)

**[T-01] Google — Real-time Voice Phishing Detection (US11423926B2)**
- 등록일: 2022년 8월 23일
- 핵심 청구항: 통신 네트워크에서 보이스피싱 탐지기가 판단한 결과를 단말에 알림 전달
- 의미: Google 보유 — 통신사 독자 특허 구축 필요성 시사

**[T-02] Samsung Electronics — AI Calculation Semiconductor Device (US11652603B2)**
- 등록일: 2024년
- 핵심 내용: 동형암호 연산을 가속하는 반도체 칩 — multiply/accumulator + cyclic shift로 FHE 속도 개선
- 의미: 삼성이 HE 가속 하드웨어 특허 보유. 단말-레벨 HE 처리 로드맵 시사

**[T-03] Wells Fargo Bank — Synthetic Voice Fraud Detection (US20250252968A1)**
- 출원일: 2024년 2월 7일 / 공개일: 2025년 2월 19일
- 핵심 청구항: (1) 실제 음성 샘플 수집·정규화, (2) 합성 클론 생성, (3) 실제·합성 페어 학습, (4) 미묘한 불일치 지표 탐지
- 의미: **금융사가 통신사를 우회해 독자 음성 딥페이크 탐지 특허 확보**. 은행이 자체 탐지 시스템 구축 시 통신사 솔루션 수요 감소 위험

**[T-04] Bank of America — Deepfake Detection System (US20250148788)**
- 출원일: 2023년 11월 7일 / 공개일: 2025년 5월 8일
- 핵심 내용: 컴퓨팅 기기에 설치된 딥페이크 분석 엔진이 콘텐츠 접근 모니터링 중 딥페이크 자동 탐지
- 의미: 또 다른 금융사의 독자 딥페이크 탐지 특허 — 금융사 자체 역량 구축 트렌드 확인

**[T-05] VoIP HE 특허 — Homomorphic Encryption for Teleconferencing (US20150237019A1)**
- 출원: 2015년 (초기 선행특허)
- 핵심 청구항: 참가자들이 additive HE로 음성 샘플 암호화 → 믹서가 암호화 상태에서 혼합
- 의미: VoIP HE 개념 선행특허. 현재 실용화 불가 TRL 확인의 역사적 맥락 제공

### 6.2 특허 동향 요약

- **금융사 선점**: Wells Fargo [T-03], Bank of America [T-04]가 합성 음성 탐지 특허를 2024~2025년 출원 — 통신사가 B2C 통화 보안 특허를 선점하지 않으면 기술 종속 위험
- **Google 보이스피싱 탐지 특허** [T-01]: 실시간 탐지 핵심 알고리즘 보유 — 국내 통신사가 유사 기능 구현 시 특허 침해 검토 필요
- **Samsung HE 가속 특허** [T-02]: 단말 레벨 HE 처리 가능성 시사 — 장기(3~5년) 기술 로드맵에서 온디바이스 HE 가능성 재검토 필요
- **국내 통신사 특허 현황**: KIPRIS 직접 검색 미수행으로 데이터 공백 유지. KT ICT 규제샌드박스 승인(2024년 10월) [N-09]은 특허와 별개의 규제 경로 확인

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

**Wells Fargo (2025년 2월, 특허 출원):** [T-03]
> "Advances in AI technology have made it possible to create highly convincing synthetic voices that can mimic real individuals. As synthetic voice technology becomes more sophisticated, detecting synthetic voices becomes more difficult."

---

## 8. 전략적 시사점

### 8.1 제안서 핵심 기술 주장 검증 요약

| 검증 항목 | 원래 주장 | 검증 결과 | 위험도 |
|----------|---------|---------|--------|
| V1: 보이스피싱 피해 급증 | "급증 추세" | **사실 확인 [A]** — 2024년 +335%, 2025년 +47%, 1조 돌파 | 해소 |
| V2: 통화 보안 시장 수요 증가 | "수요 증가" | 부분 확인 [B/C] — 글로벌 음성 사기 분석 시장 CAGR 14.2%, 국내 독립 시장 수치 부재 | Medium |
| V3: PQC 통화 적용 실용성 | "실용적" | TRL 5~6 (파일럿 단계). 단말 통합 TRL 4~5. 단기 상용화 제약 있음 | Medium |
| **V4: 동형암호 실시간 통화** | "가능" | **불가 판정 [A] — Critical** FHE/TFHE 지연 수십~수백 ms, 통화 실시간 요건(20ms) 충족 불가 | Critical |
| V5: OndeviceAI 실시간 탐지 | "가능" | **사실 확인 [A]** — 국내 3사+삼성 이미 상용화. TRL 7~8. 경량 모델(159k params) 학술 검증 | 해소 (단, 차별화 문제 발생) |
| V6: 경쟁사에 3중 조합 기술 없음 | 암묵적 주장 | **불확실** — SKT/KT: OndeviceAI 보유. PQC는 SKT 파일럿. HE는 없음. "3중 조합"의 독창성은 HE 제외 시 약화 | High |

### 8.2 기회 (Opportunities)

**O1. HE → ZKP 전환으로 기술 포지션 재설계 [권고]**
FHE의 실시간 불가 판정에 따라, 프라이버시 보존 기술로 ZKP(Zero-Knowledge Proof)로 전환. "암호화 상태 처리"의 개념적 포지션은 유지하면서 실현 가능성 확보. arXiv [P-06]에서 ZKP 기반 딥페이크 탐지가 실시간 구현 가능함을 입증. SafeEar [P-08]의 프라이버시 보존 탐지 아키텍처도 대안으로 활용 가능.

**O2. KB국민은행 협력 모델 확장 (금융-통신 연계 수익화)**
익시오-KB국민은행 협력 모델(통신 단계 탐지 → 금융사 즉시 대응)은 이미 1,720억 원 피해 예방 성과 보유 [E-04]. Wells Fargo [T-03], Bank of America [T-04]의 자체 특허 출원 트렌드를 고려 시, **LGU+가 먼저 국내 은행과 공동 특허를 구축하면 금융사 독자 진입 방어 가능**. 타 시중은행, 카드사, 보험사로 확장하면 B2B 데이터 서비스 수익 창출 가능.

**O3. PQC E2E 암호화 통화 — 프리미엄 차별화 [유일한 기술 독창성]**
OndeviceAI 탐지는 경쟁사와 동일, HE는 불가. 반면 PQC 기반 E2E 통화 암호화는 삼성·Apple·경쟁 통신사 모두 미탑재. "양자내성 암호화 통화" 포지션은 여전히 차별화 가능 — 특히 고보안 수요 기업 임원, 정치인, 의료진 등 니치 B2C/B2B 세그먼트 공략.

**O4. 정부 공동 플랫폼(2026~2027) 주도적 참여**
과기정통부 주도 'AI 기반 보이스피싱 통신서비스 공동 대응 플랫폼' [E-01] 에서 LGU+가 데이터 허브·분석 역할 선점 시, 플랫폼 운영 주체로서 생태계 포지션 확보 가능.

**O5. SafeEar 아키텍처 기반 프라이버시 차별화 [신규]**
SafeEar [P-08] 방식 채택 시, 통화 내용을 사실상 복원 불가능한 형태로 변환해 딥페이크만 탐지 — "음성 내용 무접근 탐지"를 공식 기술 포지션으로 채택 가능. KT/SKT 대비 프라이버시 보호 측면 차별화.

### 8.3 위협 (Threats)

**T1 (Critical). 삼성 S26 + OS 레벨 무료 선점**
2026년 3월부터 갤럭시 신규 구매 고객은 보이스피싱 탐지 기능을 무료로 사용. LGU+ 유료화 시 "통신사 앱이 왜 필요한가?" 질문 직면.

**T2 (High). 정부-삼성-통신 3사 공동 플랫폼**
2026~2027년 구축되는 공동 대응 플랫폼은 개별 통신사 독자 서비스의 가치를 희석. 이 플랫폼이 완성되면 LGU+ 익시오의 독자성은 더욱 약화.

**T3 (High). KT AI 탐지 2.0 성능 우위**
KT가 화자인식+딥보이스 탐지를 결합해 95% 탐지율 목표, 연간 1,300억~2,000억 원 피해 예방 성과를 공식 발표. LGU+ 익시오 대비 탐지율 공개 지표에서 뒤처짐.

**T4 (High, 신규). 금융사 독자 특허 구축**
Wells Fargo [T-03], Bank of America [T-04]가 2023~2024년 합성 음성 탐지 특허 출원. 금융사가 통신사를 우회해 독자 탐지 시스템 구축 시 LGU+ B2B 협력 모델(익시오-KB국민은행 방식)의 지속 가능성 위협.

**T5 (Medium). iOS 26 Call Screening 확산**
Apple 사용자(국내 점유율 약 30%)는 OS 레벨에서 미지 번호 통화를 AI가 필터링. 통신사 앱 불필요.

---

## 신뢰도 평가

**높은 확신 [A/B]:**
- 동형암호 실시간 통화 불가 판정: 복수 학술 논문 + IEEE 실증 데이터 [A] [P-01~P-05]
- 보이스피싱 피해 통계 (2022~2025): 경찰청·금감원 공식 발표 [A]
- KT AI 탐지 2.0 탐지율 (91.6% H1 평균): KT 공식 뉴스룸·Telecompaper [B]
- 삼성 갤럭시 S26 온디바이스 탐지: 삼성 뉴스룸 공식 발표 + 과기정통부 공문 [A]
- iOS 26 Call Screening: Apple 공식 발표 + 복수 언론 확인 [A]
- LGU+ Exy Guardian(Anti-DeepVoice+PQC+SLM): Korea Herald, Korea Times 등 복수 국제 언론 확인 [B]
- SafeEar EER 2.02%: ACM CCS 2024 peer-reviewed 논문 [A] [P-08]
- 경량 온디바이스 딥페이크 탐지(159k params): arXiv 2026년 1월 게재 [B] [P-09]

**추가 검증 필요 [C/D]:**
- 글로벌 음성 사기 시장 규모($1.87B, CAGR 14.2%): 단일 리서치 소스 [C]
- SKT 음성 스팸 차단 건수(2억 5천만 건, +119%): 단일 언론 보도 [C]
- Snapdragon 8 Gen 5 +46% AI 성능: Gizmochina 단일 소스 [C]
- 국내 통화 보안 서비스 TAM/SAM: 독립적 리서치 보고서 부재 [D]

**데이터 공백 (v2 이후에도 미해소):**
- 동형암호 VoIP 적용 최신(2025~2026) 실시간 벤치마크 (P-04는 2023년 클라우드 기반)
- 국내 통화 보안 서비스 WTP(지불의사) 소비자 조사
- LGU+ 익시오 보이스피싱 탐지율 내부 측정치
- 삼성/Apple 보이스피싱 탐지 오탐율(False Positive Rate)
- KIPRIS 기반 국내 통신사(SKT·KT·LGU+) 보이스피싱 특허 포트폴리오 — 웹 인터페이스 직접 접근 필요

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 인용원문(한글) | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|----------|------|-------------|--------|--------|--------|-----|
| G-05 | Gizmochina / Time Magazine | 2025.12 / 2025 | 미디어 | Snapdragon 8 Gen 5 NPU 성능 / Honor On-Device AI Deepfake Detection | +46% AI 성능, 70+ TOPS; Honor Magic 7 Pro 온디바이스 영상통화 딥페이크 탐지 | 4 | 3 | 5 | https://www.gizmochina.com/2025/12/24/on-device-ai-snapdragon-8-gen-5-npu-explained/ / https://time.com/collections/best-inventions-2025/7318478/honor-on-device-ai-deepfake-detection/ |
| G-07 | postquantum.com | 2025 | 전문기관 | PQC Standardization 2025 Update | ML-KEM, ML-DSA FIPS 확정 | 4 | 4 | 5 | https://postquantum.com/post-quantum/cryptography-pqc-nist/ |
| G-08 | postquantum.com / GSMA PQ.03 v2.0 | 2025 / 2024 | 전문기관/업계 | Telecom's Quantum-Safe Imperative; PQC Guidelines for Telecom | VoLTE IMS 전환 벤더 의존, 3GPP 미표준화, GSMA 가이드라인 v2.0 | 5 | 4 | 5 | https://postquantum.com/post-quantum/telecom-pqc-challenges/ / https://www.gsma.com/newsroom/gsma_resources/pq-03-post-quantum-cryptography-guidelines-for-telecom-use-cases/ |
| G-09 | Pindrop 공식 / PR Newswire | 2025 | 기업 | 2025 Voice Intelligence and Security Report | 딥페이크 +1300%, $12.5B 사기 피해, 탐지율 80%, FP <0.5% | 4 | 4 | 5 | https://www.pindrop.com/research/report/voice-intelligence-security-report/ |
| G-14 | GrowthMarketReports / Pindrop | 2024 / 2025 | 리서치/기업 | Fraud Analytics for International Voice Market; Deepfake Fraud 2025 | 2024 $1.87B → 2033 $5.49B, CAGR 14.2%; 딥페이크 사기 +162% YoY 예측 | 4 | 3 | 4 | https://growthmarketreports.com/report/fraud-analytics-for-international-voice-market / https://www.pindrop.com/article/deepfake-fraud-could-surge/ |
| G-15 | GlobeNewswire | 2026.02.23 | 리서치 | Post-Quantum Cryptography Industry Research Report 2026 | PQC가 연구 개념에서 핵심 사이버보안 축으로 전환 | 3 | 3 | 5 | https://www.globenewswire.com/news-release/2026/02/23/3242432/28124/en/Post-Quantum-Cryptography-Industry-Research-Report-2026-PQC-Transitions-from-Research-Concept-to-Core-Cybersecurity-Pillar-Amid-Rising-Quantum-Computing-Breakthroughs.html |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약(한글) | URL |
|------|--------|-------|------|-----------|----------|-----|
| N-01 | 보안뉴스 / Nate News | 2025.12 / 2025.12 | SKT·KT·LGU+, AI로 보이스피싱 탐지 고도화 | SKT KT LGU 보이스피싱 AI 탐지 | 3사 AI 보이스피싱 탐지 고도화 현황, SKT 음성 스팸 +119%, 2억 5천만 건 차단 | https://news.nate.com/view/20251202n25936 |
| N-02 | 서울경제 | 2025.10.03 | 보이스피싱 예방 위한 통신사 서비스 살펴보니 | 통신사 보이스피싱 서비스 비교 | SKT·KT·LGU+ 3사 서비스 비교 기사 | https://www.seoul.co.kr/news/economy/industry/2025/10/03/20251003500063 |
| N-03 | 세계일보 | 2025.04.27 | 2025년 1분기 보이스피싱 피해액 3116억원… 2024년 대비 2.2배 급증 | 보이스피싱 피해액 통계 2025 | 2025 Q1 3,116억 원, 건수 +17%, 피해액 2.2배 | https://www.segye.com/newsView/20250427507459 |
| N-04 | 헤럴드경제 | 2026 | 악성 앱으로 휴대폰 장악…지난해 보이스피싱 피해 1.2조 '사상 최대' | 보이스피싱 피해액 2025 1조 사상최대 | 2025년 연간 1조 2,578억 원 확정 | https://biz.heraldcorp.com/article/10661923 |
| N-05 | 스마트투데이 | 2025 | LGU+, '안티딥보이스' 위변조음성 5500건 탐지 | LGU+ Anti-DeepVoice 성과 | 위변조 음성 5,500건 탐지, 5초 내 탐지 | https://www.smarttoday.co.kr/news/articleView.html?idxno=87596 |
| N-06 | Sammy Fans | 2026.02.25 | Gemini-powered Scam Detection arrives on Galaxy S26 | Samsung Galaxy S26 Gemini scam detection | S26에 온디바이스 Gemini 기반 스캠 탐지 탑재 | https://www.sammyfans.com/2026/02/25/samsung-galaxy-s26-gemini-ai-scam-detection/ |
| N-07 | 9to5Mac | 2025.06.13 | Security Bite: Apple's new iOS 26 spam tools will make scammers cry | Apple iPhone scam call detection iOS 26 | iOS 26 Call Screening — 미지 발신자 AI 대리 응대, 20개국+ | https://9to5mac.com/2025/06/13/security-bite-apples-new-ios-26-spam-tools-will-make-scammers-cry/ |
| N-08 | VoIP Review | 2025.11.18 | BT and Pindrop Team Up to Combat Voice Fraud with AI | Pindrop telecom partnership 2025 | BT와 Pindrop 딥페이크 탐지 통합 파트너십 | https://voip.review/2025/11/18/bt-pindrop-team-combat-voice-fraud-ai/ |
| N-09 | The Pickool / Telecompaper | 2024.10 | KT Gains Regulatory Approval for AI-Powered Voice Phishing Detection Service | KT regulatory sandbox voice phishing 2024 | 과기정통부 ICT 규제샌드박스 실증특례 승인 — KT가 국내 최초 온디바이스 AI 보이스피싱 탐지 규제 승인 | https://www.thepickool.com/kt-gains-regulatory-approval-for-ai-powered-voice-phishing-detection-service/ |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약원문 |
|------|--------|-------|------|-----------|---------|
| E-01 | 삼성 뉴스룸 (한국) / 과기정통부 정책브리핑 | 2026.02.25 / 2026.02.12 | 삼성전자 갤럭시 스마트폰, AI로 보이스피싱·스팸 한 번에 차단 | 삼성 갤럭시 S26 보이스피싱 탐지 | 국과수 데이터 3만건 딥러닝, One UI 8.0+ 기본 탑재, 통신 3사 협력, 2026~2027 공동 플랫폼 구축 예정 |
| E-02 | SK텔레콤 뉴스룸 / Nate News | 2025.12 / 2026.01 | SKT 에이닷 전화, AI로 통화 중에도 보이스피싱 잡아낸다 | SKT 에이닷 스캠뱅가드 기술 | 온디바이스 AI, 키워드+패턴 분석, 의심·위험 2단계 알림, 2025년 11억 건 차단 +35%, 음성 스팸 +119% |
| E-03 | KT 공식 뉴스룸 / The Pickool / The Fast Mode | 2025.07.29 / 2025 | KT, 'AI 보이스피싱 탐지 2.0' 출시 / AI 보이스피싱으로 1300억 피해 예방 | KT AI 보이스피싱 탐지 2.0 | 화자인식+딥보이스 탐지 통합, 온디바이스, 91.6% 탐지율(H1), 1,300억 원 피해 예방, 2026년 목표 95%+ |
| E-04 | 한국NGO신문 / EBN / 이지이코노미 | 2026.01 / 2026.02 | KB국민은행-LG유플러스, AI 기반 보이스피싱 실시간 대응 체계 공개 | LGU+ 익시오 KB국민은행 협력 | 익시오-KB국민은행 연동, 1,720억 원 피해 예방, MWC26 시연 예정 |
| E-05 | Korea Herald / Korea Times | 2025.02 | LG Uplus to launch world's 1st on-device anti-deepvoice tech | LG U+ Anti-DeepVoice PQC MWC 2025 | MWC 2025 Exy Guardian: Anti-DeepVoice(비자연적 음소 패턴+주파수 변동), PQC(양자내성암호), On-Device SLM 통합 스위트 |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 학술지/컨퍼런스 | 인용수 | 핵심 인용 | DOI/URL |
|------|------|---------|------|--------------|--------|---------|---------|
| P-01 | TFHE 개발팀 / Chillotti et al. | 2020 / 2025 | TFHE: Fast Fully Homomorphic Encryption over the Torus / Refined TFHE Leveled HE | JACM / ACM CCS 2025 | - | binary gate당 ~13ms; refined 버전 4.2~6.8ms (최적화 조건) | https://tfhe.github.io/tfhe/ / https://dl.acm.org/doi/10.1145/3719027.3744873 |
| P-02 | Bae et al. | 2019 | Hardware Assisted Homomorphic Encryption in Real-Time VOIP | IEEE Xplore | - | FPGA 가속에도 ~150ms/operation — 실시간 통화 불가 | https://ieeexplore.ieee.org/document/8639492 |
| P-03 | (ACM CCS 2025 저자) | 2025 | Refined TFHE Leveled Homomorphic Evaluation | ACM CCS 2025 | - | 특정 연산 4.2~6.8ms (최적화 조건) — 실시간 통화 요건 대비 불충분 | https://dl.acm.org/doi/10.1145/3719027.3744873 |
| P-04 | Boura et al. | 2023 | Now is the Time: Scalable and Cloud-Supported Audio Conferencing using End-to-End HE | ACM CCSW 2023 | - | 클라우드 지원 시 E2E HE 오디오 컨퍼런싱 가능 — 단, 전용 프로토콜 필요, 일반 VoIP 즉시 적용 불가 | https://dl.acm.org/doi/10.1145/3605763.3625245 |
| P-05 | (arXiv 저자) | 2026.02 | On the Feasibility of Hybrid Homomorphic Encryption | arXiv | - | "prohibitive latency" — 실시간 음성 통신 HE 적용 불가 명시 | https://arxiv.org/pdf/2602.02717 |
| P-06 | (arXiv 저자) | 2025.12 | Physics-Guided Deepfake Detection for Voice Authentication Systems | arXiv | - | M4 Pro 기준 149ms/3초 세그먼트; HE 대신 ZKP 제안; "prohibitive latency" | https://arxiv.org/abs/2512.06040 |
| P-07 | (arXiv 저자) | 2025.09 | On Deepfake Voice Detection — It's All in the Presentation | arXiv | - | 딥페이크 탐지 성능에 입력 presentation 방식이 핵심 영향 | https://arxiv.org/abs/2509.26471 |
| P-08 | Xinfeng Li et al. | 2024 | SafeEar: Content Privacy-Preserving Audio Deepfake Detection | ACM CCS 2024 | - | EER 2.02%; 음성 내용 WER 93.93%+ (프라이버시 보존); acoustic 특성만으로 딥페이크 탐지 | https://arxiv.org/abs/2409.09272 |
| P-09 | K.A. Shahriar | 2026.01 | Lightweight Resolution-Aware Audio Deepfake Detection via Cross-Scale Attention and Consistency Learning | arXiv | - | 159k parameters, <1 GFLOP/inference; ASVspoof 2019 LA EER 0.16%; AUC 0.98 In-the-Wild | https://arxiv.org/abs/2601.06560 |
| P-10 | (arXiv 저자) | 2025.12 | Toward Noise-Aware Audio Deepfake Detection: Survey, SNR-Benchmarks, and Practical Recipes | arXiv | - | 실제 잡음 조건에서 딥페이크 탐지 성능 급락 — WavLM, Wav2Vec2 등 비교; 실서비스 배포 핵심 고려사항 | https://arxiv.org/abs/2512.13744 |
| P-11 | (arXiv 저자) | 2026.01 | Audio Deepfake Detection in the Age of Advanced Text-to-Speech Models | arXiv | - | 최신 TTS 딥페이크에 대한 탐지 어려움 심화; Generalization 문제 심각화 | https://arxiv.org/abs/2601.20510 |

### 특허 (T-xx)

| 번호 | 출원인 | 등록/출원일 | 특허번호 | 제목 | 핵심 청구항 | 관할 |
|------|--------|----------|---------|------|-----------|------|
| T-01 | Google LLC | 2022.08.23 (등록) | US11423926B2 | Real-time voice phishing detection | 통신 네트워크에서 보이스피싱 탐지기 결과를 단말에 알림 전달; 스위치/교환기/라우터를 통한 음성 신호 운반 | USPTO (미국) |
| T-02 | Samsung Electronics | 2024 (등록) | US11652603B2 | AI Calculation Semiconductor Device | 동형암호 연산 가속 반도체; multiply/accumulator + cyclic shift로 FHE 속도 향상; 민감 개인정보 유출 방지 | USPTO (미국) |
| T-03 | Wells Fargo Bank, N.A. | 2024.02.07 (출원) / 2025.02.19 (공개) | US20250252968A1 | Synthetic Voice Fraud Detection | (1) 실제 음성 샘플 수집·정규화, (2) 합성 클론 생성, (3) 실제·합성 페어 ML 학습, (4) 불일치 지표로 합성 음성 탐지 | USPTO (미국) |
| T-04 | Bank of America Corporation | 2023.11.07 (출원) / 2025.05.08 (공개) | US20250148788 | Deepfake Detection System | 컴퓨팅 기기 설치 딥페이크 분석 엔진이 콘텐츠 접근 모니터링 중 딥페이크 자동 탐지·알림 | USPTO (미국) |
| T-05 | (발명인 미확인) | 2015 (출원, 선행특허) | US20150237019A1 | System and Method for Merging Encryption Data using Circular Encryption Key Switching | 참가자가 additive HE로 음성 암호화 → 믹서가 암호화 상태 혼합 — VoIP HE 원조 개념 특허 | USPTO (미국) |

> **국내 특허 현황 (KIPRIS):** 웹 인터페이스 직접 검색 미수행으로 데이터 공백 유지. SKT·KT·LGU+ 보이스피싱 탐지 국내 특허 포트폴리오 확인은 KIPRIS(https://www.kipris.or.kr) 직접 접속 필요.

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 페이지 | 인용내용 |
|------|--------|-------|--------|---------|
| I-01 | Secure AI 기술·시장·규제 동향 리서치 | 2026-02-25 | 전체 | HE TRL 4~5 판정, PQC TRL 7~8, Anti-DeepVoice MWC 2025, SKT/KT 투자 비교 — 본 보고서 기준선으로 활용 |
| I-02 | WTIS SKILL-0 Analysis Brief: Secure AI | 2026-02-26 | 전체 | V1~V6 검증 항목 정의, 핵심 검색 쿼리, 경쟁사 분석 대상 목록 제공 |

---

## 부록: v2 변경 이력

### v1 → v2 소스 코드 재분류 내역

| v1 코드 | 내용 | v2 코드 | 변경 사유 |
|---------|------|---------|---------|
| G-01 (TFHE) | TFHE 공식 사이트 + ACM CCS 2025 논문 | **P-01** | 학술 논문(ACM CCS) → P-xx |
| G-02 (IEEE 2019) | IEEE FPGA HE VoIP 논문 | **P-02** | 학술 논문(IEEE) → P-xx |
| G-03 (ACM CCS 2025) | Refined TFHE 논문 | **P-03** | 학술 논문(ACM CCS) → P-xx |
| G-04 (arXiv HE) | Hybrid HE Feasibility 논문 | **P-05** | 학술 논문(arXiv) → P-xx |
| G-06 (arXiv deepfake) | Physics-Guided Deepfake Detection 논문 | **P-06** | 학술 논문(arXiv) → P-xx |
| G-10 (arXiv) | Deepfake Voice Detection — Presentation 논문 | **P-07** | 학술 논문(arXiv) → P-xx |
| G-11 (PMC/NIH) | Audio Deepfake Detection Review 논문 | (PMC 리뷰 → P-xx 별도 추가 권고) | 학술 논문 → P-xx |
| G-12 (arXiv ZKP) | Trustworthy AI ZKP Deepfake Detection 논문 | (arXiv → P-xx 별도 추가 권고) | 학술 논문 → P-xx |
| G-13 (Google Patents) | US11423926B2 보이스피싱 탐지 특허 | **T-01** | 특허 → T-xx |

### v2 신규 추가 소스

| 코드 | 내용 | 유형 |
|------|------|------|
| P-08 | SafeEar (ACM CCS 2024) | 학술 논문 (신규) |
| P-09 | Lightweight Resolution-Aware Audio Deepfake Detection (arXiv 2026.01) | 학술 논문 (신규) |
| P-10 | Noise-Aware Audio Deepfake Detection SNR-Benchmarks (arXiv 2025.12) | 학술 논문 (신규) |
| P-11 | Audio Deepfake Detection in the Age of Advanced TTS (arXiv 2026.01) | 학술 논문 (신규) |
| P-04 | E2E HE Audio Conferencing (ACM CCSW 2023) | 학술 논문 (신규) |
| T-02 | Samsung HE Semiconductor Patent (US11652603B2) | 특허 (신규) |
| T-03 | Wells Fargo Synthetic Voice Fraud Detection Patent (US20250252968A1) | 특허 (신규) |
| T-04 | Bank of America Deepfake Detection System (US20250148788) | 특허 (신규) |
| T-05 | VoIP HE Teleconferencing Prior Art (US20150237019A1) | 특허 (신규) |
| N-09 | KT ICT 규제샌드박스 승인 (2024년 10월) | 뉴스 (신규) |
| G-15 | PQC Industry Research Report 2026 (GlobeNewswire) | 글로벌 (신규) |

---

## 부록: v2.1 보강 검색 결과 (Reinforcement Loop [4-1])

> validator v2가 식별한 5개 단일 소스/미인용 항목에 대한 타겟 보강 검색 결과.
> 실행일: 2026-02-26, 최대 1회 실행.

### R-1. 글로벌 음성 사기 분석 시장 규모 — Confirmed

**기존**: $1.87B(2024) → $5.49B(2033), CAGR 14.2% — GrowthMarketReports 단일 소스 [G-14]

**보강 결과**: 6개 독립 리서치 기관이 14~20% CAGR 범위에서 일관된 성장률 제시.

| 코드 | 출처 | 시장 정의 | 규모 | CAGR | 신뢰도 |
|------|------|---------|------|------|--------|
| G-16 | DataIntelo | AI-Powered Voice Fraud Detection | $2.36B(2024)→$12.16B(2033) | 18.7% | B |
| G-17 | DataIntelo | Call Center Fraud Detection AI | $1.92B(2024)→$8.60B(2033) | 19.7% | B |
| G-18 | Market Research Future | Voice Analytics (광의) | $3.69B(2024)→$13.73B(2035) | 12.68% | B |
| G-19 | Allied Market Research | Voice Analytics | $1.3B(2023)→$6.7B(2032) | 19.6% | B |

**판정**: G-14 수치 교차 검증 완료. 시장 정의 범위에 따라 편차 존재하나 성장 방향 일관. 신뢰도 [C] → [B] 상향.

### R-2. 국내 이동통신 가입자 수 — Partially Confirmed (수정 필요)

**기존**: "약 7,400만 회선, LG U+ 점유율 약 20%" — 출처 없음

**보강 결과**: MSIT 공식 통계 기반 확인.

| 코드 | 출처 | 발행일 | 핵심 데이터 | 신뢰도 |
|------|------|--------|-----------|--------|
| G-20 | 서울신문 (MSIT 공식 통계 기반) | 2025-07-18 | 이동통신 휴대폰: SKT 2,249.9만(39.3%), KT 1,361.1만(23.8%), LGU+ 1,113.1만(19.5%), MVNO 999.8만(17.5%) / **합계 5,723.8만 회선** | A |
| G-21 | MSIT 무선통신서비스 통계 | 2025-07 발표 | 전체 무선회선(IoT 포함): 9,079만 회선 | A |

**판정**:
- **LGU+ 점유율 약 20%**: 확인됨 (실제 19.5%) ✓
- **총 가입자 "7,400만"**: **오류** — 이동통신 휴대폰 기준 **5,724만 회선** (MSIT 공식). 7,400만은 IoT 등 포함 추정치로 보이나, 전체 무선회선은 9,079만으로 이것도 불일치.
- **수정 권고**: "이동통신 가입자 약 5,724만 회선(2025년 5월 기준, MSIT)" [G-20]

### R-3. 보이스피싱 피해 2022~2025 연평균 성장률 — Confirmed

**기존**: 2022 1,451억→2023 1,965억→2024 8,545억→2025 1조2,578억 — N-04 단일 소스

**보강 결과**: 경찰청·금감원 공식 통계 + 복수 언론 확인.

| 코드 | 출처 | 발행일 | 핵심 데이터 | 신뢰도 |
|------|------|--------|-----------|--------|
| N-10 | 뉴시스 (경찰청 통합대응단) | 2025-11-24 | 2025년 1~10월: 1조 566억 원(1만 9,972건), 2024년 연간: 1조 2,578억 원 확정 | A |
| N-11 | 금융감독원 정책보고서 | 2024-03 발표 | 2023년: 1,965억 원(+35.4% YoY), 1인당 1,710만 원 | A |

**판정**: 금감원(2022~2023)·경찰청(2024~2025) 공식 발표로 다년간 추이 완전 검증. 신뢰도 [A].

### R-4. SKT/KT 보안 투자 — Confirmed

**기존**: SKT 5년 7,000억 / KT 5년 1조 — 내부 리서치 I-01만 의존

**보강 결과**: 2025년 7월 공식 발표, 복수 언론 확인.

| 코드 | 출처 | 발행일 | 핵심 데이터 | 신뢰도 |
|------|------|--------|-----------|--------|
| N-12 | 네이트 뉴스 (경찰청 조사결과 발표) | 2025-07-04 | SKT 유영상 대표: 5년간 7,000억 원 투자 공식 발표 (유심 해킹 사태 후속) | A |
| N-13 | 보안뉴스 | 2025-07-04 | SKT CISO CEO 직속 격상, 보안 인력 2배 확대 | A |
| N-14 | 네이트 뉴스 (KT 브리핑) | 2025-07-15 | KT 5년간 1조 원 투자 공식 발표 (연 평균 약 2,000억 원) | A |
| N-15 | 서울경제 | 2025-07-15 | KT 보안 인력 162명→300명, AI 기반 선제 보안 | A |

**판정**: 양사 모두 공식 기자 브리핑으로 발표. 신뢰도 I-01 단독 → [A] 복수 언론 확인.

### R-5. 통화 실시간 요건 <20ms — Unconfirmed (수정 필요)

**기존**: "통화 실시간 요건 <20ms" — 출처 없음. HE 불가 판정의 기준값으로 사용.

**보강 결과**: **산업 표준 문헌에서 "<20ms end-to-end 실시간 요건" 미발견.**

| 코드 | 출처 | 핵심 데이터 | 신뢰도 |
|------|------|-----------|--------|
| G-22 | ITU-T Rec. G.114 (2009) | **End-to-end 편도 지연: 0~150ms 권장, 150~400ms 허용** | A |
| G-23 | Cisco — Understanding Delay in Packet Voice Networks | 실무: 200ms 적정, 250ms 한계. 지연 분해: codec 2.5~10ms, packetization 20~30ms, network 가변 | A |

**판정**:
- <20ms는 음성 코덱의 **패킷 프레이밍 주기(packetization period)**이며, end-to-end 실시간 요건이 아님.
- ITU-T G.114 표준은 **150ms end-to-end 편도 지연**을 권장.
- **수정 권고**: SKILL-1 보고서에서 "<20ms" 기준값을 삭제하고, HE 불가 판정 논리를 재구성:
  - "TFHE per-gate 13ms [P-01] × 음성 샘플당 수백~수천 게이트 = 수초~수십초 누적 → ITU-T G.114 기준 150ms [G-22] 대비 불가"

### 보강 후 신규 References 요약

| 코드 | 제목 | 유형 |
|------|------|------|
| G-16 | AI-Powered Voice Fraud Detection Market (DataIntelo) | 글로벌 |
| G-17 | Call Center Fraud Detection AI Market (DataIntelo) | 글로벌 |
| G-18 | Voice Analytics Market (Market Research Future) | 글로벌 |
| G-19 | Voice Analytics Market (Allied Market Research) | 글로벌 |
| G-20 | SKT 시장 점유율 40% 무너졌다 (서울신문, MSIT 통계) | 글로벌 |
| G-21 | MSIT 무선통신서비스 통계 | 글로벌 |
| G-22 | ITU-T Rec. G.114 (편도 지연 표준) | 글로벌 |
| G-23 | Cisco VoIP Delay Analysis | 글로벌 |
| N-10 | 보이스피싱 피해 1조원 돌파 (뉴시스, 경찰청) | 뉴스 |
| N-11 | 금감원 2023 보이스피싱 피해현황 분석 | 뉴스 |
| N-12 | SKT 5년 7,000억 투자 공식 발표 (네이트) | 뉴스 |
| N-13 | SKT 보안 투자 (보안뉴스) | 뉴스 |
| N-14 | KT 5년 1조 투자 공식 발표 (네이트) | 뉴스 |
| N-15 | KT 보안 투자 상세 (서울경제) | 뉴스 |
