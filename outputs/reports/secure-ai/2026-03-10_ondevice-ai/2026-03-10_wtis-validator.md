---
validator_status: uncertain
target_file: /Users/ctoti/Project/ClaudeCode/outputs/reports/secure-ai/2026-03-10_ondevice-ai/skill1.md
verified_at: 2026-03-10
---

# Validation Report

## 요약
- **상태**: UNCERTAIN
- **주요 이슈**:
  1. References 테이블 등재 소스 다수(10건)가 본문에서 미인용 (고아 소스)
  2. P-01~P-09 (논문 9건) 전부 본문 미인용 — 수집만 하고 분석에 미활용된 것으로 추정
  3. `prior N-12`, `prior N-14` 2건 — References에 미등재 상태에서 수치(SKT 7,000억, KT 1조) 인용
  4. Apple A19 Pro 추론 속도 추정치(`~50~80 tok/s`) 및 iPhone 14 A16 수치(`12 tok/s`) 출처가 `research line` 내부 참조에만 의존, 공개 References 없음
  5. 점수 변화(-13점) 산술 합계 불일치 확인

---

## 1. 인용 검증

### 1.1 References 테이블 존재 여부

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | 파일 하단에 완전한 테이블 존재 |
| 모든 [N] 인용 매칭 | ❌ | 미인용 소스 다수 (아래 상세) |
| 미인용 주장 발견 | ❌ | prior N-12, N-14 미등재 + research line 내부 참조 다수 |

### 1.2 본문 실제 인용 코드 vs References 테이블

**본문에서 실제 사용된 코드:**

| 계열 | 사용된 코드 |
|------|------------|
| G | G-03, G-06, G-09, G-10, G-11, G-12, G-13, G-16, G-17 |
| N | N-01 |
| E | E-01, E-02, E-03, E-04 |
| P | 없음 |
| T | T-01, T-02, T-03 |

**References 테이블 등재 코드:**

| 계열 | 등재 코드 |
|------|----------|
| G | G-01 ~ G-17 (17건) |
| N | N-01, N-02 (2건) |
| E | E-01 ~ E-04 (4건) |
| P | P-01 ~ P-09 (9건) |
| T | T-01 ~ T-03 (3건) |

### 1.3 고아 소스 (References 등재 + 본문 미인용)

| 코드 | 소스명 | 심각도 |
|------|--------|--------|
| G-01 | V. Chandra — On-Device LLMs: State of the Union, 2026 | 중간 |
| G-02 | AssemblyAI — Top 8 Speaker Diarization Libraries 2026 | 중간 |
| G-04 | Microsoft / Local AI Zone — INT4 Quantization Guide | 중간 |
| G-05 | PR Newswire — Samsung Galaxy S26 On-Device SLM | 중간 |
| G-07 | Deloitte — 2026 TMT Predictions | 낮음 |
| G-08 | ETRI Trends — 온디바이스 소형언어모델 기술개발 동향 | 낮음 |
| G-14 | Apple Developer — WWDC25 SpeechAnalyzer Session 277 | **높음** (E-02와 중복 수집 후 미활용) |
| G-15 | Google Developers Blog — MediaTek NPU and LiteRT | 낮음 |
| N-02 | Ubergizmo — NTT Docomo SyncMe at MWC 2026 | 낮음 |
| P-01 ~ P-09 | 논문 9건 전체 | **높음** (전량 미인용) |

**총 고아 소스: 18건** (G-계열 8건 + N 1건 + P-계열 9건)

### 1.4 미등재 인용 (본문 사용 + References 미등재)

| 인용 표기 | 위치 | 문제 |
|----------|------|------|
| `prior N-12` | line 292, 359 | References 테이블에 N-12 없음. SKT 7,000억 투자액 근거 |
| `prior N-14` | line 292, 359 | References 테이블에 N-14 없음. KT 1조 투자액 근거 |

`prior` 접두사가 붙은 것으로 보아 이전 버전(2026-03-03) 리포트 참조를 의미하는 것으로 추정되나, 현재 파일의 References 테이블에 등재되지 않아 독립 검증 불가능.

### 1.5 research line 내부 참조 평가

본문에서 `[research line N]` 형식의 내부 참조가 약 30회 이상 사용됨. 이는 원본 리서치 문서의 행 번호를 지칭하는 것으로 추정되나, 해당 내부 문서가 검증 범위에 없음. 주요 사례:

- Apple A19 Pro `~50~80 tok/s`: `[research line 55]` 단독 인용 — 공개 References 없음
- iPhone 14 A16 / Phi-3-mini `12 tok/s`: `[research line 57]` 단독 인용 — 공개 References 없음
- CAGR 24.6% 수치: `[research lines 104]`만 인용, [B] 등급 (단일 소스)
- SKT CTO 발언 인용: `[research lines 221-224]`에만 의존 (E-04와 병기된 경우도 있으나 불완전)

---

## 2. 수치 검증

| 수치 | 인용 소스 수 | 판정 | 비고 |
|------|------------|------|------|
| Snapdragon 8 Elite Gen 5 — 220 tok/s | 1 (G-03) | [B] 적절 | 단일 기술 뉴스 소스, 공식 Qualcomm 발표 아님 |
| pyannoteAI DER 9.9% | 1 (G-11) | [A] 적절 | 공식 벤치마크 페이지 |
| Picovoice Falcon DER | 0 | [D] | 공개 수치 없음으로 명시 — 적절한 처리 |
| SpeakerKit 9.6× 속도 | 1 (G-11) | [B] | G-11 + research line 83 — research line의 독립성 불분명 |
| 온디바이스 AI TAM $10.8B | 1 (G-06, research line 101) | [B] | 시장 리서치 보고서 단일 소스 |
| 온디바이스 AI TAM $26.6B | 미상 (research line 101) | [D] | G-06과 별도 소스인지 불분명 |
| CAGR 24.6% | 1 (research line 104 = Coherent Market Insights) | [B] | 단일 시장 조사 기관 |
| CAGR 15.1% | 미상 (research lines 104-110) | [D] | 하한값 소스 불명 |
| $20.7B~$124.1B 2030/2032 전망 | 미상 (research lines 104-110) | [D] | 여러 기관 통합이나 참조 불분명 |
| 20억대 스마트폰 온디바이스 sLM | 1 (G-12, research line 111) | [B] | 단일 블로그 소스 |
| Apple SpeechAnalyzer KV 캐시 37.5% 절감 | 1 (E-02) | [A] | 공식 Apple ML Research |
| SKT 에이닷 통화요약 월 30건 | 1 (N-01) | [B] | 단일 뉴스 소스 (2024-10) |
| SKT 7,000억 AI 투자 | 0 (prior N-12만 언급, 미등재) | ❌ | References에 근거 없음 |
| KT 1조 AI 투자 | 0 (prior N-14만 언급, 미등재) | ❌ | References에 근거 없음 |
| Apple A19 Pro ~50~80 tok/s (추정) | 0 (research line 55만) | [D] 추정값 | "추정"으로 명시되어 있어 부분 인정 |
| iPhone 14 A16 / Phi-3-mini 12 tok/s | 0 (research line 57만) | [D] | 공개 References 없음 |
| Samsung 보이스피싱 탐지 경찰청 3만건 | 1 (E-01) | [B] | E-01 Samsung 공식 발표로 간접 인용 |

### 2.1 점수 산술 검증

보고서 내 이전 분석 대비 변화표:

| 항목 | 변화 |
|------|------|
| 기술경쟁력 | -1 |
| 시장매력도 | -3 |
| 경쟁우위 | -2 |
| 고객가치 | -5 |
| 실행가능성 | -2 |
| **합계** | **-13** |

산술 합계: -1 + (-3) + (-2) + (-5) + (-2) = **-13** → 일치 ✅

세부 채점 소계 합계: 21 + 26 + 21 + 18 + 21 = **107/200** → 일치 ✅

---

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "SKT AI 투자 7,000억원"
    current_sources: 0 (prior N-12, 현재 References 미등재)
    suggested_keywords: ["SKT AI 투자 2025 7000억", "SKT annual report AI investment"]

  - claim: "KT AI 투자 1조원"
    current_sources: 0 (prior N-14, 현재 References 미등재)
    suggested_keywords: ["KT AI 투자 2025 1조", "KT annual report AI capital expenditure"]

  - claim: "iPhone 14 A16 Bionic / Phi-3-mini 3.8B — 12 tok/s"
    current_sources: 0 (internal research line 57 only)
    suggested_keywords: ["Phi-3 mini iPhone 14 inference speed benchmark", "A16 Bionic LLM throughput"]

  - claim: "온디바이스 AI 시장 CAGR 15.1% (하한)"
    current_sources: 0 (research lines 104-110 범위만 언급, 소스 미특정)
    suggested_keywords: ["on-device AI market CAGR 2025 15%", "small language model market growth"]

  - claim: "SpeakerKit 9.6× 실시간 대비 속도"
    current_sources: 1 (G-11 공식 벤치마크)
    suggested_keywords: ["Argmax SpeakerKit speed benchmark", "on-device speaker diarization Apple Silicon throughput"]
```

---

## 3. 논리 검증

**전반적 평가: PASS (경미한 이슈 2건)**

### 3.1 결론-근거 일관성

- **기술 성숙도 판정 (TRL 7~8)**: Snapdragon 220 tok/s [G-03] + Picovoice Falcon 상용화 [G-10] + pyannoteAI DER 9.9% [G-11] → TRL 7~8 판정 논리적으로 타당.
- **B2C 유료 서비스 연기 권고**: Samsung S26 무료 탑재 [E-01] + Apple 무료 API [E-02] + SKT 유료화 연기 [E-04] 세 가지 독립 신호 → 결론 강도 적절.
- **B2B 프라이버시 기회**: "빅테크 미진출" 주장은 근거 없이 단언되는 경향 있음 (빅테크의 B2B 화자분할 시장 부재를 직접 증명하는 소스 없음) — 논리적 약점이나 치명적 수준 아님.

### 3.2 경미한 논리 도약

1. **"B2B 경쟁사 없음"** (line 183): "경쟁사: 없음 (빅테크는 B2C 집중, 통신사 대상 솔루션 없음)" — 이를 뒷받침하는 직접 인용 없음. 현존하는 기업용 화자분할 솔루션(AWS Transcribe, Azure Speaker, Google CCAI)이 언급되지 않아 주장이 과장될 수 있음.

2. **SKT 7,000억/KT 1조 ROI 비교**: 투자 규모를 ROI 불명의 근거로 활용하나 해당 수치의 References가 없어 전제 자체가 불검증 상태.

### 3.3 불확실성 인정

- 배터리 소모, 한국어 DER, WTP 3개 항목 모두 [D] 명시 + "데이터 부족" 태그 부착 — 적절한 불확실성 처리.
- "prior" 참조로 이전 분석 결과를 가져오는 방식은 독립 검증 가능성을 저해하나, 비교 분석 맥락에서 부분적으로 수용 가능.

---

## 4. 편향 검증

**전반적 평가: PASS**

### 4.1 긍정/부정 균형

- **강점/리스크 이중 구조**: 섹션 6.1~6.5 전체에서 "강점" + "리스크(감점 요인)" 이분 구조 유지 — 편향 없음.
- **기술 낙관 편향 없음**: 220 tok/s 달성을 인정하면서도 이를 차별화 소멸 근거로 활용 — 균형 잡힌 해석.
- **경쟁사 분석 균형**: Samsung/Apple 빅테크 우위, SKT/KT 동료 신호 부정적 측면 모두 명시.

### 4.2 경미한 편향 요소

1. **B2B 기회 과장 가능성**: B2B 프라이버시 시장에 대한 낙관적 전망이 검증 없이 제시됨 (WTP, 시장 규모 미검증). 하지만 이는 편향이라기보다 데이터 부족 상황에서의 가설 제시로 볼 수 있으며, 문서 자체가 PoC 선행 권고로 마무리되어 수용 가능.

2. **논문(P-01~P-09) 미활용**: 9편의 학술 논문을 References에 등재했으나 전혀 인용하지 않음. 학술 근거가 있었다면 기술 평가의 객관성이 강화될 수 있었으나, 현재는 실무 소스 위주의 편중이 있음.

---

## 결론

UNCERTAIN 판정. References 테이블이 존재하고 핵심 사실 주장(220 tok/s, 무료 탑재, DER 수치 등)의 공개 소스 인용은 양호하나, 두 가지 구조적 이슈가 있다. 첫째, P-01~P-09 논문 9건을 포함한 총 18건의 고아 소스가 References에 등재만 되고 본문에서 미인용 상태이며, 이 중 학술 논문 전량 미인용은 기술 평가 신뢰도 보강 기회를 놓친 것이다. 둘째, SKT 7,000억/KT 1조 투자 수치가 `prior N-12`, `prior N-14`로만 참조되어 현재 문서의 References에서 검증 불가능하며, B2B 시장 경쟁사 부재 주장이 직접 근거 없이 단언되는 논리 약점도 있다. 이상의 이슈가 핵심 결론을 뒤집는 수준은 아니나 독립 검증 완결성 기준에서 PASS 판정은 불가하다.
