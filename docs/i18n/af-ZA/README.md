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

**Afrikaans** · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP is 'n Python-adapter wat die vermoëns van die
[Cacti MCP-inprop](https://github.com/somethingwithproof/plugin_mcp) as MCP-nutsgoed
oor stdio blootstel. Die inprop bedien reeds MCP regstreeks oor HTTP, so gebruik
dit wanneer jou kliënt aan 'n afgeleë bediener kan koppel. Hierdie adapter is vir
kliënte wat slegs stdio praat. Dit gebruik die amptelike Python MCP SDK en
vertaal nutsmiddelroepe na die inprop se HTTPS-API (vermoëkontrak v2, bedien
onder `/v1/`-paaie, slegs draertoken).
Cacti beheer verifikasie, magtiging, validering en uitvoering.

**Status: in ontwikkeling, voor 1.0.** Weergawe 0.1.0 ondersteun leesalleen-toestelinventaris
en installasieweergawes deur die meegaande
[Cacti MCP-inprop](https://github.com/somethingwithproof/plugin_mcp).
Daar is nog geen gemerkte vrystelling nie. Dokterdiagnostiek en herstelwerk is toekomstige werk.

## Wat dit blootstel

| Bewerking | MCP-nutsmiddel verskaf deur die Cacti MCP-inprop |
|---|---|
| Lys die toestelle wat die tokeneienaar mag sien | `cacti-list-devices` |
| Lees een toegelate toestel | `cacti-get-device` |
| Lees Cacti-, inprop- en API-weergawes | `cacti-get-system-info` |

Name, beskrywings en toevoerskemas kom van Cacti se toestemminggefiltreerde
ontdekkingsrespons. Bykomende toegelate leesalleen-verskaffers kan ontdek word
sonder om Python-nutsmiddelhanterers by te voeg.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Gebruiksgevalle

Koppel 'n MCP-kliënt om die Cacti-toestelle te lys wat sy toegewyde gebruiker mag sien,
een toegelate toestel op te soek, of installasieweergawes op te haal wanneer die gebruiker
die vereiste administratiewe domein het. Name en toevoerskemas kom van
die inprop se ontdekkingsrespons, sodat die adapter nie elke verskaffer dupliseer nie.
Sien die inprop se
[vermoëregistrasiereëls](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
vir die registrasiemodel en huidige beperkings.

## Kode- en toetskaart

| Gedrag | Implementering | Toetsbewyse in hierdie bewaarplek |
|---|---|---|
| HTTPS-validering, grense, slegs-draer-verifikasie en v2-bladsyverdeling | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP-ontdekking, roepe en toestemmingsveranderings | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Opdragreëlhulp, weergawe en ontbrekende konfigurasie | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Die subprosestoets gebruik 'n regte SDK-kliënt en -bediener met 'n toetsstuk-HTTP-eindpunt.
Dit vereis of vervang nie 'n lewendige Cacti-integrasiekontrole nie.

## Hoe dit veilig bly

- Gebruik die amptelike [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  vir inisialisering, nutsmiddelontdekking, roepe en stdio-raming.
- Stel slegs vermoëns bloot waarvan die annotasies presies leesalleen, nie-vernietigend en idempotent is. Skemas en name kom
  van Cacti; die adapter bevat geen SQL, toestelgeloofsbriewe of herstelopdragte nie.
- Stuur slegs die draertoken: geen koekies, geen CSRF-stap nie. Die inprop kontroleer
  tokengeldigheid en toestemmings by elke versoek opnuut.
- Gebruik geverifieerde HTTPS, stoor nooit koekies nie, weier herleidings, en
  ignoreer instaanbediener-omgewingsveranderlikes. HTTP vereis `--allow-loopback-http`
  en 'n letterlike teruglusadres of `localhost`.
- Beperk API-roepe tot 35 sekondes algeheel, 5 sekondes om te koppel, 30 sekondes van
  netwerkonaktiwiteit, en ongeveer 1 MB per respons (1 100 000 grepe).
  Versoekliggame is beperk tot 16 384 grepe. Roepe word per kliëntsessie
  geserialiseer.
- Kontroleer nutsmiddelargumente teen die toevoerskema van die laaste ontdekking voordat
  dit gestuur word, en voer slegs ID's uit daardie geverifieerde katalogus uit. 'n Wanpassing, of
  'n wangevormde skema van die bediener af, kom terug as 'n nutsmiddelfout, nie 'n omval nie.
- Herprobeer nie uitvoering outomaties nie. Nutsmiddelfoute dra slegs die HTTP-status,
  die AIP-193 `status`, en die ErrorInfo `reason`; nooit bedienerboodskapteks,
  responsliggame of geloofsbriewe nie. Stdout is gereserveer vir MCP-boodskappe.

Die SDK-weergawe word vasgepen deur `uv.lock` (`mcp>=2.3,<3` in `pyproject.toml`). Hierdie
adapter gebruik sy 2.x-laevlakbediener met die stdio-vervoer; dit implementeer nie
'n afgeleë MCP HTTP-eindpunt, OAuth, hulpbronne,
aanwysings, intekeninge of agtergrondtake nie.

Sien [die API-kontrak](../../../docs/api.md) en [implementeringsplan](../../../docs/plan.md).

## Installasie en opdragreël

Vereis Python 3.12 of nuwer en [uv](https://docs.astral.sh/uv/).
Vanuit 'n plaaslike kopie van hierdie bewaarplek:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Installeer en aktiveer die PHP-inprop, ken sy domein aan 'n toegewyde Cacti-gebruiker toe,
en skep 'n persoonlike toegangstoken vir daardie gebruiker (formaat `cmcp_pat_` gevolg
deur 64 kleinletter-heksadesimale syfers) in die inprop se konsole, op sy My MCP Tokens-bladsy,
of met sy `tokens.php`-opdrag.
Die gebruiker se bestaande Cacti-domeine en toesteltoestemmings geld steeds.

Verskaf die token deur jou geheimebestuurder as `CACTI_MCP_TOKEN`; voeg dit nooit
by bronbeheer of opdragargumente nie. Stel die eindpunt afsonderlik. Dit moet 'n
HTTPS-URL wees wat eindig op `/plugins/mcp/api.php`, sonder geloofsbriewe, navraagstring of
fragment:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` stel die eindpunt in plaas van `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` laat gewone HTTP na `localhost`, `127.0.0.1`, of `::1` toe
vir plaaslike toetsing, `--lang LOCALE` oorskryf CLI-boodskaplokalisering, en
`--version` druk die weergawe. Sonder sowel die eindpunt as `CACTI_MCP_TOKEN`,
sluit die opdrag af met 'n gebruiksfout.

### Lokalisering

CLI-hulp en adapterfoutboodskappe word in 45 lokale (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) verskeep met geen bykomende afhanklikhede nie. Lokaaloplossing
kontroleer `--lang`, dan `LC_ALL`, `LC_MESSAGES`, en `LANG`, en val
terug na `en` (`C`/`POSIX` en onbekende etikette los ook op na `en`). MCP-nutsmiddelname,
skemas en suksesvolle JSON-nutsmiddelvragte word nie geraak nie; adapterfoutboodskappe
wat met `is_error=True` teruggestuur word, volg die aktiewe lokaal.

Die proses wag vir MCP-boodskappe op stdin. 'n MCP-kliënt begin dit gewoonlik.
Vir kliënte wat die algemene `mcpServers`-konfigurasieformaat aanvaar:

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

Konfigureer die kliënt om `CACTI_MCP_ENDPOINT` en `CACTI_MCP_TOKEN` deur sy
omgewings- of geheimfasiliteit aan die subproses deur te gee. Oorerwing van
omgewingsveranderlikes hang van die kliënt af. Daar is geen token-opdragreëlvlag nie.

Die afsonderlik installeerbare Python-verspreiding verskaf die `cacti-mcp`-konsoleopdrag.
Geen PyPI-publikasie word vereis om vanuit die werkkopie te hardloop nie. Die PHP-inprop het
geen Python-afhanklikheid nie.

## Vrystellings

Die verspreidingsweergawe word in [pyproject.toml](../../../pyproject.toml) aangeteken.
Totdat gemerkte vrystellings beskikbaar is, gebruik 'n bronkopie of die
`python-distributions`-artefak van 'n suksesvolle
[CI-lopie](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Die artefak bevat 'n wheel en bronargief. Die geïnstalleerde pakket verskaf
beide die `cacti-mcp`-opdrag en `python -m cacti_mcp`; dit bevat nie die
PHP-inprop nie.

## Ontwikkeling en toetse

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Toetse dek HTTP-validering, geloofsbriefisolasie, slegs-draer-versoeke,
bladsyverdeling, foutredigering, en 'n werklike SDK-kliënt/bediener-subprosesuitruiling teen
'n toetsstuk-HTTP-bediener. Dit vereis nie 'n lewendige Cacti-installasie nie.

Die bewaarplek gebruik `src/cacti_mcp/`, pytest, Ruff, uv, en Hatchling. CI toets
Python 3.12, 3.13, en 3.14. 'n Afsonderlike verpakkingstaak bou die wheel
en bronargief, installeer die wheel buite die werkkopie, en rooktoets
albei ingangspunte. Verspreidings en toetsresultate is werkvloei-artefakte.

## Bydraes

Trekversoeke gaan na `develop`. Hou die adapter versoenbaar met Python 3.12,
volg die bestaande Ruff-konfigurasie en `src/cacti_mcp/`-pakketuitleg, en
hou stdout gereserveer vir MCP-boodskappe. Voeg toetse by vir gewysigde vervoer- of nutsmiddelgedrag,
voer die bogenoemde kontroles uit, en teken commits af met `git commit -s`.
Koördineer API-veranderings met die Cacti MCP-inprop en werk [docs/api.md](../../../docs/api.md) by.

## Lisensie

Kopiereg (C) 2026 Thomas Vincent. Vrygestel onder die GNU General Public
License, weergawe 2 of later. Sien [LICENSE](../../../LICENSE).
