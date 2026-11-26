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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · **አማርኛ** · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP የ[Cacti MCP ፕለጊን](https://github.com/somethingwithproof/plugin_mcp) ችሎታዎችን በstdio በኩል እንደ MCP መሣሪያዎች የሚያቀርብ የPython አዳፕተር ነው። ፕለጊኑ ቀድሞውኑ MCPን በHTTP በኩል በቀጥታ ስለሚያገለግል፣ ደንበኛዎ ከሩቅ አገልጋይ ጋር መገናኘት ሲችል ያንን ይጠቀሙ። ይህ አዳፕተር በstdio ብቻ ለሚነጋገሩ ደንበኞች የታሰበ ነው። ይፋዊውን የPython MCP SDK ይጠቀማል እንዲሁም የመሣሪያ ጥሪዎችን ወደ ፕለጊኑ HTTPS API (abilities contract v2፣ በ`/v1/` መንገዶች ሥር የሚቀርብ፣ bearer token ብቻ) ይተረጉማል።
የማንነት ማረጋገጫ፣ የፈቃድ ቁጥጥር፣ ማረጋገጥ እና አፈጻጸም በCacti ቁጥጥር ሥር ናቸው።

**ሁኔታ: በልማት ላይ፣ ከ1.0 በፊት።** ስሪት 0.1.0 ከአጃቢው [Cacti MCP ፕለጊን](https://github.com/somethingwithproof/plugin_mcp) ጋር በመሆን ለንባብ ብቻ የሚሆን የመሣሪያዎች ዝርዝር እና የመጫኛ ስሪቶችን ይደግፋል። እስካሁን መለያ የተሰጠው ልቀት የለም። የDoctor ምርመራዎች እና ጥገናዎች የወደፊት ሥራዎች ናቸው።

## የሚያቀርባቸው መሣሪያዎች

| ክዋኔ | በCacti MCP ፕለጊን የሚቀርብ የMCP መሣሪያ |
|---|---|
| የቶከኑ ባለቤት ማየት የሚችላቸውን መሣሪያዎች መዘርዘር | `cacti-list-devices` |
| አንድ የተፈቀደ መሣሪያ ማንበብ | `cacti-get-device` |
| የCacti፣ የፕለጊን እና የAPI ስሪቶችን ማንበብ | `cacti-get-system-info` |

ስሞች፣ መግለጫዎች እና የግቤት ንድፎች የሚመጡት በፈቃድ ከተጣራው የCacti የግኝት ምላሽ ነው። ተጨማሪ የተፈቀዱ ለንባብ ብቻ የሚሆኑ አቅራቢዎች የPython መሣሪያ ተቆጣጣሪዎችን ሳይጨምሩ ሊገኙ ይችላሉ።

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## የአጠቃቀም ሁኔታዎች

የተወሰነ ተጠቃሚው ማየት የሚችላቸውን የCacti መሣሪያዎች ለመዘርዘር፣ አንድ የተፈቀደ መሣሪያ ለመፈለግ፣ ወይም ተጠቃሚው የሚያስፈልገው የአስተዳደር ክልል ሲኖረው የመጫኛ ስሪቶችን ለማምጣት የMCP ደንበኛን ያገናኙ። ስሞች እና የግቤት ንድፎች የሚመጡት ከፕለጊኑ የግኝት ምላሽ ስለሆነ፣ አዳፕተሩ እያንዳንዱን አቅራቢ አይደግምም።
ስለ ምዝገባ ሞዴሉ እና ወቅታዊ ገደቦች የፕለጊኑን [የችሎታ ምዝገባ ደንቦች](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) ይመልከቱ።

## የኮድ እና የሙከራ ካርታ

| ባህሪ | አተገባበር | በዚህ ማከማቻ ውስጥ ያለ የሙከራ ማስረጃ |
|---|---|---|
| የHTTPS ማረጋገጫ፣ ገደቦች፣ bearer-only ማንነት ማረጋገጫ እና የv2 ገጽ ክፍፍል | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| የMCP ግኝት፣ ጥሪዎች እና የፈቃድ ለውጦች | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| የትእዛዝ መስመር እገዛ፣ ስሪት እና የጎደለ ውቅር | [server.py](../../../src/cacti_mcp/server.py)፣ [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

የንዑስ ሂደት ሙከራው እውነተኛ የSDK ደንበኛ እና አገልጋይን ከሙከራ የHTTP መድረሻ ጋር ይጠቀማል። ቀጥታ የCacti ውህደት ፍተሻን አይጠይቅም እንዲሁም አይተካውም።

## ደህንነቱን እንዴት እንደሚጠብቅ

- ለመጀመሪያ ዝግጅት፣ ለመሣሪያ ግኝት፣ ለጥሪዎች እና ለstdio ክፈፍ ሥራ ይፋዊውን [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) ይጠቀማል።
- ማብራሪያዎቻቸው በትክክል ለንባብ ብቻ የሚሆኑ፣ የማያጠፉ እና ተደጋጋሚ ውጤት የማይቀይሩ ችሎታዎችን ብቻ ያቀርባል። ንድፎች እና ስሞች ከCacti ይመጣሉ፤ አዳፕተሩ ምንም SQL፣ የመሣሪያ ምስጢራዊ መረጃዎች ወይም የጥገና ትእዛዞችን አልያዘም።
- bearer token ብቻ ይልካል: ምንም ኩኪዎች የሉም፣ ምንም የCSRF እርምጃ የለም። ፕለጊኑ በእያንዳንዱ ጥያቄ ላይ የቶከኑን ትክክለኛነት እና ፈቃዶች እንደገና ይፈትሻል።
- የተረጋገጠ HTTPS ይጠቀማል፣ ኩኪዎችን በፍጹም አያስቀምጥም፣ አቅጣጫ ማዞሪያዎችን አይቀበልም እንዲሁም የproxy አካባቢ ተለዋዋጮችን ችላ ይላል። HTTP ለመጠቀም `--allow-loopback-http` እና ቀጥተኛ የloopback አድራሻ ወይም `localhost` ያስፈልጋል።
- የAPI ጥሪዎችን በአጠቃላይ በ35 ሰከንድ፣ ለመገናኘት በ5 ሰከንድ፣ በአውታረ መረብ እንቅስቃሴ-አልባነት በ30 ሰከንድ እና በአንድ ምላሽ በግምት በ1 MB (1,100,000 ባይት) ይገድባል። የጥያቄ አካላት በ16,384 ባይት የተገደቡ ናቸው። ጥሪዎች በእያንዳንዱ የደንበኛ ክፍለ ጊዜ በተከታታይ ይፈጸማሉ።
- የመሣሪያ መለኪያዎችን ከመላኩ በፊት ከመጨረሻው ግኝት ከተገኘው የግቤት ንድፍ ጋር ያረጋግጣል እንዲሁም ከዚያ ከተረጋገጠው ካታሎግ የተገኙ መለያዎችን ብቻ ያስፈጽማል። አለመጣጣም ወይም ከአገልጋዩ የመጣ የተበላሸ ንድፍ እንደ መሣሪያ ስህተት ይመለሳል እንጂ ፕሮግራሙን አያቋርጥም።
- አፈጻጸምን በራስ ሰር እንደገና አይሞክርም። የመሣሪያ ስህተቶች የHTTP ሁኔታን፣ የAIP-193 `status`ን እና የErrorInfo `reason`ን ብቻ ይይዛሉ፤ የአገልጋይ መልእክት ጽሑፍን፣ የምላሽ አካላትን ወይም ምስጢራዊ መረጃዎችን በፍጹም አይይዙም። stdout ለMCP መልእክቶች ብቻ የተጠበቀ ነው።

የSDK ስሪት በ`uv.lock` (`pyproject.toml` ውስጥ `mcp>=2.3,<3`) ተወስኗል። ይህ አዳፕተር የ2.x ዝቅተኛ-ደረጃ አገልጋዩን ከstdio ማጓጓዣ ጋር ይጠቀማል፤ የሩቅ MCP HTTP መድረሻ፣ OAuth፣ ሀብቶች፣ ጥያቄዎች፣ ምዝገባዎች ወይም የጀርባ ተግባራትን አይተገብርም።

[የAPI ውል](../../../docs/api.md) እና [የአተገባበር ዕቅድ](../../../docs/plan.md) ይመልከቱ።

## መጫን እና የትእዛዝ መስመር

Python 3.12 ወይም ከዚያ በላይ እና [uv](https://docs.astral.sh/uv/) ያስፈልጋል።
ከዚህ ማከማቻ ቅጂ ውስጥ:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

የPHP ፕለጊኑን ይጫኑ እና ያንቁ፣ ክልሉን ለተወሰነ የCacti ተጠቃሚ ይስጡ፣ እና ለዚያ ተጠቃሚ የግል መዳረሻ ቶከን (ቅርጸቱ `cmcp_pat_` ተከትሎ 64 ትንንሽ የሄክሳዴሲማል አኃዞች) በፕለጊኑ ኮንሶል፣ በMy MCP Tokens ገጹ ላይ ወይም በ`tokens.php` ትእዛዙ ይፍጠሩ።
የተጠቃሚው ነባር የCacti ክልሎች እና የመሣሪያ ፈቃዶች አሁንም ተፈጻሚ ይሆናሉ።

ቶከኑን በምስጢር አስተዳዳሪዎ በኩል እንደ `CACTI_MCP_TOKEN` ያቅርቡ፤ ወደ ምንጭ ኮድ ቁጥጥር ወይም የትእዛዝ መለኪያዎች በፍጹም አይጨምሩት። መድረሻውን ለብቻው ያዘጋጁ። በ`/plugins/mcp/api.php` የሚያበቃ የHTTPS URL መሆን አለበት፣ ምንም ምስጢራዊ መረጃ፣ መጠይቅ ወይም ቁርጥራጭ ሳይኖረው:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` በ`CACTI_MCP_ENDPOINT` ፋንታ መድረሻውን ያዘጋጃል።
`--allow-loopback-http` ለአካባቢ ሙከራ ወደ `localhost`፣ `127.0.0.1` ወይም `::1` ቀላል HTTP ይፈቅዳል፣ `--lang LOCALE` የCLI መልእክት ቋንቋን ይተካል፣ እንዲሁም `--version` ስሪቱን ያትማል። ሁለቱም መድረሻው እና `CACTI_MCP_TOKEN` ከሌሉ ትእዛዙ በአጠቃቀም ስህተት ይወጣል።

### የቋንቋ አካባቢያዊነት

የCLI እገዛ እና የአዳፕተር ስህተት መልእክቶች ምንም ተጨማሪ ጥገኝነቶች ሳይኖራቸው በ45 ቋንቋዎች (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ይቀርባሉ። የቋንቋ አመራረጥ መጀመሪያ `--lang`ን፣ ከዚያ `LC_ALL`፣ `LC_MESSAGES` እና `LANG`ን ይፈትሻል፣ ወደ `en` በመመለስ (`C`/`POSIX` እና ያልታወቁ መለያዎችም ወደ `en` ይመለሳሉ)። የMCP መሣሪያ ስሞች፣ ንድፎች እና የተሳኩ የJSON መሣሪያ መረጃዎች አይነኩም፤ በ`is_error=True` የሚመለሱ የአዳፕተር ስህተት መልእክቶች ንቁውን ቋንቋ ይከተላሉ።

ሂደቱ በstdin ላይ የMCP መልእክቶችን ይጠብቃል። አንድ የMCP ደንበኛ በተለምዶ ያስጀምረዋል።
የተለመደውን የ`mcpServers` ውቅር ቅርጸት ለሚቀበሉ ደንበኞች:

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

ደንበኛው `CACTI_MCP_ENDPOINT` እና `CACTI_MCP_TOKEN`ን በአካባቢ ተለዋዋጭ ወይም በምስጢር አገልግሎቱ በኩል ወደ ንዑስ ሂደቱ እንዲያስተላልፍ ያዋቅሩት። የአካባቢ ተለዋዋጭ ውርስ በደንበኛው ላይ ይወሰናል። ለቶከን ምንም የትእዛዝ መስመር ባንዲራ የለም።

ለብቻው የሚጫነው የPython ስርጭት የ`cacti-mcp` ኮንሶል ትእዛዝን ያቀርባል። ቅጂውን ለማስኬድ የPyPI ህትመት አያስፈልግም። የPHP ፕለጊኑ ምንም የPython ጥገኝነት የለውም።

## ልቀቶች

የስርጭት ስሪቱ በ[pyproject.toml](../../../pyproject.toml) ውስጥ ተመዝግቧል።
መለያ የተሰጣቸው ልቀቶች እስኪገኙ ድረስ የምንጭ ቅጂ ወይም ከተሳካ [የCI አፈጻጸም](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) የተገኘውን `python-distributions` ውጤት ይጠቀሙ።
ውጤቱ wheel እና የምንጭ ማህደር ይዟል። የተጫነው ጥቅል ሁለቱንም የ`cacti-mcp` ትእዛዝ እና `python -m cacti_mcp`ን ያቀርባል፤ የPHP ፕለጊኑን አልያዘም።

## ልማት እና ሙከራዎች

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

ሙከራዎቹ የHTTP ማረጋገጫን፣ የምስጢራዊ መረጃ መነጠልን፣ bearer-only ጥያቄዎችን፣ የገጽ ክፍፍልን፣ የስህተት መረጃ መደበቅን እና ከሙከራ የHTTP አገልጋይ ጋር የሚደረግ እውነተኛ የSDK ደንበኛ/አገልጋይ ንዑስ ሂደት ልውውጥን ይሸፍናሉ። ቀጥታ የCacti ጭነት አያስፈልጋቸውም።

ማከማቻው `src/cacti_mcp/`፣ pytest፣ Ruff፣ uv እና Hatchling ይጠቀማል። CI Python 3.12፣ 3.13 እና 3.14ን ይፈትሻል። የተለየ የማሸጊያ ሥራ wheel እና የምንጭ ማህደርን ይገነባል፣ wheelን ከቅጂው ውጭ ይጭናል እንዲሁም ሁለቱንም መግቢያ ነጥቦች በመሠረታዊ ሙከራ ይፈትሻል። ስርጭቶች እና የሙከራ ውጤቶች የሥራ ፍሰት ውጤቶች ናቸው።

## አስተዋጽዖ ማበርከት

የለውጥ ጥያቄዎች ወደ `develop` ይላካሉ። አዳፕተሩን ከPython 3.12 ጋር ተኳሃኝ አድርገው ይጠብቁ፣ ነባሩን የRuff ውቅር እና የ`src/cacti_mcp/` ጥቅል አቀማመጥ ይከተሉ፣ እና stdout ለMCP መልእክቶች ብቻ የተጠበቀ እንዲሆን ያድርጉ። ለተቀየረ የማጓጓዣ ወይም የመሣሪያ ባህሪ ሙከራዎችን ይጨምሩ፣ ከላይ ያሉትን ፍተሻዎች ያስኪዱ እና ኮሚቶችን በ`git commit -s` ይፈርሙ።
የAPI ለውጦችን ከCacti MCP ፕለጊን ጋር ያስተባብሩ እና [docs/api.md](../../../docs/api.md)ን ያዘምኑ።

## ፈቃድ

የቅጂ መብት (C) 2026 Thomas Vincent። በGNU General Public License ስሪት 2 ወይም ከዚያ በላይ ሥር ተለቋል። [LICENSE](../../../LICENSE)ን ይመልከቱ።
