<h1 align="center">
	<picture>
		<source media="(prefers-color-scheme: dark)" srcset="../../../images/cacti_mcp_logo_dark.png">
		<img src="../../../images/cacti_mcp_logo.png" width="360" alt="Cacti MCP: a cactus with linked connectors. Connect. Discover. Call.">
	</picture>
</h1>

<p align="center">
	<a href="https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml"><img src="https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml/badge.svg?branch=develop" alt="CI"></a>
	<a href="../../../LICENSE"><img src="https://img.shields.io/badge/license-GPL--2.0--or--later-blue" alt="License: GPL-2.0-or-later"></a>
	<img src="https://img.shields.io/badge/Python-3.12%2B-3776ab?logo=python&amp;logoColor=white" alt="Python 3.12+">
	<img src="https://img.shields.io/badge/MCP-stdio-2e7d32" alt="MCP over stdio">
	<img src="https://img.shields.io/badge/MCP_plugin_API-v2-2e7d32" alt="MCP plugin API v2">
</p>

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · **日本語** · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP は、[Cacti MCP プラグイン](https://github.com/somethingwithproof/plugin_mcp) のアビリティを stdio 経由の MCP ツールとして公開する Python アダプターです。プラグイン自体は HTTP 経由で直接 MCP を提供しているため、クライアントがリモートサーバーに接続できる場合はそちらを使用してください。このアダプターは stdio のみに対応するクライアント向けです。公式の Python MCP SDK を使用し、ツール呼び出しをプラグインの HTTPS API（abilities contract v2、`/v1/` パス配下で提供、Bearer トークン認証のみ）に変換します。認証、認可、検証、および実行はすべて Cacti 側が担います。

**ステータス: 開発中（1.0 未満）。** バージョン 0.1.0 では、対になる [Cacti MCP プラグイン](https://github.com/somethingwithproof/plugin_mcp) を通じて、読み取り専用のデバイスインベントリとインストールバージョンの取得をサポートしています。タグ付きリリースはまだありません。Doctor 診断および修復機能は今後の課題です。

## 提供される機能

| 操作 | Cacti MCP プラグインが提供する MCP ツール |
|---|---|
| トークン所有者が参照できるデバイスの一覧を取得 | `cacti-list-devices` |
| 許可されたデバイスを 1 件取得 | `cacti-get-device` |
| Cacti、プラグイン、および API のバージョンを取得 | `cacti-get-system-info` |

ツール名、説明、入力スキーマは Cacti の権限フィルタリング済みディスカバリ応答から取得されます。Python 側のツールハンドラーを追加しなくても、許可された追加の読み取り専用プロバイダーを検出できます。

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## ユースケース

MCP クライアントを接続し、専用ユーザーが参照できる Cacti デバイスの一覧を取得したり、許可されたデバイスを 1 件検索したり、必要な管理権限（realm）を持つユーザーでインストールバージョンを取得したりできます。名前と入力スキーマはプラグインのディスカバリ応答から取得されるため、アダプター側で各プロバイダーの定義を重複して持つことはありません。登録モデルと現在の制限については、プラグインの [アビリティ登録ルール](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) を参照してください。

## コードとテストの対応表

| 動作 | 実装 | このリポジトリ内のテスト証跡 |
|---|---|---|
| HTTPS 検証、上限設定、Bearer のみの認証、v2 ページング | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP ディスカバリ、呼び出し、権限変更 | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| コマンドラインのヘルプ、バージョン、設定不足時の挙動 | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

サブプロセスのテストでは、フィクスチャ HTTP エンドポイントに対して実際の SDK クライアントとサーバーを使用しています。これは稼働中の Cacti 環境に対する結合チェックを必須としたり代替したりするものではありません。

## 安全性の仕組み

- 初期化、ツールディスカバリ、ツール呼び出し、stdio フレーミングに公式の [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) を使用しています。
- アノテーションが厳密に読み取り専用、非破壊的、かつべき等であるアビリティのみを公開します。スキーマと名前は Cacti から取得され、アダプターには SQL、デバイス認証情報、修復コマンドは含まれません。
- Bearer トークンのみを送信します（Cookie なし、CSRF 手順なし）。プラグインはすべてのリクエストでトークンの有効性と権限を再検証します。
- 検証済みの HTTPS を使用し、Cookie を保存せず、リダイレクトを拒否し、プロキシ環境変数を無視します。HTTP の利用には `--allow-loopback-http` とリテラルのループバックアドレスまたは `localhost` が必要です。
- API 呼び出しの上限を全体 35 秒、接続 5 秒、ネットワーク無通信 30 秒、レスポンスあたり約 1 MB（1,100,000 バイト）に制限しています。リクエストボディは 16,384 バイトまでに制限され、呼び出しはクライアントセッションごとに直列化されます。
- ツール引数を送信前に直近のディスカバリで得た入力スキーマと照合し、その検証済みカタログに含まれる ID のみを実行します。不一致やサーバーからの不正なスキーマはクラッシュではなくツールエラーとして返されます。
- 実行の自動リトライは行いません。ツールエラーには HTTP ステータス、AIP-193 の `status`、および ErrorInfo の `reason` のみを含め、サーバーのメッセージテキスト、レスポンスボディ、認証情報は一切含めません。標準出力（stdout）は MCP メッセージ専用として予約されています。

SDK のバージョンは `uv.lock` によって固定されています（`pyproject.toml` では `mcp>=2.3,<3`）。このアダプターは 2.x の低レベルサーバーと stdio トランスポートを使用しており、リモートの MCP HTTP エンドポイント、OAuth、リソース、プロンプト、サブスクリプション、バックグラウンドタスクは実装していません。

詳細は [API 契約](../../../docs/api.md) および [実装計画](../../../docs/plan.md) を参照してください。

## インストールとコマンドライン

Python 3.12 以降および [uv](https://docs.astral.sh/uv/) が必要です。このリポジトリのチェックアウトから次のように実行します:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

PHP プラグインをインストールして有効化し、専用の Cacti ユーザーにその権限（realm）を付与したうえで、プラグインの管理画面、My MCP Tokens ページ、または `tokens.php` コマンドを使ってそのユーザーの個人アクセストークン（`cmcp_pat_` に続いて 64 桁の小文字 16 進数）を作成してください。そのユーザーの既存の Cacti 権限（realm）およびデバイス権限は引き続き適用されます。

トークンはシークレットマネージャー経由で `CACTI_MCP_TOKEN` として渡してください。ソース管理やコマンド引数には決して含めないでください。エンドポイントは別途指定します。認証情報、クエリ、フラグメントを含まない、`/plugins/mcp/api.php` で終わる HTTPS URL である必要があります:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` は `CACTI_MCP_ENDPOINT` の代わりにエンドポイントを指定します。`--allow-loopback-http` はローカルテスト用に `localhost`、`127.0.0.1`、または `::1` への平文 HTTP を許可します。`--lang LOCALE` は CLI メッセージのローカライズを上書きし、`--version` はバージョンを表示します。エンドポイントと `CACTI_MCP_TOKEN` の両方が指定されていない場合、コマンドは使用法エラーで終了します。

### ローカライズ

CLI のヘルプおよびアダプターのエラーメッセージは、追加の依存関係なしで 45 ロケール（`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`）に対応しています。ロケールの解決は `--lang`、次に `LC_ALL`、`LC_MESSAGES`、`LANG` の順に確認し、`en` にフォールバックします（`C`/`POSIX` および未知のタグも `en` に解決されます）。MCP ツール名、スキーマ、成功時の JSON ツールペイロードは影響を受けません。`is_error=True` で返されるアダプターのエラーメッセージは有効なロケールに従います。

プロセスは標準入力（stdin）で MCP メッセージを待機します。通常は MCP クライアントが起動します。一般的な `mcpServers` 設定形式を受け付けるクライアントでは次のように設定します:

```json
{
  "mcpServers": {
    "cacti": {
      "command": "uv",
      "args": ["run", "--locked", "--directory", "/absolute/path/cacti-mcp", "cacti-mcp"]
    }
  }
}
```

環境変数またはシークレット機能を通じて `CACTI_MCP_ENDPOINT` と `CACTI_MCP_TOKEN` をサブプロセスに渡すようにクライアントを設定してください。環境変数の継承はクライアントに依存します。トークンを指定するコマンドラインフラグはありません。

個別にインストール可能な Python ディストリビューションは `cacti-mcp` コンソールコマンドを提供します。チェックアウトを実行するために PyPI への公開は不要です。PHP プラグインに Python への依存関係はありません。

## リリース

ディストリビューションのバージョンは [pyproject.toml](../../../pyproject.toml) に記載されています。タグ付きリリースが利用可能になるまでは、ソースチェックアウトまたは成功した [CI 実行](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) の `python-distributions` アーティファクトを使用してください。アーティファクトには wheel とソースアーカイブが含まれています。インストールされたパッケージは `cacti-mcp` コマンドと `python -m cacti_mcp` の両方を提供しますが、PHP プラグインは含まれません。

## 開発とテスト

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

テストでは HTTP 検証、認証情報の分離、Bearer のみのリクエスト、ページング、エラーの秘匿化、およびフィクスチャ HTTP サーバーに対する実際の SDK クライアント/サーバー間のサブプロセス通信をカバーしています。稼働中の Cacti 環境は不要です。

このリポジトリは `src/cacti_mcp/`、pytest、Ruff、uv、Hatchling を使用しています。CI では Python 3.12、3.13、3.14 をテストします。別のパッケージングジョブでは wheel とソースアーカイブをビルドし、チェックアウト外に wheel をインストールして両方のエントリーポイントのスモークテストを行います。ディストリビューションとテスト結果はワークフローのアーティファクトとして保存されます。

## コントリビューション

プルリクエストは `develop` ブランチ宛てに送ってください。アダプターの Python 3.12 互換性を維持し、既存の Ruff 設定と `src/cacti_mcp/` パッケージ構成に従い、標準出力（stdout）を MCP メッセージ専用に保ってください。変更したトランスポートまたはツール動作に対するテストを追加し、上記のチェックを実行したうえで、`git commit -s` でコミットに署名してください。API の変更は Cacti MCP プラグインと調整し、[docs/api.md](../../../docs/api.md) を更新してください。

## ライセンス

Copyright (C) 2026 Thomas Vincent. GNU General Public License バージョン 2 以降の下で公開されています。詳細は [LICENSE](../../../LICENSE) を参照してください。
