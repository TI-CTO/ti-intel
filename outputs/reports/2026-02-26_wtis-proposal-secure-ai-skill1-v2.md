# WTIS 선정검증: Secure AI (v2 — 재테스트)

---
date: 2026-02-26
wtis_skill: SKILL-1
version: v2 (P-xx/T-xx retest)
confidence: Medium
status: completed
analyst: WTIS SKILL-1 (feasibility assessor)
input_sources:
  - 2026-02-26_wtis-proposal-secure-ai-skill0.md (SKILL-0)
  - 2026-02-26_wtis-proposal-secure-ai-research-v2.md (research-deep v2)
  - scoring-framework.md
---

## 경영진 요약

> **판정: Conditional Go | 총점: 122/200 | 신뢰도: Medium**
>
> Secure AI(B2C 통화 보안) 과제는 보이스피싱 피해액 1조 2,578억 원(2025년) [N-04]이라는 명확한 시장 명분과, 온디바이스 AI 딥페이크 탐지(TRL 7~8) [E-04, P-09]의 기술 기반을 갖추고 있다. 그러나 제안서의 핵심 기술 조합인 "양자암호 + 동형암호 + OndeviceAI 3중 보안"에서 동형암호(HE)의 실시간 통화 적용이 현재 기술로 불가능하다는 critical risk가 확인되었고 [P-01, P-02, P-05], 삼성 갤럭시 S26(2026년 3월)의 OS 레벨 무료 보이스피싱 탐지 [E-01]와 정부-통신 3사 공동 플랫폼(2026~2027) [E-01]이 독자 유료 서비스의 차별화 공간을 급격히 축소시킨다. **HE를 제외하고 PQC E2E 암호화 통화 + 프라이버시 보존 온디바이스 탐지(SafeEar 아키텍처 [P-08])로 기술 조합을 재설계할 경우**, 니치 프리미엄 시장(고보안 수요 고객)과 금융-통신 연계 B2B 모델(익시오-KB국민은행 확장 [E-04])에서 Conditional Go가 가능하다. 3B 전략: Build(온디바이스 탐지 고도화) + Borrow(PQC 네트워크 통합). 데이터 부족 항목이 3개 존재하여 신뢰도를 Medium으로 설정했다.

## 평가 항목 및 배점 안내

> 본 보고서는 WTIS 위닝테크 평가 체계(200점 만점, 5개 항목 각 40점)에 따라 정량 평가한다.
> 상세 기준: scoring-framework.md 참조.

---

## 1. 목표 검증

### 1.1 SMART Test

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| **Specific** | **미흡** — 제안서에 정량 KPI가 명시되지 않음. "통화 보안 서비스"의 범위(B2C 단독 vs B2B 포함), 목표 탐지율, 가입자 수 등 미정의. | SKILL-0 분석: "목표 KPI: 미지정, 타임라인: 미정, 예산/규모: 미지정" [I-02] |
| **Measurable** | **조건부 충족** — 탐지율, 오탐율, 서비스 가입 전환율 등 측정 가능한 지표가 존재하나, 제안서에서 명시하지 않음. KT가 91.6% 탐지율 [E-03], SKT가 11억 건 차단 [E-02] 등 경쟁사 벤치마크로 역설정 가능. | KT AI 탐지 2.0: 탐지율 91.6%(H1), 목표 95%+ [E-03] |
| **Achievable** | **기술 조건부** — 온디바이스 AI 탐지는 TRL 7~8로 즉시 실현 가능 [E-04, P-09]. PQC 통화 암호화는 TRL 5~6 파일럿 단계 [G-07, G-08]. **동형암호 실시간 적용은 불가** [P-01, P-02, P-05]. 3중 조합 중 HE 제외 시 실현 가능. | HE: per-gate 13ms~150ms [P-01, P-02], 통화 요건 <20ms 미충족 |
| **Relevant** | **충족** — LG U+ '보안퍼스트' 전략 [I-01], Exy Guardian 스위트(Anti-DeepVoice+PQC+SLM) MWC 2025 발표 [E-05]와 직접 연계. 보이스피싱 피해 1조 원 돌파 [N-04]로 사회적 긴급성 확인. | LG U+ Exy Guardian: Anti-DeepVoice + PQC + On-Device SLM [E-05] |
| **Time-bound** | **미충족** — 제안서에 타임라인 미지정. 경쟁사 참고: KT는 2025년 7월 2.0 출시 [E-03], 삼성 S26은 2026년 3월 [E-01], 정부 공동 플랫폼은 2026~2027년 구축 [E-01]. LG U+가 2026년 하반기~2027년 상반기에 서비스를 출시하지 못하면 시장 기회 상실. | 정부 공동 플랫폼 2026~2027 구축 [E-01]; KT 2.0 2025년 7월 출시 [E-03] |

**SMART 종합 판정: Fail (3/5 미충족)** — KPI, 타임라인, 예산 미지정으로 목표 객관성이 부족하다. 제안서 보완 시 아래 권고 KPI를 참조해야 한다.

**권고 KPI (에이전트 제안):**

| KPI | 목표치 | 벤치마크 근거 |
|-----|--------|-------------|
| 보이스피싱 탐지율 | 95%+ | KT 2.0 목표치 [E-03] |
| 오탐율 (False Positive) | <1% | Pindrop FP <0.5% [G-09] |
| 탐지 지연 | <5초 | LGU+ 익시오 "5초 내 탐지" [N-05] |
| 연간 피해 예방액 | 2,000억 원+ | KT 2.0 2026년 목표 [E-03]; LGU+ 익시오 1,720억 원(2025) [E-04] |
| B2B 금융 파트너 | 5개사+ | KB국민은행 선례 [E-04] |

### 1.2 Market Sizing

**TAM (Total Addressable Market):**

- **글로벌 음성 사기 분석 시장**: $1.87B(2024) → $5.49B(2033), CAGR 14.2% [G-14]
- **아시아태평양 음성 사기 분석**: $520M(2024), CAGR 16.8% [G-14]
- **글로벌 Contact Center 사기 피해**: $12.5B(2024) [G-09]
- **교차 확인**: GrowthMarketReports 단일 소스. Pindrop 리포트($12.5B 피해)는 시장 규모가 아닌 피해액으로 별도 카테고리 [G-09]. 독립 교차 확인 소스 부재 [C].
- **Counter-argument**: 글로벌 시장 규모는 B2B Contact Center 중심. B2C 통화 보안은 이 시장의 하위 세그먼트이며, 별도 규모 추정이 필요하나 공개 데이터 부재.

**SAM (Serviceable Available Market):**

- **국내 보이스피싱 피해**: 1조 2,578억 원(2025년) [N-04]. 이 피해액이 "방지 서비스" 수요의 근거.
- **국내 이동통신 가입자**: 약 7,400만 회선(2025 기준). LG U+ 점유율 약 20% = 약 1,480만 회선.
- **B2C 유료 통화 보안 서비스 독립 TAM/SAM**: `데이터 부족` — 공개 리서치 보고서 부재. 보강 키워드: `"Korea B2C voice security service market size"`, `"통화보안 유료서비스 시장규모 국내"`
- **Counter-argument**: 삼성 S26 무료 탑재 [E-01], 통신 3사 앱 무료 [E-02, E-03, E-04], Apple iOS 26 무료 [N-07]로 B2C 유료화 TAM이 극히 제한될 수 있음.

**SOM (Serviceable Obtainable Market):**

- 제안서 미지정. 에이전트 추정: LG U+ 가입자 1,480만 중 프리미엄 유료 전환율 1~3% 가정 시 14.8만~44.4만 명. 월 1,000~3,000원 가정 시 연간 약 178억~1,600억 원 범위.
- **이 추정은 유료 전환율(WTP) 소비자 조사 없이 산출한 것으로, 신뢰도 극히 낮음**. `데이터 부족` — 보강 키워드: `"LG U+ voice security ARPU"`, `"통화보안 유료서비스 전환율 WTP"`, `"mobile security premium subscription conversion rate Korea"` [D]

---

## 2. 기술 성숙도 맵

```
         High TRL (7~9)
              |
   [유지]     |     [베팅]
   PQC 알고리즘|     OndeviceAI 딥페이크 탐지 (TRL 7~8) ★
   (TRL 7~8)  |     SafeEar 프라이버시 보존 탐지 (TRL 6~7)
              |
--------------+----------------------------------------------
              |
   [탐색]     |     [Watch]
   HE(TRL 2~3|     PQC-VoLTE 통합 (TRL 5~6)
   실시간통화)|     ZKP 기반 프라이버시 보존 (TRL 4~5)
              |     경량 온디바이스 모델(159k params) (TRL 5~6)
         Low TRL (1~6)

   Low Disruption <-----> High Disruption
```

**배치 근거:**

| 기술 | TRL | 파괴성 | 사분면 | 근거 |
|------|-----|--------|--------|------|
| 온디바이스 AI 딥페이크 탐지 | 7~8 | High | **[베팅]** | 국내 3사+삼성 상용화 완료 [E-01~E-04]. 159k 파라미터 경량 모델 학술 검증 [P-09]. |
| SafeEar 프라이버시 보존 탐지 | 6~7 | High | **[베팅]** | ACM CCS 2024 peer-reviewed, EER 2.02% [P-08]. 프라이버시 차별화 기회. |
| PQC 알고리즘 (ML-KEM 등) | 7~8 | Medium | **[유지]** | NIST 표준 확정 [G-07], GSMA PQ.03 v2.0 가이드라인 [G-08]. 파괴성은 장기적. |
| PQC-VoLTE 통합 | 5~6 | High | **[Watch]** | SoftBank/SKT 파일럿 단계 [I-01]. 3GPP 미표준화 [G-08]. 2~3년 내 상용화 가능성. |
| ZKP 기반 프라이버시 보존 | 4~5 | High | **[Watch]** | arXiv [P-06]에서 HE 대안으로 제시. 실시간 구현 가능성 입증 초기 단계. |
| 경량 온디바이스 모델 (159k) | 5~6 | Medium | **[Watch]** | arXiv 2026년 1월 [P-09]. ASVspoof EER 0.16%. 실서비스 검증 미완. |
| 동형암호 (HE) 실시간 통화 | 2~3 | High | **[탐색]** | per-gate 13ms~150ms [P-01, P-02], "prohibitive latency" 명시 [P-05, P-06]. 통화 실시간 요건 미충족. |

**핵심 판정:** 제안서의 "3중 보안 조합" 중 동형암호(HE)는 [탐색] 사분면으로 현 시점 투자 부적합. **OndeviceAI [베팅] + PQC [유지/Watch]의 2중 조합으로 재설계 권고.**

---

## 3. 경쟁사 현황

### 3.1 경쟁사 비교표

| Competitor | Similar Project | Stage | Timeline | Patents | Investment | Source |
|------------|----------------|-------|----------|---------|------------|--------|
| **SKT** | 스캠뱅가드 + 에이닷 전화 (온디바이스 AI) | 상용화, 연간 11억 건 차단 | 2024~2025 상용 | PQC SIM(Thales 협력) 실증 [I-01] | 5년 7,000억 원 보안 투자 [I-01] | [E-02, N-01] |
| **KT** | AI 보이스피싱 탐지 2.0 (화자인식+딥보이스) | 상용화, 탐지율 91.6% | 2025년 7월 출시, 목표 95%+ | ICT 규제샌드박스 승인 [N-09] | 5년 1조 원 보안 투자 [I-01] | [E-03, N-09] |
| **LG U+ (자사)** | 익시오 Anti-DeepVoice + PQC + SLM | 상용화(Anti-DeepVoice), PQC 파일럿 | MWC 2025 발표, MWC 2026 시연 | Exy Guardian 스위트 [E-05] | 5년 7,000억 원 [I-01] | [E-04, E-05, N-05] |
| **삼성전자** | 갤럭시 S26 온디바이스 AI + Gemini 스캠 탐지 | 상용 출시 예정 | 2026년 3월 11일 | Google 보이스피싱 탐지 특허 [T-01] | 미공개 | [E-01, N-06] |
| **Apple** | iOS 26 Call Screening | 상용 출시 | 2025년 9월 | 미확인 | 미공개 | [N-07] |
| **Pindrop** | 음성 사기 탐지 (B2B Contact Center) | 글로벌 상용화, BT 파트너십 | 2025년 | 1,300개 음향 피처 엔진 [G-09] | 미공개 | [G-09, N-08] |
| **Honor** | Magic 7 Pro 온디바이스 딥페이크 영상통화 탐지 | 상용 출시 | 2025년 | 미확인 | 미공개 | [G-05] |

### 3.2 Gap Analysis

**LG U+ vs 경쟁사 핵심 갭:**

| 영역 | LG U+ 현재 | 경쟁사 최고 수준 | 갭 크기 | 출처 |
|------|-----------|----------------|---------|------|
| 탐지율 공개 | 미공개 | KT 91.6%(H1), 목표 95%+ | **High** — 탐지율 공개 경쟁에서 불리 | [E-03] |
| 연간 차단 규모 | 위변조 5,500건(H1) | SKT 11억 건/년 | **Very High** — 차단 규모 10만배+ 차이 (측정 기준 상이: LGU+는 딥보이스 특화, SKT는 전체 스팸/피싱 포함) | [N-05, E-02] |
| 피해 예방액 | 1,720억 원(KB국민은행 협력 포함) | KT 1,300억 원(단독), 목표 2,000억+ | **Low** — 금융 협력 모델로 이미 동등 수준 | [E-04, E-03] |
| PQC 통화 암호화 | Exy Guardian 스위트 발표 [E-05] | SKT PQC SIM 실증 [I-01] | **Medium** — 양사 모두 파일럿 단계 | [E-05, I-01] |
| OS 레벨 대응 | 삼성 S26과 협력 [E-01] | 삼성 S26 기본 탑재 무료 | **갭 아닌 공통 과제** — 3사 모두 OS 무료 탑재와 공존 과제 | [E-01] |
| 금융-통신 연계 | KB국민은행 (선두) | KT: 공개 사례 없음 | **LG U+ 우위** — KB국민은행 실시간 연동 선점 | [E-04] |

**핵심 시사점:**
1. 온디바이스 AI 탐지는 3사 모두 상용화 완료 — **기술 차별화 소멸** [E-01~E-04]
2. **삼성 S26 무료 탑재가 B2C 유료 서비스 모델의 최대 위협** [E-01]
3. LG U+의 유일한 선점 우위는 **KB국민은행 금융 연계 모델** [E-04]과 **PQC E2E 암호화** [E-05]

---

## 4. 3B 전략 분석

### 4.1 기술별 3B 의사결정 매트릭스

| 기술 영역 | 판단 | 긴급도 | 차별화 | 내부역량 | 근거 |
|----------|------|--------|--------|---------|------|
| 온디바이스 AI 딥페이크 탐지 | **Build** (고도화) | High (9/10) | Medium (경쟁사 동등) | High (익시오 운영 중) | 이미 Anti-DeepVoice 상용화 [E-05, N-05]. SafeEar [P-08] 아키텍처 적용으로 프라이버시 차별화 가능. 경량 모델(159k params) [P-09] 적용으로 배터리 효율 개선. |
| PQC E2E 통화 암호화 | **Borrow** | Medium (7/10) | High (경쟁사 미탑재) | Medium (Exy Guardian 발표, 실제 통합 미완) | NIST 표준 확정 [G-07], GSMA 가이드라인 존재 [G-08]. 3GPP 미표준화 상태에서 SoftBank/SKT 파일럿 참조 [I-01]. 칩셋 벤더(Qualcomm, Samsung)와 협력 필수. |
| 금융-통신 연계 플랫폼 | **Build** | High (9/10) | High (KB국민은행 선점) | High (익시오-KB 연동 완료) | KB국민은행 협력 모델 1,720억 원 피해 예방 [E-04]. Wells Fargo [T-03], Bank of America [T-04] 독자 특허 출원 트렌드를 고려 시, 국내 금융사와 공동 특허 선점 필요. |
| 동형암호 (HE) | **Watch** (투자 보류) | Low (2/10) | - | Low | 실시간 통화 불가 [P-01, P-02, P-05]. Samsung HE 가속 칩 특허 [T-02] 동향만 모니터링. 3~5년 후 재평가. |
| ZKP 기반 프라이버시 보존 | **Watch** → **Borrow** (장기) | Low~Medium (4/10) | High (경쟁사 미적용) | Low | arXiv [P-06]에서 HE 대안으로 제시. 현재 TRL 4~5. 학술 연구 추적 후 1~2년 내 Borrow 전환 검토. |

### 4.2 3B 종합 권고

**Build (핵심 역량 내재화):**
- 온디바이스 탐지 고도화 (SafeEar 아키텍처 + 경량 모델)
- 금융-통신 연계 플랫폼 확장 (KB국민은행 → 타 금융사)

**Borrow (외부 협력):**
- PQC 네트워크 통합 (칩셋 벤더·3GPP 표준화 협력)
- 정부 공동 플랫폼 참여 (과기정통부 AI 10대 프로젝트 [E-01])

**Watch (모니터링):**
- 동형암호 (HE) — Samsung HE 가속 칩 [T-02] 동향
- ZKP — arXiv 논문 추적 [P-06]

---

## 5. 최종 제언

### Recommendation Block

| 항목 | 내용 |
|------|------|
| **과제명** | Secure AI — B2C 통화 보안 (재설계안) |
| **판정** | **Conditional Go** |
| **추천 방향** | Build + Borrow (HE 제외, 2중 조합으로 전환) |
| **핵심 전제조건** | (1) HE 실시간 통화 적용 주장 철회, (2) 정량 KPI 설정, (3) B2C 유료화 WTP 검증 |

**핵심 근거:**

1. **시장 명분 강력**: 보이스피싱 피해 1조 2,578억 원(2025년) [N-04], 2024년 +335% 폭증. 사회적·정책적 긴급성 확인 [E-01].
2. **기술 기반 존재**: Anti-DeepVoice 이미 상용화 [E-05, N-05], 경량 모델(159k params) 학술 검증 [P-09], SafeEar 프라이버시 보존 탐지(EER 2.02%) [P-08].
3. **금융 연계 선점**: KB국민은행 협력 모델 1,720억 원 피해 예방 [E-04] — 타사 대비 유일한 실질적 차별화.
4. **PQC 유일 차별화**: PQC E2E 암호화 통화는 삼성·Apple·경쟁 통신사 모두 미탑재 [E-05, G-07].

**핵심 리스크:**

| 리스크 | 심각도 | 완화 전략 | 근거 |
|--------|--------|---------|------|
| 삼성 S26 + OS 레벨 무료 선점 | Critical | 무료와 공존 — 프리미엄(PQC 암호화+금융 연계)으로 차별화 | [E-01] |
| 정부 공동 플랫폼으로 독자성 희석 | High | 플랫폼 데이터 허브 역할 선점 — 분석·API 공급자 포지션 | [E-01] |
| B2C 유료화 WTP 미검증 | High | 출시 전 소비자 WTP 조사 필수. 무료 기본 + 프리미엄 유료(PQC) 프리미엄 모델 | [D] |
| KT 탐지율 공개 우위 (95%+ 목표) | Medium | 탐지율 공개 경쟁 참여 + "프라이버시 보존" 차별화 포지션 | [E-03, P-08] |
| 금융사 독자 특허 구축 (Wells Fargo 등) | Medium | KB국민은행과 공동 특허 출원으로 국내 금융사 이탈 방어 | [T-03, T-04] |
| 잡음 환경 탐지 성능 저하 | Medium | 실제 통화 잡음 조건 벤치마크 수행 [P-10], 강건성 개선 | [P-10] |

**Next Action (마일스톤):**

| 기간 | 액션 | 근거 |
|------|------|------|
| 0~3개월 | (1) 정량 KPI 확정 (탐지율 95%+, 오탐 <1%). (2) B2C WTP 소비자 조사 착수. (3) HE 실시간 적용 주장 철회 → PQC+OndeviceAI 2중 조합 재설계. | KT 2.0 벤치마크 [E-03]; HE 불가 [P-01, P-05] |
| 3~6개월 | (1) SafeEar [P-08] / 경량 모델 [P-09] 아키텍처 적용 PoC. (2) PQC E2E 암호화 통화 PoC (칩셋 벤더 협력). (3) KB국민은행 모델 → 2~3개 금융사 확장 협의. | [P-08, P-09, E-04] |
| 6~12개월 | (1) 정부 공동 플랫폼 참여 + 데이터 분석 허브 역할 확보. (2) PQC 암호화 통화 파일럿 (고보안 B2B 세그먼트 우선). (3) 삼성 S26 탑재 탐지 기능과 익시오 연동 최적화. | [E-01, G-08] |
| 12~18개월 | (1) B2C 프리미엄 서비스 정식 출시 (무료 기본 + PQC 유료). (2) 금융 연계 B2B 파트너 5개사+ 확보. (3) 탐지율·오탐율 공개 경쟁 참여. | [추정, 근거부족] [D] — 경쟁사 유사 서비스 출시-확장 타임라인 공개 데이터 부재. 보강 키워드: `"telecom voice security service launch timeline"`, `"통신사 보안서비스 출시 일정 사례"` |

---

## 6. 3축 평가 근거

### 고객가치

| 구분 | 내용 | 출처 |
|------|------|------|
| Pain Point 심각도 | 보이스피싱 피해액 2025년 1조 2,578억 원, 1인당 5,290만 원. 2024년 대비 +47%. 악성 앱 장악형 신종 수법 확산. | [N-04, N-03] |
| 제공 가치 | 실시간 온디바이스 AI 딥페이크 탐지(위변조 5초 내 식별) + PQC 양자내성 통화 암호화 | [N-05, E-05] |
| 대체제 현황 | 삼성 S26 무료 탑재 [E-01], Apple iOS 26 무료 [N-07], SKT 에이닷 무료 [E-02], KT 후후 무료 [E-03] — **무료 대체제 풍부** | [E-01, N-07] |
| 차별화 포인트 | (1) PQC E2E 암호화는 경쟁사 미탑재 [E-05]. (2) SafeEar 방식 프라이버시 보존 탐지 [P-08]. (3) 금융-통신 연계 실시간 계좌 정지 [E-04]. | [E-05, P-08, E-04] |
| Counter-argument | 무료 대체제가 "충분히 좋으면" 프리미엄 WTP 발생하지 않을 수 있음. PQC 암호화의 소비자 체감 가치 불확실. | 데이터 부족 [D] |

### 사업포텐셜

| 구분 | 내용 | 출처 |
|------|------|------|
| 글로벌 시장 규모 | 음성 사기 분석: $1.87B(2024) → $5.49B(2033), CAGR 14.2%. 아태 CAGR 16.8%. | [G-14] |
| 국내 피해 규모 (수요 근거) | 2025년 1조 2,578억 원. 2022~2025 연평균 성장률 +100%+. | [N-04] |
| 수익 모델 | (1) B2C 프리미엄 구독 (PQC 통화). (2) B2B 금융 데이터 서비스 (익시오-은행 연동 API). (3) 정부 플랫폼 분석 허브 계약. | [E-04, E-01] |
| 국내 B2C 유료 TAM | `데이터 부족` — 독립 리서치 보고서 부재. 보강 키워드: `"Korea B2C mobile security subscription market"`, `"통화보안 프리미엄 서비스 시장규모"` | [D] |
| 규제 환경 | 정부 적극 지원: AI 10대 민생 프로젝트 [E-01], ICT 규제샌드박스 [N-09]. 보이스피싱 방지법 강화 추세. | [E-01, N-09] |
| Counter-argument | 정부 공동 플랫폼 완성 시(2027년), 개별 통신사 독자 서비스의 수익 공간 축소 가능성. 금융사 자체 특허 구축 시 [T-03, T-04] B2B 모델 약화. | [E-01, T-03] |

### 기술경쟁력

| 구분 | 내용 | 출처 |
|------|------|------|
| 온디바이스 AI 탐지 TRL | TRL 7~8 (상용). LGU+ Anti-DeepVoice 5,500건 탐지(H1), 5초 내 식별. | [E-05, N-05] |
| PQC TRL | 알고리즘 TRL 7~8. VoLTE 통합 TRL 5~6. 단말 E2E TRL 4~5. | [G-07, G-08, I-01] |
| HE TRL (실시간 통화) | TRL 2~3. **불가 판정.** per-gate 13ms~150ms, "prohibitive latency". | [P-01, P-02, P-05] |
| 학술 기반 | SafeEar EER 2.02% [P-08], 경량 모델 159k params EER 0.16% [P-09] — 온디바이스 배포 학술 검증 완료. | [P-08, P-09] |
| 특허 포트폴리오 | Google 보이스피싱 탐지 [T-01], Samsung HE 가속 [T-02] 등 해외 선행 특허 존재. **LGU+ 국내 특허 현황 미확인** — KIPRIS 검색 필요. | [T-01, T-02] |
| 잡음 환경 강건성 | 실제 통화 잡음에서 탐지 성능 급락 문제 확인 [P-10]. 최신 TTS 딥페이크 대응 Generalization 문제 [P-11]. | [P-10, P-11] |
| Counter-argument | 온디바이스 탐지는 3사+삼성 모두 보유 — 기술 자체로는 차별화 불가. PQC 통합은 칩셋 벤더 의존도 높아 LGU+ 독자 기술 장벽 구축 어려움. | [E-01~E-04, G-08] |

---

## 7. 정량 평가 (122/200)

### 1. 고객가치 (28/40)

| 세부 지표 | 점수 | 근거 |
|----------|------|------|
| Pain Point 심각도 | **9/10** | 2025년 피해 1조 2,578억 원, 1인당 5,290만 원 [N-04]. 2024년 +335% 폭증 [N-03]. 사회적 긴급성 최고 수준. |
| 제공 가치 명확성 | **8/10** | 실시간 딥페이크 탐지 + PQC 암호화의 기술적 가치는 명확 [E-05, N-05]. 단, HE 제거 후 "3중 보안" 포지션 약화. |
| 대체제 대비 우위 | **5/10** | 삼성 S26 무료 [E-01], Apple iOS 26 무료 [N-07], SKT/KT 무료 [E-02, E-03]. PQC 암호화만 유일한 차별화이나 소비자 체감 불확실 [D]. |
| 고객 수용성 | **6/10** | WTP 소비자 조사 미실시 [D]. 무료 대체제 풍부 환경에서 프리미엄 전환 저항 예상. 금융 연계 모델 [E-04]은 B2B 수용성 높음. |

### 2. 시장매력도 (26/40)

| 세부 지표 | 점수 | 근거 |
|----------|------|------|
| 시장 규모 TAM/SAM/SOM | **6/10** | 글로벌 TAM $1.87B [G-14]. 국내 B2C 유료 TAM 데이터 부재 [D]. 피해액 1조 원이 수요 근거이나, "수요=유료 시장"은 아님. |
| 성장률 CAGR | **7/10** | 글로벌 CAGR 14.2%, 아태 16.8% [G-14]. 국내 피해액 2022~2025 연평균 +100%+로 수요 급증 [N-04]. 단일 리서치 소스 [C]. |
| 시장 타이밍 | **7/10** | 2026~2027년이 적절한 진입 시점. 삼성 S26 [E-01], 정부 플랫폼 [E-01], KT 2.0 [E-03]과 동시 활성화. 단, 너무 늦으면 플랫폼 주도권 상실. |
| 규제/정책 환경 | **6/10** | 정부 AI 10대 민생 프로젝트 적극 지원 [E-01]. KT 규제샌드박스 승인 선례 [N-09]. 단, 정부 공동 플랫폼이 독자 서비스를 희석할 양면성. |

### 3. 기술경쟁력 (25/40)

| 세부 지표 | 점수 | 근거 |
|----------|------|------|
| TRL 수준 | **7/10** | 온디바이스 TRL 7~8 [E-04], PQC 알고리즘 TRL 7~8 [G-07]. 단, PQC-VoLTE 통합 TRL 5~6 [G-08], HE TRL 2~3 [P-01]. 가중 평균 TRL 5~6. |
| 특허 포트폴리오 | **5/10** (데이터 부족) | LGU+ 국내 특허 포트폴리오 미확인. Google [T-01], Samsung [T-02] 해외 선행 특허 존재. KIPRIS 검색 필요. 보강 키워드: `"LG유플러스 보이스피싱 탐지 특허"`, `"KIPRIS 양자암호 통화 보안 특허"` |
| 기술 장벽 | **6/10** | 온디바이스 탐지는 3사+삼성 모두 보유 — 장벽 낮음 [E-01~E-04]. PQC E2E 통화는 칩셋 벤더 협력 필요 — 모방 장벽 중간. SafeEar 적용 시 프라이버시 장벽 구축 가능 [P-08]. |
| 표준/인증 | **7/10** | NIST PQC 표준 확정 [G-07], GSMA PQ.03 v2.0 [G-08]. 3GPP 미표준화 [G-08]. KT 규제샌드박스 승인 선례 — LGU+도 동일 경로 활용 가능 [N-09]. |

### 4. 경쟁우위 (20/40)

| 세부 지표 | 점수 | 근거 |
|----------|------|------|
| 시장 포지션 | **5/10** | 온디바이스 탐지는 3사 동등 [E-01~E-04]. PQC는 SKT도 파일럿 [I-01]. KB국민은행 금융 연계만 선발 [E-04]. 전체적으로 동등~후발. |
| 차별화 지속성 | **5/10** | PQC E2E 암호화 차별화 가능 기간: SKT/KT가 파일럿 완료 시까지 약 1~2년 [추정, 근거부족] [D]. SafeEar 프라이버시 포지션은 경쟁사 모방 용이(오픈 논문). 금융 연계 선점 효과는 파트너 확대 속도에 의존. 보강 키워드: `"PQC telecom deployment timeline competitor"`, `"양자내성암호 통신사 상용화 일정"` |
| 경쟁사 대응력 | **4/10** | SKT 7,000억 [I-01], KT 1조 원 [I-01] 보안 투자 — LGU+와 동등~우위. 삼성 S26 OS 레벨 무료 선점 [E-01]. 경쟁사 대응 속도 빠름. |
| 생태계/파트너 | **6/10** | KB국민은행 실시간 연동 [E-04] = 금융 생태계 선점. MWC 2026 시연 [E-04]. 정부 공동 플랫폼 참여 예정 [E-01]. 단, SKT IBK 기업은행 파트너십 [E-02]도 확대 중. |

### 5. 실행가능성 (23/40)

| 세부 지표 | 점수 | 근거 |
|----------|------|------|
| 내부 역량 | **7/10** | Anti-DeepVoice 상용화 완료 [E-05], 익시오 운영 중 [N-05], ixi-GEN SLM 보유 [I-01]. PQC 역량은 Exy Guardian 발표 수준 [E-05]. |
| 투자 규모 대비 ROI | **5/10** (데이터 부족) | 예산 미지정(제안서). B2C 유료 수익 모델 WTP 미검증 [D]. B2B 금융 연계 수익은 KB 사례로 가능성 확인 [E-04]. 정확한 ROI 산출 불가. 보강 키워드: `"telecom voice security service ROI case study"`, `"통화보안 서비스 투자수익률 사례"` |
| 일정 현실성 | **6/10** | 온디바이스 탐지 고도화는 6개월 내 PoC 가능 (기존 역량 활용). PQC 통합은 칩셋 벤더 의존으로 12~18개월 필요 — SoftBank/SKT 파일럿 참조 [I-01]. 정부 플랫폼 2026~2027 일정과 동기화 필요 [E-01]. |
| 리스크 관리 | **5/10** | HE 불가 리스크 식별 완료 [P-01, P-05]. 삼성 S26 무료 리스크 식별 [E-01]. 단, WTP 미검증·금융사 이탈 리스크에 대한 완화 전략이 제안서에 미포함. |

### 종합 점수표

| # | 평가 항목 | 점수 | 등급 |
|---|----------|------|------|
| 1 | 고객가치 | **28/40** | 양호 |
| 2 | 시장매력도 | **26/40** | 양호 |
| 3 | 기술경쟁력 | **25/40** | 양호 |
| 4 | 경쟁우위 | **20/40** | 보통 |
| 5 | 실행가능성 | **23/40** | 보통 |
| **총점** | | **122/200** | **Conditional Go** |

**판정: Conditional Go (120~159 구간)**
보완 후 추진 권고. 핵심 보완 항목: (1) HE 제외 기술 재설계, (2) 정량 KPI 확정, (3) B2C WTP 조사.

---

## 데이터 부족 항목 및 보강 키워드

| # | 항목 | 영향받는 평가 | 부여 점수 | 보강 검색 키워드 |
|---|------|-------------|----------|----------------|
| D-1 | 국내 B2C 통화 보안 유료 서비스 TAM/SAM | 시장매력도(시장 규모), 사업포텐셜 | 6/10 (중앙값+1) | `"Korea B2C mobile security subscription market size"`, `"통화보안 유료서비스 시장규모 국내"` |
| D-2 | B2C 유료 전환율(WTP) 소비자 조사 | 고객가치(고객 수용성), 실행가능성(ROI) | 5~6/10 (중앙값) | `"LG U+ voice security ARPU"`, `"통화보안 유료서비스 전환율 WTP"`, `"mobile security premium subscription conversion rate Korea"` |
| D-3 | LGU+ 국내 특허 포트폴리오 (KIPRIS) | 기술경쟁력(특허) | 5/10 (중앙값) | `"LG유플러스 보이스피싱 탐지 특허 KIPRIS"`, `"양자암호 통화보안 특허 한국"` |
| D-4 | PQC/SafeEar 차별화 지속 기간 | 경쟁우위(차별화 지속성) | 5/10 (중앙값) | `"PQC telecom deployment timeline competitor"`, `"양자내성암호 통신사 상용화 일정"` |
| D-5 | 투자 규모 대비 ROI | 실행가능성(ROI) | 5/10 (중앙값) | `"telecom voice security service ROI"`, `"통화보안 서비스 투자수익률 사례"` |
| D-6 | 12~18개월 서비스 출시 타임라인 근거 | 실행가능성(일정) | - (추정 표시) | `"telecom voice security service launch timeline"`, `"통신사 보안서비스 출시 일정 사례"` |

**데이터 부족 항목 6개 (>3개) → 신뢰도 자동 Low 기준 해당. 단, 핵심 기술 판정(HE 불가, 온디바이스 TRL 7~8)은 복수 학술 소스로 High 확신 수준이므로, 전체 신뢰도를 Medium으로 조정 (Low에서 1단계 상향).**

---

## 신뢰도: Medium

**근거:**

- **High 확신 영역**: 동형암호 실시간 불가 판정(복수 학술 논문 [P-01, P-02, P-05] + IEEE 실증 [P-02]), 보이스피싱 피해 통계(경찰청·금감원 공식 [N-03, N-04]), 삼성 S26/iOS 26 무료 탑재(공식 발표 [E-01, N-07]), 온디바이스 AI TRL 7~8(3사+삼성 상용화 [E-01~E-04])
- **Medium 확신 영역**: 글로벌 시장 규모 $1.87B(GrowthMarketReports 단일 소스 [G-14]), KT 탐지율 91.6%(KT 뉴스룸+Telecompaper 2개 소스 [E-03]), LGU+ 익시오 피해 예방 1,720억 원(복수 언론 [E-04])
- **Low 확신/데이터 부재 영역**: 국내 B2C 유료 TAM [D-1], WTP [D-2], LGU+ 특허 포트폴리오 [D-3], 차별화 지속 기간 [D-4], ROI [D-5]
- **데이터 부족 항목 6개**: 규칙상 3개 초과 시 자동 Low. 그러나 핵심 기술 판정과 경쟁사 현황은 High 확신이므로 Medium으로 상향 조정.

---

## References

### 글로벌 출처 (G-xx)

| 번호 | 출처명 | 발행일 | 기관유형 | 제목 | 인용원문(한글) | 관련성 | 신뢰성 | 최신성 | URL |
|------|--------|-------|----------|------|-------------|--------|--------|--------|-----|
| G-05 | Gizmochina / Time Magazine | 2025.12 / 2025 | 미디어 | Snapdragon 8 Gen 5 NPU / Honor On-Device AI Deepfake Detection | +46% AI 성능, 70+ TOPS; Honor Magic 7 Pro 온디바이스 영상통화 딥페이크 탐지 | 4 | 3 | 5 | https://www.gizmochina.com/2025/12/24/on-device-ai-snapdragon-8-gen-5-npu-explained/ |
| G-07 | postquantum.com | 2025 | 전문기관 | PQC Standardization 2025 Update | ML-KEM, ML-DSA FIPS 확정 | 4 | 4 | 5 | https://postquantum.com/post-quantum/cryptography-pqc-nist/ |
| G-08 | postquantum.com / GSMA PQ.03 v2.0 | 2025 / 2024 | 전문기관/업계 | Telecom's Quantum-Safe Imperative; PQC Guidelines for Telecom | VoLTE IMS 전환 벤더 의존, 3GPP 미표준화, GSMA 가이드라인 v2.0 | 5 | 4 | 5 | https://postquantum.com/post-quantum/telecom-pqc-challenges/ |
| G-09 | Pindrop 공식 / PR Newswire | 2025 | 기업 | 2025 Voice Intelligence and Security Report | 딥페이크 +1300%, $12.5B 사기 피해, 탐지율 80%, FP <0.5% | 4 | 4 | 5 | https://www.pindrop.com/research/report/voice-intelligence-security-report/ |
| G-14 | GrowthMarketReports / Pindrop | 2024 / 2025 | 리서치/기업 | Fraud Analytics for International Voice Market | 2024 $1.87B -> 2033 $5.49B, CAGR 14.2%; 딥페이크 사기 +162% YoY | 4 | 3 | 4 | https://growthmarketreports.com/report/fraud-analytics-for-international-voice-market |
| G-15 | GlobeNewswire | 2026.02.23 | 리서치 | Post-Quantum Cryptography Industry Research Report 2026 | PQC가 연구 개념에서 핵심 사이버보안 축으로 전환 | 3 | 3 | 5 | https://www.globenewswire.com/news-release/2026/02/23/3242432/28124/en/ |

### 최신 동향 (N-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약(한글) | URL |
|------|--------|-------|------|-----------|----------|-----|
| N-01 | 보안뉴스 / Nate News | 2025.12 | SKT/KT/LGU+, AI로 보이스피싱 탐지 고도화 | SKT KT LGU 보이스피싱 AI 탐지 | 3사 AI 보이스피싱 탐지 고도화, SKT 음성 스팸 +119%, 2억 5천만 건 차단 | https://news.nate.com/view/20251202n25936 |
| N-03 | 세계일보 | 2025.04.27 | 2025년 1분기 보이스피싱 피해액 3116억원 | 보이스피싱 피해액 2025 | Q1 3,116억 원, 건수 +17%, 피해액 2.2배 | https://www.segye.com/newsView/20250427507459 |
| N-04 | 헤럴드경제 | 2026 | 악성 앱으로 휴대폰 장악... 지난해 보이스피싱 피해 1.2조 사상 최대 | 보이스피싱 피해액 2025 | 2025년 연간 1조 2,578억 원 확정 | https://biz.heraldcorp.com/article/10661923 |
| N-05 | 스마트투데이 | 2025 | LGU+, 안티딥보이스 위변조음성 5500건 탐지 | LGU+ Anti-DeepVoice 성과 | 위변조 음성 5,500건 탐지, 5초 내 탐지 | https://www.smarttoday.co.kr/news/articleView.html?idxno=87596 |
| N-06 | Sammy Fans | 2026.02.25 | Gemini-powered Scam Detection arrives on Galaxy S26 | Samsung Galaxy S26 Gemini scam | S26에 온디바이스 Gemini 기반 스캠 탐지 탑재 | https://www.sammyfans.com/2026/02/25/samsung-galaxy-s26-gemini-ai-scam-detection/ |
| N-07 | 9to5Mac | 2025.06.13 | Apple's new iOS 26 spam tools will make scammers cry | Apple iPhone scam iOS 26 | iOS 26 Call Screening: 미지 발신자 AI 대리 응대, 20개국+ | https://9to5mac.com/2025/06/13/security-bite-apples-new-ios-26-spam-tools-will-make-scammers-cry/ |
| N-08 | VoIP Review | 2025.11.18 | BT and Pindrop Team Up to Combat Voice Fraud with AI | Pindrop telecom partnership | BT-Pindrop 딥페이크 탐지 통합 파트너십 | https://voip.review/2025/11/18/bt-pindrop-team-combat-voice-fraud-ai/ |
| N-09 | The Pickool / Telecompaper | 2024.10 | KT Gains Regulatory Approval for AI Voice Phishing Detection | KT regulatory sandbox 2024 | 과기정통부 ICT 규제샌드박스 실증특례 승인 | https://www.thepickool.com/kt-gains-regulatory-approval-for-ai-powered-voice-phishing-detection-service/ |

### 기업 발언 (E-xx)

| 번호 | 출처명 | 발행일 | 제목 | 검색키워드 | 요약원문 |
|------|--------|-------|------|-----------|---------|
| E-01 | 삼성 뉴스룸 / 과기정통부 | 2026.02.25 / 2026.02.12 | 갤럭시 AI로 보이스피싱 차단 | 삼성 S26 보이스피싱 | 국과수 3만건 딥러닝, One UI 8.0+ 기본 탑재, 통신 3사 협력, 공동 플랫폼 2026~2027 |
| E-02 | SK텔레콤 뉴스룸 | 2025.12 / 2026.01 | SKT 에이닷, AI로 보이스피싱 탐지 | SKT 스캠뱅가드 | 온디바이스 AI, 2025년 11억 건 차단, +35%, IBK 기업은행 기술 이전 |
| E-03 | KT 뉴스룸 / The Pickool | 2025.07.29 | KT AI 보이스피싱 탐지 2.0 출시 | KT AI 탐지 2.0 | 화자인식+딥보이스, 온디바이스, 91.6% 탐지율, 1,300억 원 예방, 2026 목표 95%+ |
| E-04 | 한국NGO신문 / EBN | 2026.01 / 2026.02 | KB국민은행-LGU+ AI 보이스피싱 대응 | LGU+ 익시오 KB | 익시오-KB 연동 1,720억 원 예방, MWC26 시연 예정 |
| E-05 | Korea Herald / Korea Times | 2025.02 | LG Uplus world's 1st on-device anti-deepvoice | LGU+ Anti-DeepVoice PQC MWC 2025 | MWC 2025 Exy Guardian: Anti-DeepVoice+PQC+SLM 통합 스위트 |

### 학술 논문 (P-xx)

| 번호 | 저자 | 발행년도 | 제목 | 핵심 인용 | DOI/URL |
|------|------|---------|------|---------|---------|
| P-01 | Chillotti et al. | 2020/2025 | TFHE: Fast FHE over the Torus / Refined TFHE | binary gate당 ~13ms; refined 4.2~6.8ms | https://tfhe.github.io/tfhe/ |
| P-02 | Bae et al. | 2019 | Hardware Assisted HE in Real-Time VOIP (IEEE) | FPGA 가속에도 ~150ms/operation | https://ieeexplore.ieee.org/document/8639492 |
| P-03 | (ACM CCS 2025) | 2025 | Refined TFHE Leveled HE Evaluation | 특정 연산 4.2~6.8ms, 실시간 통화 불충분 | https://dl.acm.org/doi/10.1145/3719027.3744873 |
| P-04 | Boura et al. | 2023 | Scalable E2E HE Audio Conferencing (ACM CCSW) | 클라우드 지원 시 가능, 일반 VoIP 불가 | https://dl.acm.org/doi/10.1145/3605763.3625245 |
| P-05 | (arXiv) | 2026.02 | Hybrid Homomorphic Encryption Feasibility | "prohibitive latency" 명시 | https://arxiv.org/pdf/2602.02717 |
| P-06 | (arXiv) | 2025.12 | Physics-Guided Deepfake Detection for Voice Auth | M4 Pro 149ms/3초; HE 대신 ZKP 제안 | https://arxiv.org/abs/2512.06040 |
| P-07 | (arXiv) | 2025.09 | Deepfake Voice Detection: All in the Presentation | 입력 presentation 방식이 탐지 성능 핵심 | https://arxiv.org/abs/2509.26471 |
| P-08 | Xinfeng Li et al. | 2024 | SafeEar: Privacy-Preserving Audio Deepfake Detection (ACM CCS) | EER 2.02%; WER 93.93%+ 프라이버시 보존 | https://arxiv.org/abs/2409.09272 |
| P-09 | K.A. Shahriar | 2026.01 | Lightweight Resolution-Aware Audio Deepfake Detection | 159k params, <1 GFLOP; EER 0.16% | https://arxiv.org/abs/2601.06560 |
| P-10 | (arXiv) | 2025.12 | Noise-Aware Audio Deepfake Detection SNR-Benchmarks | 실제 잡음에서 탐지 성능 급락 확인 | https://arxiv.org/abs/2512.13744 |
| P-11 | (arXiv) | 2026.01 | Audio Deepfake Detection in the Age of Advanced TTS | 최신 TTS 딥페이크 탐지 어려움 심화, Generalization 문제 | https://arxiv.org/abs/2601.20510 |

### 특허 (T-xx)

| 번호 | 출원인 | 등록/출원일 | 특허번호 | 제목 | 관할 |
|------|--------|----------|---------|------|------|
| T-01 | Google LLC | 2022.08.23 | US11423926B2 | Real-time voice phishing detection | USPTO |
| T-02 | Samsung Electronics | 2024 | US11652603B2 | AI Calculation Semiconductor Device (HE 가속) | USPTO |
| T-03 | Wells Fargo Bank | 2024.02.07 출원 / 2025.02.19 공개 | US20250252968A1 | Synthetic Voice Fraud Detection | USPTO |
| T-04 | Bank of America | 2023.11.07 출원 / 2025.05.08 공개 | US20250148788 | Deepfake Detection System | USPTO |
| T-05 | (미확인) | 2015 출원 | US20150237019A1 | HE for Teleconferencing (선행특허) | USPTO |

### 내부 자료 (I-xx)

| 번호 | 자료명 | 작성일 | 페이지 | 인용내용 |
|------|--------|-------|--------|---------|
| I-01 | Secure AI 기술/시장/규제 동향 리서치 | 2026-02-25 | 전체 | HE TRL 4~5, PQC TRL 7~8, Anti-DeepVoice MWC 2025, SKT 7,000억/KT 1조 투자 비교, LGU+ 보안퍼스트 전략 |
| I-02 | WTIS SKILL-0 Analysis Brief: Secure AI | 2026-02-26 | 전체 | V1~V6 검증 항목, 핵심 검색 쿼리, 경쟁사 분석 대상, 핵심 기술 위험 플래그(V4 HE Critical) |

---

*본 보고서는 WTIS v4.0 파이프라인의 SKILL-1(선정검증) 단계 산출물이다. 최종 의사결정은 경영진의 판단에 위임한다.*
