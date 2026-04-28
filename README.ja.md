# 🥷 Django Ninja Skills

> Django を使用して、高性能でタイプセーフ、かつ非同期優先の API を構築するためのエキスパートレベルのパターン。

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.2+-092e20.svg)](https://www.djangoproject.com/)
[![Framework](https://img.shields.io/badge/framework-Django--Ninja-ff69b4.svg)](https://django-ninja.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)

このプロジェクトは、Python 3.10+ のタイプヒントと Pydantic を使用して RESTful API を開発するための包括的なガイドです。[Django Ninja](https://django-ninja.dev/) の 3 つの柱である「非同期並行処理」、「自動ドキュメント化」、「厳格なタイプセーフ」の習得に焦点を当てています。

## 🚀 コアコンピテンシー

1. 高度なデータ処理
* 精密なパース: タイプヒントを使用して Path, Query, Header, Cookie パラメータを処理。
* 複雑なペイロード: Pydantic Schemas を使用して堅牢なリクエストボディを定義。
* インジェクションの習熟: フォームデータ、マルチパートリクエスト、ファイルアップロードをシームレスに処理。

2. レスポンスの最適化
* 効率的なシリアライゼーション: ModelSchema を使用して、Django モデルへの直接的で高性能なマッピングを実現。
* きめ細やかな制御: HTTP ステータスコードごとに特定のレスポンスモデルを定義。
* 内蔵ユーティリティ: ネイティブのページネーション (Pagination) とカスタムレスポンスレンダラー (Response Renderers) を活用。

3. スケーラブルなアーキテクチャ
* モジュール式ルーティング: Router クラスを使用してビジネスドメインを切り離し。
* 依存性の注入: 認証とデータ注入のための再利用可能なロジックを実装。

## 💡 ベストプラクティス

| カテゴリ | 標準操作手順 (SOP) | 
|---	|---	|
| 設計 | スキーマ優先: データ交換には常に Pydantic Schemas を定義する。|
| 並行処理 | 非同期統合: I/O 拘束型のビューには ```async def``` を優先し、Django 5.0+ ORM を使用する。|
| エラー | 標準化された契約: 一貫したエラーレスポンスのために ```ninja.errors.HttpError``` を使用する。|
| セキュリティ | 注入による保護: ```Router``` または ```NinjaAPI``` の ```auth``` パラメータを介して認証を強制する。 |
| クリーンコード | 命名規則: スキーマクラスに ```In``` または ```Out``` サフィックスを付ける (例: ```UserIn```, ```UserOut```)。 |
| 構造 | シンビュー: ロジックは API ハンドラーではなく、専用の ```services.py``` レイヤーに保持する。| 

## 📚 実装リファレンス

貢献またはコード生成を行う際は、以下のローカルモジュールで確立されたパターンに従ってください：

* 📂 [Schemas](snippets/schemas.py): ModelSchema の定義とフィールド命名の標準。
* 📂 [Async CRUD](snippets/crud_async.py): async def とモダンな Django ORM コールのパターン。
* 📂 [Authentication](snippets/auth.py): APIKey, JWT, および依存ベースのセキュリティ実装。
* 📂 [Quality Benchmarks](snippets/comparison.py): アンチパターンと最適化されたコードの比較。

---
