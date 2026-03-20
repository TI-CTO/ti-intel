---
topic: Hybrid AI Infra
domain: agentic-ai
l2_topic: hybrid-ai-infra
date: 2026-03-16
wtis_version: v4.1
wtis_mode: standard
skills_executed: [research-deep, SKILL-1, validator]
confidence: medium
status: completed
total_references: 55
score: 131
verdict: Conditional Go
strategy: Borrow + Build (L3별 차등)
---

# WTIS Report: Hybrid AI Infra

## Executive Summary

> **Conditional Go — 131/200점, Borrow + Build 하이브리드 전략(L3별 차등), 신뢰도 Medium.**
>
> Hybrid AI Infra는 클라우드-엣지-단말 3계층 AI 추론 아키텍처의 통합을 목표로 하며, 4개 L3 기술(Speaker Diarization TRL 9, On-Device sLM TRL 8, Edge AI/MEC TRL 7~8, 5G SA/AI-RAN TRL 6~7)을 포함한다. Edge AI TAM은 $25.65B(2025) → $143B(2034), CAGR 21% [[G-16]](#ref-g-16)이며, AI-RAN TAM은 $2.96B(2025) → $37.2B(2035), CAGR 28.8% [[G-12]](#ref-g-12)로 시장매력도(35/40)가 최고 항목이다. 그러나 SKT의 AI Native 선언·AI-RAN Alliance 이사회 참여·A.X K1 풀스택 소버린 AI 구축 [[E-13]](#ref-e-13)과 KT의 5G SA 전국망·삼성 AI-RAN 상용망 검증 완료 [[E-15]](#ref-e-15)로 국내 경쟁사 대비 6개 역량 항목 모두 Behind 포지션이며, 경쟁우위(22/40)·실행가능성(20/40)이 취약하다. L3별 차별화된 3B 전략이 필요하며, Speaker Diarization(Buy+Build)과 On-Device sLM(Borrow+Build)은 단기 수확이 가능하고, AI-RAN은 Nokia 2027 상용화에 맞춘 중기 파트너십 확보(Borrow)가 요구된다.

---

## 1. 시장 분석

### TAM / SAM / SOM

| 구분 | 수치 | 출처 | 교차 검증 |
|------|------|------|-----------|
| **TAM (Edge AI)** | $25.65B(2025) → $143B(2034), CAGR 21% | [[G-16]](#ref-g-16) Precedence Research | ⚠️ validator 수치 보정: 원 리서치 "$47.6B(2026), CAGR 33.3%"는 출처 원본과 불일치. 실제 Precedence 페이지: $25.65B(2025), CAGR 21.04%. GVR $119B(2033) [[G-25]](#ref-g-25)과 방향성 일치 |
| **TAM (AI-RAN)** | $2.96B(2025) → $37.2B(2035), CAGR 28.8% | [[G-12]](#ref-g-12) Precedence Research | ⚠️ 원 리서치 시작점 "$3.81B(2026)"은 출처 기준연도(2025)와 불일치. CAGR 28.8%는 일치. 단일 소스 |
| **TAM (MEC)** | $7.78B(2025) → $175.8B(2033), CAGR 47.7% | [[G-17]](#ref-g-17) Precedence Research | 단일 소스. 본 보고서도 과대 추정 가능성 인정 |
| **Edge AI 교차검증** | $157B(2030) | [[G-18]](#ref-g-18) STL Partners | Precedence $143B(2034)와 시점 차에도 유사 규모 |
| **Edge AI 추가 교차** | $11.8B(2025) → $56.8B(2030), CAGR 36.9% | [[G-28]](#ref-g-28) BCC Research | 시작점 낮으나 고성장 방향 일치 |
| **SAM** | $3~4B (MEC 레이어 40~50%) | [D] 자체 추정 | 교차검증 미완료, 산식 근거 미제시 |
| **SOM (국내)** | $120~200M (2025), 글로벌 3~5% | [D] 자체 추정 | 교차검증 미완료 |

**시장매력도 채점 근거:**

| 세부 지표 | 점수 | 근거 |
|-----------|------|------|
| 시장 규모 | 9/10 | Edge AI TAM $143B(2034) [[G-16]](#ref-g-16), AI-RAN $37.2B(2035) [[G-12]](#ref-g-12). 복수 리서치사 방향성 수렴. -1은 리서치사별 편차(CAGR 21~37%) |
| 성장률 | 9/10 | CAGR 21~37%(출처별 상이, 방향성은 고성장 확실). BCC Research 36.9% [[G-28]](#ref-g-28), GVR, Precedence 교차 참조 |
| 시장 타이밍 | 8/10 | Speaker Diarization/On-Device sLM은 적시. AI-RAN은 2027 상용화 직전 진입 적기 [[E-05]](#ref-e-05). MEC 킬러 앱 대기 중 |
| 규제/정책 환경 | 9/10 | 과기정통부 1조 2,040억원 AI·ICT R&D [[G-08]](#ref-g-08). IITP 10대 이슈 온디바이스 AI 포함 [[G-21]](#ref-g-21) |
| **소계** | **35/40** | |

> **주의**: 시장 규모 수치는 리서치 기관별 정의 범위와 방법론이 상이하여 직접 비교 불가하다. 모든 수치는 [C] 이하 등급이며 방향성 참고용으로 활용한다. validator가 Edge AI CAGR 33.3%(SKILL-1 인용)과 실제 소스(21.04%) 간 12%p 이상 불일치를 확인하였으나, research-deep에서 복수 소스(BCC 36.9%, GVR, Precedence 21%, STL Partners)를 교차하면 **실질 CAGR 범위는 21~37%**로, 시장 규모 채점(9/10)의 근거는 유지된다. 다만 정확한 CAGR은 리서치사 합의 부재로 불확실하다.

**연도별 시장 규모 (Edge AI 복수 소스 비교):**

| 리서치사 | 시작점 | 종점 | CAGR | 출처 |
|----------|--------|------|------|------|
| Precedence Research | $25.65B (2025) | $143.06B (2034) | 21.04% | [[G-16]](#ref-g-16) |
| Grand View Research | — | $118.69B (2033) | — | [[G-25]](#ref-g-25) |
| BCC Research | $11.8B (2025) | $56.8B (2030) | 36.9% | [[G-28]](#ref-g-28) |
| STL Partners | — | $157B (2030) | — | [[G-18]](#ref-g-18) |

---

## 2. 기술 성숙도 분석

### TRL 4사분면 매트릭스

```
                   High TRL (7~9)
                        │
   [유지]               │               [베팅]
   Speaker Diarization  │   On-Device sLM (TRL 8)
   (TRL 9, Low Disrupt) │   (High Disruption)
                        │
                        │   Edge AI/MEC (TRL 7~8)
                        │   (High Disruption)
────────────────────────┼────────────────────────
                        │
   [탐색]               │               [Watch]
                        │   5G SA/AI-RAN (TRL 6~7)
                        │   (Very High Disruption)
                        │
                   Low TRL (1~6)

   Low Disruption  ←────────────→  High Disruption
```

### L3별 상세 TRL

| L3 기술 | TRL | 사분면 | 근거 | 시사점 |
|---------|-----|--------|------|--------|
| **Speaker Diarization** | 9 | 유지 | 콜센터 40%+ 기업 도입 완료. Falcon 온디바이스 SDK 상용 [[G-14]](#ref-g-14)[[G-19]](#ref-g-19). pyannote 3.1 DER ~10% [[G-27]](#ref-g-27) | 즉시 수확 가능. Buy(SDK) → 도메인 최적화 Build |
| **On-Device sLM** | 8 | 베팅 | SmolLM3/Qwen3.5/Gemma 3n Apache 2.0 출시 [[G-24]](#ref-g-24). Snapdragon 8 Elite 100+ tok/sec [[E-09]](#ref-e-09). NetoAI TSLAM-1.5B 텔레콤 특화 sLM 출시 [[G-26]](#ref-g-26) | 오픈소스 생태계 성숙. 통신사 Fine-Tuning이 차별화 핵심 |
| **Edge AI/MEC** | 7~8 | 베팅 | SKT 5GX Edge 운영 중 [[E-01]](#ref-e-01). 일반 엣지 AI(Jetson Orin 등) TRL 8~9이나 통신사 MEC AI 서비스는 TRL 6~7 | MEC 킬러 앱 부재가 최대 과제 [[G-11]](#ref-g-11) |
| **5G SA/AI-RAN** | 6~7 | Watch | Nokia 2027 상용화 확정 [[E-05]](#ref-e-05). KT-삼성 상용망 AI-RAN 검증 완료(성남, 1.8만 명) [[E-15]](#ref-e-15). 3GPP Rel-20 Two-sided AI 2027H2 [[G-15]](#ref-g-15) | 2027년 분수령. 파트너십 확보 단계 |

### SMART Test

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| **Specific** | **부분 충족.** On-Device sLM 추론 레이턴시 <20ms, Speaker Diarization DER <10%는 구체적이나, Edge AI 수익화·AI-RAN 에너지 효율 목표는 수치 미설정 | Snapdragon 8 Elite 100+ tok/sec, TTFT 0.12초 [[E-09]](#ref-e-09). pyannote DER ~10% [[G-27]](#ref-g-27) |
| **Measurable** | **충족.** 4개 L3 모두 산업 표준 지표 존재 (tok/sec, TTFT, DER%, W/Gbps, OPEX 절감률) | [[G-14]](#ref-g-14)[[P-01]](#ref-p-01) |
| **Achievable** | **L3별 차등 달성.** Speaker Diarization(즉시) → On-Device sLM(6~12개월) → Edge AI(12~24개월) → AI-RAN(24~36개월) | Falcon SDK 즉시 배포 [[G-14]](#ref-g-14). Nokia AI-RAN 2027 [[E-05]](#ref-e-05) |
| **Relevant** | **높음.** 통신사 AI 서비스 플랫폼 전환 + 5G SA 투자 수익화에 직결 | SKT AI Pyramid [[G-01]](#ref-g-01), KT Agentic AICC [[E-04]](#ref-e-04) |
| **Time-bound** | **부분 충족.** Nokia 2027 AI-RAN 명확, 자사 내부 마일스톤 미설정 | 3GPP Rel-20 2027H2 [[G-15]](#ref-g-15) |

### 성능 벤치마크

| 기술 | 지표 | 수치 | 출처 |
|------|------|------|------|
| On-Device sLM | Decode 속도 | 100+ tok/sec (Snapdragon 8 Elite) | [[E-09]](#ref-e-09) |
| On-Device sLM | TTFT | 0.12초 (FastVLM) | [[E-09]](#ref-e-09) |
| On-Device sLM | iPhone/Galaxy | 70+ tok/sec (Qwen3-600M INT8, Cactus v1) | [[G-13]](#ref-g-13) |
| Speaker Diarization | DER | ~10% (pyannote 3.1) | [[G-27]](#ref-g-27) |
| Speaker Diarization | 실시간 팩터 | 2.5% (NVIDIA V100) | [[G-27]](#ref-g-27) |
| Speaker Diarization | 온디바이스 지연 | 0.32초 (CoreML 2인 특화) | [[G-29]](#ref-g-29) |
| Edge AI | 추론 지연 | <20ms (온디바이스), 200~500ms (클라우드) | [[G-30]](#ref-g-30) |

---

## 3. 경쟁 환경

### 경쟁사 비교표

| Competitor | 유사 프로젝트 | Stage | Timeline | Source |
|------------|-------------|-------|----------|--------|
| **SKT** | AI Native 전환 (AI Pyramid). A.X K1 5,190억 MoE. 5GX Edge + AIDC 1GW+. AI-RAN Alliance 이사회. 삼성 AI-RAN MOU(2025-11). ATHENA 6G 백서. 에이닷 가입자 1,000만+ | 상용/파일럿 혼재 | Edge: 운영 중. AI-RAN: 2027 목표 | [[E-01]](#ref-e-01)[[E-02]](#ref-e-02)[[G-01]](#ref-g-01)[[G-10]](#ref-g-10)[[E-13]](#ref-e-13)[[E-14]](#ref-e-14) |
| **KT** | 5G SA 전국망(국내 유일). 삼성 AI-RAN 상용망 검증 완료(성남 1.8만 명). 믿:음 K 2.3B Mini. Agentic AICC(~300개사). MS 2.4조원 공동투자 | 상용(sLM/SA), 파일럿(AICC) | SA: 운영 중. AI-RAN: 검증 완료 | [[E-03]](#ref-e-03)[[E-04]](#ref-e-04)[[E-12]](#ref-e-12)[[E-15]](#ref-e-15)[[E-16]](#ref-e-16) |
| **Nokia** | AI-RAN 플랫폼 (Doksuri RRH + NVIDIA GH200). NVIDIA $1B 투자 유치 | 필드 트라이얼 | 2026 트라이얼 → 2027 상용 | [[E-05]](#ref-e-05)[[G-03]](#ref-g-03) |
| **Ericsson** | 자사 ASIC 기반 AI-RAN (NVIDIA 독립). T-Mobile Cloud RAN | 시연 완료 | 2026~2027 상용 목표 | [[E-06]](#ref-e-06)[[G-04]](#ref-g-04) |
| **DT/T-Mobile** | 6G Innovation Hub. AI Smart Call Assistant. AI-RAN OTA 검증 | 파일럿/R&D | 2026 Hub 출범 | [[E-07]](#ref-e-07)[[G-05]](#ref-g-05) |
| **NVIDIA** | 6G AI-native 플랫폼. AI Aerial SDK. 130개사+ 연합. 텔코 서베이 90% 긍정 ROI | 생태계 구축 | MWC 2026 분수령 | [[E-08]](#ref-e-08)[[G-06]](#ref-g-06)[[E-17]](#ref-e-17) |

### Gap Analysis

| 역량 항목 | 자사 포지션 | Gap 크기 | 근거 |
|-----------|-----------|---------|------|
| 자체 sLM | **Behind** (없음) | 중간 (KT 대비) | KT 믿:음 K 2.3B Mini 운영 중 [[E-12]](#ref-e-12). SKT A.X K1 풀스택 [[E-13]](#ref-e-13) |
| Edge AI/MEC 서비스 | **Behind** | 높음 (SKT 대비) | SKT 5GX Edge 운영 중 [[E-01]](#ref-e-01). 자사 MEC 서비스 미공개 |
| AI-RAN 로드맵 | **Behind** | 높음 | SKT AI-RAN Alliance 이사회 + 삼성 MOU [[E-14]](#ref-e-14). KT 상용망 검증 완료 [[E-15]](#ref-e-15) |
| Speaker Diarization | **Behind** | 높음 (KT 대비) | KT Agentic AICC 콜센터 자동화 시연 [[E-04]](#ref-e-04). 자사 Voice AI 미공개 |
| 표준화 기여 | **Behind** | 높음 | SKT ATHENA 6G 백서 [[E-11]](#ref-e-11). 삼성-SKT AI-RAN Alliance Work Item 채택 [[E-14]](#ref-e-14) |
| 글로벌 파트너십 | **Behind** | 높음 | SKT: NVIDIA, OpenAI, Singtel 등 [[E-01]](#ref-e-01). KT: MS 2.4조원 [[E-16]](#ref-e-16). 자사 미공개 |

> **종합**: 6개 역량 항목 모두 Behind. 경쟁사 대비 1~2년 후발 포지션. 빠른 파트너십 확보와 특화 영역 집중이 필수적.

### 주요 기업 발언

> **SKT (A.X K1, 2025-12-28)**: "SKT 정예팀은 AI 반도체, AI 데이터센터, AI 모델, AI 서비스에 이르는 전체 밸류체인을 독자 기술로 구축한 '풀스택 소버린 AI'를 완성했다. A.X K1은 총 5,190억 개의 매개변수로 구성되며, 추론 시 약 330억 개의 매개변수가 활성화되는 MoE 구조다." [[E-13]](#ref-e-13)

> **Samsung-SKT AI-RAN MOU (2025-11-26)**: "Samsung Research는 AI 기반 채널 추정, 스케줄러, 분산 MIMO 기술을 개발하고, SKT는 전국 상용망 기반 데이터 제공 및 테스트 인프라를 담당한다. 양사는 AI-RAN Alliance에서 AI 기반 채널 추정 기술을 Work Item으로 공식 채택시켰다." [[E-14]](#ref-e-14)

> **KT-삼성 AI-RAN 상용망 검증 (2025-12)**: "AI-RAN 최적화 기술은 사용자의 이동 경로와 사용 패턴에 따른 문제를 AI가 학습해 반복 발생 트렌드를 파악, 잠재적 문제를 사전에 예방한다. 성남 약 1.8만 명 대상 필드 테스트에서 접속 실패율이 크게 감소했다." [[E-15]](#ref-e-15)

> **NVIDIA Telecom Survey (2026-02)**: "89%의 텔코가 2026년 AI 지출을 확대할 계획이며, 90%가 AI가 수익과 비용에 긍정적 영향을 미쳤다고 응답했다. 자율 네트워크가 ROI 1위(50%) 사용 사례다." [[E-17]](#ref-e-17)

---

## 4. 전략 권고

### 3B 의사결정 경로 (L3별 차등)

본 L2는 4개 L3의 TRL이 6~9로 분산되어 있어 단일 3B 전략 적용이 부적합하다.

#### Speaker Diarization (TRL 9) → **Buy + Build**

| Factor | 평가 | 근거 |
|--------|------|------|
| Differentiation | 5/10 | 성숙 기술, 차별화보다 적용 속도가 중요 [[G-19]](#ref-g-19) |
| Internal capability | 낮음 | 자사 Voice AI 역량 미공개 |
| Market urgency | 8/10 | KT Agentic AICC 이미 시연 [[E-04]](#ref-e-04). 즉각 대응 필요 |
| Tech gap | ~1년 (KT 대비) | KT 2025-07 운영 시작 [[E-12]](#ref-e-12) |

**결정**: Market urgency 8/10, Tech gap ~1년 → **Buy**(Falcon SDK 또는 동급) + 통신 도메인 Fine-Tuning **Build**.

#### On-Device sLM (TRL 8) → **Borrow + Build**

| Factor | 평가 | 근거 |
|--------|------|------|
| Differentiation | 7/10 | 통신사 앱 내 프라이버시 보장 AI 서비스로 차별화 가능 [[E-02]](#ref-e-02) |
| Internal capability | 낮음 | 자사 sLM 없음. 오픈소스 활용 가능 [[G-24]](#ref-g-24) |
| Market urgency | 6/10 | 시장 초기. 2026년 내 파일럿 배포로 충분 |
| Tech gap | ~1년 (KT 대비) | KT 자체 모델 [[E-12]](#ref-e-12), SKT 외부 모델 활용 [[E-01]](#ref-e-01) |

**결정**: Differentiation 7/10이나 내부 역량 부족 → **Borrow**(오픈소스 + Qualcomm NPU 파트너십 [[E-09]](#ref-e-09)) + 통신 특화 Fine-Tuning **Build**.

#### Edge AI/MEC (TRL 7~8) → **Borrow**

| Factor | 평가 | 근거 |
|--------|------|------|
| Differentiation | 6/10 | MEC 플랫폼 표준화 경향. 킬러 앱이 차별화 요소 |
| Market urgency | 5/10 | "Architecture Deployed, Monetisation Pending" [[G-11]](#ref-g-11) |
| Tech gap | 1~2년 (SKT 대비) | SKT AWS Wavelength 5GX Edge 운영 중 [[E-01]](#ref-e-01) |

**결정**: 시장 긴급성 중간, 내부 역량 부족 → **Borrow**(하이퍼스케일러 파트너십) + 산업별 킬러 앱 공동 개발.

#### 5G SA/AI-RAN (TRL 6~7) → **Borrow**

| Factor | 평가 | 근거 |
|--------|------|------|
| Differentiation | 4/10 | 벤더 플랫폼 위 운영. 장비 선택이 핵심 |
| Market urgency | 4/10 | 필드 트라이얼 단계. 전략적 파트너십 우선 |
| Tech gap | 동등 | Nokia/Ericsson 상용화 전. 모든 통신사 유사 포지션 |

**결정**: 자체 개발 불가, 시장 미성숙 → **Borrow**(Nokia/Ericsson 필드 트라이얼 파트너십 + AI-RAN Alliance 참여). SKT Alliance 이사회 선점 [[G-10]](#ref-g-10)으로 파트너 접근에서 불리할 수 있음.

### L3별 가중치

| L3 기술 | 가중치 | 근거 |
|---------|-------|------|
| Speaker Diarization | 20% | 즉시 수확, 콜센터 직접 적용 [[G-14]](#ref-g-14) |
| On-Device sLM | 30% | 통신사 앱 차별화 핵심, 오픈소스 성숙 [[G-24]](#ref-g-24) |
| Edge AI/MEC | 25% | 5G 투자 수익화 핵심 경로 |
| 5G SA/AI-RAN | 25% | 중장기 인프라 전략적 중요도 높으나 시기 불확실 |

### 200점 채점표

| # | 평가 항목 | 세부1 (10) | 세부2 (10) | 세부3 (10) | 세부4 (10) | 소계 (40) |
|---|----------|-----------|-----------|-----------|-----------|----------|
| 1 | **고객가치** | pain point 심각도: **7** | 제공 가치 명확성: **7** | 대체제 대비 우위: **5** | 고객 수용성: **5** ⚠️ | **24** |
| 2 | **시장매력도** | 시장 규모: **9** | 성장률: **9** | 시장 타이밍: **8** | 규제/정책 환경: **9** | **35** |
| 3 | **기술경쟁력** | TRL 수준: **8** | 특허 포트폴리오: **5** ⚠️ | 기술 장벽: **8** | 표준/인증: **9** | **30** |
| 4 | **경쟁우위** | 시장 포지션: **4** | 차별화 지속성: **6** | 경쟁사 대응력: **7** | 생태계/파트너: **5** ⚠️ | **22** |
| 5 | **실행가능성** | 내부 역량: **5** ⚠️ | 투자 ROI: **5** ⚠️ | 일정 현실성: **6** | 리스크 관리: **4** | **20** |
| | **총점** | | | | | **131/200** |

> ⚠️ = 데이터 부족으로 보수적 평가 적용 항목 (5건)

### 채점 근거

**1. 고객가치 (24/40)**
- pain point 심각도 (7/10): 콜센터 AI 자동화, 5G SA 투자 수익화 지연, MEC 킬러 앱 부재는 실재 과제 [[G-11]](#ref-g-11)[[E-04]](#ref-e-04)
- 제공 가치 명확성 (7/10): Speaker Diarization + sLM → 콜센터 자동화, 온디바이스 프라이버시 AI는 명확. Edge AI/AI-RAN의 최종 고객 가치는 추상적 [[E-02]](#ref-e-02)
- 대체제 대비 우위 (5/10): Speaker Diarization SDK 다수 존재 [[G-19]](#ref-g-19)[[G-20]](#ref-g-20). 온디바이스 AI는 OS 벤더 무료 제공과 경쟁
- 고객 수용성 (5/10): WTP 검증 데이터 없음 ⚠️

**2. 시장매력도 (35/40)**
- 시장 규모 (9/10): Edge AI TAM $143B(2034), AI-RAN $37.2B(2035). TAM 1조원 초과 [[G-16]](#ref-g-16)[[G-12]](#ref-g-12)
- 성장률 (9/10): CAGR 범위 21~37%(출처별 상이). 방향성은 고성장 확실. 복수 리서치사 교차 확인
- 시장 타이밍 (8/10): Speaker Diarization/On-Device sLM 적시. AI-RAN 2027 직전 [[E-05]](#ref-e-05)
- 규제/정책 환경 (9/10): 과기정통부 1조 2,040억원 [[G-08]](#ref-g-08). IITP 10대 이슈 [[G-21]](#ref-g-21)

**3. 기술경쟁력 (30/40)**
- TRL 수준 (8/10): 4개 L3 평균 ~TRL 7.5. Speaker Diarization TRL 9이 견인
- 특허 포트폴리오 (5/10): 자사 특허 데이터 없음 ⚠️
- 기술 장벽 (8/10): AI-RAN은 통신+AI 융합으로 진입 장벽 높음 [[P-01]](#ref-p-01). sLM은 오픈소스로 장벽 낮으나 도메인 데이터 필요
- 표준/인증 (9/10): 3GPP Rel-18/19/20 명확 [[G-15]](#ref-g-15). AI-RAN Alliance 130개사+ [[E-08]](#ref-e-08)

**4. 경쟁우위 (22/40)**
- 시장 포지션 (4/10): 6개 역량 항목 모두 Behind [[E-01]](#ref-e-01)[[G-10]](#ref-g-10)
- 차별화 지속성 (6/10): 통신사 고유 자산(네트워크 컨텍스트, 가입자 데이터) 활용 가능하나 가설 단계
- 경쟁사 대응력 (7/10): AI-RAN은 벤더 플랫폼 기반이므로 유사 시점 접근 가능 [[E-05]](#ref-e-05)
- 생태계/파트너 (5/10): 자사 파트너십 미공개 ⚠️

**5. 실행가능성 (20/40)**
- 내부 역량 (5/10): AI Lab 역량 추정 가능하나 데이터 없음 ⚠️
- 투자 ROI (5/10): AI-RAN 투자 규모·회수 기간 미산출 ⚠️
- 일정 현실성 (6/10): Speaker Diarization 6개월 내 파일럿 가능. AI-RAN은 Nokia 2027 의존 [[E-05]](#ref-e-05)
- 리스크 관리 (4/10): NVIDIA 단일 의존 [[G-09]](#ref-g-09), OS 벤더 잠금 리스크 완화 전략 미수립

### 판정

| 총점 | 판정 기준 | 결과 |
|------|----------|------|
| **131/200** | 120~159: Conditional Go | **Conditional Go** |

### 후속 조건 체크리스트

- [ ] Speaker Diarization SDK 벤더 평가 (Picovoice Falcon vs. Speechmatics Flow vs. AssemblyAI) — 담당: AI 서비스팀, 기한: 2026-Q2
- [ ] 오픈소스 sLM(SmolLM3/Qwen3.5) 통신 도메인 Fine-Tuning PoC — 담당: AI Lab, 기한: 2026-Q3
- [ ] Nokia/Ericsson AI-RAN 필드 트라이얼 파트너십 타진 — 담당: 네트워크 전략, 기한: 2026-Q3
- [ ] AI-RAN Alliance 가입 검토 및 3GPP Rel-20 기고 참여 — 담당: 표준화팀, 기한: 2026-Q2
- [ ] 과기정통부 IITP 6G AI-RAN 국책 과제 컨소시엄 참여 — 담당: R&D 기획, 기한: 2026-Q3
- [ ] 자사 Edge AI/MEC 인프라 현황 조사 및 내부 역량 데이터(I-xx) 확보 — 담당: 인프라팀, 기한: 2026-Q2

---

## 5. 교차검증 결과

validator 판정: **PARTIAL** (심각 2건, 경미 7건)

### 심각 이슈

| # | 유형 | 내용 | 처리 |
|---|------|------|------|
| 1 | 수치 불일치 | Edge AI TAM 시작점 "$47.6B(2026)" 및 CAGR "33.3%"가 Precedence Research 실제 수치($25.65B, 2025, CAGR 21.04%)와 불일치 | **해소**: 본 최종 보고서에서 소스 원본 수치($25.65B, CAGR 21%)로 수정. 복수 소스(BCC 36.9%, GVR, STL Partners)를 교차하여 CAGR 범위 21~37%로 제시. 시장매력도 채점(9/10) 근거 유지 |
| 2 | 수치 불일치 | AI-RAN TAM 시작점 "$3.81B(2026)"이 Precedence Research 기준연도($2.96B, 2025)와 불일치 | **해소**: 본 보고서에서 $2.96B(2025)로 수정. CAGR 28.8%, 종점 $37.2B(2035)는 소스 일치 확인 |

### 경미 이슈

| # | 유형 | 내용 | 처리 |
|---|------|------|------|
| 3 | 고아 소스 | E-10(Apple Core ML Llama) — 본문 미인용 | **잔존**: 참조 가치 있으나 본문에서 직접 인용하지 않음. References에 유지 |
| 4 | 고아 소스 | G-07(Qualcomm Edge AI Workshops) — 본문 미인용 | **잔존**: 동일 |
| 5 | 고아 소스 | P-02(Han et al. 6G Networks) — 본문 미인용 | **잔존**: 동일 |
| 6 | 고아 소스 | P-03(Shokouhi & Wong O-RAN) — 본문 미인용 | **잔존**: 동일 |
| 7 | 고아 소스 | P-04(arXiv KV Cache) — 본문 미인용 | **잔존**: 동일 |
| 8 | 논리 | "통신사 인증 + 온디바이스 AI = 고유 가치 제안" — 인용 소스가 결론을 직접 지지하지 않음 | **인정**: 가설 수준 주장으로 재분류. 검증 필요 표기 |
| 9 | 논리 | "5G 슬라이싱 SLA 보장" — 인용 P-06, G-16이 직접 근거 아님 | **인정**: 기술적 가능성 수준 주장으로 완화 표현 |

최종 교차검증 판정: **PARTIAL → 심각 이슈 2건 해소, 경미 이슈 7건 중 5건 잔존(고아 소스, 참조 가치 유지)**

---

## References

### 기업 발언/보도자료 (E-xx)

| # | 출처 | URL | 발행일 | 신뢰도 |
|---|------|-----|--------|--------|
| <a id="ref-e-01"></a>E-01 | Telecoms Infrastructure Blog — SKT Builds AI Infrastructure Momentum with GPUaaS and Haein Cluster | [링크](https://www.telecomsinfrastructure.com/2026/03/sk-telecom-builds-ai-infrastructure.html) | 2026-03 | [B] |
| <a id="ref-e-02"></a>E-02 | Telecomstechnews — SKT Why the AI infrastructure bottleneck matters | [링크](https://www.telecomstechnews.com/news/sk-telecom-why-ai-infrastructure-bottleneck-matters/) | 2026 | [B] |
| <a id="ref-e-03"></a>E-03 | Korea IT Times — KT Showcases AI and K-Culture Innovations at MWC 2026 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151338) | 2026-03 | [B] |
| <a id="ref-e-04"></a>E-04 | Korea IT Times — KT Unveils Agentic AICC at MWC 2026 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151275) | 2026-03 | [B] |
| <a id="ref-e-05"></a>E-05 | Nokia Newsroom — Nokia expands network portfolio for AI-RAN era | [링크](https://www.nokia.com/newsroom/nokia-expands-network-portfolio-for-premium-performance-in-the-ai-ran-era-mwc26/) | 2026-03-01 | [A] |
| <a id="ref-e-06"></a>E-06 | Ericsson — T-Mobile boost portable AI RAN on NVIDIA platform | [링크](https://www.ericsson.com/en/news/2026/3/ericsson-t-mobile-boost-portable-ai-ran-on-nvidia-platform) | 2026-03-02 | [A] |
| <a id="ref-e-07"></a>E-07 | T-Mobile — T-Mobile and Deutsche Telekom Launch Joint 6G Innovation Hub | [링크](https://www.t-mobile.com/news/network/t-mobile-and-deutsche-telekom-6g-innovation-hub) | 2026-02-28 | [A] |
| <a id="ref-e-08"></a>E-08 | NVIDIA Newsroom — NVIDIA and Global Telecom Leaders 6G AI-Native Platforms | [링크](https://nvidianews.nvidia.com/news/nvidia-and-global-telecom-leaders-commit-to-build-6g-on-open-and-secure-ai-native-platforms) | 2026-03-01 | [A] |
| <a id="ref-e-09"></a>E-09 | Qualcomm — Snapdragon Wear Elite Press Release (MWC 2026) | [링크](https://www.qualcomm.com/news/releases/2026/03/qualcomm-powers-the-rise-of-personal-ai-with-new-snapdragon-wear) | 2026-03 | [A] |
| <a id="ref-e-10"></a>E-10 | Apple ML Research — Core ML on-device Llama 3.1 | [링크](https://machinelearning.apple.com/research/core-ml-on-device-llama) | 2025 | [A] |
| <a id="ref-e-11"></a>E-11 | SK Telecom Newsroom — ATHENA 6G White Paper | [링크](https://news.sktelecom.com/en/2751) | 2026-02-23 | [A] |
| <a id="ref-e-12"></a>E-12 | KT Enterprise — 믿음 K 2.0 온디바이스 Mini 모델 | [링크](https://enterprise.kt.com/pd/P_PD_NE_00_316.do) | 2025-07 | [A] |
| <a id="ref-e-13"></a>E-13 | SKT 뉴스룸 — A.X K1 5,190억 파라미터 MoE 풀스택 소버린 AI | [링크](https://news.sktelecom.com/217811) | 2025-12-28 | [A] |
| <a id="ref-e-14"></a>E-14 | Samsung Global Newsroom — Samsung-SKT AI-RAN MOU (채널 추정·분산 MIMO) | [링크](https://news.samsung.com/global/samsung-and-sk-telecom-join-forces-to-lead-6g-era-with-ai-ran-technology) | 2025-11-26 | [A] |
| <a id="ref-e-15"></a>E-15 | Samsung Global Newsroom — KT-삼성 AI-RAN 상용망 검증 (성남 1.8만 명) | [링크](https://news.samsung.com/global/samsung-electronics-and-kt-corporation-successfully-validate-ai-ran-on-commercial-networks-accelerating-6g-development) | 2025-12 | [A] |
| <a id="ref-e-16"></a>E-16 | 한국NGO신문 — KT, NVIDIA AI-RAN 글로벌 허브 구축 MOU | [링크](https://www.ngonews.kr/news/articleView.html?idxno=217442) | 2025-11 | [B] |
| <a id="ref-e-17"></a>E-17 | NVIDIA Blog — State of AI in Telecom 2026 Survey (90% ROI, 89% AI 지출 확대) | [링크](https://blogs.nvidia.com/blog/ai-in-telco-survey-2026/) | 2026-02 | [A] |

### 글로벌 출처 (G-xx)

| # | 출처 | URL | 발행일 | 신뢰도 |
|---|------|-----|--------|--------|
| <a id="ref-g-01"></a>G-01 | Telecompaper — SKT AI Pyramid Strategy | [링크](https://www.telecompaper.com/news/sk-telecom-ai-pyramid-strategy/) | 2025 | [B] |
| <a id="ref-g-02"></a>G-02 | Seoul.co.kr — KT, 6G로 AI 지능형 네트워크 시대 | [링크](https://www.seoul.co.kr/news/economy/industry/2026/03/03/20260303500004) | 2026-03-03 | [B] |
| <a id="ref-g-03"></a>G-03 | Fierce Network — Nokia promises commercial AI-RAN in 2027 | [링크](https://www.fierce-network.com/wireless/nokia-promises-commercial-ai-ran-2027) | 2026-03-02 | [B] |
| <a id="ref-g-04"></a>G-04 | Light Reading — Ericsson does AI-RAN minus Nvidia | [링크](https://www.lightreading.com/5g/ericsson-does-ai-ran-minus-nvidia-in-push-for-5g-silicon-freedom) | 2026-02-20 | [B] |
| <a id="ref-g-05"></a>G-05 | TelecomTV — DT, T-Mobile US unite for 6G R&D | [링크](https://www.telecomtv.com/content/6g/mwc26-dt-t-mobile-us-unite-for-6g-r-d-54958/) | 2026-03-02 | [B] |
| <a id="ref-g-06"></a>G-06 | NVIDIA Blog — Software-Defined AI-RAN Is the Next Wireless Generation | [링크](https://blogs.nvidia.com/blog/software-defined-ai-ran/) | 2026-03-01 | [B] |
| <a id="ref-g-07"></a>G-07 | Qualcomm Developer — Edge AI Workshops MWC 2026 | [링크](https://www.qualcomm.com/developer/events/mwc-talent-arena-2026) | 2026-03 | [A] |
| <a id="ref-g-08"></a>G-08 | AI Times — 과기정통부 온디바이스 AI 활성화, 1조 2,040억원 AI·ICT R&D | [링크](https://www.aitimes.com/news/articleView.html?idxno=157152) | 2025 | [B] |
| <a id="ref-g-09"></a>G-09 | Fierce Network — Intel sits out AI-RAN Alliance | [링크](https://www.fierce-network.com/wireless/mwc-2026-intel-sits-out-ai-ran-alliance-now) | 2026-03-02 | [B] |
| <a id="ref-g-10"></a>G-10 | Korea IT Times — SKT Declares Shift to AI Native Company at MWC 2026 | [링크](https://www.koreaittimes.com/news/articleView.html?idxno=151344) | 2026-03-01 | [B] |
| <a id="ref-g-11"></a>G-11 | Opensignal — 5G SA: Architecture Deployed, Monetisation Pending | [링크](https://insights.opensignal.com/2026/02/5g-standalone-state-of-play-architecture-deployed-monetisation-pending/dt) | 2026-02 | [B] |
| <a id="ref-g-12"></a>G-12 | Precedence Research — AI-RAN Market $2.96B(2025) → $37.19B(2035), CAGR 28.8% | [링크](https://www.precedenceresearch.com/ai-ran-market) | 2026 | [C] |
| <a id="ref-g-13"></a>G-13 | InfoQ — Cactus v1 Cross-Platform LLM Inference | [링크](https://www.infoq.com/news/2025/12/cactus-on-device-inference/) | 2025-12 | [B] |
| <a id="ref-g-14"></a>G-14 | Picovoice — Falcon Speaker Diarization SDK (100x Faster, 5x More Accurate) | [링크](https://picovoice.ai/blog/speaker-diarization/) | 2025 | [A] |
| <a id="ref-g-15"></a>G-15 | 3GPP — AI/ML for NG-RAN & 5G-Advanced towards 6G (Rel-18/19/20) | [링크](https://www.3gpp.org/technologies/ai-ml-ngran) | 2026-03 | [A] |
| <a id="ref-g-16"></a>G-16 | Precedence Research — Edge AI Market $25.65B(2025) → $143.06B(2034), CAGR 21% | [링크](https://www.precedenceresearch.com/edge-ai-market) | 2026 | [C] |
| <a id="ref-g-17"></a>G-17 | Precedence Research — MEC Market $7.78B → $175.8B, CAGR 47.7% | [링크](https://www.precedenceresearch.com/press-release/multi-access-edge-computing-market) | 2026 | [C] |
| <a id="ref-g-18"></a>G-18 | STL Partners — Edge AI $157B opportunity (2030) | [링크](https://stlpartners.com/research/edge-ai-market-forecast-computer-vision-leads-the-way/) | 2025 | [B] |
| <a id="ref-g-19"></a>G-19 | AssemblyAI — Top 8 Speaker Diarization Libraries and APIs 2026 | [링크](https://www.assemblyai.com/blog/top-speaker-diarization-libraries-and-apis) | 2026 | [B] |
| <a id="ref-g-20"></a>G-20 | MarkTechPost — Speaker Diarization 2025 Technical Guide | [링크](https://www.marktechpost.com/2025/08/21/what-is-speaker-diarization-a-2025-technical-guide-top-9-speaker-diarization-libraries-and-apis-in-2025/) | 2025-08-21 | [B] |
| <a id="ref-g-21"></a>G-21 | Byline Network — 2026년 IITP 10대 전망 온디바이스 AI 포함 | [링크](https://byline.network/2025/11/13-573/) | 2025-11 | [B] |
| <a id="ref-g-22"></a>G-22 | 경제미디어일보 — 통신망이 곧 컴퓨터다: SKT·KT AI-RAN 전략 비교 | [링크](https://www.economidaily.com/view/20260227172207712) | 2026-02-27 | [B] |
| <a id="ref-g-23"></a>G-23 | RCR Wireless — Telecom GPU-as-a-Service: Beyond the hype | [링크](https://www.rcrwireless.com/20251030/analyst-angle/telecom-gpu-as-a-service) | 2025-10-30 | [B] |
| <a id="ref-g-24"></a>G-24 | VentureBeat — Qwen3.5-9B beats GPT-OSS-120B (오픈소스 sLM 성능 돌파) | [링크](https://venturebeat.com/technology/alibabas-small-open-source-qwen3-5-9b-beats-openais-gpt-oss-120b-and-can-run) | 2026-03 | [B] |
| <a id="ref-g-25"></a>G-25 | Grand View Research — Edge AI Market $118.69B by 2033 | [링크](https://www.grandviewresearch.com/industry-analysis/edge-ai-market-report) | 2026 | [C] |
| <a id="ref-g-26"></a>G-26 | isStories — NetoAI TSLAM-1.5B Telecom Specific sLM | [링크](https://www.isstories.com/2025/03/04/netoai-launched-tslam-1-5b-telecom-specific-small-language-model-for-mobile-and-edge/) | 2025-03-04 | [B] |
| <a id="ref-g-27"></a>G-27 | pyannote — Speaker Diarization 3.1 (DER ~10%, 실시간 팩터 2.5%) | [링크](https://github.com/pyannote/pyannote-audio) | 2025 | [A] |
| <a id="ref-g-28"></a>G-28 | BCC Research — Edge AI Market $11.8B(2025) → $56.8B(2030), CAGR 36.9% | [링크](https://www.bccresearch.com/market-research/information-technology/edge-ai-market.html) | 2025 | [C] |
| <a id="ref-g-29"></a>G-29 | inference.plus — Near-Real-Time Speaker Diarization CoreML (0.32s latency) | [링크](https://inference.plus/p/low-latency-speaker-diarization-on) | 2025 | [C] |
| <a id="ref-g-30"></a>G-30 | TechCrates — Edge AI vs Cloud AI 2026: Latency <20ms vs 200~500ms | [링크](https://www.techcrates.com/edge-ai-vs-cloud-ai-2026-which-wins-for-business-efficiency/) | 2026 | [C] |
| <a id="ref-g-31"></a>G-31 | NVIDIA Streaming Sortformer — Real-Time Speaker Identification | [링크](https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/) | 2025 | [B] |
| <a id="ref-g-32"></a>G-32 | Argmax — pyannoteAI On-Device Diarization | [링크](https://www.argmaxinc.com/blog/pyannote-argmax) | 2025 | [B] |
| <a id="ref-g-33"></a>G-33 | O-RAN Alliance — 60 New/Updated Technical Documents (WG2 AI/ML API) | [링크](https://www.o-ran.org/blog/60-new-or-updated-o-ran-technical-documents-released-since-march-2025) | 2025 | [A] |
| <a id="ref-g-34"></a>G-34 | nybsys — Gen AI in Telecom: OPEX 20~25%, MTTR 30~50% | [링크](https://nybsys.com/generative-ai-in-telecom/) | 2025 | [C] |
| <a id="ref-g-35"></a>G-35 | CEOSCOREDAILY — SKT·KT·LGU+ '돈 버는 AI' 전략 비교 | [링크](https://ceoscoredaily.com/page/view/2024112913043906447) | 2024-11-29 | [B] |

### 학술 논문 (P-xx)

| # | 저자 | 년도 | 제목 | DOI/URL |
|---|------|------|------|---------|
| <a id="ref-p-01"></a>P-01 | Kundu et al. | 2025-01 | AI-RAN: Transforming RAN with AI-driven Computing Infrastructure | [arXiv](https://arxiv.org/abs/2501.09007) |
| <a id="ref-p-02"></a>P-02 | Han et al. | 2026-02 | Toward E2E Intelligence in 6G Networks | [arXiv](https://arxiv.org/abs/2602.23623) |
| <a id="ref-p-03"></a>P-03 | Shokouhi & Wong | 2026-02 | Agentic AI for Intent-driven Optimization in Cell-free O-RAN | [arXiv](https://arxiv.org/abs/2602.22539) |
| <a id="ref-p-04"></a>P-04 | arXiv | 2026-03 | Agent Memory Below the Prompt: Persistent Q4 KV Cache | [arXiv](https://arxiv.org/abs/2026.03) |
| <a id="ref-p-05"></a>P-05 | ACM DL | 2025 | Fast On-device LLM Inference with NPUs (ASPLOS 2025) | [ACM](https://dl.acm.org/doi/10.1145/3669940.3707239) |
| <a id="ref-p-06"></a>P-06 | arXiv | 2025-05 | Edge-First Language Model Inference: Models, Metrics, Tradeoffs | [arXiv](https://arxiv.org/html/2505.16508v1) |
| <a id="ref-p-07"></a>P-07 | Liu et al. | 2025-08 | SpeakerLM: E2E Speaker Diarization with Multimodal LLMs | [arXiv](https://arxiv.org/abs/2508.06372) |
| <a id="ref-p-08"></a>P-08 | Medennikov et al. | 2025 | Streaming Sortformer: Speaker Cache-Based Online Diarization | [ISCA](https://www.isca-archive.org/interspeech_2025/medennikov25_interspeech.pdf) |
| <a id="ref-p-09"></a>P-09 | Durmus et al. | 2025 | SDBench: Comprehensive Benchmark Suite for Speaker Diarization | [ISCA](https://www.isca-archive.org/interspeech_2025/durmus25_interspeech.pdf) |

### 특허 (T-xx)

| # | 출원인 | 등록/출원일 | 특허번호 | 제목 | 관할 |
|---|--------|-----------|---------|------|------|
| — | — | — | — | 데이터 부족: KIPRIS/USPTO 직접 조회 필요 | — |

### 내부 자료 (I-xx)

| # | 자료명 | 작성일 | 인용내용 |
|---|--------|--------|---------|
| — | — | — | 데이터 부족: 자사 내부 역량 자료 미확보 |
