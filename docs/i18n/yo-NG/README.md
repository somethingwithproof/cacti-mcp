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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · **Yorùbá** · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP jẹ́ aláṣepọ̀ Python tó ń ṣí àwọn agbára [àfikún Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) sílẹ̀ gẹ́gẹ́ bí àwọn irinṣẹ́ MCP lórí stdio. Àfikún náà ti ń pèsè MCP lórí HTTP tààrà tẹ́lẹ̀, nítorí náà lo ìyẹn nígbà tí oníbàárà rẹ bá lè sopọ̀ mọ́ sáfà jíjìnà. Aláṣepọ̀ yìí wà fún àwọn oníbàárà tó ń lo stdio nìkan. Ó ń lo SDK MCP ti Python tòótọ́, ó sì ń túmọ̀ àwọn ìpè irinṣẹ́ sí API HTTPS ti àfikún náà (àdéhùn agbára v2, tí a pèsè lábẹ́ àwọn ọ̀nà `/v1/`, pẹ̀lú tókínì bearer nìkan).
Cacti ni ó ní àṣẹ ìdánimọ̀, ìfúnni-láṣẹ, ìfìdímúlẹ̀, àti ìṣiṣẹ́.

**Ipò: ó ṣì wà lọ́wọ́ ìdàgbàsókè, ṣáájú 1.0.** Ẹ̀dà 0.1.0 ṣe àtìlẹ́yìn fún àkójọ àwọn ẹ̀rọ kíkà-nìkan àti àwọn ẹ̀dà ìfisórí nípasẹ̀ [àfikún Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) alábàáṣiṣẹ́pọ̀ rẹ̀. Kò tíì sí ìtúsílẹ̀ tí a fàmì sí síbẹ̀. Ìwádìí àyẹ̀wò Doctor àti àtúnṣe jẹ́ iṣẹ́ ọjọ́ iwájú.

## Ohun tí ó ń ṣí sílẹ̀

| Iṣẹ́ | Irinṣẹ́ MCP tí àfikún Cacti MCP pèsè |
|---|---|
| Ṣe àkójọ àwọn ẹ̀rọ tí olówó tókínì lè rí | `cacti-list-devices` |
| Ka ẹ̀rọ kan tí a gbà láàyè | `cacti-get-device` |
| Ka àwọn ẹ̀dà Cacti, àfikún, àti API | `cacti-get-system-info` |

Àwọn orúkọ, àpèjúwe, àti àwọn ètò ìtẹ̀wọlé wá láti inú ìdáhùn ìwárí tí a sẹ́ nípa ìyọ̀ǹda ti Cacti. A lè ṣàwárí àwọn olùpèsè kíkà-nìkan mìíràn tí a gbà láàyè láìfikún àwọn olùtọ́jú irinṣẹ́ Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Àwọn ọ̀nà ìlò

So oníbàárà MCP kan pọ̀ láti ṣe àkójọ àwọn ẹ̀rọ Cacti tí olùmúlò rẹ̀ pàtó lè rí, láti wá ẹ̀rọ kan tí a gbà láàyè, tàbí láti gba àwọn ẹ̀dà ìfisórí nígbà tí olùmúlò bá ní agbègbè ìṣàkóso tí a béèrè. Àwọn orúkọ àti ètò ìtẹ̀wọlé wá láti inú ìdáhùn ìwárí ti àfikún náà, nítorí náà aláṣepọ̀ kì í ṣe ẹ̀dà olùpèsè kọ̀ọ̀kan lẹ́ẹ̀mejì. Wo [àwọn òfin ìforúkọsílẹ̀ agbára](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) ti àfikún náà fún àwòkọ́ṣe ìforúkọsílẹ̀ àti àwọn ààlà lọ́wọ́lọ́wọ́.

## Máàpù kóòdù àti àyẹ̀wò

| Ìwà ìṣiṣẹ́ | Ìmúṣẹ | Ẹ̀rí àyẹ̀wò nínú ibi-ìpamọ́ yìí |
|---|---|---|
| Ìfìdímúlẹ̀ HTTPS, àwọn ààlà, ìdánimọ̀ bearer-nìkan, àti ìpín ojú-ìwé v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Ìwárí MCP, àwọn ìpè, àti àwọn àyípadà ìyọ̀ǹda | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Ìrànlọ́wọ́ ìlà-àṣẹ, ẹ̀dà, àti ìṣètò tí ó sọnù | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Àyẹ̀wò ìlànà-abẹ́lẹ̀ náà ń lo oníbàárà àti sáfà SDK gidi pẹ̀lú ojú-ìsopọ̀ HTTP àyẹ̀wò kan. Kò béèrè fún tàbí rọ́pò àyẹ̀wò ìṣọ̀kan Cacti gidi.

## Bí ó ṣe ń wà ní ààbò

- Ó ń lo [SDK Python ti `mcp`](https://github.com/modelcontextprotocol/python-sdk) tòótọ́ fún ìbẹ̀rẹ̀, ìwárí irinṣẹ́, àwọn ìpè, àti ìṣètò àpótí stdio.
- Ó ń ṣí àwọn agbára tí àwọn àkíyèsí wọn jẹ́ kíkà-nìkan, aláìparun, àti aláìyípadà lẹ́yìn àtúnṣe (idempotent) pàtó nìkan sílẹ̀. Àwọn ètò àti orúkọ wá láti Cacti; aláṣepọ̀ kò ní SQL, àwọn ẹ̀rí ìdánimọ̀ ẹ̀rọ, tàbí àwọn àṣẹ àtúnṣe kankan nínú.
- Ó ń fi tókínì bearer nìkan ránṣẹ́: kò sí àwọn kókì, kò sí ìgbésẹ̀ CSRF. Àfikún náà tún ń ṣàyẹ̀wò ìwúlò tókínì àti àwọn ìyọ̀ǹda lórí gbogbo ìbéèrè.
- Ó ń lo HTTPS tí a ti fìdí rẹ̀ múlẹ̀, kì í fi àwọn kókì pamọ́ láé, ó ń kọ ìdarí-síbòmíràn, ó sì ń pa àwọn onírúurú àyíká aṣojú (proxy) tì. HTTP nílò `--allow-loopback-http` àti àdírẹ́sì loopback gidi tàbí `localhost`.
- Ó ń fi ààlà lé àwọn ìpè API sí ìṣẹ́jú-àáyá 35 lápapọ̀, ìṣẹ́jú-àáyá 5 láti sopọ̀, ìṣẹ́jú-àáyá 30 ti àìṣiṣẹ́ nẹ́tíwọ́ọ̀kì, àti nǹkan bí 1 MB fún ìdáhùn kọ̀ọ̀kan (1,100,000 báìtì). Ara ìbéèrè ní ààlà sí 16,384 báìtì. A ń ṣètò àwọn ìpè lọ́kọ̀ọ̀kan fún ìgbà ìṣiṣẹ́ oníbàárà kọ̀ọ̀kan.
- Ó ń ṣàyẹ̀wò àwọn àríyànjiyàn irinṣẹ́ pẹ̀lú ètò ìtẹ̀wọlé láti inú ìwárí tí ó kẹ́yìn ṣáájú kí ó tó fi wọ́n ránṣẹ́, ó sì ń ṣiṣẹ́ lórí àwọn ID láti inú àkójọ tí a ti fìdí rẹ̀ múlẹ̀ nìkan. Àìbáramu, tàbí ètò tí kò dára láti ọ̀dọ̀ sáfà, yóò padà wá gẹ́gẹ́ bí àṣìṣe irinṣẹ́, kì í ṣe ìṣubú ètò.
- Kì í tún ìṣiṣẹ́ ṣe fúnra rẹ̀. Àwọn àṣìṣe irinṣẹ́ gbé ipò HTTP, `status` ti AIP-193, àti `reason` ti ErrorInfo nìkan; kì í gbé ọ̀rọ̀ ìfiránṣẹ́ sáfà, ara ìdáhùn, tàbí àwọn ẹ̀rí ìdánimọ̀ láé. A ya stdout sọ́tọ̀ fún àwọn ìfiránṣẹ́ MCP.

A so ẹ̀dà SDK mọ́lẹ̀ pẹ̀lú `uv.lock` (`mcp>=2.3,<3` nínú `pyproject.toml`). Aláṣepọ̀ yìí ń lo sáfà ìpele-ìsàlẹ̀ 2.x rẹ̀ pẹ̀lú ìgbésẹ̀ stdio; kò ṣe àgbékalẹ̀ ojú-ìsopọ̀ HTTP MCP jíjìnà, OAuth, àwọn ohun-èlò, àwọn ìtọ́ni, àwọn ìforúkọsílẹ̀, tàbí àwọn iṣẹ́ abẹ́lẹ̀.

Wo [àdéhùn API](../../../docs/api.md) àti [ètò ìmúṣẹ](../../../docs/plan.md).

## Ìfisórí àti ìlà-àṣẹ

Ó nílò Python 3.12 tàbí tuntun jù bẹ́ẹ̀ lọ àti [uv](https://docs.astral.sh/uv/).
Láti inú ẹ̀dà ibi-ìpamọ́ yìí:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Fi àfikún PHP náà sórí ẹ̀rọ kí o sì mú un ṣiṣẹ́, fún olùmúlò Cacti pàtó kan ní agbègbè rẹ̀, kí o sì ṣẹ̀dá tókínì ààyè ti ara ẹni fún olùmúlò náà (ọ̀nà `cmcp_pat_` tí àwọn nọ́ńbà hex kékeré 64 tẹ̀ lé) nínú kọ́nsóòlù àfikún náà, lórí ojú-ìwé My MCP Tokens rẹ̀, tàbí pẹ̀lú àṣẹ `tokens.php` rẹ̀.
Àwọn agbègbè Cacti àti àwọn ìyọ̀ǹda ẹ̀rọ tí olùmúlò náà ti ní tẹ́lẹ̀ ṣì wà ní ìlò.

Pèsè tókínì náà nípasẹ̀ olùṣàkóso àṣírí rẹ gẹ́gẹ́ bí `CACTI_MCP_TOKEN`; má ṣe fi í kún ìṣàkóso orísun kóòdù tàbí àwọn àríyànjiyàn àṣẹ láé. Ṣètò ojú-ìsopọ̀ náà lọ́tọ̀. Ó gbọ́dọ̀ jẹ́ URL HTTPS tó parí pẹ̀lú `/plugins/mcp/api.php`, láìsí ẹ̀rí ìdánimọ̀, ìbéèrè, tàbí àjákù:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` ń ṣètò ojú-ìsopọ̀ náà dípò `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` gba HTTP lásán láàyè sí `localhost`, `127.0.0.1`, tàbí `::1` fún àyẹ̀wò abẹ́lé, `--lang LOCALE` ń borí ìsọdèdè ìfiránṣẹ́ ìlà-àṣẹ, bẹ́ẹ̀ ni `--version` ń tẹ ẹ̀dà náà jáde. Láìsí ojú-ìsopọ̀ àti `CACTI_MCP_TOKEN` méjèèjì, àṣẹ náà yóò jáde pẹ̀lú àṣìṣe ìlò.

### Ìsọdèdè

Ìrànlọ́wọ́ ìlà-àṣẹ àti àwọn ìfiránṣẹ́ àṣìṣe aláṣepọ̀ wà ní èdè agbègbè 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) láìsí àfikún ìgbẹ́kẹ̀lé kankan. Ìyànjú èdè agbègbè ń ṣàyẹ̀wò `--lang`, lẹ́yìn náà `LC_ALL`, `LC_MESSAGES`, àti `LANG`, ó sì ń padà sí `en` (`C`/`POSIX` àti àwọn àmì àìmọ̀ náà tún ń yanjú sí `en`). Àwọn orúkọ irinṣẹ́ MCP, àwọn ètò, àti àwọn ẹrù-ìṣiṣẹ́ JSON tó ṣàṣeyọrí kò ní yípadà; àwọn ìfiránṣẹ́ àṣìṣe aláṣepọ̀ tí a dá padà pẹ̀lú `is_error=True` ń tẹ̀lé èdè agbègbè tó ń ṣiṣẹ́.

Ìlànà náà ń retí àwọn ìfiránṣẹ́ MCP lórí stdin. Oníbàárà MCP ló sábà máa ń ṣí i.
Fún àwọn oníbàárà tó ń gba ọ̀nà ìṣètò `mcpServers` tó wọ́pọ̀:

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

Ṣètò oníbàárà láti fi `CACTI_MCP_ENDPOINT` àti `CACTI_MCP_TOKEN` ránṣẹ́ sí ìlànà-abẹ́lẹ̀ nípasẹ̀ àyíká rẹ̀ tàbí ohun-èlò àṣírí rẹ̀. Ìjogún àyíká sinmi lórí oníbàárà náà. Kò sí àmì ìlà-àṣẹ fún tókínì.

Ìpínkiri Python tí a lè fi sórí ẹ̀rọ lọ́tọ̀ ń pèsè àṣẹ kọ́nsóòlù `cacti-mcp`. A kò nílò ìtẹ̀jáde PyPI láti ṣiṣẹ́ pẹ̀lú ẹ̀dà ibi-ìpamọ́ náà. Àfikún PHP kò ní ìgbẹ́kẹ̀lé Python kankan.

## Àwọn ìtúsílẹ̀

A kọ ẹ̀dà ìpínkiri sílẹ̀ nínú [pyproject.toml](../../../pyproject.toml).
Títí di ìgbà tí àwọn ìtúsílẹ̀ tí a fàmì sí yóò fi wà, lo ẹ̀dà orísun tàbí ohun-ìpamọ́ `python-distributions` láti inú [ìṣiṣẹ́ CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) tó ṣàṣeyọrí.
Ohun-ìpamọ́ náà ní wheel àti àkójọ orísun. Àpò tí a fi sórí ẹ̀rọ ń pèsè àṣẹ `cacti-mcp` àti `python -m cacti_mcp` méjèèjì; kò ní àfikún PHP nínú.

## Ìdàgbàsókè àti àwọn àyẹ̀wò

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Àwọn àyẹ̀wò bo ìfìdímúlẹ̀ HTTP, ìyàsọ́tọ̀ ẹ̀rí ìdánimọ̀, àwọn ìbéèrè bearer-nìkan, ìpín ojú-ìwé, ìbò-mọ́lẹ̀ àṣìṣe, àti ìpàṣípààrọ̀ ìlànà-abẹ́lẹ̀ oníbàárà/sáfà SDK gidi lòdì sí sáfà HTTP àyẹ̀wò kan. Wọn kò nílò ìfisórí Cacti gidi.

Ibi-ìpamọ́ náà ń lo `src/cacti_mcp/`, pytest, Ruff, uv, àti Hatchling. CI ń ṣàyẹ̀wò Python 3.12, 3.13, àti 3.14. Iṣẹ́ ìdìpọ̀ ọ̀tọ̀ kan ń kọ wheel àti àkójọ orísun, ó ń fi wheel náà sórí ẹ̀rọ lóde ẹ̀dà ibi-ìpamọ́ náà, ó sì ń ṣe àyẹ̀wò kíákíá lórí àwọn ojú-ìbẹ̀rẹ̀ méjèèjì. Àwọn ìpínkiri àti àwọn èsì àyẹ̀wò jẹ́ àwọn ohun-ìpamọ́ ìṣàn-iṣẹ́.

## Ìfikún

Àwọn ìbéèrè ìfàwọ́ (pull requests) lọ sí `develop`. Jẹ́ kí aláṣepọ̀ náà bá Python 3.12 mu, tẹ̀lé ìṣètò Ruff tó wà tẹ́lẹ̀ àti ìṣètò àpò `src/cacti_mcp/`, kí o sì ya stdout sọ́tọ̀ fún àwọn ìfiránṣẹ́ MCP. Fi àwọn àyẹ̀wò kún un fún ìwà ìgbésẹ̀ tàbí irinṣẹ́ tí a yípadà, ṣe àwọn àyẹ̀wò lókè yìí, kí o sì fọwọ́ sí àwọn ìfìsílẹ̀ pẹ̀lú `git commit -s`.
Ṣètò àwọn àyípadà API pẹ̀lú àfikún Cacti MCP kí o sì ṣe àtúnṣe [docs/api.md](../../../docs/api.md).

## Ìwé-àṣẹ

Ẹ̀tọ́ àdàkọ (C) 2026 Thomas Vincent. A tú u sílẹ̀ lábẹ́ GNU General Public License, ẹ̀dà 2 tàbí tuntun jù bẹ́ẹ̀ lọ. Wo [LICENSE](../../../LICENSE).
