---
type: portfolio
domain: agentic-ai
domain_name: Agentic AI
updated: 2026-03-27
wtis_version: v4.1
total_l2: 5
evaluated: 5
---

# Agentic AI 포트폴리오

| L2 기술 | 최근 평가일 | 점수 | 판정 | 전략 | 세션 링크 |
|---------|-----------|------|------|------|----------|
| Self Evolving Architecture | 2026-02-24 | —/200 | Conditional Go | Build + Borrow | [[self-evolving-agent/2026-02-24_wtis-self-evolving-agent]] |
| Model & Delta Foundry | 2026-03-27 | 126/200 | Conditional Go | Borrow + Build | [[model-delta-foundry/2026-03-27_wtis-model-delta-foundry]] |
| Trusted Multi-Agent Orchestration | 2026-03-09 | 155/200 | Conditional Go | Buy + Borrow | [[multi-agent/2026-03-09_wtis-multi-agent]] |
| Hybrid AI Infra | 2026-03-16 | 131/200 | Conditional Go | Borrow + Build (L3별 차등) | [[hybrid-ai-infra/2026-03-16_wtis-hybrid-ai-infra]] |
| 의도 파악 기술 | 2026-03-16 | 131/200 | Conditional Go | Borrow + Build | [[adaptive-rag/2026-03-16_wtis-adaptive-rag]] |

## 종합 권고

- **우선 추진**: 해당 없음 (Go 판정 L2 없음)
- **조건부**:
  - Trusted Multi-Agent Orchestration (155/200) — 최고 점수. Claude Agent SDK 런타임 MCP, A2A v0.3 gRPC 등 표준 성숙 가속. 조건: 오케스트레이션 설계 역량 + MCP/A2A 표준화 선행
  - Self Evolving Architecture (—/200) — ACE/CORPGEN 생태계 성숙 지속. 조건: KPI 재설계, SMART 3/5 충족 필수
  - Hybrid AI Infra (131/200) — 4개 L3(Speaker Diarization TRL 9, On-Device sLM TRL 8, Edge AI TRL 7~8, AI-RAN TRL 6~7) 통합. L3별 차등 3B 전략 필요. 조건: 자사 내부 역량 데이터 확보, AI-RAN Alliance 가입, Speaker Diarization SDK 벤더 선정
  - 의도 파악 기술 (131/200) — Adaptive RAG(CRAG/Self-RAG) 기술 성숙(TRL 7~8). 조건: 한국어 Telco CRAG 평가기 PoC, 클라우드 인프라 파트너십
  - Model & Delta Foundry (126/200) — MLOps/GPU Orchestration 고성장 시장. SKT GPUaaS 선점($354M). 조건: NVIDIA 파트너십 확보, GPU 가동률 60%+ 달성, 특허 포트폴리오 구축
- **보류**: 해당 없음
- **미평가**: 없음 (전 L2 평가 완료)

## 도메인 인사이트

4개 L2 평가 결과, Agentic AI 도메인은 전체적으로 **Conditional Go** 밴드(131~155/200)에 위치한다. 공통 취약점:
- **경쟁우위** (평균 ~22/40): 모든 L2에서 SKT/KT 대비 후발 포지션
- **실행가능성** (평균 ~21/40): 자사 내부 역량 데이터 부재가 일관된 감점 요인
- **시장매력도** (평균 ~34/40): 모든 L2에서 고성장 시장 확인

Go 전환을 위한 핵심 조건: 자사 AI 인력·특허·파트너십 현황 데이터(I-xx) 확보 → 경쟁우위·실행가능성 재평가.

## 평가 이력

| 날짜 | L2 | 점수 | 판정 | 비고 |
|------|-----|------|------|------|
| 2026-02-24 | Self Evolving Architecture | — | Conditional Go | Proposal 모드, SMART 3/5 미충족 |
| 2026-03-09 | Trusted Multi-Agent Orchestration | 155/200 | Conditional Go | Standard 모드, 3B: Buy+Borrow |
| 2026-03-16 | — | — | — | 포트폴리오 구조 갱신: taxonomy 5 L2 정렬, W12 시그널 반영 |
| 2026-03-16 | Hybrid AI Infra | 131/200 | Conditional Go | Standard 모드, 3B: Borrow+Build (L3별 차등) |
| 2026-03-16 | 의도 파악 기술 | 131/200 | Conditional Go | Standard 모드, 3B: Borrow+Build |
| 2026-03-27 | Model & Delta Foundry | 126/200 | Conditional Go | Standard 모드, 3B: Borrow+Build. SKT GPUaaS 선점 대응 |
