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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · **한국어** · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP는 [Cacti MCP 플러그인](https://github.com/somethingwithproof/plugin_mcp)의 기능을 stdio 기반 MCP 도구로 노출하는 Python 어댑터입니다. 이 플러그인은 이미 HTTP를 통해 MCP를 직접 제공하므로, 클라이언트가 원격 서버에 연결할 수 있는 경우에는 해당 방식을 사용하세요. 이 어댑터는 stdio만 지원하는 클라이언트를 위한 것입니다. 공식 Python MCP SDK를 사용하며, 도구 호출을 플러그인의 HTTPS API(abilities contract v2, `/v1/` 경로에서 제공, Bearer 토큰 전용)로 변환합니다. 인증, 권한 부여, 검증 및 실행은 Cacti가 담당합니다.

**상태: 개발 중, 1.0 이전 버전.** 버전 0.1.0은 함께 제공되는 [Cacti MCP 플러그인](https://github.com/somethingwithproof/plugin_mcp)을 통해 읽기 전용 장치 인벤토리 및 설치 버전 조회를 지원합니다. 아직 태그된 릴리스는 없습니다. Doctor 진단 및 복구 기능은 향후 작업으로 예정되어 있습니다.

## 노출되는 기능

| 작업 | Cacti MCP 플러그인이 제공하는 MCP 도구 |
|---|---|
| 토큰 소유자가 볼 수 있는 장치 목록 조회 | `cacti-list-devices` |
| 허용된 단일 장치 정보 조회 | `cacti-get-device` |
| Cacti, 플러그인 및 API 버전 조회 | `cacti-get-system-info` |

이름, 설명 및 입력 스키마는 Cacti의 권한 필터링된 검색(discovery) 응답에서 가져옵니다. Python 도구 핸들러를 추가하지 않고도 허용된 추가 읽기 전용 공급자를 검색할 수 있습니다.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## 사용 사례

MCP 클라이언트를 연결하여 전용 사용자가 볼 수 있는 Cacti 장치 목록을 조회하거나, 허용된 단일 장치를 검색하거나, 사용자에게 필요한 관리 영역(realm) 권한이 있는 경우 설치 버전을 가져올 수 있습니다. 이름과 입력 스키마는 플러그인의 검색 응답에서 가져오므로 어댑터가 각 공급자를 중복 정의하지 않습니다. 등록 모델과 현재 제한 사항은 플러그인의 [기능 등록 규칙](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)을 참조하세요.

## 코드 및 테스트 맵

| 동작 | 구현 | 이 저장소의 테스트 근거 |
|---|---|---|
| HTTPS 검증, 제한, Bearer 전용 인증 및 v2 페이징 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP 검색, 호출 및 권한 변경 | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| 명령줄 도움말, 버전 및 설정 누락 처리 | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

하위 프로세스 테스트는 픽스처 HTTP 엔드포인트와 함께 실제 SDK 클라이언트 및 서버를 사용합니다. 이는 실제 Cacti 통합 검사를 요구하거나 대체하지 않습니다.

## 안전성 유지 방식

- 초기화, 도구 검색, 호출 및 stdio 프레이밍에 공식 [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)를 사용합니다.
- 어노테이션이 정확히 읽기 전용, 비파괴적(non-destructive), 멱등성(idempotent)인 기능만 노출합니다. 스키마와 이름은 Cacti에서 가져오며, 어댑터에는 SQL, 장치 자격 증명 또는 복구 명령이 포함되어 있지 않습니다.
- 쿠키나 CSRF 단계 없이 Bearer 토큰만 전송합니다. 플러그인은 모든 요청에서 토큰 유효성과 권한을 다시 확인합니다.
- 검증된 HTTPS를 사용하며, 쿠키를 저장하지 않고, 리디렉션을 거부하며, 프록시 환경 변수를 무시합니다. HTTP를 사용하려면 `--allow-loopback-http`와 리터럴 루프백 주소 또는 `localhost`가 필요합니다.
- API 호출은 전체 35초, 연결 5초, 네트워크 비활성 30초, 응답당 약 1 MB(1,100,000바이트)로 제한됩니다. 요청 본문은 16,384바이트로 제한됩니다. 호출은 클라이언트 세션별로 직렬화됩니다.
- 전송 전 마지막 검색에서 얻은 입력 스키마와 비교하여 도구 인수를 확인하고, 검증된 카탈로그의 ID만 실행합니다. 불일치가 발생하거나 서버에서 잘못된 스키마가 반환되면 충돌 대신 도구 오류로 반환됩니다.
- 실행을 자동으로 재시도하지 않습니다. 도구 오류에는 HTTP 상태, AIP-193 `status` 및 ErrorInfo `reason`만 포함되며, 서버 메시지 텍스트, 응답 본문 또는 자격 증명은 절대 포함되지 않습니다. Stdout은 MCP 메시지 전용으로 예약되어 있습니다.

SDK 버전은 `uv.lock`에 고정되어 있습니다(`pyproject.toml`의 `mcp>=2.3,<3`). 이 어댑터는 stdio 전송과 함께 2.x 저수준 서버를 사용하며, 원격 MCP HTTP 엔드포인트, OAuth, 리소스, 프롬프트, 구독 또는 백그라운드 작업은 구현하지 않습니다.

자세한 내용은 [API 계약](../../../docs/api.md) 및 [구현 계획](../../../docs/plan.md)을 참조하세요.

## 설치 및 명령줄

Python 3.12 이상과 [uv](https://docs.astral.sh/uv/)가 필요합니다. 이 저장소의 체크아웃 디렉터리에서 다음을 실행하세요:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

PHP 플러그인을 설치하고 활성화한 후 전용 Cacti 사용자에게 해당 영역(realm) 권한을 부여하고, 플러그인 콘솔, My MCP Tokens 페이지 또는 `tokens.php` 명령을 사용하여 해당 사용자의 개인 액세스 토큰(형식: `cmcp_pat_` 뒤에 소문자 16진수 64자리)을 생성합니다. 사용자의 기존 Cacti 영역 및 장치 권한은 계속 적용됩니다.

비밀 관리자를 통해 `CACTI_MCP_TOKEN`으로 토큰을 제공하세요. 소스 제어나 명령 인수에 토큰을 절대 추가하지 마세요. 엔드포인트는 별도로 설정합니다. 자격 증명, 쿼리 또는 프래그먼트 없이 `/plugins/mcp/api.php`로 끝나는 HTTPS URL이어야 합니다:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL`은 `CACTI_MCP_ENDPOINT` 대신 엔드포인트를 설정합니다. `--allow-loopback-http`는 로컬 테스트를 위해 `localhost`, `127.0.0.1` 또는 `::1`로의 일반 HTTP를 허용하며, `--lang LOCALE`은 CLI 메시지 지역화를 재정의하고, `--version`은 버전을 출력합니다. 엔드포인트와 `CACTI_MCP_TOKEN`이 모두 없으면 명령은 사용법 오류와 함께 종료됩니다.

### 지역화

CLI 도움말과 어댑터 오류 메시지는 추가 종속성 없이 45개 로캘(`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`)로 제공됩니다. 로캘 확인은 `--lang`, `LC_ALL`, `LC_MESSAGES`, `LANG` 순서로 확인하며 기본값은 `en`입니다(`C`/`POSIX` 및 알 수 없는 태그도 `en`으로 확인됨). MCP 도구 이름, 스키마 및 성공적인 JSON 도구 페이로드는 영향을 받지 않으며, `is_error=True`와 함께 반환되는 어댑터 오류 메시지는 활성 로캘을 따릅니다.

프로세스는 stdin에서 MCP 메시지를 기다립니다. 일반적으로 MCP 클라이언트가 이를 실행합니다. 일반적인 `mcpServers` 구성 형식을 지원하는 클라이언트의 경우:

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

클라이언트가 환경 변수 또는 비밀 관리 기능을 통해 하위 프로세스에 `CACTI_MCP_ENDPOINT` 및 `CACTI_MCP_TOKEN`을 전달하도록 구성하세요. 환경 상속 방식은 클라이언트에 따라 다릅니다. 토큰용 명령줄 플래그는 없습니다.

별도로 설치 가능한 Python 배포판은 `cacti-mcp` 콘솔 명령을 제공합니다. 체크아웃을 실행하는 데 PyPI 배포는 필요하지 않습니다. PHP 플러그인에는 Python 종속성이 없습니다.

## 릴리스

배포 버전은 [pyproject.toml](../../../pyproject.toml)에 기록되어 있습니다. 태그된 릴리스가 제공되기 전까지는 소스 체크아웃 또는 성공한 [CI 실행](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml)의 `python-distributions` 아티팩트를 사용하세요. 아티팩트에는 wheel과 소스 아카이브가 포함되어 있습니다. 설치된 패키지는 `cacti-mcp` 명령과 `python -m cacti_mcp`를 모두 제공하며, PHP 플러그인은 포함하지 않습니다.

## 개발 및 테스트

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

테스트는 HTTP 검증, 자격 증명 격리, Bearer 전용 요청, 페이징, 오류 마스킹(redaction), 그리고 픽스처 HTTP 서버를 대상으로 하는 실제 SDK 클라이언트/서버 하위 프로세스 교환을 다룹니다. 실제 Cacti 설치 환경은 필요하지 않습니다.

이 저장소는 `src/cacti_mcp/`, pytest, Ruff, uv 및 Hatchling을 사용합니다. CI는 Python 3.12, 3.13 및 3.14를 테스트합니다. 별도의 패키징 작업이 wheel과 소스 아카이브를 빌드하고, 체크아웃 외부에 wheel을 설치하며, 두 진입점을 모두 스모크 테스트합니다. 배포판과 테스트 결과는 워크플로 아티팩트입니다.

## 기여

Pull Request는 `develop` 브랜치로 보내주세요. Python 3.12와의 호환성을 유지하고, 기존 Ruff 설정 및 `src/cacti_mcp/` 패키지 레이아웃을 따르며, stdout은 MCP 메시지 전용으로 유지해야 합니다. 변경된 전송 또는 도구 동작에 대한 테스트를 추가하고, 위의 검사를 실행하며, `git commit -s`로 커밋에 서명(sign off)하세요. API 변경 사항은 Cacti MCP 플러그인과 조율하고 [docs/api.md](../../../docs/api.md)를 업데이트하세요.

## 라이선스

Copyright (C) 2026 Thomas Vincent. GNU General Public License 버전 2 이상에 따라 배포됩니다. 자세한 내용은 [LICENSE](../../../LICENSE)를 참조하세요.
