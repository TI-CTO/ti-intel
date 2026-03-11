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
| reference  | `docs/guide-*.md`                                       | `10-Reference/`                                  |
| goal       | (Obsidian-only)                                         | `20-Goals/`                                      |
| wtis       | `outputs/reports/{domain}/{date}_{slug}/`               | `30-Reports/{domain}/{date}_{slug}/`             |
| portfolio  | `outputs/reports/{domain}/portfolio.*`                   | `30-Reports/{domain}/`                           |
| weekly     | `outputs/reports/weekly/{date}_weekly-{domain}.*`       | `30-Reports/weekly/`                             |
| research   | `outputs/reports/weekly/{date}_research-*.md`            | `30-Reports/weekly/`                             |
| devlog     | manual                                                  | `40-DevLog/`                                     |

**볼트 루트**: `/Users/ctoti/Obsidian/Obsidian_Work/`

## 타입별 동기화 규칙

### wtis (WTIS 분석 세션)
- **단위**: 세션 폴더 전체 (`{date}_{slug}/`)
- **복사 대상**: `final.md` + `final.*.pdf` (intermediate 파일 제외)
- **대상 구조**: `30-Reports/{domain}/{date}_{slug}/final.md` + PDF
- **도메인 폴더** 자동 생성 (secure-ai, agentic-ai 등)

### portfolio (도메인 포트폴리오)
- **파일**: `portfolio.md` + `portfolio.*.pdf`
- **대상**: `30-Reports/{domain}/portfolio.md` + PDF
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
- **파일**: `docs/guide-*.md`
- **대상**: `10-Reference/` (한글 파일명으로 변환)

## Process

1. **소스 파일 읽기**: 첫 번째 인자의 파일 또는 폴더를 Read로 읽는다

2. **타입 자동 감지** (두 번째 인자 생략 시):
   - 경로에 `outputs/reports/{domain}/{date}_{slug}/` 패턴 → `wtis`
   - 파일명 `portfolio.*` → `portfolio`
   - 파일명 `*_weekly-*` → `weekly`
   - 파일명 `*_research-*` → `research`
   - 그 외 → 수동 지정 필요

3. **기존 frontmatter 확인**: YAML frontmatter가 있으면 보존, 없으면 새로 생성

4. **Obsidian 형식으로 변환:**
   - 타입별 태그 추가: `tags: [claude-code, {type}]`
   - `created` 날짜 추가 (파일 날짜 접두사 또는 오늘)
   - `updated` 날짜 추가 (오늘)

5. **파일 복사:**
   - wtis: 세션 폴더 내 `final.md` + `final.*.pdf`만 복사
   - portfolio: `portfolio.md` + `portfolio.*.pdf` 복사
   - weekly/research: 단일 파일 + 동반 PDF 복사
   - **PPTX는 복사하지 않음** (Obsidian 미지원)

6. **결과 보고:**
   - 생성된 파일의 전체 경로
   - 복사된 파일 수
