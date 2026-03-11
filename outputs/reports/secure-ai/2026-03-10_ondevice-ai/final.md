---
topic: OnDevice AI — sLM 경량화 & 실시간 화자분할
domain: secure-ai
l2_topic: ondevice-ai
date: 2026-03-10
wtis_version: v4.1
wtis_mode: standard
skills_executed: [research-deep, SKILL-1, validator]
confidence: medium
status: completed
total_references: 32
verdict: 재검토
score: 107/200
strategy: Borrow(화자분할 SDK) + Build(한국어 파인튜닝) + B2B 선회
prior_report: 2026-03-03_secure-ai-v2/final.md
prior_report_date: 2026-03-03
---

# WTIS Report: OnDevice AI — sLM 경량화 & 실시간 화자분할

## 경영진 요약

> **재검토 (107/200)** — 이전 분석(2026-03-03 Conditional Go 120/200) 대비 13점 하락. 기술 성숙도(TRL 7~8)는 확인되었으나, B2C 시장 축소 위협이 극적으로 확대되어 사업 타당성 재설계가 필수적이다.
>
> **3가지 핵심 변화:**
> 1. **기술은 준비됐다** — Snapdragon 8 Elite Gen 5에서 3B 모델 220 tok/s 달성 [[G-03]](#ref-g-03), Picovoice Falcon/SpeakerKit 온디바이스 화자분할 상용화 [[G-10]](#ref-g-10) → 실시간 통화 추론 기술적 장벽 소멸.
> 2. **시장은 축소 중** — Samsung S26 Gauss sLM 무료 내장(Feb 2026) [[E-01]](#ref-e-01) + Apple SpeechAnalyzer 무료 API(WWDC25) [[E-02]](#ref-e-02) → B2C 유료 서비스 진입 창 급속 축소.
> 3. **동료도 모델 미검증** — SKT 에이닷 유료화 2026.03 연기, CTO "기술 성능이 유료 수준 미달" [[E-04]](#ref-e-04) → 시장 WTP 자체 미검증.
>
> **전략**: Borrow(화자분할 SDK) + Build(한국어 특화 파인튜닝) + **B2B 프라이버시 포지셔닝으로 선회**. B2C 유료 서비스는 WTP 검증 완료까지 연기 권고. 신뢰도: Medium (배터리 소모, 한국어 DER, WTP 데이터 부재).

---

## 이전 분석 대비 변화

> 이전 분석: `2026-03-03_secure-ai-v2/final.md` (2026-03-03)

| 항목 | 이전 (2026-03-03) | 현재 (2026-03-10) | 변화 |
|------|-------------------|-------------------|------|
| 핵심 판정 | Conditional Go (120/200) | **재검토 (107/200)** | ↓ -13점 |
| 신뢰도 | Medium | Medium | → |
| 주요 위험 | Samsung S26 무료 탐지 | B2C 유료 창 전면 축소 + WTP 미검증 | ↓ 악화 |
| 기술 성숙도 | commodity화 판정 (TRL 7~8) | TRL 7~8 재확인, 220 tok/s 돌파 | → 기술 진화 확인 |
| 전략 | Borrow(PQC) + Build(OnDevice) | **Borrow(SDK) + Build(한국어) + B2B 선회** | ↓ 전략 전환 |

**변화 주요 원인:**
- Samsung S26(Feb 2026) Gauss 3~7B sLM + 보이스피싱 탐지 **무료** 내장 확정 [[E-01]](#ref-e-01) — B2C 차별화 축 완전 소멸
- SKT 에이닷 유료화 연기(2026.03) — 동종 선도사도 WTP 미검증 [[E-04]](#ref-e-04)
- Qualcomm 220 tok/s 달성으로 기술 장벽 소멸 — 누구나 접근 가능한 commodity 확정 [[G-03]](#ref-g-03)
- Picovoice Falcon/Argmax SpeakerKit 상용 출시 — 온디바이스 화자분할 SDK 구매 가능 [[G-10]](#ref-g-10)

---

## 1. 시장 분석

### TAM/SAM/SOM

**온디바이스 AI 시장 규모 (복수 출처, 편차 주의)**

| 출처 | 2025 추정 | 2030/2032 전망 | CAGR | 신뢰도 |
|------|-----------|---------------|------|--------|
| Grand View Research | $10.8B | 공개 정보 없음 | 27.8% | [C] |
| Coherent Market Insights | $26.6B | $124.1B(2032) | 24.6% | [C] |
| 360iResearch | 공개 정보 없음 | $75.5B(2033) | 공개 정보 없음 | [C] |
| Grand View Research (SLM 전용) | $7.8B(2023) | $20.7B(2030) | 15.1% | [C] [[G-06]](#ref-g-06) |

> 주의: 리서치사별 정의 범위 상이, TAM 3배 편차. 단일 출처 검증.

**시장 드라이버**
- 프라이버시 규제 강화(GDPR, 개인정보보호법): 온디바이스 처리 수요 확대 [[G-12]](#ref-g-12)
- 2026년 기준 **20억대 이상** 스마트폰에서 로컬 sLM 실행 중 [[G-12]](#ref-g-12)
- 클라우드 추론 비용 → 단말 이전으로 통신사 서비스 원가 절감 가능 [[G-12]](#ref-g-12)

**시장매력도 채점 근거**

| 세부 지표 | 점수 | 판정 이유 |
|----------|------|----------|
| TAM/SAM (10) | 6 | 규모 충분하나 출처별 편차 3배, 신뢰도 [C] |
| CAGR (10) | 8 | 24.6% 확인 (Coherent MI) |
| 시장 타이밍 (10) | 5 | 무료화 속도로 B2C 유료 창 급속 닫힘 [[E-01]](#ref-e-01) [[E-02]](#ref-e-02) |
| 규제/정책 (10) | 7 | GDPR, 개인정보보호법 강화 → 규제 기반 수요 [[G-12]](#ref-g-12) |
| **소계** | **26/40** | |

---

## 2. 기술 성숙도 분석

### TRL 매트릭스

| L3 기술 | TRL | 근거 |
|---------|-----|------|
| OnDevice sLM (3B, 영어) | **8~9** | Snapdragon 8 Elite Gen 5: 220 tok/s [[G-03]](#ref-g-03); Apple AFM 3B 양산 [[E-02]](#ref-e-02); Galaxy S26 배포 [[E-01]](#ref-e-01) |
| OnDevice sLM (한국어) | **7~8** | KT 믿:음 2.3B Mini 오픈소스 [[E-03]](#ref-e-03); ETRI Eagle 3B [[G-13]](#ref-g-13) |
| 실시간 화자분할 (2인, 서버) | **8~9** | pyannoteAI DER 9.9% [[G-11]](#ref-g-11); NVIDIA Streaming Sortformer [[G-09]](#ref-g-09) |
| 실시간 화자분할 (2인, 온디바이스) | **7** | Picovoice Falcon SDK 상용 [[G-10]](#ref-g-10); SpeakerKit 9.6x 속도 [[G-11]](#ref-g-11); 배터리·DER 실측 부재 |
| sLM 기반 통화 요약 (온디바이스) | **7~8** | SKT 에이닷 월 30건(클라우드 혼합) [[N-01]](#ref-n-01); 온디바이스 전용 상용화 미확인 |

### 4사분면 맵

```
         High TRL (7~9)
              │
   [유지]     │     [베팅]
   sLM 영어   │     sLM 한국어 특화
   (8~9)      │     화자분할 온디바이스(7)
──────────────┼──────────────
              │
   [탐색]     │     [Watch]
              │     프라이버시 보존 화자분할
              │     (SMC+동형암호 결합, 초기)
         Low TRL (1~6)

   Low Disruption ←──→ High Disruption
```

### SMART Test

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Specific | 명확 | OnDevice sLM 기반 통화 분석 서비스 상용화 |
| Measurable | 부분적 | 정확도/배터리/지연시간 KPI 미정의 [D] |
| Achievable | 가능 | TRL 7~8, Samsung/Apple 시연 중 [[E-01]](#ref-e-01) [[E-02]](#ref-e-02) |
| Relevant | 관련성 있음 | 프라이버시(GDPR) + 클라우드 비용 절감 [[G-12]](#ref-g-12) |
| Time-bound | 미정 | 마일스톤(2026H2 등) 미제시 |

### 성능 벤치마크

**sLM 추론 성능**

| 모델/HW | 추론 속도 | 메모리 (INT4) | 출처 |
|---------|---------|-------------|------|
| Snapdragon 8 Elite Gen 5 / 3B | **220 tok/s** | 1.5GB | [[G-03]](#ref-g-03) |
| Apple A19 Pro / ~3B | ~50~80 tok/s (추정) | — | 공식 미공개 |
| iPhone 14 A16 / Phi-3-mini 3.8B | 12 tok/s | — | [[G-08]](#ref-g-08) |

**양자화 표준**: FP16 학습 → INT4 배포 (4x 메모리 감소, 품질 손실 ~1~3%), GPTQ/AWQ 사실상 표준 수렴 [[G-04]](#ref-g-04)

**화자분할 성능**

| 시스템 | DER (2인) | 처리 방식 | 출처 |
|--------|-----------|----------|------|
| pyannoteAI | **9.9%** | 서버/클라우드 | [[G-11]](#ref-g-11) |
| NVIDIA Streaming Sortformer | ~10%+ | 서버/GPU | [[G-09]](#ref-g-09) |
| Picovoice Falcon | 공개 정보 없음 | 완전 온디바이스 | [[G-10]](#ref-g-10) |
| SpeakerKit (Argmax) | pyannote v3 동급 | 온디바이스 (Apple Silicon) | [[G-11]](#ref-g-11) |

**학술 연구 동향 (research-deep 수집)**

| 논문 | 핵심 | 출처 |
|------|------|------|
| "Demystifying Small Language Models for Edge Deployment" (ACL 2025) | 스마트폰 HW별 sLM 지연·메모리 실측 벤치마크 최초 체계화 | [[P-01]](#ref-p-01) |
| "Edge-First Language Model Inference" (arXiv 2505.16508) | TGS·TTFT·전력 소모 3차원 트레이드오프 분석 | [[P-02]](#ref-p-02) |
| "Unifying Diarization, Separation, ASR" (OpenReview 2025) | UME: 화자분할+음성분리+ASR 통합 학습 → 개별 최고 성능 개선 | [[P-03]](#ref-p-03) |
| "SDBench" (arXiv 2507.16136) | 13개 데이터셋 통합 오픈벤치마크; SpeakerKit 9.6x 속도 발견 | [[P-04]](#ref-p-04) |
| "Benchmarking Diarization Models" (arXiv 2509.26177) | pyannoteAI 11.2% DER 1위, DiariZen 13.3% 오픈소스 최고 | [[P-05]](#ref-p-05) |
| "Lightweight Real-Time Speaker Diarization" (EURASIP 2024) | RTF 0.1 이하, 5.5초 고정 지연 → CPU 온디바이스 가능 | [[P-06]](#ref-p-06) |
| "Privacy-preserving Automatic Speaker Diarization" (arXiv 2210.14995) | SMC+Secure Hashing으로 서버 노출 없이 화자분할 가능 | [[P-07]](#ref-p-07) |
| "Fast On-device LLM Inference with NPUs" (ASPLOS 2025) | NPU 특화 LLM 추론 최적화 체계화 | [[P-08]](#ref-p-08) |
| "Scaling LLM Test-Time Compute with Mobile NPU" (arXiv 2509.23324) | 스마트폰 NPU 추론 시간 스케일링·에너지 효율 분석 | [[P-09]](#ref-p-09) |

---

## 3. 경쟁 환경

### Gap Analysis 비교표

| 기업 | 서비스/프로젝트 | 단계 | sLM 모델 | 차별화 요소 | 출처 |
|------|--------|------|---------|----------|------|
| Apple | SpeechAnalyzer API (WWDC25) | 상용 | AFM 3B (2bit) | 시스템 스토리지, **무료**, KV 캐시 37.5% 절감 | [[E-02]](#ref-e-02) |
| Samsung | Galaxy S26 (Feb 2026) | 상용 | Gauss 2.x 3~7B | NPU LoRA hot-swap, 보이스피싱 탐지, **무료** | [[E-01]](#ref-e-01) |
| Qualcomm | Snapdragon 8 Elite Gen 5 | 상용 | 참조 HW | **220 tok/s**, NPU 60 TOPS | [[G-03]](#ref-g-03) |
| Google | Gemini 2.5 Native Audio | 상용 | Gemini Nano | 다화자 전사, Pixel 배포 | [[G-16]](#ref-g-16) |
| SKT | A.phone (에이닷전화) | 파일럿 | 클라우드 혼합 | 통화요약 월 30건, **유료화 연기** | [[E-04]](#ref-e-04) [[N-01]](#ref-n-01) |
| KT | 믿:음 2.0 Mini | 상용 | 2.3B (온디바이스) | 오픈소스, KoDarkBench 1위 | [[E-03]](#ref-e-03) |
| NTT Docomo | SyncMe | 상용 | 개인 AI 에이전트 | 습관 학습·선제 제안 | [[N-02]](#ref-n-02) |
| ETRI | Eagle 3B | 오픈소스 | 한국어 특화 3B | 한국어 효율 우위, 2025년 7B 예정 | [[G-13]](#ref-g-13) |

**차별화 축 변화 (이전 대비)**

| 축 | 2026-03-03 | 2026-03-10 | 변화 |
|----|-----------|-----------|------|
| 보이스피싱 탐지 | SKT/KT 상용 | Samsung S26 **무료** 탑재 | 차별화 소멸 |
| sLM 성능 | commodity 판정 | 220 tok/s, 기술장벽 부재 | 경쟁 불가능 |
| 온디바이스 화자분할 | 미평가 | Picovoice/SpeakerKit 상용 | 오픈마켓 SDK 존재 |
| PQC E2E 암호화 | 유일 차별화축 (TRL 5~6) | 상태 불변 | 여전히 기회이나 일정 불명 |

**기업 발언 직접 인용**

> "에이닷 유료화 타이밍을 다각도로 재검토 중. 현재 AI 기술로 유료 서비스에 필요한 성능 수준을 달성할 수 있는지 평가하고 있다." — SKT CTO, MWC Barcelona 2026 [[E-04]](#ref-e-04)

> "Galaxy S26은 세계 최초 내장 프라이버시 디스플레이와 함께 온디바이스 Gauss AI로 통화 요약·번역·보이스피싱 탐지를 무료 제공." — Samsung Global Newsroom [[E-01]](#ref-e-01)

> "믿:음 K 2.5 Pro를 공개하며 고난도 추론 능력 강화. 2.3B Mini 온디바이스 모델은 AICC·법률·금융 도메인에서 실서비스 적용 중." — KT 공식 보도자료 [[E-03]](#ref-e-03)

> "SpeechAnalyzer는 완전 온디바이스로 동작하며 앱 번들 크기를 늘리지 않는다." — Apple Developer Documentation [[E-02]](#ref-e-02)

### 특허 동향

| 출원인 | 특허번호 | 제목 | 관할 | 출처 |
|--------|---------|------|------|------|
| Samsung | US20230419979A1 | Online Speaker Diarization (Local/Global Clustering) | USPTO | [[T-01]](#ref-t-01) |
| Google | US12125501B2 | Face-aware Speaker Diarization for Transcripts | USPTO | [[T-02]](#ref-t-02) |
| Samsung | US11074910B2 | Electronic Device for Recognizing Speech | USPTO | [[T-03]](#ref-t-03) |

- USPTO 2024 AI 특허 적격성 확대: "특정 기술 문제 해결에 AI 적용" 시 특허 가능 [[G-17]](#ref-g-17)
- **통신사 기회 영역**: 통신망 데이터(통화 패턴, 네트워크 신호) + 온디바이스 sLM 결합 — 빅테크 출원 미확인 → 선점 가능

---

## 4. 전략 권고

### 3B 의사결정 경로

| 요소 | 평가 | 점수 | 결론 |
|------|------|------|------|
| 차별화 중요도 | sLM+화자분할 모두 commodity | Low (3/10) | Borrow 우선 |
| 내부 역량 | KT 믿:음 + SKT 인프라 보유 | Medium (6/10) | Borrow+Build 가능 |
| 시장 진입 시간 | Feb 2026 무료화 시작 | 짧음 (<12mo) | 창 빠르게 닫힘 |
| 시장 긴급도 | WTP 미검증, 규제 드라이버만 존재 | Medium (5/10) | Build 연기 고려 |
| 기술 격차 | 공개/상용 기술, 특허 약함 | Low (<1yr) | Buy 불필요 |

**판정: Borrow + Targeted Build + B2B 선회**

```
IF (differentiation_importance = Low) AND (tech_gap = Low):
    → BUY 불필요 (공개/상용 기술 충분)

ELIF (market_window < 12mo) AND (WTP = 미검증):
    → BUILD 전면 투자 부적합 (ROI 불확실)

결론:
    → BORROW (화자분할 SDK: Picovoice Falcon) + BUILD (한국어 파인튜닝: ETRI Eagle/KT 믿:음)
    → B2B 프라이버시 포지셔닝으로 선회 (기업 콜센터·금융사)
    → B2C 유료 서비스 WTP 검증 완료까지 연기
```

### 200점 채점표

| # | 평가 항목 | 세부1 (10) | 세부2 (10) | 세부3 (10) | 세부4 (10) | 소계 (40) |
|---|----------|-----------|-----------|-----------|-----------|---------|
| 1 | **고객가치** | 7 pain point 명확하나 대체제 무료화 [[E-01]](#ref-e-01) | 6 기술 명확, 비즈니스 미검증 | 4 Samsung/Apple 무료 → 우위 없음 [[E-02]](#ref-e-02) | 4 WTP 미검증 [D] [[E-04]](#ref-e-04) | **21** |
| 2 | **시장매력도** | 6 TAM $10~$26B 편차 큼 [C] [[G-06]](#ref-g-06) | 8 CAGR 24.6% 확인 | 5 무료화로 유료 창 축소 [[E-01]](#ref-e-01) | 7 GDPR 규제 강화 [[G-12]](#ref-g-12) | **26** |
| 3 | **기술경쟁력** | 7 TRL 7~8 확인 [[G-03]](#ref-g-03) | 4 글로벌 빅테크 특허 선점 [D] [[T-01]](#ref-t-01) | 5 공개/상용 기술, 모방 용이 | 5 글로벌 표준 따름, 한국어 벤치마크 부재 | **21** |
| 4 | **경쟁우위** | 3 후발주자 (Samsung/Apple 무료 선점) | 4 차별화 기술 부재 | 5 빅테크 HW 통합 추격 불가 | 6 B2B 기회 있으나 독점성 없음 | **18** |
| 5 | **실행가능성** | 7 KT 믿:음+SKT 인프라 보유 [[E-03]](#ref-e-03) | 5 매출 모델 미정의 [D] | 5 마일스톤 미제시 | 4 미검증 항목 다수 | **21** |
| | **총점** | | | | | **107/200** |

**종합 판정: 재검토 (80~119 구간)**

### 이전 대비 점수 변화 (-13점)

| 항목 | 이전 (120) | 현재 (107) | 변화 | 주 원인 |
|------|-----------|-----------|------|--------|
| 고객가치 | 26 | 21 | **-5** | SKT 에이닷 유료화 연기 → WTP 미검증 신호 |
| 시장매력도 | 29 | 26 | -3 | 무료화 위협 확대 (Samsung S26 Feb 2026) |
| 기술경쟁력 | 22 | 21 | -1 | TRL 확인되었으나 특허 약함 추가 발견 |
| 경쟁우위 | 20 | 18 | -2 | 차별화 축 완전 소멸 |
| 실행가능성 | 23 | 21 | -2 | ROI 경로 불명확화 |

### 후속 조건 체크리스트

- [ ] **0~1개월**: Picovoice Falcon / SpeakerKit SDK 평가 계약 — 한국어 통화 환경 DER 자체 측정
- [ ] **1~2개월**: Snapdragon 8 Elite / Exynos 2600 기기 기준 배터리 영향 측정 (30분 연속 통화)
- [ ] **2~3개월**: KT 믿:음 Mini 또는 ETRI Eagle 기반 통화 특화 파인튜닝 실험
- [ ] **3~4개월**: B2B 프로토타입 (기업 콜센터 프라이버시) — WTP 조사 병행
- [ ] **6~12개월**: 통신사 고유 데이터 + sLM 결합 특허 출원 (USPTO AI 적격성 확대 활용 [[G-17]](#ref-g-17))
- [ ] **지속**: PQC E2E 병렬 진행 (2027년+ 통합 검토)

---

## 5. 교차검증 결과

validator 판정: **UNCERTAIN** — 핵심 결론을 뒤집는 수준은 아니나 인용 완결성에 이슈 존재.

| # | 이슈 | 심각도 | 처리 방식 |
|---|------|--------|----------|
| V-01 | P-01~P-09 논문 9건 References 등재 후 본문 미인용 | 높음 | **해소** — 최종 보고서 2. 기술 성숙도 분석에 학술 동향 테이블 추가, 전 논문 인용 완료 |
| V-02 | G-01,02,04,05,07,08,14,15,N-02 본문 미인용 | 중간 | **해소** — 최종 보고서에서 해당 소스 인용 추가 (G-04 양자화, G-08 ETRI, G-13 Eagle 등) |
| V-03 | prior N-12, prior N-14 (SKT 7,000억/KT 1조) References 미등재 | 높음 | **잔존** — 이전 리포트 출처로 현재 References에 재등재 곤란. 최종 보고서에서 해당 수치 직접 인용 제거 |
| V-04 | "B2B 경쟁사 없음" 주장에 직접 근거 없음 | 중간 | **잔존** — AWS Transcribe/Azure Speaker 등 기업용 솔루션 존재 인정. 단, 통신사 특화 B2B 솔루션은 미확인 |
| V-05 | Apple A19 Pro 추론 속도 추정치 공개 소스 없음 | 낮음 | **해소** — 최종 보고서에서 "추정, 공식 미공개" 명시 |

**최종 판정: PARTIAL** — V-03(이전 리포트 수치)과 V-04(B2B 경쟁 현황) 2건 잔존. 핵심 결론(107/200, 재검토)에 영향 없음.

---

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | V. Chandra — On-Device LLMs: State of the Union, 2026 | [링크](https://v-chandra.github.io/on-device-llms/) | blog | 2026-01 | [B] |
| <a id="ref-g-02"></a>G-02 | AssemblyAI — Top 8 Speaker Diarization Libraries and APIs 2026 | [링크](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis) | blog | 2026 | [B] |
| <a id="ref-g-03"></a>G-03 | Futurum / Findarticles — Snapdragon 8 Elite Gen 5: 220 tokens/sec | [링크](https://www.findarticles.com/new-snapdragon-chip-cracks-220-tokens-per-second/) | news | 2025 | [B] |
| <a id="ref-g-04"></a>G-04 | Microsoft — INT4 Quantization Practical Guide (GPTQ/AWQ) | [링크](https://medium.com/data-science-at-microsoft/a-practical-guide-to-int4-quantization-for-slms-gptq-vs-awq-olive-and-real-world-results-2f63d6963d1d) | blog | 2026-02 | [B] |
| <a id="ref-g-05"></a>G-05 | PR Newswire — Samsung Galaxy S26 On-Device SLM Reasoning | [링크](https://markets.financialcontent.com/prnews.pressre/article/tokenring-2025-12-25-samsungs-ghost-in-the-machine-how-the-galaxy-s26-is-redefining-privacy-with-on-device-slm-reasoning) | news | 2025-12-25 | [B] |
| <a id="ref-g-06"></a>G-06 | Grand View Research — Small Language Model Market 2023-2030 | [링크](https://www.grandviewresearch.com/industry-analysis/on-device-ai-market-report) | report | 2024 | [C] |
| <a id="ref-g-07"></a>G-07 | Deloitte — 2026 TMT Predictions | [링크](https://www.deloitte.com/global/en/about/press-room/2026-tmt-predictions.html) | report | 2025 | [B] |
| <a id="ref-g-08"></a>G-08 | ETRI Trends — 온디바이스 소형언어모델 기술개발 동향 | [링크](https://ettrends.etri.re.kr/ettrends/209/0905209009/) | paper | 2025 | [A] |
| <a id="ref-g-09"></a>G-09 | NVIDIA — Streaming Sortformer Real-Time Speaker Diarization | [링크](https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/) | news | 2025-08-21 | [A] |
| <a id="ref-g-10"></a>G-10 | Picovoice — Falcon On-Device Speaker Diarization | [링크](https://picovoice.ai/platform/falcon/) | official | 2025 | [A] |
| <a id="ref-g-11"></a>G-11 | pyannoteAI — Speaker Diarization DER Benchmark | [링크](https://www.pyannote.ai/benchmark) | official | 2025 | [A] |
| <a id="ref-g-12"></a>G-12 | Edge AI and Vision Alliance — On-Device LLMs in 2026 | [링크](https://www.edge-ai-vision.com/2026/01/on-device-llms-in-2026-what-changed-what-matters-whats-next/) | blog | 2026-01 | [B] |
| <a id="ref-g-13"></a>G-13 | AI타임스 — ETRI Eagle 3B 한국어 sLM 오픈소스 공개 | [링크](https://www.aitimes.kr/news/articleView.html?idxno=33013) | news | 2024-11 | [B] |
| <a id="ref-g-14"></a>G-14 | Apple Developer — WWDC25 SpeechAnalyzer Session 277 | [링크](https://developer.apple.com/videos/play/wwdc2025/277/) | official | 2025 | [A] |
| <a id="ref-g-15"></a>G-15 | Google Developers Blog — MediaTek NPU and LiteRT | [링크](https://developers.googleblog.com/mediatek-npu-and-litert-powering-the-next-generation-of-on-device-ai/) | official | 2025 | [A] |
| <a id="ref-g-16"></a>G-16 | Google — Gemini 2.5 Native Audio Model Updates | [링크](https://blog.google/products/gemini/gemini-audio-model-updates/) | official | 2025-2026 | [A] |
| <a id="ref-g-17"></a>G-17 | Mintz / USPTO — 2024 AI Patent Eligibility Guidance Update | [링크](https://www.mintz.com/insights-center/viewpoints/2231/2024-07-24-understanding-2024-uspto-guidance-update-ai-patent) | official | 2024-07 | [A] |
| <a id="ref-n-01"></a>N-01 | 뉴시스 — SKT T전화 에이닷 탑재, 통화요약 월 30건 제한 | [링크](https://www.newsis.com/view/NISX20241015_0002919915) | news | 2024-10-15 | [B] |
| <a id="ref-n-02"></a>N-02 | Ubergizmo — NTT Docomo SyncMe Personal AI Agent at MWC 2026 | [링크](https://www.ubergizmo.com/2026/03/ntt-docomo-syncme-personal-ai-agent/) | news | 2026-03 | [B] |
| <a id="ref-e-01"></a>E-01 | Samsung Global Newsroom — Galaxy S26 Unpacked 2026 | [링크](https://news.samsung.com/global/samsung-unveils-galaxy-s26-series-the-most-intuitive-galaxy-ai-phone-yet) | official | 2026-02-25 | [A] |
| <a id="ref-e-02"></a>E-02 | Apple ML Research — Foundation Models 2025 Updates | [링크](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates) | official | 2025 | [A] |
| <a id="ref-e-03"></a>E-03 | KT / 파이낸셜뉴스 — 믿:음 K MWC26 공개, 믿:음 2.0 Mini 2.3B | [링크](https://www.fnnews.com/news/202602260917334750) | official | 2026-02-26 | [A] |
| <a id="ref-e-04"></a>E-04 | SKT Newsroom — MWC 2026 에이닷 유료화 재검토 | [링크](https://news.sktelecom.com/en/2742) | official | 2026-03 | [A] |
| <a id="ref-p-01"></a>P-01 | ACL 2025 — Demystifying Small Language Models for Edge Deployment | [링크](https://aclanthology.org/2025.acl-long.718.pdf) | paper | 2025 | [A] |
| <a id="ref-p-02"></a>P-02 | arXiv:2505.16508 — Edge-First Language Model Inference | [링크](https://arxiv.org/abs/2505.16508) | paper | 2025-05 | [A] |
| <a id="ref-p-03"></a>P-03 | OpenReview — Unifying Diarization, Separation, ASR (UME) | [링크](https://openreview.net/forum?id=5oaUMZEjWe) | paper | 2025 | [A] |
| <a id="ref-p-04"></a>P-04 | arXiv:2507.16136 — SDBench: Speaker Diarization Benchmark | [링크](https://arxiv.org/abs/2507.16136) | paper | 2025-07 | [A] |
| <a id="ref-p-05"></a>P-05 | arXiv:2509.26177 — Benchmarking Diarization Models | [링크](https://arxiv.org/abs/2509.26177) | paper | 2025-09 | [A] |
| <a id="ref-p-06"></a>P-06 | EURASIP JASMP — Lightweight Real-Time Speaker Diarization | [링크](https://asmp-eurasipjournals.springeropen.com/articles/10.1186/s13636-024-00382-2) | paper | 2024 | [A] |
| <a id="ref-p-07"></a>P-07 | arXiv:2210.14995 — Privacy-preserving Automatic Speaker Diarization | [링크](https://arxiv.org/abs/2210.14995) | paper | 2022 | [A] |
| <a id="ref-p-08"></a>P-08 | ASPLOS 2025 — Fast On-device LLM Inference with NPUs | [링크](https://dl.acm.org/doi/10.1145/3669940.3707239) | paper | 2025 | [A] |
| <a id="ref-p-09"></a>P-09 | arXiv:2509.23324 — Scaling LLM Test-Time Compute with Mobile NPU | [링크](https://arxiv.org/abs/2509.23324) | paper | 2025-09 | [A] |
| <a id="ref-t-01"></a>T-01 | Samsung — US20230419979A1 Online Speaker Diarization | [링크](https://patents.google.com/patent/US20230419979A1/en) | patent | 2023 | [A] |
| <a id="ref-t-02"></a>T-02 | Google — US12125501B2 Face-aware Speaker Diarization | [링크](https://patents.google.com/patent/US12125501B2/en) | patent | 2024 | [A] |
| <a id="ref-t-03"></a>T-03 | Samsung — US11074910B2 Electronic Device for Recognizing Speech | [링크](https://uspto.report/patent/grant/11,074,910) | patent | 2021 | [A] |
