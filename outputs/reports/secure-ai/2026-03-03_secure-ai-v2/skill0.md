# Analysis Brief: Secure AI (v2 — post-pipeline refresh)

---
date: 2026-02-26
wtis_skill: SKILL-0
version: v2 (post-pipeline refresh)
status: completed
proposal_version: v2.0
analyst: WTIS SKILL-0 (parser)
prior_pipeline:
  - 2026-02-26_wtis-proposal-secure-ai-skill0.md (SKILL-0 v1)
  - 2026-02-26_wtis-proposal-secure-ai-research-v2.md (research-deep v2 + 부록 v2.1)
  - 2026-02-26_wtis-proposal-secure-ai-skill1-v3.md (SKILL-1 v3, Conditional Go 123/200)
  - 2026-02-26_wtis-proposal-secure-ai-skill1-v3-validator.md (validator: UNCERTAIN)
refresh_reason: "v1 파이프라인 완료 후, 제안서 v2 재제출에 따른 SKILL-0 재실행. validator UNCERTAIN(고아 인용 5건) 해소 목적 포함."
---

## 과제 개요

| 항목 | 내용 |
|------|------|
| 과제명 | Secure AI |
| 기술 도메인 | Security — B2C 통화 보안 (Voice Call Security) |
| LG U+ 택소노미 | Security > network security + AI/Data > on-device AI |
| 타겟 고객 | LG U+ 통화 서비스 이용 고객 (B2C, 일반 소비자) |
| Pain Point | (1) 통화 중 개인정보 보안 위협 (2) 보이스피싱·딥페이크 음성에 의한 금전적 피해 |
| 현재 솔루션 | 통신사 네트워크 레벨 스팸 차단(규칙 기반), 금융사 사후 피해 보상. 실시간 AI 탐지는 경쟁사(SKT 스캠뱅가드·KT AI 2.0) 등장 중 |
| 목표 KPI | 미지정 (제안서에 정량 KPI 없음) |
| 타임라인 | 미정 |
| 예산/규모 | 미지정 |
| 내부 참고 자료 | 없음 (Section 6 비어 있음) |

> **v2 변경점**: v1 SKILL-0 대비, 이전 파이프라인(research-deep v2, SKILL-1 v3, validator v3) 실행 결과를 반영하여 검증 필요 항목·경쟁 분석 대상·검색 전략을 갱신했다. 특히 validator가 UNCERTAIN으로 판정한 고아 인용 5건(G-17, G-18, G-19, G-21, G-23)이 발생한 원인인 "시장 데이터 보강 방향"을 명시적으로 검색 전략에 반영했다.

---

## 핵심 키워드

| 키워드 | 영문 | 카테고리 | 관련어 |
|--------|------|----------|--------|
| 양자암호화 | Post-Quantum Cryptography (PQC) / QKD | 암호 기술 | CRYSTALS-Kyber, ML-KEM, NIST PQC 표준, 3GPP PQC |
| 동형암호 | Homomorphic Encryption (HE / FHE) | 암호 기술 | TFHE, CKKS, Microsoft SEAL, Zama, 암호화 상태 연산 |
| 온디바이스 AI | On-device AI | AI / 단말 | Edge AI, TinyML, NPU, SafeEar, 경량 딥페이크 탐지 |
| 보이스피싱 탐지 | Voice Phishing / Scam Call Detection | AI 보안 | 딥페이크 음성, Anti-DeepVoice, 스캠 탐지, 합성 음성 |
| 통화 보안 서비스 | Voice Call Security Service | 통신 보안 | VoLTE 보안, E2E 통화 암호화, B2C 보안 ARPU |
| 실시간 음성 처리 | Real-time Voice Processing | AI 추론 | Sub-second inference, 스트리밍 AI, on-device SLM |
| 보이스피싱 시장 규모 | Voice Fraud Market Size / TAM | 시장 분석 | SAM, 보이스피싱 피해액, 경찰청 통계, 금감원 통계 |

---

## 검증 필요 항목

> **v2 갱신**: v1 V1~V7 항목을 유지하되, v3 validator UNCERTAIN 판정을 반영하여 각 항목의 검증 우선순위와 검증 방법을 갱신했다. 파이프라인에서 이미 확인된 사항은 "확인됨(검증완료)" 표시.

| # | 주장 | 출처 | 검증 방법 | v3 pipeline 상태 |
|---|------|------|-----------|-----------------|
| V1 | "국내 보이스피싱 피해액 급증 추세" | 미지정 | 경찰청·금감원 공식 연도별 통계 직접 확인. 2022~2025 연도별 추이 수치화. | **부분 확인** — 1조 2,578억(2025년) 확인, 그러나 N-04·N-10 연도 표기 불일치 발생. 공식 출처 재확인 필요 |
| V2 | "통화 보안 서비스 수요 증가" | 미지정 | 글로벌 음성 사기 탐지 시장 TAM 리서치 보고서 인용. G-14·G-16 교차 확인, G-17~G-19 고아 인용 해소 필요. | **부분 확인** — 글로벌 시장 $1.87B CAGR 14.2% 확인. 단 G-17·G-18·G-19 인용 활용 미완. |
| V3 | 양자암호화(PQC)가 통화 데이터 암호화에 실용적 | 미지정 | NIST PQC 표준(ML-KEM), 3GPP 5G PQC 통합 현황, TRL 평가. | **확인** — PQC TRL 5~6 (5G 파일럿 단계), PQC 알고리즘 TRL 7~8. 실용성 조건부 인정. |
| V4 | 동형암호로 실시간 통화 데이터 처리 가능 | 미지정 | FHE/TFHE 지연(ms) 측정값 vs ITU-T G.114 기준(150ms) 비교. Cisco 실무 기준(200~250ms) 보완. | **확인(Critical Risk)** — TFHE 13ms/gate, 실음성 처리 수초 이상. ITU-T 150ms 불가. 제안서 핵심 가정 파괴. G-22 단독 인용 → G-23 Cisco 기준도 본문 활용 필요. |
| V5 | OndeviceAI가 단말에서 실시간 보이스피싱 탐지 가능 | 미지정 | 경량 딥페이크 탐지 모델(159k params, <1 GFLOP) TRL 확인. 단말 NPU 성능·배터리·메모리 제약 검증. | **확인(조건부 가능)** — TRL 7~8 확인(P-09). 단 단말 제조사 OS 레벨 선점 위험(삼성 S26, iOS 26) 병렬 확인 필요. |
| V6 | SKT·KT에 동일한 3중 조합(PQC+HE+OndeviceAI) 기술이 없음 (암묵적 주장) | 미지정 | SKT 스캠뱅가드 기술 스택 상세, KT AI 보이스피싱 탐지 2.0 스펙. | **확인(HE 차별화 무의미)** — 경쟁사도 HE 미적용. HE 자체가 실시간 불가이므로 3중 조합 차별화 근거 소멸. |
| V7 | "고객 필수 서비스로 자리매김" 가능성 | 미지정 | 정부·통신 3사 공동 플랫폼(2026~2027년) 차별화 공간 재평가. WTP·ARPU 영향 벤치마크. | **미확인(고위험)** — 삼성 S26·iOS 26 OS 레벨 무료 탑재로 차별화 공간 축소 확인. 유료 ARPU 전환율 미확인. |

**v2 신규 추가 검증 항목:**

| # | 주장 | 검증 방법 |
|---|------|-----------|
| V8 | Call Center Fraud Detection AI 시장 $1.92B(2024)→$8.60B(2033) CAGR 19.7% (DataIntelo) | G-17 단일 소스 — 복수 시장 리서치 기관(Grand View, IDC 등) 교차 확인 필요. 고아 인용 해소 목적. |
| V9 | Voice Analytics 시장 $3.69B(2024)→$13.73B(2035) CAGR 12.68% (Market Research Future) | G-18 단일 소스 — 보완 리서치로 교차 확인 또는 본문 활용 방법 확정. |
| V10 | IoT 포함 무선 전체 회선 9,079만 (MSIT) vs 순수 휴대폰 5,724만 — TAM 산정 시 어느 기준 적용? | G-21 미활용 이유 명확화. 서비스 TAM(5,724만 통화 가입자) vs 전체 무선(9,079만) 구분 논거 수립. |

---

## 경쟁 분석 대상

> **v2 갱신**: v1 경쟁사 목록에 v3 pipeline에서 발견된 Wells Fargo(T-03 특허) 및 Zama(HE 스타트업) 추가.

| 기업 | 티어 | 분석 포인트 | v3 확인 상태 |
|------|------|-------------|-------------|
| SKT | Tier 1 (항상) | 스캠뱅가드 기술 스택, PQC SIM 파일럿(Thales 협력), 5년 7,000억 AI 보안 투자 | 투자 규모·스캠뱅가드 확인. 기술 스택 세부 미확인. |
| KT | Tier 1 (항상) | AI 보이스피싱 탐지 2.0 (91.6% 탐지율, 2025년 7월 출시), 5년 1조 투자 | 탐지율·출시일 확인. 단일 소스(KT 자사 발표) → 검증 필요. |
| LG U+ (자사) | 자사 기준 | 익시오(Exy Guardian): Anti-DeepVoice + PQC + On-Device SLM (MWC 2025 발표). 본 제안서와 중복·연계 관계 명확화. | MWC 2025 발표 확인. 1,720억 피해 예방 수치 단일 소스 경고. |
| Samsung | Tier 2 (단말 OS) | 갤럭시 S26 (2026년 3월) OS 레벨 무료 보이스피싱 탐지 내장 — 통신사 유료 서비스 차별화 위협 | **Critical Risk 확인**. S26 출시 후 서비스 포지셔닝 재검토 필요. |
| Apple | Tier 2 (단말 OS) | iOS 26 온디바이스 스캠 탐지 기능 탑재 여부 | v3 pipeline에서 부분 확인. 정확한 스펙·출시 시기 추가 확인 필요. |
| Pindrop | Global Startup | 통화 보안·음성 인증 전문. FP rate <0.5% 벤치마크. 통신사 파트너십 현황 | 성능 지표 확인. 국내 사업 진출 여부 미확인. |
| Nuance (Microsoft) | Global Tier 2 | 금융 대상 음성 AI 사기 탐지. 통신사 B2B 적용 가능성 | 미확인. 추가 조사 필요. |
| Wells Fargo | Global 금융사 | 합성 음성 사기 탐지 특허 US20250252968A1 (T-03) — 금융사가 통신사 우회 독자 특허 구축 시사 | **신규 발견(v2)**. 특허 상세 검토 필요. |
| Zama | HE 스타트업 | TFHE/CKKS 오픈소스 라이브러리. HE 실시간 성능 로드맵 확인 필요 | **신규 추가(v2)**. HE TRL 업데이트 목적으로 모니터링 필요. |

---

## 검색 전략

> **v2 갱신**: v1 쿼리를 유지하되, (1) validator UNCERTAIN의 고아 인용 해소용 쿼리, (2) Samsung S26/iOS 26 OS 레벨 탐지 최신 스펙 확인용 쿼리, (3) 수치-소스 불일치(+335% 폭증, 1인당 5,290만원) 해소용 쿼리를 신규 추가했다.

### 기술 트렌드

**한국어:**
- `동형암호 실시간 통화 처리 지연 성능 2025 2026`
- `온디바이스 AI 보이스피싱 탐지 스마트폰 NPU 경량 모델`
- `양자내성암호 PQC 5G VoLTE 통화 암호화 3GPP 2025`
- `TFHE FHE 실시간 음성 latency 최신 성능 개선`
- `SafeEar 프라이버시 보존 보이스피싱 탐지 아키텍처`

**English:**
- `homomorphic encryption real-time voice call latency TFHE CKKS 2025 2026`
- `on-device voice deepfake detection lightweight model NPU benchmark smartphone`
- `post-quantum cryptography VoLTE 3GPP integration TRL 2025`
- `federated learning voice phishing detection edge inference privacy-preserving`
- `NIST PQC ML-KEM deployment telecom network 2025`

### 경쟁사

**한국어:**
- `SKT 스캠뱅가드 기술 스택 양자암호 보이스피싱 탐지 상세`
- `KT AI 보이스피싱 탐지 2.0 탐지율 91.6% 검증 독립 평가`
- `삼성 갤럭시 S26 보이스피싱 탐지 기능 출시 사양 2026`
- `LG U+ 익시오 Anti-DeepVoice PQC MWC 2025 기술 상세`
- `iOS 26 사기 전화 탐지 온디바이스 기능 애플 2026`

**English:**
- `SKT Scam Vanguard voice phishing detection technical stack quantum PQC`
- `KT AI voice phishing detection 2.0 accuracy 91.6% independent verification`
- `Samsung Galaxy S26 on-device scam call detection feature specification 2026`
- `Apple iOS 26 scam call detection on-device AI feature 2026`
- `Pindrop telecom carrier partnership voice fraud detection deployment`

### 시장/투자 (v2 신규: 고아 인용 해소용)

**한국어:**
- `국내 보이스피싱 피해액 2022 2023 2024 2025 경찰청 금감원 공식 통계` *(V1·N-04·N-10 연도 불일치 해소)*
- `보이스피싱 1인당 피해액 5290만원 출처 경찰청 2025` *(수치-소스 불일치 V1 해소)*
- `보이스피싱 피해 증가율 335% 출처 연도 통계` *("+335% 폭증" 수치 출처 확인)*
- `통화 보안 서비스 시장 규모 TAM SAM 국내 통신사 가입자 2025`

**English:**
- `voice fraud telecom global market size 2024 2025 CAGR Grand View IDC MarketsandMarkets` *(G-17~G-19 교차 확인)*
- `call center fraud detection AI market size 2024 DataIntelo verification` *(G-17 단일 소스 검증)*
- `voice analytics market size 2024 2035 forecast multiple sources` *(G-18·G-19 교차 확인)*
- `South Korea voice phishing financial damage statistics 2022 2023 2024 2025 official`
- `secure voice call service monetization ARPU B2C telecom willingness to pay`

### 특허/논문

**한국어:**
- `동형암호 음성통화 실시간 처리 특허 KIPRIS 2024 2025`
- `보이스피싱 딥페이크 탐지 온디바이스 모델 논문 한국`

**English:**
- `homomorphic encryption voice communication real-time site:arxiv.org 2025 2026`
- `on-device voice deepfake detection lightweight transformer 159k parameters arxiv`
- `post-quantum cryptography voice over LTE patent USPTO 2024 2025`
- `Wells Fargo synthetic voice fraud detection patent US20250252968A1` *(T-03 상세 확인)*
- `Zama TFHE real-time voice performance roadmap 2025 2026` *(HE TRL 업데이트)*
- `SafeEar privacy-preserving voice phishing detection architecture paper`

---

## 내부 자료 목록 (I-xx)

> **v2 갱신**: 이전 v1 SKILL-0의 I-01~I-03에서, 실제 파이프라인 산출물(v2 research, v3 SKILL-1, validator v3)을 추가 등재.

| 번호 | 자료명 | 파일경로 | 핵심 내용 요약 |
|------|--------|---------|--------------|
| I-01 | Secure AI 기술·시장·규제 동향 리서치 (초기) | `/Users/ctoti/Project/ClaudeCode/outputs/reports/2026-02-25_research-secure-ai.md` | 글로벌 AI 보안 시장, PQC TRL 7~8, HE TRL 4~5, Anti-DeepVoice MWC 2025. B2B 중심 리서치. |
| I-02 | Research Report: Secure AI B2C 통화 보안 (v2) | `/Users/ctoti/Project/ClaudeCode/outputs/reports/2026-02-26_wtis-proposal-secure-ai-research-v2.md` | HE 실시간 불가(TFHE 13ms/gate), 삼성 S26 OS 레벨 탐지, 피해액 1조 2,578억, 경량 탐지 모델(159k params) TRL 7~8. P-xx/T-xx 분리 완료. |
| I-03 | WTIS SKILL-1 선정검증: Secure AI (v3, reinforcement loop) | `/Users/ctoti/Project/ClaudeCode/outputs/reports/2026-02-26_wtis-proposal-secure-ai-skill1-v3.md` | Conditional Go 123/200. HE Critical Risk 확인. 3B: Build(온디바이스) + Borrow(PQC). 권고 KPI: 탐지율 95%+, FP <1%, 지연 <5초. |
| I-04 | Validator Report (v3): Secure AI SKILL-1 v3 | `/Users/ctoti/Project/ClaudeCode/outputs/reports/2026-02-26_wtis-proposal-secure-ai-skill1-v3-validator.md` | UNCERTAIN. 고아 인용 5건(G-17, G-18, G-19, G-21, G-23). 수치-소스 불일치 2건. N-04·N-10 연도 표기 혼선. |
| I-05 | WTIS 이전 선정검증: SecureAI (표준 v1) | `/Users/ctoti/Project/ClaudeCode/outputs/reports/2026-02-23_wtis-standard-secureai-skill1.md` | KPI 200억/50사 검증(B2B), 3B 전략(Buy+Build), HE Watch 판정. 현 제안서(B2C)와 포커스 상이. |
| I-06 | WTIS 최종 보고서: SecureAI (표준 v1) | `/Users/ctoti/Project/ClaudeCode/outputs/reports/2026-02-23_wtis-standard-secureai-final.md` | 종합 전략 리포트(B2B AI 거버넌스 중심). 현 B2C 통화 보안 제안서와 포커스 이동 확인 참조용. |

**포커스 델타 (v2 갱신)**: I-01·I-05·I-06는 B2B/AI 거버넌스 중심이며 현 제안서(B2C 통화 보안)와 포커스가 상이하다. I-02·I-03·I-04가 현 제안서의 직접 선행 파이프라인 산출물이다. v2 SKILL-0의 검색 전략은 I-04(validator UNCERTAIN)에서 지적된 고아 인용 해소와 수치 검증에 특화되어 있다.

---

## SKILL-1 입력 데이터

```yaml
project_name: "Secure AI"
domain: "Security > Voice Call Security (B2C)"
taxonomy_tags:
  - security
  - on-device-AI
  - quantum-crypto (PQC)
  - homomorphic-encryption
  - voice-phishing-detection

target_customer:
  segment: "B2C"
  description: "LG U+ 통화 서비스 이용 일반 소비자 (5,724만 휴대폰 가입자 시장)"

pain_points:
  - "통화 중 실시간 보이스피싱·딥페이크 음성 피해 (1조 2,578억원, 2025년)"
  - "통화 데이터 개인정보 유출"

core_technologies:
  - name: "양자암호화 / PQC (Post-Quantum Cryptography)"
    role: "통화 데이터 암호화"
    claimed_trl: "미지정"
    pipeline_confirmed_trl: "PQC 알고리즘 TRL 7~8, 5G 통화 통합 TRL 5~6 (파일럿 단계)"
    risk: "low-medium"
    pipeline_status: "V3 확인 완료"

  - name: "동형암호 (Homomorphic Encryption / FHE)"
    role: "암호화 상태에서 데이터 처리"
    claimed_trl: "미지정"
    pipeline_confirmed_trl: "TRL 4~5. 실시간 통화(<150ms) 적용 현재 기술로 불가"
    risk: "critical — 제안서 핵심 가정 파괴"
    pipeline_status: "V4 Critical Risk 확인. 3중 조합에서 HE 제외 필요"

  - name: "OndeviceAI (On-device AI)"
    role: "단말 단에서 실시간 보이스피싱 탐지/차단"
    claimed_trl: "미지정"
    pipeline_confirmed_trl: "TRL 7~8 (경량 탐지 모델 기준). 단말 배포 TRL 5~6"
    risk: "medium — Samsung/Apple OS 레벨 선점 위협"
    pipeline_status: "V5 조건부 가능 확인. OS 레벨 선점 위험 추가 확인 필요"

differentiation_claimed:
  - "양자암호 + 동형암호 + OndeviceAI 3중 보안 조합"
  - uniqueness_verified: false
  - pipeline_finding: "HE 실시간 불가로 3중 조합 그대로 차별화 주장 불가. PQC E2E + 온디바이스 탐지 2중 조합으로 재설계 권고."

kpis: []  # 미지정 — SKILL-1 에이전트가 벤치마크 기반으로 제안해야 함
recommended_kpis:  # pipeline SKILL-1 v3 제안치
  - {kpi: "보이스피싱 탐지율", target: "95%+", benchmark: "KT 2.0 목표치"}
  - {kpi: "오탐율 (FP)", target: "<1%", benchmark: "Pindrop FP <0.5%"}
  - {kpi: "탐지 지연", target: "<5초", benchmark: "LG U+ 익시오 '5초 내 탐지'"}
  - {kpi: "연간 피해 예방액", target: "2,000억원+", benchmark: "KT 2.0 2026년 목표"}

timeline: "미정 — 단, 2026년 하반기 이전 서비스 미출시 시 시장 기회 상실 위험"

competitors_to_research:
  - {name: "SKT", priority: "high", focus: "스캠뱅가드 기술 스택 세부, PQC 적용 범위"}
  - {name: "KT", priority: "high", focus: "AI 탐지 2.0 탐지율 91.6% 독립 검증"}
  - {name: "Samsung", priority: "critical", focus: "S26 OS 레벨 무료 탐지 출시 일정·스펙"}
  - {name: "Apple", priority: "high", focus: "iOS 26 스캠 탐지 기능 탑재 여부·시기"}
  - {name: "Wells Fargo", priority: "medium", focus: "T-03 특허 US20250252968A1 상세 분석"}
  - {name: "Pindrop", priority: "medium", focus: "글로벌 음성 보안 스타트업, FP <0.5% 검증"}
  - {name: "Zama", priority: "low", focus: "TFHE 성능 로드맵, HE 실시간화 가능 시점"}

critical_claims_to_verify:
  - id: "V4"
    claim: "동형암호로 실시간 통화 데이터 처리"
    risk_level: "critical"
    pipeline_status: "CONFIRMED INFEASIBLE — TFHE 13ms/gate, 실음성 수초 누적. 재설계 필요."

  - id: "V7"
    claim: "고객 필수 서비스로 자리매김"
    risk_level: "high"
    pipeline_status: "UNCONFIRMED — 삼성 S26·iOS 26 무료 탑재로 차별화 공간 급축소."

  - id: "V1"
    claim: "국내 보이스피싱 피해액 급증"
    risk_level: "medium"
    pipeline_status: "PARTIAL — 1조 2,578억(2025) 확인. N-04·N-10 연도 표기 불일치 미해소."

  - id: "V8"
    claim: "콜센터 사기 탐지 AI 시장 $1.92B→$8.60B (DataIntelo)"
    risk_level: "medium"
    pipeline_status: "UNVERIFIED — G-17 단일 소스. 교차 확인 필요."

  - id: "V9"
    claim: "Voice Analytics 시장 $3.69B→$13.73B (MRF)"
    risk_level: "medium"
    pipeline_status: "UNVERIFIED — G-18 단일 소스. 교차 확인 필요."

validator_issues_to_resolve:
  orphaned_citations: ["G-17", "G-18", "G-19", "G-21", "G-23"]
  numeric_discrepancy: ["+335% 폭증 출처 미확인", "1인당 5,290만원 출처 미확인"]
  year_inconsistency: "N-04(헤럴드경제, 2026): 2025년 기준 vs N-10(뉴시스/경찰청): 2024년 기준 — 동일 수치 1조 2,578억원"

prior_research_available: true
prior_pipeline_version: "v3 (Conditional Go 123/200)"
focus_delta_vs_v1_skill0: |
  v1 SKILL-0 대비 v2의 주요 변경:
  1. validator UNCERTAIN 지적사항(고아 인용 5건, 수치 불일치 2건, 연도 혼선 1건)을 검증 항목(V8~V10) 및 검색 전략에 반영.
  2. Wells Fargo T-03 특허, Zama HE 스타트업을 경쟁 분석 대상에 추가.
  3. Samsung S26 OS 레벨 선점 위험을 Critical 등급으로 격상.
  4. 내부 자료 목록(I-xx)에 v2 research, v3 SKILL-1, validator v3 추가 등재.
  5. 권고 KPI(탐지율 95%, FP <1%, 지연 <5초, 피해 예방 2,000억)를 SKILL-1 입력에 포함.
```

---

## 권장 분석

- **티어**: Deep (v1 판정 유지)
- **실행 스킬**: `research-deep v3` → `SKILL-1 v4` → `validator v4`
- **특이사항 (v2 갱신)**:
  1. **validator UNCERTAIN 해소 최우선**: 고아 인용 5건(G-17~G-19, G-21, G-23)을 본문에 활용하거나 삭제. 수치 불일치(+335%, 1인당 5,290만원) 및 N-04·N-10 연도 혼선 해소.
  2. **동형암호 HE 재설계 확정 필요 (Critical)**: SKILL-1 v4에서 HE를 3중 조합에서 제외하고 "PQC E2E 통화 암호화 + 온디바이스 AI 탐지 2중 조합"으로 기술 재구성. HE는 미래 TRL 모니터링 항목으로 분류.
  3. **Samsung S26·iOS 26 선점 위험 (Critical)**: 2026년 3월 출시 S26 이후 서비스 포지셔닝 재설계. 니치 프리미엄(고보안 고객)·금융-통신 B2B 연계 모델 집중.
  4. **시장 데이터 교차 검증 (High)**: G-17(DataIntelo), G-18(MRF), G-19(Allied MR) 고아 인용 해소를 위해 Grand View Research·IDC 등 별도 시장 보고서 교차 확인.
  5. **권고 KPI 활용**: SKILL-1 v4는 v3에서 제안한 권고 KPI(탐지율 95%+, FP <1%, 지연 <5초, 피해 예방 2,000억)를 기준점으로 삼아 최종 평가표 작성.
  6. **Deep 유지 이유**: 기술 재설계(HE 제외) + 시장 포지셔닝 재설정 + validator 미해소 이슈 복합 존재. 표준(Standard) 티어로 하향 불가.
