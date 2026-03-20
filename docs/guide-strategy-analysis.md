# WTIS 2-Tier 가이드

> 기술 의사결정을 위한 2단계 분석 체계.
> Standard로 스크리닝하고, Full로 투자 제안서를 만든다.

---

## 왜 2-Tier인가

기존에는 기술 하나를 검토하려면 3개 스킬을 순서대로 실행해야 했다:

```
/wtis standard → /strategy-options → /biz-case → /report-pdf
  (15분)            (7분)              (8분)        (2분)
= 4단계, 32분, 4개 파일
```

문제:
- CTO가 하나의 기술을 판단하려면 **4개 파일을 열어야** 한다
- 시장 분석·경쟁 환경이 **3개 리포트에서 중복** 반복
- No-Go 기술에도 전략/재무 분석을 돌릴 위험

해결: **Standard로 먼저 걸러내고, Go 기술만 Full로 종합 제안서를 생성한다.**

---

## Tier 비교

| | Standard | Full |
|---|---|---|
| **핵심 질문** | "이 기술을 추진해야 하는가?" | "이 기술에 어떻게, 얼마를 투자하고, 누구랑 할 것인가?" |
| **용도** | 포트폴리오 스크리닝, Go/No-Go 판정 | CTO 투자 제안서, 경영진 보고 |
| **소요 시간** | ~15분 | ~30분 |
| **선행 조건** | 없음 | Standard Go/Conditional Go |
| **호출** | `/wtis standard {기술명}` | `/wtis full {기술명}` |
| **산출물** | 기술 평가 리포트 (1파일) | 종합 투자 제안서 (1파일) |
| **에이전트** | research-deep 1 + validator | research-deep 4~5 + fact-checker + validator |

---

## Standard 모드 (기존)

기술의 투자 가치를 판정한다. 모든 L2 기술에 대해 수시로 실행.

```
/wtis standard speech-generation
```

### 커버 범위

| 섹션 | 내용 |
|------|------|
| 시장 분석 | TAM/SAM/SOM, 시장 드라이버 |
| 기술 성숙도 | TRL 매트릭스, SMART Test, 벤치마크 |
| 경쟁 환경 | 주요 플레이어, Gap Analysis |
| 전략 권고 | 3B 의사결정 (Buy/Borrow/Build 방향성) |
| 교차검증 | Validator 독립 검증 |

### 산출물
- 200점 채점 + Go/No-Go 판정
- 3B 전략 방향 (수준: 방향성)
- 포트폴리오 자동 갱신

### 판정 기준

| 점수 | 판정 | 다음 단계 |
|------|------|----------|
| 140+ | **Go** | → Full 모드 실행 권고 |
| 100~139 | **Conditional Go** | → Full 모드로 조건 해소 경로 확인 |
| ~99 | **No-Go** | → 보류. Full 불필요 |

---

## Full 모드 (신규)

Go/Conditional Go 기술에 대해 **하나의 종합 투자 제안서**를 생성한다.
Standard가 "추진 가치가 있다"고 판단한 기술만 대상이다.

```
/wtis full speech-generation
```

### 종합 투자 제안서 구조

```markdown
# 기술 투자 제안서: {기술명}

§1. 기술 평가 요약
    - Standard 5차원 점수 + 핵심 강점/약점
    - 시장 규모 (TAM/SAM/SOM)
    - 경쟁 포지션 요약

§2. 전략 옵션 비교
    - Build / Buy / Partner 3옵션 정량 매트릭스 (5기준 × 20점)
    - 옵션별 핵심 근거 (1~2줄)
    - 권고 옵션 + Hybrid 전략

§3. 후보 기업 분석
    - 권고 옵션에 따른 기업 테이블
      - Partner → 파트너 후보 (협업 모델, 기대 효과)
      - Buy → 인수 후보 (밸류에이션, 적합도)
      - Build → 벤치마크 기업 (기술 수준 비교)
    - deal_stage 연동 (startup-db에 등록된 경우 현재 단계 표시)
    - 유사 딜/파트너십 사례

§4. 투자 케이스
    - 비용 구조 (Y1~Y5, 전략 옵션에 맞춤)
    - 3시나리오 매출 전망 (낙관/기본/비관)
    - ROI + 회수 기간 + 민감도 분석
    - Go/No-Go 투자 권고

§5. 실행 로드맵
    - Q 단위 마일스톤
    - 후속 조건 체크리스트 (Conditional Go 연계)
    - 담당 조직 배정

References
```

### 내부 프로세스

```
Standard 리포트 읽기
    │
    ├── research-deep (Build 리서치)  ─┐
    ├── research-deep (Buy 리서치)    ─┼── 최대 3개 병렬
    ├── research-deep (Partner 리서치) ─┘
    │
    ├── research-deep (시장·비용 리서치) ── 1개 추가
    │
    ▼
스코어링 + 종합 리포트 작성
    │
    ▼
fact-checker (핵심 주장 팩트 체크 — Devil's Advocate)
    │
    ▼
validator 교차검증 (내부 일관성)
    │
    ▼
종합 투자 제안서 저장 + 포트폴리오 갱신
```

> Full 모드는 내부적으로 strategy-options + biz-case의 로직을 통합 실행한다.
> 별도 스킬(`/strategy-options`, `/biz-case`)은 독립 실행 옵션으로 유지한다.

---

## 의사결정 플로우

```
                        기술 후보 발생
                    (weekly-monitor 🔴, 과제 제안서, 탐색)
                             │
                             ▼
                    ┌─────────────────┐
                    │  /wtis standard  │  ~15분
                    │  200점 채점       │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
          No-Go          Conditional      Go
          (~99)          (100~139)        (140+)
              │              │              │
              ▼              │              │
           보류/재검토         │              │
                             ▼              ▼
                    ┌─────────────────┐
                    │   /wtis full    │  ~30분
                    │  종합 투자 제안서 │
                    └────────┬────────┘
                             │
                    ┌────────┼────────┐
                    ▼        ▼        ▼
              ┌──────────┐ ┌────────┐ ┌──────────────┐
              │report-pdf│ │ slides │ │obsidian-bridge│
              │  PDF     │ │ PPTX   │ │  Obsidian    │
              └──────────┘ └────────┘ └──────────────┘
                             │
                             ▼
                      CTO 보고 패키지
```

### 언제 Standard만으로 충분한가

- **포트폴리오 스크리닝**: 다수 기술을 빠르게 Go/No-Go 분류
- **weekly-monitor 후속**: 긴급 시그널에 대한 빠른 판정
- **과제 제안서 검증**: 접수된 제안서의 타당성 빠른 확인

### 언제 Full이 필요한가

- **CTO 보고**: "이 기술에 투자합시다" → 전략+재무+업체가 한 문서에 필요
- **투자 심의**: 경영진에게 투자 승인 요청
- **파트너 협상 전**: 후보 기업 분석과 비용 구조가 사전 필요

---

## 산출물 구조

```
outputs/reports/{domain}/{date}_{slug}/
  ├── {date}_wtis-{slug}.md             ← Standard 평가
  ├── {date}_wtis-{slug}.pdf
  ├── {date}_wtis-full-{slug}.md        ← Full 종합 투자 제안서
  ├── {date}_wtis-full-{slug}.pdf
  ├── {date}_strategy-options-{slug}.md ← (독립 실행 시에만)
  └── {date}_biz-case-{slug}.md         ← (독립 실행 시에만)

outputs/reports/{domain}/
  └── {domain}-portfolio.md             ← 포트폴리오 (자동 갱신)
```

---

## 독립 스킬 (개별 실행도 가능)

Full 모드가 내부적으로 통합하는 로직은 개별 스킬로도 실행 가능하다:

| 스킬 | 용도 | 언제 단독 실행하나 |
|------|------|-----------------|
| `/strategy-options` | Build/Buy/Partner 비교 | 전략 옵션만 깊이 검토할 때 |
| `/biz-case` | ROI·시나리오 분석 | 재무 모델만 별도로 갱신할 때 |
| `/startup-scout` | 스타트업 후보 발굴 | 전략 옵션과 무관하게 기업 탐색 |
| `/startup-analyst` | 특정 기업 심층 분석 | 후보 기업 개별 평가 |

---

## CTO 보고 패키지

| Tier | 보고 자료 | 형식 |
|------|----------|------|
| **Standard** | 기술 평가 리포트 | PDF (1건) |
| **Full** | 종합 투자 제안서 (기술+전략+기업+재무) | PDF (1건) |
| (선택) | 발표 자료 | PPTX |
| (참고) | 포트폴리오 현황 | MD/PDF |

```
# 실행 예시: 전체 흐름
/wtis standard speech-generation       ← Conditional Go (128/200)
/wtis full speech-generation           ← 종합 투자 제안서 생성
/report-pdf {full 리포트 경로}          ← PDF 변환
/slides {full 리포트 경로}              ← CTO 발표용 PPTX
/obsidian-bridge {세션폴더} wtis        ← Obsidian 동기화
```

---

## 주의사항

- **Standard No-Go 판정은 Full 대상이 아님** — Full 모드가 자동으로 거부
- **Full은 Standard 선행 필수** — Standard 리포트가 없으면 자동으로 Standard 먼저 실행
- **모든 재무 수치에 출처 또는 `[추정]` 태그** — 근거 없는 숫자는 신뢰도 저하
- **통신사 맥락 반영** — LG U+ 관점 (네트워크 자산, 가입자 기반, 규제 환경)
- **research-deep 최대 3~4개 병렬** — 리소스 경합 방지 (Full 모드는 2배치로 분할)
