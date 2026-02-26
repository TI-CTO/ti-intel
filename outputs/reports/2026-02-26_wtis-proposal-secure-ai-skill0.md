# Analysis Brief: Secure AI

---
date: 2026-02-26
wtis_skill: SKILL-0
status: completed
proposal_version: v1.0
analyst: WTIS SKILL-0 (parser)
prior_research: 2026-02-25_research-secure-ai.md, 2026-02-23_wtis-standard-secureai-skill1.md
---

## 과제 개요

| 항목 | 내용 |
|------|------|
| 과제명 | Secure AI |
| 기술 도메인 | Security — 통화 보안 (B2C Voice Security) |
| LG U+ 택소노미 | Security > network security / on-device AI |
| 타겟 고객 | LG U+ 통화 서비스 이용 고객 (B2C, 일반 소비자) |
| Pain Point | 통화 중 개인정보 보안 위협 / 보이스피싱 금전 피해 |
| 현재 솔루션 | 통신사 네트워크 레벨 스팸 차단 (규칙 기반), 금융사 사후 피해 보상 — 실시간 AI 탐지는 미비 |
| 목표 KPI | 미지정 (제안서에 정량 KPI 없음) |
| 타임라인 | 미정 |
| 예산/규모 | 미지정 |
| 내부 참고 자료 | 없음 |

## 핵심 키워드

| 키워드 | 영문 | 카테고리 | 관련어 |
|--------|------|----------|--------|
| 양자암호화 | Quantum Cryptography / PQC | 암호 기술 | CRYSTALS-Kyber, ML-KEM, QKD, 양자내성암호 |
| 동형암호 | Homomorphic Encryption (HE) | 암호 기술 | FHE, CKKS, TFHE, 암호화 상태 연산 |
| 온디바이스 AI | On-device AI | AI/단말 | Edge AI, TinyML, on-device inference, NPU |
| 보이스피싱 탐지 | Voice Phishing Detection | AI 보안 | 딥페이크 음성, Anti-DeepVoice, 스캠 탐지 |
| 통화 보안 | Voice Call Security | 통신 보안 | VoLTE 보안, 통화 암호화, E2E Encryption |
| 실시간 탐지 | Real-time Detection | AI 추론 | Sub-second inference, 스트리밍 AI |

## 검증 필요 항목

| # | 주장 | 출처 | 검증 방법 |
|---|------|------|-----------|
| V1 | "국내 보이스피싱 피해액 급증 추세" | 미지정 | 경찰청/금감원 연도별 통계 확인. 최근 3~5년 추이 수치화 필요 |
| V2 | "통화 보안 서비스 수요 증가" | 미지정 | 시장 리서치 보고서 인용 근거 확인. TAM/SAM 규모 수치 필요 |
| V3 | 양자암호화가 통화 데이터 암호화에 실용적 | 미지정 | TRL 평가 필요. QKD vs PQC 구분, 단말-네트워크 연동 아키텍처 가능성 확인 |
| V4 | 동형암호로 실시간 통화 처리 가능 | 미지정 | HE 연산 지연(latency) 검증 필수. 현재 FHE는 수십~수백 ms → 실시간 통화(< 20ms) 요건과 충돌 가능성 높음 |
| V5 | OndeviceAI가 단말에서 실시간 보이스피싱 탐지 가능 | 미지정 | 현행 스마트폰 NPU 성능으로 음성 딥페이크 탐지 모델 실행 가능 여부, 배터리·메모리 제약 확인 |
| V6 | SKT·KT에 동일한 3중 조합 기술이 없음 (암묵적 주장) | 미지정 | SKT 스캠뱅가드 기술 스택 확인, KT AI 보이스피싱 탐지 2.0 상세 검토 |
| V7 | "고객 필수 서비스로 자리매김" 가능성 | 미지정 | 유료 전환율 벤치마크 필요. 무료/유료 구분 전략, WTP(지불의사) 조사 근거 없음 |

**핵심 기술 위험 플래그**: V4(동형암호 실시간 한계)는 제안서의 핵심 가정을 파괴할 수 있는 critical risk. 최우선 검증 필요.

## 경쟁 분석 대상

| 기업 | 티어 | 분석 포인트 |
|------|------|-------------|
| SKT | Tier 1 (항상) | 스캠뱅가드 기술 스택, PQC SIM 파일럿(Thales 협력), Anti-DeepVoice 여부 |
| KT | Tier 1 (항상) | AI 보이스피싱 탐지 2.0 상세 스펙, B2C 통화 보안 서비스 유료화 여부 |
| LG U+ (자사) | 자사 기준 | Anti-DeepVoice + PQC 기존 발표(MWC 2025)와 본 제안서 연계 관계 |
| Samsung / Apple | Tier 2 (단말) | 온디바이스 AI 보이스피싱 탐지 기능 탑재 여부 (OS 레벨 선점 위험) |
| Naver Cloud | Tier 2 (국내 AI) | 음성 AI 보안 솔루션, CLOVA 기반 사기 탐지 |
| V-Key / Pindrop | Global Startup | 통화 보안·음성 인증 전문 스타트업. 서비스 스펙 및 통신사 파트너십 현황 |
| Nuance (Microsoft) | Global Tier 2 | 음성 AI 사기 탐지 솔루션 (금융 대상), 통신사 적용 가능성 |

## 검색 전략

### 기술 트렌드

**한국어:**
- `동형암호 실시간 통화 처리 지연 성능 2025`
- `온디바이스 AI 보이스피싱 탐지 스마트폰 NPU`
- `양자암호화 5G VoLTE 통합 현황`
- `PQC 양자내성암호 스마트폰 통화 암호화 TRL`

**English:**
- `homomorphic encryption real-time voice call latency feasibility 2025`
- `on-device AI voice phishing detection smartphone NPU benchmark`
- `post-quantum cryptography VoLTE integration 3GPP 2025`
- `federated learning voice deepfake detection edge inference`

### 경쟁사

**한국어:**
- `SKT 스캠뱅가드 기술 스택 보이스피싱 탐지 방식`
- `KT AI 보이스피싱 탐지 2.0 상세 기능 2025`
- `삼성 갤럭시 사기 전화 탐지 온디바이스 AI`
- `LG U+ Anti-DeepVoice PQC MWC 2025 통화 보안`

**English:**
- `SKT Scam Vanguard voice phishing detection technical architecture`
- `telecom voice security on-device AI competitor landscape 2025`
- `Pindrop telecom voice fraud detection technology`
- `Apple Samsung on-device scam call detection feature 2025`

### 시장/투자

**한국어:**
- `국내 보이스피싱 피해액 통계 2023 2024 경찰청 금감원`
- `통화 보안 서비스 시장 규모 국내 2025`
- `보이스피싱 방지 서비스 유료화 통신사 사례`
- `통화 보안 스타트업 투자 유치 2024 2025`

**English:**
- `voice fraud telecom market size global 2025 CAGR`
- `voice phishing Korea financial damage statistics 2024`
- `secure voice call service monetization B2C telecom case study`
- `voice security startup funding investment 2024 2025`

### 특허/논문

**한국어:**
- `동형암호 음성통화 실시간 처리 특허`
- `보이스피싱 딥페이크 탐지 온디바이스 모델 논문`

**English:**
- `homomorphic encryption voice communication real-time site:arxiv.org`
- `on-device voice deepfake detection transformer lightweight model arxiv 2025`
- `post-quantum cryptography voice over LTE patent USPTO 2024 2025`
- `federated learning voice phishing detection telecom patent`

## 내부 자료 목록 (I-xx)

| 번호 | 자료명 | 파일경로 | 핵심 내용 요약 |
|------|--------|---------|--------------|
| I-01 | Secure AI 기술·시장·규제 동향 리서치 | `/Users/ctoti/Project/ClaudeCode/outputs/reports/2026-02-25_research-secure-ai.md` | 글로벌 AI 보안 시장($354B→$863B), SKT/KT 투자 비교, PQC TRL 7~8, HE TRL 4~5, Anti-DeepVoice MWC 2025 발표 |
| I-02 | WTIS SKILL-1 선정검증: SecureAI | `/Users/ctoti/Project/ClaudeCode/outputs/reports/2026-02-23_wtis-standard-secureai-skill1.md` | KPI 200억/50사 검증, 3B 전략(Buy+Build), HE Watch 판정, SKT/KT/Palo Alto 경쟁 현황 |
| I-03 | WTIS 최종 보고서: SecureAI | `/Users/ctoti/Project/ClaudeCode/outputs/reports/2026-02-23_wtis-standard-secureai-final.md` | 종합 전략 리포트 (확인 필요) |

**주의**: I-01/I-02는 이전 Secure AI 과제(AI 거버넌스·B2B 중심)와 부분 중복. 본 제안서는 **B2C 통화 보안**으로 포커스가 다름. 이전 HE Watch 판정(TRL 4~5)은 본 제안서 핵심 기술에 직접 영향.

## SKILL-1 입력 데이터

```yaml
project_name: "Secure AI"
domain: "Security > Voice Call Security (B2C)"
taxonomy_tags:
  - security
  - on-device-AI
  - quantum-crypto
  - homomorphic-encryption
  - voice-phishing-detection

target_customer:
  segment: "B2C"
  description: "LG U+ 통화 서비스 이용 일반 소비자"

pain_points:
  - "통화 중 실시간 보이스피싱 피해"
  - "통화 데이터 개인정보 유출"

core_technologies:
  - name: "양자암호화 (Quantum Cryptography / PQC)"
    role: "통화 데이터 암호화"
    claimed_trl: "미지정"
    known_trl: "PQC 알고리즘 TRL 7~8, 5G 통합 TRL 5~6 (I-01 기준)"
    risk: "low-medium"
  - name: "동형암호 (Homomorphic Encryption)"
    role: "암호화 상태에서 데이터 처리"
    claimed_trl: "미지정"
    known_trl: "TRL 4~5 (I-01, I-02 기준)"
    risk: "critical — 실시간 통화 지연 요건과 충돌 가능성"
  - name: "OndeviceAI"
    role: "단말 단에서 실시간 보이스피싱 탐지/차단"
    claimed_trl: "미지정"
    known_trl: "TRL 5~6 (음성 딥페이크 탐지), 단말 배포 TRL 4~5"
    risk: "medium"

differentiation_claimed:
  - "양자암호 + 동형암호 + OndeviceAI 3중 보안 조합"
  - uniqueness_verified: false

kpis: []  # 미지정

timeline: "미정"

competitors_known:
  domestic: ["SKT", "KT"]
  global: "에이전트 판단에 위임"

competitors_to_research:
  - {name: "SKT", priority: "high", focus: "스캠뱅가드 기술 스택, PQC 적용 범위"}
  - {name: "KT", priority: "high", focus: "AI 보이스피싱 탐지 2.0 상세"}
  - {name: "Samsung/Apple", priority: "high", focus: "OS 레벨 온디바이스 탐지 선점 위험"}
  - {name: "Pindrop", priority: "medium", focus: "글로벌 음성 보안 전문 스타트업"}
  - {name: "Nuance/Microsoft", priority: "medium", focus: "음성 AI 사기 탐지 솔루션"}

critical_claims_to_verify:
  - id: "V4"
    claim: "동형암호로 실시간 통화 데이터 처리"
    risk_level: "critical"
    reason: "FHE 현재 지연 수십~수백ms, 통화 실시간 요건 20ms 이하와 충돌"
  - id: "V5"
    claim: "온디바이스 AI 실시간 보이스피싱 탐지"
    risk_level: "high"
    reason: "단말 NPU 성능·배터리 제약, 모델 크기 vs 정확도 트레이드오프"
  - id: "V1"
    claim: "국내 보이스피싱 피해액 급증"
    risk_level: "medium"
    reason: "정량 수치·출처 없음. 경찰청/금감원 통계 필요"

prior_research_available: true
prior_research_files:
  - "outputs/reports/2026-02-25_research-secure-ai.md"
  - "outputs/reports/2026-02-23_wtis-standard-secureai-skill1.md"
focus_delta_vs_prior: "이전 과제는 B2B AI 거버넌스 중심. 본 제안서는 B2C 통화 보안으로 포커스 이동. HE 실시간 적용 가능성이 신규 핵심 이슈."
```

## 권장 분석

- **티어**: Deep
- **실행 스킬**: `research-deep` → `SKILL-1` → `validator`
- **특이사항**:
  1. **동형암호 실시간 한계 (Critical)**: FHE/TFHE의 현재 연산 지연이 실시간 통화 요건(< 20ms)을 충족하는지 최우선 검증. 불가 판정 시 제안서 핵심 기술 조합 재설계 필요.
  2. **Samsung/Apple 선점 위험 (High)**: iOS/Android OS 레벨에서 보이스피싱 탐지 기능 탑재 시 통신사 서비스의 차별화 근거 소멸. 2025~2026년 발표 여부 즉시 확인 필요.
  3. **이전 리서치 활용**: `2026-02-25_research-secure-ai.md`에 PQC TRL, Anti-DeepVoice, 경쟁사 투자 현황 등 상당량의 사전 데이터 존재. research-deep은 해당 파일을 베이스라인으로 활용하고 **B2C 통화 보안 갭 영역만 신규 조사** 권고.
  4. **KPI 부재**: SKILL-1 선정검증 시 KPI를 에이전트가 적합한 벤치마크로 제안해야 함 (예: 보이스피싱 탐지율, 오탐율, 서비스 가입 전환율, ARPU 영향).
  5. **Deep 권장 이유**: 3개 기술(PQC·HE·OndeviceAI)의 동시 통합은 구현 복잡도가 높고, B2C 통화 인프라 연동 아키텍처 검증이 필요하며, 기술 실현 가능성 리스크가 복수 존재함.
