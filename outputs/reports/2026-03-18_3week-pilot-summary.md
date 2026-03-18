---
type: summary
date: 2026-03-18
period: 2026-03-05 ~ 2026-03-20
title: Tech Intelligence Platform 3주 시범운영 누적 통계
---

# Tech Intelligence Platform — 3주 시범운영 누적 통계

> 기간: 2026-03-05 ~ 2026-03-18 (Phase 1~3, Week 1~3 Day 3)
> 최종 리뷰 예정: 2026-03-20 (금)

---

## KPI 달성 현황

| KPI | 목표 | 실제 | 달성률 | 상태 |
|-----|------|------|--------|------|
| intel_items | 500+ | **724건** | **145%** | ✅ 초과 달성 |
| weekly-monitor 실행 | 9회 | **9회** | **100%** | ✅ 달성 |
| WTIS 심층 분석 | 6건+ | **10건** | **167%** | ✅ 초과 달성 |
| portfolio.md | 3개 (도메인별) | **3개** | **100%** | ✅ 달성 |
| 자동화 파이프라인 | 완료 | 드라이런 통과 | **90%** | ⚠️ 설치 미실행 |

---

## 데이터 현황

### intel-store

| 항목 | 수치 |
|------|------|
| 전체 아이템 | **724건** |
| ├ news | ~600건 (83%) |
| ├ paper | ~100건 (14%) |
| └ patent | ~24건 (3%) |
| L3 토픽 | 25개 + 경쟁사 2개 = **27개** |
| 빈 토픽 (0건) | **0개** ✅ |
| 최소 토픽 건수 | **25건+** (보강 완료) |

### 성장 추이

| 시점 | 건수 | 비고 |
|------|------|------|
| Week 1 (3/6) | 361건 | Phase 1 시딩 |
| Week 2 (3/13) | 609건 | +248건, 500건 돌파 |
| Week 3 (3/18) | **724건** | +115건, 토픽 보강 |

---

## weekly-monitor 실행 이력 (9회)

| # | 날짜 | 도메인 | Deep | 주요 시그널 |
|---|------|--------|------|-----------|
| 1 | 3/3 | secure-ai | 4건 | PQC 규제 마감, LG U+ Anti-DeepVoice |
| 2 | 3/5 | secure-ai | — | 데이터 시딩 중 보조 실행 |
| 3 | 3/6 | axops | 2건 | 개편 전 마지막 |
| 4 | 3/9 | agentic-ai | 3건 | Claude Agent SDK, A2A 프로토콜 |
| 5 | 3/11 | secure-ai | 4건 | Google PLANTS/MTC, Cloudflare PQC SASE |
| 6 | 3/11 | voice-ai | 4건 | ElevenLabs 생태계, Voice Cloning 규제 |
| 7 | 3/16 | agentic-ai | 4건 | Claude MCP GA, OpenAI Agent SDK |
| 8 | 3/17 | voice-ai | 4건 | ElevenLabs 지배력, Big Tech 통합 |
| 9 | **3/18** | **secure-ai** | **3건** | VaaS $399, Intel Heracles, KT 2.0 |

### 도메인별 실행 횟수

| 도메인 | 횟수 | 스케줄 |
|--------|------|--------|
| secure-ai | 4회 (3/3, 3/5, 3/11, 3/18) | 수요일 |
| agentic-ai | 2회 (3/9, 3/16) | 월요일 |
| voice-ai | 2회 (3/11, 3/17) | 화요일 |
| axops (폐지) | 1회 (3/6) | — |

---

## WTIS 분석 (10건)

### 전체 목록

| # | 날짜 | 도메인 | L2 | 점수 | 판정 | 전략 |
|---|------|--------|-----|------|------|------|
| 1 | 2/24 | agentic-ai | Self Evolving Agent | — | Conditional | Build+Borrow |
| 2 | 2/26 | secure-ai | Secure AI v1 (전체) | 128 | Conditional | Borrow+Build |
| 3 | 3/3 | secure-ai | Secure AI v2 (전체) | 120 | Conditional | Borrow+Build |
| 4 | 3/9 | agentic-ai | Multi-Agent | 155 | Conditional | Buy+Borrow |
| 5 | 3/10 | secure-ai | OnDevice AI | 107 | 재검토 | Borrow+Build+B2B |
| 6 | 3/16 | agentic-ai | Hybrid AI Infra | 131 | Conditional | Borrow+Build |
| 7 | 3/16 | agentic-ai | Adaptive RAG | 131 | Conditional | Borrow+Build |
| 8 | 3/17 | voice-ai | Speech Generation | 128 | Conditional | Borrow+Build |
| 9 | **3/18** | **secure-ai** | **HE 키워드검색** | **125** | **Conditional** | **Borrow(CryptoLab)+Build** |
| 10 | **3/18** | **secure-ai** | **스팸/피싱 감지** | **115** | **재검토** | **Borrow+Build** |
| 11 | **3/18** | **voice-ai** | **Speech Perception** | **118** | **재검토** | **Borrow(API)+Build** |

### 판정 분포

| 판정 | 건수 | L2 목록 |
|------|------|---------|
| Go (160+) | 0 | — |
| Conditional Go (120~159) | **5** | Multi-Agent(155), Hybrid AI(131), Adaptive RAG(131), Speech Generation(128), HE 키워드검색(125) |
| 재검토 (80~119) | **3** | Speech Perception(118), 스팸/피싱(115), OnDevice AI(107) |
| No-Go (~79) | 0 | — |
| 미산출 | 1 | Self Evolving Agent (점수 없이 Conditional) |

---

## 포트폴리오 현황 (3도메인 10 L2)

### Agentic AI (5 L2)

| L2 | 점수 | 판정 |
|----|------|------|
| Trusted Multi-Agent | 155 | Conditional Go |
| Hybrid AI Infra | 131 | Conditional Go |
| 의도 파악 기술 | 131 | Conditional Go |
| Self Evolving Architecture | — | Conditional Go |
| Model & Delta Foundry | — | Watch (미평가) |

### Voice AI (3 L2)

| L2 | 점수 | 판정 |
|----|------|------|
| Speech Generation | 128 | Conditional Go |
| Speech Perception | 118 | 재검토 |
| Personal Intelligence | — | Watch (미평가) |

### Secure AI (2 L2, 하위 기술 세분화)

| L2 | 점수 | 판정 |
|----|------|------|
| 양자/동형암호 (HE 키워드검색) | 125 | Conditional Go |
| 스팸/피싱탐지 | 115 | 재검토 |
| (온디바이스 AI) | 107 | 재검토 |

---

## 자동화 현황

| 컴포넌트 | 상태 |
|----------|------|
| `run-weekly-monitor.sh` | ✅ 작성 완료, 요일 가드 동작 확인 |
| `log-to-obsidian.py` | ✅ 작성 완료, 드라이런 통과 |
| launchd plist (3개) | ✅ 문법 검증 통과 |
| Claude CLI | ✅ v2.1.78 확인 |
| **launchd 설치** | ⚠️ 미실행 (수동 운영 중) |

---

## MCP 서버 현황

| 서버 | 도구 수 | 상태 |
|------|---------|------|
| intel-store | 14 | ✅ 정상 |
| design-system | 3 | ✅ 정상 |
| trend-tracker | 5 | ✅ 정상 |
| startup-db | 15 | ✅ 정상 |
| youtube-transcript | 1 | ✅ 정상 |
| context7 | 2 | ✅ 정상 |

---

## 핵심 성과 요약

1. **데이터 기반 구축**: 724건 인텔리전스 아이템, 27개 토픽, 빈 토픽 0개
2. **운영 리듬 확립**: 월/화/수 도메인별 주간 모니터링 9회 실행
3. **의사결정 프레임워크**: WTIS v4.1로 10개 L2 기술 정량 평가 (200점 채점)
4. **포트폴리오 관리**: 3개 도메인 포트폴리오 구축, L2별 Go/No-Go 판정
5. **자동화 준비**: 스크립트 완성, 드라이런 통과 (설치만 남음)

## 남은 과제 (3/19~20)

- [ ] 팀 가이드 작성 (도구 레퍼런스, Quick Start)
- [ ] 최종 KPI 리뷰 + 이관 준비
- [ ] 자동화 설치 결정 (로컬 vs 서버)
- [ ] Startup DB Obsidian 재동기화 (펀딩 데이터 수정 반영)
