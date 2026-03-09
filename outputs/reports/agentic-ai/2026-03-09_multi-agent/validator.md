---
validator_status: uncertain
target_file: outputs/reports/agentic-ai/2026-03-09_multi-agent/skill1.md
verified_at: 2026-03-09
---

# Validation Report

## 요약
- 상태: UNCERTAIN
- 주요 이슈:
  1. **고아 인용 1건**: [G-12]가 본문에서 사용되었으나 References 테이블에 미정의
  2. **출처-주장 불일치**: [G-21]이 특허 관련 법률 문서로 등재되었으나, 시장 성공률·Gartner 예측에도 인용 — 출처 신뢰성 의심
  3. **수치 연산 미세 불일치**: TAM 중앙값 계산 오류, CAGR 중앙값 계산 오류
  4. **미인용 주장 2건**: "IBM 핸드오프 45% 감소", "7개월마다 2배 가속" — 신뢰도 섹션에서 언급되었으나 인용 코드 없음
  5. **단일 출처 고위험 수치**: 1,445% 문의 급증, 62% 조직 도입율, 성공률 10% 미만 수치가 모두 단일 비공식 소스 기반

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | G-xx / E-xx / P-xx 3개 섹션으로 구성 |
| 모든 [N] 인용 → References 매칭 | ❌ | 미매칭: [G-12] |
| References → 본문 역매칭 (고아 References) | ✅ | 테이블 내 모든 코드가 본문에서 사용됨 |
| 미인용 주장 발견 | ❌ | 2건 발견 (하단 상세) |

### 고아 인용 상세

| 인용 코드 | 본문 위치 | References 정의 | 판정 |
|-----------|----------|----------------|------|
| [G-12] | 경쟁사 비교표 Anthropic 행 ("14.5시간 태스크 완료") | 미정의 | **고아 인용** |

### 미인용 주장 (인용 코드 없는 사실 주장)

| 위치 | 주장 내용 | 비고 |
|------|----------|------|
| 신뢰도 섹션 [C] 항목 | "IBM 핸드오프 45% 감소" | [C] 태그 있으나 인용 코드 없음 |
| 신뢰도 섹션 [C] 항목 | "7개월마다 2배" 가속 추세 | [C] 태그 있으나 인용 코드 없음 |

---

## 2. 수치 검증

| 수치 | 소스 수 | 소스 유형 | 판정 |
|------|---------|----------|------|
| TAM $91.4B~$108.6B (2026) | 3 (Fortune, Mordor, Precedence) | [B] 시장조사 기관 | 적절 (복수 소스) |
| CAGR 40.50%~43.84% | 3 (동일 소스 세트) | [B] | 적절 |
| TAM 중앙값 계산 | - | 연산 | **오류**: (91.4+108.6)/2 = 100.0B → 본문 표기 99.6B |
| CAGR 중앙값 계산 | - | 연산 | **오류**: (40.50+43.84)/2 = 42.17% → 본문 표기 42.14% |
| Gartner 문의 1,445% 급증 | 1 (Keepler 블로그) | [B] 비공식 | **단일 소스 고위험** |
| 62% 조직 AI 에이전트 실험/확장 | 1 (Flowful AI 블로그) | [B] 비공식 | **단일 소스 고위험** |
| 기업 성공률 10% 미만 | 1 (G-21: Mintz 법률) | [B] 비공식 | **출처-주장 불일치** (하단 참조) |
| 40% 이상 프로젝트 취소 (Gartner) | 1 (G-21: Mintz 법률) | [B] 비공식 | **출처-주장 불일치** |
| NTT Docomo 장애 대응 50% 단축 | 1 (G-17: NTT 공식) | [A] | 적절 (공식 보도자료) |
| Context Rot 컨텍스트 60% 초과 시 성능 저하 | 1 (G-15: LogRocket) | [B] | 단일 소스 — [D] 태그 권장 |
| LangGraph PyPI 617만 다운로드 | 1 (G-06: LangChain 공식) | [A] | 적절 (공식) |
| CrewAI GitHub 44,923 stars | 1 (G-04: CrewAI 공식) | [A] | 적절 |
| AT&T 410개+ 에이전트, 750억 API 호출 | 1 (G-24: Mobile World Live) | [B] | 단일 언론 소스 |
| SKT 2,000개+ 내부 에이전트 | 1 (E-01: SKT 프레스릴리스) | [A] | 적절 (공식 발표) |
| AdaptOrch 12~23% 성능 향상 | 1 (P-02: arxiv) | [A] | 적절 (논문 수치) |
| Microsoft 119,196개 글로벌 특허 | 1 (G-26: PatentPC 블로그) | [B] | 단일 비공식 소스 |
| Verizon 96% 정확도 | 1 (G-25: CX Today) | [B] | 단일 언론 소스 |
| IBM 핸드오프 45% 감소 | 0 | 없음 | **미인용 수치** |
| CrewAI 월 4.5억 워크플로우 | 신뢰도 섹션 [C] 태그 | 비공식 | 단일 비공식 소스 (본문 자체 인정) |

### G-21 출처-주장 불일치 상세

References 테이블에서 G-21은 **Mintz (법률회사) "Understanding How to Patent Agentic AI Systems"** (2025-03-19)로 등재되어 있다. 그러나 본문에서 G-21은 다음 세 가지 전혀 다른 맥락에 인용된다:

1. "80% 엔터프라이즈가 멀티에이전트 확장 계획하나 성공률 10% 미만" (섹션 3. 경쟁사 Gap Analysis)
2. "Gartner 예측: 2027년까지 현재 에이전트 프로젝트의 40% 이상 취소 가능성" (섹션 5. 리스크)
3. "오케스트레이터 에이전트 기반 시스템의 구체적 특허화 어려움" (섹션 6. 기술경쟁력 리스크)

특허 관련 법률 문서에 Gartner 예측과 시장 성공률이 함께 인용될 수는 있으나, References 제목만으로는 해당 수치들이 G-21 출처에서 직접 나온 것인지 확인이 불가능하다. 특히 "Gartner"라는 특정 기관 예측을 법률 블로그 출처로 인용하는 것은 원출처 불명확 위험이 있다.

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "Gartner: 2027년까지 현재 에이전트 프로젝트의 40% 이상 취소 가능성"
    current_sources: 1
    source_issue: "G-21은 특허 법률 블로그 — Gartner 원출처 확인 불가"
    suggested_keywords: ["Gartner agentic AI project cancellation 2027", "Gartner multi-agent forecast 2025"]

  - claim: "80% 엔터프라이즈 멀티에이전트 확장 계획, 성공률 10% 미만"
    current_sources: 1
    source_issue: "G-21 특허 법률 문서가 출처 — 시장 성공률 통계 원출처 불명확"
    suggested_keywords: ["enterprise multi-agent success rate survey 2025", "agentic AI implementation failure rate"]

  - claim: "Gartner 1,445% 기업 문의 급증 (2024 Q1→2025 Q2)"
    current_sources: 1
    source_issue: "G-09 Keepler 블로그 단일 비공식 소스"
    suggested_keywords: ["Gartner multi-agent systems enterprise inquiry growth 2025", "Gartner agentic AI hype cycle 2025"]

  - claim: "62% 조직이 AI 에이전트 실험·확장 중"
    current_sources: 1
    source_issue: "G-13 Flowful AI 블로그 단일 비공식 소스"
    suggested_keywords: ["enterprise AI agent adoption survey 2025 2026", "Salesforce IBM McKinsey AI agent survey"]

  - claim: "IBM 핸드오프 45% 감소"
    current_sources: 0
    source_issue: "인용 코드 없음 — 출처 미확인 수치"
    suggested_keywords: ["IBM multi-agent handoff reduction case study", "IBM AI agent orchestration benchmark"]

  - claim: "Context Rot — 컨텍스트 60% 초과 시 성능 저하"
    current_sources: 1
    source_issue: "G-15 LogRocket 블로그 단일 비공식 소스 — 핵심 기술 리스크 판단 근거"
    suggested_keywords: ["LLM context length performance degradation study", "long context window accuracy benchmark 2025"]
```

---

## 3. 논리 검증

### 긍정 사항

- 판정 흐름이 일관적이다: TRL 7~8 → 성숙 단계 → Conditional Go 판정이 수치 근거와 연결됨
- Context Rot 미해결을 승인 조건으로 명시함으로써 약점을 숨기지 않고 조건부 요구사항으로 전환한 구조가 논리적이다
- "데이터 부족" 항목(내부 역량, 투자 ROI)을 중앙값 처리하고 명시적으로 표기한 것은 투명성 있는 방법론이다
- 3B 의사결정 매트릭스에서 조건문 형태로 Buy+Borrow 도출 과정을 명시한 것은 추론 근거가 명확하다

### 논리적 약점

| 이슈 | 위치 | 내용 |
|------|------|------|
| **근거 강도 초과** | 경쟁사 비교표 | "80% 확장 계획, 10% 성공" vs "Fast follower 전략으로 따라잡기" — 10% 성공률이라면 단순 Fast follower 전략으로 해결되는지 논리적 연결이 약함 |
| **Gartner 인용 불명확** | Gap Analysis, 리스크표 | "Gartner 예측"으로 권위를 부여했으나 법률 블로그(G-21)가 출처 — 원출처 불명확 시 논거 강도 저하 |
| **조직 TRL "가정"의 일관성** | Gap Analysis | "조직 TRL 4~5 가정"이라고 명시하고 이후 Gap 1~2년을 확정 수치처럼 제시 — 가정 기반 추정임을 전 섹션에 걸쳐 일관되게 표기할 필요 |

전반적으로 논리 구조는 건전하며 비약적 결론은 발견되지 않았다. 위 3건은 경미한 수준이다.

---

## 4. 편향 검증

### 긍정 사항

- 강점/리스크를 모든 3축(고객가치, 사업포텐셜, 기술경쟁력)에서 균형 있게 병렬 제시한다
- Context Rot 미해결을 반복적으로 강조하며 기술 성숙도의 한계를 은폐하지 않는다
- SKT/KT 선점 위협을 경쟁우위 항목에서 낮은 점수(6/10)로 반영하여 긍정 편향 없이 현실을 반영한다
- "Build 제외 사유"를 명시하여 모든 전략 선택지를 공정하게 평가한다
- 데이터 공백 3건을 명시적으로 인정하고 보강 키워드를 제시한다

### 편향 이슈

| 이슈 | 위치 | 내용 |
|------|------|------|
| **긍정 수치 단독 강조** | 경영진 요약 | "CAGR 40~44%", "TRL 7~8", "SKT 2,000개+" 등 긍정 수치를 선두에 배치하는 반면, 10% 성공률은 후반부에서만 제시. 경영진 요약에 성공률 리스크 미포함 |
| **LangSmith 비용 추정** | Phase 1 실행 계획 | "$500/월~" 추정에 근거 없음 — 긍정적 방향(저비용 도입 가능)으로 판단 유도 가능 |

전반적으로 편향 수준은 낮다. 위 2건은 구조적 편향이 아닌 표현상 순서 문제에 가깝다.

---

## 결론

**최종 판정: UNCERTAIN**

References 테이블은 존재하며 구조가 체계적이다. 그러나 [G-12] 고아 인용 1건이 확인되어 자동 fail 조건에 해당하지 않으나 심각도 있는 미정의 출처다 (Anthropic "14.5시간 태스크 완료" 수치의 근거 없음). 또한 G-21(특허 법률 블로그)이 Gartner 시장 예측과 기업 성공률의 출처로 반복 인용되어 원출처 신뢰성 검증이 불가능한 상태다. 수치 연산(TAM 중앙값, CAGR 중앙값)에서 미세 오류가 발견되었고, "IBM 핸드오프 45% 감소" 및 "7개월마다 2배" 수치가 인용 코드 없이 사실처럼 기술되어 있다. 논리 구조와 편향 수준은 전반적으로 양호하나, 위 인용·수치 이슈 해소 전까지 UNCERTAIN 판정을 유지한다.
