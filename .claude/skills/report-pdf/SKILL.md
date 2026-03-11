# report-pdf Skill

WTIS 리포트 또는 마크다운 파일을 컨설팅 스타일 PDF로 변환한다.

## I/O Contract

### Input
| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `markdown_path` | yes | 파일 경로 | 변환할 마크다운 파일 절대 경로 |
| `theme` | no | `professional` \| `minimal` \| `dark` | 디자인 테마 (기본: professional) |
| `output_path` | no | 파일 경로 | 출력 PDF 경로 (기본: 소스와 같은 디렉토리) |

### Output Files
| Artifact | Path Pattern | Description |
|----------|-------------|-------------|
| PDF | `{source_dir}/{name}.{theme}.pdf` | 변환된 PDF |

### Return
```yaml
status: pass | fail
file_path: "PDF 절대 경로"
theme: "적용된 테마"
```

## 실행

`design-system` MCP의 `render_pdf` 도구를 호출한다:

```
render_pdf(
  markdown_path = "<절대경로>",
  theme = "professional",          # 기본값
  output_path = "<출력경로>.pdf"  # 생략 시 소스와 같은 디렉토리
)
```

## 디자인 스펙

- **색상**: 프라이머리 `#C50063` (섹션 타이틀, 테이블 헤더, 액센트)
- **헤더**: 다크 네이비 `#1E3A5F` 배경 + 흰색 제목
- **레이아웃**: Design 1(Executive Summary 박스, 메타 카드) + Design 2(점선 구분자, 2단 테이블)
- **푸터**: 다크 네이비 바 — 신뢰도/분석 기관/시스템/분석일 표시
- **용지**: A4, 인쇄 최적화

## WTIS 마크다운 매핑

| frontmatter 키 | PDF 위치 |
|----------------|---------|
| `topic` | 헤더 제목 |
| `date` | 헤더 메타 + 메타 카드 + 푸터 |
| `confidence` | 헤더 메타 + 메타 카드 + 푸터 (색상 구분) |
| `status` | 메타 카드 |
| `sources_used` | 헤더 출처 건수 |

| 본문 섹션 | HTML 컴포넌트 |
|-----------|--------------|
| `## Executive Summary` | Executive Summary callout box |
| `## N. 섹션명` | 번호 배지 + 프라이머리 섹션 타이틀 |
| `\|테이블\|` | 프라이머리 헤더 data-table |
| `[G-xx]` 인라인 인용 | 프라이머리 뱃지 |
| `## References` | 새 페이지 + 참조 테이블 |

## 출력 위치

- 기본: 소스 `.md` 파일과 같은 디렉토리, `.professional.pdf` 확장자
- 예: `outputs/reports/2026-02-25_research-secure-ai.professional.pdf`

## 사용 예시

```
/report-pdf outputs/reports/2026-02-25_research-secure-ai.md
```

**완료 시:**
```
PDF 생성 완료
파일: outputs/reports/2026-02-25_research-secure-ai.professional.pdf
테마: professional  용지: A4
```

또는 WTIS 완료 후 자동 후속 작업으로:

```
render_pdf(
  markdown_path = "/Users/ctoti/Project/ClaudeCode/outputs/reports/2026-02-25_research-secure-ai.md"
)
```

## Next Steps

PDF 생성 완료 후 아래 후속 옵션을 사용자에게 제시한다:

```
📋 Next Steps:
  📊 프레젠테이션 필요 시:
    → /slides {원본 마크다운 경로}                  — PPTX 슬라이드 변환
  📂 Obsidian 동기화:
    → /obsidian-bridge {파일 경로} {type}           — PDF 포함 볼트에 동기화
```
