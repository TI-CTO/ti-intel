---
validator_status: partial
target_file: /Users/ctoti/Project/ClaudeCode/outputs/reports/weekly/2026-03-30_weekly-agentic-ai.md
verified_at: 2026-03-30
---

# Validation Report — 2026-03-30_weekly-agentic-ai.md

## 요약
- 상태: **PARTIAL** (부분 합격)
- 총 검증 건수: 30건 (G-01~G-27, E-01~E-03)
- 접근 가능: 25건 / 접근 불가(403/CSS만): 5건 / 내용 불일치(Critical): 3건 / 부분 불일치(Minor): 5건
- 주요 이슈:
  1. **[Critical] G-21**: 본문 "NVIDIA $20B Groq 인수" 주장 → G-21 출처(Groq 3 LPX 기술 블로그)에 인수 내용 없음. 인수 사실 자체는 사실이나 출처가 틀린 소스 귀속 오류
  2. **[Critical] G-01**: 본문 "OpenAI SDK 0.13.2 WebSocket transport 추가(3/26)" → References 페이지는 v0.13.0이 최신이며, WebSocket(v0.10.0), Python 3.9 드롭(v0.9.0), openai v2.x 필수(v0.4.0) — 복수 기능이 이미 이전 버전에서 적용된 내용
  3. **[Critical] G-09**: 본문 인용 핵심 수치 6개($155M, 92%, $91~109억→$1,390억 CAGR 40.5%, Gartner 40%, 72%, 40%+ 실패) 모두 Axis Intelligence 페이지에서 미확인
  4. **[Minor] G-02**: 본문 "RC5(3/20)" 표기 — 페이지 발행일 2026-02-19, RC 번호 미기재(RC1). References 날짜 2026-02-19는 정확하나 본문의 RC5/3월20일 표기 불일치
  5. **[Minor] G-23**: 본문 "GPU as a Service 2026년 $7.3~7.6B" → Fortune Business Insights 페이지 실제값 $7.80B, CAGR 32.10%
  6. **[Minor] G-03**: NVIDIA Agent Toolkit 파트너십(3/20) — LangSmith Fleet 출시 페이지에 미언급 (별도 URL 필요)
  7. **[Minor] G-07**: IBM watsonx Orchestrate — 403 접근 불가
  8. **[Minor] G-26**: EU Council — 403 접근 불가 (WebSearch로 내용 확인, 16개월 연장 주장은 사실 확인됨)

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | G-01~G-27, E-01~E-03 총 30건 |
| 모든 [N] 인용 매칭 | ✅ | 본문 인용 코드 전수 확인. 미매칭 없음 |
| 고아 소스 (테이블 등재 후 본문 미인용) | ✅ | 해당 없음. 30건 모두 본문에서 인용됨 |
| 미인용 수치 발견 | ⚠️ | G-23 수치($7.3~7.6B)가 출처 페이지 실제값($7.80B)과 상이 |

---

## 2. 수치 검증

| 수치 | 출처 | 소스 수 | 판정 |
|------|------|---------|------|
| MCP 9,700만 다운로드 / Claude Code 300% 증가 | G-06 | 1 | [B] — 페이지 CSS만 로드. 내용 직접 확인 불가 |
| 에이전틱 AI 스타트업 평균 라운드 $155M | G-09 | 1 | ❌ 페이지에서 수치 미확인 |
| 에이전트 투자 기업 92% 예산 증액 | G-09 | 1 | ❌ 페이지에서 수치 미확인 |
| 글로벌 에이전틱 AI 시장 $91~109억(2026)→$1,390억(2034) CAGR 40.5% | G-09 | 1 | ❌ 페이지에서 수치 미확인 (페이지 내 수치: $89.6억(2026), CAGR 미기재) |
| Gartner 2026년 40% 에이전트 탑재 | G-09 | 1 | ❌ 페이지에서 수치 미확인 |
| 40%+ 에이전트 프로젝트 2027년 실패 | G-09 | 1 | ❌ 페이지에서 수치 미확인 |
| Global 2000 기업 72% 프로덕션 배포 | G-09 | 1 | ❌ 페이지에서 수치 미확인 |
| Nscale $2B 시리즈 C, $14.6B 밸류 | G-19 | 1 | ✅ 페이지 확인 |
| NVIDIA $20B Groq 인수 | G-21 | 1 | ❌ G-21 페이지는 Groq 3 LPX 기술 블로그 — 인수 언급 없음. WebSearch로 인수 사실 자체는 확인됨 (CNBC, Motley Fool 등) |
| GPU as a Service 2026년 $7.3~7.6B, 27-29% 성장 | G-23 | 1 | ❌ 페이지 실제값: $7.80B, CAGR 32.10% — 수치 불일치 |
| AWS 2026년 1M+ NVIDIA GPU 배포 | G-24 | 1 | ✅ 페이지 확인 |
| Tess AI $5M 라운드(3/2) | G-10 | 1 | ✅ 페이지 확인 |

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "에이전틱 AI 스타트업 평균 라운드 $155M(Q4 2025~Q1 2026), 투자 기업 92% 예산 증액, 글로벌 시장 $91~109억(2026)→$1,390억(2034) CAGR 40.5%, Gartner 2026년 40%, 40%+ 프로젝트 실패, Global 2000 기업 72%"
    current_sources: 1 (G-09, Axis Intelligence)
    reason: "페이지에서 해당 수치들이 발견되지 않음. 페이지 내 실제 수치: Fortune 500 78%, 시장 $89.6억(2026), ROI 540%"
    suggested_keywords:
      - "agentic AI market size 2026 CAGR forecast"
      - "Gartner enterprise agent 40 percent 2026"
      - "agentic AI startup funding average round 2025 2026"
      - "AI agents production deployment enterprise statistics"

  - claim: "NVIDIA $20B Groq 인수 성과: Groq 3 LPX Vera Rubin 플랫폼 편입"
    current_sources: 1 (G-21 — 소스 귀속 오류)
    reason: "G-21(Groq 3 LPX 기술 블로그)에 인수 내용 없음. 인수 사실은 WebSearch로 확인(CNBC 2025-12-24 등). 올바른 출처 미등재."
    suggested_keywords:
      - "NVIDIA Groq acquisition $20 billion 2025"
      - "site:cnbc.com NVIDIA Groq 20 billion"

  - claim: "GPU as a Service 시장 2026년 $7.3~7.6B, 27-29% 성장"
    current_sources: 1 (G-23)
    reason: "페이지 실제값: $7.80B (2026), CAGR 32.10% — 본문 수치와 불일치"
    suggested_keywords:
      - "GPU as a service market 2026 forecast billion"
      - "site:fortunebusinessinsights.com GPU service market 107797"

  - claim: "MCP 9,700만 다운로드, Claude Code 사용량 300% 증가"
    current_sources: 1 (G-06, The New Stack)
    reason: "WebFetch 시 CSS/JS만 로드, 기사 본문 미접근. 수치 직접 확인 불가."
    suggested_keywords:
      - "MCP 97 million downloads March 2026 Anthropic"
      - "Claude Code usage 300 percent increase 2026"
```

---

## 5. URL-Content 검증

| # | URL 상태 | 본문 주장 | 판정 | 비고 |
|---|---------|---------|------|------|
| G-01 | 200 OK | SDK 0.13.2 WebSocket transport 추가(3/26), Python 3.9 드롭, openai v2.x 필수, gpt-realtime-1.5 | ❌ 불일치 | 페이지 최신 버전은 v0.13.0. WebSocket은 v0.10.0, Python 3.9 드롭은 v0.9.0, openai v2.x는 v0.4.0에서 이미 적용됨. 0.13.2 릴리스 존재 미확인 |
| G-02 | 200 OK | Agent Framework RC5(3/20), GA 임박 | ⚠️ 부분 일치 | 페이지는 RC1 발행일 2026-02-19. RC5/3월20일 표기 근거 없음. A2A·MCP 지원은 확인됨 |
| G-03 | 200 OK | LangSmith Fleet(3/19), NVIDIA Agent Toolkit 파트너십(3/20), LangGraph+NVIDIA 통합 | ⚠️ 부분 일치 | Fleet 출시(3/19), 계층형 권한 확인. NVIDIA 파트너십은 페이지에 없음 — 별도 소스 필요 |
| G-04 | CSS/JS만 로드 | ADK Python 2.0 Alpha, A2A v0.3 gRPC, 에이전트 카드 서명 | 🔗 내용 미확인 | 페이지 로드 실패(JS 전용). 내용 검증 불가 |
| G-05 | 200 OK | AgentCore Stateful MCP GA, elicitation/sampling/progress notification, Policy Controls GA | ⚠️ 부분 일치 | elicitation/sampling/progress notification 확인. Policy Controls GA는 페이지에 없음 |
| G-06 | CSS/JS만 로드 | "madcap March" 14+ 릴리스, MCP 9,700만 다운로드, Claude Code 300% 증가, AAIF 기증 | 🔗 내용 미확인 | The New Stack 페이지 CSS만 로드됨. 수치 직접 확인 불가 |
| G-07 | 403 접근 불가 | IBM watsonx Orchestrate AgentOps, Agent Catalog 수백 개, Finance·Supply Chain 도메인 에이전트 | 🔗 접근 불가 | IBM 공식 페이지 403. 내용 검증 불가 |
| G-08 | 200 OK | DeepSeek V3.2, tool-use + thinking 통합, agent-first 아키텍처, 1,800개 환경 85k+ 훈련 | ✅ 일치 | 모든 주장 페이지 확인됨 |
| G-09 | 200 OK | $155M 평균 라운드, 92% 예산 증액, $91~109억→$1,390억 CAGR 40.5%, Gartner 40%, 72%, 40%+ 실패 | ❌ 불일치 | 6개 핵심 수치 모두 페이지 미확인. 페이지 내 수치는 Fortune 500 78%, 시장 $89.6억 등 상이한 데이터 |
| G-10 | 200 OK | Tess AI $5M 라운드(3/2), 엔터프라이즈 에이전트 오케스트레이션 | ✅ 일치 | |
| G-11 | 200 OK | Talkdesk CXA Operations Center(3/10), AI·인간 에이전트 단일 운영 거버넌스 | ✅ 일치 | |
| G-12 | 200 OK | NVIDIA DRA Driver CNCF 기부(3/24), 8개사 공동 협력, CNCF CTO 인용 | ✅ 일치 | |
| G-13 | 200 OK | Grove API, Dynamo 에코시스템 Kubernetes API, 단일 Custom Resource, llm-d 통합 | ⚠️ 부분 일치 | Grove API/Dynamo/Custom Resource 확인. llm-d 직접 통합 언급 없음 |
| G-14 | 200 OK | KAI Scheduler CNCF Sandbox, Gang-scheduling, 계층적 큐, 플러그인 확장 | ✅ 일치 | |
| G-15 | 200 OK | llm-d CNCF Sandbox(3/24), Red Hat·Google·IBM·CoreWeave·NVIDIA 공동 창립, Prefill/Decode 분리, 계층형 KV 캐시 | ✅ 일치 | |
| G-16 | 200 OK | AI Runway(3/24), HuggingFace 검색, GPU 메모리 적합도, 비용 추정, Dynamo·KubeRay·llm-d·KAITO 런타임 | ✅ 일치 | |
| G-17 | 200 OK | GPU Kata Containers, 하드웨어 수준 격리 + GPU 가속 | ✅ 일치 | 상세 기술 사양은 표면적 언급 수준 |
| G-18 | 200 OK | Dynamo 1.0 GA(3/16), GKE Inference Gateway 통합, 프로덕션 사례 8개 기업 | ✅ 일치 | |
| G-19 | 200 OK | Nscale $2B 시리즈 C, $14.6B 밸류, NVIDIA·Citadel·Dell·Jane Street 투자 | ✅ 일치 | |
| G-20 | 200 OK | Shopify SkyPilot 멀티클라우드 GPU, 훈련 잡 일→분 단축, Kueue 공정 분배, 팀별 비용 추적 | ✅ 일치 | |
| G-21 | 200 OK | "NVIDIA $20B Groq 인수 성과: Groq 3 LPX Vera Rubin 편입" | ❌ 불일치 | 페이지(Groq 3 LPX 기술 블로그)에 인수/M&A 내용 전혀 없음. 인수 사실은 CNBC/Motley Fool 등 별도 소스에서 확인. 대안 URL: https://www.cnbc.com/2025/12/24/nvidia-buying-ai-chip-startup-groq-for-about-20-billion-biggest-deal.html |
| G-22 | 200 OK | Pure Storage KVA + NVIDIA Dynamo 통합 | ✅ 일치 | |
| G-23 | 200 OK | GPU as a Service 시장 2026년 $7.3~7.6B, 27-29% 성장 | ❌ 불일치 | 페이지 실제값: $7.80B(2026), CAGR 32.10%. 본문 수치 과소 표기 |
| G-24 | 200 OK | AWS 2026년 1M+ NVIDIA GPU 배포(Blackwell + Rubin) | ✅ 일치 | |
| G-25 | CSS만 로드 | EU AI Act GPAI 투명성 의무 집행 개시(3월), 합성 콘텐츠 마킹·라벨링 실행 규범 2차 초안(3/3) | 🔗 내용 미확인 | Kennedys Law 페이지 CSS만 로드. 내용 직접 검증 불가 |
| G-26 | 403 접근 불가 | EU 이사회 AI Act 간소화 합의(3/13), 고위험 AI 적용 기한 최대 16개월 연장 | 🔗 접근 불가 | EU Council 403. WebSearch로 내용 확인: 16개월 연장 제안 사실 확인됨 (Consilium PDF, Medium, Burges Salmon 등) |
| G-27 | 200 OK | 한국 AI 기본법 시행령, 고영향 AI 범위, 영향 평가, 해외 빅테크 대리인, 범용 에이전트 고영향 분류 여부 | ⚠️ 부분 일치 | 고영향 AI 범위·영향 평가 확인. 해외 빅테크 국내 대리인 지정·범용 에이전트 고영향 분류 여부는 페이지 미언급 |
| E-01 | 200 OK | SKT MWC26 풀스택 AI, AI-RAN, 온디바이스 AI 안테나, 에이전틱 AI 서비스 | ✅ 일치 | |
| E-02 | 200 OK | SKT A.X K1, 519B 파라미터, 한국 최초, 정부 자율형 AI 기반모델 2단계 | ✅ 일치 | |
| E-03 | 200 OK | KT MWC26 에이전트 빌더(3/3), 노코드, RAG 모듈화, 드래그앤드롭, K GPUaaS | ✅ 일치 | |

---

## 3. 논리 검증

- **PASS**: 전반적으로 기술 변화 → 시사점 도출 구조가 논리적으로 일관됨
- **이슈 1**: G-01 관련 — 본문이 v0.13.2를 단일 이벤트("3/26 업데이트")로 서술하나, 실제로는 여러 버전에 걸쳐 이미 적용된 기능들을 한 릴리스에 귀속시키는 오류. 3/26 기준 실제 변경 내용이 무엇인지 불명확해짐.
- **이슈 2**: G-09 수치 6개가 출처에서 확인되지 않는 상태에서, 해당 수치들을 기반으로 "에이전틱 AI 거버넌스 없는 배포는 리스크"라는 결론(Gartner 40% 실패 인용)을 도출 — 근거 미검증 상태에서의 논리적 도약.

---

## 4. 편향 검증

- **PASS**: 기회/위협 모두 제시. OpenAI SDK 의존성 위험, 표준 경쟁 불확실성, Groq LPX 운영 복잡성 등 부정적 시각 포함됨.
- **주의**: GPU 오케스트레이션 섹션의 플레이어 동향이 NVIDIA/MS/Google 중심으로 편중. AMD·Intel 등 대안 하드웨어 진영 동향 부재.

---

## 결론

총 30개 URL 중 3건 Critical 불일치(G-01 버전 오귀속, G-09 핵심 수치 6개 미확인, G-21 소스 귀속 오류), 5건 Minor 불일치(G-02 RC 버전/날짜, G-03 NVIDIA 파트너십 미확인, G-05 Policy Controls 미확인, G-23 수치 불일치, G-27 부분 미언급)가 발견되었다. 특히 G-09(Axis Intelligence)의 경우 본문 "시장 시그널" 전체를 지지하는 수치 6개가 출처 페이지에서 확인되지 않아, 이 섹션의 신뢰도가 전반적으로 저하된다. G-21의 Groq 인수 소스 귀속 오류는 사실 자체는 맞으나 인용 소스가 틀린 전형적인 오귀속 사례다. 판정: **PARTIAL**.

Sources:
- [Groq and NVIDIA Non-Exclusive Licensing Agreement](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale)
- [NVIDIA buying Groq for $20 billion — CNBC](https://www.cnbc.com/2025/12/24/nvidia-buying-ai-chip-startup-groq-for-about-20-billion-biggest-deal.html)
- [EU Council AI Act Streamline Position](https://www.consilium.europa.eu/en/press/press-releases/2026/03/13/council-agrees-position-to-streamline-rules-on-artificial-intelligence/)
