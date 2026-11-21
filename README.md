# AAI-Release-Intelligence-Assistance
AAI Release Intelligence Assistant is an AI-powered platform designed to simplify the way teams access release information, technical components, dependencies, and implementation details for AAI22 and AAI44 Release Notes.

The solution enables users to ask questions in natural language and receive intelligent responses without manually searching through release documentation, stories, or technical records.

The platform combines release knowledge, search capabilities, trend analysis, and intelligent query routing to provide a single source of truth for release intelligence.

# What does this project do?
The AAI Release Intelligence Assistant helps users quickly find information across release data without manually searching through documents and release records.

# Business Benefits
Faster access to release information

Reduced manual effort

Improved knowledge discovery

Better visibility into dependencies

Faster decision making for delivery teams


# Examples:
Find Azure Blob Storage

Show Release 25

Find story AAI-IRS-44

Show technology trends

List dependencies for a release


# Current Capabilities
Release Search

Story Search

Component Search

Dependency Analysis

Trend Analysis

FastAPI REST API

Swagger Documentation

Streamlit User Interface


# Technology Stack
Python

FastAPI

Streamlit

Swagger/OpenAPI



# Current Status
✅ FastAPI Working

✅ Swagger UI Working

✅ Query Routing Working

✅ Trend Engine Working

✅ Streamlit UI Working


## Solution Architecture

```text
User Question
      │
      ▼
FastAPI API
      │
      ▼
Intent Router
      │
      ├── Search Engine
      ├── Trend Engine
      ├── Query Engine
      └── Entity Extractor
      │
      ▼
Knowledge Base
      │
      ▼
Formatted Response
```

### Example Flow

Question:

```text
Find Azure Blob Storage
```

Processing:

1. User submits a question.
2. FastAPI receives the request.
3. Intent Router determines the request type.
4. Search Engine identifies matching releases, stories, and components.
5. Results are formatted.
6. Response is returned to the user.

Output:

```text
Related Releases: 25
Related Stories: AAI-IRS-44
Related Components: Azure Blob Storage
```


## Project Journey

This project was developed incrementally to build an AI-powered AAI Release Intelligence solution for AAI22 and AAI44.

### Phase 1: Foundation

✅ Project structure created

✅ Release documents analyzed

✅ Knowledge base generation implemented

✅ Component, dependency, and story indexing completed

### Phase 2: Intelligence Layer

✅ Entity extraction implemented

✅ Question routing implemented

✅ Search engine implemented

✅ Trend analysis engine implemented

✅ Response formatting implemented

### Phase 3: API Layer

✅ FastAPI application created

✅ REST endpoints exposed

✅ Swagger documentation enabled

✅ End-to-end API testing completed

### Phase 4: User Interface

✅ Streamlit user interface created

✅ User question submission enabled

✅ FastAPI integration completed

### Current Focus

🔄 User experience improvements

🔄 Integration readiness

🔄 Deployment preparation

### Future Roadmap

- Microsoft Teams Integration


## How It Works

When a user submits a question, the system processes it through multiple stages.

### Example Question

```text
Find Azure Blob Storage
```

### Processing Flow

#### Step 1 - User Question

The user submits a natural language query.

#### Step 2 - API Layer

FastAPI receives the request and validates the payload.

#### Step 3 - Intent Classification

The Intent Router determines what type of question was asked.

Examples:

- Search Request
- Trend Request
- Comparison Request
- Summary Request

#### Step 4 - Entity Extraction

Relevant entities are identified.

Example:

```text
Azure Blob Storage
```

Entity Type:

```text
Component
```

#### Step 5 - Search & Analysis

The appropriate engine is invoked:

- Search Engine
- Trend Engine
- Query Engine
- Knowledge Engine

#### Step 6 - Response Formatting

Results are formatted into a user-friendly response.

#### Step 7 - Response Returned

The final answer is returned through the API and displayed in the user interface.

### Example Response

```text
Related Releases: 25
Related Stories: AAI-IRS-44
Related Components: Azure Blob Storage
Related Dependencies: N/A

```

## Testing & Validation

The solution has been validated using FastAPI Swagger UI and end-to-end testing.

### Sample Test Questions

#### Search

```text
Find Azure Blob Storage
```

```text
Show Release 25
```

```text
Find story AAI-IRS-44
```

#### Trend Analysis

```text
Show technology trends
```

```text
Which components appear most frequently?
```

#### Release Intelligence

```text
What stories belong to Release 25?
```

```text
What dependencies exist in Release 25?
```

### Validation Areas

✅ API Endpoint Validation

✅ Query Routing Validation

✅ Entity Extraction Validation

✅ Search Engine Validation

✅ Trend Engine Validation

✅ Swagger Testing

✅ Streamlit Integration Testing

### Current Test Environment

- Local Development Environment
- FastAPI Swagger UI
- Streamlit User Interface
- Python 3.11
