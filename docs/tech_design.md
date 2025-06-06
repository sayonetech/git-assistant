# Technical Design: Context-Aware Git Assistant

## Overview
This document outlines the technical architecture and stack for the Context-Aware Git Assistant, focusing on performance, maintainability, and future integrations with Cursor and Modal.

## Core Tech Stack

### Agent & Processing Layer
| Component | Technology | Purpose |
|-----------|------------|----------|
| Agent Workflow | LangGraph | Orchestrates branching conversational logic (LLM + tool-based) |
| Tool Layer | LangChain | Handles embeddings, retrievers, and tool definitions |
| Vector Store | Qdrant | Provides fast semantic search and chunk indexing |
| Embedding Model | OpenAI (text-embedding-3-small) | Generates embeddings for code and documentation |

### API & Infrastructure
| Component | Technology | Purpose |
|-----------|------------|----------|
| API Framework | FastAPI | Provides lightweight, async-ready REST APIs |
| Git Operations | GitPython | Enables programmatic Git repository cloning |
| File Processing | LangChain TextSplitters | Handles intelligent chunking of code and documentation |
| Background Jobs | Celery + Redis (optional) | Manages asynchronous repo parsing and indexing |
| Deployment | Modal | Serverless backend with built-in FastAPI support |
| Interface | Cursor IDE Plugin / HTTP Client | Provides local testing and IDE integration |

## Development Tools

### Monitoring & Testing
| Tool | Purpose |
|------|----------|
| LangSmith/Langfuse | Tracing and debugging LangGraph workflows |
| pytest + httpx | API testing |
| Pydantic | Input validation for FastAPI |
| dotenv | Secure API key management |
| tqdm | Progress tracking for chunking/embedding |
| Uvicorn | Async server for FastAPI |

## Environment Requirements

### Runtime Environment
| Requirement | Specification |
|-------------|---------------|
| Python Version | >=3.10 (for match statements + LangGraph compatibility) |
| Virtual Environment | Poetry or venv |
| IDE | Cursor (for testing) or VSCode |
| Hosting | Modal or Docker container |

## Architecture Summary

### Core Components
1. **API Layer**
   - FastAPI for REST endpoints
   - Async request handling
   - Input validation with Pydantic

2. **Language Processing**
   - LangGraph for workflow orchestration
   - LangChain for tool integration
   - OpenAI for embeddings

3. **Data Storage**
   - Qdrant for vector storage
   - Optional Redis for job queue

4. **Git Integration**
   - GitPython for repository operations
   - LangChain text splitters for code processing

5. **Deployment**
   - Modal for serverless deployment
   - Docker support for alternative deployment

## Development Workflow

### Local Development
1. Set up Python 3.10+ environment
2. Install dependencies via Poetry/requirements.txt
3. Configure environment variables
4. Run FastAPI server locally with Uvicorn
5. Test with Cursor IDE or HTTP client

### Testing Strategy
1. Unit tests with pytest
2. API integration tests with httpx
3. LangGraph workflow tracing with LangSmith
4. Performance testing for embedding generation

### Deployment Process
1. Code review and testing
2. Environment configuration
3. Modal deployment
4. Monitoring setup

## Security Considerations

### API Security
- API key authentication
- Rate limiting
- Input validation
- Secure environment variable handling

### Data Security
- Secure storage of embeddings
- Access control for repositories
- API key management

## Performance Considerations

### Optimization Areas
- Efficient chunking strategies
- Caching frequently accessed data
- Asynchronous processing
- Vector search optimization

## Future Enhancements

### Planned Improvements
1. Enhanced code analysis
2. Multi-repository support
3. Advanced caching strategies
4. Extended IDE integration

## Notes
- All timestamps use ISO 8601 format
- API responses are JSON-formatted
- Base URL configuration is environment-specific 