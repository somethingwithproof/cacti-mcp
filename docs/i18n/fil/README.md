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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · **Filipino** · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Ang Cacti MCP ay isang Python adapter na naglalantad ng mga kakayahan ng
[Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp) bilang mga MCP
tool sa pamamagitan ng stdio. Direktang nagbibigay na ang plugin ng MCP sa HTTP, kaya iyon ang
gamitin kapag kayang kumonekta ng iyong client sa isang remote server. Ang adapter na ito ay para sa
mga client na stdio lang ang sinusuportahan. Ginagamit nito ang opisyal na Python MCP SDK at
isinasalin ang mga tool call sa HTTPS API ng plugin (abilities contract v2, na ibinibigay
sa ilalim ng mga path na `/v1/`, gamit ang bearer token lang).
Ang Cacti ang may hawak ng authentication, authorization, validation, at execution.

**Katayuan: nasa development pa, bago ang 1.0.** Sinusuportahan ng bersyon 0.1.0 ang read-only na
imbentaryo ng mga device at mga bersyon ng installation sa pamamagitan ng kasamang
[Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp).
Wala pang naka-tag na release sa ngayon. Ang mga diagnostic ng Doctor at mga pag-aayos ay nakaplanong trabaho para sa hinaharap.

## Mga inilalantad nito

| Operasyon | MCP tool na ibinibigay ng Cacti MCP plugin |
|---|---|
| Ilista ang mga device na maaaring makita ng may-ari ng token | `cacti-list-devices` |
| Basahin ang isang pinahihintulutang device | `cacti-get-device` |
| Basahin ang mga bersyon ng Cacti, plugin, at API | `cacti-get-system-info` |

Ang mga pangalan, paglalarawan, at input schema ay nagmumula sa discovery response ng Cacti
na na-filter ayon sa pahintulot. Maaaring matuklasan ang mga karagdagang pinahihintulutang read-only na provider
nang hindi nagdadagdag ng mga Python tool handler.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Mga gamit

Ikonekta ang isang MCP client upang mailista ang mga Cacti device na maaaring makita ng nakalaang user nito,
tingnan ang isang pinahihintulutang device, o kunin ang mga bersyon ng installation kapag may kinakailangang
administrative realm ang user. Nagmumula sa discovery response ng plugin ang mga pangalan at input schema,
kaya hindi inuulit ng adapter ang bawat provider.
Tingnan ang
[mga panuntunan sa pagpaparehistro ng kakayahan](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
ng plugin para sa modelo ng pagpaparehistro at mga kasalukuyang limitasyon.

## Mapa ng code at test

| Gawi | Implementasyon | Katibayan ng test sa repository na ito |
|---|---|---|
| Pag-validate ng HTTPS, mga hangganan, bearer-only auth, at v2 paging | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Pag-discover ng MCP, mga call, at mga pagbabago sa pahintulot | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Tulong sa command-line, bersyon, at nawawalang configuration | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Gumagamit ang subprocess test ng totoong SDK client at server na may fixture HTTP
endpoint. Hindi ito nangangailangan o pumapalit sa isang live na Cacti integration check.

## Paano ito nananatiling ligtas

- Ginagamit ang opisyal na [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  para sa initialization, pag-discover ng tool, mga call, at stdio framing.
- Inilalantad lamang ang mga kakayahang may mga annotation na eksaktong read-only, non-destructive, at idempotent. Nagmumula sa Cacti ang mga schema at pangalan;
  walang nilalamang SQL, mga kredensyal ng device, o mga utos sa pag-aayos ang adapter.
- Ipinapadala lamang ang bearer token: walang cookies, walang hakbang para sa CSRF. Sinusuri muli ng plugin
  ang bisa ng token at mga pahintulot sa bawat request.
- Gumagamit ng na-verify na HTTPS, hindi nagtatago ng cookies, tumatanggi sa mga redirect, at
  hindi pinapansin ang mga proxy environment variable. Nangangailangan ang HTTP ng `--allow-loopback-http`
  at isang literal na loopback address o `localhost`.
- Nililimitahan ang mga API call sa 35 segundo sa kabuuan, 5 segundo para kumonekta, 30 segundo ng
  pagkawala ng aktibidad sa network, at humigit-kumulang 1 MB bawat response (1,100,000 bytes).
  Limitado sa 16,384 bytes ang mga request body. Naka-serialize ang mga call sa bawat client
  session.
- Sinusuri ang mga argumento ng tool laban sa input schema mula sa huling discovery bago
  ipadala ang mga ito, at mga id lamang mula sa na-verify na catalog na iyon ang pinapatakbo. Ang hindi pagtutugma, o
  isang sirang schema mula sa server, ay bumabalik bilang isang tool error, hindi isang crash.
- Hindi awtomatikong inuulit ang pagpapatakbo. Ang mga tool error ay nagdadala lamang ng HTTP
  status, AIP-193 `status`, at ErrorInfo `reason`; hindi kailanman ng text ng mensahe ng server,
  mga response body, o mga kredensyal. Nakalaan ang stdout para sa mga mensahe ng MCP.

Naka-pin ang bersyon ng SDK sa `uv.lock` (`mcp>=2.3,<3` sa `pyproject.toml`). Ginagamit ng
adapter na ito ang 2.x low-level server nito kasama ang stdio transport; hindi ito
nagpapatupad ng remote MCP HTTP endpoint, OAuth, mga resource,
mga prompt, mga subscription, o mga background task.

Tingnan [ang API contract](../../../docs/api.md) at [plano ng implementasyon](../../../docs/plan.md).

## Pag-install at command line

Nangangailangan ng Python 3.12 o mas bago at ng [uv](https://docs.astral.sh/uv/).
Mula sa isang checkout ng repository na ito:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

I-install at i-enable ang PHP plugin, ibigay ang realm nito sa isang nakalaang user ng Cacti,
at gumawa ng personal access token para sa user na iyon (format na `cmcp_pat_` na sinusundan
ng 64 na lowercase hex digit) sa console ng plugin, sa pahina nitong My MCP Tokens,
o gamit ang command nitong `tokens.php`.
Umiiral pa rin ang mga kasalukuyang Cacti realm at mga pahintulot sa device ng user.

Ibigay ang token sa pamamagitan ng iyong secret manager bilang `CACTI_MCP_TOKEN`; huwag kailanman ilagay ito
sa source control o mga argumento ng command. Itakda nang hiwalay ang endpoint. Dapat itong maging isang
HTTPS URL na nagtatapos sa `/plugins/mcp/api.php`, at walang mga kredensyal, query, o
fragment:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

Itinatakda ng `--endpoint URL` ang endpoint sa halip na `CACTI_MCP_ENDPOINT`.
Pinapayagan ng `--allow-loopback-http` ang plain HTTP papunta sa `localhost`, `127.0.0.1`, o `::1`
para sa lokal na pag-test, pinapalitan ng `--lang LOCALE` ang localization ng mensahe sa CLI, at
ipinapakita ng `--version` ang bersyon. Kung wala pareho ang endpoint at ang `CACTI_MCP_TOKEN`,
magsasara ang command na may usage error.

### Localization

Ang tulong ng CLI at mga mensahe ng error ng adapter ay may kasamang 45 locale (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) nang walang karagdagang dependency. Sinusuri ng pagresolba ng locale
ang `--lang`, pagkatapos ay ang `LC_ALL`, `LC_MESSAGES`, at `LANG`, at bumabalik
sa `en` kung wala (ang `C`/`POSIX` at mga hindi kilalang tag ay nagre-resolve din sa `en`). Hindi apektado ang mga pangalan ng MCP tool,
mga schema, at mga matagumpay na JSON tool payload; ang mga mensahe ng error ng adapter
na ibinabalik nang may `is_error=True` ay sumusunod sa aktibong locale.

Naghihintay ang proseso ng mga mensahe ng MCP sa stdin. Karaniwang isang MCP client ang naglulunsad nito.
Para sa mga client na tumatanggap ng karaniwang format ng configuration na `mcpServers`:

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

I-configure ang client upang ipasa ang `CACTI_MCP_ENDPOINT` at `CACTI_MCP_TOKEN` sa
subprocess sa pamamagitan ng environment o secret facility nito. Nakadepende sa client ang pagmamana ng environment.
Walang token flag sa command-line.

Ang hiwalay na mai-install na Python distribution ay nagbibigay ng `cacti-mcp` console
command. Hindi kinakailangan ang paglalathala sa PyPI upang patakbuhin ang checkout. Walang Python dependency
ang PHP plugin.

## Mga Release

Naitatala ang bersyon ng distribution sa [pyproject.toml](../../../pyproject.toml).
Hangga't hindi pa available ang mga naka-tag na release, gumamit ng source checkout o ng
`python-distributions` artifact mula sa isang matagumpay na
[CI run](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Naglalaman ang artifact ng isang wheel at source archive. Ang naka-install na package ay nagbibigay ng
parehong `cacti-mcp` command at `python -m cacti_mcp`; hindi ito naglalaman ng
PHP plugin.

## Pag-develop at mga test

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Saklaw ng mga test ang HTTP validation, pagbubukod ng kredensyal, mga bearer-only request,
paging, pag-redact ng error, at isang aktwal na SDK client/server subprocess exchange laban
sa isang fixture HTTP server. Hindi nangangailangan ang mga ito ng isang live na installation ng Cacti.

Gumagamit ang repository ng `src/cacti_mcp/`, pytest, Ruff, uv, at Hatchling. Sinusuri ng CI ang
Python 3.12, 3.13, at 3.14. Gumagawa ang isang hiwalay na packaging job ng wheel
at source archive, nag-i-install ng wheel sa labas ng checkout, at nagsasagawa ng smoke-test
sa parehong entry point. Mga workflow artifact ang mga distribution at resulta ng test.

## Pag-ambag

Ang mga pull request ay papunta sa `develop`. Panatilihing tugma ang adapter sa Python 3.12,
sundin ang kasalukuyang configuration ng Ruff at layout ng package na `src/cacti_mcp/`, at
panatilihing nakalaan ang stdout para sa mga mensahe ng MCP. Magdagdag ng mga test para sa binagong transport o gawi ng tool,
patakbuhin ang mga pagsusuri sa itaas, at lagdaan ang mga commit gamit ang `git commit -s`.
Makipag-ugnayan para sa mga pagbabago sa API kasama ng Cacti MCP plugin at i-update ang [docs/api.md](../../../docs/api.md).

## Lisensya

Copyright (C) 2026 Thomas Vincent. Inilabas sa ilalim ng GNU General Public
License, bersyon 2 o mas bago. Tingnan ang [LICENSE](../../../LICENSE).
