---
name: obsidian-bridge
description: "워크스페이스의 산출물을 Obsidian 볼트로 동기화한다. frontmatter를 추가하고 볼트에 복사한다."
user-invokable: true
argument-hint: "[file-path-or-folder] [type: wtis|weekly|research|reference|devlog]"
---

# Obsidian Bridge

워크스페이스 파일을 Obsidian 볼트에 동기화한다.

## 빠른 시작

```
/obsidian-bridge outputs/reports/agentic-ai/2026-03-09_multi-agent wtis
/obsidian-bridge outputs/reports/weekly/2026-03-09_weekly-agentic-ai.md weekly
/obsidian-bridge outputs/reports/weekly/2026-03-09_research-adaptive-rag.md research
```

---

## Arguments
- 첫 번째 인자: 소스 파일 또는 폴더 경로
- 두 번째 인자: 노트 타입 (destination 결정)

## I/O Contract

### Input
| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `source` | yes | 파일/폴더 경로 | 동기화할 소스 경로 |
| `type` | auto-detect | `wtis` \| `portfolio` \| `weekly` \| `research` \| `reference` \| `devlog` | 노트 타입 (미지정 시 경로 패턴으로 자동 감지) |

### Output
| Artifact | Description |
|----------|-------------|
| Obsidian 파일 | 볼트 대상 경로에 frontmatter 추가된 파일 복사 |

### Return
```yaml
status: pass | fail
files_copied: ["복사된 파일 절대 경로 목록"]
vault_paths: ["Obsidian 볼트 내 경로 목록"]
```

## Destination Mapping

| Type       | Git Source                                              | Obsidian Vault Path                              |
|------------|---------------------------------------------------------|--------------------------------------------------|
| reference  | `docs/guide-*.md`, `docs/spec-*.md`                     | `10-지식베이스/{subfolder}/`                      |
| goal       | (Obsidian-only)                                         | `20-Goals/`                                      |
| wtis       | `outputs/reports/{domain}/{date}_{slug}/`               | `30-Reports/{domain}/{date}_{slug}/`             |
| portfolio  | `outputs/reports/{domain}/{domain}-portfolio.*`          | `30-Reports/{domain}/`                           |
| weekly     | `outputs/reports/weekly/{date}_weekly-{domain}.*`       | `30-Reports/weekly/`                             |
| research   | `outputs/reports/weekly/{date}_research-*.md`            | `30-Reports/weekly/`                             |
| devlog     | manual                                                  | `40-DevLog/`                                     |

**볼트 루트**: `/Users/ctoti/Obsidian/Obsidian_Work/`

## 타입별 동기화 규칙

### wtis (WTIS 분석 세션)
- **단위**: 세션 폴더 전체 (`{date}_{slug}/`)
- **복사 대상**: `{date}_wtis-{slug}.md` + `{date}_wtis-{slug}.*.pdf` (intermediate 파일 제외)
- **대상 구조**: `30-Reports/{domain}/{date}_{slug}/{date}_wtis-{slug}.md` + PDF
- **도메인 폴더** 자동 생성 (secure-ai, agentic-ai 등)

### portfolio (도메인 포트폴리오)
- **파일**: `{domain}-portfolio.md` + `{domain}-portfolio.pdf`
- **대상**: `30-Reports/{domain}/{domain}-portfolio.md` + PDF
- wtis 스킬이 portfolio 갱신 시 자동 동기화 대상

### weekly (주간 모니터링 메인 리포트)
- **파일**: `{date}_weekly-{domain}.md` + `.pdf`
- **대상**: `30-Reports/weekly/` (flat)
- 파일명 패턴: `YYYY-MM-DD_weekly-{domain}.*`

### research (Tier 2 심층 리서치)
- **파일**: `{date}_research-{topic}.md`
- **대상**: `30-Reports/weekly/` (weekly와 같은 폴더, flat)
- 파일명 패턴: `YYYY-MM-DD_research-{topic}.md`
- PDF 없음 (마크다운만)

### reference
- **파일**: `docs/guide-*.md`, `docs/spec-*.md`
- **대상**: `10-지식베이스/{subfolder}/` (한글 파일명으로 변환)
- **서브폴더 매핑**:

| docs/ 파일명 | Obsidian 서브폴더 | Obsidian 파일명 |
|---|---|---|
| `guide-team-quickstart.md` | `시작하기/` | `01-팀-퀵스타트.md` |
| `guide-platform-overview.md` | `시작하기/` | `05-시스템-개요.md` |
| `guide-strategy-analysis.md` | `워크플로우/` | `01-WTIS-2Tier-가이드.md` |
| `guide-skill-chaining.md` | `워크플로우/` | `10-스킬-체이닝-맵.md` |
| `guide-startup-dashboard.md` | `워크플로우/` | `15-대시보드-개요.md` |
| `tech-taxonomy-overview.md` | `레퍼런스/` | `01-기술-분류체계.md` |
| `guide-tool-reference.md` | `레퍼런스/` | `10-도구-레퍼런스.md` |
| `spec-dashboard-ui.md` | `레퍼런스/` | `15-대시보드-UI스펙.md` |
| `guide-final-review-demo.md` | `레퍼런스/` | `20-최종리뷰-데모.md` |

## Process

1. **소스 파일 읽기**: 첫 번째 인자의 파일 또는 폴더를 Read로 읽는다

2. **타입 자동 감지** (두 번째 인자 생략 시):
   - 경로에 `outputs/reports/{domain}/{l2_slug}/` 패턴 → `wtis`
   - 파일명 `*-portfolio.*` → `portfolio`
   - 파일명 `*_weekly-*` → `weekly`
   - 파일명 `*_research-*` → `research`
   - 그 외 → 수동 지정 필요

3. **기존 frontmatter 확인**: YAML frontmatter가 있으면 보존, 없으면 새로 생성

4. **Obsidian 형식으로 변환:**
   - 타입별 태그 추가: `tags: [claude-code, {type}]`
   - `created` 날짜 추가 (파일 날짜 접두사 또는 오늘)
   - `updated` 날짜 추가 (오늘)

5. **파일 복사:**
   - wtis: 세션 폴더 내 `{date}_wtis-{slug}.md` + `{date}_wtis-{slug}.*.pdf`만 복사
   - portfolio: `{domain}-portfolio.md` + `{domain}-portfolio.pdf` 복사
   - weekly/research: 단일 파일 + 동반 PDF 복사
   - **PPTX는 복사하지 않음** (Obsidian 미지원)

6. **결과 보고:**
   - 생성된 파일의 전체 경로
   - 복사된 파일 수

## 동기화 영향 범위 체크리스트

**모든 동기화 실행 시** 아래 범위를 확인한다. 특히 폴더명·파일명 변경 시 필수.

| # | 점검 대상 | git 경로 | Obsidian 경로 | 확인 사항 |
|---|----------|---------|-------------|----------|
| 1 | 지식베이스 문서 | `docs/` | `10-지식베이스/` | 매핑 테이블 파일명 일치 + 본문 동기화 |
| 2 | WTIS 리포트 | `outputs/reports/{domain}/{l2_slug}/` | `30-Reports/{domain}/` | 폴더명 + 파일명 정합성 |
| 3 | 주간 리포트 | `outputs/reports/weekly/` | `30-Reports/weekly/` | 파일명 정합성 |
| 4 | 포트폴리오 | `outputs/reports/{domain}/{domain}-portfolio.md` | `30-Reports/{domain}/` | 세션 링크(wikilink) 경로 |
| 5 | 스팟 리서치 | `outputs/reports/spot/` | `30-Reports/spot/` | 파일 복사 여부 |
| 6 | 스타트업 노트 | startup-db MCP | `50-Startups/` | company slug 일치 |
| 7 | 업무일지 | (직접 작성) | `40-DevLog/` | 산출물 링크 경로 |

### 폴더 구조 변경 시 추가 점검

폴더명·파일명 규칙이 바뀔 때는 위 6개 + 아래를 반드시 확인:

- [ ] git 내부 참조: portfolio wikilink, SKILL.md 경로 패턴, prior_report 경로
- [ ] Obsidian 볼트 내 wikilink: `30-Reports/` 아래 기존 복사본의 링크
- [ ] MEMORY.md 경로 참조
- [ ] 전체 개요(`00-전체-개요.md`) 산출물 구조 설명
