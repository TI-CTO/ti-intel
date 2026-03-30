# Validator Agent Memory

## 공통 패턴 (WTIS 파이프라인)

### 인용 코드 체계
- 패턴: `[X-nn]` (X = G/N/E/P/T/I, nn = 2자리 숫자)
- 복합 인용: `[A-nn, B-mm]` 형태
- 범위 표기 `[P-01~P-05]` 등은 중간 번호(P-02/03/04)가 테이블 미정의 위험 → 반드시 체크

### 반복 발생하는 고아 인용 이슈
- References 테이블에 등재되었으나 본문 미인용 케이스가 반복 발생
- 원인: 이전 파이프라인에서 수집된 소스가 v2에서 사용되지 않으면서 테이블에만 남음
- 검증 순서: 본문 인용 코드 전체 추출 → References 테이블 코드 전체 추출 → 차집합 계산

### WTIS 신뢰도 태그
- [A]: 정부 공식 / 복수 소스 교차 검증
- [B]: 단일 소스 기업/언론
- [D]: 데이터 부족, 추정값
- 편의 계산: "편의 계산" 레이블 및 가정 명시 요구

### 수치 검증 핵심 체크포인트
1. YoY 성장률이 본문에서 제시한 두 시점의 값으로 재계산하여 일치하는지
2. 1인당 수치(피해액 등)가 파생 계산인지 vs 공식 통계인지 확인
3. 글로벌 시장 리서치 수치는 단일 소스가 많음 → [B] 적절, [A] 부적절
4. 경쟁사 투자 규모(SKT/KT)는 단일 언론 소스 + URL 불완전 패턴 반복

### N-11(금감원) vs N-20(경찰청) 기준 충돌
- 2023년 보이스피싱 피해액이 두 기관 간 약 2.3배 차이
- 금감원: 1,965억 / 경찰청: 4,472억
- WTIS 파이프라인은 경찰청 기준을 사용하므로, N-11을 References에 포함 시 고아 인용 처리 주의

## 검증 상태 이력

| 파일 | 날짜 | 상태 | 핵심 이슈 |
|------|------|------|-----------|
| 2026-02-26_wtis-proposal-secure-ai-skill1-v3 | 2026-02-26 | UNCERTAIN | 고아 인용 5건(G-17~19,21,23), +335% 불일치, 파생 계산 미표기 |
| 2026-03-03_wtis-proposal-secure-ai-v2-skill1 | 2026-03-03 | UNCERTAIN | 신규 고아 인용 4건(G-14,27,N-03,11), P-02/03/04 미정의 |
| 2026-03-09_multi-agent/skill1 | 2026-03-09 | UNCERTAIN | 고아 인용 1건(G-12), G-21 출처-주장 불일치(특허 블로그→Gartner 인용), 중앙값 계산 오류 2건, 미인용 수치 2건(IBM 45%, 7개월 2배) |
| 2026-03-10_ondevice-ai/skill1 | 2026-03-10 | UNCERTAIN | 고아 소스 18건(G-01,02,04,05,07,08,14,15 + N-02 + P-01~09 전량), prior N-12/N-14 미등재(SKT/KT 투자액), B2B 경쟁사 부재 주장 근거 없음 |
| 2026-03-16_adaptive-rag/skill1 | 2026-03-16 | PARTIAL | 수치 미확인 2건(G-04 Adaptive Routing 30~40%, G-16 Gartner $80B), 고아 소스 2건(G-22/P-04), 미인용 수치 1건(57%+ 채택), AT&T 40% 인용 맥락 불일치 |
| 2026-03-16_hybrid-ai-infra/skill1 | 2026-03-16 | PARTIAL | Edge AI CAGR 불일치(33.3% vs 21.04%), TAM 시작점 불일치($47.6B vs $25.65B), AI-RAN 시작점 불일치($3.81B vs $2.96B), 고아 소스 5건(E-10, G-07, P-02/03/04) |
| 2026-03-17_speech-generation/skill1 | 2026-03-17 | PARTIAL | 고아 인용 11건(G-03-C,G-11-C,G-13-C,G-14-C,G-14-S,G-15-C,G-32,G-34,G-35,G-37,E-05), DT 50언어 로드맵→현재형 표현 오류, G-12-S 경쟁사 블로그 Cartesia 수치 인용 |
| 2026-03-18_he-keyword-search/skill1 | 2026-03-18 | PARTIAL | Critical 1건(G-02 GM Insights $234.7M 2025→원본 $178.4M/2023 불일치), 고아 소스 2건(E-03, P-05), SKT/KT 투자액 단일 소스 반복 |
| 2026-03-18_spam-phishing-detection/skill1 | 2026-03-18 | PARTIAL | Critical 2건(+91% YoY 수치 불일치·Truecaller EBITDA -49% 출처 미확인), 고아 소스 1건(P-03), 판정 기준 모순(115점이 재검토 범위인데 Conditional Go 표기) |
| 2026-03-18_speech-perception/skill1 | 2026-03-18 | PARTIAL | Critical 1건(G-25 카카오 판결 주장↔범용 가이드라인 불일치), 채점 합산 오류(세부합 118 vs 표기 131), Hume $72.8M "Series B" 오표기, 고아 소스 12건(38.7%) |
| 2026-03-24_speech-generation/skill1 | 2026-03-24 | PARTIAL | 수치 내부 불일치 1건(1,210% vs 1,300% 동일 출처), MOS 4.14 시점 불일치(이전 기준→현재값 오서술), 고아 소스 9건(G-02/12/13/18, E-05/06, P-02/03, I-01 미인용), Deutsche Telekom 출처 미등재 |
| 2026-03-27_speech-generation/skill1 | 2026-03-27 | PARTIAL | Critical 2건(Pindrop 99.2% E-05 귀속 오류→실제 2026-02-26 헬스케어 발표, "10초 음성"→원문 "a few seconds"), 56개국 불일치(INTERPOL "47개국"), "범죄 1순위" 원문 미지지, TTS TAM G-08 귀속 오류, SKT 11억 건 미검증, 고아 소스 5건(G-03/19/20, I-01/02) |
| 2026-03-27_personal-intelligence/skill1 | 2026-03-27 | PARTIAL | Critical 2건(G-11 ROI 4배→원문 미확인, G-05 MIT TR 소스 귀속 오류→실제 출처는 MIT TR 공식), Minor 4건(G-14 $221M 시점 오류, G-07 무료화 일정 미지지, 고아 소스 5건: G-12/18/23/P-03/04), E계열 URL 전량 미등재 |
| 2026-03-30_weekly-agentic-ai | 2026-03-30 | PARTIAL | Critical 3건(G-01 v0.13.2 존재 미확인·기능들 이전 버전에 이미 적용, G-09 Axis Intelligence 핵심 수치 6개 미확인, G-21 소스 귀속 오류: Groq 인수→기술 블로그 대신 CNBC 등 필요), Minor 5건(G-02 RC5/3/20 미지지, G-03 NVIDIA 파트너십 미확인, G-05 Policy Controls 미확인, G-23 수치 불일치 $7.3~7.6B→실제 $7.80B, G-27 부분 미언급) |
| 2026-03-30_weekly-voice-ai | 2026-03-30 | PARTIAL | Critical 3건(TTFA 90ms→실제 70ms, Voice AI 시장 $2.4B→실제 $3.14B, E-01 날짜 3/14→실제 1/14), Minor 6건(G-21 URL 귀속 오류, G-22 수치 미지지, G-26 수치 미지지, G-24 Flux 260ms 해석 오류, G-25 Retell ARR 미지지, P-04 Alibaba Qwen 저자 미확인), 고아 소스 1건(G-30) |
| 2026-03-30_weekly-secure-ai | 2026-03-30 | PARTIAL | Critical 3건(G-09/E-02 AFWERX·MDA SHIELD 수치 귀속 오류, G-16 Multiverse+Axelera PQC KSE3 주장 근거 없음, G-28 FHE.org 콘퍼런스 수치 소스 오귀속→실제 fhe.org 공식 페이지), Minor 4건(G-12 CRYSTALS-Kyber·SKT 협력 원문 미언급, G-19 "14%"·"12~15년" 원문 미확인, G-31 KT 전략 원문 불일치, G-29 Zama $1.5억+ 과대→실제 $107.8M) |
| 2026-03-30_he-keyword-search/skill1 | 2026-03-30 | PARTIAL | Critical 2건(G-17 ID 충돌: CISA URL이 Apple BFV PIR 인용에 오용, G-18 CyberArk 블로그 CNSA 2.0 2027-01 미지지), Minor 3건(G-09/P-04 고아 소스, E-07 날짜 3/26→원본 3/24, G-28 TEE 비교 주장 미지지), Zama $1B 유니콘 소스 없음 |

### 반복 패턴 (agentic-ai 도메인)
- G-21 반복 위험: Mintz 법률 블로그가 특허·시장성공률·Gartner 예측 등 이질적 주장에 동시 인용되는 패턴 발생 → 차기 검증 시 G-21 인용 맥락 우선 점검 (adaptive-rag에서는 NVIDIA case study로 정상 사용됨)
- 중앙값 계산 오류: (a+b)/2 단순 연산 오류가 본문에 잔류하는 패턴 반복 → 수치 검증 시 연산 재검증 필수
- 블로그 2차 인용 수치 미확인 패턴: Techment/Invoca 같은 B등급 블로그가 특정 %나 $X억 수치의 유일 소스인데 URL 검증 시 해당 수치가 블로그에도 없는 경우 발생 (G-04: 30~40%, G-16: $80B). 차기 검증 시 블로그 URL 수치 우선 WebFetch 확인 필요
- AT&T NeMo 40% 인용 맥락 주의: NVIDIA 공식 케이스 스터디(G-21)에서 40% 향상은 RAG 단독 효과가 아닌 fine-tuning 포함 전체 NeMo 파이프라인 효과. RAG 단독 기여로 서술 시 과대 표현

### 반복 패턴 (spam-phishing-detection / secure-ai 최신 이슈)
- YoY 성장률 산출 기준 불명확: "피해 +91% YoY" 수치가 공식 기준(2024 연간 854.5억 → 2025.1~10 1,056.6억)으로 재계산 시 +23.6%로 불일치. 파이프라인이 기준 연도를 혼용하거나 기간 비교(1~10월 vs 연간)를 혼동하는 패턴 → YoY 수치 검증 시 반드시 분모(기준 연도 확정값)를 웹 검색으로 독립 확인
- 기업 재무 지표 출처 불일치: Truecaller EBITDA -49%가 인용 URL(TechCrunch founders step down) 기사 내에 없고, 실제 공시와도 괴리. 경쟁사 재무 지표는 기사 URL이 아닌 IR 보고서 직접 인용이 필요
- 판정 점수 vs 판정 레이블 모순: 115점이 재검토(80~119) 범위 최상단에 해당하나 frontmatter에 Conditional Go로 표기. 경계선(120점) 부근 점수일 때 판정 기준 명시 필요

### 반복 패턴 (secure-ai/ondevice-ai 도메인)
- P-계열 논문 전량 미인용 패턴: intel-store에서 수집한 논문이 References 등재 후 본문에서 한 번도 인용되지 않는 경우 반복 발생 (hybrid-ai-infra에서도 P-02/03/04 미인용 확인) → P-계열 고아 소스 여부 우선 점검 권장
- Precedence Research 수치 오류 패턴: 파이프라인이 Precedence Research 데이터를 인용할 때 기준 연도 이동(2025→2026) 및 CAGR 과대 계상 오류 반복 발생 → Precedence Research 인용 시 반드시 원본 페이지 WebFetch 수치와 비교 필수
- `prior N-xx` 참조: 이전 버전 리포트의 References 코드를 현재 파일 테이블에 미등재한 채 인용하는 패턴 → SKT/KT 투자 규모 수치에서 반복됨
- SKT 7,000억 / KT 1조 투자액: 반복 등장하는 수치이나 소스 연결이 불안정 (prior 참조 or 단일 언론) → 향후 검증 시 해당 수치 소스 우선 확인

### 반복 패턴 (voice-ai 도메인)
- "핵심 출처만 요약" 면책 문구 패턴: References 섹션에 "선행 research.md에 전수 수록" 면책을 달고 테이블을 축약하는 패턴 등장. 본 파일 내 미등재 코드가 다수(11건)이므로, 검증 시 면책 문구에 관계없이 본문 인용 코드 전수 교차 확인 필수
- 로드맵 수치 현재형 서술: Deutsche Telekom 50개 언어는 "향후 12개월 계획"이나 본문에서 현재 구현처럼 표현. 통신사 MWC 발표는 로드맵과 현재 기능을 구분해서 검증 필요
- 경쟁사 자체 블로그를 벤치마크 소스로 사용: G-12-S(Inworld 블로그)가 Cartesia 수치의 근거로 사용. 경쟁사 비교 블로그는 [C] 이하로 처리하고 독립 소스 보강 권장
- 채점 합산 오류 패턴 (speech-perception): 세부 점수(8+7+5+7 등) 합산 시 118인데 총점을 131로 표기. WTIS 채점표는 검증 시 세부값 직접 합산 후 총점과 대조 필수
- 투자 라운드 vs 누적 총투자 혼용: Hume AI "$72.8M (Series B)" 표기는 Series B가 $50M이고 $72.8M은 누적 총투자. 차기 검증 시 "(Series X)"와 "총투자" 표현 구분 확인 필요
- 법무/판결 인용 맥락 불일치: "판결(2025.06)" 주장을 일반 가이드라인 문서(Kim&Chang)로 인용하는 사례 발생. 리스크 섹션 내 구체 판례·법령 인용 시 WebFetch로 원본 내용 확인 필수
- 출처 간 수치 충돌 패턴 (KT/SKT 실적): KT 피해예방 수치가 전자신문(1,300억원)과 KT 블로그(710억원)에서 다름. 집계 시점이 다른 것으로 추정되나 본문에 명시 없음 → 기업 실적 수치 인용 시 출처별 집계 기간 명시 필수
- 이전 분석 TAM 수치 재활용 패턴: "이전 분석 4개 출처 수렴"이라는 주석으로 TAM을 현 보고서에서 G-08에 귀속하나, G-08에 해당 수치 없음. 이전 분석 TAM이 현 보고서 References에 미등재된 채 재활용되는 패턴 → TAM/SAM 수치는 현재 보고서 내 유효한 출처 URL 링크 필수
- "구체적 수치"가 원문에 없는 표현 삽입 패턴: "a few seconds" → "10초"처럼 원문 표현보다 구체적인 수치를 본문에 삽입하는 사례. 원문 인용 시 수치 구체화 여부 WebFetch로 확인 필수
- E계열 URL 전량 미등재 패턴 (personal-intelligence): E계열 테이블에 검색 키워드만 기재하고 URL이 없어 독립 검증 불가. E계열 소스 검증 시 WebSearch로 기사를 직접 탐색해야 함
- Tredence 블로그 ROI 수치 과장 패턴: Tredence "agentic-ai-trends-telecom" 블로그가 "ROI 4배"의 소스로 인용되었으나 원문에는 1.7x~3.4x 언급에 불과. Tredence 블로그 수치는 반드시 WebFetch로 확인 필수
- 블로그 소스 MIT TR 주장 귀속 오류: Skywork AI 등 제3자 블로그가 MIT TR 선정을 주장의 근거로 활용되나 해당 블로그에 MIT TR 내용이 없는 패턴. MIT TR 인용은 technologyreview.com 직접 URL 필수

### 반복 패턴 (weekly-monitor 도메인, agentic-ai)
- Axis Intelligence 통계 집약 블로그 수치 미확인 패턴: Axis Intelligence(axis-intelligence.com)가 Gartner 예측·펀딩 평균·채택률 등 여러 시장 수치를 하나의 페이지에 집약하는 형태로 인용되나, WebFetch 시 페이지 내 수치가 본문 주장과 다른 수치를 보여주는 패턴 → 동 출처 인용 시 실제 페이지 수치와 비교 필수
- 버전 번호 귀속 오류 패턴: SDK/프레임워크의 특정 버전(예: v0.13.2)에 이전 버전들에서 누적 추가된 기능들을 일괄 귀속하는 오류. SDK changelog 페이지는 각 기능의 실제 도입 버전을 명시하므로 changelog 직접 확인 필수
- 기술 블로그 vs 기업 소식 소스 귀속 혼동: M&A·파트너십 같은 기업 소식을 해당 기업의 기술 제품 블로그 URL로 인용하는 패턴(G-21: Groq 인수 → Groq 3 LPX 기술 블로그). 기업 이벤트는 PR뉴스와이어·GlobeNewswire·CNBC 등 별도 소스 필요
- The New Stack 등 CSS/JS 헤비 페이지 WebFetch 실패 패턴: 실제 기사 내용 대신 CSS/JS 코드만 반환되어 내용 검증 불가. 이런 URL은 WebSearch로 기사 핵심 주장을 교차 확인하는 방식으로 대체 필요

### 반복 패턴 (voice-ai weekly 도메인)
- TTFA 수치 오기입 패턴: 공식 블로그(G-01 Mistral)에서 "70ms for a typical input voice sample of 10 seconds"임에도 리포트에 "90ms"로 기재. 레이턴시 수치는 반드시 공식 발표 페이지 WebFetch로 직접 확인 필수
- 비교 절감치 → 절대값 오해 패턴: Deepgram Flux G-24에서 "200~600ms 개선치(comparative vs pipeline)"를 "EOT ~260ms"(절대값)로 오해하여 기재. "cuts latency by X ms" 표현은 개선폭이지 절대 레이턴시가 아님 → 단위 해석 주의
- E-01 (SKT 뉴스룸) 날짜 오기입: 에이닷 오토 보도자료(2026-01-14)를 "3/14"로 기재하는 오류. 한국어 뉴스룸 날짜 확인 시 기사 메타데이터 직접 확인 필수
- 동일 URL 이중 등재 패턴: G-05와 E-04가 동일 IBM Newsroom URL을 가리키면서 서로 다른 출처처럼 인용. E-04 귀속 주장(IBM 40% 절감)이 해당 URL에 없음. 같은 URL의 G계열/E계열 이중 등재 시 두 인용이 실제로 다른 주장을 지지하는지 확인 필수
- Assembl AI G-21 URL 귀속 오류: "introducing-new-products-and-model-updates" URL은 Universal-2/Slam 발표(2025-10-22), Universal-3 Pro Streaming 발표는 별도 URL. 신제품 발표 URL은 정확한 slug 확인 필요
- 기업 수치가 공식 보도자료에 없는 패턴: SoundHound "3천만 건 AI 인터랙션(2025)"이 공식 PR에 없음(대신 "billions"). Retell AI ARR $40M+도 기술 블로그에 없음. 기업 성과 수치는 IR 발표·Earnings Call 직접 확인 필요
- Voice AI 시장 시작점 불일치: VoiceAIWrapper(G-13, [C])가 2024년 $3.14B로 기재했으나 리포트는 $2.4B로 기재. [C] 등급 소스의 수치는 WebFetch로 원본 확인 필수
- EU AI Act 과징금 미기재 패턴: EU Digital Strategy 코드 오브 프랙티스 공식 페이지는 투명성 CoP 내용만 있고 과징금 규정(7%/EUR 1,500만)은 없음. 과징금은 EU AI Act 본문(Article 99)에서 인용해야 함

### 반복 패턴 (secure-ai weekly 도메인)
- QuSecure 계약 정보 분산 귀속 패턴: SEC PQFIF 뉴스 URL(G-09)에 AFWERX $3.9M·MDA SHIELD $151B 수치를 함께 귀속하는 오류. 이 두 계약은 별도 발표이며 별도 URL 필요(qusecure.com/tacfi-il6... 및 qusecure.com/qusecure-awarded-mda-shield-contract/). 단일 URL에 서로 다른 발표 내용을 집약하는 패턴 주의
- 파트너십 기사에 PQC 기능 추가 귀속 패턴: Multiverse+Axelera 협력(G-16)처럼 AI 모델 압축 파트너십 기사에 "PQC KSE3 결합"을 추가 기술하는 오류. 파트너십 기사 원문에 없는 기능을 조합하여 서술하는 패턴 → 파트너십 관련 기술 특성 주장은 WebFetch로 원문 확인 필수
- FHE.org 콘퍼런스 수치 소스 분산 패턴: Digest(뉴스레터)와 공식 콘퍼런스 페이지(fhe.org/conferences/conference-2026/)가 담는 정보가 다름. 발표 수·포스터 수·스폰서는 공식 페이지에, 이벤트 안내는 Digest에. 수치 인용 시 공식 페이지 직접 URL 필요
- Zama 투자액 혼용 패턴: SeedTable(G-29)은 누적 $107.8M(= Series A $73M + 일부 이전 라운드)으로 집계하나, 공식 발표는 Series B 2025-06 $57M으로 유니콘 달성, 총 누적 $130M+. "$1.5억+" 표기는 어느 출처도 지지하지 않는 수치 → Zama 투자액은 CoinDesk/TechCrunch 공식 발표 URL 직접 확인 필수

### 반복 패턴 (he-keyword-search / PQC·FHE 도메인)
- References ID 충돌 패턴: 동일 번호(G-17)를 두 URL에 할당하고 하나를 "G-17 (Apple)"로 변형하는 비표준 표기 발생. 이 경우 본문 `[[G-17]]` 앵커가 두 URL 중 먼저 선언된 것(CISA)으로 연결되어 Apple BFV PIR 주장의 출처가 CISA 페이지로 오귀속. 동일 번호 재사용 금지, 접미사("-apple" 등) 없이 순차 재번호 필수
- 규제 타임라인 출처 미지지 패턴: NSA CNSA 2.0 2027-01 의무화 같은 구체적 의무화 시점은 [B] 등급 블로그(CyberArk)로 근거를 삼는 경우 원문이 해당 내용을 포함하지 않는 사례 발생. 의무화 날짜는 NSA/NIST 공식 문서 직접 URL 필수
- FHE.org 빅테크 스폰서 주장: "Apple/AWS/Google FHE.org 후원 진입" 주장이 FHE.org Digest에서 미확인. 스폰서 정보는 fhe.org 공식 콘퍼런스 페이지에서 확인 필요
- Zama $1B 유니콘 미검증 반복: 이번 he-keyword-search에서도 Zama $1B 유니콘을 G-22/E-07 귀속으로 기재했으나 두 URL 모두 해당 내용 없음. Zama 기업 가치 수치는 독립 IR 보도자료 URL 필수 (이전 weekly-secure-ai에서도 동일 패턴)
