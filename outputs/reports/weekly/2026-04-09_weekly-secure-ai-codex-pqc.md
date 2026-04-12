---
type: weekly-monitor
domain: secure-ai
week: 2026-W15
date: 2026-04-09
l3_count: 5
deep_count: 3
tags:
  - codex
  - weekly
created: 2026-04-09
updated: 2026-04-09
---

# 주간 기술 동향: Secure AI (2026-W15 Codex PQC Update)

## Executive Summary

> **이번 주 핵심(2026-04-01~2026-04-09)**: Secure AI 도메인에서는 Post-Quantum Cryptography (PQC) 마이그레이션 압력이 가장 강했다. Scott Aaronson이 Google·Caltech 계열 결과를 교차 해석해 Elliptic Curve Cryptography (ECC)-256 공격 하한을 "25,000 물리 큐비트" 수준으로 제시했고(4/1), Nature와 Bruce Schneier가 각각 주류 과학 커뮤니케이션과 실무 아키텍처 관점에서 이를 확산했다(4/6). Fully Homomorphic Encryption (FHE) 쪽은 CryptoLab의 상용화 서사 확산과 Niobium The Fog의 프라이빗 베타가 병행됐지만, 성능 검증 공개 수준은 아직 제한적이다. 스팸·피싱 영역은 Microsoft가 AI 피싱 클릭률 450% 상승과 Device Code Phishing 자동화를 경고했고, 한국은 2026-04-02 시행령 개정안 입법예고로 정보공유 법제화를 추진했다.

| Layer 2 | 세부기술 | 신호 | 핵심 내용 |
|---------|----------|------|----------|
| 양자/동형 암호 | On-Device PQC | 🔴 | [기술돌파] Aaronson 25K 물리 큐비트 하한 제시 · [규제] 캐나다 PQC 마이그레이션 일정 본격화 · [생태계] Nature·Schneier가 위협을 주류 담론으로 확산 |
| | On-Device 동형암호 | 🟡 | [제품출시] Niobium The Fog 프라이빗 베타 · [생태계] CryptoLab 상용화 서사 확산 · [논문] Hermes·client-side FHE 최적화가 secure vector search 실용성을 보강 |
| | Secure Vector Search | 🟡 | Hermes가 MySQL 내 FHE 질의 처리 경로를 제시했지만, 상용 벤더의 독립 검증 벤치마크는 제한적 |
| 스팸/피싱탐지 | 스팸/피싱 감지(통화전) | 🟡 | [기술돌파] AI 기반 Device Code Phishing 자동화 · [규제] 한국 보이스피싱 정보공유 법제화 추진 · [생태계] AI 피싱 클릭률 450% 상승 경고 |
| | OCR 이미지 스팸 차단 | 🟢 | 이번 주기(2026-04-01~2026-04-09) 공개된 독립 시그널 없음 |

> **신호** : 🔴 긴급 — 경쟁사 출시, 규제 변경, 기술 돌파 | 🟡 주목 — 주요 발표·논문·표준 변화 감지 | 🟢 평온 — 유의미 변화 없음
> **태그** : [기술돌파] [제품출시] [경쟁사] [규제] [투자] [논문] [생태계]

---

## 🟢 Quick 요약 (변화 미미)

### Secure Vector Search
- Hermes(arXiv 2506.03308)가 MySQL 엔진 내부에서 FHE 기반 벡터화 관계형 질의를 처리하는 경로를 제시했다. 다만 이번 주기 기준 상용 secure vector search 제품군에서 독립 검증된 지연시간·비용 지표는 여전히 부족하다. [[P-01]](#ref-p-01), [[E-04]](#ref-e-04), [[G-05]](#ref-g-05)

### OCR 활용 이미지 스팸 차단
- 이번 주기(2026-04-01~2026-04-09) 동안 OCR 이미지 스팸 차단 관련 신규 공개 발표는 확인되지 않았다. 기존 온디바이스 분류·멀티모달 필터링 체계 유지 국면으로 판단된다.

---

## 🟡🔴 Deep 심층 분석

### On-Device PQC (양자내성암호) — 🔴 긴급

#### 이전 대비 변화
- 전주: Google이 공개키 노출 암호자산의 양자 취약성을 연구 블로그와 논문으로 공식화하고, 캐나다가 연방 PQC 로드맵을 공개했다. [[E-01]](#ref-e-01), [[E-02]](#ref-e-02)
- 금주: Aaronson이 ECC-256 공격 하한을 25,000 물리 큐비트 수준으로 재해석(4/1)했고, Nature가 이를 "real shock"으로 대중화했으며(4/6), Schneier는 위협 시점보다 crypto-agility 관점에서 PQC 전환 정당성을 강조했다(4/6). [[G-01]](#ref-g-01), [[G-02]](#ref-g-02), [[G-03]](#ref-g-03)
- 변화 방향: "양자 위협이 언젠가 올 수 있다"는 단계에서 "마이그레이션 준비를 지금 시작해야 한다"는 실행 담론으로 이동했다.

#### 기술 동향

1. **Aaronson — Google·Caltech 계열 결과를 교차 해석해 ECC-256 공격 하한을 25,000 물리 큐비트 수준으로 제시(4/1).**
   Aaronson은 Caltech/Oratomic 계열 qLDPC 코드 진전과 Google의 Shor 알고리즘 자원 추정 결과를 함께 읽으면, 특정 가정하에서 ECC-256 공격에 필요한 물리 큐비트 하한이 25,000 수준까지 내려갈 수 있다고 설명했다. 이는 "실제 구현까지 곧장 도달"을 뜻하지는 않지만, CRQC 논의가 더 이상 느슨한 장기 가정으로만 남아 있지 않음을 보여준다. [[G-01]](#ref-g-01)

2. **Nature — PQC 전환을 미룰 수 없는 주류 과학 담론으로 확산(4/6).**
   Nature는 최근 양자 보안 관련 결과를 "real shock"으로 묘사하며, 사이버보안 실무자와 정책기관이 PQC 마이그레이션을 더 공격적으로 준비해야 한다는 메시지를 강화했다. 학술 결과가 산업 의사결정 언어로 번역되기 시작한 점이 핵심이다. [[G-02]](#ref-g-02)

3. **Schneier — 위협 시점의 불확실성과 별개로 crypto-agility 관점에서 PQC 전환 지지(4/6).**
   Schneier는 2029년 이전 실용 양자컴퓨터 등장 가능성에는 신중했지만, 알고리즘 교체 유연성을 미리 확보하는 것이 합리적이라고 평가했다. 이는 보수적 실무자에게도 "지금 바로 전체 전환"이 아니라 "지금부터 교체 가능한 아키텍처 설계"라는 접근을 정당화한다. [[G-03]](#ref-g-03)

4. **캐나다 로드맵 — 2026년 4월 초기 부처별 PQC 계획, 2031/2035 완료 일정 제시.**
   Canadian Centre for Cyber Security는 2026년 4월 초기 부처별 PQC migration plan 수립과 연례 진척 보고를 요구하고, 고우선순위 시스템은 2031년 말, 나머지 시스템은 2035년 말까지 완료하는 일정표를 제시했다. "권고" 문서이지만 사실상 정부 조달·운영 기준을 선행 정렬하는 신호로 읽힌다. [[E-02]](#ref-e-02)

5. **NIST HQC 선정 — ML-KEM 단일 의존을 줄이는 백업 축이 유지됨.**
   NIST는 HQC를 다섯 번째 post-quantum encryption 알고리즘으로 선정해, 코드 기반 대안을 공식 포트폴리오에 추가했다. 이는 격자 기반 일변도 리스크를 낮추는 표준화 신호다. [[E-03]](#ref-e-03)

#### 플레이어 동향

| 기업/기관 | 동향 | 출처 |
|-----------|------|------|
| Scott Aaronson | 4/1 블로그에서 ECC-256 공격 하한 25,000 물리 큐비트 수준 해석 제시 | [[G-01]](#ref-g-01) |
| Nature | 4/6 기사로 양자 보안 위협을 주류 과학 담론으로 확산 | [[G-02]](#ref-g-02) |
| Bruce Schneier | 4/6 Google 2029 PQC 전환 계획을 crypto-agility 관점에서 긍정 평가 | [[G-03]](#ref-g-03) |
| Google | 공개키 노출 암호자산에 대한 양자 취약성 공개와 책임 있는 공시 프레임 제시 | [[E-01]](#ref-e-01) |
| Canadian Centre for Cyber Security | 2026년 4월 계획 수립, 2031/2035 완료 마일스톤 제시 | [[E-02]](#ref-e-02) |
| NIST | HQC 선정으로 PQC 알고리즘 포트폴리오 다변화 지속 | [[E-03]](#ref-e-03) |

#### 시장 시그널

**표준·정책**
- 캐나다 로드맵은 PQC를 "기술 검토"가 아니라 "부처별 계획과 보고" 대상으로 격상했다. [[E-02]](#ref-e-02)
- NIST HQC 선정은 vendor roadmap 상에서 ML-KEM 외 대체 라인업 확보 압력을 높인다. [[E-03]](#ref-e-03)

**상용화·실행**
- Google의 책임 있는 공시 방식은 암호자산과 네트워크 인프라 사업자 모두에게 "취약성 공개와 마이그레이션 커뮤니케이션"을 제품 전략의 일부로 편입시키는 선례가 됐다. [[E-01]](#ref-e-01)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- 위협 시점이 불확실해도, 이미 배포된 시스템에서 알고리즘 교체가 어렵다는 점이 가장 큰 실무 리스크다.
- PQC는 단일 알고리즘 교체가 아니라 인증서, 키 수명주기, 장비 호환성, 계약·조달 기준까지 함께 움직여야 한다.

**도입 장벽**
- 레거시 시스템은 crypto-agility가 설계돼 있지 않아, 실제 마이그레이션이 일정 발표보다 훨씬 오래 걸릴 가능성이 높다.
- 실시간 서비스에서는 PQC 서명·핸드셰이크 오버헤드가 통신 품질과 바로 연결된다.

**시장 니즈**
- 하이브리드 PQC 전환 경로와 암호 자산 인벤토리 자동화 도구 수요가 계속 커질 가능성이 높다.
- 통신·보안 사업자는 "지금 당장 완전 전환"보다 "교체 가능한 설계"를 먼저 상품화하는 편이 현실적이다.

#### 전략적 시사점

**기회**
- 통신·보안 장비 사업자는 Canada형 마일스톤 모델을 기준으로 PQC readiness assessment와 migration consulting 패키지를 설계할 수 있다.
- crypto-agility를 전면에 둔 하이브리드 배포 전략은 위협 시점 논쟁과 무관하게 구매 의사결정을 당길 수 있다.

**위협**
- 공개키 노출 자산, 장기 보관 통신 기록, 인증서 교체가 어려운 인프라는 HNDL(Harvest Now, Decrypt Later) 위험에 더 직접적으로 노출된다.
- 표준이 다변화될수록 제품 포트폴리오가 특정 알고리즘 하나에 과도하게 결합돼 있으면 재설계 비용이 커진다.

---

### On-Device 동형암호 키워드 검색 — 🟡 주목

#### 이전 대비 변화
- 전주: CryptoLab의 GS 인증 및 LG U+ 연계 실증, Niobium The Fog 발표로 FHE의 제품화 서사가 형성됐다. [[G-04]](#ref-g-04), [[E-04]](#ref-e-04)
- 금주: CryptoLab의 상용화 메시지가 확산됐고, Hermes·client-side FHE 최적화 논문이 secure vector search의 기술 기반을 보강했다. 동시에 Niobium은 베타 오픈을 진행했지만 독립 검증 공개 수준은 제한적이라는 반응이 나왔다. [[G-04]](#ref-g-04), [[G-05]](#ref-g-05), [[P-01]](#ref-p-01), [[P-02]](#ref-p-02)
- 변화 방향: FHE가 "기술 가능성" 단계를 넘어 "누가 먼저 검증 가능한 제품 지표를 내놓느냐"의 경쟁 구도로 옮겨가고 있다.

#### 기술 동향

1. **CryptoLab — 상용화 가능성 메시지를 공공·통신 중심으로 확산.**
   Seoul Economic Daily 기사 메타데이터와 설명에 따르면, CryptoLab은 Gartner recognition과 함께 homomorphic encryption의 full commercialization readiness를 healthcare, finance, telecom으로 확장 가능한 형태로 제시했다. LG Uplus `ixi-O`도 기사 키워드에 포함돼 있어, 통신 사용 사례가 여전히 핵심 레퍼런스다. [[G-04]](#ref-g-04)

2. **Niobium The Fog — 완전 암호화 상태의 AI/데이터 처리용 private beta 개시, late Q2 2026 공개 출시 목표.**
   PR Newswire에 따르면 The Fog는 private beta 상태로 공개됐고, 데이터 소유자가 키를 유지한 채 encrypted applications and AI workloads를 실행하는 private cloud 인프라를 표방한다. 이는 제품 메시지 측면에서는 강하지만, 실제 지연시간과 비용 구조는 추가 검증이 필요하다. [[E-04]](#ref-e-04)

3. **Hermes — MySQL 내 FHE 질의 처리 경로를 제시한 연구 시스템.**
   Hermes는 SIMD-aware 데이터 모델과 rotation-free aggregation, slot masking 기반 수정 알고리즘을 통해 MySQL의 native loadable functions 안에서 FHE 질의를 처리한다. arXiv 초록 기준으로 암호화 처리량 3,400배+, 삽입 4,000배+, 삭제 300배 가속을 제시해, secure vector search와 encrypted analytics의 실무 경로를 보여준다. [[P-01]](#ref-p-01)

4. **"Privacy at your Fingertips" — client-side FHE 오버헤드 감소가 온디바이스 배포 임계값을 낮춤.**
   IACR ePrint 2026/515는 bootstrapping을 활용한 client-side 최적화로 FHE의 느린 encryption/decryption과 ciphertext expansion 문제를 직접 겨냥한다. secure vector search가 실제 제품으로 가려면 서버 측 연산뿐 아니라 단말 측 오버헤드도 낮아져야 하므로, 이 논문은 상용화에 직접 연결되는 선행 기술이다. [[P-02]](#ref-p-02)

5. **Niobium 검증 압력 — 발표와 독립 벤치마크 사이 간극이 지적됨.**
   Zubnet.ai는 The Fog의 구체 암호 기법, 트랜스포머 추론 성능, AI 프레임워크 호환성이 충분히 공개되지 않았다고 지적했다. 벤더 발표와 별개로 시장이 "FHE 가능 여부"가 아니라 "구체적인 SLO와 비용"을 요구하기 시작했다는 의미다. [[G-05]](#ref-g-05) [추가확인 필요]

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| CryptoLab | Gartner recognition과 상용화 readiness 메시지를 공공·금융·통신 축으로 확산 | [[G-04]](#ref-g-04) |
| Niobium | The Fog private beta 시작, late Q2 2026 공개 출시 목표 | [[E-04]](#ref-e-04) |
| LG U+ | CryptoLab 연계 사례가 계속 FHE 통신 use case의 대표 레퍼런스로 언급 | [[G-04]](#ref-g-04) |
| 연구 커뮤니티 | Hermes와 client-side FHE 최적화가 secure vector search 실용성 논거를 보강 | [[P-01]](#ref-p-01), [[P-02]](#ref-p-02) |

#### 시장 시그널

**상용화**
- FHE 벤더 메시지가 "프라이버시 보호"에서 "AI 워크로드와 secure vector retrieval"로 이동했다. [[E-04]](#ref-e-04)
- 한국 시장에서는 공공 조달·통신 실증이 제품 신뢰를 만드는 핵심 레퍼런스로 기능한다. [[G-04]](#ref-g-04)

**검증**
- 제품 발표 이후 시장의 질문이 "가능한가"에서 "얼마나 빠르고 얼마가 드는가"로 바뀌고 있다. [[G-05]](#ref-g-05)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- FHE 도입의 병목은 알고리즘 자체보다 지연시간, 비용, 기존 DB/AI 스택과의 접착 문제에 있다.
- secure vector search는 검색 정확도뿐 아니라 색인 갱신, 삽입·삭제, 운영 도구 호환성이 중요하다.

**도입 장벽**
- 독립 검증 없는 성능 주장은 실제 구매 전환으로 이어지기 어렵다.
- client-side 오버헤드가 크면 모바일·엣지 적용은 곧바로 막힌다.

**시장 니즈**
- MySQL·vector DB·RAG 파이프라인에 얹을 수 있는 SDK/플러그인 방식이 가장 현실적이다.
- 벤치마크 공개, reference architecture, 통신·공공 실증 결과가 상용화 전환의 핵심이다.

#### 전략적 시사점

**기회**
- 한국 통신사 PoC와 공공 조달 레퍼런스를 선점한 플레이어는 FHE의 "설명 가능한 상용화"를 먼저 확보할 가능성이 높다.
- secure vector search는 FHE 전체를 전면 도입하는 것보다, 특정 retrieval 경로를 암호화하는 방식으로 먼저 시장에 안착할 수 있다.

**위협**
- 검증되지 않은 성능 서사가 반복되면 FHE 전체 시장 신뢰가 훼손될 수 있다.
- 대형 모델 추론까지 포함한 일반화된 FHE AI 플랫폼 메시지는 아직 과장으로 인식될 위험이 있다.

---

### 스팸/피싱 감지(통화전) — 🟡 주목

#### 이전 대비 변화
- 전주: AI 사기와 딥페이크 음성 탐지가 시장 이슈로 유지됐다.
- 금주: Microsoft가 AI 피싱 클릭률 450% 상승과 device code phishing 자동화를 공개했고, Help Net Security는 EvilTokens가 340개 이상 Microsoft 365 조직을 겨냥했다고 전했다. 한국은 2026-04-02 시행령 개정안 입법예고로 정보공유 제도화를 밀어붙였다. [[G-06]](#ref-g-06), [[G-07]](#ref-g-07), [[G-08]](#ref-g-08), [[E-05]](#ref-e-05)
- 변화 방향: 통화·이메일·OAuth 흐름이 분리된 위협이 아니라, 동일한 AI 자동화 피싱 체인으로 연결되는 양상이다.

#### 기술 동향

1. **Microsoft — AI 피싱 클릭률 450% 상승, agent ecosystem이 차기 공격 표면으로 부상.**
   Microsoft는 AI가 정교한 현지화와 역할 맞춤형 메시지를 가능하게 하면서 click-through rate를 약 12%에서 54% 수준으로 끌어올렸다고 밝혔다. 또한 "agent ecosystem will become the most attacked surface"라고 경고했다. [[G-06]](#ref-g-06)

2. **EvilTokens — Device Code Phishing의 서비스화와 대규모 확산.**
   Help Net Security는 EvilTokens가 340개 이상 Microsoft 365 조직을 겨냥했다고 전했다. 이는 MFA를 직접 우회하기보다, 사용자가 공식 `microsoft.com/devicelogin` 흐름 안에서 공격자의 세션을 승인하게 만드는 모델이다. [[G-08]](#ref-g-08)

3. **Microsoft 4/6 분석 — Dynamic Device Code Generation과 serverless redirect 인프라가 핵심.**
   Microsoft는 이 캠페인이 Vercel, Cloudflare Workers, AWS Lambda를 리다이렉트 체인에 활용하고, 사용자가 클릭하는 시점에 device code를 동적으로 생성해 15분 만료 한계를 우회한다고 설명했다. 즉, 단순 lure 품질 향상이 아니라 end-to-end automation이 성공률을 끌어올린 것이다. [[G-07]](#ref-g-07)

4. **한국 정책 — 금융·통신·수사기관 간 정보공유 범위를 명확화하는 시행령 개정 추진.**
   정책브리핑은 2026-04-02 개정안이 의심거래 탐지 정보공유 범위와 분석기관 지정 절차를 정비하고, "선제적 탐지·차단" 법적 근거를 강화한다고 설명했다. 이는 통신사 단독 탐지에서 연합 탐지 구조로의 이동을 뜻한다. [[E-05]](#ref-e-05)

5. **Cofense — AI 피싱이 여전히 대량화되고 있음을 재확인.**
   Cofense는 2025년 AI-powered phishing이 19초당 1건 수준으로 관측됐다고 밝혔다. Microsoft의 정밀도 개선 경고와 합치면, 공격은 동시에 "더 자주" 그리고 "더 잘" 이뤄지고 있다는 의미다. [[G-09]](#ref-g-09)

#### 플레이어 동향

| 기업 | 동향 | 출처 |
|------|------|------|
| Microsoft | 4/2 AI 위협 보고서, 4/6 device code phishing 심층 분석 발표 | [[G-06]](#ref-g-06), [[G-07]](#ref-g-07) |
| EvilTokens | Device Code Phishing을 PhaaS 형태로 확산 | [[G-08]](#ref-g-08) |
| 한국 금융위원회·관계부처 | 보이스피싱 정보공유·선제 차단 강화를 위한 시행령 개정안 입법예고 | [[E-05]](#ref-e-05) |
| SKT | ScamVanguard AI 기반 스팸·보이스피싱 차단 실적을 가장 강하게 공개한 국내 통신사 | [[G-10]](#ref-g-10) |
| KT | 후후(HuHu) 실시간 AI voice phishing detection을 상용 서비스로 제시 | [[G-11]](#ref-g-11) |

#### 시장 시그널

**공격 고도화**
- AI는 피싱의 양적 확대뿐 아니라 인증 흐름 악용 자동화까지 포함하는 공격 운영 체계로 진화했다. [[G-06]](#ref-g-06), [[G-07]](#ref-g-07)

**정책 대응**
- 한국의 제도 변화는 통신사·금융사·수사기관 간 실시간 연계 탐지 수요를 키운다. [[E-05]](#ref-e-05)

#### 시장 수요 (voice-of-market)

**고객 페인포인트**
- MFA가 있어도 OAuth·device code flow를 악용하면 방어가 무너질 수 있다.
- 통화전 탐지는 음성 자체만이 아니라 계정 탈취, 세션 토큰, 메시지 유입 채널과 함께 봐야 한다.

**도입 장벽**
- 탐지 모델이 한 채널만 보면 AI 기반 다단계 피싱을 놓치기 쉽다.
- 통신·금융 간 데이터 공유가 없으면 조기 차단 체계가 느리다.

**시장 니즈**
- 토큰 기반 피싱 방어, 위험 세션 단축, 실시간 교차 채널 인텔리전스가 핵심 수요다.
- 통신사 측에는 네트워크 레이어와 컨택센터 레이어를 연결하는 방어 운영 체계가 필요하다.

#### 전략적 시사점

**기회**
- 통신사와 보안 벤더는 device code phishing을 포함한 cross-channel fraud defense를 신규 제품군으로 묶을 수 있다.
- 한국의 정보공유 제도화는 연합 탐지 API와 데이터 허브 구축을 촉진할 가능성이 크다.

**위협**
- 피싱의 성공 지표가 클릭률 개선과 인증 흐름 악용 자동화로 이동하면서, 기존 MFA 홍보만으로는 보안 우위를 설명하기 어려워졌다.
- 공격자는 합법적 Microsoft 인증 흐름과 고신뢰 cloud redirect 인프라를 동시에 악용하고 있어 단순 blocklist 방식의 방어 효율이 낮다.

---

## 경쟁사 동향 (SKT / KT)

> 이번 주기(2026-04-01~2026-04-09) 기준 공개 자료상 신규 대형 발표는 제한적이었다. 아래는 현재까지 유지되는 가장 최근 공개 포지셔닝이다.

### SKT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| ScamVanguard AI | 2025년 보이스피싱 2.5억건, 스팸 문자 8.5억건 등 차단 실적 공개 | spam-phishing-detection | [[G-10]](#ref-g-10) |
| Thales 5G PQC | 5G SIM용 PQC 협력 레퍼런스를 여전히 보유 | pqc-voice-encryption | [[G-12]](#ref-g-12) |

### KT

| 항목 | 내용 | 관련 L3 | 출처 |
|------|------|---------|------|
| 후후(HuHu) AI | 실시간 AI voice phishing detection 서비스 상용화 포지셔닝 유지 | spam-phishing-detection | [[G-11]](#ref-g-11) |

### 시사점
- SKT는 차단 실적 공개에서, KT는 서비스 제품화 메시지에서 강점을 보인다.
- 이번 주기 기준 PQC와 FHE에서 국내 통신사 신규 공개 업데이트는 제한적이어서, LG U+와 CryptoLab의 레퍼런스가 상대적으로 더 눈에 띈다. [[G-04]](#ref-g-04)

---

## 규제 & 거버넌스

> 해당 도메인에 영향을 미치는 국내외 규제·표준·가이드라인 동향.

### 시행 임박 / 카운트다운

| 규제 / 로드맵 | 기준일 | 상태 |
|---------------|--------|------|
| 캐나다 부처별 초기 PQC migration plan 수립 | 2026-04 | 진행 중 |
| 캐나다 PQC migration progress annual reporting 시작 | 2026-04 이후 매년 | 진행 중 |
| 한국 보이스피싱 시행령 개정안 의견수렴 종료 | 2026-05-12 | D-33 |
| 캐나다 고우선순위 시스템 PQC 완료 | 2031-12-31 | 장기 카운트다운 |
| 캐나다 잔여 시스템 PQC 완료 | 2035-12-31 | 장기 카운트다운 |

### 신규 발의 & 가이드라인

- **캐나다 Cyber Centre ITSM.40.001**: 부처별 계획 수립, 연례 보고, 2031/2035 완료 일정 제시. PQC를 실행 로드맵 단계로 격상. [[E-02]](#ref-e-02)
- **NIST HQC 선정**: ML-KEM 외 코드 기반 백업 축을 공식 포트폴리오에 추가. [[E-03]](#ref-e-03)
- **한국 보이스피싱 대응 시행령 개정안**: 금융·통신·수사기관 간 정보공유와 선제 차단 법적 기반을 강화. [[E-05]](#ref-e-05)

### 시사점
- Secure AI 관점에서 규제의 핵심은 "새로운 의무"보다 "조직별 계획·보고·정보공유 체계"를 만들게 한다는 점이다.
- PQC는 조달과 운영 표준으로, AI 사기 대응은 데이터 공유와 연합 탐지로 제도화되는 흐름이 뚜렷하다.

---

## 종합 시사점 및 후속 조치

### 기술 간 교차 시사점

1. **PQC는 위협 추정보다 마이그레이션 준비도가 더 중요한 국면에 들어섰다.** Aaronson·Nature·Schneier 조합은 서로 다른 층위에서 같은 결론을 강화한다. 지금 필요한 것은 Q-Day 예측 경쟁보다 crypto-agility 설계와 자산 인벤토리 정리다.

2. **FHE는 이제 검증 가능성이 경쟁력이다.** 제품 발표는 늘고 있지만, secure vector search와 encrypted AI workload에서 실제 구매를 당기는 것은 독립 벤치마크와 reference deployment다.

3. **AI 피싱은 음성·이메일·OAuth가 하나의 자동화 체인으로 합쳐지고 있다.** 통신사·보안 벤더는 voice phishing만 따로 떼어 보는 모델에서 벗어나 세션·토큰·메시지·통화를 함께 보는 운영 체계로 가야 한다.

### 후속 조치 제안

- 🟡 PQC: 통신·보안 인프라의 crypto-agility 현황과 공개키 사용 지점을 먼저 인벤토리화하고, Canada형 단계 계획 포맷으로 내부 로드맵을 작성할 것
- 🟡 동형암호: CryptoLab·Niobium 관련 벤치마크와 실제 고객 사례 공개 여부를 계속 추적하고, secure vector search PoC의 삽입·삭제·운영 비용까지 검증할 것
- 🟡 스팸/피싱: Device Code Phishing 대응 관점에서 토큰 수명, 세션 정책, 컨택센터·이메일 보안 연동 시나리오를 별도 점검할 것

## References

| # | 출처 | URL | 유형 | 날짜 | 신뢰도 |
|---|------|-----|------|------|--------|
| <a id="ref-g-01"></a>G-01 | Scott Aaronson — Quantum computing bombshells that are not April Fools | [링크](https://scottaaronson.blog/?p=9665) | blog | 2026-04-01 | [A] |
| <a id="ref-g-02"></a>G-02 | Nature — It's a real shock: quantum-computing breakthroughs pose imminent risks to cybersecurity | [링크](https://www.nature.com/articles/d41586-026-01054-1) | news | 2026-04-06 | [A] |
| <a id="ref-g-03"></a>G-03 | Schneier on Security — Google Wants to Transition to Post-Quantum Cryptography by 2029 | [링크](https://www.schneier.com/blog/archives/2026/04/google-wants-to-transition-to-post-quantum-cryptography-by-2029.html) | blog | 2026-04-06 | [A] |
| <a id="ref-g-04"></a>G-04 | Seoul Economic Daily — Gartner-Recognized Encryption Firm CryptoLab Pushes to Commercialize Korea's Homomorphic Tech | [링크](https://en.sedaily.com/news/2026/04/04/gartner-recognized-encryption-startup-seeks-to) | news | 2026-04-06 | [B] |
| <a id="ref-g-05"></a>G-05 | Zubnet.ai — Niobium's Fog Promises Fully Encrypted AI, But Details Are Thin | [링크](https://zubnet.ai/news/niobiums-fog-promises-fully-encrypted-ai-details-thin/) | blog | 2026-04 | [C] |
| <a id="ref-g-06"></a>G-06 | Microsoft Security Blog — Threat actor abuse of AI accelerates from tool to cyberattack surface | [링크](https://www.microsoft.com/en-us/security/blog/2026/04/02/threat-actor-abuse-of-ai-accelerates-from-tool-to-cyberattack-surface/) | news | 2026-04-02 | [A] |
| <a id="ref-g-07"></a>G-07 | Microsoft Security Blog — Inside an AI-enabled device code phishing campaign | [링크](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/) | news | 2026-04-06 | [A] |
| <a id="ref-g-08"></a>G-08 | Help Net Security — EvilTokens ramps up device code phishing targeting Microsoft 365 users | [링크](https://www.helpnetsecurity.com/2026/03/31/eviltokens-phishing-microsoft-365/) | news | 2026-03-31 | [B] |
| <a id="ref-g-09"></a>G-09 | Cofense — Cofense Report Reveals AI-Powered Phishing Accelerated to One Attack Every 19 Seconds | [링크](https://cofense.com/Blog/Cofense-Report-Reveals-AI-Powered-Phishing-Accelerated-to-One-Attack-Every-19-Seconds) | 보고서 | 2026-02 | [A] |
| <a id="ref-g-10"></a>G-10 | Telecompaper — SKT reveals rise in AI-driven blocking of spam and voice phishing attempts | [링크](https://www.telecompaper.com/news/skt-reveals-rise-in-ai-driven-blocking-of-spam-and-voice-phishing-attempts--1558993) | news | 2026-01-13 | [B] |
| <a id="ref-g-11"></a>G-11 | The Fast Mode — KT unveils real-time AI voice phishing protection | [링크](https://www.thefastmode.com/technology-solutions/39153-kt-unveils-real-time-ai-voice-phishing-protection) | news | 2026 | [B] |
| <a id="ref-g-12"></a>G-12 | SK Telecom Newsroom — SK Telecom and Thales Collaborate on Post-Quantum Cryptography | [링크](https://news.sktelecom.com/en/628) | news | 2023-02 | [B] |
| <a id="ref-p-01"></a>P-01 | Zhao — Hermes: Bridging Relational and Algebraic Abstractions in Homomorphically Encrypted Databases (arXiv:2506.03308) | [링크](https://arxiv.org/abs/2506.03308) | paper | 2026-03-16 | [A] |
| <a id="ref-p-02"></a>P-02 | Aikata et al. — Privacy at your Fingertips: Enabling Rapid Client-Side Operations in Fully Homomorphic Encryption (IACR ePrint 2026/515) | [링크](https://eprint.iacr.org/2026/515) | paper | 2026-03-13 | [A] |
| <a id="ref-e-01"></a>E-01 | Google Research Blog — Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly | [링크](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) | IR/발표 | 2026-03-31 | [A] |
| <a id="ref-e-02"></a>E-02 | Canadian Centre for Cyber Security — Roadmap for the migration to post-quantum cryptography for the Government of Canada (ITSM.40.001) | [링크](https://www.cyber.gc.ca/en/guidance/roadmap-migration-post-quantum-cryptography-government-canada-itsm40001) | 공식 | 2026-04 | [A] |
| <a id="ref-e-03"></a>E-03 | NIST — NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption | [링크](https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption) | 공식 | 2025-03-11 | [A] |
| <a id="ref-e-04"></a>E-04 | PR Newswire — Niobium Introduces The Fog, a New Encrypted Cloud Platform for Private AI and Data Processing | [링크](https://www.prnewswire.com/news-releases/niobium-introduces-the-fog-a-new-encrypted-cloud-platform-for-private-ai-and-data-processing-302732387.html) | press-release | 2026-04-02 | [A] |
| <a id="ref-e-05"></a>E-05 | 정책브리핑 — 보이스피싱 범죄 더 빠르고, 더 강력히 대응합니다 | [링크](https://www.korea.kr/news/policyNewsView.do?newsId=148962033) | 공식 | 2026-04-02 | [A] |
