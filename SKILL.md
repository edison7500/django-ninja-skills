---
name: django-ninja-skills
description: Expert guidance for high-performance Django API development using Django Ninja.
---

# Django Ninja Skills

## Overview

This skill provides expert-level guidance for building RESTful APIs using **Python 3.10+ type hints** and **Pydantic**. It focuses on leveraging Django Ninja's core strengths: **Asynchronous support (Async)**, **Automatic OpenAPI/Swagger generation**, and **Type-safe data validation**.

## Core Competencies

**1. Input Parsing & Validation:**
- **Parameter Handling**: Using type hints for Path, Query, Header, and Cookie parameters.
- **Request Body**: Defining complex payloads using Pydantic Schemas.
- **Data Ingestion**: Managing Form data, file uploads, and multi-part requests.

**2. Response Serialization:**
- **Schema Modeling**: Utilizing `ModelSchema` for direct Django model mapping.
- **Response Control**: Defining status-code-specific responses (e.g., `{201: SuccessOut, 403: ErrorOut}`).
- **Optimization**: Implementing built-in Pagination and custom Response Renderers.

**3. API Architecture:**
- **Modular Routing**: Using `Router` to decouple business domains.
- **Dependency Injection**: Implementing reusable authentication and logic injection.

## Instructions

1.  **Schema-First Design**: Always define Pydantic Schemas for data exchange. Use `ModelSchema` to map Django models, explicitly controlling field exposure via `model_fields` or `model_exclude`.
2.  **Async Integration**: Prefer `async def` for I/O-bound view functions, ensuring compatibility with Django’s asynchronous ORM features.
3.  **Standardized Error Handling**: Avoid manual JSON error responses. Use `ninja.errors.HttpError` or register global `exception_handlers` for consistent API error contracts.
4.  **Injected Security**: Do not manually verify users within views. Use the `auth` parameter in `Router` or `NinjaAPI` to enforce authentication via dependency injection.
5.  **Documentation Standards**: Every endpoint must include a docstring and use `tags` to maintain a clean and navigable Swagger UI.

## Best Practices

- **Naming**: Suffix schema classes with `In` or `Out` (e.g., `UserIn`, `UserOut`) to clarify data flow.
- **Status Codes**: Be explicit with HTTP status codes (e.g., return `201` for successful creation).
- **Logic Separation**: Keep view functions thin; move complex business logic to a dedicated `services.py` layer.

## Reference Templates

**Refer to `snippets/schema.py` for the ModelSchema definitions and field naming.**
- Standard Pydantic Schema (Non-Model based)
- Model-based Schemas
- Advanced Filtering/Search Schema
- Auth/Token Schemas

**Refer to `snippets/crud_async.py` for the standard implementation of:**
- Async CRUD operations.
- Multi-status code handling (201, 204, 404).
- Integration with Django 5.0+ Async ORM.

**Refer to `snippets/auth.py` Implementations for APIKey, JWT, and dependency-based security.**
- API Key Authentication (e.g., for Internal Service-to-Service)
- JWT / Bearer Token Authentication (Standard Web Auth)
- Role-Based Access Control (RBAC) Pattern

**Refer to `snippets/csrf.py` for CSRF protection patterns in Django Ninja.**
- CSRF exemption and validation patterns.
- Integration with frontend CSRF tokens.

**Refer to `snippets/comparison.py` for comparisons between anti-patterns and optimized code.**
- Response Handling
- Async Usage
- Error Handling
- Authentication



---