---
topic: multimodal-vlm
date: 2026-03-12
skill: validator
status: partial
---

# Validator Report: 멀티모달 VLM

## 검증 요약
> 전체 판정: **PARTIAL** — 구조와 논리의 완성도는 높으나, (1) References에 등록된 소스의 절반가량이 본문에서 미인용 상태이고, (2) TCO 절감액 계산 불일치, (3) 판정 임계값 모순, (4) SAM 수치 미인용 등 수정이 필요한 이슈가 존재한다.

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | 5개 카테고리 35개 소스 |
| 모든 [N] 인용 → References 매칭 | ✅ | 본문 인용 기호 전부 테이블에 존재 |
| References → 본문 역방향 매칭 | ❌ | 아래 미인용 소스 목록 참조 |
| 미인용 주장 발견 | ❌ | SAM AICC 수치 출처 누락 |

### 본문 미인용 References (등록됐으나 인용 없음)

| 소스 ID | 출처명 | 비고 |
|---------|--------|------|
| D-03 | Qwen3-VL Technical Report | 본문 Qwen 관련 내용에서 미인용 |
| D-04 | Nature Communications — MiniCPM-V | EV-04와 동일 논문 중복 등록 의심 |
| D-05 | NVIDIA — AI in Telecom Survey 2026 | G-03과 동일 URL 중복 등록 (아래 참조) |
| D-06 | Huawei — Agentic Internet MWC 2026 | 본문 미인용 |
| D-07 | SKT 뉴스룸 — A.X K1 멀티모달 확장 | 경쟁사 분석에 인용 없음 |
| D-08 | ZDNet Korea — SKT 멀티모달 계획 | 본문 미인용 |
| DA-01 | PaddleOCR-VL 1.5 | Step 4에서 PaddleOCR 언급하나 인용 없음 |
| DA-02 | OmniDocBench (CVPR 2025) | 본문 미인용 |
| DA-03 | Mistral OCR 3 | Step 4에서 Mistral OCR 언급하나 인용 없음 |
| DA-07 | KT MWC 2026 에이전틱 패브릭 | 경쟁사 분석에 인용 없음 |
| EV-03 | VideoScan | 본문 미인용 |
| EV-04 | MiniCPM-V 2.6 | D-04와 동일 논문 중복 등록 의심 |
| EV-05 | Columbia Distributed VLMs | 본문 미인용 |
| CS-04 | CC-OCR Benchmark (한국어 OCR 비교) | P-01과 동일 URL, 내용 중복 등록 |

**중복 등록 의심 쌍:**
- D-05 (`blogs.nvidia.com/blog/ai-in-telco-survey-2026/`) = G-03 (동일 URL, 서로 다른 ID 부여)
- D-04 (`nature.com/articles/s41467-025-61040-5`) = EV-04 (동일 URL)
- CS-04 (`arxiv.org/html/2412.02210v2`) = P-01 (동일 URL)

### 미인용 주장 (출처 기호 없는 수치)

| 위치 | 주장 | 문제 |
|------|------|------|
| Step 1.2 SAM 행 | "AICC (컨택센터 AI) 2025 $4.4B → 2030 $14.6B, CAGR 27%" | 출처 표기 "AICC 시장 추정"으로만 기재, 정식 인용 없음 |
| Step 1.2 SAM 행 | "통신사 97% AI 도입 검토 중" | 일부 본문에서 [G-03]으로 인용하나 시장 규모 표에서 누락 |

---

## 2. 수치 교차 검증

| 수치 | 위치 | 소스 수 | 판정 | 비고 |
|------|------|---------|------|------|
| 총점 148/200 | 표지 + Step 7.6 | 내부 계산 | ✅ | 33+36+28+24+27=148 일치 |
| 각 항목 소계 | Step 7.1~7.5 | 내부 계산 | ✅ | 모든 항목 세부 합산 일치 |
| TAM 멀티모달 $3.4~3.9B(2026) | Step 1.2, Step 5.3 | 2개 (D-01, D-02) | ✅ | 복수 소스 교차 검증 |
| IDP TAM $43.9B(2034) | Step 1.2 | 2개 (DA-05, DA-06) | ✅ | 복수 소스 |
| 통신 AI SAM $14.86B | Step 1.2 | 1개 (G-03) | ⚠️ | 단일 소스, D-05 중복 등록이라면 실질 1개 |
| AICC SAM $4.4B→$14.6B | Step 1.2 | 0개 | ❌ | 출처 없음 |
| 한국어 CC-OCR 69.1점 | 복수 위치 | 1개 (P-01/CS-04 중복) | ⚠️ | 실질 단일 소스 |
| Qwen2.5-VL DocVQA 96.4% | Step 5.3 | 1개 (P-03) | ⚠️ | 단일 소스 |
| Gemini CC-OCR 80.0점 | Step 5.4 | 1개 (P-01) | ⚠️ | 단일 소스 |
| 온프레미스 TCO $54~84K | Step 4.2 | 1개 (CS-05) | ❌ | 계산 불일치 (아래 참조) |
| 엣지 Moondream 2B 2.45GB VRAM | Step 6.3 | 1개 (EV-06) | ⚠️ | 단일 소스 |
| StreamingVLM 8 FPS/H100 | Step 6.3 | 1개 (EV-02) | ⚠️ | 단일 소스 |

### TCO 계산 불일치 (심각도: 중)

**본문(Step 4.2):** "$54~84K vs API $102~300K → 연 $48~216K 절감"

**검증:**
- 하한 절감: $102K - $84K = **$18K** (본문 주장 $48K와 불일치)
- 상한 절감: $300K - $54K = **$246K** (본문 주장 $216K와 불일치)

올바른 범위: $18~246K. 본문의 $48~216K는 계산 오류로 보임. Step 5.3, 6.2에서도 "$48~216K"가 반복 인용되어 오류가 전파됨.

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "AICC 시장 2025 $4.4B → 2030 $14.6B, CAGR 27%"
    current_sources: 0
    suggested_keywords: ["contact center AI market size 2030", "AICC market CAGR", "intelligent contact center market forecast"]

  - claim: "통신 AI SAM $14.86B (2034)"
    current_sources: 1
    suggested_keywords: ["telecom AI market size 2034", "AI in telecommunications market forecast", "telco AI market research"]

  - claim: "Qwen2.5-VL 7B DocVQA 96.4%"
    current_sources: 1
    suggested_keywords: ["Qwen2.5-VL benchmark DocVQA", "VLM document visual QA leaderboard 2025"]

  - claim: "한국어 CC-OCR Qwen 69.1점, Gemini 80.0점"
    current_sources: 1
    suggested_keywords: ["CC-OCR Korean benchmark", "Korean OCR VLM evaluation 2024"]
```

---

## 3. 논리 검증

### 이슈 1: 선점 기회 기간 상충 (심각도: 중)

- **Executive Summary**: "SKT 대비 6~12개월 선점 기회"
- **Step 3.3**: "SKT 대비 동시 또는 소폭 후행 (0~6개월)"

두 진술이 모순된다. Executive Summary는 선점 가능하다고 기술하고, Step 3.3은 동시 또는 후행 가능성을 인정한다. 본문의 세부 분석(Step 3.3)이 더 구체적이므로 Executive Summary의 "6~12개월 선점"은 과장된 표현으로 판단된다.

### 이슈 2: Go 전환 임계값 모순 (심각도: 중)

**Step 7.7:** "조건 충족 시 155~159점 → Go 경계에 도달 가능"

Go 기준은 160+이므로 155~159점은 여전히 Conditional Go 구간이다. "Go 경계"라는 표현은 오해를 유발한다. "B2B 1호 계약 확보 시 경쟁우위(+2~3점) 추가로 Go(160+) 달성 예상"이라는 후속 설명이 있으나, 155~159에 2~3점을 더하면 최대 162점이고 최소 157점으로 여전히 Go 미달 가능성이 있다. 논리적 엄밀성이 부족하다.

### 이슈 3: SMART A 항목 점수 미반영 (심각도: 낮음)

Step 1.1에서 "A(달성 가능)" 항목이 CONDITIONAL 판정을 받았으나, 이것이 채점표에서 어떻게 반영되었는지 명시적 연결이 없다. 기술경쟁력 점수(28/40)가 이를 반영한 것으로 보이나, SMART 조건부 판정과 채점 항목 간 트레이서빌리티 부재.

### 긍정 항목

- 단계적 투자(Phase 1 → 2 → 3)와 각 Phase별 Go/No-Go 기준이 명확하게 제시됨 ✅
- 리스크 레지스터(R1~R5)가 영향·확률·완화방안으로 구조화됨 ✅
- 판정 구간(148점 → Conditional Go 120~159) 자체는 수치 일치 ✅

---

## 4. 편향 검증

### 낙관적 편향 의심 항목

| 항목 | 점수 | 우려 |
|------|------|------|
| 고객 수용성 (고객가치) | 8/10 | "이미지 채널 도입 초기 이용률 불확실"을 리스크로 인정하면서도 8점 부여. 신채널 전환 저항이 "낮을 것으로 예상"이라는 근거 미약. |
| 시장 타이밍 (시장매력도) | 9/10 | Step 3.3에서 "동시 또는 소폭 후행"을 인정하면서도 "선점 윈도우 6~12개월"로 근거 제시. 내부 모순이 채점에 반영되지 않음. |
| 표준/인증 (기술경쟁력) | 8/10 | "특별한 표준/인증 요구 없음"이라는 이유로 8점 부여. 이는 장점이 아니라 중립 상태이며 8점은 과대 평가 가능성. |

### 균형 있는 항목

- 특허 포트폴리오(4/10): 자사 0건이라는 약점을 낮은 점수로 정확히 반영 ✅
- 경쟁사 대응력(5/10): SKT 500B 모델 우위와 KT MS 파트너십 약점 인정 ✅
- 6.1~6.3 각 항목에 강점/리스크 양면 기술 ✅
- SOM 추정, FCR 목표, 한국어 파인튜닝 달성 가능성을 "추가 검증 필요"로 명시 ✅

### 리스크 다양성

5개 리스크(R1~R5)가 기술/경쟁/운영 영역에 걸쳐 균형 있게 분포. 다만 아래 리스크가 누락됨:
- 데이터 프라이버시 사고 시 브랜드 리스크 (이미지 데이터 처리)
- 오픈소스 Qwen 라이선스 정책 변경 리스크 (현재 Apache 2.0이나 Alibaba 정책 변경 가능)

---

## 이슈 목록

| # | 유형 | 심각도 | 내용 | 처리 권고 |
|---|------|--------|------|----------|
| I-01 | 수치 | 높음 | TCO 절감액 계산 오류: $54~84K vs $102~300K이면 절감은 $18~246K이나 본문은 $48~216K로 표기. Step 4.2, 5.3, 6.2에 오류 전파 | 계산식 재검토 후 수정 |
| I-02 | 논리 | 높음 | Go 전환 임계값 모순: 155~159점은 여전히 Conditional Go 구간이나 "Go 경계 도달"로 기술 | "Conditional Go 상단 경계" 또는 정확한 도달 점수 재산출 필요 |
| I-03 | 논리 | 중간 | 선점 기회 기간 상충: Executive Summary "6~12개월 선점" vs Step 3.3 "0~6개월" | 두 진술 중 하나로 통일 |
| I-04 | 인용 | 중간 | AICC SAM $4.4B→$14.6B 수치에 출처 없음 | 정식 인용 소스 추가 또는 추정임을 명시 |
| I-05 | 인용 | 낮음 | References 중복 등록 3쌍: (D-05=G-03), (D-04=EV-04), (CS-04=P-01) | 중복 ID 정리, 하나로 통일 |
| I-06 | 인용 | 낮음 | 14개 References 소스가 본문에서 미인용 (D-03, D-06, D-07, D-08, DA-01~03, DA-07, EV-03~05 등) | 미인용 소스 제거 또는 본문에 인용 추가 |
| I-07 | 편향 | 낮음 | 고객 수용성 8/10: 신채널 전환 저항 불확실성 인정에도 불구 높은 점수 부여 | 점수 재검토 또는 근거 강화 |
| I-08 | 편향 | 낮음 | 표준/인증 8/10: 요구사항 부재를 긍정 요소로 해석한 점 | 중립(5~6점) 재평가 검토 |
| I-09 | 수치 | 낮음 | 단일 소스 수치 4건: AICC SAM, 통신AI SAM, CC-OCR 한국어 점수, StreamingVLM FPS | 추가 소스 확보 또는 불확실성 명시 |

---

## 최종 판정

**PARTIAL**: 200점 채점 구조, 단계적 투자 로드맵, 3B 전략 의사결정, 리스크 레지스터 등 분석 뼈대는 견고하다. 그러나 TCO 절감액 계산 오류(I-01)와 Go 전환 임계값 논리 모순(I-02)은 핵심 판단 근거에 영향을 미치므로 수정이 필요하다. References 중복 및 다수 미인용 소스(I-05, I-06)는 문서 품질 이슈이며, AICC SAM 수치의 출처 부재(I-04)는 시장매력도 채점 신뢰도에 영향을 준다. 심각도 높음 이슈(I-01, I-02) 2건 수정 후 재검토를 권고한다.

---

*검증일: 2026-03-12 | 검증 모델: Claude Sonnet 4.6*
