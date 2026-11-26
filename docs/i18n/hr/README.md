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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [Bosanski](../bs/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · **Hrvatski** · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Српски](../sr/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP je Python prilagodnik koji izlaže mogućnosti
[dodatka Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) kao MCP
alate preko stdio sučelja. Dodatak već izravno poslužuje MCP putem HTTP-a, stoga
koristite tu mogućnost kada se vaš klijent može spojiti na udaljeni poslužitelj.
Ovaj prilagodnik namijenjen je klijentima koji podržavaju isključivo stdio.
Koristi službeni Python MCP SDK i prevodi pozive alata u HTTPS API dodatka
(ugovor mogućnosti v2, poslužen na putanjama `/v1/`, samo s nositeljskim tokenom).
Cacti upravlja provjerom autentičnosti, ovlastima, provjerom valjanosti i izvođenjem.

**Status: u razvoju, prije inačice 1.0.** Inačica 0.1.0 podržava popis uređaja
samo za čitanje i inačice instalacije putem pratećeg
[dodatka Cacti MCP](https://github.com/somethingwithproof/plugin_mcp).
Označenog izdanja još nema. Dijagnostika (doctor) i popravci predviđeni su za buduće inačice.

## Što izlaže

| Radnja | MCP alat koji isporučuje dodatak Cacti MCP |
|---|---|
| Ispis uređaja koje vlasnik tokena smije vidjeti | `cacti-list-devices` |
| Čitanje jednog dopuštenog uređaja | `cacti-get-device` |
| Čitanje inačica sustava Cacti, dodatka i API-ja | `cacti-get-system-info` |

Nazivi, opisi i ulazne sheme dolaze iz odgovora otkrivanja koji Cacti filtrira
prema korisničkim ovlastima. Dodatni dopušteni pružatelji samo za čitanje mogu se
otkriti bez dodavanja Python rukovatelja alata.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Slučajevi uporabe

Povežite MCP klijent radi ispisa Cacti uređaja koje njegov namjenski korisnik
smije vidjeti, uvida u jedan dopušteni uređaj ili dohvaćanja inačica instalacije
kada korisnik posjeduje potrebnu administrativnu ovlast (realm). Nazivi i ulazne
sheme potječu iz odgovora otkrivanja dodatka, pa prilagodnik ne udvostručuje
svakog pružatelja. Pogledajte
[pravila registracije mogućnosti](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
dodatka za model registracije i trenutačna ograničenja.

## Karta koda i testova

| Ponašanje | Implementacija | Pokrivenost testovima u ovom repozitoriju |
|---|---|---|
| Provjera valjanosti HTTPS-a, ograničenja, autentifikacija samo tokenom i v2 straničenje | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP otkrivanje, pozivi i promjene ovlasti | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Pomoć naredbenog retka, inačica i nedostajuće postavke | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Test podprocesa koristi stvarni SDK klijent i poslužitelj s ispitnom HTTP
krajnjom točkom. On ne zahtijeva niti zamjenjuje integracijsku provjeru sa
stvarnom instalacijom sustava Cacti.

## Kako ostaje siguran

- Koristi službeni [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  za pokretanje, otkrivanje alata, pozive i stdio uokvirivanje.
- Izlaže samo mogućnosti čije su napomene isključivo samo za čitanje,
  nedestruktivne i idempotentne. Sheme i nazivi dolaze iz sustava Cacti;
  prilagodnik ne sadrži SQL, vjerodajnice uređaja ni naredbe za popravak.
- Šalje samo nositeljski token (bearer token): bez kolačića i bez CSRF koraka.
  Dodatak ponovno provjerava valjanost tokena i ovlasti pri svakom zahtjevu.
- Koristi provjereni HTTPS, nikada ne pohranjuje kolačiće, odbija preusmjeravanja
  i zanemaruje varijable okruženja posrednika (proxy). HTTP zahtijeva
  `--allow-loopback-http` i doslovnu povratnu adresu ili `localhost`.
- Ograničava API pozive na ukupno 35 sekundi, 5 sekundi za spajanje, 30 sekundi
  mrežne neaktivnosti te približno 1 MB po odgovoru (1.100.000 bajtova). Tijela
  zahtjeva ograničena su na 16.384 bajta. Pozivi se izvršavaju slijedno unutar
  svake klijentske sesije.
- Provjerava argumente alata prema ulaznoj shemi iz posljednjeg otkrivanja prije
  slanja te izvodi samo identifikatore iz tog provjerenog kataloga. Nepodudaranje
  ili nevaljana shema s poslužitelja vraća se kao pogreška alata, a ne kao rušenje.
- Ne ponavlja izvođenje automatski. Pogreške alata sadrže samo HTTP status,
  AIP-193 `status` i ErrorInfo `reason`; nikada tekst poruke poslužitelja, tijela
  odgovora ili vjerodajnice. Stdout je rezerviran za MCP poruke.

Inačica SDK-a zaključana je u datoteci `uv.lock` (`mcp>=2.3,<3` u
`pyproject.toml`). Ovaj prilagodnik koristi niskorazinski 2.x poslužitelj sa
stdio prijenosom; ne implementira udaljenu MCP HTTP krajnju točku, OAuth,
resurse, upute (prompts), pretplate ni pozadinske zadatke.

Pogledajte [API ugovor](../../../docs/api.md) i [plan implementacije](../../../docs/plan.md).

## Instalacija i naredbeni redak

Zahtijeva Python 3.12 ili noviji i [uv](https://docs.astral.sh/uv/).
Iz lokalne kopije ovog repozitorija:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Instalirajte i uključite PHP dodatak, dodijelite njegovu ovlast (realm)
namjenskom korisniku sustava Cacti i izradite osobni pristupni token za tog
korisnika (oblik `cmcp_pat_` iza kojeg slijede 64 male heksadekadske znamenke) u
konzoli dodatka, na stranici My MCP Tokens ili naredbom `tokens.php`.
Postojeće ovlasti sustava Cacti i prava pristupa uređajima tog korisnika i dalje vrijede.

Token osigurajte putem upravitelja tajni kao `CACTI_MCP_TOKEN`; nikada ga nemojte
dodavati u sustav nadzora inačica ili argumente naredbenog retka. Krajnju točku
zadajte zasebno. Mora biti HTTPS URL koji završava s `/plugins/mcp/api.php`, bez
vjerodajnica, upitnog niza ili odlomka:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` zadaje krajnju točku umjesto varijable `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` dopušta nešifrirani HTTP prema `localhost`, `127.0.0.1`
ili `::1` za lokalno ispitivanje, `--lang LOCALE` nadjačava lokalizaciju poruka
naredbenog retka, a `--version` ispisuje inačicu. Bez zadane krajnje točke i
`CACTI_MCP_TOKEN`, naredba završava pogreškom uporabe.

### Lokalizacija

Pomoć naredbenog retka i poruke o pogreškama prilagodnika isporučuju se na 48
lokaliteta (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`, `bs`, `hr`, `sr`)
bez dodatnih ovisnosti. Razrješavanje lokaliteta provjerava `--lang`, zatim
`LC_ALL`, `LC_MESSAGES` i `LANG`, s pričuvnim povratkom na `en` (`C`/`POSIX` i
nepoznate oznake također se svode na `en`). Nazivi MCP alata, sheme i uspješni
JSON sadržaji alata ostaju nepromijenjeni; poruke o pogreškama prilagodnika
vraćene s `is_error=True` prate aktivni lokalitet.

Proces čeka MCP poruke na ulazu stdin. Uobičajeno ga pokreće MCP klijent. Za
klijente koji prihvaćaju standardni oblik postavki `mcpServers`:

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

Podesite klijent tako da podprocesu prosljeđuje `CACTI_MCP_ENDPOINT` i
`CACTI_MCP_TOKEN` putem okruženja ili pohrane tajni. Nasljeđivanje okruženja
ovisi o klijentu. Zastavica naredbenog retka za token ne postoji.

Zasebno instalabilna Python distribucija pruža konzolnu naredbu `cacti-mcp`.
Objava na PyPI-ju nije potrebna za pokretanje iz lokalne kopije. PHP dodatak nema
ovisnost o Pythonu.

## Izdanja

Inačica distribucije zapisana je u datoteci [pyproject.toml](../../../pyproject.toml).
Dok označena izdanja ne postanu dostupna, koristite izvornu kopiju ili artefakt
`python-distributions` iz uspješnog
[CI izvođenja](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Artefakt sadrži wheel paket i izvornu arhivu. Instalirani paket pruža naredbu
`cacti-mcp` i poziv `python -m cacti_mcp`; ne sadrži PHP dodatak.

## Razvoj i testiranje

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Testovi obuhvaćaju provjeru valjanosti HTTP-a, izolaciju vjerodajnica, zahtjeve
samo s nositeljskim tokenom, straničenje, uklanjanje osjetljivih podataka iz
pogrešaka te stvarnu razmjenu poruka između SDK klijenta i poslužitelja u
podprocesu prema ispitnom HTTP poslužitelju. Ne zahtijevaju živu instalaciju
sustava Cacti.

Repozitorij koristi `src/cacti_mcp/`, pytest, Ruff, uv i Hatchling. CI provjerava
Python 3.12, 3.13 i 3.14. Zaseban zadatak pakiranja izrađuje wheel i izvornu
arhivu, instalira wheel izvan radne kopije te provjerava obje ulazne točke.
Distribucije i rezultati ispitivanja pohranjuju se kao artefakti tijeka rada.

## Doprinosi

Zahtjeve za povlačenje (pull requests) usmjerite na granu `develop`. Očuvajte
kompatibilnost prilagodnika s Pythonom 3.12, slijedite postojeće postavke alata
Ruff i raspored paketa `src/cacti_mcp/` te zadržite stdout rezerviranim za MCP
poruke. Dodajte testove za promijenjeno ponašanje prijenosa ili alata, pokrenite
navedene provjere i potpišite predaje naredbom `git commit -s`. Promjene API-ja
uskladite s dodatkom Cacti MCP i ažurirajte [docs/api.md](../../../docs/api.md).

## Licencija

Autorsko pravo (C) 2026 Thomas Vincent. Objavljeno pod licencijom GNU General
Public License, inačica 2 ili novija. Pogledajte [LICENSE](../../../LICENSE).
