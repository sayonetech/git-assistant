.PHONY: install run test lint format clean run-python

# Variables
PYTHON := python
POETRY := poetry
UVICORN := uvicorn

# Default target
.DEFAULT_GOAL := help

# Help
help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies using Poetry"
	@echo "  make run        - Run the FastAPI application"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linting checks"
	@echo "  make format     - Format code using black and isort"
	@echo "  make clean      - Clean up Python cache files"

# Installation
install:
	$(POETRY) install


# Testing
test:
	$(POETRY) run pytest

# Linting
lint:
	$(POETRY) run flake8 src tests
	$(POETRY) run black --check src tests
	$(POETRY) run isort --check-only src tests

# Formatting
format:
	$(POETRY) run black src tests
	$(POETRY) run isort src tests

# Clean up
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".tox" -exec rm -r {} +
	find . -type d -name "htmlcov" -exec rm -r {} +
	find . -type d -name "dist" -exec rm -r {} +
	find . -type d -name "build" -exec rm -r {} +

# Run the application
run:
	$(POETRY) run python src/main.py 