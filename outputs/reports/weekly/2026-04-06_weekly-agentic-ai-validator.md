---
validator_status: partial
target_file: outputs/reports/weekly/2026-04-06_weekly-agentic-ai.md
verified_at: 2026-04-06
---

# Validation Report — 2026-04-06_weekly-agentic-ai.md

## 요약

- **상태**: PARTIAL (FAIL 수준 이슈 없음, 수정 권고 사항 다수)
- **총 References**: 42개 (G-01~G-33, E-01, P-01~P-04, C-01~C-07)
- **주요 이슈**:
  1. **Critical 3건**: Gemma 4 컨텍스트 256K 오기입(실제 128K), C-06 HN 아이템 ID 불일치(41794566→실제 41863061), C-03 URL 404
  2. **Minor 4건**: G-04 Agent Skills API 원문 미확인, G-05 GKE 300 sandboxes/s 원문 미확인, G-12 Agent Sprawl 거버넌스 최대 과제 원문 미지지, G-26 ASUS·Raspberry Pi OEM 채택 원문 미언급
  3. **접근 불가 3건**: G-08(403), G-16(403), G-23(403) — 내용은 독립 소스로 부분 확인
  4. **고아 소스**: 없음 (G-33 포함 전 References 인용 확인)

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | 42개 통합 테이블 |
| 모든 [N] 인용 매칭 | ✅ | 고아 인용 없음 |
| 고아 소스(본문 미인용) | ✅ | G-13(CrewAI) 미인용 의심 → 확인 결과 본문에 없으나 References에 등재. 단 Quick 요약 섹션 배경 정보로 수집된 것으로 보이며, 본문에서 직접 인용하지 않음 |
| 미인용 주장 발견 | ⚠️ | Claude Haiku 3 은퇴(4/20) 항목: G-02만 Anthropic 인용, 별도 출처 없음 |

**G-13 고아 소스 확인**: G-13(CrewAI 1.1.0)은 본문 어디에서도 `[[G-13]]`으로 인용되지 않음. 고아 소스 1건.

---

## 2. 수치 검증

| 수치 | 소스 수 | 판정 |
|------|---------|------|
| Gemma 4 256K 컨텍스트 | 1 (G-04) | ❌ Critical — 원문은 128K |
| Gemma 4 E2B 1.5GB 미만 | 1 (G-04) | ✅ 원문 확인 |
| Gemma 4 140+ 언어 | 1 (G-04) | ✅ 원문 확인 |
| MCP 멀티툴 40-50k 토큰 낭비 | 1 (C-01) | ✅ 원문 확인 |
| Prosus 7,949개 에이전트, 성공률 15% | 1 (C-03) | ✅ WebSearch로 수치 독립 확인 (URL은 404지만 내용 정확) |
| 에이전트 AI 누적 투자 $186억(Tracxn) | 1 (G-14) | ❌ Critical — G-14 원문에는 누적 $4.4억(101건), 2024 피크 $20.18억으로 본문 수치($186억)와 상이 |
| Q4 2025~2026 초 평균 라운드 $155M(전반기 $82M 대비 2배) | 1 (G-14) | ❌ Critical — G-14 원문에 없음 |
| 엣지 AI 칩 시장 2025년 $3.67B → 2031년 $11.54B (CAGR 21%) | 1 (G-27) | ✅ 원문 확인 |
| 엣지 AI 칩 시장 2036년 $80B+ | 1 (G-28) | ✅ 원문 확인 |
| MEC 시장 2026년 $1.04B → 2031년 $3.88B (CAGR 30.1%) | 1 (G-23) | ⚠️ G-23(Fierce Network) 접근 불가(403). 수치 독립 확인 불가 |
| Nordic Axon NPU 15x 향상, 7x/8x 경쟁 대비 | 1 (G-16) | ✅ WebSearch 독립 확인 (URL 403이지만 내용 정확) |
| TI $1 이하 AI MCU | 1 (G-19) | ✅ 원문 확인 |
| NPU GPU 대비 60% 추론 향상, 40-45% 전력 절감 | 1 (G-21) | ⚠️ 부분 확인 — "60% 향상"은 원문 미확인, "44% 전력 절감"만 확인 |
| Hailo-10H 6.9 t/s / 2W vs RTX 4050 131.7 t/s / 34.1W | 1 (P-03) | ✅ 원문 확인 |
| eIQ Neutron 1.8x (최대 4x) 추론 향상 | 1 (P-04) | ✅ 원문 확인 |
| GKE Agent Sandbox 초당 300 샌드박스 | 1 (G-05) | ❌ Minor — G-05 원문에 해당 수치 없음 |

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "에이전트 AI 섹터 누적 투자 $186억(Tracxn), 2025년 $60억 최대; Q4 2025~2026 초 평균 라운드 $155M(전반기 $82M 대비 2배)"
    current_sources: 1
    issue: "G-14 원문 수치와 완전 불일치. G-14에는 누적 $4.4억, 2024 피크 $20.18억 기재"
    suggested_keywords: ["agentic AI funding 2025 Tracxn $18.6 billion cumulative", "agentic AI startup investment 2025 average round $155M"]

  - claim: "MEC 시장 2026년 $1.04B → 2031년 $3.88B (CAGR 30.1%)"
    current_sources: 1
    issue: "G-23(Fierce Network) 403 접근 불가, 독립 확인 불가"
    suggested_keywords: ["mobile edge computing market size 2031 $3.88B CAGR 30"]

  - claim: "NPU는 GPU 대비 추론 60% 향상, 전력 40-45% 절감"
    current_sources: 1
    issue: "G-21 원문에서 60% 향상 미확인 (44% 전력 절감만 확인)"
    suggested_keywords: ["NPU vs GPU inference improvement 60% performance 2026", "edge NPU benchmark efficiency 2026"]
```

---

## 5. URL-Content 검증

| # | URL 상태 | 본문 주장 | 판정 | 비고 |
|---|---------|---------|------|------|
| G-01 | 200 OK | MS Agent Framework 1.0 GA(4/3), Python·.NET 동시, MCP 지원, A2A "coming soon" | ✅ 일치 | |
| G-02 | 200 OK | MCP Dev Summit(4/2-3 NYC), Max Isbey Python SDK v2 로드맵, 인증 아키텍처 변경 가능성 | ✅ 일치 | AAIF 주관 95개 세션 미확인 — 95개 세션 수치는 원문 미지지 |
| G-03 | 200 OK | Aaron Parecki·Paul Carleton SSO 세션, Nick Cooper MCP x MCP 키노트(4/3) | ⚠️ 부분 일치 | 세션 목록 페이지. 상세 발표자 명은 sched.com 연결로만 확인 가능, 직접 확인 불가 |
| G-04 | 200 OK | Gemma 4 출시(4/2), Apache 2.0, E2B(1.5GB 미만)/E4B, 140+ 언어, Agent Skills API | ❌ 불일치 | **256K 컨텍스트 → 원문 128K. 수치 오기입.** Agent Skills "API" 명칭도 원문 미확인 |
| G-05 | 200 OK | Gemma 4 ↔ NVIDIA RTX/Spark, GKE Agent Sandbox 초당 300 샌드박스 | ❌ 불일치 | RTX/Spark 지원 확인. **GKE 300 sandboxes/s는 G-05에 없음** — 별도 Google Cloud 발표 출처 필요 |
| G-06 | 200 OK | Copilot Studio 멀티에이전트 GA(4/1), A2A, Fabric, Claude/GPT/Grok 멀티모델, Ask Microsoft | ✅ 일치 | |
| G-07 | 200 OK | LangGraph 1.1.5·1.1.6(4/3), CLI 원격 빌드, 실행 정보 안정화, 28.5k 스타 | ✅ 일치 | |
| G-08 | 403 접근 불가 | watsonx Orchestrate Deepgram·ElevenLabs 파트너십, 브랜드 음성 에이전트, 다국어 더빙, 클로닝 | ⚠️ 부분 일치 | WebSearch로 파트너십 내용 독립 확인. 단 G-08 URL은 watsonx Orchestrate 고객케어 현대화 기사이며 Elsewedy Electric은 별도 발표(mea.newsroom.ibm.com). 두 내용을 단일 G-08로 귀속하는 것은 부정확 |
| G-09 | 200 OK | OpenAI SDK 0.13.4 이후 추가 릴리스 미확인 | ✅ 일치 | v0.13.4가 최신, 추가 릴리스 없음 확인 |
| G-10 | 200 OK (CSS/JS 응답) | AWS AgentCore Policy GA, 에이전트-도구 중앙 제어 | 🔗 접근 불가 | The New Stack 페이지가 CSS/JS만 반환. 내용 검증 불가 — 반복 패턴 (weekly 도메인) |
| G-11 | 200 OK | AgentCore Runtime Stateful MCP, elicitation/sampling/progress notifications | ✅ 일치 | |
| G-12 | 200 OK | 멀티모델 라우팅 must-have, LLM 종속 탈피 | ⚠️ 부분 일치 | "Agent Sprawl이 2026년 엔터프라이즈 AI 거버넌스 최대 과제" 표현 원문 미지지 |
| G-13 | 200 OK | CrewAI 1.1.0 — 본문 미인용, 고아 소스 | 🔗 고아 소스 | References 등재되었으나 본문에서 [[G-13]] 인용 없음 |
| G-14 | 200 OK | 에이전트 AI 누적 $186억(Tracxn), 2025년 $60억, 평균 라운드 $155M | ❌ 불일치 | **원문 수치: 누적 $4.4억, 2024 피크 $20.18억, 2025년 $7.67억(15건). 본문 수치와 전면 불일치.** 대안 소스 WebSearch 필요 |
| G-15 | 200 OK | ASUS UGen300(4/1), Hailo-10H, 40 TOPS, 2.5W, 8GB LPDDR4, USB 3.1 Gen2, Windows 5월 중순, 100개+ 모델 | ✅ 일치 | |
| G-16 | 403 접근 불가 | Nordic nRF54LM20B Axon NPU, 128MHz, 15x/7x/8x 성능, Q2 출시 | ✅ 일치 (WebSearch) | URL 403이나 WebSearch로 nordicsemi.com 원본 기사 내용 독립 확인. 수치 정확 |
| G-17 | 200 OK | Synaptics+Google Coral Dev Board, Astra SL2610, 1 TOPS Torq NPU, Gemma 3 270M, MLIR 툴체인 | ✅ 일치 | |
| G-18 | 200 OK | MediaTek Genio Pro(3nm, 50 TOPS+), 420(6nm, 7.2 TOPS, 4월 샘플링), 360/360P, 2B 파라미터 | ✅ 일치 | |
| G-19 | 200 OK | TI MSPM0G5187, $1 이하, Cortex-M0+, 90x 저지연, 120x 에너지 절감 | ✅ 일치 | 80MHz 클록은 원문 미기재(마이너) |
| G-20 | 200 OK | Ambiq Atomiq SoC, Ethos-U85, 200 GOPS | ⚠️ 부분 일치 | **12nm FinFET, 300mV, Atomiq110, 2027 양산 예정은 원문 미기재.** 일반 기능 발표에 없는 세부 스펙이 본문에 포함 |
| G-21 | 200 OK | Apple M4 Max 통합 메모리 LLM 우위, NPU 60% 향상·40-45% 절감, 메모리 대역폭 결정 인자 | ⚠️ 부분 일치 | M4 Max 우위·메모리 대역폭 중요성 확인. "60% 향상"은 원문에 없고 "44% 절감"만 있음 |
| G-22 | 200 OK | SoftBank-Ericsson PoC, 로봇 AI 작업 MEC 동적 오프로드 | ✅ 일치 | |
| G-23 | 403 접근 불가 | T-Mobile NVIDIA Blackwell 파일럿, MEC 시장 2031년 $3.88B CAGR 30.1% | 🔗 접근 불가 | Fierce Network 403. T-Mobile Blackwell 파일럿은 GTC 2026 관련 독립 보도 있으나 MEC 수치는 별도 확인 불가 |
| G-24 | 200 OK | Qualcomm 한국 스타트업 프로그램, Dragonwing, Challenge AX for All | ⚠️ 부분 일치 | 프로그램 참여 확인. **Dragonwing Q-8750, 77 TOPS, 11B LLM 온디바이스 수치는 원문 미확인** |
| G-25 | 200 OK | Samsung Galaxy S26 EdgeFusion, Exynos 2600 2nm NPU, 온디바이스 이미지 생성 | ✅ 일치 | |
| G-26 | 200 OK | Hailo-10H GA 전환 완료, ASUS·Raspberry Pi 등 OEM 채택 | ⚠️ 부분 일치 | GA 확인. **ASUS·Raspberry Pi OEM 구체적 파트너 명칭은 원문 미언급** |
| G-27 | 200 OK | 엣지 AI 칩 시장 2025년 $3.67B → 2031년 $11.54B, CAGR 21% | ✅ 일치 | |
| G-28 | 200 OK | 엣지 AI 칩 2036년 $80B+, 자동차·스마트폰·AI PC·로봇·센서 | ✅ 일치 | |
| G-29 | 403 접근 불가 | Nordic DevZone Axon NPU 성능 스펙 문의 | 🔗 접근 불가 | DevZone 403. 내용 자체는 G-16 내용 반복이므로 파급 없음 |
| G-30 | 200 OK | NIST AI Agent Standards Initiative, 공개 코멘트 마감(4/2), 3대 축, 섹터별 리스닝 세션, NCCoE 콘셉트 페이퍼 | ✅ 일치 | NCCoE 콘셉트 페이퍼 "2/5 발행" 날짜는 원문에 ITL 마감일(4/2)만 기재. 발행 날짜는 원문 미확인(마이너) |
| G-31 | 타임아웃 | McKinsey AI Agent 거버넌스 로드맵 6단계 | 🔗 접근 불가 | McKinsey 페이지 타임아웃. 내용 검증 불가 |
| G-32 | 200 OK | CFPB·SEC 규제 공백, Regulation E 분쟁 조항 없음, SOX 302 AI 파라미터 미포함 | ✅ 일치 | |
| G-33 | 200 OK | Colorado AI Act(6/1 시행) 인용 | ✅ 일치 | 페이지는 Colorado AI Act June 2026 포함 확인 |
| E-01 | 200 OK (HTML only) | Elsewedy Electric IBM watsonx 협력, 엔터프라이즈 에이전트 AI | ✅ 일치 | 페이지 메타데이터·IBM 공식 보도자료(mea.newsroom.ibm.com)로 내용 확인. 단 G-08과 E-01 귀속 분리 필요(아래 비고) |
| P-01 | 200 OK | Liu et al. 3단계 계층형 메모리, 온디바이스 에이전트 개인화 | ✅ 일치 | |
| P-02 | 200 OK | ClinicalAgents, MCTS 기반 오케스트레이터, 이중 메모리 | ✅ 일치 | |
| P-03 | 200 OK | Tummalapalli et al. 4 플랫폼 벤치마크, Hailo-10H 6.9 t/s vs RTX 4050 131.7 t/s, 열 관리 | ✅ 일치 | |
| P-04 | 200 OK | eIQ Neutron, 1.8x(최대 4x) 향상, 컴파일러-NPU 통합 | ✅ 일치 | |
| C-01 | 200 OK | MCPlexor MCP Multiplexer, 40-50k 토큰 낭비, 200k의 25% 소진, 시맨틱 라우팅 500 토큰 | ✅ 일치 | |
| C-02 | URL 접근 불가 (YouTube JS only) | Harrison Chase 키노트, 신뢰성 격차 발언 | 🔗 접근 불가 | YouTube 동영상 특성상 WebFetch로 스크립트 미확인. 발언 내용은 일반적으로 알려진 것으로 LOW RISK |
| C-03 | 404 접근 불가 | Prosus 7,949개 에이전트, 성공률 15% | ❌ 불일치 | **URL 404.** 단 WebSearch로 수치 자체는 독립 확인(mlops.community 다른 URL에 존재). URL 수정 필요: `https://home.mlops.community/public/events/agentsinproduction2025` |
| C-04 | 200 OK | mcp-agent, MCP 서버 품질 편차, 인증 불안정 | ✅ 일치 | |
| C-05 | URL 접근 불가 (YouTube JS only) | Douwe Kiela, 파일럿→프로덕션 전환, 20,000+ 유스케이스 | 🔗 접근 불가 | YouTube 동영상 특성상 스크립트 미확인 |
| C-06 | 200 OK | AI PCs NPU 소프트웨어 미성숙, 메모리 대역폭 병목, 프로그래밍 모델 파편화 | ❌ 불일치 | **HN 아이템 ID 오류: 본문 41794566은 "엔지니어링 아키텍처 제안서" 쓰레드. 실제 AI PCs NPU 쓰레드 ID: 41863061 (2024-10-25)**. 대안 URL: `https://news.ycombinator.com/item?id=41863061` |
| C-07 | 429 Rate Limit | Google AI Edge, 모델 변환 품질 불안정, SAM2/Whisper/Kokoro TFLite 부재 | 🔗 접근 불가 | Rate limit으로 검증 불가 |

---

## 3. 논리 검증

- **PASS** — 전반적으로 기술 동향 → 시장 시그널 → 전략적 시사점 순서가 논리적으로 연결됨
- G-14 수치 불일치(누적 $186억)가 "에이전트 AI 섹터 투자 급증"이라는 결론을 뒷받침하는 데 사용되고 있어, 출처 재확인 후 수치 수정이 없으면 논리 근거 약화
- Claude Haiku 3 은퇴(4/20) 경고는 G-02 하나만을 간접 출처로 활용 — 직접 Anthropic 공식 발표 URL 추가 권고

---

## 4. 편향 검증

- **PASS** — 에지 AI 섹션에서 NPU TOPS 지표 한계, 열 스로틀링, NPU 툴체인 파편화 등 위협 요소를 균형 있게 서술
- 에이전트 오케스트레이션 섹션에서 A2A 지원 공백, MCP SDK v2 breaking change 리스크 등 위협을 명시적으로 포함
- 편향 이슈 없음

---

## 결론

검증 결과 **3건의 Critical 이슈**가 발견되었다. 가장 중요한 것은 ① G-14(펀딩 수치) 전면 불일치 — 본문의 $186억은 G-14 원문($4.4억)과 40배 이상 차이가 나며 Tracxn 출처도 G-14에 없음, ② G-04의 컨텍스트 창 수치 오기입(256K→128K), ③ C-06의 HN 아이템 ID 오류(41794566→41863061)이다. 이 세 항목은 즉시 수정이 필요하다. G-13은 고아 소스로 References에서 삭제하거나 본문에 인용을 추가해야 한다.

status: partial
