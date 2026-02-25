# references — 리포트 참조 파일

리포트 작성 시 Claude가 직접 읽는 **입력 파일** 보관소.
URL로 접근할 수 없는 파일(사내 자료, 유료 논문, 표준 문서 등)을 저장한다.

## 용도
MCP 서버(research-hub, patent-intel, trend-tracker)는 메타데이터(제목, 초록, URL)만 저장한다.
실제 파일을 Claude가 직접 읽어야 할 때 이 폴더에 저장한다.

## 인용 방식
리포트 본문에 각주로 직접 삽입:
> "테라헤르츠 대역 커버리지는 실내 10m 한계" [ref: 6g_samsung-whitepaper.pdf, p.12]

리포트가 완성되면 각주가 리포트에 내장되므로 이 폴더를 매번 조회할 필요 없음.
파일은 사용 후 아카이브로 남긴다.

## 파일명 규칙
`{topic-slug}_{설명}.{ext}`
예: `6g_samsung-whitepaper.pdf`, `open-ran_lgu-internal-report-2025.pdf`

## 저장 대상 예시
- LG U+ 사내 보고서, 제안서 초안
- 유료 논문 PDF (URL 접근 불가)
- 표준 기구 문서 (3GPP, ITU 등)
- 다운로드한 API 스펙 문서 (.yaml, .json)
