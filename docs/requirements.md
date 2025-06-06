# Git Assistant Project Requirements

## Overview
This project aims to create an intelligent Git repository assistant that can understand, analyze, and help developers work with codebases more effectively. The project is divided into four phases, each building upon the previous one to create a comprehensive development assistant.

## Objective

To build a LangGraph-based agent that can ingest a code repository, understand its structure and contents, and respond intelligently to developer queries about it.


## Phase 1: Core Assistant
**Goal**: Answer questions about a Git repo using LangGraph + basic context.

### Features
- Input handling for GitHub repo URL or local file list
- Parse and embed files (code, markdown, config)
- LangGraph agent capabilities:
  - Repository summarization
  - Code file explanations
  - "What does this do?" question answering

### Technical Stack
- LangGraph for orchestration
- FAISS/Qdrant for vector database
- LangChain Tools (code_interpreter, retriever_tool)
- Modal for hosting
- Cursor for endpoint triggering

## Phase 2: Code-Aware Enhancements
**Goal**: Understand and navigate codebase like a junior developer.

### Features
- Function-level summaries
- Call graph tracing (e.g., who calls this function?)
- Link between README sections and actual code

### Technical Add-ons
- AST parsing (Python: ast, JS: acorn)
- Chunking via language-aware splitters
- Tagging by file type for smart prioritization

## Phase 3: Dev Flow Assistant
**Goal**: Help during active development in Cursor.

### Features
- PR summary: "Summarize changes in this PR"
- Test case suggestions for current diff
- Comment generator: "Add docstring to this function"
- Works on hover or inline context
- Bonus: Cursor plugin integration (via devtools.json + REST calls)

## Phase 4: Multimodal + Fine-tuning
**Goal**: Add capability to view diagrams or understand architecture.

### Features
- Parse Mermaid / PlantUML diagrams
- Upload architecture image → describe or question
- Plan deployment (infra + steps)

## Technical Requirements
- Python-based implementation
- RESTful API endpoints
- Vector database integration
- AST parsing capabilities
- Image processing capabilities
- Integration with Cursor IDE
- Modal deployment support

## Future Considerations
- Scalability for large codebases
- Multi-language support
- Real-time collaboration features
- Performance optimization
- Security considerations for code analysis 