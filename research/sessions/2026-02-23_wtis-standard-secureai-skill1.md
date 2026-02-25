---
topic: SecureAI 선정검증
date: 2026-02-23
wtis_skill: SKILL-1
confidence: medium-high
status: completed
---

# WTIS SKILL-1 선정검증: SecureAI

## 경영진 요약

> 글로벌 AI 사이버보안 시장은 2025년 약 340억 달러에서 2030년 860억 달러로 연 22.8% 성장이 예상되며, 한국 AI 기본법(2026년 1월 시행)·EU AI Act가 규제 수요를 폭발적으로 창출하고 있다. SKT·KT는 각각 5년간 7,000억·1조 원의 보안 투자를 선언하며 시장 선점에 나섰고, LG U+는 '보안퍼스트' 전략과 ixi-GEN sLLM을 보유하나 AI 거버넌스 전문 솔루션은 아직 공백 상태다. 200억 원 B2B 매출·50사 기업 고객이라는 KPI는 현실적으로 달성 가능하나, 기술 자체보다 규제 컴플라이언스 + 신뢰 브랜딩이 핵심 차별화 요인이 될 전망이다. 글로벌 전문업체(Palo Alto, Cisco 등)의 한국 진출 속도를 감안할 때 선택적 Buy + Borrow 전략으로 18개월 내 시장 진입이 권고된다.

## 1. 목표 객관성 검증

### KPI SMART 검증: Pass
- KPI 1: B2B 매출 200억 원 (3년) — 한국 네트워크 보안 시장 7,601억 원 대비 약 2.6% 점유율
- KPI 2: 기업 고객 50사 — 규제 시행 첫 해 수요 감안 시 현실적
- 단, 50사 × 4억 원 단가 가정 검증 필요

### TAM/SAM/SOM
- TAM: 글로벌 AI 사이버보안 $34.1B(2025) → $86.3B(2030), CAGR 22.8%
- SAM: 한국 AI 보안·거버넌스 B2B 약 2,000~2,100억 원(2025)
- SOM: 200억 원 = SAM 성장 후(2028 약 3,900억) 5.1% 점유율 — 달성 가능

## 2. 대체기술 맵

| 기술 | 파괴성 | TRL | 사분면 |
|---|---|---|---|
| LLM Guardrails | 높음 | 7~8 | [베팅] |
| AI Red Teaming | 높음 | 7~8 | [베팅] |
| Adversarial AI Defense | 높음 | 6~7 | [베팅/Watch] |
| Differential Privacy | 중간 | 6~7 | [Watch] |
| Federated Learning | 높음 | 6~7 | [Watch] |
| AI SBOM | 중간 | 5~6 | [Watch] |
| Model Watermarking | 중간 | 5~6 | [Watch] |
| Homomorphic Encryption | 높음 | 4~5 | [탐색] |

## 3. 경쟁사 현황

| 경쟁사 | 유사 과제 | 단계 | 투자 |
|---|---|---|---|
| SKT | 스캠뱅가드, AI 보안 플랫폼 | 상용화 | 5년 7,000억 |
| KT | K-시큐리티, AI 침투테스트 | B2B 확장 중 | 5년 1조 |
| Palo Alto | Protect AI 인수, AI 방화벽 | 글로벌 상용화 | $650~700M 인수 |
| Cisco | AI Defense, Robust Intelligence | 글로벌 상용화 | $400M 인수 |

## 4. 3B 전략 분석

| 영역 | 판단 | 이유 |
|---|---|---|
| LLM Guardrails / AI Red Teaming | **Buy** | 기술격차 2년+, 시장 긴급도 9/10 |
| AI 거버넌스 컴플라이언스 | **Build** | 차별화 9/10, 시장여유 18~24M, ixi-GEN 기반 |
| Federated Learning / DP / AI SBOM | **Borrow** | 차별화 중간, TRL 6~7 |
| Homomorphic Encryption | **Watch** | TRL 4~5, 단기 매출 기여 없음 |

## 5. Winning 전략 제언

[과제명]: SecureAI — AI 보안 및 거버넌스 솔루션
[추천 방향]: Buy + Build 혼합 (Borrow 보조)
[핵심 근거]:
  - 시장: AI 보안 CAGR 22.8%, AI 기본법 규제 수요 즉각 발생
  - 기술: LLM Guardrails·Red Teaming은 Buy, 거버넌스 컴플라이언스는 Build
  - 사업: B2B 2028 AI 서비스매출 2조 목표 포트폴리오 필수 항목
[리스크]:
  - SKT 선점 (높음) → 금융·의료·공공 수직 특화로 대응
  - Palo Alto/Cisco 직진출 (중간) → 로컬 컴플라이언스 특화 차별화
  - ixi-GEN 보안 특화 지연 (중간) → Buy로 즉각 보완
[Next Action]:
  1. 0~3개월: AI Red Teaming/LLM Guardrails 파트너 쇼트리스트 + M&A 협상
  2. 3~6개월: AI 거버넌스 컴플라이언스 PoC (ixi-GEN 기반)
  3. 6~12개월: 파일럿 기업 5~10사 확보
  4. 12~18개월: 50사 목표 채널 구축, 200억 매출 로드맵

## 신뢰도: Medium-High

## 참고 자료
- Gartner: Worldwide Information Security Spending 2025
- Fortune Business Insights: AI in Cybersecurity Market
- MarketsandMarkets: AI Governance Market
- 보안뉴스: SKT 7,000억, KT 1조 투자
- 전자신문: LG U+ 2028 AI B2B 2조 목표
- AI 기본법 원문 (국가법령정보센터)
- Lakera: AI Security Trends 2025
