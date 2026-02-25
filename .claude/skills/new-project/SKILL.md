---
name: new-project
description: "새 서브프로젝트를 표준 구조로 스캐폴딩한다. projects/ 아래에 프로젝트를 생성한다."
user-invokable: true
argument-hint: "[project-name]"
---

# Create a New Sub-Project

워크스페이스에 새 프로젝트를 스캐폴딩한다.

## Arguments
- 첫 번째 인자: 프로젝트 이름 (lowercase-kebab-case)
- 실험적 프로젝트는 날짜 접두사 사용 (예: `2026-02-agent-test`)

## Steps

1. **대상 디렉토리 결정:**
   - `/Users/ctoti/Project/ClaudeCode/projects/{name}/`
   - 인자가 없으면 사용자에게 물어본다

2. **디렉토리 구조 생성:**
   ```
   {target}/
     CLAUDE.md
     pyproject.toml
     src/
       __init__.py
     tests/
       __init__.py
   ```

3. **CLAUDE.md 작성** (프로젝트별 컨텍스트):
   ```markdown
   # {project-name}

   ## Purpose
   > (describe the project goal)

   ## Key Files
   - src/: Source code
   - tests/: Test files

   ## Dependencies
   > (list key dependencies)

   ## Testing
   Run: `uv run pytest`
   ```

4. **pyproject.toml 작성:**
   ```toml
   [project]
   name = "{project-name}"
   version = "0.1.0"
   requires-python = ">=3.11"
   dependencies = []

   [tool.pytest.ini_options]
   testpaths = ["tests"]

   [tool.ruff]
   target-version = "py311"
   ```

5. 생성 결과 보고
