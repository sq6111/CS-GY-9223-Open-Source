# Contributing Guide

## Setup

1. Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone and setup:
```bash
git clone https://github.com/sq6111/CS-GY-9223-Open-Source
cd CS-GY-9223-Open-Source
uv sync
```

## Development Workflow

1. Create a branch:
```bash
git checkout -b feature/my-feature
```

2. Make changes

3. Run checks:
```bash
uv run ruff check .
uv run mypy .
uv run pytest
```

4. Commit and push:
```bash
git add .
git commit -m "Add feature"
git push origin feature/my-feature
```

5. Create PR on GitHub

## Code Quality

- All code must pass ruff and mypy strict checks
- Test coverage must be >= 80%
- Use absolute imports only
- Follow type hints

## Testing

- Unit tests: Test individual components with mocks
- Integration tests: Test dependency injection
- E2E tests: Test against real APIs (with test credentials)
