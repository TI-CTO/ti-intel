# projects — 활성 코드 프로젝트

독립적인 구현 프로젝트. 실험적 프로젝트도 여기에 포함 (날짜 접두사 사용).

## Project Structure
```
project-name/
  CLAUDE.md          # 프로젝트별 컨텍스트
  pyproject.toml     # uv 기반 의존성 관리
  src/               # 소스 코드
  tests/             # pytest 테스트
```

## Rules
- 모든 프로젝트는 자체 `CLAUDE.md`를 가져야 한다
- 테스트 커버리지 80% 이상 유지
- `uv run pytest`로 테스트 실행
- `uv run ruff check . && uv run ruff format .`로 린트/포맷
