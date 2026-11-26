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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · **繁體中文** · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP 是一個 Python 配接器，可透過 stdio 將 [Cacti MCP 外掛程式](https://github.com/somethingwithproof/plugin_mcp) 的功能公開為 MCP 工具。該外掛程式本身已能透過 HTTP 直接提供 MCP 服務，若您的用戶端可連線至遠端伺服器，請直接使用該方式；本配接器專為僅支援 stdio 通訊的用戶端設計。本工具採用官方 Python MCP SDK，並將工具呼叫轉換為該外掛程式的 HTTPS API（abilities 合約 v2，於 `/v1/` 路徑提供服務，僅支援 Bearer 權杖驗證）。身分驗證、授權、資料檢核與執行皆由 Cacti 負責。

**狀態：開發中，尚未達 1.0 版。** 0.1.0 版透過搭配的 [Cacti MCP 外掛程式](https://github.com/somethingwithproof/plugin_mcp) 支援唯讀的裝置清冊與安裝版本查詢。目前尚未發佈帶有標籤的正式版本。Doctor 診斷與修復功能為未來規劃項目。

## 提供的功能

| 操作項目 | 由 Cacti MCP 外掛程式提供的 MCP 工具 |
|---|---|
| 列出權杖擁有者可檢視的裝置 | `cacti-list-devices` |
| 讀取單一已授權裝置 | `cacti-get-device` |
| 讀取 Cacti、外掛程式與 API 版本 | `cacti-get-system-info` |

名稱、描述與輸入結構描述（input schema）皆來自 Cacti 依權限過濾後的探索回應。無須新增 Python 工具處理常式，即可探索其他已授權的唯讀提供者。

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## 使用情境

連線 MCP 用戶端以列出其專用使用者有權檢視的 Cacti 裝置、查詢單一已授權裝置，或在使用者具備所需管理領域權限時擷取安裝版本資訊。名稱與輸入結構描述皆來自外掛程式的探索回應，因此配接器不會重複實作各個提供者。有關註冊模型與目前限制，請參閱該外掛程式的 [ability 註冊規則](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)。

## 程式碼與測試對照

| 行為 | 實作檔案 | 此儲存庫中的測試佐證 |
|---|---|---|
| HTTPS 驗證、邊界限制、僅限 Bearer 驗證與 v2 分頁 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP 探索、呼叫與權限變更 | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| 命令列說明、版本與缺少設定處理 | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

子處理程序測試使用真實的 SDK 用戶端與伺服器搭配模擬 HTTP 端點，不需要也不會取代實際的 Cacti 整合檢查。

## 安全性設計

- 使用官方 [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) 處理初始化、工具探索、呼叫與 stdio 框架封裝。
- 僅公開註記完全符合唯讀、非破壞性且具冪等性的功能。結構描述與名稱皆來自 Cacti；配接器本身不包含任何 SQL、裝置憑證或修復指令。
- 僅傳送 Bearer 權杖：不使用 Cookie，也不執行 CSRF 步驟。外掛程式會在每次請求時重新檢查權杖有效性與權限。
- 使用經憑證驗證的 HTTPS、從不儲存 Cookie、拒絕重新導向，並忽略代理環境變數。若使用 HTTP，必須指定 `--allow-loopback-http` 且目標僅限明確的回送位址或 `localhost`。
- 對 API 呼叫設定邊界限制：總逾時 35 秒、連線逾時 5 秒、網路無活動逾時 30 秒，且單次回應上限約 1 MB（1,100,000 位元組）。請求主體上限為 16,384 位元組。每個用戶端工作階段的呼叫皆會依序執行。
- 傳送前會依據最近一次探索取得的輸入結構描述檢查工具引數，並僅執行該已驗證目錄中的 ID。若參數不符或伺服器回傳格式錯誤的結構描述，將回傳工具錯誤而非造成程式當機。
- 不會自動重試執行。工具錯誤僅包含 HTTP 狀態碼、AIP-193 `status` 與 ErrorInfo `reason`，絕不包含伺服器訊息文字、回應主體或憑證。Stdout 保留專供 MCP 訊息使用。

SDK 版本已由 `uv.lock` 鎖定（`pyproject.toml` 中為 `mcp>=2.3,<3`）。本配接器使用其 2.x 低階伺服器搭配 stdio 傳輸層；未實作遠端 MCP HTTP 端點、OAuth、resources、prompts、訂閱或背景工作。

請參閱 [API 合約](../../../docs/api.md) 與 [實作計畫](../../../docs/plan.md)。

## 安裝與命令列操作

需要 Python 3.12 或更新版本與 [uv](https://docs.astral.sh/uv/)。
在此儲存庫的簽出複本中執行：

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

請安裝並啟用 PHP 外掛程式，將其權限領域授予專用的 Cacti 使用者，並在該外掛程式的主控台、My MCP Tokens 頁面或使用其 `tokens.php` 指令為該使用者建立個人存取權杖（格式為 `cmcp_pat_` 後接 64 個小寫十六進位字元）。該使用者原有的 Cacti 權限領域與裝置權限仍維持適用。

請透過您的密鑰管理員以 `CACTI_MCP_TOKEN` 提供權杖，切勿將其加入版本控制或命令列引數。端點須另外設定，且必須為以 `/plugins/mcp/api.php` 結尾的 HTTPS URL，不得包含憑證、查詢字串或片段識別碼：

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` 可取代 `CACTI_MCP_ENDPOINT` 設定端點。`--allow-loopback-http` 允許針對 `localhost`、`127.0.0.1` 或 `::1` 使用純 HTTP 進行本機測試，`--lang LOCALE` 可覆寫 CLI 訊息語系，而 `--version` 會印出版本號。若缺少端點或 `CACTI_MCP_TOKEN`，指令將以使用方式錯誤結束。

### 在地化

CLI 說明與配接器錯誤訊息內建支援 45 種語系（`en`、`de`、`es`、`fr`、`it`、`pt-BR`、`nl`、`ru`、`uk`、`ja`、`ko`、`zh-CN`、`zh-TW`、`ar`、`hi`、`pl`、`tr`、`sv`、`vi`、`id`、`af-ZA`、`am-ET`、`ar-EG`、`ar-MA`、`fr-MA`、`fr-SN`、`ha-NG`、`ig-NG`、`mg-MG`、`rw-RW`、`so-SO`、`sw-KE`、`xh-ZA`、`yo-NG`、`zu-ZA`、`bn`、`fa`、`he`、`mr`、`ta`、`te`、`th`、`ur`、`ms`、`fil`），無須額外相依套件。語系解析順序為檢查 `--lang`，接著是 `LC_ALL`、`LC_MESSAGES` 與 `LANG`，最後備援至 `en`（`C`/`POSIX` 與未知標籤亦解析為 `en`）。MCP 工具名稱、結構描述與成功的 JSON 工具酬載不受影響；當回傳 `is_error=True` 時，配接器錯誤訊息會依作用中的語系顯示。

處理程序會在 stdin 等待 MCP 訊息，通常由 MCP 用戶端啟動。針對接受常見 `mcpServers` 設定格式的用戶端：

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

請設定用戶端透過環境變數或密鑰機制將 `CACTI_MCP_ENDPOINT` 與 `CACTI_MCP_TOKEN` 傳遞給子處理程序。環境變數的繼承方式取決於用戶端實作，本工具不提供透過命令列旗標傳入權杖的功能。

可獨立安裝的 Python 發行套件提供 `cacti-mcp` 主控台指令。執行本機簽出複本無須透過 PyPI 發佈。PHP 外掛程式本身沒有 Python 相依性。

## 發佈版本

發行版本號記錄於 [pyproject.toml](../../../pyproject.toml)。在有正式標籤版本前，請使用原始碼簽出複本，或使用成功執行的 [CI 工作流程](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) 中的 `python-distributions` 產物。該產物包含 wheel 與原始碼封存檔。安裝後的套件同時提供 `cacti-mcp` 指令與 `python -m cacti_mcp`；其中不包含 PHP 外掛程式。

## 開發與測試

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

測試涵蓋 HTTP 驗證、憑證隔離、僅限 Bearer 請求、分頁、錯誤敏感資訊遮罩，以及針對模擬 HTTP 伺服器進行的實際 SDK 用戶端／伺服器子處理程序互動。測試無須連線至實際的 Cacti 安裝環境。

本儲存庫使用 `src/cacti_mcp/`、pytest、Ruff、uv 與 Hatchling。CI 會測試 Python 3.12、3.13 與 3.14。另有獨立的封裝工作會建置 wheel 與原始碼封存檔，在簽出目錄外部安裝 wheel，並對兩個進入點執行冒煙測試。發行套件與測試結果皆作為工作流程產物保存。

## 參與貢獻

Pull Request 請發送至 `develop` 分支。請維持配接器對 Python 3.12 的相容性、遵循現有的 Ruff 設定與 `src/cacti_mcp/` 套件結構，並確保 stdout 專供 MCP 訊息使用。請為變更的傳輸或工具行為新增測試、執行上述檢查，並使用 `git commit -s` 簽署提交。API 變更請與 Cacti MCP 外掛程式協調，並同步更新 [docs/api.md](../../../docs/api.md)。

## 授權條款

Copyright (C) 2026 Thomas Vincent. 本專案依 GNU General Public License 第 2 版或更新版本條款釋出。詳情請參閱 [LICENSE](../../../LICENSE)。
