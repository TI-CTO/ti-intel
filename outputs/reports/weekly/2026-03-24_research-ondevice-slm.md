---
type: deep-research
topic: ondevice-slm
l2: Hybrid AI Infra
date: 2026-03-24
parent: 2026-03-24_weekly-agentic-ai.md
---

# Deep 리서치: On-Device sLM (W14)

## 이전 대비 변화
- 전주: Gemma 3n GA + SmolLM3-3B SOTA 안정화, 신규 릴리스 없음
- 금주: OpenAI GPT-5.4 mini + nano 출시(3/17), TI NPU MCU(3/10), SLM "First, LLM Backup" 엔터프라이즈 패턴 확산
- 변화 방향: 오픈소스 sLM 안정화 위에 **상용 소형 모델(GPT-5.4 mini/nano) 등장** → 엔터프라이즈 에지 도입 가속

## 기술 동향

1. **OpenAI GPT-5.4 mini + nano 출시(3/17) — "가장 능력 있는 소형 모델".**
   GPT-5.3 출시 2일 만에 GPT-5.4 발표. GPT-5.4 mini는 코딩·추론·에이전틱 워크플로우에서 GPT-5 mini 대비 전면 향상, 2x 이상 빠른 실행. tool search 네이티브 지원으로 에이전트 대규모 도구 생태계 효율적 활용. nano 모델은 모바일·IoT 타깃. [[G-01]](#ref-g-01)

2. **SLM-First, LLM-Backup 엔터프라이즈 패턴 정착.**
   성숙한 엔터프라이즈 AI 아키텍처에서 일상 요청 80%를 로컬 sLM으로 처리, 복잡한 20%만 클라우드 LLM으로 라우팅하는 티어드 전략이 표준화. AI 컴퓨트 비용 60-70% 절감 효과. Phi-4(3.8B), Gemma 3(270M~), Qwen3-8B, SmolLM3-3B가 주요 선택지. [[G-02]](#ref-g-02)

3. **Google AI Edge RAG — 온디바이스 RAG (Retrieval-Augmented Generation) 라이브러리.**
   Google AI Edge가 온디바이스 RAG를 정식 지원. 파인튜닝 없이 대량 데이터에서 관련 정보를 sLM에 제공. Android 우선, 멀티플랫폼 확장 예정. Gemma 3n 멀티모달(텍스트·이미지·비디오·오디오) + RAG 결합으로 온디바이스 에이전트 역할 수행 가능. [[G-03]](#ref-g-03)

4. **NPU 세대교체 본격화 — 2026형 칩셋의 sLM 최적화.**
   Qualcomm X2, Samsung Exynos 2600, MediaTek 신규 NPU가 sLM 추론 전용 최적화. 4비트 양자화 상태에서 Gemma 3 4B가 Apple Silicon M-시리즈에서 인터랙티브 속도 달성. TI NPU MCU는 초저전력 에지(90x 지연 감소, 120x 에너지 절감)에서 sLM 실행 가능성 시연. [[G-04]](#ref-g-04), [[G-05]](#ref-g-05)

## 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| OpenAI | GPT-5.4 mini + nano 출시(3/17), tool search 네이티브, 모바일·IoT 타깃 | [[G-01]](#ref-g-01) |
| Google | Gemma 3n 멀티모달 GA, AI Edge RAG 라이브러리, LiteRT HuggingFace 커뮤니티 | [[G-03]](#ref-g-03) |
| Microsoft | Phi-4 mini(3.8B) 엔터프라이즈 에지 주력 | [[G-02]](#ref-g-02) |
| HuggingFace | SmolLM3-3B SOTA 유지, 온디바이스 최적화 도구 확장 | [[G-02]](#ref-g-02) |
| TI | NPU 내장 MCU(3/10) — 초저전력 에지 AI 하드웨어 | [[G-05]](#ref-g-05) |

## 시장 시그널

**시장 전망**
- SLM 시장 2026~2034 고성장 전망, 에지 AI 혁명의 핵심 동력 [[G-06]](#ref-g-06)
- Gartner: 2027년까지 과업별 소형 AI 모델 사용이 범용 LLM 대비 3배 [[G-06]](#ref-g-06)

**도입 사례**
- 엔터프라이즈 "sLM-First" 아키텍처: 일상 요청 80%를 로컬 처리, 비용 60-70% 절감 [[G-02]](#ref-g-02)
- Apple: Siri에 Gemini 탑재 계획(2026.1 발표), Private Cloud Compute로 프라이버시 유지 [[G-03]](#ref-g-03)

**연구 동향**
- Qwen3-8B: 듀얼모드 추론(thinking/non-thinking) + 확장 컨텍스트로 엔터프라이즈 에지 주목 [[G-02]](#ref-g-02)
- MoE 모델(Mixtral-8x7B)의 온디바이스 한계: "컴퓨트는 빠르나 메모리 셔플링이 병목" [[G-07]](#ref-g-07)

## 시장 수요

**고객 페인포인트**
- 모델 크기 vs 성능 트레이드오프 — 4GB RAM 환경에서 실용적 품질 달성 과제
- MoE 모델의 전문가 로딩 병목(메모리 셔플링 > 컴퓨트)
- 도메인 특화 파인튜닝을 위한 고품질 데이터 확보 어려움

**도입 장벽**
- 기존 LLM 인프라 투자에 대한 조직 관성 — sLM 전환 저항
- sLM 전용 벤치마크 부재로 엔터프라이즈 과업별 성능 비교 어려움
- AI/ML 인재 부족 + sLM 파인튜닝·유지보수 역량 갭

**시장 니즈**
- 턴키 sLM 배포 + 에지 최적화 + 매니지드 서비스 결합 제품
- 프라이버시 보존 온디바이스 AI(의료·금융·통신 규제 산업 핵심 요구)

## 전략적 시사점

1. **GPT-5.4 mini/nano의 상용 진입** — OpenAI가 소형 모델 시장에 본격 진입. 기존 오픈소스 sLM(Gemma, Phi, SmolLM) 대비 성능·편의성 경쟁 심화.
2. **sLM-First 아키텍처 도입 검토** — 80% 로컬 + 20% 클라우드 패턴으로 비용 60-70% 절감. 자사 AI 서비스에 티어드 전략 적용 가능성 평가.
3. **온디바이스 RAG** — Google AI Edge RAG처럼 파인튜닝 없이 도메인 데이터를 sLM에 주입하는 패턴이 표준화. 자사 서비스의 온디바이스 RAG 파이프라인 검토.
4. **NPU 세대교체 활용** — 2026형 NPU가 sLM 전용 최적화를 제공. 단말 연동 AI 서비스 기획 시 NPU 성능 기준 반영.

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | 9to5Mac — OpenAI GPT-5.4 mini/nano | [링크](https://9to5mac.com/2026/03/17/openai-releases-gpt-5-4-mini-and-nano-its-most-capable-small-models-yet/) | G | 2026-03-17 | high |
| <a id="ref-g-02"></a>G-02 | Iterathon — sLM Enterprise 2026 가이드 | [링크](https://iterathon.tech/blog/small-language-models-enterprise-2026-cost-efficiency-guide) | G | 2026-03 | medium |
| <a id="ref-g-03"></a>G-03 | Google Developers Blog — AI Edge sLM + RAG | [링크](https://developers.googleblog.com/google-ai-edge-small-language-models-multimodality-rag-function-calling/) | E | 2026-03 | high |
| <a id="ref-g-04"></a>G-04 | Meta Intelligence — Phi-4 vs Gemma 3 vs Llama 3.3 | [링크](https://www.meta-intelligence.tech/en/insight-slm-enterprise) | G | 2026-03 | medium |
| <a id="ref-g-05"></a>G-05 | TI Newsroom — 에지 AI MCU 포트폴리오 | [링크](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-10-ti-expands-microcontroller-portfolio-and-software-ecosystem-to-enable-edge-ai-in-every-device.html) | E | 2026-03-10 | high |
| <a id="ref-g-06"></a>G-06 | Research and Markets — SLM Market 2026-2034 | [링크](https://www.researchandmarkets.com/reports/6183431/small-language-model-slm-market-outlook) | G | 2026-03 | medium |
| <a id="ref-g-07"></a>G-07 | Edge AI Vision Alliance — On-Device LLMs 2026 | [링크](https://www.edge-ai-vision.com/2026/01/on-device-llms-in-2026-what-changed-what-matters-whats-next/) | G | 2026-01 | medium |
