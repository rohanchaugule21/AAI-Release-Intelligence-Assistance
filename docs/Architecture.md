# Architecture Overview

## Objective

The AAI Release Intelligence Assistant provides a natural language interface for exploring release information, stories, components, dependencies, and trends.

---

## High-Level Architecture

```text
User
 │
 ▼
FastAPI API
 │
 ▼
Intent Router
 │
 ├── Search Engine
 ├── Query Engine
 ├── Trend Engine
 └── Entity Extractor
 │
 ▼
Knowledge Base
 │
 ▼
Response Formatter
 │
 ▼
User Response
```

---

## Core Components

### FastAPI Layer

Responsible for:

- Receiving requests
- Validating inputs
- Exposing REST endpoints
- Generating Swagger documentation

---

### Intent Router

Determines the type of incoming question.

Examples:

- Search
- Trend Analysis
- Comparison
- Summary

---

### Entity Extractor

Identifies key entities from questions.

Examples:

- Release Numbers
- Story IDs
- Components
- Dependencies

---

### Search Engine

Processes information retrieval requests and identifies relationships between:

- Releases
- Stories
- Components
- Dependencies

---

### Trend Engine

Analyzes release information to identify patterns and trends.

---

### Knowledge Base

Stores the structured information used by the application.

---

### Response Formatter

Formats raw results into readable responses for end users.