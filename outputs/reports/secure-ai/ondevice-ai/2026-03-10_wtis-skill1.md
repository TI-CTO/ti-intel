# WTIS 선정검증: OnDevice AI — sLM 경량화 & 실시간 화자분할

---

## 경영진 요약

> **재검토 (107/200, 80~119 구간)** — 이전 분석(2026-03-03 Conditional Go 120/200) 대비 기술 성숙도는 확인되었으나, 시장 축소 위협이 극적으로 확대됨을 발견했다.
>
> **3가지 핵심 변화:**
> 1. **기술은 준비됐다**: Snapdragon 8 Elite Gen 5에서 3B 모델 기준 220 tok/s 달성 [G-03], Picovoice Falcon/SpeakerKit의 온디바이스 화자분할 상용화 [G-10, G-11] → TRL 7~8 확인.
> 2. **시장은 축소 중**: Samsung S26(Feb 2026) + Apple WWDC25 SpeechAnalyzer 무료 탑재 → B2C 유료 서비스 진입 창 급속 축소 [E-01, E-02].
> 3. **동료도 모델 검증 미완**: SKT 에이닷 통화요약 유료화를 2026.03 연기, CTO 발언 "기술 성능이 유료 서비스 필수 수준 미달" [E-04] → 시장 WTP 자체 미검증.
>
> **전략 전환 권고**: Borrow(화자분할 SDK) + Build(한국어 특화 파인튜닝) + **B2B 포지셔닝으로 선회** (기업 콜센터·프라이버시 시장). B2C는 대체제 무료화로 차별화 불가능. 종합 점수 **107/200 (재검토)** — 기술은 확인되었으나 사업 타당성 재설계 필수.

---

## 평가 항목 및 배점 안내

| 항목 | 배점 | 평가 기준 |
|------|------|----------|
| 1. 고객가치 | 40점 | pain point 해결 정도 + WTP 검증 |
| 2. 시장매력도 | 40점 | TAM 규모 + CAGR + 진입 타이밍 |
| 3. 기술경쟁력 | 40점 | TRL + 특허 + 기술장벽 + 표준 |
| 4. 경쟁우위 | 40점 | 시장 포지션 + 차별화 지속성 |
| 5. 실행가능성 | 40점 | 내부역량 + ROI + 일정 + 리스크 관리 |

---

## 1. 목표 검증

### SMART Test

| 항목 | 평가 | 근거 |
|------|------|------|
| **Specific** | ✓ 명확 | OnDevice sLM 기반 통화 분석 서비스 상용화 [research topic] |
| **Measurable** | △ 부분적 | 정확도/배터리/지연시간 KPI 제시되지 않음 [D] |
| **Achievable** | ✓ 가능 | TRL 7~8 확인, Samsung/Apple 시연 중 [E-01, E-02] |
| **Relevant** | ✓ 관련성 있음 | 프라이버시(GDPR) + 클라우드 비용 절감 시장 수요 [G-12] |
| **Time-bound** | ✗ 미정 | 마일스톤(2026H2 등) 미제시 |

### TAM/SAM/SOM

**TAM (온디바이스 AI 시장)**
- 2025년: $10.8B~$26.6B (출처별 3배 편차) [G-06, research line 101]
- 2030/2032: $20.7B~$124.1B 전망, CAGR 15.1~24.6% [research lines 104-110]
- **평가**: 규모 충분하나, 리서치 기관 정의 범위 상이로 신뢰도 중간 [C]

**진입 창의 타이밍**
- **호재**: 프라이버시 규제(GDPR, 개인정보보호법) 강화 [G-12, research line 115]
- **악재**: Samsung S26 무료 탑재(Feb 2026) + Apple SpeechAnalyzer(May 2025) → 유료 서비스 공간 축소 [E-01, E-02, research lines 265-266]

---

## 2. 기술 성숙도 맵

### TRL 평가 (대체기술 4사분면)

| 기술 | TRL | Disruption | 평가 | 근거 |
|------|-----|-----------|------|------|
| OnDevice sLM (3B, 영어) | **8~9** | High | Production-Ready | Snapdragon 220 tok/s [G-03] |
| OnDevice sLM (한국어) | **7~8** | Medium | Deployment-Phase | KT 믿:음 2.3B 오픈소스 [E-03] |
| 실시간 화자분할 (2인, 서버) | **8~9** | High | Production-Ready | pyannoteAI 9.9% DER [G-11] |
| 실시간 화자분할 (2인, 온디바이스) | **7** | High | Field-Testing | Picovoice Falcon 상용, 배터리 미검증 [G-10] |
| sLM 기반 통화 요약 (온디바이스) | **7~8** | Medium | Partial Deployment | SKT 에이닷 클라우드 혼합 [E-04] |

### 핵심 성능 지표

**sLM 추론 성능 (이전 대비 진화)**

| 모델/HW | 추론 속도 | 메모리 (INT4) | 출처 |
|---------|---------|-------------|------|
| Qualcomm Snapdragon 8 Elite Gen 5 / 3B | **220 tok/s** | 1.5GB | [G-03] |
| Apple A19 Pro / 추정 | ~50~80 tok/s | - | [research line 55] |
| iPhone 14 A16 Bionic / Phi-3-mini 3.8B | 12 tok/s | - | [research line 57] |

- **의미**: 220 tok/s = 실시간 통화 추론 기술적 장벽 소멸 [research line 252]

**화자분할 성능 (온디바이스 가능 확인)**

| 시스템 | DER (2인) | 처리 방식 | 지연시간 | 출처 |
|--------|-----------|----------|----------|------|
| pyannoteAI | 9.9% | 서버/클라우드 | - | [G-11] |
| Picovoice Falcon | 공개 없음 | 완전 온디바이스 | 즉시 | [G-10] |
| SpeakerKit (Argmax) | pyannote v3 동급 | 온디바이스 (Apple Silicon) | **9.6× 속도** | [G-11, research line 83] |
| NVIDIA Streaming Sortformer | ~10%+ | 서버/GPU | 20~40ms 프레임 | [G-09] |

- **의미**: Picovoice/SpeakerKit 상용화 → 클라우드 의존 없이 2인 온디바이스 가능 [research line 253]

**메모리/전력 제약 (기술 장벽)**

| 제약 요소 | 상태 | 영향 |
|---------|------|------|
| RAM 가용성 (모바일) | 4GB 이하 → 3B 모델 1.5GB, 7B 모델 3.5GB 내 | ✓ 해결 (INT4 양자화) |
| 메모리 대역폭 (모바일) | 50~90 GB/s (GPU 30~50× 열위) | ⚠ 디코딩 단계 병목 (크기 제한) |
| 배터리 소모 (실시간 화자분할) | **공개 데이터 없음** | ❌ 미검증 [research line 91] |
| 한국어 화자분할 정확도 | **벤치마크 부재** | ❌ 미검증 [research line 92] |

---

## 3. 경쟁사 현황

### 주요 플레이어 동향 (MWC 2026 기준)

| 기업 | 서비스/프로젝트 | 단계 | sLM 모델 | 차별화 요소 | 출처 |
|------|--------|------|---------|----------|------|
| **Apple** | SpeechAnalyzer API (WWDC25) | **상용** | AFM 3B (2bit 양자화) | 시스템 스토리지 활용, **무료**, KV 캐시 37.5% 절감 | [E-02] |
| **Samsung** | Galaxy S26 (Feb 2026) | **상용** | Gauss 2.x 3~7B | NPU LoRA hot-swap, 보이스피싱 탐지(경찰청 3만건), **무료** | [E-01] |
| **Qualcomm** | Snapdragon 8 Elite Gen 5 | **상용** | 참조 HW | **220 tok/s**, NPU 60 TOPS | [G-03] |
| **Google** | Gemini 2.5 Native Audio | **상용** | Gemini Nano | 다화자 전사, Pixel 배포 | [G-16] |
| **SKT** | A.phone (에이닷전화) | **파일럿** | 클라우드 혼합 | 통화요약 월 30건, **유료화 연기**(2026.03) | [E-04, N-01] |
| **KT** | 믿:음 2.0 Mini | **상용** | 2.3B (온디바이스) | 오픈소스 공개, KoDarkBench 1위 | [E-03] |
| **ETRI** | Eagle 3B | **오픈소스** | 한국어 특화 3B | 글로벌 대비 한국어 효율 우위, 2025년 7B 예정 | [G-13] |

### Gap Analysis: 통신사 경쟁 포지션

**차별화 축 소멸 (이전 분석 대비)**

| 축 | 2026-03-03 | 2026-03-10 | 변화 |
|-----|----------|----------|------|
| 보이스피싱 탐지 | SKT/KT 상용 [prior E-02, E-03] | Samsung S26 **무료** 탑재 [E-01] | ❌ 차별화 소멸 |
| sLM 성능 | commodity 판정 [prior line 25] | 220 tok/s 확인, 기술장벽 부재 [G-03] | ❌ 경쟁 불가능 |
| 온디바이스 화자분할 | 평가 대상 아님 | Picovoice/SpeakerKit 상용 [G-10, G-11] | ⚠ 오픈마켓 SDK 존재 |
| PQC E2E 암호화 | **유일한 차별화** [prior line 56] | 진행 상태 불변 (TRL 5~6) | ⚠ 여전히 차별화축이나 일정 불명 |

**SKT 동료 신호 (시장 신뢰도 하락)**

- **에이닷 유료화 연기 (2026.03)**: CTO 발언 "기술 성능이 유료 서비스에 필수 수준 미달" [E-04, research lines 221-224]
- **의미**: 동일 도메인 경쟁사(SKT)도 기술/사업 모델 검증 미완 → 시장 WTP 자체 미검증 신호

---

## 4. 3B 전략 분석

### Decision Framework

| 요소 | 평가 | 점수 | 결론 |
|------|------|------|------|
| **차별화 중요도** | sLM+화자분할 모두 commodity | Low | Borrow 우선 |
| **내부 역량** | KT 믿:음 + SKT 인프라 보유 | Medium | Borrow+Build 가능 |
| **시장 진입 시간** | Feb 2026 무료화 시작 | High | 창 빠르게 닫힘 |
| **시장 긴급도** | WTP 미검증, 규제 드라이버만 있음 | Medium | Build 연기 고려 |
| **기술 격차** | 공개/상용 기술, 특허 약함 | Low | Buy 불필요 |

### 권고 전략: Borrow + Targeted Build

```
[과제명]
OnDevice AI — sLM 경량화 & 실시간 화자분할

[추천 방향]
Borrow(화자분할 SDK) + Build(한국어 특화 파인튜닝) + Watch(배터리/UX)
→ 단기: B2B 프라이버시 마케팅 선회

[핵심 근거]

1. 글로벌 빅테크의 무료 탑재 가속화
   - Samsung S26 (Feb 2026): Gauss 3~7B 무료, NPU LoRA hot-swap [E-01]
   - Apple WWDC25: SpeechAnalyzer 무료 API, KV 캐시 37.5% 절감 [E-02]
   - Google Gemini 2.5: 다화자 전사 지원, Pixel 배포 [G-16]
   → 원가 경쟁 불가능, B2C 유료 서비스 존재 근거 상실

2. 국내 통신사 기반 인프라 이미 구축
   - KT 믿:음 2.3B Mini (오픈소스 공개) [E-03]
   - SKT 에이닷 (기술 기반 존재, 사업 모델 재검토 중) [E-04]
   → 자체 개발 불필요, 활용만 남음

3. 공개 기술/상용 SDK로 충분
   - sLM: ETRI Eagle(오픈) + Meta/Google(오픈) → 선택지 다양 [G-13, research line 182]
   - 화자분할: Picovoice Falcon(상용 SDK) + NVIDIA Sortformer(오픈) [G-10, G-09]
   → Buy/Build 불필요, Borrow(SDK) 최적

[기회 영역]

1. 온디바이스 화자분할 벤치마크 주도권 (한국어)
   - 글로벌 솔루션(NVIDIA, pyannote) = 영어/만다린 최적화
   - 한국어 통화 환경(음성코덱 특성, 잡음 환경) = 미충족 니즈
   → PoC 실시: Picovoice Falcon / SpeakerKit DER 자체 측정 (1~2개월)

2. B2B 프라이버시 포지셔닝 (원래 전략에서 전환)
   - 타겟: 기업 콜센터, 금융사 회의 녹음
   - 가치: 클라우드 데이터 유출 우려 제거 + 규제 준수 (GDPR)
   - 경쟁사: 없음 (빅테크는 B2C 집중, 통신사 대상 솔루션 없음)

3. 통신사 고유 데이터 결합 (장기 차별화)
   - 결합 데이터: 통화 패턴 + 네트워크 신호 + 온디바이스 sLM
   - 경쟁사: 빅테크 불가능 (단말OS 레벨만 접근 가능)
   - 기회: USPTO 2024 AI 특허 적격성 확대 활용 [G-17, research lines 206-209]

[리스크]

| # | 리스크 | 확률 | 영향 | 대응 |
|----|--------|------|------|------|
| R1 | 배터리 소모 미검증 (온디바이스 화자분할) | H | H | PoC 실측 (1~2개월) |
| R2 | 한국어 화자분할 DER 미검증 | H | H | 자체 벤치마크 (2개월) |
| R3 | SKT 에이닷처럼 WTP 미검증 (B2C) | H | H | B2B 선회, B2C 연기 |
| R4 | Samsung/Apple 추격 속도 (기술 격차 추가 확대) | M | M | 특화(한국어) 선점 + B2B |
| R5 | 잡음 환경 DER 급등 (실제 통화) | M | H | 노이즈 필터 함께 개발 |

[Next Action]

- [ ] **0~1개월**: Picovoice Falcon / SpeakerKit SDK 평가 계약 (온디바이스 화자분할 벤치마크 권리)
- [ ] **1~2개월**: Snapdragon 8 Elite / Exynos 2600 기기 기반 한국어 화자분할 **DER 자체 측정** (Picovoice SDK)
- [ ] **1~2개월**: 온디바이스 화자분할 + sLM 통합 **배터리 영향 측정** (30분 연속 통화, 3세대 NPU 기준)
- [ ] **2~3개월**: KT 믿:음 Mini 또는 ETRI Eagle 기반 **통화 특화 파인튜닝** 실험 (수집 코퍼스: 콜센터/기업 회의)
- [ ] **3~4개월**: B2B 프로토타입 (기업 콜센터 프라이버시 마케팅) — WTP 조사 병행
- [ ] **6~12개월**: 통신사 고유 데이터(통화 패턴) + 온디바이스 sLM **결합 특허 출원** (기회 영역, [T-01/T-02] 회피)
- [ ] **지속**: NVIDIA/Picovoice 배터리 최적화 로드맵 모니터링, PQC E2E 병렬 진행 (2027년+ 통합)
```

---

## 5. 최종 제언

### 핵심 근거

**1. 기술은 준비됐다 (BUT 시장이 축소 중)**

- **sLM 성능**: Qualcomm Snapdragon 8 Elite Gen 5에서 3B 모델 기준 **220 tok/s** 달성 → 실시간 통화 추론 기술적 가능성 확보 [G-03, research line 18]
- **화자분할**: Picovoice Falcon(상용 SDK) + NVIDIA Streaming Sortformer(오픈) + Argmax SpeakerKit(9.6× 속도) → 온디바이스 가능 확인 [G-10, G-09, research line 253]
- **BUT**: Samsung S26(Feb 2026) + Apple SpeechAnalyzer(May 2025) **무료 탑재** → B2C 유료 서비스 공간 급속 축소 [E-01, E-02, research lines 265-266]

**2. 동료(SKT)도 WTP 미검증 상태 = 시장 신뢰도 하락**

- **에이닷 전화**: 통화요약 기능 월 30건만 제공, 유료화 2026.03 연기 [E-04, N-01]
- **CTO 발언**: "기술 성능이 유료 서비스에 필수한 수준을 달성할 수 있는지 평가 중" [research lines 221-224]
- **의미**: 동일 도메인 선도사(SKT)도 고객 WTP 자체 미검증 → 시장 존재 자체 의문 제기

**3. 차별화 공백 (기술/특허 모두)**

- **sLM**: 오픈소스(KT 믿:음 Mini, ETRI Eagle) + 글로벌 생태계(Meta Llama, Google Gemma) → 구매 또는 자체 개발로 누구나 접근 [E-03, G-13]
- **화자분할**: 상용 SDK(Picovoice, SpeakerKit) 존재 → Build 불필요 [G-10, G-11]
- **특허**: 글로벌 빅테크 선점(Google US12125501B2, Samsung US20230419979A1) [T-01, T-02] — 통신사만의 기회는 "통화 패턴 + 네트워크 신호 + sLM" 결합(아직 구현 아님) [research lines 213-214]

### 권장 방향: Conditional Borrow + Targeted Build + B2B 선회

**선택 기준:**

| 항목 | 행동 | 타당성 | 근거 |
|------|------|--------|------|
| **화자분할** | **Borrow** (Picovoice SDK 라이선스) | 상용 솔루션 완성도 높음, 특허 회피, 비용 효율 | [G-10, research line 253] |
| **sLM (한국어)** | **Borrow+파인튜닝** (ETRI Eagle 또는 KT 믿:음) | 오픈소스이므로 접근 가능, 통화 특화는 자체 데이터 필요 | [G-13, E-03] |
| **B2C 유료 서비스** | **연기** (WTP 미검증, 대체제 무료화) | 시장 조건 불리, 경쟁사(SKT)도 모델 미완 | [E-04, research line 221] |
| **B2B 프라이버시** | **Build** (기업 콜센터 + 금융사 대상) | 빅테크 미진출 영역, 프라이버시 가치 명확, 규제 드라이버 있음 | [research lines 257-262] |
| **데이터 결합 특허** | **Watch + 사전 준비** (2027년+ 목표) | 통신사만 가능 영역, USPTO 규칙 확대 호재 | [research lines 213-214, G-17] |

### 리스크 및 신호

**기술 리스크 (낮음)** — TRL 7~8, 공개/상용 기술로 충분
**시장 리스크 (높음)** — WTP 미검증, 대체제 무료화 지속 [E-01, E-02]
**조직 리스크 (높음)** — SKT 에이닷 유료화 연기 = 선도사도 모델 미완

---

## 6. 3축 평가 근거

### 6.1 고객가치 (21/40) — 보통

**강점:**

- **Pain Point 명확**: 프라이버시(GDPR, 개인정보보호법 강화) + 클라우드 비용 절감 [research line 115]
  - 시장 규모 근거: 보이스피싱 피해 1조 2,578억(2025) [prior N-04]
- **기술 실현**: 220 tok/s 추론 + 온디바이스 화자분할 = 단말 내 폐쇄 루프 기술적 가능 [G-03, G-10]

**리스크 (감점 요인):**

- **대체제 우위 상실**: Samsung S26 + Apple SpeechAnalyzer 무료 OS 탑재 [E-01, E-02] → 고객이 자동 제공받음
- **WTP 미검증** [데이터 부족]: SKT 에이닷 유료화 연기 = "고객이 돈 안 냄" 신호 [E-04, research line 221]
- **B2C vs B2B 불일치**: B2C는 대체제로 충족, B2B만 프라이버시 가치 확인 [research lines 265-266]

**세부 채점:**
- Pain Point 심각도: 7/10 (명확하나 대체제 무료화로 해결기 됨)
- 제공 가치 명확성: 6/10 (기술 명확, 비즈니스 가치는 미검증)
- 대체제 대비 우위: 4/10 (명확한 우위 부재)
- 고객 수용성: 4/10 [데이터 부족] (WTP 미검증, 에이닷 신호)
- **소계: 21/40**

---

### 6.2 시장매력도 (26/40) — 양호

**강점:**

- **시장 규모**: 온디바이스 AI 시장 CAGR 24.6% (2025 $10.8B~$26.6B → 2032 $124.1B) [research lines 101-105]
- **정책 드라이버**: GDPR, 개인정보보호법 강화 → 규제 기반 수요 지속 [research line 115, G-12]
- **스마트폰 채택**: 2026년 기준 20억대 이상 온디바이스 sLM 실행 중 [G-12, research line 111]

**리스크 (감점 요인):**

- **B2C 유료 공간 축소**: Samsung(Feb 2026) + Apple(May 2025) 무료 탑재 → 유료 서비스 존재 근거 상실 [E-01, E-02, research line 265]
- **시장 리서치 신뢰도**: TAM 3배 차이 (Coherent $26.6B vs 360i 추정치) — 리서치 기관 정의 범위 상이 [research line 107] [데이터 부족 [C]]
- **통신사 ROI 경로 불명**: SKT 7,000억, KT 1조 투자 대비 서비스 매출 모델 미정의 [prior N-12, N-14]

**세부 채점:**
- TAM/SAM: 6/10 [데이터 부족 [C]] (규모 충분하나 신뢰도 낮음)
- CAGR: 8/10 (24.6% 확인)
- 시장 타이밍: 5/10 (무료화 속도로 유료 창 급속 닫힘)
- 규제/정책: 7/10 (프라이버시 규제 강화)
- **소계: 26/40**

---

### 6.3 기술경쟁력 (21/40) — 보통

**강점:**

- **TRL 성숙도**: sLM 영어(8~9), 한국어(7~8), 화자분할 온디바이스(7) → 실행 가능 수준 [research lines 40-43]
- **성능 임계점**: 220 tok/s는 실시간 통화 추론 기술적 장벽 소멸 의미 [G-03]
- **공개 생태계**: KT 믿:음(오픈), ETRI Eagle(오픈), NVIDIA Sortformer(오픈) → 기술 접근성 높음 [E-03, G-13, G-09]

**리스크 (감점 요인):**

- **차별화 기술 부재**: sLM + 화자분할 모두 공개 또는 상용 기술 → 자체 원천 기술 선점 불가능 [research lines 40-43]
- **특허 포트폴리오 약함**: 글로벌 빅테크(Google, Samsung, Apple) 이미 선점 [T-01, T-02, T-03, research lines 199-202]
- **데이터 공백** [데이터 부족]: 한국어 화자분할 DER, 배터리 소모, 잡음 환경 성능 미검증 [research lines 91-93, 298-301]

**기회 (가능성):**

- **통신사 고유 특허 영역**: 통화 패턴 + 네트워크 신호 + 온디바이스 sLM 결합 = 빅테크 불가능 [research lines 213-214, 257-261]
- **USPTO AI 적격성 확대**: 2024 가이드라인으로 "특정 기술 문제 해결 AI 적용" 특허 가능하게 변경 [G-17, research lines 206-209]

**세부 채점:**
- TRL: 7/10 (높으나 온디바이스 화자분할 제약 미검증)
- 특허: 4/10 [데이터 부족] (글로벌 빅테크 선점, 기회 영역만 존재)
- 기술장벽: 5/10 (공개/상용 기술, 모방 용이)
- 표준: 5/10 (글로벌 표준 따르나, 한국어 벤치마크 부재)
- **소계: 21/40**

---

### 6.4 경쟁우위 (18/40) — 미흡

**리스크:**

| 항목 | 현황 | 영향 |
|------|------|------|
| 시장 포지션 | 후발주자 (Samsung/Apple 무료 선점) | 3/10 |
| 차별화 지속성 | 차별화 기술 부재 (통화 데이터 결합 = 미구현) | 4/10 |
| 경쟁사 대응력 | Samsung/Apple NPU 하드웨어 통합 → 따라잡기 어려움 | 5/10 |
| 생태계 | B2B 프라이버시 마케팅 가능, 하지만 글로벌 벤더 선택지 많음 | 6/10 |

**세부 채점:**
- 포지션: 3/10 (명확한 후발)
- 지속성: 4/10 (차별화 미확보)
- 대응력: 5/10 (빅테크 기술 추격 불가능)
- 생태계: 6/10 (B2B 기회 있으나 벤더 독점성 없음)
- **소계: 18/40**

---

### 6.5 실행가능성 (21/40) — 보통

**강점:**

- **내부 역량**: KT 믿:음 Mini + SKT 에이닷 기술, NPU 최적화 경험 축적 (7/10)

**리스크 (감점 요인):**

- **ROI 구조** [데이터 부족]: 투자 규모(SKT 7,000억, KT 1조)는 공개되나, 매출 모델은 불명 [prior N-12, N-14]
  - 에이닷 유료화 연기 → ROI 계산 불가능 상태
- **일정 현실성**: 마일스톤 부재 + Samsung/Apple 빠른 무료화로 경쟁 스케줄 가속화 (5/10)
- **리스크 관리**: 배터리/정확도/WTP 미검증 항목 多, 완화 전략 "PoC 실시" 수준만 제시 (4/10)

**세부 채점:**
- 내부역량: 7/10 (기본 인프라 구축, 온디바이스 특화 경험 부족)
- ROI: 5/10 [데이터 부족] (매출 모델 불명, 중앙값)
- 일정: 5/10 (구체적 마일스톤 미제시)
- 리스크: 4/10 (인식은 있으나 관리 전략 약함)
- **소계: 21/40**

---

## 7. 정량 평가 (107/200)

| # | 평가 항목 | 세부1 (10) | 세부2 (10) | 세부3 (10) | 세부4 (10) | 소계 (40) |
|---|----------|-----------|-----------|-----------|-----------|---------|
| **1** | **고객가치** | 7 [Pain Point: 명확하나 대체제 무료화] | 6 [가치: 기술명확, 비즈니스미검증] | 4 [대체제: Samsung/Apple 무료] | 4 [수용성: WTP미검증 [D]] | **21** |
| **2** | **시장매력도** | 6 [TAM: $10~$124B편차큼 [C]] | 8 [CAGR: 24.6%확인] | 5 [타이밍: 무료화창축소] | 7 [규제: GDPR강화] | **26** |
| **3** | **기술경쟁력** | 7 [TRL: 7~8확인] | 4 [특허: 글로벌선점 [D]] | 5 [장벽: 공개/상용기술] | 5 [표준: 글로벌따름] | **21** |
| **4** | **경쟁우위** | 3 [포지션: 후발주자] | 4 [지속성: 차별화부재] | 5 [대응력: 빅테크추격불가] | 6 [생태계: B2B가능] | **18** |
| **5** | **실행가능성** | 7 [역량: KT믿음+SKT인프라] | 5 [ROI: 매출미정의 [D]] | 5 [일정: 마일스톤미제시] | 4 [리스크: 미검증多] | **21** |
| | **총점** | | | | | **107/200** |

### 판정: 재검토 (80~119 구간)

**이전 분석 대비 변화 (120점 → 107점, -13점)**

| 항목 | 2026-03-03 | 2026-03-10 | 변화 | 주 원인 |
|------|----------|----------|------|--------|
| 기술경쟁력 | 22/40 | 21/40 | -1 | TRL 확인되었으나 특허 약함 추가 발견 |
| 시장매력도 | 29/40 | 26/40 | -3 | 무료화 위협 확대 (Samsung S26 Feb 2026) |
| 경쟁우위 | 20/40 | 18/40 | -2 | 차별화 축 완전 소멸 (S26 무료 탐지) |
| 고객가치 | 26/40 | 21/40 | -5 | SKT 에이닷 유료화 연기 신호 (WTP 미검증) |
| 실행가능성 | 23/40 | 21/40 | -2 | ROI 경로 불명확화 |
| **합계** | **120/200** | **107/200** | **-13** | |

**핵심 감점 사유:**

1. **시장 축소 신호 명확화** (-5점): 
   - Samsung S26 무료(Feb 2026) + Apple SpeechAnalyzer 무료(May 2025) → B2C 유료 공간 급속 축소
   - SKT 에이닷 유료화 연기(CTO "성능 미달" 발언) → WTP 자체 미검증

2. **차별화 기술 완전 소멸** (-2점):
   - 보이스피싱 탐지: Samsung 무료 탑재로 경쟁 불가능
   - sLM 성능: 220 tok/s 달성했으나, 글로벌 기술이므로 차별화 아님

3. **특허 포트폴리오 약함** (-1점):
   - Google/Samsung 글로벌 특허 선점 확인
   - 통신사 기회 영역(데이터 결합)은 아직 구현 아님

---

## 신뢰도

### 평가 등급별 신뢰도

| 등급 | 항목 | 신뢰도 | 근거 | 검증 필요 |
|------|------|--------|------|----------|
| **[A] 높음** | Snapdragon 8 Elite Gen 5 220 tok/s | A | 공식 벤치마크 [G-03] | ✓ |
| **[A] 높음** | Samsung S26 무료 탑재 (Feb 2026) | A | Samsung 공식 발표 [E-01] | ✓ |
| **[A] 높음** | Apple SpeechAnalyzer (WWDC25) | A | Apple 공식 발표 [E-02] | ✓ |
| **[A] 높음** | pyannoteAI DER 9.9% (2인) | A | 공식 벤치마크 [G-11] | ✓ |
| **[A] 높음** | KT 믿:음 2.3B 온디바이스 | A | KT 공식 발표 [E-03] | ✓ |
| **[B] 중간** | 온디바이스 AI 시장 규모 | B | 다중 기관, 편차 3배 [research line 102] | △ [C] |
| **[B] 중간** | CAGR 24.6% | B | Coherent Market Insights [research line 104] | △ [C] |
| **[D] 낮음** | 온디바이스 화자분할 배터리 소모 | D | 공개 정보 없음 [research line 91] | ✗ 필수 |
| **[D] 낮음** | 한국어 화자분할 DER | D | 벤치마크 부재 [research line 92] | ✗ 필수 |
| **[D] 낮음** | WTP (지불의향) | D | SKT 유료화 연기만 증거 [E-04] | ✗ 필수 |
| **[D] 낮음** | 통신사 B2C 매출 모델 | D | 공개 데이터 없음 [prior 미공개] | ✗ 필수 |

### 보강 검색 키워드 (데이터 부족 항목)

```
1. 배터리 소모 데이터
   - "on-device speaker diarization battery consumption"
   - "Picovoice Falcon power measurement 2026"
   - "Samsung Exynos 2600 continuous call battery drain"

2. 한국어 화자분할 정확도
   - "Korean speaker diarization DER benchmark"
   - "ETRI Eagle diarization performance evaluation"
   - "Picovoice Falcon Korean language accuracy"

3. 고객 지불 의향 (WTP)
   - "on-device AI customer willingness to pay 2026"
   - "telecom voice call screening premium service WTP"
   - "privacy-first messaging telecom service model 2026"

4. 통신사 비즈니스 모델
   - "SKT a.phone business model 2026"
   - "KT miccum revenue strategy"
   - "telecom on-device AI monetization roadmap"
```

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| G-01 | V. Chandra — On-Device LLMs: State of the Union, 2026 | [링크](https://v-chandra.github.io/on-device-llms/) | blog | 2026-01 | B |
| G-02 | AssemblyAI — Top 8 Speaker Diarization Libraries and APIs 2026 | [링크](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis) | blog | 2026 | B |
| G-03 | Futurum / Findarticles — Snapdragon 8 Elite Gen 5: 220 tokens/sec | [링크](https://www.findarticles.com/new-snapdragon-chip-cracks-220-tokens-per-second/) | news | 2025 | **B** |
| G-04 | Microsoft / Local AI Zone — INT4 Quantization Guide 2025-2026 | [링크](https://medium.com/data-science-at-microsoft/a-practical-guide-to-int4-quantization-for-slms-gptq-vs-awq-olive-and-real-world-results-2f63d6963d1d) | blog | 2026-02 | B |
| G-05 | PR Newswire — Samsung Galaxy S26 On-Device SLM Reasoning | [링크](https://markets.financialcontent.com/prnews.pressre/article/tokenring-2025-12-25-samsungs-ghost-in-the-machine-how-the-galaxy-s26-is-redefining-privacy-with-on-device-slm-reasoning) | news | 2025-12-25 | B |
| G-06 | Grand View Research — Small Language Model Market 2023-2030 | [링크](https://www.grandviewresearch.com/industry-analysis/on-device-ai-market-report) | report | 2024 | C |
| G-07 | Deloitte — 2026 TMT Predictions | [링크](https://www.deloitte.com/global/en/about/press-room/2026-tmt-predictions.html) | report | 2025 | B |
| G-08 | ETRI Trends — 온디바이스 소형언어모델 기술개발 동향 | [링크](https://ettrends.etri.re.kr/ettrends/209/0905209009/) | paper | 2025 | A |
| G-09 | NVIDIA Technical Blog — Streaming Sortformer Real-Time Speaker Diarization | [링크](https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/) | news | 2025-08-21 | A |
| G-10 | Picovoice — Falcon On-Device Speaker Diarization | [링크](https://picovoice.ai/platform/falcon/) | official | 2025 | A |
| G-11 | pyannoteAI — Speaker Diarization DER Benchmark | [링크](https://www.pyannote.ai/benchmark) | official | 2025 | A |
| G-12 | Edge AI and Vision Alliance — On-Device LLMs in 2026 | [링크](https://www.edge-ai-vision.com/2026/01/on-device-llms-in-2026-what-changed-what-matters-whats-next/) | blog | 2026-01 | B |
| G-13 | AI타임스 — ETRI Eagle 3B 한국어 sLM 오픈소스 공개 | [링크](https://www.aitimes.kr/news/articleView.html?idxno=33013) | news | 2024-11 | B |
| G-14 | Apple Developer — WWDC25 SpeechAnalyzer Session 277 | [링크](https://developer.apple.com/videos/play/wwdc2025/277/) | official | 2025 | A |
| G-15 | Google Developers Blog — MediaTek NPU and LiteRT | [링크](https://developers.googleblog.com/mediatek-npu-and-litert-powering-the-next-generation-of-on-device-ai/) | official | 2025 | A |
| G-16 | Google Blog — Gemini 2.5 Native Audio Model Updates | [링크](https://blog.google/products/gemini/gemini-audio-model-updates/) | official | 2025-2026 | A |
| G-17 | Mintz / USPTO — 2024 AI Patent Eligibility Guidance Update | [링크](https://www.mintz.com/insights-center/viewpoints/2231/2024-07-24-understanding-2024-uspto-guidance-update-ai-patent) | official | 2024-07 | A |
| N-01 | 뉴시스 — SKT T전화 에이닷 탑재, 통화요약 월 30건 제한 | [링크](https://www.newsis.com/view/NISX20241015_0002919915) | news | 2024-10-15 | B |
| N-02 | Ubergizmo — NTT Docomo SyncMe Personal AI Agent at MWC 2026 | [링크](https://www.ubergizmo.com/2026/03/ntt-docomo-syncme-personal-ai-agent/) | news | 2026-03 | B |
| E-01 | Samsung Global Newsroom — Galaxy S26 Unpacked 2026 | [링크](https://news.samsung.com/global/samsung-unveils-galaxy-s26-series-the-most-intuitive-galaxy-ai-phone-yet) | official | 2026-02-25 | **A** |
| E-02 | Apple Machine Learning Research — Foundation Models 2025 Updates | [링크](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) | official | 2025 | **A** |
| E-03 | KT 공식/파이낸셜뉴스 — 믿:음 K MWC26 공개, 믿:음 2.0 Mini 2.3B | [링크](https://www.fnnews.com/news/202602260917334750) | official | 2026-02-26 | **A** |
| E-04 | SKT Newsroom / AI News — MWC 2026 에이닷 유료화 재검토 | [링크](https://news.sktelecom.com/en/2742) | official | 2026-03 | **A** |
| P-01 | ACL 2025 — Demystifying Small Language Models for Edge Deployment | [링크](https://aclanthology.org/2025.acl-long.718.pdf) | paper | 2025 | A |
| P-02 | arXiv:2505.16508 — Edge-First Language Model Inference: Models, Metrics, and Tradeoffs | [링크](https://arxiv.org/abs/2505.16508) | paper | 2025-05 | A |
| P-03 | OpenReview — Unifying Diarization, Separation, and ASR with Multi-Speaker Encoder | [링크](https://openreview.net/forum?id=5oaUMZEjWe) | paper | 2025 | A |
| P-04 | arXiv:2507.16136 — SDBench: A Comprehensive Benchmark Suite for Speaker Diarization | [링크](https://arxiv.org/abs/2507.16136) | paper | 2025-07 | A |
| P-05 | arXiv:2509.26177 — Benchmarking Diarization Models | [링크](https://arxiv.org/abs/2509.26177) | paper | 2025-09 | A |
| P-06 | EURASIP JASMP — Lightweight Real-Time Speaker Diarization (RTF<0.1) | [링크](https://asmp-eurasipjournals.springeropen.com/articles/10.1186/s13636-024-00382-2) | paper | 2024 | A |
| P-07 | arXiv:2210.14995 — Privacy-preserving Automatic Speaker Diarization | [링크](https://arxiv.org/abs/2210.14995) | paper | 2022 | A |
| P-08 | ACM ASPLOS 2025 — Fast On-device LLM Inference with NPUs | [링크](https://dl.acm.org/doi/10.1145/3669940.3707239) | paper | 2025 | A |
| P-09 | arXiv:2509.23324 — Scaling LLM Test-Time Compute with Mobile NPU | [링크](https://arxiv.org/abs/2509.23324) | paper | 2025-09 | A |
| T-01 | Samsung Electronics — US20230419979A1 Online Speaker Diarization (Local/Global Clustering) | [링크](https://patents.google.com/patent/US20230419979A1/en) | patent | 2023 | A |
| T-02 | Google LLC — US12125501B2 Face-aware Speaker Diarization | [링크](https://patents.google.com/patent/US12125501B2/en) | patent | 2024 | A |
| T-03 | Samsung Electronics — US11074910B2 Electronic Device for Recognizing Speech | [링크](https://uspto.report/patent/grant/11,074,910) | patent | 2021 | A |

---

## 첨부: 데이터 부족 주의

이 평가는 다음 항목의 공개 데이터 부재로 인해 신뢰도가 제한됨:

1. **온디바이스 화자분할 배터리 소모** (30분 연속 통화 기준) — Picovoice Falcon / SpeakerKit 미공개
2. **한국어 화자분할 DER** — 공개 벤치마크 없음
3. **고객 WTP** — SKT 에이닷 유료화 연기만 증거
4. **통신사 B2C 매출 모델** — 공개 전략 없음

**권장**: 의사결정 전에 PoC 실시 (1~2개월)로 배터리/정확도/WTP 검증 필수.

---

**작성일**: 2026-03-10
**분석자**: WTIS Skill-1 (Sonnet 4.5)
**신뢰도**: Medium (기술 성숙도 A, 시장 신뢰도 C, WTP/배터리 D)
**다음 평가 주기**: 2026-06 (B2B PoC 결과 반영)

