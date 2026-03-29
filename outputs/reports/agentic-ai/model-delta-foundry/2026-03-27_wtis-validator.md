---
type: wtis-validator
target: 2026-03-27_wtis-skill1.md
date: 2026-03-27
validator_status: fail
---

# Validator Report

## 검증 요약

- 상태: **FAIL**
- issues_found: 13
- critical_issues: 3

주요 이슈: (1) 채점표 개별 점수 합산이 총점 143과 불일치 — 실제 합산 126/200 (Critical), (2) 핵심 시장 수치 불일치 3건 (G-01 2025년 수치, G-03 전 수치, G-10 수치), (3) G-07 Databricks 블로그 URL 페이지가 CSS/스타일시트만 반환 — 본문 주장 확인 불가.

---

## 상세 이슈 목록

| # | 유형 | 심각도 | 내용 | 권고 |
|---|------|--------|------|------|
| I-01 | 수치 오류 | Critical | 채점표 세부 점수 합산이 총점과 불일치. 각 항목 합산: 26+31+21+22+26=**126**, 보고서 표기는 **143/200**. 17점 차이 발생. frontmatter의 `scoring: 143/200`, 본문 판정 모두 143 기준. | 채점표 재계산 필요. 세부 점수 또는 총점 중 하나가 오기재됨. |
| I-02 | 수치 불일치 | High | G-01(Fortune BI) MLOps 2025년 수치: 보고서는 **$2.33B** 인용, 실제 페이지는 **$2.98B** 표기 (2026년 $4.39B는 일치). CAGR도 보고서 "28~42%"와 달리 페이지는 45.8% 표기. | G-01 인용 수치 재확인 필요. Executive Summary 및 Market Sizing 섹션 영향. |
| I-03 | 수치 불일치 | High | G-03(Straits Research) 수치 전면 불일치: 보고서는 "2025년 $2.23B, 2033년 $35.4B, CAGR 41.3%" 인용, 실제 페이지 수치는 "2024년 $3.24B, 2025년 $3.63B, 2033년 $8.68B, CAGR 12.31%". 수치와 CAGR 방향성 자체가 다름. | G-03 출처 매핑 오류 가능성 높음. 해당 수치의 실제 출처 재탐색 필요. |
| I-04 | 수치 불일치 | Medium | G-09(Fortune BI) GPUaaS 2026년 수치: 보고서는 "$7.34B" 인용, 실제 페이지는 **$7.80B** 표기. $460M 차이. | G-09 수치 수정 필요. |
| I-05 | 수치 불일치 | Medium | G-10(MarketsandMarkets AI Inference) 수치 불일치: 보고서는 "추론 시장 2026년 $50B 초과, AI 컴퓨팅의 67%"라고 인용. 실제 페이지 내용: 2025년 $106.15B, 2030년 $254.98B, CAGR 19.2%. "$50B, 67%" 수치 미확인. | G-10 인용 근거 재확인 필요. 다른 버전의 보고서 또는 다른 출처일 가능성. |
| I-06 | 수치 불일치 | Medium | G-15(Analysys Mason) SAM 수치 오기: 보고서는 "글로벌 통신사 AI 클라우드 누적 $770B"라고 인용. 실제 페이지는 "**USD77 billion** cumulatively in AI cloud infrastructure between 2025 and 2030". **$77B와 $770B는 10배 차이**. | SAM 계산(~$230B 누적)과 관련 인용 전면 재검토 필요. Executive Summary 포함. |
| I-07 | URL 접근 불가 | Medium | G-07(Databricks Blog, MLflow 3.0): WebFetch 결과 페이지가 CSS/스타일시트만 반환, 실질 텍스트 콘텐츠 없음. "MLflow 3.0: GenAI+에이전트 평가 통합, OpenTelemetry 호환" 주장 확인 불가. | 대안 URL 탐색 권장: https://mlflow.org/blog 또는 Databricks 공식 릴리스 노트. |
| I-08 | 수치 불일치 | Medium | G-23(Spheron Blog) 벤치마크 수치 불일치: 보고서는 "SGLang 16,215 tok/s vs vLLM 12,553 tok/s (29% 우위)" 인용. 실제 페이지에 해당 수치 없음. 페이지 실제 수치는 SGLang ~2,460 tok/s vs vLLM ~2,400 tok/s (약 3% 우위). 출처 또는 벤치마크 조건 불일치. | 수치 출처 재확인 필요. 해당 수치가 다른 출처(e.g., LMSys, SGLang 공식 벤치마크)에서 인용된 것일 가능성. |
| I-09 | 수치 불확실 | Medium | G-24(NVIDIA NIM) 성능 수치: 보고서는 "2.6배 처리량 향상"으로 인용. 실제 페이지는 NIM ON 1,201 tok/s, NIM OFF 613 tok/s로 **약 2.0배** (1.96배)에 해당. "2.6배" 수치의 출처 불분명. | 보고서 수치 수정 필요. 실제 검증 수치는 ~2배. |
| I-10 | 주장 미검증 | Low | G-17(arXiv ADAS) ICLR 2025 채택 표기: 보고서 References 테이블에 "[A] 2025" 등급으로 "ICLR 2025 / arXiv"를 소속 기관으로 표기. 실제 arXiv 페이지에 ICLR 2025 채택 정보 없음 — arXiv 논문으로만 확인됨. 채택 여부 미검증. | ICLR 2025 proceedings에서 직접 확인 필요. ICLR 2025 accepted papers 목록에 "Automated Design of Agentic Systems" 검색 권장. |
| I-11 | 주장 미검증 | Low | G-14(QuickMarketPitch) URL 접근 불가(SSL 인증서 만료): "MLOps 투자 $4.5B(2024), $6B+(2025), 2026년 15~20건 M&A 예상" 주장 확인 불가. 보고서 자체도 "[미검증]" 태그 표기. | 신뢰도 낮은 블로그 소스 — 주요 주장에 사용 부적절. CB Insights 또는 Pitchbook 대체 출처 탐색 권장. |
| I-12 | 주장 미검증 | Low | G-33(SKT Newsroom) AI DC 매출 $354M 및 소버린 AI 519B 파라미터: 실제 페이지에서 Haein GPU 1,000+ B200 확인되나, "$354M" 재무 수치와 "519B 파라미터"는 페이지에 미확인. 이 수치들은 별도 출처(SKT IR, 별도 보도)에서 인용된 것으로 보임. | G-33 인용 범위 재분리 필요. $354M과 519B 수치는 별도 출처를 추가해야 함. |
| I-13 | 논리 검증 | Low | G-25(NVIDIA Run:ai) GPU 활용률 2~3배 향상 및 오픈소스화 계획: 실제 블로그 페이지에 배수 수치와 오픈소스화 계획 미확인. 인수 발표 사실은 확인되나 구체적 수치의 출처 불명. | Run:ai 공식 기술 문서 또는 NVIDIA GTC 발표자료에서 재확인 필요. |

---

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "국내 MLOps/GPUaaS 시장 규모 (SOM 추정 근거)"
    current_sources: 0
    suggested_keywords: ["한국 AI 인프라 시장 규모 2025", "국내 GPUaaS 시장 점유율", "Korea MLOps market size"]

  - claim: "SKT AI DC 매출 $354M (YoY +35%)"
    current_sources: 1
    suggested_keywords: ["SKT AI Data Center revenue 2025", "SKT annual report 2025 AI revenue", "SKT 2025 실적발표 AI"]

  - claim: "MLOps 투자 $4.5B(2024), $6B+(2025) 전망 (G-14)"
    current_sources: 1
    suggested_keywords: ["MLOps venture funding 2024", "AI infrastructure investment 2025 Pitchbook", "MLOps M&A 2026 forecast"]

  - claim: "통신사 내부 MLOps 전문 인력 현황"
    current_sources: 0
    suggested_keywords: ["통신사 AI 엔지니어 채용 현황", "telco AI talent shortage", "MLOps engineer demand Korea"]
```

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | G-01~G-38, 38개 항목 |
| 모든 [N] 인용 매칭 | ✅ | 본문 인용 G-01~G-38 전수 확인, 미매칭 없음 |
| 미인용 레퍼런스 | ✅ | G-11, G-20, G-26, G-29, G-31 본문 미인용 — References 테이블에만 존재 (규칙 위반 아님, 다만 불필요 항목 가능성) |
| 인용 없는 주요 주장 | 부분 ⚠️ | 내부 역량 평가, 경쟁사 대응력 점수(5/10), 1~2년 격차 판단 등은 "[추정, 근거부족]" 명시됨 — 명시적으로 표기하여 투명성 확보됨 |

---

## 2. 수치 검증

| 수치 | 소스 수 | 판정 |
|------|---------|------|
| MLOps TAM $2.2~3.2B (2025) | 5개 기관 | ⚠️ G-01 2025년 $2.33B이 실제 $2.98B와 불일치. G-03 수치 전면 불일치. 범위 상단 $3.2B는 G-04($3.18B)로 뒷받침되나 하단 $2.2B 근거 취약 |
| GPUaaS TAM $8.2B (2025) | 2개 기관 | ✅ G-08 페이지에서 $8.21B 확인 |
| GPUaaS TAM $7.34B (2026, G-09) | 1개 기관 | ❌ 실제 페이지는 $7.80B. $460M 오기재 |
| 통신사 AI 클라우드 $770B | 1개 기관 | ❌ 실제 $77B — 10배 과대 표기 (Critical) |
| AI 추론 시장 $50B (2026, G-10) | 1개 기관 | ❌ 실제 페이지에 해당 수치 미존재 |
| NIM 2.6배 처리량 향상 | 1개 기관 | ⚠️ 실제는 약 2배(1.96배). 2.6배 출처 불명 |
| SGLang 29% 우위 벤치마크 | 1개 기관 | ❌ 실제 페이지에 해당 수치 없음 |
| SKT AI DC $354M (YoY +35%) | 1개 기관 | ⚠️ G-33 페이지에 수치 미확인. 별도 출처 필요 |
| Run:ai GPU 활용률 2~3배 | 1개 기관 | ⚠️ G-25 페이지에 수치 미확인 |
| 채점표 총점 143/200 | 내부 계산 | ❌ 세부 점수 합산 = 126. 17점 차이 |

---

## 5. URL-Content 검증

| # | URL 상태 | 본문 주장 | 판정 | 비고 |
|---|---------|---------|------|------|
| G-01 | 200 OK | MLOps 2025년 $2.33B | ⚠️ 부분 일치 | 실제 페이지는 $2.98B. 2026년 $4.39B는 일치. CAGR 45.8% (보고서 28~42%와 상이) |
| G-02 | 200 OK | MLOps 2027년 $5.9B, CAGR 41.0% | ✅ 일치 | |
| G-03 | 200 OK | MLOps 2025년 $2.23B, 2033년 $35.4B, CAGR 41.3% | ❌ 불일치 | 실제: 2025년 $3.63B, 2033년 $8.68B, CAGR 12.31%. 완전 불일치 |
| G-04 | 미검증 | MLOps 2025년 $3.18B | — | 페이지 직접 접근 미실행 (G-01~G-05 범위 인용) |
| G-05 | 미검증 | CAGR 28.9% | — | |
| G-06 | 미검증 | LLMOps 2025년 $5.2B, 2032년 $19.8B | — | |
| G-07 | 200 (CSS only) | MLflow 3.0 GenAI+에이전트 통합, OpenTelemetry 호환 | 🔗 접근 불가 | 페이지가 CSS/스타일시트만 반환. 실질 콘텐츠 확인 불가 |
| G-08 | 200 OK | GPUaaS 2025년 $8.2B, 2030년 $26.6B, CAGR 26.5% | ✅ 일치 | |
| G-09 | 200 OK | GPUaaS 2026년 $7.34B | ❌ 불일치 | 실제: $7.80B |
| G-10 | 200 OK | AI 추론 2026년 $50B 초과, AI 컴퓨팅 67% | ❌ 불일치 | 실제: 2025년 $106.15B 시장 (다른 분류체계). "$50B, 67%" 수치 미존재 |
| G-12 | 리다이렉트 | AI 프로덕션 사용 31%로 2배 증가, GenAI YoY 140~180% | 🔗 접근 불가 | Medium(paywall/인증) 리다이렉트. 확인 불가 |
| G-13 | 200 OK | MLOps 범위 확장: LLM+RAG+에이전트 통합 운영 | ⚠️ 부분 일치 | 생성형 AI 언급은 있으나 RAG/에이전트 통합 운영 명시 없음 |
| G-14 | SSL 오류 | MLOps 투자 $4.5B(2024), $6B+(2025), 2026년 M&A 15~20건 | 🔗 접근 불가 | SSL 인증서 만료. 신뢰도 낮은 소스 ([미검증] 태그 본문 표기) |
| G-15 | 200 OK | 통신사 AI 클라우드 누적 $770B | ❌ 불일치 | 실제: **$77B** (10배 차이). GPU 가동률 60~70%+ 언급 미확인 |
| G-16 | 200 OK | DSPy+TextGrad GSM8k 82.1%, Math +25~65% | ❌ 불일치 | 페이지에 해당 수치 없음. Stanford HAI 뉴스 섹션에 텍스트 콘텐츠 부재 |
| G-17 | 200 OK | ADAS ICLR 2025 채택, 메타 에이전트 자동 설계 | ⚠️ 부분 일치 | arXiv 논문 ADAS 확인. 메타 에이전트+도메인 전이 확인. ICLR 2025 채택 정보 미확인 |
| G-18 | 200 OK | DSPy 정확도 46.2%→64.0% | ✅ 일치 | |
| G-19 | 미검증 | HELM 7개 지표 16개 시나리오 | — | |
| G-20 | 미검증 | LM Eval Harness 60+ 벤치마크 | — | |
| G-21 | 미검증 | LangSmith 프로덕션 에이전트 추적·평가·배포 | — | |
| G-22 | 리다이렉트 | AWS Bedrock AgentCore, Azure AI Foundry, A2A | 🔗 접근 불가 | Medium 리다이렉트. 확인 불가 |
| G-23 | 200 OK | SGLang 16,215 tok/s, vLLM 12,553 tok/s (29% 우위) | ❌ 불일치 | 실제 페이지 수치: SGLang ~2,460 tok/s, vLLM ~2,400 tok/s (~3% 우위). 해당 수치 없음 |
| G-24 | 200 OK | NIM 2.6배 처리량 향상 | ⚠️ 부분 일치 | 페이지 확인: NIM ON 1,201/NIM OFF 613 tok/s = 약 **2.0배** (1.96배). "2.6배" 미확인 |
| G-25 | 200 OK | Run:ai ~$700M 인수, GPU 활용률 2~3배, 오픈소스화 | ⚠️ 부분 일치 | 인수 발표 사실 확인. $700M, 2~3배, 오픈소스화 계획은 페이지에 미확인 |
| G-27 | 200 OK | CoreWeave W&B $1.7B 인수 완료 | ⚠️ 부분 일치 | 인수 완료 확인. $1.7B 금액은 페이지에 미표기 |
| G-28 | 200 OK | W&B 인수 교차 검증 | ✅ 일치 | TechCrunch에서 $1.7B 수치 확인됨 |
| G-30 | 200 OK | FriendliAI $20M 조달, LG전자 파트너십, 매출 6~7배 | ✅ 일치 | |
| G-32 | 200 OK | NTT DATA NVIDIA NIM+NeMo AI Factory | ✅ 일치 | |
| G-33 | 200 OK | Haein 1,000+ GPU, AI DC $354M, 519B 파라미터 | ⚠️ 부분 일치 | Haein 1,000+ B200 확인. $354M 재무 수치, 519B 파라미터 페이지 미확인 |
| G-34 | 200 OK | MWC 2026 Best Cloud Solution 수상 | ✅ 일치 | |
| G-35 | 200 OK | KT-Microsoft GPT-4o 커스터마이즈, Azure AI Studio 에이전트 | ✅ 일치 | |
| G-36 | 200 OK | VESSL AI $12M, GPU 비용 80% 절감 | ✅ 일치 | |
| G-37 | 403 Forbidden | NVIDIA-SK 그룹 AI Factory 한국 | 🔗 접근 불가 | 403 오류. 내용 확인 불가 |
| G-38 | 접속 불가 | 통신사 AI-as-a-Service 전략 | 🔗 접근 불가 | 소켓 연결 오류. 확인 불가 |

---

## 3. 논리 검증

**채점표 합산 오류 (Critical)**
세부 점수를 직접 합산하면: 26(고객가치)+31(시장매력도)+21(기술경쟁력)+22(경쟁우위)+26(실행가능성) = **126점**이나, 보고서는 **143/200**으로 표기. Conditional Go 기준이 120~160점 구간이라면 126점도 동일 판정이 될 수 있으나, 정확한 점수 표기가 필요하다. 17점 차이는 검증 불가능한 수준이 아니라 명확한 계산 오류다.

**$77B vs $770B (Critical)**
SAM 계산 근거인 G-15 수치가 $77B임에도 보고서는 $770B를 인용. "$770B × 아태 30% = $230B 누적"이라는 SAM 추정 전체가 무효화된다. 실제 $77B × 30% ≈ $23B로, SAM이 10분의 1 규모.

**3B 전략 도출 논리**: Borrow+Build 전략 도출 로직(differentiation 5/10 + urgency 7/10 + tech_gap 1~2년)은 내부적으로 일관되며 논리적으로 타당하다. PASS.

**판정 Conditional Go**: 채점 오류가 있으나, 수정된 126점도 Conditional Go 구간(120~160점) 내에 있을 가능성이 높다. 단, 정확한 채점 기준(임계값)이 명시되지 않아 단정 불가.

## 4. 편향 검증

**낙관 편향 — 부분 확인**
- GPU 가동률 리스크를 "probability: M, impact: H"로 상중 수준으로 명시 — 적절.
- SKT 선점 효과를 "probability: H"로 명시 — 적절.
- 그러나 Borrow+Build 전략에서 NVIDIA Run:ai 파트너십을 핵심으로 권고하면서, NVIDIA의 독점적 지위와 파트너십 비용·의존성 리스크는 경쟁 섹션에서만 단편적으로 언급. 파트너십 실패 시나리오가 전략 섹션에 없음.

**확증 편향 — 경미**
- 하이퍼스케일러 대비 열위(고객가치 5점)를 명시적으로 인정. 경쟁우위도 낮게 평가(22/40). 단점을 숨기지 않음. PASS.

**단일 소스 의존**
- SKT $354M 수치: G-33 단일 소스 + G-33 페이지에서 해당 수치 미확인.
- 통신사 AI 클라우드 $770B: G-15 단일 소스 + 실제 수치($77B) 오기재.
- SAM($230B 추정)은 두 오류가 결합되어 전혀 다른 규모를 제시함.

---

## 결론

**status: fail**

3개의 Critical/High 이슈로 인해 FAIL 판정: (1) 채점표 세부 점수 합산이 총점과 17점 불일치하여 보고서 신뢰성 훼손, (2) 핵심 SAM 근거인 G-15의 $770B는 실제 $77B의 10배 과대기재로 시장 규모 추정 전체의 유효성이 의심됨, (3) G-03 MLOps 시장 수치 전면 불일치(CAGR 41.3% vs 실제 12.31%)로 TAM 범위 근거 취약화. 전체 신뢰도 "Medium" 자체 평가는 적절하나, 위 3개 이슈는 수치 정확성이 요구되는 의사결정 문서에서 수정 없이 상정하기 어려운 수준이다.
