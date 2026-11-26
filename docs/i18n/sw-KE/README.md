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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · **Kiswahili** · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP ni adapta ya Python inayotoa uwezo wa
[Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp) kama zana za MCP
kupitia stdio. Programu-jalizi tayari inahudumia MCP kupitia HTTP moja kwa moja, kwa hivyo
itumie wakati mteja wako anaweza kuunganisha na seva ya mbali. Adapta hii ni kwa ajili ya
wateja wanaotumia stdio pekee. Inatumia SDK rasmi ya Python MCP na
hutafsiri maombi ya zana kwenda kwenye API ya HTTPS ya programu-jalizi (mkataba wa uwezo v2, unaohudumiwa
chini ya njia za `/v1/`, bearer token pekee).
Cacti inamiliki uthibitishaji, uidhinishaji, uhakiki, na utekelezaji.

**Hali: inaendelea kutengenezwa, kabla ya 1.0.** Toleo la 0.1.0 linasaidia orodha ya vifaa
ya kusoma pekee na matoleo ya usakinishaji kupitia programu-jalizi shirikishi ya
[Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp).
Bado hakuna toleo lililowekewa lebo. Uchunguzi wa Doctor na marekebisho ni kazi ya baadaye.

## Kinachotoa

| Operesheni | Zana ya MCP inayotolewa na programu-jalizi ya Cacti MCP |
|---|---|
| Orodhesha vifaa ambavyo mmiliki wa tokeni anaweza kuviona | `cacti-list-devices` |
| Soma kifaa kimoja kilichoidhinishwa | `cacti-get-device` |
| Soma matoleo ya Cacti, programu-jalizi, na API | `cacti-get-system-info` |

Majina, maelezo, na skima za ingizo zinatoka kwenye majibu ya ugunduzi ya Cacti yaliyochujwa
kwa ruhusa. Watoa huduma wa ziada wa kusoma pekee walioidhinishwa wanaweza kugunduliwa
bila kuongeza vidhibiti vya zana vya Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Matukio ya matumizi

Unganisha mteja wa MCP ili kuorodhesha vifaa vya Cacti ambavyo mtumiaji wake mahususi anaweza kuviona,
kutafuta kifaa kimoja kilichoidhinishwa, au kupata matoleo ya usakinishaji wakati mtumiaji
ana eneo la usimamizi linalohitajika. Majina na skima za ingizo zinatoka kwenye
majibu ya ugunduzi ya programu-jalizi, hivyo adapta hairudii kila mtoa huduma.
Tazama
[sheria za usajili wa uwezo](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
za programu-jalizi kwa muundo wa usajili na mipaka ya sasa.

## Ramani ya msimbo na majaribio

| Tabia | Utekelezaji | Ushahidi wa majaribio katika hazina hii |
|---|---|---|
| Uthibitishaji wa HTTPS, mipaka, uthibitishaji wa bearer pekee, na ugawaji kurasa wa v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Ugunduzi wa MCP, miito, na mabadiliko ya ruhusa | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Usaidizi wa mstari wa amri, toleo, na usanidi uliokosekana | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Jaribio la mchakato mdogo linatumia mteja na seva halisi ya SDK pamoja na kituo cha majaribio cha HTTP.
Halihitaji wala halichukui nafasi ya ukaguzi wa ujumuishaji wa Cacti halisi.

## Jinsi inavyobaki salama

- Inatumia [SDK rasmi ya `mcp` ya Python](https://github.com/modelcontextprotocol/python-sdk)
  kwa uanzishaji, ugunduzi wa zana, miito, na uundaji wa fremu za stdio.
- Inatoa uwezo ambao maelezo yake ni ya kusoma pekee, yasiyoharibu, na yanayojirudia bila kubadilisha matokeo. Skima na majina yanatoka
  Cacti; adapta haina SQL, vitambulisho vya vifaa, au amri za urekebishaji.
- Inatuma bearer token pekee: hakuna vidakuzi, hakuna hatua ya CSRF. Programu-jalizi inakagua upya
  uhalali wa tokeni na ruhusa kwenye kila ombi.
- Inatumia HTTPS iliyothibitishwa, haihifadhi kamwe vidakuzi, inakataa uelekezaji upya, na
  inapuuza vigeu vya mazingira vya proksi. HTTP inahitaji `--allow-loopback-http`
  na anwani halisi ya loopback au `localhost`.
- Inawekea kikomo miito ya API hadi sekunde 35 kwa ujumla, sekunde 5 kuunganisha, sekunde 30 za
  kutokuwa na shughuli za mtandao, na takriban MB 1 kwa kila jibu (baiti 1,100,000).
  Miili ya maombi ina kikomo cha baiti 16,384. Miito inafuatana kwa kila kipindi cha mteja.
- Inakagua hoja za zana dhidi ya skima ya ingizo kutoka kwa ugunduzi wa mwisho kabla ya
  kuzituma, na inatekeleza vitambulisho kutoka kwa katalogi hiyo iliyothibitishwa pekee. Kutolingana, au
  skima iliyoharibika kutoka kwa seva, hurudi kama kosa la zana, si ajali ya programu.
- Hairudii utekelezaji kiotomatiki. Makosa ya zana hubeba tu hali ya HTTP,
  `status` ya AIP-193, na `reason` ya ErrorInfo; kamwe si maandishi ya ujumbe
  wa seva, miili ya majibu, au vitambulisho. Stdout imetengwa kwa ajili ya ujumbe wa MCP.

Toleo la SDK limebanwa na `uv.lock` (`mcp>=2.3,<3` katika `pyproject.toml`). Adapta hii
inatumia seva yake ya kiwango cha chini ya 2.x pamoja na usafirishaji wa stdio; haitekelezi
kituo cha mbali cha MCP HTTP, OAuth, rasilimali,
vidokezo, usajili wa ufuatiliaji, au kazi za chinichini.

Tazama [mkataba wa API](../../../docs/api.md) na [mpango wa utekelezaji](../../../docs/plan.md).

## Usakinishaji na mstari wa amri

Inahitaji Python 3.12 au mpya zaidi na [uv](https://docs.astral.sh/uv/).
Kutoka kwenye nakala ya hazina hii:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Sakinisha na uwashe programu-jalizi ya PHP, mpe mtumiaji mahususi wa Cacti eneo lake,
na utengeneze tokeni ya ufikiaji binafsi kwa mtumiaji huyo (muundo wa `cmcp_pat_` ukifuatiwa
na tarakimu 64 ndogo za hex) kwenye koni ya programu-jalizi, kwenye ukurasa wake wa My MCP Tokens,
au kwa amri yake ya `tokens.php`.
Maeneo yaliyopo ya Cacti na ruhusa za vifaa za mtumiaji huyo bado zinatumika.

Toa tokeni kupitia kidhibiti chako cha siri kama `CACTI_MCP_TOKEN`; kamwe usiiongeze
kwenye udhibiti wa msimbo chanzo au hoja za amri. Weka kituo cha mwisho kando. Lazima kiwe
URL ya HTTPS inayoishia na `/plugins/mcp/api.php`, bila vitambulisho, hoja ya query, au
kipande cha fragment:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` huweka kituo cha mwisho badala ya `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` huruhusu HTTP ya kawaida kwenda `localhost`, `127.0.0.1`, au `::1`
kwa majaribio ya ndani, `--lang LOCALE` hubadilisha lugha ya ujumbe wa CLI, na
`--version` huchapisha toleo. Bila kituo cha mwisho na `CACTI_MCP_TOKEN`,
amri huisha kwa kosa la matumizi.

### Ujanibishaji

Usaidizi wa CLI na ujumbe wa makosa wa adapta hutolewa katika lugha 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) bila vitegemezi vya ziada. Utatuzi wa lugha
hukagua `--lang`, kisha `LC_ALL`, `LC_MESSAGES`, na `LANG`, na kurudi
kwenye `en` (`C`/`POSIX` na lebo zisizojulikana pia hutatuliwa kuwa `en`). Majina ya zana za MCP,
skima, na majibu ya JSON ya zana yaliyofanikiwa hayaathiriwi; ujumbe wa makosa wa adapta
unaorudishwa na `is_error=True` hufuata lugha inayotumika.

Mchakato husubiri ujumbe wa MCP kwenye stdin. Mteja wa MCP kwa kawaida huuanzisha.
Kwa wateja wanaokubali muundo wa kawaida wa usanidi wa `mcpServers`:

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

Sanidi mteja ili apitishe `CACTI_MCP_ENDPOINT` na `CACTI_MCP_TOKEN` kwa
mchakato mdogo kupitia mazingira yake au kituo chake cha siri. Urithi wa mazingira
unategemea mteja. Hakuna bendera ya mstari wa amri kwa ajili ya tokeni.

Usambazaji wa Python unaosakinishwa kando hutoa amri ya koni ya `cacti-mcp`.
Hakuna uchapishaji wa PyPI unaohitajika ili kuendesha nakala ya hazina. Programu-jalizi ya PHP
haina kitegemezi cha Python.

## Matoleo

Toleo la usambazaji limerekodiwa katika [pyproject.toml](../../../pyproject.toml).
Hadi matoleo yaliyowekewa lebo yapatikane, tumia nakala ya msimbo chanzo au
kifurushi cha `python-distributions` kutoka kwa
[mwendesho wa CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) uliofanikiwa.
Kifurushi hicho kina faili ya wheel na kumbukumbu ya chanzo. Kifurushi kilichosakinishwa hutoa
amri ya `cacti-mcp` na `python -m cacti_mcp`; hakina
programu-jalizi ya PHP.

## Uendelezaji na majaribio

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Majaribio yanahusu uthibitishaji wa HTTP, utengaji wa vitambulisho, maombi ya bearer pekee,
ugawaji kurasa, ufichaji wa makosa, na ubadilishanaji halisi wa mteja/seva ya SDK ya mchakato mdogo dhidi ya
seva ya majaribio ya HTTP. Hayahitaji usakinishaji halisi wa Cacti.

Hazina hii inatumia `src/cacti_mcp/`, pytest, Ruff, uv, na Hatchling. CI hupima
Python 3.12, 3.13, na 3.14. Kazi tofauti ya ufungashaji hujenga wheel
na kumbukumbu ya chanzo, husakinisha wheel nje ya nakala ya hazina, na kufanya jaribio la awali la
sehemu zote mbili za kuingilia. Usambazaji na matokeo ya majaribio ni vizalia vya mtiririko wa kazi.

## Kuchangia

Maombi ya kuvuta huenda kwenye `develop`. Weka adapta ikiendana na Python 3.12,
fuata usanidi uliopo wa Ruff na mpangilio wa kifurushi wa `src/cacti_mcp/`, na
weka stdout ikiwa imetengwa kwa ajili ya ujumbe wa MCP. Ongeza majaribio kwa tabia ya usafirishaji au zana
iliyobadilishwa, endesha ukaguzi ulio hapo juu, na utie saini ahadi kwa `git commit -s`.
Ratibu mabadiliko ya API na programu-jalizi ya Cacti MCP na usasishe [docs/api.md](../../../docs/api.md).

## Leseni

Hakimiliki (C) 2026 Thomas Vincent. Imetolewa chini ya Leseni ya Umma ya GNU,
toleo la 2 au la baadaye. Tazama [LICENSE](../../../LICENSE).
