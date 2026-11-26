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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · **Malagasy** · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Ny Cacti MCP dia adaptatera Python izay mamoaka ireo fahaizan'ny
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) ho fitaovana MCP
amin'ny alalan'ny stdio. Efa manolotra MCP mivantana amin'ny HTTP ny plugin, koa
ampiasao izany rehefa afaka mifandray amin'ny mpizara lavitra ny mpanjifanao. Ity adaptatera ity dia natao ho an'ny
mpanjifa tsy mampiasa afa-tsy stdio. Mampiasa ny SDK Python MCP ofisialy izy ary
mandika ny antso fitaovana ho ao amin'ny API HTTPS an'ny plugin (fifanarahana fahaiza-manao v2, omena
eo ambanin'ny lalana `/v1/`, mari-pamantarana bearer ihany).
Ny Cacti no miandraikitra ny fanamarinana maha-izy azy, ny fanomezana alalana, ny fanamarinana ary ny fanatanterahana.

**Sata: eo am-pamolavolana, mialoha ny 1.0.** Ny dikan-teny 0.1.0 dia manohana lisitry ny milina
vakiana ihany sy dikan-tenin'ny fametrahana amin'ny alalan'ny
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) mpiara-miasa aminy.
Mbola tsy misy famoahana nasiana marika (tagged release) aloha. Ny fitiliana doctor sy ny fanamboarana dia asa ho avy.

## Ny zavatra avoakany

| Asa | Fitaovana MCP omen'ny plugin Cacti MCP |
|---|---|
| Mitantara ny lisitry ny milina azon'ny tompon'ny mari-pamantarana jerena | `cacti-list-devices` |
| Mamaky milina iray nahazoana alalana | `cacti-get-device` |
| Mamaky ny dikan-tenin'ny Cacti, ny plugin, ary ny API | `cacti-get-system-info` |

Ny anarana, ny famaritana, ary ny rafitra fampidirana (input schemas) dia avy amin'ny valin'ny
fahitana voasivana araka ny alalana ao amin'ny Cacti. Azo hita ireo mpanome vaovao vakiana ihany nahazoana alalana
nefa tsy mila manampy mpitantana fitaovana Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Fampiasana mahazatra

Ampifandraiso ny mpanjifa MCP mba hampisehoana ny lisitry ny milina Cacti azon'ilay mpampiasa natokana jerena,
hijery milina iray nahazoana alalana, na haka ny dikan-tenin'ny fametrahana rehefa manana ny
sehatra fitantanana takiana ny mpampiasa. Avy amin'ny valin'ny fahitan'ny plugin ny anarana sy ny rafitra fampidirana,
ka tsy mamerina mpanome tsirairay ny adaptatera.
Jereo ny
[fitsipika fisoratana anarana fahaiza-manao](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
an'ny plugin raha mila ny maodely fisoratana anarana sy ny fetra ankehitriny.

## Sarintanin'ny kaody sy fitsapana

| Fiasa | Fampiharana | Porofon'ny fitsapana ato amin'ity tahiry ity |
|---|---|---|
| Fanamarinana HTTPS, fetra, fanamarinana bearer ihany, ary fizarana pejy v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Fahitana MCP, antso, ary fiovan'ny alalana | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Fanampiana andalan-kibaiko, dikan-teny, ary fanefena tsy ampy | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Ny fitsapana subprocess dia mampiasa mpanjifa sy mpizara SDK tena izy miaraka amin'ny teboka fiafarana HTTP
natao ho an'ny fitsapana (fixture). Tsy mitaky na manolo ny fanamarinana fampidirana amin'ny Cacti mivantana izany.

## Ny fomba itandroany ny fiarovana

- Mampiasa ny [SDK Python `mcp`](https://github.com/modelcontextprotocol/python-sdk) ofisialy
  ho an'ny fanombohana, ny fahitana fitaovana, ny antso, ary ny fandrafetana stdio.
- Tsy mamoaka afa-tsy fahaiza-manao manana fanamarihana mazava hoe vakiana ihany, tsy manimba, ary idempotent. Avy amin'ny
  Cacti ny rafitra sy ny anarana; tsy misy SQL, tenimiafin'ny milina, na baiko fanamboarana ao amin'ny adaptatera.
- Tsy mandefa afa-tsy ny mari-pamantarana bearer: tsy misy cookies, tsy misy dingana CSRF. Hamarinin'ny plugin indray
  ny fahamarinan'ny mari-pamantarana sy ny alalana isaky ny fangatahana.
- Mampiasa HTTPS voamarina, tsy mitahiry cookies mihitsy, mandà ny fampiviliana lalana (redirects), ary
  tsy miraharaha ny fari-tontolo proxy. Mitaky `--allow-loopback-http` ny HTTP
  sy adiresy loopback ara-bakiteny na `localhost`.
- Mametra ny antso API ho 35 segondra amin'ny ankapobeny, 5 segondra hifandraisana, 30 segondra
  tsy fihetsehan'ny tambajotra, ary eo amin'ny 1 MB eo ho eo isaky ny valiny (1,100,000 bytes).
  Ferana ho 16,384 bytes ny vatan'ny fangatahana. Atambatra milahatra isaky ny fotoam-pifandraisan'ny mpanjifa ny antso.
- Manamarina ny masontsivana fitaovana amin'ny rafitra fampidirana avy amin'ny fahitana farany alohan'ny
  handefasana azy, ary tsy manatanteraka afa-tsy famantarana avy amin'izany lisitra voamarina izany. Ny tsy fifanarahana, na
  ny rafitra simba avy amin'ny mpizara, dia miverina ho hadisoan'ny fitaovana fa tsy fahatapahana tampoka.
- Tsy mamerina manatanteraka mandeha ho azy. Tsy mitondra afa-tsy ny satan'ny HTTP,
  ny `status` AIP-193, ary ny `reason` ErrorInfo ny hadisoan'ny fitaovana; tsy mitondra lahatsoratra hafatra avy amin'ny mpizara,
  vatan'ny valiny, na fampahalalana miafina mihitsy. Natokana ho an'ny hafatra MCP ny stdout.

Voatokana ao amin'ny `uv.lock` ny dikan-tenin'ny SDK (`mcp>=2.3,<3` ao amin'ny `pyproject.toml`). Ity
adaptatera ity dia mampiasa ny mpizara ambany lenta 2.x miaraka amin'ny fitaterana stdio; tsy
manatanteraka teboka fiafarana MCP HTTP lavitra, OAuth, loharanon-karena,
prompts, famandrihana, na asa ao ambadika izy.

Jereo [ny fifanarahana API](../../../docs/api.md) sy [ny drafitra fampiharana](../../../docs/plan.md).

## Fametrahana sy andalan-kibaiko

Mitaky Python 3.12 na vaovao kokoa ary [uv](https://docs.astral.sh/uv/).
Avy amin'ny dika mitovy an'ity tahiry ity:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Apetraho sy alefaso ny plugin PHP, omeo ny sehatrany ny mpampiasa Cacti natokana,
ary mamorona mari-pamantarana fidirana manokana ho an'izany mpampiasa izany (endrika `cmcp_pat_` arahina
tarehimarika hex litera kely 64) ao amin'ny console an'ny plugin, ao amin'ny pejiny My MCP Tokens,
na amin'ny baikony `tokens.php`.
Mbola mihatra ihany ireo sehatra Cacti sy alalan'ny milina efa ananan'ny mpampiasa.

Omeo amin'ny alalan'ny mpitantana tsiambaratelonao amin'ny anarana `CACTI_MCP_TOKEN` ilay mari-pamantarana; aza ampidirina mihitsy
ao amin'ny fanaraha-maso kaody loharano na amin'ny masontsivan'ny baiko izany. Apetraho misaraka ny teboka fiafarana. Tsy maintsy
URL HTTPS miafara amin'ny `/plugins/mcp/api.php` izany, tsy misy tenimiafina, fangatahana (query), na
ampahany (fragment):

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

Ny `--endpoint URL` no mametra ny teboka fiafarana fa tsy ny `CACTI_MCP_ENDPOINT`.
Ny `--allow-loopback-http` dia mamela HTTP tsotra mankany amin'ny `localhost`, `127.0.0.1`, na `::1`
ho an'ny fitsapana eo an-toerana, ny `--lang LOCALE` dia manova ny fitenin'ny hafatra CLI, ary ny
`--version` dia mampiseho ny dikan-teny. Raha tsy misy azy roa na ny teboka fiafarana na ny `CACTI_MCP_TOKEN`,
dia mivoaka miaraka amin'ny hadisoana fampiasana ny baiko.

### Fiteny sy faritra

Ny fanampiana CLI sy ny hafatra hadisoan'ny adaptatera dia misy amin'ny fiteny sy faritra 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) tsy misy fiankinan-doha fanampiny. Ny famaritana ny fiteny
dia manamarina ny `--lang`, avy eo `LC_ALL`, `LC_MESSAGES`, ary `LANG`, ary miverina
amin'ny `en` (`C`/`POSIX` sy ireo marika tsy fantatra dia miverina amin'ny `en` ihany koa). Ny anaran'ny fitaovana MCP,
ny rafitra, ary ny angona JSON mahomby avy amin'ny fitaovana dia tsy miova; ny hafatra hadisoan'ny adaptatera
averina miaraka amin'ny `is_error=True` dia manaraka ny fiteny miasa.

Miandry hafatra MCP eo amin'ny stdin ilay dingana. Mpanjifa MCP mazàna no mandefa azy.
Ho an'ny mpanjifa manaiky ny endrika fanefena `mcpServers` mahazatra:

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

Amboary ny mpanjifa mba handefa ny `CACTI_MCP_ENDPOINT` sy `CACTI_MCP_TOKEN` any amin'ny
subprocess amin'ny alalan'ny tontolony na ny rafitra fitantanana tsiambaratelony. Miankina amin'ny mpanjifa ny fandovana tontolo.
Tsy misy safidy andalan-kibaiko ho an'ny mari-pamantarana.

Ny fizarana Python azo apetraka misaraka dia manome ny baiko console `cacti-mcp`.
Tsy ilaina ny famoahana ao amin'ny PyPI mba hampandehanana ny dika mitovy. Tsy miankina amin'ny Python
ny plugin PHP.

## Famoahana

Voarakitra ao amin'ny [pyproject.toml](../../../pyproject.toml) ny dikan-tenin'ny fizarana.
Mandra-pisian'ny famoahana nasiana marika, ampiasao ny dika mitovy avy amin'ny kaody loharano na ny
zavatra vokarina `python-distributions` avy amin'ny
[fampandehanana CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) nahomby.
Misy wheel sy arisiva loharano ao anatin'ilay vokatra. Ny fonosana napetraka dia manome
na ny baiko `cacti-mcp` na ny `python -m cacti_mcp`; tsy ao anatiny ny
plugin PHP.

## Fampandrosoana sy fitsapana

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Manarona ny fanamarinana HTTP, ny fanokanana fampahalalana miafina, ny fangatahana bearer ihany,
ny fizarana pejy, ny fanafenana hadisoana, ary ny fifanakalozana subprocess tena izy eo amin'ny mpanjifa/mpizara SDK miaraka
amin'ny mpizara HTTP fitsapana ny fitsapana. Tsy mitaky fametrahana Cacti mivantana izy ireo.

Mampiasa `src/cacti_mcp/`, pytest, Ruff, uv, ary Hatchling ny tahiry. Mitsapa
Python 3.12, 3.13, ary 3.14 ny CI. Ny asa famonosana misaraka dia manamboatra ny wheel
sy ny arisiva loharano, mametraka ny wheel ivelan'ny dika mitovy, ary manao fitsapana fototra
amin'ireo teboka fidirana roa. Vokatra avy amin'ny workflow ny fizarana sy ny valin'ny fitsapana.

## Fandraisana anjara

Mankany amin'ny `develop` ny Pull Requests. Tazomy hifanaraka amin'ny Python 3.12 ny adaptatera,
araho ny fanefena Ruff efa misy sy ny fandrafetana fonosana `src/cacti_mcp/`, ary
tazomy ho natokana ho an'ny hafatra MCP ny stdout. Manampia fitsapana ho an'ny fitondran-tenan'ny fitaterana na fitaovana
novaina, tanteraho ireo fanamarinana etsy ambony, ary soniavo ny commits amin'ny `git commit -s`.
Ampifanaraho amin'ny plugin Cacti MCP ny fanovana API ary havaozy ny [docs/api.md](../../../docs/api.md).

## Lisansa

Copyright (C) 2026 Thomas Vincent. Navoaka eo ambanin'ny GNU General Public
License, dikan-teny 2 na vaovao kokoa. Jereo ny [LICENSE](../../../LICENSE).
