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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · **isiXhosa** · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

I-Cacti MCP sisiguquli (adapter) se-Python esiveza amandla [eplagin ye-Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) njengezixhobo ze-MCP ngokusebenzisa i-stdio. Iplagin sele isebenzisa i-MCP ngqo phezu kwe-HTTP, ngoko ke sebenzisa oko xa iklayenti yakho inokunxibelelana neseva ekude. Esi siguquli senzelwe iiklayenti ezithetha nge-stdio kuphela. Sisebenzisa i-Python MCP SDK esemthethweni kwaye siguqulela iminxeba yezixhobo kwi-HTTPS API yeplagin (isivumelwano samandla v2, esinikezelwa phantsi kweendlela `/v1/`, sisebenzisa ithokheni ye-bearer kuphela).
I-Cacti ilawula uqinisekiso lwesazisi, ugunyaziso, uqinisekiso lwedatha, kunye nokwenziwa komsebenzi.

**Imeko: isaphuhliswa, phambi kwe-1.0.** Inguqulelo 0.1.0 ixhasa uluhlu lwezixhobo lokufunda kuphela kunye neenguqulelo zofakelo ngokusebenzisa [iplagin ehambisana nayo ye-Cacti MCP](https://github.com/somethingwithproof/plugin_mcp).
Akukabikho khupho lunethegi okwangoku. Ukuxilongwa (doctor diagnostics) kunye nolungiso ngumsebenzi wexesha elizayo.

## Oko ikuvezayo

| Umsebenzi | Isixhobo se-MCP esibonelelwa yiplagin ye-Cacti MCP |
|---|---|
| Dwelisa izixhobo anokuzibona umnini wethokheni | `cacti-list-devices` |
| Funda isixhobo esinye esivumelekileyo | `cacti-get-device` |
| Funda iinguqulelo ze-Cacti, iplagin, kunye ne-API | `cacti-get-system-info` |

Amagama, iinkcazo, kunye neeskima zokungenisa zivela kwimpendulo yokufumanisa ye-Cacti ehluzwe ngeemvume. Abanye ababoneleli bokufunda kuphela abavumelekileyo banokufunyanwa ngaphandle kokongeza abaphathi bezixhobo be-Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Iimeko zokusetyenziswa

Qhagamshela iklayenti ye-MCP ukuze udwelise izixhobo ze-Cacti umsebenzisi wayo owodwa avumeleke ukuzibona, ukhangele isixhobo esinye esivumelekileyo, okanye ufumane iinguqulelo zofakelo xa umsebenzisi enendawo yolawulo efunekayo. Amagama neeskima zokungenisa zivela kwimpendulo yokufumanisa yeplagin, ngoko ke isiguquli asiphindaphindi umboneleli ngamnye. Bona [imithetho yobhaliso lwamandla](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) yeplagin ukuze ufumane imodeli yobhaliso nemida yangoku.

## Imephu yekhowudi novavanyo

| Indlela yokusebenza | Ukuphunyezwa | Ubungqina bovavanyo kule repozithri |
|---|---|---|
| Uqinisekiso lwe-HTTPS, imida, uqinisekiso lwe-bearer kuphela, kunye nohlulo lwamaphepha lwe-v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Ukufumanisa kwe-MCP, iminxeba, kunye neenguqu zeemvume | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Uncedo lwelayini yomyalelo, inguqulelo, kunye noseto olulahlekileyo | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Uvavanyo lwenkqubo engaphantsi (subprocess) lusebenzisa iklayenti neseva yokwenyani ye-SDK kunye nesiphelo se-HTTP sovavanyo. Alufuni kwaye alutshintshi uvavanyo lodibaniso olusebenzayo lwe-Cacti.

## Indlela ehlala ikhuselekile ngayo

- Isebenzisa i-[`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) esemthethweni ukuqalisa, ukufumanisa izixhobo, iminxeba, kunye nokwakha iifreyimu ze-stdio.
- Iveza kuphela amandla amanqaku awo acacileyo athi afundwa kuphela, awonakalisi, kwaye awatshintshi ziphumo xa ephindwa (idempotent). Iiskima namagama avela kwi-Cacti; isiguquli asina-SQL, ziqinisekiso zezixhobo, okanye miyalelo yolungiso.
- Ithumela ithokheni ye-bearer kuphela: akukho zikhukhi, akukho nyathelo le-CSRF. Iplagin iphinda ihlole ukuba semthethweni kwethokheni neemvume kwisicelo ngasinye.
- Isebenzisa i-HTTPS eqinisekisiweyo, ayize igcine iikhukhi, ayivumi ukuthunyelwa kwenye idilesi (redirects), kwaye ayihoyi iziguquki zendawo ye-proxy. I-HTTP ifuna `--allow-loopback-http` kunye nedilesi ye-loopback ethe ngqo okanye `localhost`.
- Ibeka umda kwiminxeba ye-API kwimizuzwana engama-35 iyonke, imizuzwana emi-5 yokuqhagamshela, imizuzwana engama-30 yokungasebenzi kwenethiwekhi, kunye ne-1 MB malunga ngempendulo nganye (iibhayithi ezili-1,100,000). Imizimba yezicelo ilinganiselwe kwiibhayithi ezili-16,384. Iminxeba ilandelelaniswa ngokweseshoni yeklayenti nganye.
- Ihlola iimpikiswano zesixhobo ngokuchasene neskima yokungenisa evela kufumaniso lokugqibela phambi kokuzithumela, kwaye isebenzisa kuphela ii-ID ezivela kuloo khathalogu iqinisekisiweyo. Ukungahambelani, okanye iskima engalunganga evela kwiseva, kubuya njengempazamo yesixhobo, hayi ukuwa kwenkqubo.
- Ayizami kwakhona ukwenza umsebenzi ngokuzenzekelayo. Iimpazamo zesixhobo zithwala kuphela isimo se-HTTP, i-AIP-193 `status`, kunye ne-ErrorInfo `reason`; azize zithwale umbhalo womyalezo weseva, imizimba yeempendulo, okanye iziqinisekiso. I-stdout igcinelwe imiyalezo ye-MCP kuphela.

Inguqulelo ye-SDK ibotshelelwe yi-`uv.lock` (`mcp>=2.3,<3` kwi-`pyproject.toml`). Esi siguquli sisebenzisa iseva yaso yenqanaba eliphantsi ye-2.x kunye nothutho lwe-stdio; asiphumezi siphelo se-MCP HTTP ekude, OAuth, izibonelelo, imiyalelo, imirhumo, okanye imisebenzi yasemva.

Bona [isivumelwano se-API](../../../docs/api.md) kunye [nesicwangciso sokuphunyezwa](../../../docs/plan.md).

## Ufakelo kunye nelayini yomyalelo

Ifuna i-Python 3.12 okanye entsha kunye ne-[uv](https://docs.astral.sh/uv/).
Ukusuka kwikopi elayishiweyo (checkout) yale repozithri:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Faka kwaye uvule iplagin ye-PHP, unike indawo yayo yolawulo kumsebenzisi we-Cacti owodwa, kwaye udale ithokheni yokufikelela yobuqu yaloo msebenzisi (ifomathi `cmcp_pat_` elandelwa ziidijithi ezingama-64 ze-hex ezingoonobumba abancinci) kwikhonsoli yeplagin, kwiphepha layo elithi My MCP Tokens, okanye ngomyalelo wayo `tokens.php`.
Iindawo zolawulo ze-Cacti ezikhoyo kunye neemvume zezixhobo zomsebenzisi zisasebenza.

Nika ithokheni ngomphathi wakho weemfihlo njenge-`CACTI_MCP_TOKEN`; ungaze uyongeze kulawulo lwekhowudi okanye kwiimpikiswano zomyalelo. Seta isiphelo ngokwahlukeneyo. Kufuneka ibe yi-URL ye-HTTPS ephela ngo-`/plugins/mcp/api.php`, ngaphandle kweziqinisekiso, umbuzo (query), okanye isiqwenga (fragment):

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` iseta isiphelo endaweni ye-`CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` ivumela i-HTTP eqhelekileyo kwi-`localhost`, `127.0.0.1`, okanye `::1` kuvavanyo lwasekhaya, `--lang LOCALE` itshintsha ulwimi lwemiyalezo ye-CLI, kwaye `--version` iprinta inguqulelo. Ngaphandle kwazo zombini isiphelo kunye ne-`CACTI_MCP_TOKEN`, umyalelo uphuma unempazamo yokusetyenziswa.

### Uguqulelo lweelwimi

Uncedo lwe-CLI kunye nemiyalezo yempazamo yesiguquli iza ngeelwimi ezingama-45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ngaphandle kwemfuneko yokongeza ezinye iipakethi. Ukukhethwa kolwimi kuhlola `--lang`, kulandele `LC_ALL`, `LC_MESSAGES`, kunye ne-`LANG`, kubuyele kwi-`en` (`C`/`POSIX` kunye neethegi ezingaziwayo nazo zibuyela kwi-`en`). Amagama ezixhobo ze-MCP, iiskima, kunye needatha ze-JSON ezivela kwizixhobo eziphumeleleyo azichaphazeleki; imiyalezo yempazamo yesiguquli ebuyiswa ine-`is_error=True` ilandela ulwimi olusebenzayo.

Inkqubo ilinda imiyalezo ye-MCP kwi-stdin. Iklayenti ye-MCP idla ngokuyiqalisa.
Kwiiklayenti ezamkela ifomathi eqhelekileyo yoseto lwe-`mcpServers`:

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

Cwangcisa iklayenti ukuze idlulisele `CACTI_MCP_ENDPOINT` kunye ne-`CACTI_MCP_TOKEN` kwinkqubo engaphantsi ngokusebenzisa indawo yayo okanye inkonzo yeemfihlo. Ukufunyanwa kweziguquki zendawo kuxhomekeke kwiklayenti. Akukho flegi yelayini yomyalelo yethokheni.

Upapasho lwe-Python olufakelwa ngokwahlukeneyo lubonelela ngomyalelo wekhonsoli `cacti-mcp`. Akufuneki upapasho kwi-PyPI ukuze uqhube ikopi elayishiweyo. Iplagin ye-PHP ayixhomekekanga kwi-Python.

## Iinguqulelo ezikhutshiweyo

Inguqulelo yopapasho irekhodwe kwi-[pyproject.toml](../../../pyproject.toml).
Kude kubekho iinguqulelo ezinethegi ezikhoyo, sebenzisa ikopi elayishiweyo yekhowudi okanye i-artifact ethi `python-distributions` evela [kuqhutywa kwe-CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) okuphumeleleyo.
I-artifact iqulethe i-wheel kunye nogcino lwekhowudi. Ipakethi efakelweyo ibonelela ngomyalelo `cacti-mcp` kunye ne-`python -m cacti_mcp`; ayiqulethe iplagin ye-PHP.

## Uphuhliso kunye novavanyo

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Uvavanyo lubandakanya uqinisekiso lwe-HTTP, ukwahlulwa kweziqinisekiso, izicelo ze-bearer kuphela, uhlulo lwamaphepha, ukufihlwa kweenkcukacha zeempazamo, kunye notshintshiselwano lokwenyani lweklayenti/iseva ye-SDK kwinkqubo engaphantsi ngokuchasene neseva ye-HTTP yovavanyo. Alufuni ufakelo olusebenzayo lwe-Cacti.

Irepozithri isebenzisa `src/cacti_mcp/`, i-pytest, i-Ruff, i-uv, kunye ne-Hatchling. I-CI ivavanya i-Python 3.12, 3.13, kunye ne-3.14. Umsebenzi owahlukileyo wokupakisha wakha i-wheel nogcino lwekhowudi, ufaka i-wheel ngaphandle kwekopi elayishiweyo, kwaye wenza uvavanyo olukhawulezayo kuzo zombini iindawo zokungena. Iipakethi ezisasazwayo neziphumo zovavanyo zii-artifact zomsebenzi.

## Ukuba negalelo

Izicelo zokudibanisa (Pull requests) ziya kwi-`develop`. Gcina isiguquli sihambelana ne-Python 3.12, landela useto lwe-Ruff olukhoyo kunye nolwakhiwo lwepakethi lwe-`src/cacti_mcp/`, kwaye ugcine i-stdout ilungiselelwe imiyalezo ye-MCP kuphela. Yongeza uvavanyo kwindlela yokusebenza yothutho okanye isixhobo esitshintshiweyo, qhuba iitshekhi ezingentla, kwaye usayine ii-commit nge-`git commit -s`.
Ngqamanisa iinguqu ze-API kunye neplagin ye-Cacti MCP kwaye uhlaziye i-[docs/api.md](../../../docs/api.md).

## Ilayisensi

Ilungelo lokushicilela (C) 2026 Thomas Vincent. Ikhutshwe phantsi kwe-GNU General Public License, inguqulelo 2 okanye entsha. Bona [LICENSE](../../../LICENSE).
