---
topic: Speech Perception & Interaction
domain: voice-ai
l2_topic: speech-perception
date: 2026-03-18
wtis_version: v4.1
wtis_mode: standard
skills_executed: [research-deep, SKILL-1, validator]
confidence: medium
status: completed
total_references: 44
verdict: 재검토
score: 118/200
strategy: Borrow(Hume AI/Deepgram API) + Build(한국어 특화)
---

# WTIS Report: Speech Perception & Interaction

## Executive Summary

**시장**: Conversational AI TAM $11.6B(2024)→$41.4B(2030, CAGR 23.7%) [[G-05]](#ref-g-05). 음성 감정 인식 $1.3B→$3.1B(CAGR 12%) [[G-04]](#ref-g-04). 국내 AICC CAGR 23.7%.
**기술**: TRL 7~8(감정·맥락), 6~7(턴테이킹). IEMOCAP 81.33%(MemoCMT) [[P-01]](#ref-p-01). Hume AI EVI 3 레이턴시 1.2초.
**기회**: 한국어 특화 감정 인식 모델이 유일한 차별화 축. B2B AICC 고객 기반 활용 가능.
**위협**: EU AI Act 직장 내 감정 인식 금지(매출 7% 벌금) [[G-22]](#ref-g-22). SKT/KT 이미 상용화. Hume AI 한국어 진출(2026.01). Big Tech 플랫폼 통합 가속.
**권고**: Borrow(Hume AI/Deepgram API) + Build(한국어 특화). 경쟁우위(18/40)가 최대 약점 — 후발 진입의 차별화 공간 제한적.

## 1. 시장 분석

### TAM/SAM/SOM

| 구분 | 규모 | CAGR | 출처 |
|------|------|------|------|
| TAM (Conversational AI) | $11.6B(2024)→$41.4B(2030) | 23.7% | [[G-05]](#ref-g-05) |
| TAM (음성 감정 인식) | $1.3B(2025)→$3.1B(2032) | 12% | [[G-04]](#ref-g-04) |
| SAM (국내 AICC) | ~5,000억원 | 23.7% | [[G-09]](#ref-g-09) |
| SOM | 미정 | — | [D] |

## 2. 기술 성숙도 분석

### L3별 TRL

| L3 | TRL | 벤치마크 | 출처 |
|----|-----|----------|------|
| Emotional Analysis | 7~8 | IEMOCAP 81.33% (MemoCMT) | [[P-01]](#ref-p-01) |
| Context Recognition | 7~8 | Speech-LLM DST 상용화 진입 | [[P-06]](#ref-p-06) |
| Interrupt & Turn-Taking | 6~7 | Hume EVI 3 1.2초, Cartesia 45ms | [[G-12]](#ref-g-12) |

### 핵심 벤치마크

| 솔루션 | 성능 | 특이점 | 출처 |
|--------|------|--------|------|
| MemoCMT | IEMOCAP 81.33% | 멀티모달+맥락 기억 | [[P-01]](#ref-p-01) |
| Hume AI EV4-mini | 한국어 포함 다국어 | 2026.01 출시 | [[G-12]](#ref-g-12) |
| Vonova (Hume 적용) | 운영비 40% 절감 | B2B AICC 실증 | [[G-13]](#ref-g-13) |
| Cartesia | 45ms 레이턴시 | 실시간 턴테이킹 | [[G-12]](#ref-g-12) |

## 3. 경쟁 환경

### Gap Analysis

| 역량 | 자사 | SKT | KT | Hume AI | 격차 |
|------|------|-----|-----|---------|------|
| AICC 감정 분석 | 미보유 | CCaaS 상용(10+고객) | 에이센 상용 | API 제공 | **SKT/KT 선행** |
| 한국어 특화 | 미보유 | 에이닷(자체) | 믿:음(자체) | EV4-mini(2026.01) | **경쟁 치열** |
| 턴테이킹 | 미보유 | — | — | EVI 3 (1.2초) | **Hume 선행** |
| 정확도 공개 | — | 미공개 | 미공개 | 공개 | **투명성 부족** |

## 4. 전략 권고

**Borrow(Hume AI/Deepgram API) + Build(한국어 특화)**

| 기술 요소 | 전략 | 근거 |
|----------|------|------|
| 감정 인식 엔진 | **Borrow** | Hume AI API 활용, 자체 개발 비효율 |
| 한국어 감정 모델 | **Build** | 유일한 차별화 축. 한국어 데이터셋 구축 |
| 턴테이킹 | **Borrow** | Cartesia/Hume EVI 활용 |
| AICC 통합 | **Build** | 기존 B2B 인프라 활용 |

### 보완 필수 항목
- [ ] 한국어 감정 인식 벤치마크 확보 (데이터셋 구축 또는 파트너십)
- [ ] EU AI Act 국내 적용 시나리오 법무 검토
- [ ] SKT/KT 대비 차별화 전략 구체화

## 5. 교차검증 결과

**Validator 판정: PARTIAL** (Critical 1건, Warning 3건)

| # | 심각도 | 내용 | 처리 |
|---|--------|------|------|
| 1 | Critical | G-25 인용 맥락 불일치 — 카카오 판결 사실 미확인 | 본 보고서에서 해당 인용 제외 |
| 2 | Warning | **채점 합산 오류: 27+26+23+18+24=118, 131 아님** | **118/200으로 정정. 판정 "재검토"로 변경** |
| 3 | Warning | Hume AI $72.8M은 누적 투자, Series B 단독은 $50M | 수정 반영 |
| 4 | Warning | KT 3,000억 목표 기한 불명확 | 참고치로만 활용 |

## 6. 정량 평가 (118/200)

| # | 평가 항목 | 세부1 | 세부2 | 세부3 | 세부4 | 소계 |
|---|----------|-------|-------|-------|-------|------|
| 1 | 고객가치 | 8 (pain) | 7 (가치) | 5 (대체재) | 7 (수용성) | **27/40** |
| 2 | 시장매력도 | 8 (TAM) | 8 (CAGR) | 5 (타이밍) | 5 (규제) | **26/40** |
| 3 | 기술경쟁력 | 8 (TRL) | 4 (특허)[D] | 6 (장벽) | 5 (표준)[D] | **23/40** |
| 4 | 경쟁우위 | 4 (포지션) | 5 (지속성) | 4 (대응력) | 5 (생태계) | **18/40** |
| 5 | 실행가능성 | 5 (역량)[D] | 7 (ROI) | 6 (일정) | 6 (리스크) | **24/40** |
| | **총점** | | | | | **118/200** |

**판정: 재검토 (80~119)**

118점은 재검토 범위 최상단(Conditional Go 하한 120에 2점 미달). 고객가치(27)·시장매력도(26)는 양호하나, **경쟁우위(18)가 최대 약점** — SKT/KT 이미 상용화, Hume AI 한국어 진출, Big Tech 플랫폼 통합으로 후발 차별화 공간 극도로 제한.

**재검토 → Conditional Go 전환 조건:**
1. 한국어 감정 인식 IEMOCAP 상당 벤치마크 80%+ 확보 (필수)
2. EU AI Act 대응 법무 검토 완료 — B2B AICC 적용 적법성 확인 (필수)
3. SKT/KT 미커버 영역 식별 — 멀티모달, 실시간 턴테이킹 차별화 (필수)
4. Hume AI/Deepgram 파트너십 PoC 결과 확보 (필수)

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-04"></a>G-04 | Grand View — Emotion Detection Market $3.1B | [링크](https://www.grandviewresearch.com/press-release/global-emotion-detection-recognition-market) | report | 2025 | [B] |
| <a id="ref-g-05"></a>G-05 | Grand View — Conversational AI $41.4B | [링크](https://www.prnewswire.com/news-releases/conversational-ai-market-to-be-worth-41-39-billion-by-2030-at-cagr-23-7---grand-view-research-inc-302452404.html) | report | 2025 | [B] |
| <a id="ref-g-09"></a>G-09 | 국내 AICC 시장 전망 | — | report | 2025 | [C] |
| <a id="ref-g-10"></a>G-10 | KT Enterprise — AICC 매출 목표 | [링크](https://enterprise.kt.com/bt/dxstory/1057.do) | 공식 | 2025 | [B] |
| <a id="ref-g-12"></a>G-12 | Hume AI — EV4-mini 한국어 지원 | [링크](https://www.hume.ai/) | 공식 | 2026-01 | [A] |
| <a id="ref-g-13"></a>G-13 | Hume AI — Vonova 사례 운영비 40% 절감 | [링크](https://www.hume.ai/blog/case-study-hume-vonova) | 공식 | 2025 | [A] |
| <a id="ref-g-17"></a>G-17 | Google Cloud — CCAI 플랫폼 | — | 공식 | 2026 | [A] |
| <a id="ref-g-19"></a>G-19 | OpenAI — 2026 음성 모델 계획 | — | news | 2026 | [B] |
| <a id="ref-g-22"></a>G-22 | Wolters Kluwer — EU AI Act 감정 인식 금지 | [링크](https://legalblogs.wolterskluwer.com/global-workplace-law-and-policy/the-prohibition-of-ai-emotion-recognition-technologies-in-the-workplace-under-the-ai-act/) | 법률 | 2025 | [A] |
| <a id="ref-g-24"></a>G-24 | 법제처 — AI기본법 시행령 | [링크](https://www.moleg.go.kr/lawinfo/makingInfo.mo?lawSeq=84360&lawCd=0&lawType=TYPE5&mid=a10104010000) | 공식 | 2026 | [A] |
| <a id="ref-e-01"></a>E-01 | SKT — AI CCaaS 2025.03 출시 | [링크](https://news.sktelecom.com/208852) | 보도자료 | 2025-03 | [A] |
| <a id="ref-e-02"></a>E-02 | KT — 에이센 AICC | [링크](https://enterprise.kt.com/bt/dxstory/1057.do) | 보도자료 | 2025 | [A] |
| <a id="ref-p-01"></a>P-01 | MemoCMT — IEMOCAP 81.33% (Nature Sci. Rep.) | [링크](https://www.nature.com/articles/s41598-025-89202-x) | paper | 2025 | [A] |
| <a id="ref-p-06"></a>P-06 | Speech-LLM DST (arXiv:2510.09424) | [링크](https://arxiv.org/abs/2510.09424) | paper | 2025-10 | [A] |
