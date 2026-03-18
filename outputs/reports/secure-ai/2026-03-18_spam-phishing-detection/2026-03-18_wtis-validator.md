---
type: wtis-validator
target: 2026-03-18_wtis-skill1.md
date: 2026-03-18
validator_status: partial
---

# WTIS 교차검증: 스팸/피싱 감지(통화전)

## 검증 결과 요약

- **status: PARTIAL**
- 총 이슈: 6건 (Critical: 2, Minor: 4)
- 단일 소스 비율: 약 11% (핵심 수치 9개 중 1개 — VaaS $399/월)

---

## 이슈 목록

| # | 유형 | 심각도 | 내용 | 처리 제안 |
|---|------|--------|------|----------|
| 1 | 수치 오류 | **Critical** | "+91% YoY" [G-14] — 2024 854.5억 → 2025.1~10 1,056.6억 기준 실제 증가율 약 +23.6%. 어떤 비교 기준으로도 91%가 산출되지 않음 | 비교 기준 연도·기간을 명시하거나 수치 재계산 필요 |
| 2 | 수치 미확인 | **Critical** | Truecaller "EBITDA -49% YoY" [G-32] — 인용 출처(TechCrunch founders step down 기사)에 해당 수치 미기재. 2024 연간 보고서상 EBITDA는 SEK 684.2M vs 702.9M (약 -2.7% YoY)으로 -49%와 전혀 다름 | 원본 출처 재확인 필요. 해당 수치는 현재 미검증 상태 |
| 3 | 고아 소스 | Minor | P-03 (MDPI 2022 DeepDetection) — References 테이블에 등재되었으나 본문에서 한 번도 인용되지 않음 | 본문 인용 추가 또는 테이블에서 제거 |
| 4 | 출처-신뢰도 불일치 | Minor | [G-02] 인용 시 신뢰도 [A] 부여 — 등록된 URL은 Korea Herald 뉴스 기사(koreaherald.com)로 [B]급 소스. 1인당 5,290만원 및 5,724만 회선 수치에 [A] 태그를 붙이려면 MSIT/경찰청 원본 URL을 직접 인용해야 함 | G-02 URL을 MSIT 또는 경찰청 원문으로 교체하거나 신뢰도를 [B]로 하향 |
| 5 | 단일 소스 | Minor | VaaS "$399/월" — [G-01] Mirage Security 연구사 단일 소스. 신뢰도 섹션에서 [C]로 이미 플래그 처리됨. 추가 독립 소스 보강 권장 | 웹 검색 결과 Help Net Security 기사에서 동일 수치 확인 가능 — 2차 인용 소스 추가 가능 |
| 6 | 출처 누락 | Minor | Truecaller "4.5억 사용자, 77억건 식별(2025)" [G-32] — 인용 기사(TechCrunch founders step down 2024.11)는 이 수치를 담지 않음. 450M 사용자 돌파는 2025.04(별도 TechCrunch 기사), 77억건 식별은 2024년 연간 데이터에서 확인됨. G-32 단독으로는 이 두 수치를 지지하지 못함 | 사용자 수 및 식별 건수에 별도 소스 추가 필요 |

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | G-xx, E-xx, P-xx 3계열 구분 |
| 본문 [N] 인용 전수 테이블 매칭 | ✅ | 본문 인용 G/E/P 코드 전체 테이블에 존재 |
| 미인용 소스(고아 소스) 발견 | ❌ | P-03 (DeepDetection, MDPI 2022) — 테이블 등재 but 본문 미인용 |
| 미인용 주요 주장 발견 | ✅ | 모든 핵심 수치에 인용 코드 부여됨 |

**본문 인용 코드 목록 (중복 제거):**
- G계열: G-01, G-02, G-04~G-11, G-14~G-17, G-20~G-22, G-24~G-26, G-28~G-35, G-40, G-42, G-44
- E계열: E-01~E-07 (7건 전수)
- P계열: P-01, P-02

**테이블 미등재 인용: 없음 (0건)**

**테이블 등재 but 본문 미인용 (고아 소스): P-03 (1건)**

---

## 2. 수치 검증

| 수치 | 인용 | 소스 수 | 웹 교차검증 | 판정 |
|------|------|---------|-----------|------|
| 보이스피싱 피해 1조 567억원 (2025.1~10) | [G-14] | 2 (G-14, G-15) | 확인 — Korea Herald, AJU Press 동일 수치 | PASS [A] |
| 피해 +91% YoY | [G-14] | 1 | **불일치 — 2024년 854.5억 대비 +23.6%. 91% 산출 불가** | **FAIL (Critical)** |
| 1인당 평균 피해 5,290만원 | [G-02] | 2 (독립 검색 확인) | 확인 — Korea Herald, ScamWatch 동일 수치 | PASS (출처 신뢰도 등급 재검토 필요) |
| KT 탐지 정확도 97.2% | [G-08] | 1 | 확인 — Seoul Economic Daily 기사 및 Digital Today 기사로 교차 확인 | PASS [B] |
| SKT 11억건 차단 (+35% YoY) | [E-01] | 2 (E-01, G-11) | 확인 — 아시아경제, Telecompaper 동일 수치 | PASS [B] |
| KT Circuit Breaker 신고 25% 감소 | [E-02] | 1 | 확인 — Digital Today 독립 기사에서 교차 확인 가능 | PASS [B] |
| VaaS $399/월 (p1bot) | [G-01] | 1 | 확인 — Help Net Security 기사 내용 일치 | PASS [B] (단일 소스) |
| Meta 1.59억건 92% 선제 차단 | [E-05, G-05] | 2 | 확인 — Meta 공식 발표(about.fb.com), TechCrunch 보도 일치 | PASS [A/B] |
| Vishing 공격 442% 증가 | [G-24] | 1 ([C]) | 확인 — H1→H2 2024 비교. Programs.com 출처 [C]급. 신뢰도 [C] 표기 적절 | PASS [C] (맥락 명시 권장) |
| 가상화폐 보이스피싱 +660% | [G-14] | 1 | 확인 — Phemex News, Bitcoin Ethereum News 등 복수 보도 일치. 단, G-14(AJU Press)가 직접 이 수치를 포함하는지 미검증 | UNCERTAIN |
| Robocall Mitigation $5.6B → $21.1B, CAGR 14.2% | [G-25] | 1 | 확인 — Market Research Future 공식 페이지에서 동일 수치($5.585B → $21.13B, 14.23%) | PASS [B] |
| Truecaller EBITDA -49% YoY | [G-32] | 1 | **불일치 — 인용 기사에 해당 수치 없음. 2024 연간 EBITDA는 약 -2.7% YoY** | **FAIL (Critical)** |
| Truecaller 4.5억 사용자, 77억건 식별 | [G-32] | 1 | 수치 자체 확인 가능 (별도 출처), 그러나 G-32 기사(founders step down)에 해당 수치 미수록 | 출처 불일치 |
| Adaptive Security 누적 $136M | [G-30] | 1 | Series B $81M은 확인. 누적 $136M은 G-30 기사 내 언급 여부 미검증 | UNCERTAIN |

## 보강 필요 항목 (reinforcement_needed)

```yaml
reinforcement_needed:
  - claim: "피해 +91% YoY [G-14]"
    current_sources: 1
    issue: "2024 연간 854.5억원 대비 2025.1~10 1,056.6억원은 +23.6%로 91%와 불일치. 비교 기준 불명확"
    suggested_keywords: ["Korea voice phishing 2024 annual damage 854.5 billion won", "보이스피싱 2024 연간 피해액 경찰청"]

  - claim: "Truecaller EBITDA -49% YoY [G-32]"
    current_sources: 1
    issue: "인용 URL(TechCrunch founders step down) 기사 내 해당 수치 미발견. 실제 연간 EBITDA 변화와 괴리"
    suggested_keywords: ["Truecaller EBITDA 2024 annual report quarterly decline", "Truecaller Q financial results EBITDA YoY"]

  - claim: "가상화폐 보이스피싱 +660% 급증 [G-14]"
    current_sources: 1
    issue: "G-14(AJU Press)가 가상화폐 세부 통계를 직접 포함하는지 미검증"
    suggested_keywords: ["South Korea cryptocurrency voice phishing 660% increase 2025", "가상화폐 보이스피싱 660% 2025 경찰청"]
```

---

## 3. 논리 검증

**전반적으로 논리 일관성이 양호하나 1건 주의 필요:**

- **점수 계산 일관성**: 세부 점수 합산이 정확함. 9+8+5+8=30, 7+8+5+8=28, 7+5+5+7=24, 3+4+4+4=15, 5+4+4+5=18, 합계 115. 이전 분석 120/200에서의 -5 하향도 경쟁우위 -7, 실행가능성 -2, 고객가치 +2, 시장매력도 +2로 수학적으로 일치.

- **판정 기준 모순 (Minor)**: 섹션 7 말미에 "115점은 Conditional Go(120) 하한에 5점 미달이나 재검토(80~119) 범위의 최상단에 해당한다"고 기술하나, frontmatter의 `verdict: Conditional Go`와 문서 제목("Conditional Go, 115/200")은 Conditional Go로 표기함. 115점이 재검토 범위(80~119)에 속하는지 Conditional Go 범위(120~159)에 속하는지 기준이 모순됨. 이 분석의 최종 판정이 어느 범주인지 불명확.

- **3중 압박 → 경쟁우위 -7점 하향**: 논리 근거가 구체적으로 제시되어 있으며, Samsung+Meta+MS 동시 배포 사실이 복수 인용으로 뒷받침됨. 결론과 증거가 일관됨.

- **Borrow+Build 권고**: 시장 긴급도(9/10), 기술 격차(1~1.5년), 차별화 중요도(5/10), 시장 윈도우(<12개월) 등 파라미터 기반 의사결정 로직이 투명하게 서술됨.

---

## 4. 편향 검증

**전반적으로 균형 잡힌 분석. 특기 사항 없음.**

- 강점/리스크가 3축 분석(고객가치, 사업포텐셜, 기술경쟁력) 전 항목에 걸쳐 모두 제시됨.
- 경쟁사 분석이 국내(SKT/KT/LGU+/Samsung) + 글로벌(Meta/MS/Hiya/Truecaller) 모두 포함.
- Samsung S26의 위협을 "Critical Risk"로 명시하며 리스크를 과소평가하지 않음.
- 딥페이크 탐지 분야의 Arms Race 열세 및 실환경 성능 불안정을 리스크로 균형 있게 서술.
- WTP 데이터 부재, 유료화 전례 없음 등 불리한 데이터를 적극적으로 제시.
- [D] 태그를 통한 데이터 부족 항목 명시적 표시 — 편향 억제 메커니즘 작동.

---

## 5. 최종 판정

**status: PARTIAL**

보고서는 전반적으로 높은 인용 밀도와 균형 잡힌 분석을 보인다. 그러나 두 가지 Critical 이슈가 존재한다. 첫째, "+91% YoY" 피해 성장률은 2024년 공식 연간 피해액(854.5억원) 대비 계산하면 약 +23.6%로 산출되어 본문 수치와 일치하지 않으며, 비교 기준 연도·기간이 불명확하다. 둘째, Truecaller EBITDA -49% YoY는 인용 출처 기사에서 확인되지 않고, 실제 공시 자료와도 큰 차이가 있다. 아울러 판정 섹션에서 115점이 "재검토(80~119) 최상단"이면서 동시에 frontmatter에 "Conditional Go"로 표기되는 판정 기준 모순이 존재한다. 핵심 시장 판단(경쟁우위 열세, Conditional Go 방향성)에 영향을 주는 이슈는 아니나, 수치 신뢰도 측면에서 개선이 요구된다.

---

*검증 수행: validator agent (claude-sonnet-4-6) / 2026-03-18*
