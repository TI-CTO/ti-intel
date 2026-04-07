---
validator_status: partial
target_file: /Users/ctoti/Project/ClaudeCode/outputs/reports/weekly/2026-04-07_weekly-agentic-ai.md
verified_at: 2026-04-07
---

# Validation Report: 2026-04-07_weekly-agentic-ai.md

## 요약
- 상태: PARTIAL (조건부 통과)
- 검증 건수: 32건 (G-01~G-20, E-01~E-10, P-01~P-02)
- 주요 이슈: Critical 2건(G-12 출처 귀속 오류, G-18 MCP 수치 미지지), Minor 3건(G-04 수치 표현 차이, G-07 ASN.1 수치 미확인, E-05 귀속 불완전)

---

## 1. 인용 검증

| 항목 | 결과 | 비고 |
|------|------|------|
| References 테이블 존재 | ✅ | 32건, 단일 통합 테이블 |
| 모든 [N] 인용 매칭 | ✅ | 본문 인용 코드 전수 확인 — 고아 인용 없음 |
| 미인용 소스 발견 | ✅ | G-17(Fierce ISAC)이 본문에서 인용되지 않음 — 고아 소스 |

### 고아 소스 (References에 등재되었으나 본문 미인용)

- **G-17** (Fierce Network — 6G and integrated sensing ISAC): 본문 어디에서도 `[[G-17]]` 인용 없음

---

## 2. 수치 검증

| 수치 | 출처 | 소스 수 | 판정 |
|------|------|---------|------|
| AI-RAN 시장 2025년 $2.96B → 2035년 $37.19B, CAGR 28.79% | G-13 | 1 | [B] 적절 — Precedence Research 원문 일치 |
| 아시아·태평양 CAGR 25.5%, 북미 37% 점유 | G-13 | 1 | ✅ 원문 수치 일치 |
| Open RAN 시장 2025년 $6.53B → 2033년 $45.09B, CAGR 26.8% | G-14 | 1 | ⚠️ 본문 "$450.9억" 표기는 $45.09B — 단위 표기 이상(억 달러) |
| AT&T-Ericsson Open RAN 5년 최대 $140억 | G-14 | 1 | ✅ 독립 검증(Light Reading, Fierce Network) 확인됨 |
| Deutsche Telekom 독일 3,000+ 사이트 | G-14 | 1 | ✅ 독립 검증(telecoms.com) 확인됨 |
| Bharti Airtel Mavenir 2,500개 Open RAN (10,000 확장 옵션) | G-14 | 1 | ✅ 독립 검증 확인됨 |
| AI-RAN Alliance 132개 회원사 | G-04, G-08 | 2 | ✅ Yahoo Finance/HPCwire에서 "132 members" 확인 |
| 기업 평균 12개 AI 에이전트 운영 | G-18 | 1 | ✅ Belitsoft 원문 일치 |
| 50%가 사일로 운영 | G-18 | 1 | ✅ Belitsoft 원문 일치 |
| MCP 9,700만 설치 돌파 | G-18 | 1 | ❌ G-18 원문에 해당 수치 없음 |
| 6G 상용 2030년 / Qualcomm 2028년(LA 올림픽) 프리커머셜 | G-10, G-07 | 2 | ✅ 양 출처 확인 |
| 3GPP Release 21 2026년 6월 확정 예정 | G-07 | 1 | ✅ Ericsson 블로그 확인 |
| ASN.1 동결 2029년 3월 | G-07 | 1 | ❌ G-07 원문에 ASN.1 2029년 3월 내용 없음 |
| SRv6 50ms 미만 경로 복원 | G-12 | 1 | ❌ G-12(APNIC 2020) 원문에 해당 수치 없음 |
| Jio 1억 가구·6억 고객 연결 목표 | G-12 | 1 | ❌ G-12(APNIC 2020)에 없음 — Cisco 케이스스터디 기반 독립 확인됨 |

---

## 보강 필요 항목

```yaml
reinforcement_needed:
  - claim: "MCP(Model Context Protocol) 3월 기준 9,700만 설치 돌파"
    current_sources: 0 (G-18 원문 미지지)
    suggested_keywords: ["MCP model context protocol 97 million installs 2026", "Anthropic MCP installations statistics 2026"]
  - claim: "ASN.1 동결 2029년 3월"
    current_sources: 0 (G-07 원문 미확인)
    suggested_keywords: ["3GPP Release 21 ASN.1 freeze 2029", "6G standardization timeline ASN.1"]
```

---

## 5. URL-Content 검증

| # | URL 상태 | 본문 주장 | 판정 | 비고 |
|---|---------|---------|------|------|
| G-01 | 200 OK | DOCOMO-SKT vRAN/AI-RAN 백서 3대 기술 요건, 세 번째 공동 백서 | ✅ 일치 | |
| G-02 | 접속 불가(소켓 오류) | Samsung+Vodafone Intel Xeon 6 SoC 유럽 최초 콜, Dell+Wind River, 2G/4G/5G 단일 서버 | ✅ 일치 | E-02(Samsung Business)에서 동일 내용 확인 |
| G-03 | 403 | Nokia L1 RAN 전체 CUDA 설계, T-Mobile·IOH·SoftBank 테스트, AITRAS 수익화 | ✅ 일치 | WebSearch(Nokia newsroom, SDxCentral, TheFastMode)에서 확인 |
| G-04 | 200 OK | NVIDIA 11개 기관 6G AI-native 공약, T-Mobile OTA 실증 | ⚠️ 부분 불일치 | "130+ companies"(원문)를 "132개"로 기재 — 수치는 G-08에서 132개 확인됨. T-Mobile OTA 생성형 AI 실증 내용은 G-04 원문에 없음 |
| G-05 | 403 | Ericsson ASIC 이기종 전략 vs Nokia CUDA 집중 대조 | 🔗 접근 불가 | 내용 검증 불가. E-06에서 "Cloud RAN software is portable by design" 확인됨 |
| G-06 | 200 OK | T-Mobile Ericsson NVIDIA 포터블 AI RAN 실증 | ✅ 일치 | |
| G-07 | 200 OK | 3GPP Release 21 2026년 6월 확정, Ericsson 6G 스펙 2028년 말, 2030년 첫 상용 | ⚠️ 부분 불일치 | "ASN.1 동결 2029년 3월" 원문에 없음 |
| G-08 | 200 OK (내용 미로딩) | SKT·Qualcomm·Vodafone 이사회 합류, 132개 회원사, Omdia 40% 채택 | ⚠️ 부분 불일치 | URL이 기본 조직 홈만 반환. 이사회 합류/132개 회원사는 Yahoo Finance 등에서 확인. Omdia 40% 수치는 독립 검증 불가 |
| G-09 | 403 | Intel AI-RAN Alliance 불참, NVIDIA-Marvell NVLink Fusion 파트너십 | 🔗 접근 불가 | |
| G-10 | JS 렌더링 불가 | Qualcomm Agentic RAN Management Service, X105 모뎀 R19 샘플링 | ⚠️ 부분 불일치 | WebSearch(Qualcomm 공식, Converge Digest)에서 Dragonwing RAN Automation Suite 및 Agentic Layer 확인. X105 R19 샘플링은 미확인 |
| G-11 | 403 | SKT-DOCOMO vRAN/AI-RAN 백서 분석 기사(Light Reading, 2026-04-02) | 🔗 접근 불가 | |
| G-12 | 200 OK | SoftBank-Arrcus SRv6 MUP 세계 최초 상용 도입, Jio 1억 가구·6억 고객, Zain Kuwait 배포, 50ms 미만 복원 | ❌ 불일치 | 이 URL은 2020년 5월 게시된 "SRv6: Deployed use-cases" 글로, 본문 주장들(SoftBank MUP, Jio, Zain Kuwait)이 전혀 없음. SoftBank SRv6 MUP 내용은 SoftBank 공식 PR(2025-12)에서 확인됨. Jio 수치는 Cisco 케이스스터디(cisco.com)에서 확인됨. 대안 URL 참고 |
| G-13 | 200 OK | AI-RAN 시장 2025년 $29.6억 → 2035년 $371.9억, CAGR 28.79%, AP CAGR 25.5%, 북미 37% | ⚠️ 부분 불일치 | Precedence Research 원문은 2025년 "$2.96 billion"인데 본문이 "29.6억 달러"로 표기 — 수치는 동일(억 달러 환산). 기준 연도 표기 정확. CAGR/지역 수치 일치 |
| G-14 | JS 렌더링 불가 | Open RAN $6.53B→$450.9억, AT&T $140억, DT 3,000+, Airtel 2,500 | ⚠️ 부분 불일치 | 5G World Pro 본문 콘텐츠 추출 실패. 수치들은 독립 검증(Grand View Research, Light Reading, Ericsson, telecoms.com)에서 확인됨. "$450.9억 달러"는 단위 혼용(실제 $45.09 billion) |
| G-15 | 200 OK | QCT Nokia anyRAN·NVIDIA ARC-Pro 지원 AI-RAN 서버 발표 | ✅ 일치 | |
| G-16 | 418 | IEEE INFOCOM 2026 6G AI-RAN 워크숍 | 🔗 접근 불가 | |
| G-17 | 403 | (본문 미인용 — 고아 소스) | 🔗 접근 불가 | 고아 소스. 삭제 또는 본문 인용 필요 |
| G-18 | 200 OK | 기업 평균 12개 에이전트, 50% 사일로, MCP 9,700만 설치 | ⚠️ 부분 불일치 | 12개/50% 확인. MCP 9,700만 수치 원문에 없음 |
| G-19 | 200 OK | EU AI Act AI 에이전트 거버넌스 분석 | ✅ 일치 | |
| G-20 | 200 OK | EU 간소화 제안 AI Act·GDPR 변경안, 에이전트 적용 범위 논의 | ✅ 일치 | |
| E-01 | 200 OK | Yu Takki 발언, DOCOMO-SKT 백서 공동 발간, 날짜 2026-03-31 | ✅ 일치 | |
| E-02 | 200 OK | Samsung+Vodafone vRAN 검증, Dell+Wind River, 2G/4G/5G 단일 서버 | ✅ 일치 | |
| E-03 | 403 | Nokia L1 RAN CUDA 설계, T-Mobile·IOH·SoftBank 테스트 | 🔗 접근 불가 | G-03(Nokia newsroom)에서 내용 확인됨 |
| E-04 | 403 | NVIDIA-텔코 11개 기관 6G 공약 | 🔗 접근 불가 | G-04(NVIDIA newsroom)와 동일 발표, G-04에서 확인됨 |
| E-05 | 200 OK | Ericsson ASIC 이기종 전략, T-Mobile Cloud RAN 포터블 실증 | ⚠️ 부분 불일치 | Ericsson MWC 발표 페이지에서 ASIC 명시 없음. Intel/NVIDIA/Qualcomm 협력은 확인됨. T-Mobile Cloud RAN 내용은 E-06에 귀속이 더 적절 |
| E-06 | 200 OK | Ericsson-T-Mobile NVIDIA 플랫폼 AI RAN 실증, "Cloud RAN portable by design" | ✅ 일치 | |
| E-07 | JS 렌더링 불가 | Qualcomm 6G 비전, device-to-data-center | 🔗 접근 불가 | JS 의존 페이지 |
| E-08 | 200 OK | SKT-Ericsson 5년 MoU, 5개 협력 영역(AI-powered RAN·5G 수익화·자율네트워크·Zero Trust·6G), 2026-03-18 | ✅ 일치 | MoU 만료일이 "2031-03-02"로 명시 — "5년 MoU" 표현 적절 |
| E-09 | 200 OK | SKT 1인 1 AI 에이전트, 에이닷 비즈·폴라리스·플레이그라운드, AXMS, 2026-03-16 | ✅ 일치 | |
| E-10 | 200 OK | KT MWC26 노코드 에이전트 빌더 공개, 드래그앤드롭, 회의록 자동화 | ✅ 일치 | |
| P-01 | 200 OK | Frontiers AI-native 6G 종합 리뷰, 시맨틱 통신·RIS·엣지 인텔리전스 | ✅ 일치 | |
| P-02 | 303 리디렉트 | Nature Communications 광대역 실시간 스펙트럼 감지 6G 논문(2026) | ✅ 일치 | 리디렉트 후 논문 존재 확인(WebSearch). DOI: 10.1038/s41467-026-70389-0 |

---

## 3. 논리 검증

- Ericsson ASIC 이기종 전략(E-05)과 "Cloud RAN portable" 주장(E-06) 분리 귀속이 혼용되어 있으나 논리적 모순은 아님. E-05 보도자료 원문에 "ASIC" 명시가 없어 G-05(Light Reading, 403)에 더 의존하는 구조이나 G-05 접근 불가로 확인 불가
- SRv6 관련 내용을 2020년 글로 인용(G-12)한 것은 논리적으로 문제: 본문에 서술된 사건들(2025년 SoftBank MUP 상용화, Jio 6억 고객)이 출처 게시 이후 발생했으므로 출처가 해당 주장을 지지할 수 없음
- 전체 논리 흐름(AI-RAN 표준화 → 실증 → 수익화 → 6G 로드맵)은 일관성 있게 구성됨

## 4. 편향 검증

- PASS. DOCOMO-SKT 협력 긍정 측면과 Intel AI-RAN Alliance 불참, 벤더 전략 분기(Ericsson vs Nokia) 등 위협/불확실 요인을 함께 서술함
- Omdia Open RAN 채택률 40%와 5G SA 전환율 저조(253개 중 77개 SA)를 함께 제시하여 균형 유지

---

## 결론

32건 References 전수 검증 결과 Critical 이슈 2건이 발견되었다.

**Critical-1 (G-12 출처 귀속 오류)**: 본문의 SoftBank SRv6 MUP 세계 최초 상용 도입, Jio 6억 고객/1억 가구, Zain Kuwait 배포, 50ms 복원 등의 주장이 APNIC 2020년 5월 블로그(G-12)에 귀속되어 있으나 해당 페이지에 이 내용들이 전혀 없다. SoftBank MUP는 2025년 12월 별도 보도자료, Jio 수치는 Cisco 케이스스터디에서 독립 확인된다.

**Critical-2 (G-18 MCP 수치 미지지)**: "MCP 3월 기준 9,700만 설치 돌파"가 Belitsoft 보고서(G-18)에 귀속되어 있으나 해당 페이지에 MCP 설치 수치가 없다.

Minor 이슈로 G-04 원문은 "130+" 표기인데 본문이 "132개"로 서술(G-08에서 132 확인됨), G-07 ASN.1 2029년 3월 원문 미확인, G-17 고아 소스(본문 미인용), G-14/$450.9억 단위 표기 혼용 등이 있다.

---

## 수정 권고

### Critical (출처 교체 필수)

**G-12 교체**
- 현재: APNIC Blog 2020년 SRv6 일반 글 (SoftBank/Jio/Zain Kuwait/50ms 내용 없음)
- 권장:
  - SoftBank SRv6 MUP 상용 도입: `https://www.softbank.jp/en/corp/news/press/sbkk/2025/20251218_01/` (2025-12-18, SoftBank 공식 PR)
  - Jio SRv6 + 1억 가구·6억 고객: `https://www.cisco.com/site/us/en/about/case-studies-customer-stories/reliance-jio.html` (Cisco 케이스스터디)
  - 50ms 복원은 별도 기술 문서 출처 필요

**G-18 MCP 수치 보강**
- "MCP 9,700만 설치" 수치 출처를 Belitsoft가 아닌 Anthropic 공식 발표 또는 MCP 공식 통계 URL로 교체
- 검색 키워드: `"MCP" "97 million installs" 2026` 또는 `Anthropic MCP usage statistics March 2026`

### Minor

**G-07 ASN.1 수치**
- "ASN.1 동결 2029년 3월" 출처를 3GPP 공식 일정 문서로 교체 또는 [추정] 태그 추가

**G-04 수치 표현**
- "132개 회원사" 표기 시 G-08을 주 출처로 명시 (G-04 원문은 "130+")

**G-14 단위 표기 오류**
- "450.9억 달러" → "450.9억 달러($45.09 billion)" 또는 "$450.9억"이 아닌 "$450.9억(약 45.09 billion USD)"으로 명확화

**G-17 고아 소스 처리**
- 본문에서 인용하거나 References에서 삭제

**접근 불가 URL 참고**
- G-05, G-09, G-11, G-16, G-17, E-03, E-04, E-07: 403/418/JS 렌더링 불가. 내용 자체는 독립 WebSearch로 대부분 확인됨. 향후 백업 URL(Wayback Machine 또는 대안 보도) 병기 권장
