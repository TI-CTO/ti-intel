---
globs: "projects/**/*.py"
---

# Python Coding Conventions

- Type hints on all function signatures
- Google-style docstrings on public functions
- `pathlib` over `os.path`
- `dataclasses` or `Pydantic` for structured data
- No `print()` for logging; use standard `logging` module
- Use `uv` for package management (no pip, conda)
