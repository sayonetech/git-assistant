# Phase 1 Requirements: Context-Aware Git Assistant

## Overview
This document outlines the technical requirements and implementation details for Phase 1 of the Context-Aware Git Assistant project.

## Technical Components

### 1. Repository Ingestion
**Purpose:** Process and prepare repository content for analysis

#### Components:
- GitHub repository cloning
- File type filtering:
  - Python (.py)
  - JavaScript (.js)
  - TypeScript (.ts)
  - Markdown (.md)
  - Configuration (.json)
- File reading and chunking for embedding

### 2. Embedding & Vector Store
**Purpose:** Convert and store code/documentation for semantic search

#### Components:
- Embedding Models:
  - Primary: OpenAI (text-embedding-3-small)
  - Alternative: Ollama local model
- Vector Storage:
  - Options: Qdrant
- Indexing with metadata:
  - Filename
  - Function names
  - Other relevant metadata

### 3. LangGraph Agent
**Purpose:** Orchestrate intelligent code analysis and response generation

#### Workflow:
```
input → classify intent → retrieve context → respond
```

#### Core Nodes:
1. **input_node**
   - Receives question and repository path
   - Validates input

2. **retriever**
   - Fetches relevant code/documentation chunks
   - Applies semantic search

3. **agent_node**
   - Uses LLM for answer synthesis
   - Generates coherent responses

#### Optional Nodes:
- Summarizer
- Planner

### 4. Local Interface
**Purpose:** Provide testing interface before Modal deployment

#### Options:
- FastAPI endpoints
- CLI prompt interface

## Minimal Feature Set

| Feature | Implementation |
|---------|----------------|
| Git Repository Puller | gitpython or subprocess |
| Chunking & Parsing | LangChain's RecursiveCharacterTextSplitter |
| Embedding | OpenAIEmbeddings  |
| Vector Store | Qdrant |
| Agent Logic | LangGraph with LangChain tool nodes |
| Local Runner | Python script or FastAPI endpoint |

## Phase 1 Demo Scope

### Supported Developer Questions

| Question Type | Example | Intent |
|--------------|---------|---------|
| Repository Overview | "Give me a summary of this repo" | High-level repository understanding |
| File Analysis | "What does main.py do?" | File-level summarization |
| Code Reference | "Where is init_db() defined?" | Basic code search |
| Dependency Analysis | "What packages are used?" | Dependency inference |

## Learning Outcomes

### Technical Skills
1. Building custom LangGraph workflows
2. Understanding RAG architecture for code
3. Vector DB integration with embeddings
4. Modal deployment preparation

### Future Integration
- HTTP endpoint structure for Cursor integration
- Extensible architecture for Phase 2 features

## Implementation Notes

### Priority Order
1. Basic repository ingestion
2. Embedding and vector store setup
3. LangGraph agent implementation
4. Local interface development
5. Testing and refinement

### Success Criteria
- Successful repository cloning and processing
- Accurate semantic search results
- Coherent responses to basic questions
- Stable local interface
- Ready for Modal deployment

## Next Steps
1. Set up development environment
2. Implement repository ingestion
3. Configure embedding pipeline
4. Develop LangGraph workflow
5. Create local interface
6. Test with sample repositories
7. Prepare for Modal deployment 