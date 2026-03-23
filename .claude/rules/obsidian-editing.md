# Obsidian 파일 편집 규칙

Obsidian 마크다운 파일 편집 시 `sed`나 줄 기반 `Edit` 대신 `Write`(전체 파일 재작성)를 사용한다.
- 특수 문자, 한글, frontmatter가 포함된 파일에서 sed가 0B 파일을 생성하는 반복 문제 방지
- 편집 후 파일 크기가 0이 아닌지 검증한다
