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

**Languages:** [English](../../../README.md) · **Deutsch** · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP ist ein Python-Adapter, der die Fähigkeiten des
[Cacti-MCP-Plugins](https://github.com/somethingwithproof/plugin_mcp) als MCP-Tools
über stdio bereitstellt. Das Plugin bietet MCP bereits direkt über HTTP an; nutzen Sie
diesen Weg, wenn Ihr Client eine Verbindung zu einem Remote-Server herstellen kann. Dieser Adapter ist für
Clients gedacht, die nur stdio sprechen. Er verwendet das offizielle Python-MCP-SDK und
übersetzt Tool-Aufrufe in die HTTPS-API des Plugins (Abilities Contract v2, bereitgestellt
unter `/v1/`-Pfaden, nur mit Bearer-Token).
Cacti übernimmt Authentifizierung, Autorisierung, Validierung und Ausführung.

**Status: in Entwicklung, vor Version 1.0.** Version 0.1.0 unterstützt die schreibgeschützte
Abfrage des Geräteinventars und der Installationsversionen über das zugehörige
[Cacti-MCP-Plugin](https://github.com/somethingwithproof/plugin_mcp).
Es gibt noch kein getaggtes Release. Doctor-Diagnosen und Reparaturen sind für zukünftige Versionen geplant.

## Bereitgestellte Funktionen

| Vorgang | Vom Cacti-MCP-Plugin bereitgestelltes MCP-Tool |
|---|---|
| Geräte auflisten, die der Token-Eigentümer sehen darf | `cacti-list-devices` |
| Ein freigegebenes Gerät auslesen | `cacti-get-device` |
| Cacti-, Plugin- und API-Versionen auslesen | `cacti-get-system-info` |

Namen, Beschreibungen und Eingabeschemas stammen aus der berechtigungsgefilterten
Discovery-Antwort von Cacti. Weitere zulässige schreibgeschützte Provider können erkannt werden,
ohne dass Python-Tool-Handler hinzugefügt werden müssen.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Anwendungsfälle

Verbinden Sie einen MCP-Client, um die Cacti-Geräte aufzulisten, die der zugehörige dedizierte Benutzer sehen darf,
ein freigegebenes Gerät abzufragen oder Installationsversionen abzurufen, sofern der Benutzer
über den erforderlichen administrativen Realm verfügt. Namen und Eingabeschemas stammen aus
der Discovery-Antwort des Plugins, sodass der Adapter die einzelnen Provider nicht dupliziert.
Informationen zum Registrierungsmodell und den aktuellen Einschränkungen finden Sie in den
[Regeln zur Registrierung von Abilities](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
des Plugins.

## Code- und Testübersicht

| Verhalten | Implementierung | Testnachweis in diesem Repository |
|---|---|---|
| HTTPS-Validierung, Begrenzungen, reine Bearer-Authentifizierung und v2-Paging | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP-Discovery, Aufrufe und Berechtigungsänderungen | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Kommandozeilenhilfe, Version und fehlende Konfiguration | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Der Subprozess-Test verwendet einen echten SDK-Client und -Server mit einem Fixture-HTTP-Endpunkt.
Eine Live-Integrationsprüfung mit Cacti ist dafür nicht erforderlich und wird dadurch nicht ersetzt.

## Sicherheitskonzept

- Verwendet das offizielle [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  für Initialisierung, Tool-Discovery, Aufrufe und stdio-Framing.
- Stellt ausschließlich Abilities bereit, deren Annotationen exakt schreibgeschützt, nicht-destruktiv und idempotent sind. Schemas und Namen stammen
  von Cacti; der Adapter enthält weder SQL noch Geräte-Zugangsdaten oder Reparaturbefehle.
- Sendet ausschließlich das Bearer-Token: keine Cookies, kein CSRF-Schritt. Das Plugin prüft
  die Gültigkeit des Tokens und die Berechtigungen bei jeder Anfrage erneut.
- Verwendet verifiziertes HTTPS, speichert niemals Cookies, lehnt Weiterleitungen ab und
  ignoriert Proxy-Umgebungsvariablen. Für HTTP sind `--allow-loopback-http`
  sowie eine literale Loopback-Adresse oder `localhost` erforderlich.
- Begrenzt API-Aufrufe auf insgesamt 35 Sekunden, 5 Sekunden für den Verbindungsaufbau, 30 Sekunden bei
  Netzwerk-Inaktivität und etwa 1 MB pro Antwort (1.100.000 Bytes).
  Anfrage-Bodys sind auf 16.384 Bytes begrenzt. Aufrufe werden pro Client-Sitzung
  serialisiert.
- Prüft Tool-Argumente vor dem Senden gegen das Eingabeschema der letzten Discovery und
  führt nur IDs aus diesem verifizierten Katalog aus. Eine Abweichung oder
  ein fehlerhaftes Schema vom Server kommt als Tool-Fehler zurück, nicht als Absturz.
- Wiederholt fehlgeschlagene Ausführungen nicht automatisch. Tool-Fehler enthalten nur den HTTP-Status,
  den AIP-193-`status` und den ErrorInfo-`reason`; niemals Server-Meldungstexte,
  Antwort-Bodys oder Zugangsdaten. Stdout ist für MCP-Nachrichten reserviert.

Die SDK-Version ist durch `uv.lock` fixiert (`mcp>=2.3,<3` in `pyproject.toml`). Dieser
Adapter verwendet dessen 2.x Low-Level-Server mit dem stdio-Transport; er implementiert
keinen Remote-MCP-HTTP-Endpunkt, kein OAuth, keine Ressourcen,
Prompts, Subscriptions oder Hintergrundaufgaben.

Siehe [den API-Vertrag](../../../docs/api.md) und den [Implementierungsplan](../../../docs/plan.md).

## Installation und Kommandozeile

Erfordert Python 3.12 oder neuer und [uv](https://docs.astral.sh/uv/).
Aus einem Checkout dieses Repositorys:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Installieren und aktivieren Sie das PHP-Plugin, weisen Sie dessen Realm einem dedizierten Cacti-Benutzer zu
und erstellen Sie für diesen Benutzer ein persönliches Zugriffstoken (Format `cmcp_pat_` gefolgt
von 64 kleingeschriebenen Hexadezimalziffern) in der Konsole des Plugins, auf der Seite My MCP Tokens
oder mit dem Befehl `tokens.php`.
Die bestehenden Cacti-Realms und Geräteberechtigungen des Benutzers gelten weiterhin.

Stellen Sie das Token über Ihren Secret-Manager als `CACTI_MCP_TOKEN` bereit; fügen Sie es niemals
der Versionskontrolle oder Kommandozeilenargumenten hinzu. Legen Sie den Endpunkt separat fest. Es muss eine
HTTPS-URL sein, die auf `/plugins/mcp/api.php` endet, ohne Zugangsdaten, Query-Parameter oder
Fragment:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` legt den Endpunkt anstelle von `CACTI_MCP_ENDPOINT` fest.
`--allow-loopback-http` erlaubt unverschlüsseltes HTTP zu `localhost`, `127.0.0.1` oder `::1`
für lokale Tests, `--lang LOCALE` überschreibt die Lokalisierung der CLI-Meldungen und
`--version` gibt die Version aus. Fehlen entweder der Endpunkt oder `CACTI_MCP_TOKEN`,
beendet sich der Befehl mit einem Verwendungsfehler.

### Lokalisierung

CLI-Hilfe und Adapter-Fehlermeldungen werden in 45 Locales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ohne zusätzliche Abhängigkeiten ausgeliefert. Die Locale-Auflösung
prüft `--lang`, dann `LC_ALL`, `LC_MESSAGES` und `LANG` und fällt
auf `en` zurück (`C`/`POSIX` und unbekannte Tags werden ebenfalls zu `en` aufgelöst). Namen von MCP-Tools,
Schemas und erfolgreiche JSON-Tool-Payloads bleiben unverändert; mit `is_error=True` zurückgegebene
Adapter-Fehlermeldungen folgen der aktiven Locale.

Der Prozess wartet auf MCP-Nachrichten über stdin. Normalerweise startet ein MCP-Client ihn.
Für Clients, die das gängige Konfigurationsformat `mcpServers` unterstützen:

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

Konfigurieren Sie den Client so, dass er `CACTI_MCP_ENDPOINT` und `CACTI_MCP_TOKEN` über seine
Umgebung oder Secret-Verwaltung an den Subprozess weitergibt. Die Vererbung von Umgebungsvariablen
hängt vom jeweiligen Client ab. Es gibt kein Kommandozeilen-Flag für das Token.

Die separat installierbare Python-Distribution stellt den Konsolenbefehl `cacti-mcp`
bereit. Für die Ausführung aus dem Checkout ist keine Veröffentlichung auf PyPI erforderlich. Das PHP-Plugin hat
keine Python-Abhängigkeit.

## Releases

Die Distributionsversion ist in [pyproject.toml](../../../pyproject.toml) hinterlegt.
Bis getaggte Releases verfügbar sind, verwenden Sie einen Source-Checkout oder das
Artefakt `python-distributions` aus einem erfolgreichen
[CI-Lauf](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Das Artefakt enthält ein Wheel und ein Quellarchiv. Das installierte Paket stellt
sowohl den Befehl `cacti-mcp` als auch `python -m cacti_mcp` bereit; es enthält nicht das
PHP-Plugin.

## Entwicklung und Tests

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Tests decken HTTP-Validierung, Isolierung von Zugangsdaten, reine Bearer-Anfragen,
Paging, Fehler-Schwärzung sowie einen echten Subprozess-Austausch zwischen SDK-Client und -Server gegen
einen Fixture-HTTP-Server ab. Sie erfordern keine laufende Cacti-Installation.

Das Repository verwendet `src/cacti_mcp/`, pytest, Ruff, uv und Hatchling. Die CI testet
Python 3.12, 3.13 und 3.14. Ein separater Paketierungs-Job erstellt das Wheel
und das Quellarchiv, installiert das Wheel außerhalb des Checkouts und führt Smoke-Tests
für beide Einstiegspunkte durch. Distributionen und Testergebnisse sind Workflow-Artefakte.

## Mitwirken

Pull Requests gehen an `develop`. Halten Sie den Adapter mit Python 3.12 kompatibel,
folgen Sie der bestehenden Ruff-Konfiguration sowie der Paketstruktur `src/cacti_mcp/` und
halten Sie stdout für MCP-Nachrichten reserviert. Fügen Sie Tests für geändertes Transport- oder Tool-Verhalten
hinzu, führen Sie die oben genannten Prüfungen aus und signieren Sie Commits mit `git commit -s`.
Stimmen Sie API-Änderungen mit dem Cacti-MCP-Plugin ab und aktualisieren Sie [docs/api.md](../../../docs/api.md).

## Lizenz

Copyright (C) 2026 Thomas Vincent. Veröffentlicht unter der GNU General Public
License, Version 2 oder neuer. Siehe [LICENSE](../../../LICENSE).
