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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · **isiZulu**

</details>

I-Cacti MCP iyi-adapter ye-Python eveza amakhono e-[plugin ye-Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) njengamathuluzi e-MCP nge-stdio. Le plugin isivele ihlinzeka nge-MCP nge-HTTP ngokuqondile, ngakho sebenzisa lokho uma iklayenti lakho likwazi ukuxhuma kuseva ekude. Le adapter eyamaklayenti akhuluma i-stdio kuphela. Isebenzisa i-Python MCP SDK esemthethweni futhi iguqula ukubizwa kwamathuluzi kube yi-HTTPS API ye-plugin (isivumelwano samakhono i-v2, esihlinzekwa ngaphansi kwezindlela ze-`/v1/`, nge-bearer token kuphela).
I-Cacti iphethe ukuqinisekiswa kobunikazi, ukugunyazwa, ukuhlolwa kokulunga, nokusebenza.

**Isimo: isathuthukiswa, ngaphambi kwe-1.0.** Inguqulo 0.1.0 isekela uhlu lwamadivayisi lokufunda kuphela kanye nezinguqulo zokufakwa nge-[plugin ye-Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) ehambisana nayo. Ayikho inguqulo ekhishiwe enamaki okwamanje. Ukuxilonga kwe-Doctor nokulungisa kuzokwenziwa esikhathini esizayo.

## Okukuvezayo

| Umsebenzi | Ithuluzi le-MCP elihlinzekwa yi-plugin ye-Cacti MCP |
|---|---|
| Bhala uhlu lwamadivayisi umnikazi we-token avunyelwe ukuwabona | `cacti-list-devices` |
| Funda idivayisi eyodwa evunyelwe | `cacti-get-device` |
| Funda izinguqulo ze-Cacti, i-plugin, ne-API | `cacti-get-system-info` |

Amagama, izincazelo, nama-schema okufakwayo kuvela empendulweni yokuthola ehlungwe ngezimvume ye-Cacti. Abanye abahlinzeki bokufunda kuphela abavunyelwe bangatholwa ngaphandle kokwengeza abaphathi bamathuluzi be-Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Izimo zokusetshenziswa

Xhuma iklayenti le-MCP ukuze ubhale uhlu lwamadivayisi e-Cacti umsebenzisi walo okhethekile avunyelwe ukuwabona, ufune idivayisi eyodwa evunyelwe, noma uthole izinguqulo zokufakwa lapho umsebenzisi enendawo yokuphatha (realm) edingekayo. Amagama nama-schema okufakwayo kuvela empendulweni yokuthola ye-plugin, ngakho i-adapter ayimphindi umhlinzeki ngamunye. Bona [imithetho yokubhalisa amakhono](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) ye-plugin ukuze uthole imodeli yokubhalisa nemikhawulo yamanje.

## Imephu yekhodi nezivivinyo

| Ukuziphatha | Ukusetshenziswa kwekhodi | Ubufakazi bezivivinyo kuleli khosombe |
|---|---|---|
| Ukuhlolwa kwe-HTTPS, imikhawulo, ukuqinisekiswa kwe-bearer kuphela, nokuhlukaniswa kwamakhasi kwe-v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Ukutholwa kwe-MCP, ukubizwa kwamathuluzi, nezinguquko zezimvume | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Usizo lomugqa womyalo, inguqulo, nokucushwa okungekho | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Isivivinyo se-subprocess sisebenzisa iklayenti neseva yangempela ye-SDK kanye ne-endpoint ye-HTTP yokulingisa. Asidingi futhi asithathi indawo yokuhlolwa kokuhlanganiswa kwe-Cacti ephilayo.

## Indlela ehlala iphephile ngayo

- Isebenzisa i-[`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) esemthethweni yokuqalisa, ukuthola amathuluzi, ukubizwa, nokwakhiwa kwezinhlaka ze-stdio.
- Iveza kuphela amakhono izichasiselo zawo ezithi okokufunda kuphela, okungalimazi, nokungashintshi imiphumela uma kuphindwa (idempotent). Ama-schema namagama kuvela ku-Cacti; i-adapter ayinawo umyalo we-SQL, imininingwane yokungena yamadivayisi, noma imiyalo yokulungisa.
- Ithumela i-bearer token kuphela: awekho ama-cookie, asikho isinyathelo se-CSRF. I-plugin ihlola kabusha ukusebenza kwe-token nezimvume kuzo zonke izicelo.
- Isebenzisa i-HTTPS eqinisekisiwe, ayigcini ama-cookie, yenqaba ukuqondisa kabusha (redirects), futhi iyazishaya indiva okuguquguqukayo kwemvelo kwe-proxy. I-HTTP idinga i-`--allow-loopback-http` kanye nekheli le-loopback eliqondile noma i-`localhost`.
- Ibekela imikhawulo ukubizwa kwe-API kumasekhondi angu-35 sekukonke, amasekhondi angu-5 okuxhuma, amasekhondi angu-30 okungasebenzi kwenethiwekhi, kanye cishe no-1 MB ngempendulo ngayinye (amabhayithi angu-1,100,000). Izindikimba zezicelo zikhawulelwe kumabhayithi angu-16,384. Ukubizwa kulandelaniswa ngesikhathi sokuxhumana kweklayenti ngalinye.
- Ihlola izimpikiswano zamathuluzi ngokuqhathanisa ne-schema yokufakwayo evela ekutholweni kokugcina ngaphambi kokuzithumela, futhi isebenzisa kuphela ama-ID asohlwini oluqinisekisiwe. Ukungafani, noma i-schema engakhiwanga kahle evela kuseva, kubuya njengephutha lethuluzi, hhayi ukuphahlazeka kohlelo.
- Ayiphindi ukuzama ukusebenza ngokuzenzakalelayo. Amaphutha ethuluzi athwala kuphela isimo se-HTTP, i-`status` ye-AIP-193, kanye ne-`reason` ye-ErrorInfo; akulokothi kube umbhalo womlayezo weseva, izindikimba zezimpendulo, noma imininingwane yokungena. I-stdout igcinelwe imilayezo ye-MCP kuphela.

Inguqulo ye-SDK iboshwe yi-`uv.lock` (`mcp>=2.3,<3` ku-`pyproject.toml`). Le adapter isebenzisa iseva yayo ye-2.x yezinga eliphansi enokuthutha kwe-stdio; ayisebenzisi i-endpoint ye-MCP HTTP ekude, i-OAuth, izinsiza, ama-prompt, okubhaliselwe, noma imisebenzi yangemuva.

Bona [isivumelwano se-API](../../../docs/api.md) kanye [nohlelo lokusebenzisa](../../../docs/plan.md).

## Ukufakwa nomugqa womyalo

Idinga i-Python 3.12 noma yakamuva kanye ne-[uv](https://docs.astral.sh/uv/).
Kusukela kukhopi ekhishiwe yaleli khosombe:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Faka bese uvula i-plugin ye-PHP, unikeze indawo yayo yokuphatha (realm) kumsebenzisi we-Cacti okhethekile, bese wakha i-personal access token yalowo msebenzisi (ifomethi ethi `cmcp_pat_` elandelwa izinombolo ze-hex ezincane ezingu-64) kukhonsoli ye-plugin, ekhasini layo elithi My MCP Tokens, noma ngomyalo wayo othi `tokens.php`.
Izindawo zokuphatha ze-Cacti nezimvume zamadivayisi zomsebenzisi ezikhona zisaqhubeka nokusebenza.

Nikeza i-token ngomphathi wakho wezimfihlo njenge-`CACTI_MCP_TOKEN`; ungalokothi uyifake ekulawulweni kwekhodi noma ezimpikiswaneni zomyalo. Setha i-endpoint ngokwehlukana. Kufanele kube yi-URL ye-HTTPS ephela ngokuthi `/plugins/mcp/api.php`, engenayo imininingwane yokungena, i-query, noma i-fragment:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` isetha i-endpoint esikhundleni se-`CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` ivumela i-HTTP evamile ku-`localhost`, `127.0.0.1`, noma `::1` ukuze kuhlolwe endaweni yangakini, `--lang LOCALE` iguqula ulimi lwemilayezo ye-CLI, kanti `--version` iphrinta inguqulo. Ngaphandle kwakho kokubili i-endpoint ne-`CACTI_MCP_TOKEN`, umyalo uyaphuma ngephutha lokusebenzisa.

### Ukuhunyushelwa ezilimini zendawo

Usizo lwe-CLI nemilayezo yamaphutha ye-adapter itholakala ngezilimi zendawo ezingu-45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ngaphandle kokudinga okunye okuncikene nakho. Ukukhethwa kolimi kuhlolwa ku-`--lang`, kulandele i-`LC_ALL`, i-`LC_MESSAGES`, ne-`LANG`, kubuyele ku-`en` (i-`C`/`POSIX` namathegi angaziwa nawo abuyela ku-`en`). Amagama amathuluzi e-MCP, ama-schema, nezimpendulo ze-JSON eziphumelele azithinteki; imilayezo yamaphutha ye-adapter ebuyiswa nge-`is_error=True` ilandela ulimi lwendawo olusebenzayo.

Inqubo ilinda imilayezo ye-MCP ku-stdin. Iklayenti le-MCP ngokuvamile liyayiqala. Kumaklayenti amukela ifomethi evamile yokucushwa ye-`mcpServers`:

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

Cusha iklayenti ukuze lidlulisele i-`CACTI_MCP_ENDPOINT` ne-`CACTI_MCP_TOKEN` ku-subprocess ngokusebenzisa imvelo yalo noma uhlelo lwezimfihlo. Ukutholwa kwemvelo kuncike kuklayenti. Alikho ifulegi lomugqa womyalo le-token.

Ukukhishwa kwe-Python okufakwa ngokwehlukana kuhlinzeka ngomyalo wekhonsoli othi `cacti-mcp`. Akudingeki ukushicilelwa ku-PyPI ukuze kusetshenziswe ikhophi ekhishiwe. I-plugin ye-PHP ayincikile ku-Python.

## Izinguqulo ezikhishiwe

Inguqulo yokukhishwa irekhodwe ku-[pyproject.toml](../../../pyproject.toml). Kuze kube yilapho izikhishiwo ezinamaki zitholakala, sebenzisa ikhophi ekhishiwe yekhodi noma i-artifact ye-`python-distributions` evela [ekusebenzeni kwe-CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) okuphumelele. Le artifact iqukethe i-wheel ne-archive yekhodi yomthombo. Iphakheji efakiwe ihlinzeka ngakho kokubili umyalo othi `cacti-mcp` kanye no-`python -m cacti_mcp`; ayiqukethe i-plugin ye-PHP.

## Ukuthuthukiswa nezivivinyo

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Izivivinyo zihlanganisa ukuhlolwa kwe-HTTP, ukuhlukaniswa kwemininingwane yokungena, izicelo ze-bearer kuphela, ukuhlukaniswa kwamakhasi, ukufihlwa kwemininingwane yamaphutha, kanye nokushintshisana kwangempela kwe-subprocess yeklayenti neseva ye-SDK ngokuqhathanisa neseva ye-HTTP yokulingisa. Azidingi ukufakwa kwe-Cacti ephilayo.

Leli khosombe lisebenzisa i-`src/cacti_mcp/`, i-pytest, i-Ruff, i-uv, ne-Hatchling. I-CI ihlola i-Python 3.12, 3.13, ne-3.14. Umsebenzi wokupakisha ohlukile wakha i-wheel ne-archive yekhodi yomthombo, ufake i-wheel ngaphandle kwekhophi ekhishiwe, bese wenza isivivinyo sokuqinisekisa zombili izindawo zokungena. Okukhishiwe nemiphumela yezivivinyo kungama-artifact e-workflow.

## Ukufaka isandla

Ama-pull request aya ku-`develop`. Gcina i-adapter ihambisana ne-Python 3.12, landela ukucushwa kwe-Ruff okukhona kanye nohlelo lwephakheji ye-`src/cacti_mcp/`, futhi ugcine i-stdout igcinelwe imilayezo ye-MCP. Engeza izivivinyo zokuziphatha okushintshiwe kokuthutha noma kwethuluzi, sebenzisa izivivinyo ezingenhla, bese usayina ama-commit nge-`git commit -s`. Hlela izinguquko ze-API kanye ne-plugin ye-Cacti MCP futhi ubuyekeze i-[docs/api.md](../../../docs/api.md).

## Ilayisensi

Ilungelo lobunikazi (C) 2026 Thomas Vincent. Ikhishwe ngaphansi kwe-GNU General Public License, inguqulo 2 noma yakamuva. Bona i-[LICENSE](../../../LICENSE).
