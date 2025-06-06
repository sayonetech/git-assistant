# Git Assistant

A context-aware Git assistant using LangGraph and FastAPI.

## Requirements

- Python 3.10+
- Poetry

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd git-assistant
```

2. Install dependencies using Poetry:
```bash
poetry install
```

## Running the Application

1. Activate the Poetry shell:
```bash
poetry shell
```

2. Start the FastAPI server:
```bash
uvicorn src.git_assistant.main:app --reload
```

The API will be available at:
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
git-assistant/
├── src/                    # Source code
│   └── git_assistant/     # Main package
├── docs/                  # Documentation
├── tests/                # Test files
├── pyproject.toml        # Poetry configuration
├── poetry.lock          # Dependency lock file
├── Makefile             # Development commands
└── README.md            # Project documentation
```

## API Endpoints

### Health Check
- `GET /ping`: Returns a simple "pong" response to verify the service is running

## Development

### Code Formatting
The project uses Black and isort for code formatting. To format the code:

```bash
poetry run black .
poetry run isort .
```

### Running Tests
```bash
poetry run pytest
``` 