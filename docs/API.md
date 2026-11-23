# API Documentation

## Overview

The AAI Release Intelligence Assistant exposes REST APIs through FastAPI.

Swagger UI is available when running locally.

---

## Base URL

```text
http://127.0.0.1:8000
```

---

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Primary Endpoint

### POST /ask-smart

Accepts a natural language question and returns an intelligent response.

#### Request

```json
{
  "question": "Find Azure Blob Storage"
}
```

#### Sample Response

```json
{
  "route": "SEARCH",
  "answer": "Related Releases: 25"
}
```

---

## Supported Question Types

### Search Questions

Examples:

```text
Find Azure Blob Storage

Find story AAI-IRS-44

Show Release 25
```

---

### Trend Questions

Examples:

```text
Show technology trends

Which components appear most frequently?
```

---

### Release Intelligence Questions

Examples:

```text
What dependencies exist in Release 25?

What stories belong to Release 25?
```

---

## Response Structure

```json
{
  "route": "<identified_route>",
  "answer": "<formatted_response>"
}
```

### Route Types

- SEARCH
- TREND
- COMPARE
- SUMMARY

---

## Validation

All API testing is currently performed through:

- FastAPI Swagger UI
- Local Streamlit Interface
- Direct API Invocation
