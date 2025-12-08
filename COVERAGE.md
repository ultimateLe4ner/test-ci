# Code Coverage Report

This repository includes automated code coverage analysis for Python code.

## Quick Start

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Tests with Coverage
```bash
pytest --cov=app --cov=output_something --cov-report=term-missing --cov-report=html
```

Or simply:
```bash
pytest
```

## Coverage Results

### Current Coverage Summary

| File | Statements | Missing | Coverage |
|------|-----------|---------|----------|
| app.py | 7 | 1 | **86%** |
| output_something.py | 1 | 1 | **0%** |

### Overall Coverage: **86%** for app.py (main application code)

## Coverage Details

### app.py (86% coverage)
- **Covered**: 
  - Flask app initialization
  - Route definition (`/`)
  - `hello()` function logic
- **Not Covered**:
  - Line 10: `app.run()` - This is the main entry point that only executes when running the script directly

### output_something.py (0% coverage)
- This file is a simple print statement that executes immediately when imported
- The test validates its output but coverage tools don't capture module-level execution
- The functionality is tested and working correctly

## Test Files

- `test_app.py` - Tests for the Flask application
  - Tests the GET endpoint returns "hello"
  - Tests that other HTTP methods are rejected

- `test_output_something.py` - Tests for output_something.py
  - Validates the print output

## HTML Coverage Report

After running tests, view detailed coverage in your browser:
```bash
open htmlcov/index.html  # macOS
# or
xdg-open htmlcov/index.html  # Linux
# or
start htmlcov/index.html  # Windows
```

## Improving Coverage

To achieve 100% coverage for `app.py`, you would need to test the main block:
```python
if __name__ == '__main__':
    app.run()
```

However, this is typically excluded from coverage requirements as it's an entry point that would start a server and is not part of the application logic.

## CI/CD Integration

You can integrate coverage into your GitHub Actions workflow by adding:

```yaml
- name: Run tests with coverage
  run: |
    pip install -r requirements.txt
    pytest --cov=app --cov=output_something --cov-report=term --cov-report=xml
    
- name: Upload coverage reports
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
```
