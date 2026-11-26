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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · **Polski** · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP to adapter w języku Python, który udostępnia możliwości
[wtyczki Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) jako
narzędzia MCP przez stdio. Wtyczka obsługuje już MCP bezpośrednio przez HTTP,
więc korzystaj z tego trybu zawsze, gdy Twój klient może połączyć się ze
zdalnym serwerem. Ten adapter jest przeznaczony dla klientów komunikujących się
wyłącznie przez stdio. Wykorzystuje oficjalne SDK MCP dla Pythona i tłumaczy
wywołania narzędzi na wywołania HTTPS API wtyczki (kontrakt abilities v2,
udostępniany pod ścieżkami `/v1/`, wyłącznie z tokenem bearer).
Cacti odpowiada za uwierzytelnianie, autoryzację, walidację oraz wykonanie.

**Status: w trakcie rozwoju, przed wersją 1.0.** Wersja 0.1.0 obsługuje
inwentaryzację urządzeń w trybie tylko do odczytu oraz odczyt wersji instalacji
za pośrednictwem towarzyszącej
[wtyczki Cacti MCP](https://github.com/somethingwithproof/plugin_mcp).
Nie ma jeszcze oznaczonego wydania (taga). Diagnostyka typu doctor i funkcje
naprawcze są planowane na przyszłość.

## Co udostępnia

| Operacja | Narzędzie MCP dostarczane przez wtyczkę Cacti MCP |
|---|---|
| Wyświetlenie listy urządzeń widocznych dla właściciela tokenu | `cacti-list-devices` |
| Odczyt jednego dozwolonego urządzenia | `cacti-get-device` |
| Odczyt wersji Cacti, wtyczki oraz API | `cacti-get-system-info` |

Nazwy, opisy oraz schematy wejściowe pochodzą z odpowiedzi wykrywania (discovery)
Cacti filtrowanej pod kątem uprawnień. Dodatkowi dozwoleni dostawcy w trybie
tylko do odczytu mogą być wykrywani bez dopisywania handlerów narzędzi w Pythonie.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Przypadki użycia

Podłącz klienta MCP, aby wyświetlić listę urządzeń Cacti widocznych dla
dedykowanego użytkownika, wyszukać jedno dozwolone urządzenie lub pobrać wersje
instalacji, gdy użytkownik posiada wymaganą domenę uprawnień administracyjnych
(realm). Nazwy i schematy wejściowe pochodzą z odpowiedzi discovery wtyczki,
dzięki czemu adapter nie powiela definicji każdego dostawcy.
Zobacz
[reguły rejestracji możliwości (ability)](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
wtyczki, aby poznać model rejestracji i obecne ograniczenia.

## Mapa kodu i testów

| Zachowanie | Implementacja | Dowody testowe w tym repozytorium |
|---|---|---|
| Walidacja HTTPS, limity, uwierzytelnianie wyłącznie tokenem bearer i stronicowanie v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Wykrywanie MCP, wywołania i zmiany uprawnień | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Pomoc wiersza poleceń, wersja i brakująca konfiguracja | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Test podprocesu wykorzystuje rzeczywistego klienta i serwer SDK z testowym
punktem końcowym HTTP (fixture). Nie wymaga ani nie zastępuje testu
integracyjnego z działającą instancją Cacti.

## Jak zachowuje bezpieczeństwo

- Wykorzystuje oficjalne [SDK `mcp` dla Pythona](https://github.com/modelcontextprotocol/python-sdk)
  do inicjalizacji, wykrywania narzędzi, wywołań oraz ramkowania stdio.
- Udostępnia wyłącznie możliwości (abilities), których adnotacje określają je
  dokładnie jako tylko do odczytu, niedestrukcyjne i idempotentne. Schematy oraz
  nazwy pochodzą z Cacti; adapter nie zawiera zapytań SQL, poświadczeń urządzeń
  ani poleceń naprawczych.
- Wysyła wyłącznie token bearer: bez plików cookie i bez kroku CSRF. Wtyczka
  ponownie sprawdza ważność tokenu oraz uprawnienia przy każdym żądaniu.
- Korzysta ze zweryfikowanego HTTPS, nigdy nie zapisuje plików cookie, odrzuca
  przekierowania oraz ignoruje zmienne środowiskowe proxy. Zwykłe HTTP wymaga
  flagi `--allow-loopback-http` oraz dosłownego adresu loopback lub `localhost`.
- Ogranicza wywołania API do 35 sekund łącznie, 5 sekund na nawiązanie
  połączenia, 30 sekund bezczynności sieciowej oraz około 1 MB na odpowiedź
  (1 100 000 bajtów). Treści żądań są ograniczone do 16 384 bajtów. Wywołania
  są serializowane w ramach sesji klienta.
- Sprawdza argumenty narzędzi względem schematu wejściowego z ostatniego
  wykrywania przed ich wysłaniem i wykonuje wyłącznie identyfikatory z tego
  zweryfikowanego katalogu. Niezgodność lub nieprawidłowy schemat z serwera
  zwracane są jako błąd narzędzia, a nie awaria procesu.
- Nie ponawia wykonania automatycznie. Błędy narzędzi przekazują wyłącznie kod
  statusu HTTP, pole `status` zgodne z AIP-193 oraz pole `reason` z ErrorInfo;
  nigdy treści komunikatów serwera, ciał odpowiedzi ani poświadczeń. Wyjście
  stdout jest zarezerwowane dla komunikatów MCP.

Wersja SDK jest przypięta w pliku `uv.lock` (`mcp>=2.3,<3` w `pyproject.toml`).
Ten adapter używa jego niskopoziomowego serwera 2.x z transportem stdio; nie
implementuje zdalnego punktu końcowego MCP HTTP, OAuth, zasobów, promptów,
subskrypcji ani zadań w tle.

Zobacz [kontrakt API](../../../docs/api.md) oraz [plan implementacji](../../../docs/plan.md).

## Instalacja i wiersz poleceń

Wymaga Pythona 3.12 lub nowszego oraz narzędzia [uv](https://docs.astral.sh/uv/).
Z poziomu lokalnej kopii tego repozytorium:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Zainstaluj i włącz wtyczkę PHP, przyznaj jej domenę uprawnień (realm)
dedykowanemu użytkownikowi Cacti i utwórz dla niego osobisty token dostępu
(format `cmcp_pat_` oraz następujące po nim 64 małe cyfry szesnastkowe) w
konsoli wtyczki, na stronie My MCP Tokens lub za pomocą polecenia `tokens.php`.
Dotychczasowe uprawnienia realm i uprawnienia do urządzeń użytkownika w Cacti
nadal obowiązują.

Przekaż token przez menedżer sekretów jako `CACTI_MCP_TOKEN`; nigdy nie
umieszczaj go w systemie kontroli wersji ani w argumentach poleceń. Osobno
ustaw punkt końcowy. Musi to być adres URL HTTPS zakończony na
`/plugins/mcp/api.php`, bez poświadczeń, parametrów zapytania ani fragmentu:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` ustawia punkt końcowy zamiast zmiennej `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` zezwala na zwykłe HTTP dla `localhost`, `127.0.0.1`
lub `::1` do testów lokalnych, `--lang LOCALE` nadpisuje lokalizację komunikatów
CLI, a `--version` wypisuje wersję. Bez podania zarówno punktu końcowego, jak i
`CACTI_MCP_TOKEN`, polecenie kończy działanie błędem użycia.

### Lokalizacja

Pomoc CLI oraz komunikaty błędów adaptera są dostarczane w 45 językach (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) bez żadnych dodatkowych zależności. Rozpoznawanie języka sprawdza najpierw `--lang`, następnie `LC_ALL`, `LC_MESSAGES` i `LANG`, z powrotem do `en` (`C`/`POSIX` oraz nieznane tagi również rozwiązują się do `en`). Nazwy narzędzi MCP, schematy oraz poprawne odpowiedzi JSON narzędzi pozostają niezmienione; komunikaty błędów adaptera zwracane z `is_error=True` stosują się do aktywnej lokalizacji.

Proces oczekuje na komunikaty MCP na stdin. Zazwyczaj uruchamia go klient MCP.
Dla klientów akceptujących popularny format konfiguracji `mcpServers`:

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

Skonfiguruj klienta tak, aby przekazywał `CACTI_MCP_ENDPOINT` oraz
`CACTI_MCP_TOKEN` do podprocesu poprzez swoje środowisko lub mechanizm sekretów.
Dziedziczenie środowiska zależy od klienta. Nie istnieje flaga wiersza poleceń
dla tokenu.

Oddzielnie instalowalna dystrybucja Pythona dostarcza polecenie konsolowe
`cacti-mcp`. Do uruchomienia lokalnej kopii repozytorium nie jest wymagana
publikacja w PyPI. Wtyczka PHP nie ma zależności od Pythona.

## Wydania

Wersja dystrybucji jest zapisana w [pyproject.toml](../../../pyproject.toml).
Do czasu udostępnienia oznaczonych wydań korzystaj ze źródeł z repozytorium lub
z artefaktu `python-distributions` z udanego
[uruchomienia CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Artefakt zawiera pakiet wheel oraz archiwum źródłowe. Zainstalowany pakiet
dostarcza zarówno polecenie `cacti-mcp`, jak i `python -m cacti_mcp`; nie zawiera
wtyczki PHP.

## Rozwój i testy

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Testy obejmują walidację HTTP, izolację poświadczeń, żądania wyłącznie z tokenem
bearer, stronicowanie, redakcję błędów oraz rzeczywistą wymianę komunikatów
podprocesu klient/serwer SDK względem testowego serwera HTTP (fixture). Nie
wymagają działającej instalacji Cacti.

Repozytorium używa `src/cacti_mcp/`, pytest, Ruff, uv oraz Hatchling. CI testuje
Pythona 3.12, 3.13 i 3.14. Osobne zadanie budowania pakietów tworzy wheel oraz
archiwum źródłowe, instaluje wheel poza katalogiem roboczym i przeprowadza
smoke-test obu punktów wejścia. Dystrybucje oraz wyniki testów są artefaktami
przepływu pracy (workflow).

## Współpraca

Pull requesty kieruj na gałąź `develop`. Zachowaj zgodność adaptera z Pythonem
3.12, przestrzegaj istniejącej konfiguracji Ruff oraz układu pakietu
`src/cacti_mcp/`, a także pozostaw stdout zarezerwowane dla komunikatów MCP.
Dodaj testy dla zmienionego zachowania transportu lub narzędzi, uruchom powyższe
sprawdzenia i podpisuj commity za pomocą `git commit -s`.
Zmiany w API koordynuj z wtyczką Cacti MCP i aktualizuj [docs/api.md](../../../docs/api.md).

## Licencja

Copyright (C) 2026 Thomas Vincent. Udostępniono na licencji GNU General Public
License, wersja 2 lub nowsza. Zobacz [LICENSE](../../../LICENSE).
