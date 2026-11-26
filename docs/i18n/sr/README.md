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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [Bosanski](../bs/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Hrvatski](../hr/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · **Српски** · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP је Python адаптер који излаже могућности
[Cacti MCP додатка](https://github.com/somethingwithproof/plugin_mcp) као MCP
алате преко stdio. Додатак већ директно послужује MCP преко HTTP-а, па користите
ту опцију када ваш клијент може да се повеже на удаљени сервер. Овај адаптер је
намењен клијентима који подржавају искључиво stdio. Користи званични Python MCP
SDK и преводи позиве алата у HTTPS API додатка (уговор могућности v2, послужен на
`/v1/` путањама, само уз bearer токен).
Cacti управља аутентификацијом, ауторизацијом, провером и извршавањем.

**Статус: у развоју, пре верзије 1.0.** Верзија 0.1.0 подржава инвентар уређаја
само за читање и верзије инсталације преко пратећег
[Cacti MCP додатка](https://github.com/somethingwithproof/plugin_mcp).
Још увек нема означеног издања. Дијагностика (doctor) и поправке планиране су за будући рад.

## Шта излаже

| Операција | MCP алат који пружа Cacti MCP додатак |
|---|---|
| Приказ листе уређаја које власник токена сме да види | `cacti-list-devices` |
| Читање једног дозвољеног уређаја | `cacti-get-device` |
| Читање верзија Cacti-ја, додатка и API-ја | `cacti-get-system-info` |

Називи, описи и улазне шеме долазе из одговора откривања (discovery) који Cacti
филтрира према дозволама. Додатни дозвољени пружаоци само за читање могу се
открити без додавања Python руковалаца алата.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Примери употребе

Повежите MCP клијент да бисте излистали Cacti уређаје које његов наменски
корисник сме да види, пронашли један дозвољени уређај или преузели верзије
инсталације када корисник има потребну административну област (realm). Називи и
улазне шеме долазе из одговора откривања додатка, тако да адаптер не дуплира
сваког пружаоца. Погледајте
[правила регистрације могућности](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
додатка за модел регистрације и тренутна ограничења.

## Мапа кода и тестова

| Понашање | Имплементација | Тестна покривеност у овом репозиторијуму |
|---|---|---|
| HTTPS провера, ограничења, аутентификација само bearer токеном и v2 страницирање | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP откривање, позиви и промене дозвола | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Помоћ командне линије, верзија и недостајућа подешавања | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Тест подпроцеса користи стварни SDK клијент и сервер са тестном HTTP крајњом
тачком. Он не захтева нити замењује интеграциону проверу са живом Cacti
инсталацијом.

## Како остаје безбедан

- Користи званични [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  за иницијализацију, откривање алата, позиве и stdio уоквиривање.
- Излаже само могућности чије су анотације строго само за читање, недеструктивне
  и идемпотентне. Шеме и називи долазе из Cacti-ја; адаптер не садржи SQL,
  акредитиве уређаја нити команде за поправку.
- Шаље само bearer токен: без колачића (cookies) и без CSRF корака. Додатак при
  сваком захтеву поново проверава ваљаност токена и дозволе.
- Користи проверени HTTPS, никада не чува колачиће, одбија преусмеравања и
  занемарује променљиве окружења за прокси. HTTP захтева `--allow-loopback-http`
  и дословну loopback адресу или `localhost`.
- Ограничава API позиве на укупно 35 секунди, 5 секунди за повезивање, 30 секунди
  мрежне неактивности и приближно 1 MB по одговору (1.100.000 бајтова). Тела
  захтева ограничена су на 16.384 бајта. Позиви се серијализују по клијентској
  сесији.
- Проверава аргументе алата у односу на улазну шему из последњег откривања пре
  слања и извршава само идентификаторе из тог провереног каталога. Неподударање
  или неисправна шема са сервера враћа се као грешка алата, а не као пад програма.
- Не понавља извршавање аутоматски. Грешке алата носе само HTTP статус, AIP-193
  `status` и ErrorInfo `reason`; никада текст поруке сервера, тела одговора или
  акредитиве. Stdout је резервисан за MCP поруке.

Верзија SDK-а је закључана у датотеци `uv.lock` (`mcp>=2.3,<3` у
`pyproject.toml`). Овај адаптер користи његов нисконивовски 2.x сервер са stdio
транспортом; не имплементира удаљену MCP HTTP крајњу тачку, OAuth, ресурсе,
промптове, претплате нити позадинске задатке.

Погледајте [API уговор](../../../docs/api.md) и [план имплементације](../../../docs/plan.md).

## Инсталација и командна линија

Захтева Python 3.12 или новији и [uv](https://docs.astral.sh/uv/).
Из локалне копије овог репозиторијума:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Инсталирајте и омогућите PHP додатак, доделите његову област (realm) наменском
Cacti кориснику и креирајте лични приступни токен за тог корисника (облик
`cmcp_pat_` праћен са 64 мале хексадецималне цифре) у конзоли додатка, на
страници My MCP Tokens или помоћу команде `tokens.php`.
Постојеће Cacti области и дозволе за уређаје тог корисника остају на снази.

Проследите токен преко свог менаџера тајни као `CACTI_MCP_TOKEN`; никада га не
додајте у систем контроле верзија нити у аргументе командне линије. Крајњу тачку
поставите засебно. Мора бити HTTPS URL који се завршава на `/plugins/mcp/api.php`,
без акредитива, упитног низа или фрагмента:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` поставља крајњу тачку уместо променљиве `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` дозвољава обичан HTTP према `localhost`, `127.0.0.1` или
`::1` за локално тестирање, `--lang LOCALE` замењује локализацију CLI порука, а
`--version` исписује верзију. Без обе вредности, крајње тачке и
`CACTI_MCP_TOKEN`, команда завршава са грешком употребе.

### Локализација

Помоћ командне линије и поруке о грешкама адаптера испоручују се на 48 локалитета
(`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`, `bs`, `hr`, `sr`)
без додатних зависности. Одређивање локалитета проверава `--lang`, затим `LC_ALL`,
`LC_MESSAGES` и `LANG`, уз повратак на `en` (`C`/`POSIX` и непознате ознаке
такође се своде на `en`). Називи MCP алата, шеме и успешни JSON одговори алата
остају непромењени; поруке о грешкама адаптера враћене са `is_error=True` прате
активни локалитет.

Процес чека MCP поруке на stdin. Обично га покреће MCP клијент. За клијенте који
прихватају уобичајени формат подешавања `mcpServers`:

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

Конфигуришите клијент да прослеђује `CACTI_MCP_ENDPOINT` и `CACTI_MCP_TOKEN`
подпроцесу преко окружења или система за тајне. Наслеђивање окружења зависи од
клијента. Не постоји заставица командне линије за токен.

Засебно инсталабилна Python дистрибуција пружа конзолну команду `cacti-mcp`.
Објављивање на PyPI-ју није потребно за покретање из локалне копије. PHP додатак
нема зависност од Python-а.

## Издања

Верзија дистрибуције забележена је у датотеци [pyproject.toml](../../../pyproject.toml).
Док означена издања не постану доступна, користите локалну копију изворног кода
или артефакт `python-distributions` из успешног
[CI покретања](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Артефакт садржи wheel пакет и изворну архиву. Инсталирани пакет пружа и команду
`cacti-mcp` и `python -m cacti_mcp`; не садржи PHP додатак.

## Развој и тестови

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Тестови покривају HTTP проверу, изолацију акредитива, захтеве само са bearer
токеном, страницирање, уклањање осетљивих података из грешака и стварну размену
порука између SDK клијента и сервера у подпроцесу против тестног HTTP сервера.
Не захтевају живу Cacti инсталацију.

Репозиторијум користи `src/cacti_mcp/`, pytest, Ruff, uv и Hatchling. CI тестира
Python 3.12, 3.13 и 3.14. Засебан задатак паковања гради wheel и изворну архиву,
инсталира wheel изван локалне копије и проверава обе улазне тачке. Дистрибуције и
резултати тестова чувају се као артефакти радног тока.

## Допринос

Pull захтеве шаљите на грану `develop`. Одржавајте адаптер компатибилним са
Python-ом 3.12, пратите постојећа Ruff подешавања и структуру пакета
`src/cacti_mcp/`, и оставите stdout резервисан за MCP поруке. Додајте тестове за
измењено понашање транспорта или алата, покрените горње провере и потпишите
комитове са `git commit -s`. Ускладите API измене са Cacti MCP додатком и
ажурирајте [docs/api.md](../../../docs/api.md).

## Лиценца

Ауторска права (C) 2026 Thomas Vincent. Објављено под лиценцом GNU General Public
License, верзија 2 или новија. Погледајте [LICENSE](../../../LICENSE).
