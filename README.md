# test-ci

A Flask-based Python application with comprehensive test coverage.

## 📊 Code Coverage: 100%

This repository has **100% code coverage** for the main application code.

## Quick Start

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
python app.py
```

### Run Tests with Coverage
```bash
pytest
```

## 📈 Coverage Reports

After running tests, detailed coverage reports are available:

- **Terminal Output**: Shows coverage summary with missing lines
- **HTML Report**: Open `htmlcov/index.html` in your browser for detailed, interactive coverage report
- **JSON Report**: Machine-readable coverage data in `coverage.json`

## 📚 Documentation

- **[COVERAGE.md](COVERAGE.md)** - Detailed guide on running and interpreting coverage
- **[COVERAGE_SUMMARY.md](COVERAGE_SUMMARY.md)** - Comprehensive coverage analysis summary

## 🧪 Test Suite

- `test_app.py` - Tests for Flask application endpoints
- `test_output_something.py` - Tests for output_something.py functionality

All tests are passing (3/3) ✅

## 🔒 Security

CodeQL security analysis: **0 vulnerabilities found** ✅

## Project Structure

```
.
├── app.py                    # Flask web application
├── output_something.py       # Simple output script
├── test_app.py              # Tests for Flask app
├── test_output_something.py # Tests for output script
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Pytest and coverage configuration
├── COVERAGE.md             # Coverage documentation
└── COVERAGE_SUMMARY.md     # Detailed coverage analysis
```

## Configuration

Test and coverage configuration is in `pyproject.toml`. The configuration:
- Runs tests from the current directory
- Targets `app.py` and `output_something.py` for coverage
- Excludes `if __name__ == '__main__':` blocks (entry points)
- Generates both terminal and HTML reports

## Contributing

1. Make your changes
2. Add/update tests as needed
3. Run `pytest` to ensure all tests pass with coverage
4. Ensure coverage remains at or above 100%

## License

This is a test/demonstration repository.
