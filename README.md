# 🥷 Django Ninja Skills

[中文版 README](./README.zh-CN.md) | [繁體中文版 README](./README.zh-TW.md) | [日本語版 README](./README.ja.md)

> Expert-level patterns for building high-performance, type-safe, and async-first APIs with Django.

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.2+-092e20.svg)](https://www.djangoproject.com/)
[![Framework](https://img.shields.io/badge/framework-Django--Ninja-ff69b4.svg)](https://django-ninja.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)

This project serves as a comprehensive guide for developing RESTful APIs using Python 3.10+ type hints and Pydantic. It focuses on mastering the three pillars of [Django Ninja](https://django-ninja.dev/): Asynchronous concurrency, Automated documentation, and Strict type safety.

## 🚀 Core Competencies

1. Advanced Data Handling
* Precision Parsing: Utilizing type hints for Path, Query, Header, and Cookie parameters.
* Complex Payloads: Defining robust request bodies using Pydantic Schemas.
* Ingestion Mastery: Handling Form data, multi-part requests, and file uploads seamlessly.

2. Response Optimization
* Efficient Serialization: Using ModelSchema for direct, high-performance Django model mapping.
* Granular Control: Defining specific response models for different HTTP status codes.
* Built-in Utility: Leveraging native Pagination and custom Response Renderers.

3. Scalable Architecture
* Modular Routing: Decoupling business domains using the Router class.
* Dependency Injection: Implementing reusable logic for authentication and data injection.

## 💡 Best Practices

|Category|Standard Operating Procedure| 
|---	|---	|
|Design |Schema-First: Always define Pydantic Schemas for data exchange.|
|Concurrency |Async Integration: Prefer ```async def``` for I/O-bound views and use Django 5.0+ ORM.|
|Errors |Standardized Contracts: Use ```ninja.errors.HttpError``` for consistent error responses.|
|Security |Injected Protection: Enforce auth via the ```auth``` parameter in ```Router``` or ```NinjaAPI```. |
|Clean Code |Naming Conventions: Suffix schema classes with ```In``` or ```Out``` (e.g., ```UserIn```, ```UserOut```). |
|Structure |Thin Views: Keep logic in a dedicated ```services.py``` layer, not in the API handler.| 

## 📚 Implementation Reference

When contributing or generating code, adhere to the patterns established in these local modules:

* 📂 [Schemas](snippets/schemas.py): Standards for ModelSchema definitions and field naming.
* 📂 [Async CRUD](snippets/crud_async.py): Patterns for async def and modern Django ORM calls.
* 📂 [Authentication](snippets/auth.py): Implementations for APIKey, JWT, and dependency-based security.
* 📂 [Quality Benchmarks](snippets/comparison.py): Comparisons between anti-patterns and optimized code.

---
