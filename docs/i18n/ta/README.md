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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · **தமிழ்** · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP என்பது [Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp) செருகுநிரலின் திறன்களை stdio வழியாக MCP கருவிகளாக வெளிப்படுத்தும் ஒரு Python ஏற்பி ஆகும். இந்தச் செருகுநிரல் ஏற்கனவே HTTP வழியாக MCP ஐ நேரடியாக வழங்குகிறது, எனவே உங்கள் கிளையன்ட் தொலைநிலை சேவையகத்துடன் இணைக்க முடியும்போது அதைப் பயன்படுத்தவும். stdio வழியாக மட்டுமே தொடர்பு கொள்ளும் கிளையன்ட்களுக்கானது இந்த ஏற்பி. இது அதிகாரப்பூர்வ Python MCP SDK ஐப் பயன்படுத்தி, கருவி அழைப்புகளைச் செருகுநிரலின் HTTPS API ஆக (abilities contract v2, `/v1/` பாதைகளின் கீழ் வழங்கப்படுகிறது, bearer token மட்டுமே) மாற்றுகிறது.
அங்கீகாரம், அனுமதி வழங்கல், சரிபார்ப்பு மற்றும் செயல்பாடு ஆகியவற்றை Cacti கையாள்கிறது.

**நிலை: வளர்ச்சியில் உள்ளது, 1.0 க்கு முந்தையது.** பதிப்பு 0.1.0, துணை [Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp) வழியாகப் படிக்க-மட்டுமான சாதனப் பட்டியல் மற்றும் நிறுவல் பதிப்புகளை ஆதரிக்கிறது. இன்னும் டேக் செய்யப்பட்ட வெளியீடு இல்லை. Doctor நோயறிதல்கள் மற்றும் பழுதுபார்ப்புகள் எதிர்காலப் பணியாகும்.

## இது என்ன வெளிப்படுத்துகிறது

| செயல்பாடு | Cacti MCP plugin வழங்கும் MCP கருவி |
|---|---|
| டோக்கன் உரிமையாளர் பார்க்கக்கூடிய சாதனங்களைப் பட்டியலிடுதல் | `cacti-list-devices` |
| அனுமதிக்கப்பட்ட ஒரு சாதனத்தைப் படித்தல் | `cacti-get-device` |
| Cacti, செருகுநிரல் மற்றும் API பதிப்புகளைப் படித்தல் | `cacti-get-system-info` |

பெயர்கள், விளக்கங்கள் மற்றும் உள்ளீட்டுத் திட்டங்கள் Cacti இன் அனுமதி-வடிகட்டப்பட்ட கண்டறிதல் பதிலிலிருந்து வருகின்றன. Python கருவி கையாளுநர்களைச் சேர்க்காமலேயே கூடுதல் அனுமதிக்கப்பட்ட படிக்க-மட்டுமான வழங்குநர்களைக் கண்டறிய முடியும்.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## பயன்பாட்டுச் சூழல்கள்

ஒரு MCP கிளையன்ட்டை இணைத்து, அதன் பிரத்யேகப் பயனர் பார்க்கக்கூடிய Cacti சாதனங்களைப் பட்டியலிடலாம், அனுமதிக்கப்பட்ட ஒரு சாதனத்தைத் தேடலாம், அல்லது பயனருக்குத் தேவையான நிர்வாகப் பகுதி இருக்கும்போது நிறுவல் பதிப்புகளைப் பெறலாம். பெயர்களும் உள்ளீட்டுத் திட்டங்களும் செருகுநிரலின் கண்டறிதல் பதிலிலிருந்து வருவதால், ஏற்பி ஒவ்வொரு வழங்குநரையும் நகலெடுப்பதில்லை. பதிவு மாதிரி மற்றும் தற்போதைய வரம்புகளுக்குச் செருகுநிரலின் [திறன் பதிவு விதிகளைப்](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) பார்க்கவும்.

## குறியீடு மற்றும் சோதனை வரைபடம்

| நடத்தை | செயலாக்கம் | இந்தக் களஞ்சியத்தில் உள்ள சோதனைச் சான்று |
|---|---|---|
| HTTPS சரிபார்ப்பு, வரம்புகள், bearer-மட்டுமான அங்கீகாரம் மற்றும் v2 பக்கமாக்கல் | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP கண்டறிதல், அழைப்புகள் மற்றும் அனுமதி மாற்றங்கள் | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| கட்டளை வரி உதவி, பதிப்பு மற்றும் விடுபட்ட உள்ளமைவு | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

துணைச் செயல்முறை சோதனை ஒரு fixture HTTP முனையுடன் உண்மையான SDK கிளையன்ட் மற்றும் சேவையகத்தைப் பயன்படுத்துகிறது. இதற்கு நேரடி Cacti ஒருங்கிணைப்புச் சோதனை தேவையில்லை, மேலும் இது அதற்கு மாற்றாகவும் அமையாது.

## இது எவ்வாறு பாதுகாப்பாக இருக்கிறது

- துவக்கம், கருவி கண்டறிதல், அழைப்புகள் மற்றும் stdio கட்டமைப்புக்கு அதிகாரப்பூர்வ [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) ஐப் பயன்படுத்துகிறது.
- குறிப்புரைகள் துல்லியமாகப் படிக்க-மட்டுமான, அழிவில்லாத மற்றும் idempotent ஆக உள்ள திறன்களை மட்டுமே வெளிப்படுத்துகிறது. திட்டங்களும் பெயர்களும் Cacti இலிருந்து வருகின்றன; ஏற்பியில் SQL, சாதன நற்சான்றிதழ்கள் அல்லது பழுதுபார்க்கும் கட்டளைகள் எதுவும் இல்லை.
- bearer token ஐ மட்டுமே அனுப்புகிறது: குக்கீகள் இல்லை, CSRF படி இல்லை. ஒவ்வொரு கோரிக்கையிலும் செருகுநிரல் டோக்கன் செல்லுபடியையும் அனுமதிகளையும் மீண்டும் சரிபார்க்கிறது.
- சரிபார்க்கப்பட்ட HTTPS ஐப் பயன்படுத்துகிறது, ஒருபோதும் குக்கீகளைச் சேமிப்பதில்லை, திசைதிருப்பல்களை மறுக்கிறது மற்றும் proxy சூழல் மாறிகளைப் புறக்கணிக்கிறது. HTTP க்கு `--allow-loopback-http` மற்றும் ஒரு நேரடி loopback முகவரி அல்லது `localhost` தேவைப்படுகிறது.
- API அழைப்புகளை மொத்தமாக 35 வினாடிகள், இணைக்க 5 வினாடிகள், பிணையச் செயலின்மைக்கு 30 வினாடிகள் மற்றும் ஒரு பதிலுக்குச் சுமார் 1 MB (1,100,000 bytes) என வரம்பிடுகிறது. கோரிக்கை உடல்கள் 16,384 bytes ஆக வரையறுக்கப்பட்டுள்ளன. ஒரு கிளையன்ட் அமர்வுக்கு அழைப்புகள் வரிசைப்படுத்தப்படுகின்றன.
- கருவி அளவுருக்களை அனுப்புவதற்கு முன்பு கடைசிக் கண்டறிதலின் உள்ளீட்டுத் திட்டத்துடன் ஒப்பிட்டுச் சரிபார்க்கிறது, மேலும் அந்தச் சரிபார்க்கப்பட்ட பட்டியலிலிருந்து உள்ள id களை மட்டுமே இயக்குகிறது. பொருந்தாமை அல்லது சேவையகத்திலிருந்து வரும் தவறான திட்டம் செயலிழப்பாக இல்லாமல் கருவிப் பிழையாகத் திரும்பும்.
- செயல்பாட்டைத் தானாக மீண்டும் முயற்சிப்பதில்லை. கருவிப் பிழைகள் HTTP நிலை, AIP-193 `status` மற்றும் ErrorInfo `reason` ஆகியவற்றை மட்டுமே கொண்டுள்ளன; ஒருபோதும் சேவையகச் செய்தி உரை, பதில் உடல்கள் அல்லது நற்சான்றிதழ்களைக் கொண்டிருப்பதில்லை. Stdout MCP செய்திகளுக்காக மட்டுமே ஒதுக்கப்பட்டுள்ளது.

SDK பதிப்பு `uv.lock` ஆல் பின் செய்யப்பட்டுள்ளது (`pyproject.toml` இல் `mcp>=2.3,<3`). இந்த ஏற்பி அதன் 2.x கீழ்-நிலை சேவையகத்தை stdio transport உடன் பயன்படுத்துகிறது; இது தொலைநிலை MCP HTTP முனையம், OAuth, resources, prompts, subscriptions அல்லது பின்னணிப் பணிகளைச் செயல்படுத்துவதில்லை.

[API ஒப்பந்தம்](../../../docs/api.md) மற்றும் [செயலாக்கத் திட்டத்தைப்](../../../docs/plan.md) பார்க்கவும்.

## நிறுவல் மற்றும் கட்டளை வரி

Python 3.12 அல்லது அதற்குப் பிந்தைய பதிப்பு மற்றும் [uv](https://docs.astral.sh/uv/) தேவை.
இந்தக் களஞ்சியத்தின் நகலிலிருந்து:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

PHP செருகுநிரலை நிறுவி இயக்கவும், அதன் பகுதியை ஒரு பிரத்யேக Cacti பயனருக்கு வழங்கவும், மேலும் செருகுநிரலின் கன்சோலில், அதன் My MCP Tokens பக்கத்தில் அல்லது அதன் `tokens.php` கட்டளையுடன் அந்தப் பயனருக்காக ஒரு தனிப்பட்ட அணுகல் டோக்கனை (`cmcp_pat_` அதைத் தொடர்ந்து 64 சிறிய எழுத்து hex இலக்கங்கள் என்ற வடிவத்தில்) உருவாக்கவும்.
பயனரின் ஏற்கனவே உள்ள Cacti பகுதிகள் மற்றும் சாதன அனுமதிகள் தொடர்ந்து பொருந்தும்.

உங்கள் ரகசிய மேலாளர் வழியாக டோக்கனை `CACTI_MCP_TOKEN` ஆக வழங்கவும்; அதை ஒருபோதும் மூலக் கட்டுப்பாடு அல்லது கட்டளை அளவுருக்களில் சேர்க்க வேண்டாம். முனையத்தைத் தனியாக அமைக்கவும். அது `/plugins/mcp/api.php` இல் முடிவடையும் HTTPS URL ஆக இருக்க வேண்டும், அதில் நற்சான்றிதழ்கள், query அல்லது fragment எதுவும் இருக்கக் கூடாது:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` என்பது `CACTI_MCP_ENDPOINT` க்குப் பதிலாக முனையத்தை அமைக்கிறது.
உள்ளூர் சோதனைக்காக `localhost`, `127.0.0.1` அல்லது `::1` க்குச் சாதாரண HTTP ஐ `--allow-loopback-http` அனுமதிக்கிறது, `--lang LOCALE` CLI செய்தி உள்ளூர்மயமாக்கலை மாற்றுகிறது, மற்றும் `--version` பதிப்பை அச்சிடுகிறது. முனையம் மற்றும் `CACTI_MCP_TOKEN` இரண்டும் இல்லாமல், கட்டளை பயன்பாட்டுப் பிழையுடன் வெளியேறும்.

### உள்ளூர்மயமாக்கல்

CLI உதவி மற்றும் ஏற்பிப் பிழைச் செய்திகள் எந்தக் கூடுதல் சார்புகளும் இல்லாமல் 45 மொழிகளில் (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) கிடைக்கின்றன. மொழித் தீர்மானம் முதலில் `--lang`, பின்னர் `LC_ALL`, `LC_MESSAGES` மற்றும் `LANG` ஆகியவற்றைச் சரிபார்த்து, இறுதியில் `en` க்குத் திரும்புகிறது (`C`/`POSIX` மற்றும் அறியப்படாத குறிச்சொற்களும் `en` ஆகத் தீர்மானிக்கப்படுகின்றன). MCP கருவிப் பெயர்கள், திட்டங்கள் மற்றும் வெற்றிகரமான JSON கருவித் தரவுகள் பாதிக்கப்படாது; `is_error=True` உடன் திரும்பும் ஏற்பிப் பிழைச் செய்திகள் செயலில் உள்ள மொழியைப் பின்பற்றும்.

செயல்முறை stdin இல் MCP செய்திகளுக்காகக் காத்திருக்கிறது. ஒரு MCP கிளையன்ட் பொதுவாக இதைத் தொடங்கும்.
பொதுவான `mcpServers` உள்ளமைவு வடிவத்தை ஏற்கும் கிளையன்ட்களுக்கு:

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

அதன் சூழல் அல்லது ரகசிய வசதி வழியாகத் துணைச் செயல்முறைக்கு `CACTI_MCP_ENDPOINT` மற்றும் `CACTI_MCP_TOKEN` ஆகியவற்றை அனுப்புமாறு கிளையன்ட்டை உள்ளமைக்கவும். சூழல் மரபுரிமை கிளையன்ட்டைப் பொறுத்தது. டோக்கனுக்கான கட்டளை வரி கொடி எதுவும் இல்லை.

தனியாக நிறுவக்கூடிய Python விநியோகம் `cacti-mcp` கன்சோல் கட்டளையை வழங்குகிறது. செக்அவுட்டை இயக்க PyPI வெளியீடு தேவையில்லை. PHP செருகுநிரலுக்கு Python சார்பு எதுவும் இல்லை.

## வெளியீடுகள்

விநியோகப் பதிப்பு [pyproject.toml](../../../pyproject.toml) இல் பதிவு செய்யப்பட்டுள்ளது.
டேக் செய்யப்பட்ட வெளியீடுகள் கிடைக்கும் வரை, மூலக் களஞ்சிய நகலை அல்லது வெற்றிகரமான [CI இயக்கத்திலிருந்து](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) `python-distributions` artifact ஐப் பயன்படுத்தவும்.
அந்த artifact இல் ஒரு wheel மற்றும் மூலக் காப்பகம் உள்ளது. நிறுவப்பட்ட தொகுப்பு `cacti-mcp` கட்டளை மற்றும் `python -m cacti_mcp` ஆகிய இரண்டையும் வழங்குகிறது; இதில் PHP செருகுநிரல் இல்லை.

## வளர்ச்சி மற்றும் சோதனைகள்

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

சோதனைகள் HTTP சரிபார்ப்பு, நற்சான்றிதழ் தனிமைப்படுத்தல், bearer-மட்டுமான கோரிக்கைகள், பக்கமாக்கல், பிழை மறைப்பு மற்றும் fixture HTTP சேவையகத்திற்கு எதிரான உண்மையான SDK கிளையன்ட்/சேவையக துணைச் செயல்முறைப் பரிமாற்றத்தை உள்ளடக்கியவை. இவற்றுக்கு நேரடி Cacti நிறுவல் தேவையில்லை.

இந்தக் களஞ்சியம் `src/cacti_mcp/`, pytest, Ruff, uv மற்றும் Hatchling ஆகியவற்றைப் பயன்படுத்துகிறது. CI ஆனது Python 3.12, 3.13 மற்றும் 3.14 ஆகியவற்றைச் சோதிக்கிறது. ஒரு தனித் தொகுப்பு உருவாக்கப் பணி wheel மற்றும் மூலக் காப்பகத்தை உருவாக்குகிறது, களஞ்சியத்திற்கு வெளியே wheel ஐ நிறுவுகிறது மற்றும் இரண்டு நுழைவுப் புள்ளிகளையும் புகைச் சோதனை செய்கிறது. விநியோகங்களும் சோதனை முடிவுகளும் workflow artifact களாகும்.

## பங்களித்தல்

Pull request கள் `develop` கிளைக்குச் செல்ல வேண்டும். ஏற்பியை Python 3.12 உடன் இணக்கமாக வைத்திருங்கள், ஏற்கனவே உள்ள Ruff உள்ளமைவு மற்றும் `src/cacti_mcp/` தொகுப்பு அமைப்பைப் பின்பற்றுங்கள், மேலும் stdout ஐ MCP செய்திகளுக்காக ஒதுக்கி வையுங்கள். மாற்றப்பட்ட transport அல்லது கருவி நடத்தைக்குச் சோதனைகளைச் சேர்க்கவும், மேலே உள்ள சோதனைகளை இயக்கவும், மேலும் `git commit -s` உடன் commit களில் கையொப்பமிடவும்.
API மாற்றங்களை Cacti MCP plugin உடன் ஒருங்கிணைத்து [docs/api.md](../../../docs/api.md) ஐப் புதுப்பிக்கவும்.

## உரிமம்

Copyright (C) 2026 Thomas Vincent. GNU General Public License, பதிப்பு 2 அல்லது அதற்குப் பிந்தைய பதிப்பின் கீழ் வெளியிடப்பட்டது. [LICENSE](../../../LICENSE) ஐப் பார்க்கவும்.
