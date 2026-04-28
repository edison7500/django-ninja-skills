# 🥷 Django Ninja Skills

> 使用 Django 构建高性能、类型安全且异步优先 API 的专家级模式。

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.2+-092e20.svg)](https://www.djangoproject.com/)
[![Framework](https://img.shields.io/badge/framework-Django--Ninja-ff69b4.svg)](https://django-ninja.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)

本项目旨在提供一份使用 Python 3.10+ 类型提示和 Pydantic 开发 RESTful API 的全面指南。它专注于掌握 [Django Ninja](https://django-ninja.dev/) 的三大支柱：异步并发、自动化文档和严格的类型安全。

## 🚀 核心能力

1. 高级数据处理
* 精确解析：利用类型提示处理 Path、Query、Header 和 Cookie 参数。
* 复杂负载：使用 Pydantic Schemas 定义健壮的请求体。
* 摄取精通：无缝处理表单数据、多部分请求和文件上传。

2. 响应优化
* 高效序列化：使用 ModelSchema 进行直接、高性能的 Django 模型映射。
* 细粒度控制：为不同的 HTTP 状态码定义特定的响应模型。
* 内置实用程序：利用原生的分页 (Pagination) 和自定义响应渲染器 (Response Renderers)。

3. 可扩展架构
* 模块化路由：使用 Router 类解耦业务领域。
* 依赖注入：为身份验证和数据注入实现可重用逻辑。

## 💡 最佳实践

| 类别 | 标准操作程序 | 
|---	|---	|
| 设计 | 模式优先：始终定义 Pydantic Schemas 用于数据交换。|
| 并发 | 异步集成：对于 I/O 密集型视图优先使用 ```async def``` 并使用 Django 5.0+ ORM。|
| 错误 | 标准化契约：使用 ```ninja.errors.HttpError``` 确保一致的错误响应。|
| 安全 | 注入保护：通过 ```Router``` 或 ```NinjaAPI``` 中的 ```auth``` 参数强制执行身份验证。 |
| 整洁代码 | 命名约定：在 Schema 类后面添加 ```In``` 或 ```Out``` 后缀（例如：```UserIn```, ```UserOut```）。 |
| 结构 | 瘦视图：将逻辑保留在专门的 ```services.py``` 层中，而非 API 处理程序中。| 

## 📚 实现参考

在贡献或生成代码时，请遵循以下本地模块中建立的模式：

* 📂 [Schemas](snippets/schemas.py)：ModelSchema 定义和字段命名的标准。
* 📂 [Async CRUD](snippets/crud_async.py)：async def 和现代 Django ORM 调用的模式。
* 📂 [Authentication](snippets/auth.py)：APIKey、JWT 和基于依赖的安全性实现。
* 📂 [CSRF 保护](snippets/csrf.py)：CSRF 免除和验证模式。
* 📂 [Quality Benchmarks](snippets/comparison.py)：反模式与优化代码之间的对比。

---
