# Makefile for Python project with pytest markers

PYTHONPATH := $(shell pwd)
export PYTHONPATH

.PHONY: install test all fast slow coverage reports clean help

# Install project in editable mode and dependencies
install:
	pip install -e .
	pip install -r requirements.txt

# Run all tests
all: install
	pytest

# Run fast tests
fast: install
	pytest -m fast

# Run slow tests
slow: install
	pytest -m slow

# Run with coverage
coverage: install
	pytest --cov=./ --cov-report=xml --cov-report=html

# Generate test reports
reports: install
	pytest --junitxml=test-results.xml --html=report.html --self-contained-html

# Clean generated files
clean:
	rm -rf .coverage coverage.xml htmlcov test-results.xml report.html .pytest_cache

# Show help
help:
	@echo "Available commands:"
	@echo "  make install    - Install project in editable mode"
	@echo "  make all        - Run all tests"
	@echo "  make fast       - Run fast tests"
	@echo "  make slow       - Run slow tests"
	@echo "  make coverage   - Run tests with coverage"
	@echo "  make reports    - Generate test reports"
	@echo "  make clean      - Clean temporary files"

