---
topic: Self Evolving Agent 교차검증
date: 2026-02-24
wtis_skill: SKILL-5 (Cross-Validator)
source_skill: SKILL-1
status: partial
---

# WTIS 교차검증: SKILL-1 / Self Evolving Agent

## 검증 요약

| 항목 | 결과 |
|------|------|
| 검증 대상 | SKILL-1: Self Evolving Agent 선정검증 |
| 검증 범위 | full (인용·수치·논리·편향 4가지) |
| 최종 판정 | PARTIAL |
| 검증한 클레임 수 | 12 |
| 확인됨 (CONFIRMED) | 4 |
| 부분 확인 (PARTIAL) | 2 |
| 오류 발견 (ERROR) | 1 |
| 검증 불가 (UNVERIFIABLE) | 5 |

---

## 인용 검증

| # | 원본 주장 | 검증 결과 | 비고 |
|---|-----------|-----------|------|
| 1 | NICE의 Cognigy 인수 USD 955M [출처23] | UNVERIFIABLE | 원본 URL HTTP 404. NICE IR 사이트 접근 불가. NICE 뉴스룸 메인에 Cognigy 제품 협업 언급은 있으나 인수 금액 미확인 |
| 2 | Genesys LAM 기반 에이전틱 에이전트 발표 "2026 FY Q1 (2-4월) 전면 출시" [출처22] | CONFIRMED | Genesys 뉴스룸 직접 확인: 발표일 02/10/2026, 제목 "Genesys Unveils Industry's First Agentic Virtual Agent Powered by LAMs for Enterprise CX" 일치 |
| 3 | Amazon Connect 29개 에이전틱 기능, AHT 38% 감소 (140초→87초), Centrica 1만명 배포 [출처21] | UNVERIFIABLE | 원본 URL HTTP 404 (`/amazon-connect-at-reinvent-2025`). 리디렉션 후에도 접근 불가. 대체 AWS 경로도 모두 404/접근 실패 |
| 4 | 금융위원회 금융분야 망분리 개선 로드맵 존재 [출처26] | CONFIRMED | fsc.go.kr HTTP 200, 2024-08-13 발표 보도자료 제목 직접 확인. SKILL-1의 "2024 로드맵" 기술 정확 |
| 5 | AI 기본법 2026.1 시행 [출처28] | CONFIRMED | peekaboolabs.ai HTTP 200, 페이지 제목 "2026년 시행", 본문에서 "2026년 1월 시행" 명시 확인 |
| 6 | 네이버클라우드 롯데카드 AICC 운영 리소스 40% 절감 [출처17] | CONFIRMED | aitimes.com HTTP 200, 헤드라인 "롯데카드 AICC 도입 2년 간 운영 리소스 40% 절감" 직접 확인 |
| 7 | SKT MWC 2026 Agentic AICC 전시 [출처12, 13] | CONFIRMED | SKT 뉴스룸 HTTP 200. "SK Telecom to Showcase Full-Stack AI Capabilities at MWC Barcelona 2026" 및 "agentic AI services" 언급 확인 |
| 8 | Goover 리포트 KT AICC 점유율 69% [출처14] | UNVERIFIABLE | Goover URL HTTP 403 접근 거부. 핀포인트뉴스[출처15]에는 점유율 수치 없음 ("선발주자" 일반 기술만). Goover [C등급] 단일 출처로 크로스체크 불가 |
| 9 | arXiv 2025년 7-8월 Self-Evolving Agent 첫 종합 서베이 발표 [출처1, 2] | CONFIRMED | arXiv.org HTTP 200. 2508.07407: 제출 2025-08-10, 제목 "A Comprehensive Survey of Self-Evolving AI Agents" 확인. 2507.21046: 제출 2025-07-28 확인 |
| 10 | ACL 2024 SSR 논문 (출처6) | CONFIRMED | aclanthology.org HTTP 200, "Mitigating Catastrophic Forgetting in Large Language Models with Self-Synthesized Rehearsal" 확인 |
| 11 | 전자신문 2026.01.28 "은행권 망분리 규제 완화 AI·SaaS 도입 가속" [출처30] | CONFIRMED | etnews.com HTTP 200, 제목 "은행권, '망분리 규제' 빗장 느슨해지자 AI·SaaS 도입 봇물…'합종연횡'까지 가속" 일치. 발행일 2026-01-28 확인 |
| 12 | 핀포인트뉴스 국내 AICC CAGR 23.7% [출처15] | CONFIRMED | pinpointnews HTTP 200. "연평균 23.7% 성장해 오는 2030년 3억5008만달러(약 4546억원)" 텍스트 직접 확인 |

---

## 수치 검증

| # | 지표 | 원본 값 | 검증 값 | 결과 |
|---|------|---------|---------|------|
| 1 | 국내 AICC 시장 SAM (2025년) | USD 350.88M / 4,815억원 | USD ~121M / ~1,656억원 (역산) | **ERROR: 과대 계상 가능성** |
| 2 | 국내 AICC 시장 CAGR 하한 | 23.7% | 23.7% (얼라이드마켓리서치, 핀포인트뉴스 확인) | CONFIRMED |
| 3 | 국내 AICC 시장 CAGR 상한 | 28.8% | 확인 불가 (SKILL-4 내부 참조) | UNVERIFIABLE |
| 4 | 국내 AICC 시장 2030년 규모 | 4,546억원 (핀포인트뉴스 인용) | 4,546억원 (핀포인트뉴스 직접 확인) | CONFIRMED |
| 5 | NICE Cognigy 인수 금액 | USD 955M | 확인 불가 (URL 404) | UNVERIFIABLE |
| 6 | Amazon Connect AHT 감소 | 38% (140초→87초) | 확인 불가 (URL 404) | UNVERIFIABLE |
| 7 | KT AICC 시장 점유율 | 69% | 확인 불가 (Goover [C등급] 단독) | UNVERIFIABLE |
| 8 | AI 기본법 시행일 | 2026년 1월 | 2026년 1월 | CONFIRMED |
| 9 | 금융위 망분리 로드맵 발표일 | 2024년 (로드맵) | 2024-08-13 | CONFIRMED |
| 10 | 네이버클라우드 롯데카드 절감율 | 40% | 40% | CONFIRMED |

### SAM 수치 상세 분석 (주요 오류)

SKILL-1은 국내 AICC 시장 SAM을 "2025년 약 4,815억원 (USD 350.88M)"으로 기재했다. 그러나 SKILL-1이 직접 인용한 핀포인트뉴스[출처15]에는 얼라이드마켓리서치 기준으로 국내 AICC 시장이 "CAGR 23.7%로 성장해 **2030년** 3억5008만달러(약 4546억원)"에 달할 것으로 기재되어 있다.

CAGR 23.7%를 역산하면:
- 2030년 USD 350.08M → 2025년 = 350.08 / (1.237)^5 ≈ **USD 120.9M ≈ 1,656억원**

즉, SKILL-1의 "2025년 SAM USD 350.88M"은 2030년 목표값($350.08M)과 거의 동일한 수치로, Goover [C등급] 단독 출처에 의존하고 있으며 얼라이드마켓리서치 기준 2025년 추정치보다 **약 2.9배 과대 계상된 것으로 의심된다.** 두 출처(Goover vs 얼라이드마켓리서치)의 시장 정의 차이일 가능성도 있으나, SKILL-1 보고서 내에서 이 수치를 SAM으로 단일 병기한 것은 신뢰도를 저하시킨다.

---

## 논리 검증

### 3B 전략 일관성

- **전반적으로 일관**: Build+Borrow 하이브리드 결론은 TRL 분류 (TRL 7-9 → Build, TRL 4-6 → Borrow)와 대체로 일관성이 있다. 금융 컴플라이언스 모듈을 Build로 분류한 것도 "글로벌 솔루션의 국내 규제 특화 어려움"이라는 근거와 논리적으로 연결된다.

- **취약점 1 - 내부 역량 대비 Build 비중**: 내부 역량을 5/10으로 평가하면서 Build를 60%로 권고했다. 역량 부족 상황에서 Build 비중이 높은 것에 대한 명시적 정당화 논리가 부족하다. "ixi-GEN sLLM 보유"만으로 AICC 자가 진화 기술 내재화가 가능한지는 [데이터 갭]으로 표기되었으나, 이것이 Build 판단에 미치는 영향이 충분히 논의되지 않았다.

- **취약점 2 - Buy 대안 미검토**: "시장 여유 18개월 기준 미충족"이라고 평가하면서도 Buy 옵션은 "전문 벤더 부재"와 "비용 초과 가능성"만으로 배제했다. 그러나 Cognigy 외에도 더 소규모의 Borrow/Buy 가능 스타트업(예: Parloa, Cognigy 경쟁사)에 대한 탐색이 없다.

- **취약점 3 - KT 격차 3-5년 극복 경로**: "KT 대비 격차 3-5년"이라고 진단하면서, Build로 이 격차를 극복할 수 있다는 로드맵 연결이 명시적이지 않다.

### 섹션 간 내부 모순

- **모순 없음**: SMART 테스트, TRL 맵, 경쟁사 분석, 3B 결론 간에 직접적인 내부 모순은 발견되지 않는다.

- **강조 불균형**: 리스크 테이블에서 "KPI 미구체화 R&D 방향 표류" 확률 H, 영향 H로 평가했으면서 Next Action에서 이 리스크 해소가 첫 번째 액션(0단계)에 배치된 것은 일관성 있게 처리되었다.

---

## 편향 검증

- **글로벌 빅플레이어 편중 없음**: Genesys, NICE, Amazon뿐 아니라 Google, SKT, KT, 네이버클라우드, 카카오 등 국내 경쟁사도 균형 있게 다루었다.

- **자가 진화 기술에 대한 낙관 편향 일부 존재**: "Self Evolving"을 차별화 포인트로 상정한 전제에서 출발했으나, 이 차별화가 고객(5대 시중은행)에게 실제로 선택 기준이 되는지에 대한 검증이 없다. 수요측 검증(고객 인터뷰, RFP 요건 분석) 없이 공급측 기술 분석에 집중한 편향이 있다.

- **반대 근거 제시**: TRL 낮은 기술에 대한 리스크("catastrophic forgetting 미해결", "프로덕션 적용 사례 극소")와 KT 선점 리스크를 명시적으로 기술한 점은 긍정적이다.

- **Goover [C등급] 과의존**: KT 69% 점유율과 SAM 4,815억원이라는 핵심 수치가 모두 접근 불가한 [C등급] 단일 출처(Goover)에 의존하고 있다. 이 수치를 기반으로 LG U+의 SOM을 "시장의 15-20% = 약 1,500억원"으로 산출한 부분이 연쇄적으로 불확실하다.

- **확증 편향 징후**: Build 결론이 분석 방향을 선도하는 구조이며 "Buy"가 처음부터 "국내 전문 벤더 부재"로 좁게 정의된 것은 검토 범위 제한으로 볼 수 있다. 그러나 이는 SKILL-1 자체 신뢰도(Medium)와 "추가 검증 필요" 섹션에서 투명하게 고백되었다.

---

## 수정 권고

| 우선순위 | 항목 | 현재 | 수정안 |
|----------|------|------|--------|
| **P1** | SAM 수치 혼용 | 2025년 SAM을 USD 350.88M/4,815억원으로 기재 (Goover [C등급]) | 얼라이드마켓리서치 기준 2025년 USD ~120M/~1,650억원으로 수정하거나, Goover 수치를 명확히 2030년 목표값과 구분하여 제시. "SAM 불확실 범위: 1,650억원(얼라이드마켓리서치 역산) ~ 4,815억원(Goover 추정)" 형태로 범위 표기 권장 |
| **P1** | NICE Cognigy 인수 금액 출처 | 원본 URL 404, 크로스체크 없음 | BusinessWire/PR Newswire 등 배포 채널 또는 SEC 공시(NICE Systems NASDAQ: NICE)를 통해 인수 금액 재확인. 확인 불가 시 "[UNVERIFIED]" 표기 |
| **P1** | Amazon Connect 수치 출처 | 원본 URL 404 | AWS 공식 블로그 현행 URL 확인 후 수정. 슬래시 포함 URL(`/amazon-connect-at-reinvent-2025/`)로 수정하거나, AWS What's New 페이지 또는 re:Invent 세션 자료를 대체 출처로 사용 |
| **P2** | KT 69% 점유율 출처 단일화 | Goover [C등급] 단독 | IDC/Gartner 국내 CCaaS 보고서 또는 KT IR 자료로 교차 검증. 확인 불가 시 "업계 추정 기준" 명시 |
| **P2** | Build 60% 정당화 논리 | 내부 역량 5/10이나 Build 60% 권고 근거 미흡 | "ixi-GEN sLLM + 에이전틱 콜봇(2025.12)이 RAG/LLM-as-Judge 구현을 위한 충분한 기반을 제공한다"는 사내 확인 내용을 주석으로 보완 |
| **P3** | Buy 옵션 탐색 범위 확장 | "국내 전문 벤더 부재"로 Buy 즉시 배제 | 해외 소규모 스타트업(Parloa, Laivly 등) 또는 기술 라이선스 거래 가능 여부 간략 검토 추가 |
| **P3** | 수요측 검증 부재 | 공급측 기술 분석 중심 | 5대 시중은행 RFP 요건 또는 AICC 도입 담당자 인터뷰 결과를 섹션 5 근거에 추가 권고 |

---

## 검증 방법 메타 평가

| 검증 수단 | 건수 | 성공 | 실패/불가 |
|-----------|------|------|----------|
| URL HTTP 접근 확인 | 14건 | 10건 | 4건 (NICE 404, AWS 404, Goover 403, AWS IR 000) |
| 페이지 텍스트 직접 확인 | 9건 | 8건 | 1건 |
| 수치 역산 검증 | 3건 | 1건 오류 발견 | - |
| 내부 논리 분석 | 4건 | 논리 갭 2건 발견 | - |

---

## 신뢰도 판정: Medium

**판정 근거:**

- **신뢰할 수 있는 부분**: 핵심 기술 TRL 평가, Genesys/SKT/네이버클라우드 관련 사실 확인, 규제 환경(망분리 로드맵·AI 기본법) 기술, arXiv 논문 인용, SMART 테스트 구조는 독립 검증에서 오류 없음.

- **신뢰 저하 요인**:
  1. SAM 수치(4,815억원)가 Goover [C등급] 단독 출처이며, 독립 확인 가능한 얼라이드마켓리서치 수치의 약 3배에 달하는 과대 계상 가능성이 있음.
  2. 핵심 수치 2건(NICE $955M, Amazon Connect AHT 38%/29개 기능)의 원본 URL이 404로 접근 불가하여 독립 검증 불가.
  3. KT 69% 점유율이 [C등급] 단독 출처로 전략 판단의 핵심 전제임에도 크로스체크 불가.

- **전략 방향 타당성**: Build+Borrow 하이브리드 방향 자체는 TRL 분류, 시장 긴급도, 내부 역량 수준을 종합할 때 합리적이다. 수치 오류가 전략 방향을 바꾸지는 않으나, SAM 과대 계상은 투자 규모 결정 시 오판을 유발할 수 있다.

