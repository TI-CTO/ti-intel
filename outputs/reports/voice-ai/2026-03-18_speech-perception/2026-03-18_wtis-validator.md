---
validator_status: partial
target_file: /Users/ctoti/Project/ClaudeCode/outputs/reports/voice-ai/2026-03-18_speech-perception/2026-03-18_wtis-skill1.md
verified_at: 2026-03-18
---

# Validation Report

## 요약
- 상태: PARTIAL (Critical 1건, Warning 3건, 고아 소스 12건)
- 주요 이슈:
  1. [Critical] G-25 인용 맥락 불일치 — "카카오 감정 분석 스타트업 개인정보 위반 판결(2025.06)" 주장을 G-25(생성형 AI 개인정보 처리 안내서, Kim&Chang 일반 가이드라인)로 인용. 소스가 판결문이 아닌 범용 가이드라인이며, 카카오 관련 내용 없음
  2. [Warning] Hume AI 투자액 "$72.8M (Series B)" 표현 오류 — $72.8M은 Series B가 아닌 누적 총투자액 (Series A $12.7M + Series B $50M)
  3. [Warning] KT 3,000억 목표 기한 불명확 — 본문 "2025년 매출 3,000억+" 표기이나 일부 소스에서 2030년 목표로 언급됨
  4. [Warning] Hume AI "600+ 감정 태그" 독립 검증 불가 — Contrary Research(G-13) 인용이나 공식 Hume 문서에서 "600 tags" 수치 미확인
  5. 고아 소스 12건 (References 등재 후 본문 미인용)

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | G-xx, E-xx, P-xx 3개 섹션 |
| 모든 [N] 인용 매칭 (본문→References) | ✅ | 본문 인용 코드 전수 확인: G-03, G-07 등 일부 제외 전체 매칭 |
| 미인용 소스 발견 (References→본문) | ❌ | 고아 소스 12건 (아래 목록) |
| 인용 맥락 불일치 발견 | ❌ | G-25 Critical 불일치 (아래 상세) |

### 고아 소스 목록 (References에는 있으나 본문 미인용)

| 코드 | 출처명 | 등재 이유 (제목 기반 추정) |
|------|--------|--------------------------|
| G-03 | Fortune Business Insights | TAM 참고 (본문에서 G-01, G-02, G-04만 인용) |
| G-07 | NextMSC | 음성 시장 참고 (본문 미인용) |
| G-14 | gnani.ai | 턴테이킹 기술 (본문 미인용) |
| G-16 | MarkTechPost | 시장 동향 (본문 미인용) |
| G-20 | IBM Newsroom | Deepgram IBM 파트너십 (E-04와 중복, 본문 미인용) |
| G-23 | Inside Privacy | EU 규제 가이드라인 (본문에서 G-22만 인용) |
| G-26 | ElevenLabs | 시장 동향 참고 (본문 미인용) |
| E-03 | Hume AI 공식 사이트 | EVI 3 소개 (본문 미인용) |
| E-04 | IBM Newsroom | Deepgram IBM 통합 (G-20과 중복, 본문 미인용) |
| E-05 | NAVER CLOVA | Speech X (본문에서 G-18로 대체) |
| P-03 | arxiv MAMBA Fusion | 74.3% IEMOCAP (본문 미인용) |
| P-05 | Frontiers AI EmoShiftNet | F1 0.6885 IEMOCAP (본문 미인용) |

> 총 12건. 전체 소스(31건) 대비 38.7% 미인용. 연구 수집 단계의 소스가 분석 과정에서 탈락된 것으로 보이나 References 테이블에서 제거되지 않아 잔류.

### G-25 인용 맥락 불일치 (Critical)

본문 193행:
> "감정 분석 스타트업 카카오톡 데이터 무단 사용 → 개인정보보호법 위반 판결(2025.06)" [[G-25]](#ref-g-25)

G-25 실제 내용 (WebFetch 확인):
- 출처: Kim & Chang, "생성형 AI 개인정보 처리 안내서" (2025-08)
- 내용: 개인정보보호위원회가 발표한 생성형 AI 개인정보 처리 4단계 가이드라인 해설
- 카카오 감정 분석 스타트업 관련 내용 없음
- 판결문이 아닌 일반 가이드라인 문서

판단: 본문에서 주장하는 "카카오 감정 분석 스타트업 개인정보 위반 판결(2025.06)"은 G-25로 뒷받침되지 않음. 독립 웹 검색에서도 해당 판결 사실 확인 불가. 사실 자체 또는 인용 소스 모두 검증 실패.

---

## 2. 수치 검증

| 수치 | 소스 수 | 독립 검증 결과 | 판정 |
|------|---------|---------------|------|
| IEMOCAP UW 81.33% (MemoCMT) | 1 (P-01) | Nature Sci. Rep. 2025-02-14 게재 확인. 수치 정확 | ✅ [B] — 단일 소스이나 peer-reviewed |
| Conversational AI $41.39B 2030, CAGR 23.7% | 2 (G-05, G-08) | Grand View Research PR Newswire 확인. 수치 정확 | ✅ [B] |
| 국내 AICC 시장 5,000억 원 (2023) | 2 (G-09, G-08) | News2Day 기사 확인. 통신 3사 5,000억 공략 맥락 | ✅ [B] |
| Hume AI 총투자액 $72.8M | 1 (G-13) | Contrary Research 확인: $72.8M은 총 누적 투자(Series A $12.7M + Series B $50M). 정확한 수치이나 **"Series B $72.8M"으로 오표기** | ⚠️ 수치 맞으나 표현 오류 |
| Hume AI 600+ 감정 태그 | 1 (G-13) | Hume 공식 문서에서 "600 tags" 수치 미발견. Contrary Research에서만 언급 | ⚠️ [D] — 단일 소스, 1차 소스 미확인 |
| Cartesia TTS 45ms | 1 (G-13) | Contrary Research 확인: "cut latency from 90 to 45ms" 명시 | ✅ [B] |
| Vonova 운영비 40% 절감, 해결률 20% 향상 | 1 (G-13) | Hume AI 공식 케이스 스터디 확인. 수치 정확. 단, 실제 출처는 G-13(Contrary Research)이 아닌 Hume 공식 블로그 | ⚠️ 수치 정확, 원본 소스 불일치 |
| KT AICC 3,000억 매출 목표 | 1 (G-10) | GoodKyung 기사 2024년 확인. 단, 일부 소스에서 2030년 장기목표로 기술 — 2025년 목표로의 기한 확정 불명확 | ⚠️ [D] — 기한 불명확 |
| EU AI Act 벌금 EUR 35M/매출 7% | 1 (G-22) | Wolters Kluwer 법무 블로그 + EU AI Act 공식 텍스트 교차 확인. 정확 | ✅ [A] |
| SKT AI CCaaS 2025.03 출시, 10+ 기업 고객 | 1 (E-01) | SKT 뉴스룸 확인. 출시 3개월 만에 10개+ 기업 가입 사실 확인 | ✅ [A] |
| MarketsandMarkets EDR $42.9B 2027 | 1 (G-02) | MarketsandMarkets 보도자료 — 단일 소스, 시장 리서치사 특성상 [B] 적절 | ✅ [B] |

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "Hume AI 600+ 감정 태그"
    current_sources: 1
    note: "Contrary Research(G-13) 단독 언급. Hume 공식 문서에서 해당 수치 미확인"
    suggested_keywords: ["Hume AI emotion categories list", "Hume EVI emotion taxonomy 600"]

  - claim: "KT AICC 3,000억 원 2025년 매출 목표"
    current_sources: 1
    note: "GoodKyung(G-10) 단독 소스. 일부 검색 결과에서 2030년 목표로 기술됨 — 기한 불명확"
    suggested_keywords: ["KT AICC 3000억 2025", "KT 에이센 매출 목표 연도"]

  - claim: "카카오 감정 분석 스타트업 개인정보보호법 위반 판결 (2025.06)"
    current_sources: 0
    note: "G-25는 해당 판결문이 아닌 범용 AI 개인정보 가이드라인. 해당 판결 사실 자체 독립 검증 실패"
    suggested_keywords: ["카카오 감정 인식 스타트업 개인정보 판결 2025", "음성 감정 데이터 개인정보보호법 위반"]

  - claim: "Vonova 운영비 40% 절감, 해결률 20% 향상"
    current_sources: 1
    note: "수치는 Hume 공식 케이스 스터디에서 확인됨. 그러나 G-13(Contrary Research)으로 인용 — 원본 소스(Hume 공식 블로그)와 불일치"
    suggested_keywords: ["Vonova Hume AI case study 40% cost reduction"]
```

---

## 3. 논리 검증

전반적으로 논리 흐름은 일관성이 있다.

**PASS 항목:**
- SMART Test → Market Sizing → 경쟁사 Gap Analysis → 3B 판단 경로 → 점수 체계로 이어지는 논리 흐름이 일관됨
- "tech_gap > 2년 → BUY 조건이나 한국어 특화 인수 대상 부족 → Borrow + Build" 결론이 3B 프레임워크와 일치
- 131/200 Conditional Go 판정 (범위: 120~149)은 채점표 합산과 일치 (27+26+23+18+24=118... )

**주의 항목:**
- 채점 합산 재계산: 27+26+23+18+24 = **118**. 그러나 보고서는 **131**로 표기. 항목 합산(118)과 총점(131) 간 **13점 불일치** 발견. 판정 기준(120~149 Conditional Go)으로 보면 118점은 Conditional Go 범위 이하임

  | 항목 | 세부1 | 세부2 | 세부3 | 세부4 | 소계 |
  |------|-------|-------|-------|-------|------|
  | 고객가치 | 8 | 7 | 5 | 7 | 27 |
  | 시장매력도 | 8 | 8 | 5 | 5 | 26 |
  | 기술경쟁력 | 8 | 4 | 6 | 5 | 23 |
  | 경쟁우위 | 4 | 5 | 4 | 5 | 18 |
  | 실행가능성 | 5 | 7 | 6 | 6 | 24 |
  | **합계** | | | | | **118** |

  합산 118점 기준으로 "Conditional Go (120~149)" 판정 범위에 해당하지 않음. Pending(80~119) 범위에 속함. 총점 131이 맞다면 세부 점수 서술이 잘못된 것이고, 세부 점수 합산이 맞다면 총점과 판정이 틀린 것임.

- 시장 타이밍 5/10 채점과 Market Urgency 7/10 표기가 혼재. 본문 내 "Market urgency 7/10"은 3B 분석용 점수이고 채점표의 "시장 타이밍 5/10"은 별도 기준 — 동일 시장 타이밍을 두 척도로 다르게 평가한 것이나 설명 없이 혼용되어 혼란 가능

---

## 4. 편향 검증

**PASS 항목:**
- 경쟁사 분석에서 SKT/KT의 후발 우위를 명확히 인정 (경쟁우위 18/40 — 최저 항목)
- 리스크 섹션에서 EU AI Act, 개인정보, Big Tech 플랫폼 통합 위협을 균형 있게 기술
- Hume AI EV4-mini 한국어 지원(2026.01)이 차별화 기회를 축소한다는 부정적 요소 명시
- [D] 태그 4개 사용으로 데이터 부족 항목 명시

**주의 항목:**
- Vonova 40%/20% 수치가 Hume AI 자사 케이스 스터디에서 나온 것임을 감안할 때, 출처 편향(vendor-sponsored) 명시 부재

---

## 결론

총점 계산 오류(세부 합산 118 vs 표기 131)가 가장 중요한 이슈로, Conditional Go(120~149) 범위 판정의 수치적 근거가 흔들린다. G-25 인용은 주장("카카오 감정 분석 스타트업 판결")과 소스(범용 AI 가이드라인) 간 명백한 불일치로 해당 리스크 항목의 근거가 부재한 상태다. 고아 소스 12건(전체의 38.7%)은 정보 밀도 측면의 문제이나 본문 논리에는 영향을 주지 않는다. 이 두 이슈(채점 오류, Critical 인용 불일치)로 인해 판정을 PARTIAL로 설정한다.
