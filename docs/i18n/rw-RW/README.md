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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · **Kinyarwanda** · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP ni umuhuza (adapter) wanditse muri Python utanga ubushobozi bwa
[plugin ya Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) nk'ibikoresho
bya MCP binyuze kuri stdio. Iyo plugin isanzwe itanga MCP kuri HTTP mu buryo butaziguye,
bityo uyikoreshe igihe porogaramu yawe ibasha kwihuza na seriveri iri kure. Uyu muhuza
wagenewe porogaramu zikoresha stdio gusa. Ukoresha Python MCP SDK yemewe kandi ugahindura
amabwiriza y'ibikoresho akaba ubusabe kuri HTTPS API ya plugin (amasezerano y'ubushobozi
v2, atangirwa munsi y'inzira za `/v1/`, hakoreshejwe bearer token gusa).
Cacti niyo igenga iyemeza ry'umwirondoro, uburenganzira, isuzuma ry'amakuru, n'ishyirwa
mu bikorwa.

**Imiterere: iracyakorwa, mbere ya 1.0.** Verisiyo ya 0.1.0 ishyigikira gusa gusoma
urutonde rw'ibikoresho n'amaverisiyo yashyizwemo binyuze kuri
[plugin ya Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) bikorana.
Nta verisiyo yemewe (tagged release) irasohoka kugeza ubu. Isuzuma rya doctor n'uburyo
bwo gusana ibibazo bizakorwa mu gihe kizaza.

## Ibyo itanga

| Igikorwa | Igikoresho cya MCP gitangwa na plugin ya Cacti MCP |
|---|---|
| Kwerekana urutonde rw'ibikoresho nyiri token yemerewe kubona | `cacti-list-devices` |
| Gusoma igikoresho kimwe cyemewe | `cacti-get-device` |
| Gusoma verisiyo ya Cacti, plugin, na API | `cacti-get-system-info` |

Amazina, ibisobanuro, n'imiterere y'amakuru yinjizwa (input schemas) bituruka mu gisubizo
cy'ishakisha rya Cacti cyayunguruwe hakurikijwe uburenganzira. Izindi serivisi zemewe zo
gusoma gusa zishobora gutahurwa bitabaye ngombwa kongeraho kode nshya za Python zo
gucunga ibikoresho.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Uburyo ikoreshwa

Huza porogaramu ya MCP kugira ngo werekane urutonde rw'ibikoresho bya Cacti umukoresha
wayo wihariye yemerewe kubona, ushake igikoresho kimwe cyemewe, cyangwa ubone amaverisiyo
yashyizwemo igihe umukoresha afite urwego rw'ubuyobozi rusabwa. Amazina n'imiterere
y'amakuru yinjizwa bituruka mu gisubizo cy'ishakisha rya plugin, bityo umuhuza ntasubiramo
buri serivisi. Reba
[amabwiriza yo kwandikisha ubushobozi](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
ya plugin kugira ngo umenye imiterere y'iyandikisha n'imbogamizi zihari ubu.

## Ikarita ya kode n'isuzuma

| Imikorere | Ishyirwa mu bikorwa | Ibihamya by'isuzuma muri ubu bubiko |
|---|---|---|
| Isuzuma rya HTTPS, imipaka, iyemeza rya bearer gusa, n'ipaji za v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Ishakisha rya MCP, guhamagara ibikoresho, n'impinduka z'uburenganzira | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Ubufasha ku murongo w'amabwiriza, verisiyo, n'igenamiterere ribura | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Isuzuma rya subprocess rikoresha porogaramu na seriveri nyayo ya SDK hamwe n'icyitegererezo
cya HTTP. Ntirikeneye kandi ntirisimbura isuzuma ryo kwihuza na Cacti ikora nyabyo.

## Uko irinda umutekano

- Ikoresha [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) yemewe
  mu gutangiza, gushakisha ibikoresho, kubihamagara, no gutunganya ubutumwa bwa stdio.
- Itanga gusa ubushobozi bufite ibimenyetso bigaragaza neza ko ari ubwo gusoma gusa,
  butangiza, kandi budahindura ibisubizo iyo busubiwemo (idempotent). Imiterere y'amakuru
  n'amazina bituruka muri Cacti; umuhuza ntufite SQL, amakuru y'ibanga y'ibikoresho,
  cyangwa amabwiriza yo gusana.
- Yohereza bearer token gusa: nta cookies, nta ntambwe ya CSRF. Plugin isuzuma bundi
  bushya uburambe bwa token n'uburenganzira kuri buri busabe.
- Ikoresha HTTPS yemejwe, ntabwo ibika cookies, yanga iyoborwa ahandi (redirects), kandi
  yirengagiza impinduragaciro z'ibidukikije za proxy. HTTP isaba `--allow-loopback-http`
  hamwe n'aderesi ya loopback nyayo cyangwa `localhost`.
- Igabanyiriza ubusabe bwa API amasegonda 35 muri rusange, amasegonda 5 yo kwihuza,
  amasegonda 30 y'igihe nta gikorwa kiri ku muyoboro, n'hafi 1 MB kuri buri gisubizo
  (bayiti 1,100,000). Ubunini bw'ubusabe bufite umupaka wa bayiti 16,384. Ubusabe
  bukorwa mu murongo umwe umwe kuri buri sesiyo y'umukoresha.
- Isuzuma ibyinjijwe mu gikoresho ibigereranya n'imiterere y'amakuru yinjizwa yavuye mu
  ishakisha riheruka mbere yo kubyohereza, kandi igakoresha gusa ibiranga (ids) biri kuri
  urwo rutonde rwemejwe. Kutajyana kw'amakuru, cyangwa imiterere y'amakuru idatunganye
  iturutse kuri seriveri, bigaruka nk'ikosa ry'igikoresho, aho gutuma porogaramu ihagarara.
- Ntisubiramo ubusabe mu buryo bwikora. Amakosa y'igikoresho atwara gusa imiterere ya
  HTTP, `status` ya AIP-193, na `reason` ya ErrorInfo; ntabwo yigera atwara ubutumwa bwa
  seriveri, igisubizo cyose, cyangwa amakuru y'ibanga. Stdout yahariwe ubutumwa bwa MCP
  gusa.

Verisiyo ya SDK ifungirwa na `uv.lock` (`mcp>=2.3,<3` muri `pyproject.toml`). Uyu muhuza
ukoresha seriveri yayo yo ku rwego rwo hasi ya 2.x hamwe n'itumanaho rya stdio; ntabwo
ishyira mu bikorwa seriveri ya MCP ya HTTP iri kure, OAuth, ibikoresho by'ububiko
(resources), prompts, iyandikisha ry'amakuru (subscriptions), cyangwa imirimo ikorera
inyuma (background tasks).

Reba [amasezerano ya API](../../../docs/api.md) na [gahunda yo gushyira mu bikorwa](../../../docs/plan.md).

## Gushyiramo n'umurongo w'amabwiriza

Bisaba Python 3.12 cyangwa izisumbuyeho hamwe na [uv](https://docs.astral.sh/uv/).
Uhereye ku bukope bw'ubu bubiko:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Shyiramo kandi wemeze plugin ya PHP, uhe uburenganzira bwayo (realm) umukoresha wa Cacti
wihariye, hanyuma ukore personal access token y'uwo mukoresha (mu miterere ya `cmcp_pat_`
ikurikirwa n'inyuguti n'imibare 64 ntoya za hex) muri console ya plugin, ku rupapuro
rwayo rwa My MCP Tokens, cyangwa ukoresheje itegeko ryayo rya `tokens.php`.
Uburenganzira busanzwe bw'umukoresha muri Cacti n'ubw'ibikoresho bukomeza gukurikizwa.

Tanga token binyuze mu gicunga amakuru yawe y'ibanga nka `CACTI_MCP_TOKEN`; ntuzigere
uyishyira muri kode cyangwa mu byinjizwa mu murongo w'amabwiriza. Shyiraho aderesi ya
seriveri (endpoint) ukwayo. Igomba kuba ari URL ya HTTPS irangira na `/plugins/mcp/api.php`,
idafite amakuru y'ibanga, ibibazo (query), cyangwa igice cya fragment:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` ishyiraho aderesi aho gukoresha `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` yemera HTTP isanzwe kuri `localhost`, `127.0.0.1`, cyangwa `::1`
mu gihe cyo gusuzumira kuri mudasobwa yawe, `--lang LOCALE` ihindura ururimi rw'ubutumwa
bw'umurongo w'amabwiriza, naho `--version` ikerekana verisiyo. Hatariho aderesi na
`CACTI_MCP_TOKEN` byombi, itegeko rirahagarara rigatanga ikosa ry'imikoreshereze.

### Gushyira mu ndimi

Ubufasha ku murongo w'amabwiriza n'ubutumwa bw'amakosa bw'umuhuza biboneka mu ndimi 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) nta yindi mishinga y'inyongera ikenewe. Ihitamo
ry'ururimi risuzuma `--lang`, hagakurikiraho `LC_ALL`, `LC_MESSAGES`, na `LANG`, hanyuma
rigasubira kuri `en` (`C`/`POSIX` n'ibirango bitazwi na byo bisubira kuri `en`). Amazina
y'ibikoresho bya MCP, imiterere y'amakuru (schemas), n'ibisubizo bya JSON byagenze neza
ntibihinduka; ubutumwa bw'amakosa bw'umuhuza bugaruka bufite `is_error=True` bukurikiza
ururimi ruri gukoreshwa.

Porogaramu itegereza ubutumwa bwa MCP kuri stdin. Ubusanzwe porogaramu ya MCP niyo
iyitangiza. Ku maporogaramu yemera imiterere y'igenamiterere isanzwe ya `mcpServers`:

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

Gena imiterere ya porogaramu kugira ngo yoherereze `CACTI_MCP_ENDPOINT` na `CACTI_MCP_TOKEN`
kuri subprocess binyuze mu bidukikije byayo cyangwa uburyo bwayo bwo kubika amabanga.
Uburyo ibidukikije bisigirwa izindi porogaramu biterwa na porogaramu ubwayo. Nta kimenyetso
cyo ku murongo w'amabwiriza gihari cyo gutanga token.

Igice cya Python gishobora gushyirwamo ukwacyo gitanga itegeko rya console rya `cacti-mcp`.
Ntibisaba ko bishyirwa kuri PyPI kugira ngo ukoreshe ububiko bwa kode. Plugin ya PHP
ntikenera Python.

## Verisiyo zashyizwe ahagaragara

Verisiyo y'ikwirakwizwa yanditswe muri [pyproject.toml](../../../pyproject.toml).
Kugeza igihe verisiyo zemewe zizabonekera, koresha kode iri mu bubiko cyangwa igikoresho
cya `python-distributions` kivuye mu
[isuzuma rya CI ryagenze neza](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Icyo gikoresho kirimo wheel n'ububiko bwa kode. Paki yashyizwemo itanga itegeko rya
`cacti-mcp` na `python -m cacti_mcp`; ntirimo plugin ya PHP.

## Iterambere n'isuzuma

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Amasuzuma areba iyemeza rya HTTP, itandukanywa ry'amakuru y'ibanga, ubusabe bukoresha
bearer gusa, ipaji (paging), guhisha amakuru mu makosa, n'ihererekanya nyaryo rya
subprocess hagati ya porogaramu na seriveri ya SDK kuri seriveri ya HTTP y'icyitegererezo.
Ntabwo asaba ko haba hari Cacti ikora.

Ubu bubiko bukoresha `src/cacti_mcp/`, pytest, Ruff, uv, na Hatchling. CI isuzuma kuri
Python 3.12, 3.13, na 3.14. Umurimo wihariye wo gupakira wubaka wheel n'ububiko bwa kode,
ugashyira wheel hanze y'ubu bubiko, kandi ugasuzuma inzira zombi zo gutangira.
Ibyapakirwe n'ibyavuye mu isuzuma bibikwa nk'ibikoresho bya workflow.

## Gutanga umusanzu

Pull requests zoherezwa kuri `develop`. Komeza umuhuza ujyane na Python 3.12, kurikiza
igenamiterere rya Ruff rihari n'imiterere ya paki ya `src/cacti_mcp/`, kandi ukomeze
guharira stdout ubutumwa bwa MCP. Ongeraho amasuzuma ku mpinduka z'itumanaho cyangwa
imikorere y'igikoresho, ukore amasuzuma yavuzwe haruguru, kandi usinye commits ukoresheje
`git commit -s`. Huza impinduka za API na plugin ya Cacti MCP kandi uvugurure
[docs/api.md](../../../docs/api.md).

## Uruhushya

Uburenganzira bw'umwanditsi (C) 2026 Thomas Vincent. Yasohowe munsi y'uruhushya rwa GNU
General Public License, verisiyo ya 2 cyangwa izisumbuyeho. Reba [LICENSE](../../../LICENSE).
