PYTHONPATH := $(shell pwd)
export PYTHONPATH

.PHONY: install test all fast slow coverage reports full clean help

install:
	pip install -e .
	pip install -r requirements.txt

test: install
	pytest

all: test

fast: install
	pytest -m fast

slow: install
	pytest -m slow

coverage: install
	pytest --cov=./ --cov-report=xml --cov-report=html

reports: install
	pytest --junitxml=test-results.xml --html=report.html --self-contained-html

full: install
	pytest --cov=./ --cov-report=xml --junitxml=test-results.xml --html=report.html --self-contained-html

clean:
	rm -rf .coverage coverage.xml htmlcov test-results.xml report.html .pytest_cache __pycache__

help:
	@echo "Available commands:"
	@echo "  make install    - Install project in editable mode"
	@echo "  make test       - Run all tests"
	@echo "  make fast       - Run fast tests"
	@echo "  make slow       - Run slow tests"
	@echo "  make coverage   - Run tests with coverage"
	@echo "  make reports    - Generate test reports"
	@echo "  make full       - Run tests with coverage and all reports"
	@echo "  make clean      - Clean temporary files"
