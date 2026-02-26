# WTIS 선정검증: Secure AI — B2C 통화 보안

---
date: 2026-02-26
wtis_skill: SKILL-1
status: completed
analyst: WTIS SKILL-1 (feasibility)
input_skill0: 2026-02-26_wtis-proposal-secure-ai-skill0.md
input_research: 2026-02-26_wtis-proposal-secure-ai-research.md
scoring_framework: scoring-framework.md
verdict: Conditional Go
score: 128/200
confidence: Medium
---

## 경영진 요약

> **Conditional Go (128/200)** — Secure AI(B2C 통화 보안) 과제는 보이스피싱 피해 1조 2,578억 원(2025년) [N-04]이라는 명확한 시장 명분을 갖추고 있으나, 제안서 핵심 기술인 **동형암호(HE)의 실시간 통화 적용이 현재 기술로 불가능** [G-01, G-04]하며, **삼성 갤럭시 S26(2026.3)과 iOS 26이 OS 레벨에서 무료 보이스피싱 탐지를 기본 탑재** [E-01, N-07]하면서 통신사 독자 서비스의 차별화 공간이 급격히 좁아지고 있다. OndeviceAI 탐지는 이미 국내 3사 모두 상용화 완료(TRL 7~8)로 차별화 요소가 아니다. **PQC(양자내성암호) 기반 E2E 암호화 통화가 유일한 차별화 축**이나 VoLTE 통합 TRL 5~6으로 단기 상용화에 제약이 있다. Borrow(파트너십) + Build(PQC/Anti-DeepVoice 내재화) 혼합 전략을 권고하며, HE는 비실시간 용도로 범위를 재설계해야 한다. 신뢰도: Medium — 국내 독립 TAM/SAM 수치 부재, WTP 조사 미실시.

## 평가 항목 및 배점 안내

> 본 보고서는 WTIS 위닝테크 평가 체계(200점 만점, 5개 항목 각 40점)에 따라 정량 평가한다. 각 항목은 4개 세부 지표(각 10점)로 구성되며, 데이터 부족 항목은 중앙값(5점) 부여 후 "데이터 부족" 명시한다. 종합 판정: Go(160+) / Conditional Go(120~159) / 재검토(80~119) / No-Go(~79).

---

## 1. 목표 검증

### 1.1 SMART Test

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| **Specific** | **미흡** — 정량 KPI 미지정. "통화 보안 서비스"라는 방향은 있으나, 탐지율·가입자 수·매출 목표 등 구체 지표 부재 | [I-02] SKILL-0에서 "KPI: 미지정" 확인 |
| **Measurable** | **미흡** — 측정 가능한 목표 없음. 다만, 경쟁사 사례로 벤치마크 설정 가능: KT 93%+ 탐지율 [E-03], SKT 11억 건/년 차단 [E-02] | KT AI 탐지 2.0: 탐지율 93%+, 피해 예방 1,300억 원 [E-03] |
| **Achievable** | **조건부** — OndeviceAI 탐지는 달성 가능(TRL 7~8). 그러나 HE 실시간 적용은 **불가** [G-01, G-04], PQC VoLTE 통합은 TRL 5~6 [G-08] | HE per-gate 지연 13~26ms [G-01], 음성 스트림 누적 지연 초 단위 [G-04] |
| **Relevant** | **양호** — LG U+ '보안퍼스트' 전략(5년 7,000억 원 투자) [I-01], MWC 2025 Exy Guardian 발표 [E-05]와 일치. 보이스피싱 피해 1조 원 돌파라는 사회적 명분도 강력 [N-04] | LG U+ IT 투자 대비 보안 투자 비율 7.4%로 3사 중 최고 [I-01] |
| **Time-bound** | **미흡** — 타임라인 미정. 삼성 S26 출시(2026.3), 정부 공동 플랫폼(2026~2027) [E-01] 감안 시 **12개월 이내 시장 진입 필수**, 그 이후는 무료 대안 확산으로 유료화 공간 소멸 위험 | 삼성 S26 One UI 8.0+ 기본 탑재 [E-01], 과기정통부 공동 플랫폼 2026~2027 [E-01] |

**SMART 종합**: 5개 중 1개(Relevant)만 충족, 1개(Achievable) 조건부, 3개(Specific/Measurable/Time-bound) 미흡. **KPI 미지정은 가장 심각한 구조적 결함**으로, 추진 시 아래 벤치마크 KPI 설정을 선행 권고:

| 권고 KPI | 목표치 | 벤치마크 근거 |
|----------|--------|-------------|
| 보이스피싱 탐지율 | 95%+ (KT 2.0 목표 수준) | KT AI 탐지 2.0 [E-03] |
| 딥보이스(합성음) 탐지율 | 위변조 5초 내 탐지 | LGU+ 익시오 현행 [N-05] |
| 서비스 가입 전환율 | 익시오 사용자 중 30%+ | 데이터 부족 — 자체 추정 |
| 금융 연계 피해 예방액 | 2,000억 원+/년 | KT 1,300억 원/년 [E-03], LGU+ KB 1,720억 원 [E-04] |
| PQC 암호화 통화 PoC | 12개월 내 완료 | SoftBank/SKT+Thales 파일럿 [I-01] |

### 1.2 Market Sizing

**TAM (Total Addressable Market):**
- 글로벌 음성 사기 분석 시장: $1.87B(2024) → $5.49B(2033), CAGR 14.2% [G-14]
- 아시아태평양 동 시장: $520M(2024), CAGR 16.8% [G-14]
- 글로벌 Contact Center 사기 피해 규모: $12.5B/년(2024) [G-09]
- **국내 독립 TAM: 공개 리서치 부재** [데이터 부족]

**SAM (Serviceable Addressable Market) — 추정:**
- 한국 이동통신 가입자 약 7,300만 회선 (2025년 기준 추정)
- LGU+ 가입자 약 1,500만 회선 (~21% 점유율)
- 보이스피싱 직접 피해 규모: 1조 2,578억 원/년 [N-04] — 이 중 예방 가능 비율이 SAM의 상한
- **국내 통화 보안 서비스 유료화 TAM/SAM: 수치 산출 불가** — WTP 조사, 유료 전환율 데이터 부재 [데이터 부족]

**SOM (Serviceable Obtainable Market):**
- LGU+ 익시오 기반 KB국민은행 협력 모델: 1,720억 원 피해 예방 [E-04] → B2B 데이터 수익화 가능 규모
- B2C 유료 통화 보안: 삼성 S26 무료 탑재 [E-01], iOS 26 무료 제공 [N-07]으로 **유료 B2C SOM은 사실상 제한적**
- **현실적 SOM은 금융사 B2B 연계 수익 + PQC 프리미엄 니치 시장**

**Cross-check:** research-deep은 국내 독립 시장 수치를 "공개 정보 없음"으로 처리 [I-02]. 글로벌 시장 규모는 단일 리서치 소스(GrowthMarketReports)에 의존하여 신뢰도 [C] 수준.

---

## 2. 기술 성숙도 맵

### 4사분면 배치

```
                     High TRL (7~9)
                          │
                          │
   [유지]                 │          [베팅] ← Immediate review target
   PQC 알고리즘(TRL 7~8)  │          OndeviceAI 보이스피싱 탐지(TRL 7~8)
                          │          Anti-DeepVoice(TRL 6~7)
                          │
 ─────────────────────────┼──────────────────────────
                          │
   [탐색]                 │          [Watch]
   HE 실시간 통화(TRL 2~3)│          PQC VoLTE 통합(TRL 5~6)
   HE 알고리즘(TRL 4~5)   │          ZKP 딥페이크 탐지(TRL 3~4)
                          │          PQC E2E 단말 통합(TRL 4~5)
                          │
                     Low TRL (1~6)

        Low Disruption ←──────────→ High Disruption
```

### 기술별 상세 평가

| 기술 | TRL | Disruption | 사분면 | 근거 | 전략적 시사점 |
|------|-----|-----------|--------|------|-------------|
| **OndeviceAI 보이스피싱 탐지** | 7~8 | High | **베팅** | 국내 3사+삼성 상용화 완료 [E-01~E-04] | 이미 commodity화. 차별화 불가, 필수 기능으로 유지 |
| **Anti-DeepVoice** | 6~7 | High | **베팅** | LGU+ 5,500건 탐지 [N-05], KT 2.0 딥보이스 탐지 통합 [E-03] | LGU+ 선점 우위 존재하나 KT가 빠르게 추격 |
| **PQC 알고리즘** | 7~8 | Medium | **유지** | NIST FIPS 확정 [G-07], 파괴성 낮음(기존 암호 대체) | 표준화 완료. 적용 아키텍처가 과제 |
| **PQC VoLTE 통합** | 5~6 | High | **Watch** | SoftBank/SKT 파일럿 단계 [I-01], 3GPP 미표준화 [G-08] | **유일한 차별화 축** — 파일럿 가속 필요 |
| **PQC E2E 단말 통합** | 4~5 | High | **Watch** | 벤더 장비 업데이트 필요 [G-08] | 삼성/Apple 미지원. 장기 투자 항목 |
| **HE 알고리즘** | 4~5 | Medium | **탐색** | 이전 I-01/I-02 판정 유지 | 비실시간 용도로 범위 제한 |
| **HE 실시간 통화** | 2~3 | High | **탐색** | per-gate 13~26ms [G-01], "prohibitive latency" [G-04] | **현재 불가. 제안서 재설계 필수** |
| **ZKP 딥페이크 탐지** | 3~4 | High | **Watch** | HE 대안으로 arXiv 논문 입증 [G-12] | HE 대체 후보. 연구 모니터링 권고 |

**핵심 판정:**
1. **동형암호(HE)**: 제안서의 "3중 보안 조합" 중 HE는 실시간 통화에 적용 불가 [G-01, G-04]. TRL 2~3 수준으로 **탐색 사분면**. 비실시간(저장 통화 로그 분석, 메타데이터 처리)으로 용도 재정의하거나, ZKP [G-12]로 프라이버시 보존 기술을 대체해야 함.
2. **OndeviceAI**: 기술적으로 현실적이나(TRL 7~8), 국내 3사+삼성+Apple 모두 보유 → **commodity 기술**. 차별화 근거 소멸.
3. **PQC VoLTE E2E**: 경쟁사(SKT/KT/삼성/Apple) 모두 미탑재. **유일하게 차별화 가능한 기술축**.

---

## 3. 경쟁사 현황

### 3.1 경쟁사 비교표

| 경쟁사 | 유사 프로젝트 | 단계 | 타임라인 | 특허 | 투자 | 출처 |
|--------|-------------|------|---------|------|------|------|
| **SKT** | 스캠뱅가드 (ScamVanguard) + 에이닷 전화 | 상용화 | 2024~2025 상용, 연 11억 건 차단 | 공개 정보 없음 | 5년 7,000억 원 (전체 보안) | [E-02], [I-01] |
| **KT** | AI 보이스피싱 탐지 2.0 + 후후 | 상용화 (2.0 출시) | 2025.7 출시, 93%+ 탐지율 | 공개 정보 없음 | 5년 1조 원 (전체 보안) | [E-03], [I-01] |
| **Samsung** | 갤럭시 S26 Phone 앱 AI 탐지 | **2026.3 출시 예정** | One UI 8.0+ 기본 탑재 | 공개 정보 없음 | 국과수 데이터 3만건 학습 | [E-01], [N-06] |
| **Apple** | iOS 26 Call Screening | 출시 완료 (2025.9) | 20개국+ 확장 중 | 공개 정보 없음 | OS 내장, 추가 비용 없음 | [N-07] |
| **Pindrop** | Phoneprinting / 딥페이크 탐지 | B2B 상용화 | BT 파트너십 2025.11 | 다수 보유 (1,300개 음향 피처) | 비공개 | [G-09], [N-08] |
| **LGU+ (자사)** | 익시오 Anti-DeepVoice + PQC | 부분 상용 | MWC 2025 발표, MWC 2026 시연 예정 | 공개 정보 없음 | 5년 7,000억 원 (전체 보안) | [E-04], [E-05], [I-01] |

### 3.2 Gap Analysis — LGU+ 포지션 진단

**LGU+가 앞서는 영역:**
- **Anti-DeepVoice 세계 최초 상용화** (MWC 2025 발표) [E-05] — KT 2.0이 추격 중이나 LGU+가 6~12개월 선행
- **PQC + OndeviceAI 통합 발표** — 삼성/Apple/SKT/KT 모두 PQC 통화 보안 미탑재
- **금융사 연계 모델** — KB국민은행 협력 1,720억 원 피해 예방 [E-04], B2B 수익 경로 확보

**LGU+가 뒤처지는 영역:**
- **탐지율 공개 지표 부재** — KT는 93%+ 탐지율 공개 [E-03], SKT는 11억 건/년 차단 공개 [E-02]. LGU+는 정량 성과 미공개
- **삼성/Apple OS 무료 탑재** [E-01, N-07] — 통신사 앱 기반 서비스의 존재 이유를 위협하는 구조적 문제
- **투자 절대 규모** — KT 1조 원 대비 열위 [I-01]
- **가입자 기반** — 21% 점유율로 규모의 경제 불리

**구조적 위협 (2026~2027):**
- 과기정통부 'AI 보이스피싱 공동 대응 플랫폼' [E-01] 구축 시, 개별 통신사 독자 서비스 가치 희석
- **삼성 S26 + 통신 3사 앱 병렬 지원** [E-01] 구조에서 LGU+는 삼성의 생태계 하위 파트너로 포지셔닝될 위험

---

## 4. 3B 전략 분석

### 4.1 의사결정 변수 평가

| 변수 | 평가 | 근거 |
|------|------|------|
| **차별화 중요도** | 7/10 | OndeviceAI 탐지는 commodity [E-01~E-04]. PQC E2E 암호화만 차별화 가능 |
| **내부 역량** | Partial (O) | Anti-DeepVoice [E-05], ixi-GEN sLLM [I-01] 보유. PQC VoLTE 통합은 외부 벤더 의존 [G-08] |
| **시장 창(Market Window)** | < 12개월 | 삼성 S26(2026.3) [E-01], 공동 플랫폼(2026~2027) [E-01] |
| **시장 긴급도** | 8/10 | 피해 1조 원 돌파 [N-04], 삼성 무료화 임박 [E-01] |
| **기술 격차** | 영역별 상이 | OndeviceAI: 0년(동등), PQC VoLTE: 1~2년(SKT 파일럿 선행), HE: 불가 |

### 4.2 의사결정 로직 적용

```
IF (차별화 중요도 7/10 < 8) AND (시장 긴급도 8/10):
    → BORROW 우선 (파트너십/JV)

PQC VoLTE 통합: 시장 긴급도 High + 기술 격차 1~2년 → BUY or BORROW
Anti-DeepVoice/OndeviceAI: 내부 역량 보유 → BUILD (유지/강화)
HE 실시간: 불가 → WATCH (재설계 대기)
```

### 4.3 영역별 3B 판정

| 기술/영역 | 3B 판정 | 근거 |
|----------|---------|------|
| **OndeviceAI 보이스피싱 탐지** | **Build (유지)** | 이미 익시오 상용화 [E-04]. 탐지율 향상 + 삼성 협력 강화 집중 |
| **Anti-DeepVoice 고도화** | **Build** | 세계 최초 상용화 우위 [E-05]. 내재화하여 특허 확보 + 탐지 정확도 공개 |
| **PQC VoLTE E2E 암호화** | **Borrow** | Thales, IDQ(ID Quantique) 등 PQC 전문 벤더와 JV/파트너십. 벤더 장비 업데이트 필수 [G-08] |
| **PQC SIM 기술** | **Borrow** | SKT+Thales 선행 [I-01]. 동일 벤더(Thales)와 파트너십 또는 대안 벤더 탐색 |
| **금융사 연계 B2B** | **Build** | KB국민은행 모델 성공 [E-04] → 타 금융사 확장. LGU+ 내부 역량으로 가능 |
| **HE 실시간 통화** | **Watch** | TRL 2~3 [G-01, G-04]. 3~5년 후 재평가. 당장 투자 부적합 |
| **ZKP 프라이버시 보존** | **Watch** | HE 대안 후보 [G-12]. 학술 모니터링 + 소규모 PoC |

---

## 5. 최종 제언

```
[과제명]: Secure AI — B2C 통화 보안
[추천 방향]: Borrow + Build 혼합 (HE는 Watch)
[핵심 근거]:
  - 시장: 보이스피싱 피해 1조 2,578억 원/년 [N-04], 글로벌 음성 사기 시장 CAGR 14.2% [G-14]
         단, 삼성/Apple 무료 OS 탑재로 B2C 유료화 공간 축소 [E-01, N-07]
  - 기술: HE 실시간 불가(TRL 2~3) [G-01, G-04] → 제안서 핵심 가정 파괴
         PQC E2E 암호화가 유일한 차별화축(TRL 5~6, 경쟁사 미탑재) [G-08]
         OndeviceAI/Anti-DeepVoice는 commodity화 진행 중
  - 사업: KB국민은행 B2B 모델 1,720억 원 피해 예방 [E-04] → 금융 연계 수익화가 현실적 SOM
         PQC 프리미엄 통화(고보안 니치 세그먼트)로 B2C 차별화
[리스크]:
  - 삼성 S26 무료 탑재 (확률: H, 영향: H) — 2026.3부터 모든 갤럭시에 기본 제공 [E-01]
  - 정부 공동 플랫폼 (확률: H, 영향: H) — 2026~2027 구축 시 독자 서비스 가치 소멸 [E-01]
  - KT 탐지율 우위 (확률: H, 영향: M) — 93%+ 공개 vs LGU+ 미공개 [E-03]
  - PQC VoLTE 통합 지연 (확률: M, 영향: H) — 3GPP 미표준화 [G-08]
  - HE 기술 좌초 비용 (확률: L, 영향: M) — Watch 전환 시 매몰 비용 발생
[Next Action]:
  - [ ] 0~3개월: 제안서 재설계 — HE 실시간 통화 제거, PQC E2E + Anti-DeepVoice + 금융 B2B 3축으로 재구성
  - [ ] 0~3개월: PQC 벤더 쇼트리스트 (Thales, IDQ, PQShield 등) + 파트너십 협상 개시
  - [ ] 3~6개월: PQC VoLTE E2E 암호화 PoC (내부 망 + 삼성 단말 연동)
  - [ ] 3~6개월: 익시오 Anti-DeepVoice 탐지율 정량 공개 (KT 93%+ 대응)
  - [ ] 6~12개월: KB 모델 확장 — 타 시중은행 2~3사 추가 연동
  - [ ] 6~12개월: 정부 공동 플랫폼 참여 + 데이터 허브 역할 선점
  - [ ] 12~18개월: PQC 프리미엄 통화 서비스 파일럿 (기업 임원/VIP 세그먼트)
```

---

## 6. 3축 평가 근거

### 6.1 고객가치

| 구분 | 평가 | 근거 |
|------|------|------|
| **강점 1** | Pain Point 극도로 심각 | 보이스피싱 피해 2025년 1조 2,578억 원 [N-04], 1인당 평균 5,290만 원 [N-04]. 2024년 대비 +47% 급증. 생활 밀착형 공포 |
| **강점 2** | 금융 연계 즉시 대응 가치 | KB국민은행 연동으로 통화 중 탐지 → 즉시 계좌 정지 [E-04]. 피해 발생 전 차단이라는 고객가치가 명확 |
| **강점 3** | 개인정보 보호 (OndeviceAI) | 통화 내용 서버 미전송, 단말 내 완결 처리 [E-01, E-03, E-04]. GDPR/AI 기본법 규제 환경에서 프라이버시 우위 |
| **리스크 1** | 삼성/Apple 무료 대안 | 갤럭시 S26 기본 탑재 [E-01], iOS 26 Call Screening [N-07]. "왜 통신사 앱이 필요한가?" 질문 직면 |
| **리스크 2** | WTP(지불의향) 미검증 | 유료 전환율, 적정 가격대 조사 부재 [데이터 부족]. 경쟁사도 무료 포함 방식 |
| **리스크 3** | 탐지율 미공개 | KT 93%+ 공개 [E-03] 대비 LGU+ 익시오 탐지율 비공개. 고객 신뢰 확보 장애 |

### 6.2 사업포텐셜

| 구분 | 평가 | 근거 |
|------|------|------|
| **강점 1** | 피해액 기반 시장 명분 | 연간 1조 원+ 피해 [N-04]. 글로벌 음성 사기 시장 CAGR 14.2% [G-14], 아태 16.8% [G-14] |
| **강점 2** | 금융 B2B 수익 모델 실증 | KB국민은행 1,720억 원 피해 예방 [E-04]. 타 금융사 확장 시 데이터 서비스 수익 가능 |
| **강점 3** | 정부 정책 부합 | 과기정통부 'AI 10대 민생 프로젝트' 선정 [E-01]. 정책 지원 + 규제 우호적 환경 |
| **리스크 1** | B2C 유료화 불확실 | 삼성/Apple 무료 + 정부 공동 플랫폼 [E-01]. 유료 B2C SOM 제한적 |
| **리스크 2** | 국내 독립 TAM/SAM 부재 | 통화 보안 서비스 시장 규모 공개 리서치 없음 [데이터 부족] |
| **리스크 3** | 가입자 규모 열위 | LGU+ 21% 점유율, SKT/KT 대비 데이터 수집량 불리. AI 모델 학습 데이터 열세 |

### 6.3 기술경쟁력

| 구분 | 평가 | 근거 |
|------|------|------|
| **강점 1** | Anti-DeepVoice 세계 최초 | MWC 2025 발표 [E-05]. 비자연적 음소 패턴+주파수 변동 분석 기술 선점 |
| **강점 2** | PQC 통합 포지셔닝 | Exy Guardian 스위트(Anti-DeepVoice + PQC + SLM) [E-05]. 경쟁사 대비 유일한 PQC 통화 보안 포지션 |
| **강점 3** | On-Device SLM 역량 | ixi-GEN 소형 언어 모델 보유 [E-05]. 단말 내 보안 추론 아키텍처 실현 가능 |
| **리스크 1 (Critical)** | HE 실시간 불가 | FHE per-gate 13~26ms [G-01], 누적 지연 초 단위 [G-04]. "3중 보안 조합" 핵심 가정 파괴 |
| **리스크 2** | PQC VoLTE 미성숙 | TRL 5~6 [G-08], 3GPP 미표준화. 벤더 장비 의존. 상용화 12~24개월 소요 추정 |
| **리스크 3** | 딥페이크 일반화 문제 | 훈련 데이터 외 신규 합성음에 대한 탐지율 저하가 학계 공통 과제 [G-11] |

---

## 7. 정량 평가 (128/200)

### 1. 고객가치 (28/40)

| 세부 지표 | 점수 | 근거 |
|----------|------|------|
| Pain Point 심각도 | **9** | 피해 1조 2,578억 원 [N-04], 1인당 5,290만 원. 사회적 공포 수준 |
| 제공 가치 명확성 | **7** | OndeviceAI 탐지 + 금융 연동 대응 [E-04]은 명확하나, HE 기반 가치 제안 불가 [G-01] |
| 대체제 대비 우위 | **5** | 삼성 S26 무료 탑재 [E-01], iOS 26 [N-07], KT 93%+ [E-03]. PQC만 차별화 가능하나 고객 체감 약함 |
| 고객 수용성 | **7** | 익시오 앱 기반 배포 용이 [E-04]. 단, WTP 미검증 [데이터 부족], 무료 대안 존재 시 전환 저항 예상 |
| **소계** | **28** | 양호 등급 (25~32). Pain point는 극도로 강하나 대체제(삼성/Apple 무료) 때문에 우위 약화 |

### 2. 시장매력도 (25/40)

| 세부 지표 | 점수 | 근거 |
|----------|------|------|
| TAM/SAM/SOM | **5** | 글로벌 $1.87B→$5.49B [G-14]. **국내 독립 TAM 수치 부재** [데이터 부족]. 중앙값 부여 |
| 성장률 CAGR | **7** | 글로벌 CAGR 14.2%, 아태 16.8% [G-14]. 피해액 YoY +47% [N-04]. 성장 트렌드 확실 |
| 시장 타이밍 | **6** | 삼성 S26(2026.3) 무료화 임박 [E-01]. 유료 서비스 진입 window 12개월 미만. "약간 늦은" 타이밍 |
| 규제/정책 환경 | **7** | AI 기본법(2026.1) [I-01], 과기정통부 민생 프로젝트 [E-01]. 규제 우호적이나, 공동 플랫폼이 독자 서비스 약화 가능 |
| **소계** | **25** | 양호 등급 하한. 성장성은 확실하나 국내 시장 수치 부재와 무료화 압박으로 제한 |

### 3. 기술경쟁력 (26/40)

| 세부 지표 | 점수 | 근거 |
|----------|------|------|
| TRL 수준 | **6** | OndeviceAI TRL 7~8 [E-01~E-04], Anti-DeepVoice TRL 6~7 [E-05]. 그러나 HE TRL 2~3 [G-01]이 전체 조합의 TRL을 저해. PQC VoLTE TRL 5~6 [G-08] |
| 특허 포트폴리오 | **5** | LGU+ 보이스피싱 관련 특허 현황 공개 정보 없음 [데이터 부족]. Google 보유 특허 존재 [G-13]. Pindrop 다수 보유 [G-09] |
| 기술 장벽 | **7** | Anti-DeepVoice 세계 최초 상용화 [E-05] + PQC 통합 포지션은 모방에 12~18개월 소요 추정. 단, OndeviceAI 탐지 자체는 장벽 낮음 |
| 표준/인증 | **8** | PQC: NIST FIPS 확정 [G-07]. 3GPP 5G PQC 통합 논의 참여 [G-08]. 국제 표준 활용 가능 |
| **소계** | **26** | 양호 등급 (25~32). Anti-DeepVoice + PQC 조합은 강하나, HE 불가와 특허 불확실성이 감점 요인 |

### 4. 경쟁우위 (22/40)

| 세부 지표 | 점수 | 근거 |
|----------|------|------|
| 시장 포지션 | **5** | 3사 중 가입자 점유율 최저(21%). SKT CES/MWC 수상 [E-02], KT 93%+ 성과 [E-03] 대비 성과 지표 미공개 |
| 차별화 지속성 | **6** | Anti-DeepVoice 6~12개월 선점 [E-05], PQC 통합 유일. 그러나 KT 2.0 딥보이스 탐지 추격 [E-03], 삼성 무료화 [E-01]로 지속성 위협 |
| 경쟁사 대응력 | **5** | SKT/KT가 OndeviceAI 이미 보유 [E-02, E-03]. PQC는 SKT+Thales 선행 [I-01]. 차별화 방어 어려움 |
| 생태계/파트너 | **6** | KB국민은행 협력 실증 [E-04], MWC 2026 시연 [E-04]. 삼성 S26 통신 3사 병렬 지원 [E-01] 구조에서 LGU+ 배타적 우위 없음 |
| **소계** | **22** | 보통 등급 (17~24). 후발 + 소규모 포지션에서 PQC 차별화만으로 지속 우위 확보 어려움 |

### 5. 실행가능성 (27/40)

| 세부 지표 | 점수 | 근거 |
|----------|------|------|
| 내부 역량 | **7** | Anti-DeepVoice [E-05], ixi-GEN SLM [E-05], 보안 인력 292.9명(+86% YoY) [I-01]. PQC VoLTE는 외부 벤더 의존 |
| 투자 규모 대비 ROI | **6** | 5년 7,000억 원 전체 보안 예산 [I-01] 중 본 과제 배분 미정. KB 모델 1,720억 원 피해 예방 [E-04] → B2B 수익화 시 ROI 달성 가능성 |
| 일정 현실성 | **7** | OndeviceAI/Anti-DeepVoice: 이미 상용 [E-04]. PQC PoC: 12개월 내 가능(SKT/SoftBank 선례) [I-01]. HE 제거 시 일정 단축 |
| 리스크 관리 | **7** | HE → Watch 전환으로 critical risk 완화 가능. 삼성 협력 체계 기 확보 [E-01]. 금융 B2B 대안 경로 확보 [E-04] |
| **소계** | **27** | 양호 등급 (25~32). HE 제거 후 재설계 시 실행 가능성 상승. 내부 역량은 충분 |

### 종합 점수표

| # | 평가 항목 | 세부1 | 세부2 | 세부3 | 세부4 | 소계 |
|---|----------|-------|-------|-------|-------|------|
| 1 | 고객가치 | 9 (Pain Point) | 7 (가치 명확성) | 5 (대체제 우위) | 7 (수용성) | **28** |
| 2 | 시장매력도 | 5 (TAM/SAM) | 7 (CAGR) | 6 (타이밍) | 7 (규제) | **25** |
| 3 | 기술경쟁력 | 6 (TRL) | 5 (특허) | 7 (기술장벽) | 8 (표준) | **26** |
| 4 | 경쟁우위 | 5 (포지션) | 6 (지속성) | 5 (대응력) | 6 (생태계) | **22** |
| 5 | 실행가능성 | 7 (내부역량) | 6 (ROI) | 7 (일정) | 7 (리스크) | **27** |
| | **총점** | | | | | **128/200** |

### 종합 판정: **Conditional Go** (120~159)

128점은 Conditional Go 범위(120~159) 하단에 위치한다. 아래 보완 조건 충족 시 추진 가능:

**필수 보완 항목:**
1. **HE 실시간 통화 제거** — 제안서 핵심 가정 재설계. "3중 보안 조합"에서 HE를 비실시간 용도로 재정의하거나 ZKP로 대체 [G-01, G-04, G-12]
2. **KPI 설정** — 탐지율, 피해 예방액, PQC PoC 일정 등 SMART 목표 수립
3. **국내 TAM/SAM 산출** — WTP 소비자 조사 + 금융 B2B 시장 규모 정량화

**권고 보완 항목:**
4. 탐지율 정량 공개 — KT 93%+ [E-03] 대응 필요
5. PQC 벤더 파트너십 확정 — Borrow 전략 실행
6. 삼성 S26 협력 심화 전략 — OS 기본 탑재와 차별화되는 부가가치 정의

---

## 신뢰도: Medium

**근거:**

- **높은 확신 영역 [A]:** 동형암호 실시간 불가(복수 학술 논문) [G-01, G-04], 보이스피싱 피해 통계(경찰청·금감원) [N-04], 삼성 S26 탑재(삼성 뉴스룸+과기정통부) [E-01], iOS 26 Call Screening(Apple 공식) [N-07]
- **중간 확신 영역 [B]:** KT 탐지율 93%+(KT 뉴스룸·언론) [E-03], LGU+ Exy Guardian 스펙(복수 국제 언론) [E-05], SKT 11억 건 차단(SKT 뉴스룸) [E-02]
- **낮은 확신 영역 [C/D]:** 글로벌 시장 규모(단일 리서치 소스) [G-14], NPU 성능 수치(단일 미디어) [G-05]
- **데이터 공백:** 국내 통화 보안 TAM/SAM, WTP 조사, LGU+ 익시오 탐지율, 국내 통신사 특허 포트폴리오, 삼성/Apple 오탐율

**신뢰도를 Medium으로 판정한 이유:**
- 핵심 기술 판정(HE 불가, OndeviceAI 가능)은 높은 확신이나, 시장 규모와 수익성 판단의 핵심인 국내 TAM/SAM 및 WTP가 전면 부재
- 경쟁사 탐지율 비교에서 LGU+ 내부 데이터 없이 상대 비교 불가능
- 이 두 데이터 공백이 사업 포텐셜 평가의 신뢰도를 구조적으로 제한

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

| 번호 | 출처명 | 발행일 | 제목 | 요약(한글) | URL |
|------|--------|-------|------|----------|-----|
| N-01 | StarNews Korea | 2026.02.12 | Samsung Electronics, 3 mobile carriers detect voice phishing in real time | 삼성+통신 3사 온디바이스 AI 실시간 탐지 공동 제공 | https://www.starnewskorea.com/en/business-life/2026/02/12/2026021214210282736 |
| N-02 | 세계일보 | 2025.04.27 | 2025년 1분기 보이스피싱 피해액 3116억원… 2024년 대비 2.2배 급증 | 2025 Q1 3,116억 원, 건수 +17% | https://www.segye.com/newsView/20250427507459 |
| N-03 | 서울경제 | 2025.10.03 | 보이스피싱 예방 위한 통신사 서비스 살펴보니 | SKT/KT/LGU+ 3사 서비스 비교 | https://www.seoul.co.kr/news/economy/industry/2025/10/03/20251003500063 |
| N-04 | 헤럴드경제 | 2026 | 악성 앱으로 휴대폰 장악…지난해 보이스피싱 피해 1.2조 '사상 최대' | 2025년 연간 1조 2,578억 원 | https://biz.heraldcorp.com/article/10661923 |
| N-05 | 스마트투데이 | 2025 | LGU+, '안티딥보이스' 위변조음성 5500건 탐지 | 위변조 음성 5,500건 탐지, 5초 내 | https://www.smarttoday.co.kr/news/articleView.html?idxno=87596 |
| N-06 | Sammy Fans | 2026.02.25 | Gemini-powered Scam Detection arrives on Galaxy S26 | S26 온디바이스 Gemini 스캠 탐지 | https://www.sammyfans.com/2026/02/25/samsung-galaxy-s26-gemini-ai-scam-detection/ |
| N-07 | 9to5Mac | 2025.06.13 | Security Bite: Apple's new iOS 26 spam tools | iOS 26 Call Screening, 20개국+ | https://9to5mac.com/2025/06/13/security-bite-apples-new-ios-26-spam-tools-will-make-scammers-cry/ |
| N-08 | VoIP Review | 2025.11.18 | BT and Pindrop Team Up to Combat Voice Fraud with AI | BT-Pindrop 딥페이크 탐지 파트너십 | https://voip.review/2025/11/18/bt-pindrop-team-combat-voice-fraud-ai/ |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 요약원문 |
|------|--------|-------|------|---------|
| E-01 | 삼성 뉴스룸 / 과기정통부 | 2026.02 | 갤럭시 스마트폰 AI 보이스피싱 차단 | 국과수 3만건 딥러닝, One UI 8.0+ 기본, 통신 3사 협력, 공동 플랫폼 2026~2027 |
| E-02 | SKT 뉴스룸 / EBN | 2025~2026 | 에이닷 전화 보이스피싱 탐지 | 온디바이스 AI, 2025년 11억 건 차단 +35% |
| E-03 | KT 뉴스룸 / 전자신문 / 아주경제 | 2025 | AI 보이스피싱 탐지 2.0 | 화자인식+딥보이스, 93%+ 탐지율, 1,300억 원 피해 예방 |
| E-04 | 한국NGO신문 / EBN | 2026.01~02 | KB-LGU+ 보이스피싱 실시간 대응 | 익시오-KB 연동, 1,720억 원 피해 예방, MWC26 시연 |
| E-05 | Korea Herald / Korea Times | 2025.02 | LG U+ Anti-DeepVoice PQC MWC 2025 | Exy Guardian: Anti-DeepVoice+PQC+SLM 통합 스위트 |

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 인용내용 |
|------|--------|-------|---------|
| I-01 | Secure AI 기술·시장·규제 동향 리서치 | 2026-02-25 | HE TRL 4~5, PQC TRL 7~8, Anti-DeepVoice MWC 2025, 투자 비교, LGU+ 보안 비율 7.4% |
| I-02 | WTIS SKILL-0 Analysis Brief: Secure AI | 2026-02-26 | V1~V6 검증 항목, 경쟁사 분석, B2C 통화 보안 포커스 정의 |
