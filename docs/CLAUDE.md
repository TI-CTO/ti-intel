# docs — 에이전트/스킬 설계 문서

에이전트와 스킬의 설계 청사진을 보관한다.
실제 실행 파일은 `.claude/skills/`와 `.claude/agents/`에 있다.

## Naming
- 스킬 설계: `name.skill.md` (예: `wtis-v2.skill.md`)
- 에이전트 설계: `name.agent.md` (예: `code-reviewer.agent.md`)

## Rules
- 에이전트는 최소 권한 원칙 — 필요한 도구만 허용
- 스킬은 단일 책임 — 하나의 명확한 작업만 수행
- 테스트용 프롬프트와 예상 결과를 함께 문서화
