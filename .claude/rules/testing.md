---
globs: "tests/**/*.py"
---

# Testing Conventions

- Framework: `pytest`
- Test files colocated in `tests/` directory
- Naming: `test_<module>.py` for files, `test_<function>` for functions
- Use fixtures for shared setup; avoid test interdependence
- Run with: `~/.local/bin/uv run pytest`
