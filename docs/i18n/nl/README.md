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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · **Nederlands** · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP is een Python-adapter die de mogelijkheden van de
[Cacti MCP-plugin](https://github.com/somethingwithproof/plugin_mcp) als MCP-tools
beschikbaar maakt via stdio. De plugin biedt zelf al rechtstreeks MCP via HTTP aan;
gebruik dat wanneer je client verbinding kan maken met een externe server. Deze adapter
is bedoeld voor clients die alleen stdio ondersteunen. Hij maakt gebruik van de
officiële Python MCP SDK en vertaalt tool-aanroepen naar de HTTPS API van de plugin
(abilities-contract v2, aangeboden onder `/v1/`-paden, uitsluitend met bearer-token).
Cacti verzorgt de authenticatie, autorisatie, validatie en uitvoering.

**Status: in ontwikkeling, nog voor 1.0.** Versie 0.1.0 ondersteunt alleen-lezen
apparaatinventarisatie en installatieversies via de bijbehorende
[Cacti MCP-plugin](https://github.com/somethingwithproof/plugin_mcp).
Er is nog geen getagde release. Doctor-diagnostiek en herstelacties staan gepland voor toekomstige versies.

## Wat het beschikbaar maakt

| Bewerking | MCP-tool geleverd door de Cacti MCP-plugin |
|---|---|
| Apparaten weergeven die de eigenaar van het token mag zien | `cacti-list-devices` |
| Eén toegestaan apparaat uitlezen | `cacti-get-device` |
| Versies van Cacti, plugin en API uitlezen | `cacti-get-system-info` |

Namen, beschrijvingen en invoerschema's zijn afkomstig uit het op rechten gefilterde
discovery-antwoord van Cacti. Extra toegestane alleen-lezen providers kunnen worden
ontdekt zonder Python-toolhandlers toe te voegen.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Gebruikssituaties

Koppel een MCP-client om de Cacti-apparaten weer te geven die de toegewezen gebruiker
mag zien, één toegestaan apparaat op te zoeken, of installatieversies op te halen
wanneer de gebruiker over de vereiste beheerrechten beschikt. Namen en invoerschema's
komen uit het discovery-antwoord van de plugin, zodat de adapter niet elke provider
afzonderlijk hoeft te dupliceren. Raadpleeg de
[registratieregels voor abilities](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
van de plugin voor het registratiemodel en de huidige beperkingen.

## Overzicht van code en tests

| Gedrag | Implementatie | Testbewijs in deze repository |
|---|---|---|
| HTTPS-validatie, limieten, alleen-bearer-authenticatie en v2-paginering | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP-discovery, aanroepen en rechtenwijzigingen | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Command-line help, versie en ontbrekende configuratie | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

De subprocestest gebruikt een echte SDK-client en -server met een fixture-HTTP-endpoint.
Deze vereist of vervangt geen live integratiecontrole met Cacti.

## Hoe het veilig blijft

- Gebruikt de officiële [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  voor initialisatie, tool-discovery, aanroepen en stdio-framing.
- Stelt alleen abilities beschikbaar waarvan de annotaties exact alleen-lezen,
  niet-destructief en idempotent zijn. Schema's en namen komen uit Cacti; de adapter
  bevat geen SQL, apparaatinloggegevens of herstelopdrachten.
- Verstuurt alleen het bearer-token: geen cookies, geen CSRF-stap. De plugin
  controleert de geldigheid van het token en de rechten opnieuw bij elk verzoek.
- Gebruikt geverifieerde HTTPS, slaat nooit cookies op, weigert redirects en negeert
  proxy-omgevingsvariabelen. Gewone HTTP vereist `--allow-loopback-http` en een
  letterlijk loopback-adres of `localhost`.
- Begrenst API-aanroepen tot maximaal 35 seconden in totaal, 5 seconden voor het
  verbinden, 30 seconden netwerkinactiviteit en ongeveer 1 MB per antwoord
  (1.100.000 bytes). Request-bodies zijn beperkt tot 16.384 bytes. Aanroepen worden
  per clientsessie geserialiseerd.
- Controleert toolargumenten aan de hand van het invoerschema uit de laatste discovery
  voordat ze worden verzonden, en voert alleen ID's uit die voorkomen in die
  geverifieerde catalogus. Een afwijking, of een ongeldig schema van de server, wordt
  teruggegeven als een toolfout en veroorzaakt geen crash.
- Probeert uitvoering niet automatisch opnieuw. Toolfouten bevatten alleen de
  HTTP-status, de AIP-193 `status` en de ErrorInfo `reason`; nooit serverberichttekst,
  response-bodies of inloggegevens. Stdout is gereserveerd voor MCP-berichten.

De SDK-versie is vastgelegd in `uv.lock` (`mcp>=2.3,<3` in `pyproject.toml`). Deze
adapter gebruikt de 2.x low-level server met het stdio-transport; hij implementeert
geen extern MCP HTTP-endpoint, OAuth, resources, prompts, subscriptions of
achtergrondtaken.

Zie [het API-contract](../../../docs/api.md) en [het implementatieplan](../../../docs/plan.md).

## Installatie en command-line

Vereist Python 3.12 of hoger en [uv](https://docs.astral.sh/uv/).
Vanuit een checkout van deze repository:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Installeer en activeer de PHP-plugin, ken de bijbehorende realm toe aan een toegewijde
Cacti-gebruiker en maak voor die gebruiker een persoonlijk toegangstoken aan (formaat
`cmcp_pat_` gevolgd door 64 kleine hexadecimale tekens) in de console van de plugin, op
de pagina My MCP Tokens of met het commando `tokens.php`.
De bestaande Cacti-realms en apparaatrechten van de gebruiker blijven van toepassing.

Geef het token door via je secret manager als `CACTI_MCP_TOKEN`; zet het nooit in
versiebeheer of opdrachtregelargumenten. Stel het endpoint afzonderlijk in. Dit moet
een HTTPS-URL zijn die eindigt op `/plugins/mcp/api.php`, zonder inloggegevens, query
of fragment:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` stelt het endpoint in plaats van `CACTI_MCP_ENDPOINT` in.
`--allow-loopback-http` staat gewone HTTP toe naar `localhost`, `127.0.0.1` of `::1`
voor lokaal testen, `--lang LOCALE` overschrijft de lokalisatie van CLI-berichten en
`--version` drukt de versie af. Zonder zowel het endpoint als `CACTI_MCP_TOKEN` sluit
het commando af met een gebruiksfout.

### Lokalisatie

CLI-help en foutmeldingen van de adapter worden meegeleverd in 45 locales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) zonder extra afhankelijkheden. De locale-bepaling controleert eerst `--lang`, daarna `LC_ALL`, `LC_MESSAGES` en `LANG`, met `en` als terugvaloptie (`C`/`POSIX` en onbekende tags vallen ook terug op `en`). MCP-toolnamen, schema's en succesvolle JSON-toolpayloads blijven ongewijzigd; foutmeldingen van de adapter die worden geretourneerd met `is_error=True` volgen de actieve locale.

Het proces wacht op MCP-berichten op stdin. Normaal gesproken start een MCP-client dit proces.
Voor clients die het gangbare configuratieformaat `mcpServers` ondersteunen:

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

Configureer de client om `CACTI_MCP_ENDPOINT` en `CACTI_MCP_TOKEN` door te geven aan het
subproces via de omgevingsvariabelen of secret-voorziening van de client. Overerving van
omgevingsvariabelen hangt af van de client. Er is geen opdrachtregelvlag voor het token.

De afzonderlijk installeerbare Python-distributie levert het consolecommando `cacti-mcp`.
Publicatie op PyPI is niet vereist om de checkout uit te voeren. De PHP-plugin heeft geen
Python-afhankelijkheid.

## Releases

De distributieversie is vastgelegd in [pyproject.toml](../../../pyproject.toml).
Totdat er getagde releases beschikbaar zijn, kun je een broncheckout gebruiken of het
`python-distributions`-artifact van een geslaagde
[CI-run](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Het artifact bevat een wheel en een bronarchief. Het geïnstalleerde pakket levert zowel
het commando `cacti-mcp` als `python -m cacti_mcp`; het bevat niet de PHP-plugin.

## Ontwikkeling en tests

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

De tests dekken HTTP-validatie, isolatie van inloggegevens, verzoeken met alleen
bearer-tokens, paginering, redactie van fouten en een daadwerkelijke uitwisseling
tussen een SDK-client en -server in een subproces tegen een fixture-HTTP-server. Er is
geen live Cacti-installatie voor vereist.

De repository gebruikt `src/cacti_mcp/`, pytest, Ruff, uv en Hatchling. CI test Python
3.12, 3.13 en 3.14. Een afzonderlijke packaging-job bouwt het wheel en het bronarchief,
installeert het wheel buiten de checkout en voert smoke-tests uit op beide
ingangspunten. Distributies en testresultaten zijn workflow-artifacts.

## Bijdragen

Pull requests gaan naar `develop`. Houd de adapter compatibel met Python 3.12, volg de
bestaande Ruff-configuratie en de pakketindeling onder `src/cacti_mcp/`, en houd stdout
gereserveerd voor MCP-berichten. Voeg tests toe voor gewijzigd transport- of toolgedrag,
voer de bovenstaande controles uit en onderteken commits met `git commit -s`. Stem
API-wijzigingen af met de Cacti MCP-plugin en werk [docs/api.md](../../../docs/api.md) bij.

## Licentie

Copyright (C) 2026 Thomas Vincent. Uitgebracht onder de GNU General Public License,
versie 2 of hoger. Zie [LICENSE](../../../LICENSE).
