# API Design: Context-Aware Git Assistant

## Overview
This document outlines the API endpoints for the Context-Aware Git Assistant, focusing on Phase 1 implementation. The API provides endpoints for repository loading, querying, and status monitoring.

## Core Endpoints

### 1. Load Repository
**Endpoint:** `POST /load_repo`

**Purpose:** Clone a GitHub repository, process its files, and store embeddings in the vector database.

**Request Body:**
```json
{
  "repo_url": "https://github.com/user/repo",
  "branch": "main",
  "namespace": "repo123"
}
```

**Response:**
```json
{
  "message": "Repo processed and stored",
  "chunks_indexed": 143,
  "namespace": "repo123"
}
```

### 2. Ask Question
**Endpoint:** `POST /ask`

**Purpose:** Query the loaded repository using natural language questions.

**Request Body:**
```json
{
  "question": "What does main.py do?",
  "namespace": "repo123"
}
```

**Response:**
```json
{
  "answer": "The main.py file initializes the app, sets up routing, and starts the server."
}
```

### 3. Status Check
**Endpoint:** `GET /status`

**Purpose:** Health check and uptime monitoring.

**Response:**
```json
{
  "status": "ok"
}
```

## Future Endpoints (Phase 2+)

The following endpoints are planned for future phases:

| Endpoint | Method | Purpose |
|----------|--------|----------|
| `/namespaces` | GET | List all indexed repositories |
| `/namespace/{id}` | DELETE | Clear stored data for a specific repository |
| `/functions` | GET | List detected functions and classes |
| `/summarize_file` | POST | Generate summary for a specific file |

## Error Handling

All endpoints will return appropriate HTTP status codes:
- 200: Success
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error

Error responses will follow this format:
```json
{
  "error": "Error message description",
  "code": "ERROR_CODE"
}
```

## Rate Limiting

To be implemented in future phases:
- Rate limits per namespace
- Concurrent request limits
- API key authentication

## Authentication

Authentication requirements will be added in future phases:
- API key authentication
- GitHub OAuth integration
- Role-based access control

## Notes
- All timestamps are in ISO 8601 format
- All endpoints accept and return JSON
- Base URL will be determined by deployment configuration 