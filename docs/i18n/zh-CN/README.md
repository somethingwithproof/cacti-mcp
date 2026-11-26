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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · **简体中文** · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP 是一个 Python 适配器，用于通过 stdio 将 [Cacti MCP 插件](https://github.com/somethingwithproof/plugin_mcp)的功能暴露为 MCP 工具。该插件本身已直接支持通过 HTTP 提供 MCP 服务，因此当你的客户端能够连接到远程服务器时，请直接使用插件的 HTTP 服务。本适配器专为仅支持 stdio 的客户端而设计。它使用官方 Python MCP SDK，并将工具调用转换为插件的 HTTPS API（能力契约 v2，提供于 `/v1/` 路径下，仅限 Bearer 令牌认证）。身份认证、授权、校验和执行均由 Cacti 负责。

**状态：开发中，尚未发布 1.0。** 0.1.0 版本通过配套的 [Cacti MCP 插件](https://github.com/somethingwithproof/plugin_mcp)支持只读设备清单和安装版本查询。目前尚未有带标签的正式发布版本。Doctor 诊断和修复功能属于后续规划。

## 暴露的功能

| 操作 | 由 Cacti MCP 插件提供的 MCP 工具 |
|---|---|
| 列出令牌所有者有权查看的设备 | `cacti-list-devices` |
| 读取单个有权限的设备 | `cacti-get-device` |
| 读取 Cacti、插件和 API 版本 | `cacti-get-system-info` |

工具名称、描述和输入 schema 均来自 Cacti 经过权限过滤的发现响应。无需添加 Python 工具处理程序即可发现其他获准使用的只读提供程序。

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## 使用场景

连接 MCP 客户端以列出其专用用户有权查看的 Cacti 设备、查询单个有权限的设备，或在用户拥有所需管理权限域时获取安装版本信息。名称和输入 schema 来自插件的发现响应，因此适配器不会重复定义各个提供程序。有关注册模型和当前限制，请参阅插件的[能力注册规则](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)。

## 代码与测试映射

| 行为 | 实现 | 本仓库中的测试证据 |
|---|---|---|
| HTTPS 校验、边界限制、仅 Bearer 认证及 v2 分页 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP 发现、调用及权限变更 | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| 命令行帮助、版本及缺失配置处理 | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

子进程测试使用真实的 SDK 客户端和服务端以及测试夹具 HTTP 端点，不需要也无法替代针对实际 Cacti 环境的集成检查。

## 安全保障机制

- 使用官方 [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) 处理初始化、工具发现、调用和 stdio 帧封装。
- 仅暴露注解严格为只读、非破坏性且幂等的能力。Schema 和名称均来自 Cacti；适配器本身不包含任何 SQL、设备凭据或修复命令。
- 仅发送 Bearer 令牌：不使用 Cookie，也无需 CSRF 步骤。插件会在每次请求时重新校验令牌有效性和权限。
- 使用经过验证的 HTTPS，从不存储 Cookie，拒绝重定向，并忽略代理环境变量。使用 HTTP 需要指定 `--allow-loopback-http` 且目标必须是字面量回环地址或 `localhost`。
- 对 API 调用设置了严格边界：总超时 35 秒、连接超时 5 秒、网络无活动超时 30 秒，以及每次响应约 1 MB 的大小限制（1,100,000 字节）。请求体限制为 16,384 字节。每个客户端会话内的调用按顺序串行执行。
- 在发送参数前，依据上一次发现获取的输入 schema 校验工具参数，并仅执行该已验证目录中的 ID。参数不匹配或服务器返回格式错误的 schema 时，会以工具错误形式返回，而不会导致崩溃。
- 不会自动重试执行。工具错误仅携带 HTTP 状态码、AIP-193 `status` 和 ErrorInfo `reason`，绝不包含服务器消息文本、响应体或凭据。Stdout 专用于传输 MCP 消息。

SDK 版本通过 `uv.lock` 锁定（`pyproject.toml` 中为 `mcp>=2.3,<3`）。本适配器使用其 2.x 底层服务端及 stdio 传输方式；未实现远程 MCP HTTP 端点、OAuth、资源（resources）、提示词（prompts）、订阅或后台任务。

请参阅 [API 契约](../../../docs/api.md)和[实现计划](../../../docs/plan.md)。

## 安装与命令行使用

需要 Python 3.12 或更高版本以及 [uv](https://docs.astral.sh/uv/)。在本仓库的检出目录中执行：

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

安装并启用该 PHP 插件，将其权限域授予专用的 Cacti 用户，然后在插件控制台、其 My MCP Tokens 页面或使用其 `tokens.php` 命令为该用户创建个人访问令牌（格式为 `cmcp_pat_` 后跟 64 位小写十六进制数字）。该用户原有的 Cacti 权限域和设备权限依然有效。

通过密钥管理器以 `CACTI_MCP_TOKEN` 环境变量提供该令牌；切勿将其写入源代码控制或命令行参数中。单独设置端点地址，它必须是以 `/plugins/mcp/api.php` 结尾的 HTTPS URL，且不得包含凭据、查询参数或片段标识：

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` 用于替代 `CACTI_MCP_ENDPOINT` 设置端点地址。`--allow-loopback-http` 允许在本地测试时对 `localhost`、`127.0.0.1` 或 `::1` 使用明文 HTTP，`--lang LOCALE` 用于覆盖 CLI 消息本地化语言，`--version` 用于打印版本号。如果未同时提供端点和 `CACTI_MCP_TOKEN`，命令将以用法错误退出。

### 本地化

CLI 帮助和适配器错误消息内置 45 种语言区域支持（`en`、`de`、`es`、`fr`、`it`、`pt-BR`、`nl`、`ru`、`uk`、`ja`、`ko`、`zh-CN`、`zh-TW`、`ar`、`hi`、`pl`、`tr`、`sv`、`vi`、`id`、`af-ZA`、`am-ET`、`ar-EG`、`ar-MA`、`fr-MA`、`fr-SN`、`ha-NG`、`ig-NG`、`mg-MG`、`rw-RW`、`so-SO`、`sw-KE`、`xh-ZA`、`yo-NG`、`zu-ZA`、`bn`、`fa`、`he`、`mr`、`ta`、`te`、`th`、`ur`、`ms`、`fil`），无需任何额外依赖。语言区域解析依次检查 `--lang`、`LC_ALL`、`LC_MESSAGES` 和 `LANG`，最后回退到 `en`（`C`/`POSIX` 及未知标签也会解析为 `en`）。MCP 工具名称、schema 和成功的 JSON 工具载荷不受影响；以 `is_error=True` 返回的适配器错误消息会遵循当前激活的语言区域。

进程会在 stdin 上等待 MCP 消息，通常由 MCP 客户端启动。对于支持常见 `mcpServers` 配置格式的客户端：

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

请配置客户端，通过其环境或密钥管理机制向子进程传递 `CACTI_MCP_ENDPOINT` 和 `CACTI_MCP_TOKEN`。环境变量的继承方式取决于客户端本身。本工具没有用于传递令牌的命令行参数。

可单独安装的 Python 分发包提供 `cacti-mcp` 控制台命令。无需发布到 PyPI 即可从检出目录运行。该 PHP 插件不依赖 Python。

## 发布版本

分发包版本号记录在 [pyproject.toml](../../../pyproject.toml) 中。在提供带标签的正式发布版本之前，请使用源码检出目录，或使用成功的 [CI 运行](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml)中产出的 `python-distributions` 构建产物。该产物包含 wheel 包和源码归档包。安装后的软件包同时提供 `cacti-mcp` 命令和 `python -m cacti_mcp` 入口；其中不包含 PHP 插件。

## 开发与测试

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

测试涵盖 HTTP 校验、凭据隔离、仅 Bearer 请求、分页、错误脱敏，以及针对测试夹具 HTTP 服务器的真实 SDK 客户端/服务端子进程交互。这些测试不依赖实际运行的 Cacti 实例。

本仓库使用 `src/cacti_mcp/` 目录结构、pytest、Ruff、uv 和 Hatchling。CI 会测试 Python 3.12、3.13 和 3.14。独立的打包任务会构建 wheel 包和源码归档包，在检出目录之外安装 wheel 包，并对两个入口点进行冒烟测试。分发包和测试结果均作为工作流产物保留。

## 贡献指南

请将 Pull Request 提交至 `develop` 分支。请保持适配器兼容 Python 3.12，遵循现有的 Ruff 配置和 `src/cacti_mcp/` 包布局，并确保 stdout 专用于 MCP 消息。修改传输或工具行为时请补充测试，运行上述检查，并使用 `git commit -s` 对提交进行签名确认（DCO sign-off）。涉及 API 变更时请与 Cacti MCP 插件协同更新，并同步修改 [docs/api.md](../../../docs/api.md)。

## 许可证

Copyright (C) 2026 Thomas Vincent。基于 GNU General Public License 第 2 版或更高版本发布。详见 [LICENSE](../../../LICENSE)。
