# 🥷 Django Ninja Skills

> 使用 Django 構建高效能、類型安全且異步優先 API 的專家級模式。

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.2+-092e20.svg)](https://www.djangoproject.com/)
[![Framework](https://img.shields.io/badge/framework-Django--Ninja-ff69b4.svg)](https://django-ninja.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)

本專案旨在提供一份使用 Python 3.10+ 類型提示和 Pydantic 開發 RESTful API 的全面指南。它專注於掌握 [Django Ninja](https://django-ninja.dev/) 的三大支柱：異步併發、自動化文件和嚴格的類型安全。

## 🚀 核心能力

1. 高級數據處理
* 精確解析：利用類型提示處理 Path、Query、Header 和 Cookie 參數。
* 複雜負載：使用 Pydantic Schemas 定義健壯的請求體。
* 攝取精通：無縫處理表單數據、多部分請求和文件上傳。

2. 響應優化
* 高效序列化：使用 ModelSchema 進行直接、高效能的 Django 模型映射。
* 細粒度控制：為不同的 HTTP 狀態碼定義特定的響應模型。
* 內置實用程序：利用原生的分頁 (Pagination) 和自定義響應渲染器 (Response Renderers)。

3. 可擴展架構
* 模塊化路由：使用 Router 類解耦業務領域。
* 依賴注入：為身份驗證和數據注入實現可重用邏輯。

## 💡 最佳實踐

| 類別 | 標準操作程序 | 
|---	|---	|
| 設計 | 模式優先：始終定義 Pydantic Schemas 用於數據交換。|
| 併發 | 異步集成：對於 I/O 密集型視圖優先使用 ```async def``` 並使用 Django 5.0+ ORM。|
| 錯誤 | 標準化契約：使用 ```ninja.errors.HttpError``` 確保一致的錯誤響應。|
| 安全 | 注入保護：通過 ```Router``` 或 ```NinjaAPI``` 中的 ```auth``` 參數強制執行身份驗證。 |
| 整潔代碼 | 命名約定：在 Schema 類後面添加 ```In``` 或 ```Out``` 後綴（例如：```UserIn```, ```UserOut```）。 |
| 結構 | 瘦視圖：將邏輯保留在專門的 ```services.py``` 層中，而非 API 處理程序中。| 

## 📚 實現參考

在貢獻或生成代碼時，請遵循以下本地模塊中建立的模式：

* 📂 [Schemas](snippets/schemas.py)：ModelSchema 定義和字段命名的標準。
* 📂 [Async CRUD](snippets/crud_async.py)：async def 和現代 Django ORM 調用的模式。
* 📂 [Authentication](snippets/auth.py)：APIKey、JWT 和基於依賴的安全性實現。
* 📂 [Quality Benchmarks](snippets/comparison.py)：反模式與優化代碼之間的對比。

---
