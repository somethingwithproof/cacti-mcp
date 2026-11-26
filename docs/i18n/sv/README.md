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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · **Svenska** · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP är en Python-adapter som exponerar funktionerna i
[Cacti MCP-insticksprogrammet](https://github.com/somethingwithproof/plugin_mcp) som MCP-verktyg
över stdio. Insticksprogrammet tillhandahåller redan MCP direkt över HTTP, så använd
det när din klient kan ansluta till en fjärrserver. Denna adapter är avsedd för
klienter som endast talar stdio. Den använder det officiella MCP-SDK:t för Python och
översätter verktygsanrop till insticksprogrammets HTTPS-API (funktionskontrakt v2, som tillhandahålls
under sökvägarna `/v1/`, endast bearer-token).
Cacti ansvarar för autentisering, behörighetskontroll, validering och exekvering.

**Status: under utveckling, före 1.0.** Version 0.1.0 stöder skrivskyddad
enhetsinventering och installationsversioner via det tillhörande
[Cacti MCP-insticksprogrammet](https://github.com/somethingwithproof/plugin_mcp).
Det finns ännu ingen taggad utgåva. Doktor-diagnostik och reparationer är planerade för framtiden.

## Vad den exponerar

| Åtgärd | MCP-verktyg som tillhandahålls av Cacti MCP-insticksprogrammet |
|---|---|
| Lista enheter som tokeninnehavaren får se | `cacti-list-devices` |
| Läs en tillåten enhet | `cacti-get-device` |
| Läs versioner av Cacti, insticksprogram och API | `cacti-get-system-info` |

Namn, beskrivningar och indatascheman kommer från Cactis behörighetsfiltrerade
upptäcktssvar. Ytterligare tillåtna skrivskyddade leverantörer kan upptäckas
utan att några Python-verktygshanterare behöver läggas till.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Användningsområden

Anslut en MCP-klient för att lista de Cacti-enheter som dess dedikerade användare får se,
slå upp en tillåten enhet eller hämta installationsversioner när användaren
har den administrativa behörighetssfär som krävs. Namn och indatascheman kommer från
insticksprogrammets upptäcktssvar, så adaptern duplicerar inte varje leverantör.
Se insticksprogrammets
[regler för funktionsregistrering](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
för registreringsmodellen och aktuella begränsningar.

## Kod- och testöversikt

| Beteende | Implementation | Testunderlag i detta arkiv |
|---|---|---|
| HTTPS-validering, gränser, autentisering med endast bearer-token och v2-sidindelning | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP-upptäckt, anrop och behörighetsändringar | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Kommandoradshjälp, version och saknad konfiguration | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Delprocesstestet använder en riktig SDK-klient och -server med en HTTP-testslutpunkt.
Det kräver eller ersätter inte en integrationskontroll mot en skarp Cacti-installation.

## Säkerhetsmekanismer

- Använder det officiella [`mcp` Python-SDK:t](https://github.com/modelcontextprotocol/python-sdk)
  för initiering, verktygsupptäckt, anrop och stdio-inramning.
- Exponerar endast funktioner vars annoteringar är exakt skrivskyddade, icke-destruktiva och idempotenta. Scheman och namn kommer
  från Cacti; adaptern innehåller ingen SQL, inga enhetsinloggningsuppgifter och inga reparationskommandon.
- Skickar endast bearer-token: inga kakor, inget CSRF-steg. Insticksprogrammet kontrollerar
  tokenets giltighet och behörigheter på nytt vid varje begäran.
- Använder verifierad HTTPS, lagrar aldrig kakor, nekar omdirigeringar och
  ignorerar proxy-miljövariabler. HTTP kräver `--allow-loopback-http`
  och en bokstavlig loopback-adress eller `localhost`.
- Begränsar API-anrop till totalt 35 sekunder, 5 sekunder för anslutning, 30 sekunder av
  nätverksinaktivitet och cirka 1 MB per svar (1 100 000 byte).
  Förfrågningars kroppar är begränsade till 16 384 byte. Anrop serialiseras per
  klientsession.
- Kontrollerar verktygsargument mot indataschemat från den senaste upptäckten innan
  de skickas och exekverar endast ID:n från den verifierade katalogen. En avvikelse, eller
  ett felaktigt schema från servern, kommer tillbaka som ett verktygsfel, inte en krasch.
- Gör inga automatiska omförsök vid exekvering. Verktygsfel innehåller endast HTTP-status,
  AIP-193 `status` och ErrorInfo `reason`; aldrig serverns
  meddelandetext, svarskroppar eller inloggningsuppgifter. Stdout är reserverad för MCP-meddelanden.

SDK-versionen är låst via `uv.lock` (`mcp>=2.3,<3` i `pyproject.toml`). Denna
adapter använder dess lågnivåserver för 2.x med stdio-transport; den implementerar
inte en fjärransluten MCP HTTP-slutpunkt, OAuth, resurser,
prompter, prenumerationer eller bakgrundsuppgifter.

Se [API-kontraktet](../../../docs/api.md) och [implementationsplanen](../../../docs/plan.md).

## Installation och kommandorad

Kräver Python 3.12 eller senare och [uv](https://docs.astral.sh/uv/).
Från en utcheckning av detta arkiv:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Installera och aktivera PHP-insticksprogrammet, tilldela dess behörighetssfär till en dedikerad Cacti-användare
och skapa en personlig åtkomsttoken för den användaren (format `cmcp_pat_` följt
av 64 gemena hexadecimala tecken) i insticksprogrammets konsol, på sidan My MCP Tokens
eller med kommandot `tokens.php`.
Användarens befintliga Cacti-sfärer och enhetsbehörigheter gäller fortfarande.

Tillhandahåll tokenet via din hemlighetshanterare som `CACTI_MCP_TOKEN`; lägg aldrig till det
i versionshantering eller kommandoargument. Ange slutpunkten separat. Det måste vara en
HTTPS-URL som slutar med `/plugins/mcp/api.php`, utan inloggningsuppgifter, frågesträng eller
fragment:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` anger slutpunkten i stället för `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` tillåter okrypterad HTTP till `localhost`, `127.0.0.1` eller `::1`
för lokal testning, `--lang LOCALE` åsidosätter lokaliseringen av CLI-meddelanden och
`--version` skriver ut versionen. Utan både slutpunkten och `CACTI_MCP_TOKEN`
avslutas kommandot med ett användningsfel.

### Lokalisering

CLI-hjälp och adapterns felmeddelanden levereras på 45 språkversioner (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) utan ytterligare beroenden. Språkupplösningen
kontrollerar `--lang`, sedan `LC_ALL`, `LC_MESSAGES` och `LANG`, och faller
tillbaka till `en` (`C`/`POSIX` och okända taggar löses också till `en`). Namn på MCP-verktyg,
scheman och lyckade JSON-svar påverkas inte; adapterns felmeddelanden
som returneras med `is_error=True` följer den aktiva språkversionen.

Processen väntar på MCP-meddelanden på stdin. Normalt startas den av en MCP-klient.
För klienter som accepterar det vanliga konfigurationsformatet `mcpServers`:

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

Konfigurera klienten att skicka `CACTI_MCP_ENDPOINT` och `CACTI_MCP_TOKEN` till
delprocessen via dess miljö eller hemlighetshantering. Miljöarv
beror på klienten. Det finns ingen kommandoradsflagga för token.

Den separat installerbara Python-distributionen tillhandahåller konsolkommandot `cacti-mcp`.
Ingen PyPI-publicering krävs för att köra utcheckningen. PHP-insticksprogrammet har
inget Python-beroende.

## Utgåvor

Distributionsversionen anges i [pyproject.toml](../../../pyproject.toml).
Tills taggade utgåvor finns tillgängliga kan du använda en källkodsutcheckning eller
artefakten `python-distributions` från en lyckad
[CI-körning](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Artefakten innehåller ett wheel-paket och källarkiv. Det installerade paketet tillhandahåller
både kommandot `cacti-mcp` och `python -m cacti_mcp`; det innehåller inte
PHP-insticksprogrammet.

## Utveckling och tester

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Testerna omfattar HTTP-validering, isolering av inloggningsuppgifter, förfrågningar med endast bearer-token,
sidindelning, maskering av felmeddelanden samt ett verkligt SDK-klient/server-delprocessutbyte mot
en HTTP-testserver. De kräver ingen aktiv Cacti-installation.

Arkivet använder `src/cacti_mcp/`, pytest, Ruff, uv och Hatchling. CI testar
Python 3.12, 3.13 och 3.14. Ett separat paketeringsjobb bygger wheel-paketet
och källarkivet, installerar wheel-paketet utanför utcheckningen och röktestar
båda startpunkterna. Distributioner och testresultat är arbetsflödesartefakter.

## Bidra

Pull requests riktas mot `develop`. Håll adaptern kompatibel med Python 3.12,
följ den befintliga Ruff-konfigurationen och paketstrukturen `src/cacti_mcp/` och
håll stdout reserverad för MCP-meddelanden. Lägg till tester för ändrat transport- eller
verktygsbeteende, kör kontrollerna ovan och signera commits med `git commit -s`.
Samordna API-ändringar med Cacti MCP-insticksprogrammet och uppdatera [docs/api.md](../../../docs/api.md).

## Licens

Copyright (C) 2026 Thomas Vincent. Släppt under GNU General Public
License, version 2 eller senare. Se [LICENSE](../../../LICENSE).
