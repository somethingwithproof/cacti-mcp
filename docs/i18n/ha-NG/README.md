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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · **Hausa** · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP wani mai haɗawa (adapter) ne na Python wanda ke bayyana ayyukan
[Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp) a matsayin
kayan aikin MCP ta hanyar stdio. Wannan plugin ɗin ya riga yana ba da sabis na
MCP ta HTTP kai tsaye, don haka ka yi amfani da wannan idan abokin cinikinka
zai iya haɗuwa da sabar nesa. Wannan mai haɗawar na abokan ciniki ne da ke
magana ta stdio kaɗai. Yana amfani da ainihin Python MCP SDK kuma yana fassara
kiran kayan aiki zuwa HTTPS API na plugin ɗin (yarjejeniyar abilities v2, wadda
ake bayarwa a ƙarƙashin hanyoyin `/v1/`, ta hanyar bearer token kaɗai).
Cacti ne ke da alhakin tantancewa, ba da izini, tabbatar da bayanai, da aiwatarwa.

**Matsayi: ana ci gaba da haɓakawa, kafin 1.0.** Sigar 0.1.0 tana goyan bayan
duba jerin na'urori na karatu-kaɗai da sigogin shigarwa ta hanyar abokin haɗin
[Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp).
Har yanzu babu fitowar da aka yi wa alamar saki (tagged release). Binciken
matsaloli na Doctor da gyare-gyare ayyuka ne na gaba.

## Abin da yake bayyanawa

| Aiki | Kayan aikin MCP da Cacti MCP plugin ke bayarwa |
|---|---|
| Lissafa na'urorin da mai mallakar token zai iya gani | `cacti-list-devices` |
| Karanta na'ura guda da aka ba da izini | `cacti-get-device` |
| Karanta sigogin Cacti, plugin, da API | `cacti-get-system-info` |

Sunaye, bayanai, da tsarin shigar da bayanai suna fitowa ne daga martanin
bincike da aka tace bisa izini na Cacti. Za a iya gano ƙarin masu samar da
bayanai na karatu-kaɗai da aka ba da izini ba tare da ƙara masu sarrafa kayan
aiki na Python ba.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Hanyoyin amfani

Haɗa abokin cinikin MCP don lissafa na'urorin Cacti da keɓaɓɓen mai amfani da
shi zai iya gani, bincika na'ura guda da aka ba da izini, ko samo sigogin
shigarwa idan mai amfani yana da matakin izinin gudanarwa da ake buƙata. Sunaye
da tsarin shigar da bayanai suna fitowa ne daga martanin bincike na plugin ɗin,
don haka mai haɗawar ba ya maimaita kowane mai samar da bayanai. Duba
[ƙa'idojin rajistar ayyuka](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
na plugin ɗin don sanin tsarin rajista da iyakokin da ake da su a yanzu.

## Taswirar lamba da gwaje-gwaje

| Halayya | Aiwatarwa | Shaidar gwaji a wannan ma'ajiya |
|---|---|---|
| Tabbatar da HTTPS, iyakoki, tantancewar bearer-only, da raba shafuka na v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Gano MCP, kiraye-kiraye, da sauye-sauyen izini | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Taimakon layin umarni, siga, da ƙarancin saiti | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Gwajin ƙaramin tsari (subprocess) yana amfani da ainihin abokin ciniki da sabar
SDK tare da wurin gwaji na HTTP. Ba ya buƙatar ko maye gurbin ainihin gwajin
haɗin gwiwa da Cacti da ke aiki kai tsaye.

## Yadda yake kiyaye tsaro

- Yana amfani da ainihin [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  don farawa, gano kayan aiki, kiraye-kiraye, da tsara saƙonnin stdio.
- Yana bayyana ayyukan da alamominsu suke na karatu-kaɗai, marasa lalatawa,
  kuma masu ba da sakamako iri ɗaya idan aka maimaita (idempotent) kaɗai.
  Tsarin bayanai da sunaye suna fitowa daga Cacti; mai haɗawar ba ya ɗauke da
  SQL, bayanan shiga na na'ura, ko umarnin gyara.
- Yana aika bearer token kaɗai: babu cookies, babu matakin CSRF. Plugin ɗin
  yana sake duba ingancin token da izini a kowace buƙata.
- Yana amfani da ingantaccen HTTPS, ba ya adana cookies, yana ƙin tura buƙata
  zuwa wani adireshi (redirects), kuma yana watsi da masu canjin muhalli na
  proxy. HTTP yana buƙatar `--allow-loopback-http` da ainihin adireshin
  loopback ko `localhost`.
- Yana iyakance kiran API zuwa daƙiƙa 35 gaba ɗaya, daƙiƙa 5 don haɗuwa, daƙiƙa
  30 na rashin motsin hanyar sadarwa, da kusan MB 1 a kowane martani (baiti
  1,100,000). An iyakance girman jikin buƙata zuwa baiti 16,384. Ana aiwatar da
  kiraye-kiraye ɗaya bayan ɗaya a kowane zaman abokin ciniki.
- Yana duba muhawarar kayan aiki bisa tsarin shigar da bayanai daga binciken
  ƙarshe kafin aika su, kuma yana aiwatar da lambobin shaida (ids) daga wannan
  ingantaccen kundin kaɗai. Rashin daidaito, ko gurɓataccen tsarin bayanai daga
  saba, yana dawowa a matsayin kuskuren kayan aiki, ba rugujewa ba.
- Ba ya sake gwada aiwatarwa ta atomatik. Kurakuran kayan aiki suna ɗauke da
  matsayin HTTP, `status` na AIP-193, da `reason` na ErrorInfo kaɗai; ba sa
  taɓa ɗaukar rubutun saƙon saba, jikin martani, ko bayanan sirri. An keɓe
  stdout don saƙonnin MCP kaɗai.

An ɗaure sigar SDK ta hanyar `uv.lock` (`mcp>=2.3,<3` a cikin `pyproject.toml`).
Wannan mai haɗawar yana amfani da sabar 2.x mai ƙaramin mataki tare da hanyar
sadarwar stdio; ba ya aiwatar da wurin haɗin MCP HTTP na nesa, OAuth, albarkatu,
tsokaci, rajistar bibiya, ko ayyukan baya.

Duba [yarjejeniyar API](../../../docs/api.md) da [tsarin aiwatarwa](../../../docs/plan.md).

## Shigarwa da layin umarni

Yana buƙatar Python 3.12 ko mafi sabo da [uv](https://docs.astral.sh/uv/).
Daga kwafin wannan ma'ajiyar:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Shigar kuma kunna plugin ɗin PHP, ba wa keɓaɓɓen mai amfani da Cacti matakin
izininsa, sannan ka ƙirƙiri personal access token na wannan mai amfani (tsarin
`cmcp_pat_` tare da ƙananan haruffa ko lambobin hex 64) a cikin dandalin plugin
ɗin, a shafinsa na My MCP Tokens, ko ta hanyar umarninsa na `tokens.php`.
Izinin Cacti da na na'urori da mai amfani ke da su za su ci gaba da aiki.

Samar da token ɗin ta hanyar manajan sirrinka a matsayin `CACTI_MCP_TOKEN`; kada
ka taɓa sanya shi a cikin tsarin kula da lamba ko muhawarar umarni. Saita
adireshin endpoint daban. Dole ne ya zama adireshin HTTPS URL wanda ke ƙarewa da
`/plugins/mcp/api.php`, ba tare da bayanan shiga, tambaya (query), ko gutsure
(fragment) ba:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` yana saita adireshin endpoint a maimakon `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` yana ba da izinin amfani da HTTP na yau da kullun zuwa
`localhost`, `127.0.0.1`, ko `::1` don gwajin gida, `--lang LOCALE` yana canza
harshen saƙonnin CLI, kuma `--version` yana nuna sigar. Idan babu adireshin
endpoint da `CACTI_MCP_TOKEN` duk biyun, umarnin zai fita da kuskuren amfani.

### Daidaita harshe

Taimakon CLI da saƙonnin kuskuren mai haɗawa suna zuwa a cikin harsuna 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ba tare da ƙarin wani abin dogaro ba. Zaɓin harshe yana duba `--lang`, sannan `LC_ALL`, `LC_MESSAGES`, da `LANG`, yana komawa zuwa `en` a ƙarshe (`C`/`POSIX` da alamomin da ba a sani ba suma suna komawa zuwa `en`). Sunayen kayan aikin MCP, tsarin bayanai, da bayanan JSON masu nasara na kayan aiki ba su canzawa; saƙonnin kuskuren mai haɗawa da aka dawo da su da `is_error=True` suna bin harshen da ke aiki.

Tsarin yana jiran saƙonnin MCP ta stdin. Abokin cinikin MCP ne ke kunna shi a
al'ada. Ga abokan cinikin da ke karɓar sanannen tsarin saiti na `mcpServers`:

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

Saita abokin cinikin don ya tura `CACTI_MCP_ENDPOINT` da `CACTI_MCP_TOKEN` zuwa
ƙaramin tsarin ta hanyar muhallinsa ko tsarin adana sirri. Gadon muhalli ya
dogara da abokin cinikin. Babu tutar layin umarni don token.

Kunshin Python da za a iya shigarwa daban yana samar da umarnin layin umarni na
`cacti-mcp`. Ba a buƙatar wallafawa a PyPI don gudanar da kwafin ma'ajiyar ba.
Plugin ɗin PHP ba ya dogara da Python.

## Fitowa (Releases)

An rubuta sigar rarrabawar a cikin [pyproject.toml](../../../pyproject.toml).
Har sai fitowar da aka yi wa alama ta samu, yi amfani da kwafin lambar asali ko
kayan `python-distributions` daga nasarar
[gudanarwar CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Kayan yana ɗauke da wheel da rumbun lambar asali. Kunshin da aka shigar yana
samar da umarnin `cacti-mcp` da kuma `python -m cacti_mcp` duka; ba ya ɗauke da
plugin ɗin PHP.

## Haɓakawa da gwaje-gwaje

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Gwaje-gwajen sun ƙunshi tabbatar da HTTP, keɓe bayanan sirri, buƙatun
bearer-only, raba shafuka, ɓoye bayanan kuskure, da ainihin musayar ƙaramin
tsari tsakanin abokin ciniki da sabar SDK a kan sabar gwaji ta HTTP. Ba sa
buƙatar shigarwar Cacti da ke aiki kai tsaye.

Ma'ajiyar tana amfani da `src/cacti_mcp/`, pytest, Ruff, uv, da Hatchling. CI
yana gwada Python 3.12, 3.13, da 3.14. Wani aikin tattara kunshi daban yana gina
wheel da rumbun lambar asali, yana shigar da wheel ɗin a wajen kwafin ma'ajiyar,
sannan yana yi wa duka wuraren shiga gwajin farko (smoke-test). Kunshinan
rarrabawa da sakamakon gwaji kayayyakin aiki ne na tsarin aikin CI.

## Ba da gudummawa

Ana tura pull requests zuwa `develop`. Kiyaye mai haɗawar ya ci gaba da aiki da
Python 3.12, bi saitin Ruff da ke akwai da tsarin kunshin `src/cacti_mcp/`, kuma
bar stdout keɓe don saƙonnin MCP kaɗai. Ƙara gwaje-gwaje don canjin hanyar
sadarwa ko halayyar kayan aiki, gudanar da binciken da ke sama, sannan ka sanya
hannu a kan commits tare da `git commit -s`. Daidaita sauye-sauyen API tare da
Cacti MCP plugin kuma ka sabunta [docs/api.md](../../../docs/api.md).

## Lasisi

Haƙƙin mallaka (C) 2026 Thomas Vincent. An sake shi a ƙarƙashin GNU General
Public License, siga ta 2 ko mafi sabo. Duba [LICENSE](../../../LICENSE).
