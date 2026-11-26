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

<details><summary>More languages (28 locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · **Bosanski** · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Hrvatski](../hr/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Српски](../sr/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP je Python adapter koji izlaže mogućnosti
[Cacti MCP dodatka](https://github.com/somethingwithproof/plugin_mcp) kao MCP
alate putem stdio. Dodatak već direktno poslužuje MCP putem HTTP-a, pa koristite
tu opciju kada se vaš klijent može povezati na udaljeni server. Ovaj adapter je
namijenjen klijentima koji komuniciraju isključivo putem stdio. Koristi službeni
Python MCP SDK i prevodi pozive alata u HTTPS API dodatka (ugovor mogućnosti v2,
poslužen na `/v1/` putanjama, samo uz bearer token).
Cacti upravlja autentifikacijom, autorizacijom, provjerom i izvršavanjem.

**Status: u razvoju, prije verzije 1.0.** Verzija 0.1.0 podržava inventar
uređaja samo za čitanje i verzije instalacije putem pratećeg
[Cacti MCP dodatka](https://github.com/somethingwithproof/plugin_mcp).
Još uvijek nema označenog izdanja. Dijagnostika (doctor) i popravke planirane su za budućnost.

## Šta izlaže

| Operacija | MCP alat koji pruža Cacti MCP dodatak |
|---|---|
| Prikaz liste uređaja koje vlasnik tokena smije vidjeti | `cacti-list-devices` |
| Čitanje jednog dozvoljenog uređaja | `cacti-get-device` |
| Čitanje verzija Cactija, dodatka i API-ja | `cacti-get-system-info` |

Nazivi, opisi i ulazne šeme dolaze iz odgovora otkrivanja (discovery) koji Cacti
filtrira prema dozvolama. Dodatni dozvoljeni pružaoci samo za čitanje mogu se
otkriti bez dodavanja Python rukovalaca alata.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Primjeri upotrebe

Povežite MCP klijent da biste izlistali Cacti uređaje koje njegov namjenski
korisnik smije vidjeti, pronašli jedan dozvoljeni uređaj ili preuzeli verzije
instalacije kada korisnik ima potrebnu administrativnu oblast (realm). Nazivi i
ulazne šeme dolaze iz odgovora otkrivanja dodatka, tako da adapter ne duplicira
svakog pružaoca. Pogledajte
[pravila registracije mogućnosti](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
dodatka za model registracije i trenutna ograničenja.

## Mapa koda i testova

| Ponašanje | Implementacija | Testna pokrivenost u ovom repozitoriju |
|---|---|---|
| HTTPS provjera, ograničenja, autentifikacija samo bearer tokenom i v2 straničenje | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP otkrivanje, pozivi i promjene dozvola | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Pomoć komandne linije, verzija i nedostajuće postavke | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Test podprocesa koristi stvarni SDK klijent i server s testnom HTTP krajnjom
tačkom. On ne zahtijeva niti zamjenjuje integracijsku provjeru sa stvarnom Cacti
instalacijom.

## Kako ostaje siguran

- Koristi službeni [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  za inicijalizaciju, otkrivanje alata, pozive i stdio uokvirivanje.
- Izlaže samo mogućnosti čije su anotacije strogo samo za čitanje, nedestruktivne
  i idempotentne. Šeme i nazivi dolaze iz Cactija; adapter ne sadrži SQL,
  kredencijale uređaja niti komande za popravku.
- Šalje samo bearer token: bez kolačića (cookies) i bez CSRF koraka. Dodatak pri
  svakom zahtjevu ponovo provjerava valjanost tokena i dozvole.
- Koristi provjereni HTTPS, nikada ne pohranjuje kolačiće, odbija preusmjeravanja
  i zanemaruje varijable okruženja za proxy. HTTP zahtijeva `--allow-loopback-http`
  i doslovnu loopback adresu ili `localhost`.
- Ograničava API pozive na ukupno 35 sekundi, 5 sekundi za uspostavljanje veze,
  30 sekundi mrežne neaktivnosti i približno 1 MB po odgovoru (1.100.000 bajtova).
  Tijela zahtjeva ograničena su na 16.384 bajta. Pozivi se serijaliziraju po
  klijentskoj sesiji.
- Provjerava argumente alata u odnosu na ulaznu šemu iz posljednjeg otkrivanja
  prije slanja i izvršava samo identifikatore iz tog provjerenog kataloga.
  Nepodudaranje ili neispravna šema sa servera vraća se kao greška alata, a ne
  kao pad programa.
- Ne ponavlja izvršavanje automatski. Greške alata nose samo HTTP status,
  AIP-193 `status` i ErrorInfo `reason`; nikada tekst poruke servera, tijela
  odgovora ili kredencijale. Stdout je rezervisan za MCP poruke.

Verzija SDK-a zaključana je u datoteci `uv.lock` (`mcp>=2.3,<3` u
`pyproject.toml`). Ovaj adapter koristi njegov niskonivovski 2.x server sa stdio
transportom; ne implementira udaljenu MCP HTTP krajnju tačku, OAuth, resurse,
promptove, pretplate niti pozadinske zadatke.

Pogledajte [API ugovor](../../../docs/api.md) i [plan implementacije](../../../docs/plan.md).

## Instalacija i komandna linija

Zahtijeva Python 3.12 ili noviji i [uv](https://docs.astral.sh/uv/).
Iz lokalne kopije ovog repozitorija:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Instalirajte i omogućite PHP dodatak, dodijelite njegovu oblast (realm)
namjenskom Cacti korisniku i kreirajte lični pristupni token za tog korisnika
(oblik `cmcp_pat_` praćen sa 64 mala heksadecimalna znaka) u konzoli dodatka, na
stranici My MCP Tokens ili pomoću komande `tokens.php`.
Postojeće Cacti oblasti i dozvole za uređaje tog korisnika ostaju na snazi.

Proslijedite token putem svog upravitelja tajni kao `CACTI_MCP_TOKEN`; nikada ga
ne dodajte u sistem za kontrolu verzija niti u argumente komandne linije. Krajnju
tačku postavite zasebno. To mora biti HTTPS URL koji završava na
`/plugins/mcp/api.php`, bez kredencijala, upitnog niza ili fragmenta:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` postavlja krajnju tačku umjesto varijable `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` dozvoljava obični HTTP prema `localhost`, `127.0.0.1` ili
`::1` za lokalno testiranje, `--lang LOCALE` zamjenjuje lokalizaciju CLI poruka,
a `--version` ispisuje verziju. Bez obje vrijednosti, krajnje tačke i
`CACTI_MCP_TOKEN`, komanda završava s greškom upotrebe.

### Lokalizacija

Pomoć komandne linije i poruke o greškama adaptera isporučuju se na 48 lokaliteta
(`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`, `bs`, `hr`, `sr`)
bez ikakvih dodatnih ovisnosti. Određivanje lokaliteta provjerava `--lang`, zatim
`LC_ALL`, `LC_MESSAGES` i `LANG`, uz povratak na `en` (`C`/`POSIX` i nepoznate
oznake također se svode na `en`). Nazivi MCP alata, šeme i uspješni JSON
odgovori alata ostaju nepromijenjeni; poruke o greškama adaptera vraćene sa
`is_error=True` prate aktivni lokalitet.

Proces čeka MCP poruke na stdin. Obično ga pokreće MCP klijent. Za klijente koji
prihvataju uobičajeni format postavki `mcpServers`:

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

Podesite klijent da prosljeđuje `CACTI_MCP_ENDPOINT` i `CACTI_MCP_TOKEN`
podprocesu putem okruženja ili sistema za tajne. Nasljeđivanje okruženja zavisi
od klijenta. Ne postoji zastavica komandne linije za token.

Zasebno instalabilna Python distribucija pruža konzolnu komandu `cacti-mcp`.
Objava na PyPI-ju nije potrebna za pokretanje iz lokalne kopije. PHP dodatak nema
ovisnost o Pythonu.

## Izdanja

Verzija distribucije zabilježena je u datoteci [pyproject.toml](../../../pyproject.toml).
Dok označena izdanja ne budu dostupna, koristite lokalnu kopiju izvornog koda ili
artefakt `python-distributions` iz uspješnog
[CI pokretanja](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Artefakt sadrži wheel paket i izvornu arhivu. Instalirani paket pruža i komandu
`cacti-mcp` i `python -m cacti_mcp`; ne sadrži PHP dodatak.

## Razvoj i testovi

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Testovi pokrivaju HTTP provjeru, izolaciju kredencijala, zahtjeve samo s bearer
tokenom, straničenje, uklanjanje osjetljivih podataka iz grešaka te stvarnu
razmjenu poruka između SDK klijenta i servera u podprocesu protiv testnog HTTP
servera. Ne zahtijevaju živu Cacti instalaciju.

Repozitorij koristi `src/cacti_mcp/`, pytest, Ruff, uv i Hatchling. CI testira
Python 3.12, 3.13 i 3.14. Zaseban zadatak pakiranja gradi wheel i izvornu arhivu,
instalira wheel izvan lokalne kopije i provjerava obje ulazne tačke. Distribucije
i rezultati testova spremaju se kao artefakti radnog toka.

## Doprinos

Zahtjeve za povlačenje (pull requests) šaljite na granu `develop`. Održavajte
adapter kompatibilnim s Pythonom 3.12, pratite postojeće Ruff postavke i strukturu
paketa `src/cacti_mcp/` te ostavite stdout rezervisan za MCP poruke. Dodajte
testove za izmijenjeno ponašanje transporta ili alata, pokrenite gornje provjere
i potpišite commitove sa `git commit -s`. Uskladite API izmjene s Cacti MCP
dodatkom i ažurirajte [docs/api.md](../../../docs/api.md).

## Licenca

Copyright (C) 2026 Thomas Vincent. Objavljeno pod licencom GNU General Public
License, verzija 2 ili novija. Pogledajte [LICENSE](../../../LICENSE).
