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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · **Soomaali** · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP waa adabtar Python ah oo awoodaha [Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp) u soo bandhiga sidii qalabka MCP iyadoo la adeegsanayo stdio. Plugin-ku wuxuu horeba si toos ah ugu adeegaa MCP isagoo maraya HTTP, markaa adeegso habkaas marka macmiilkaagu ku xirmi karo seerfar fog. Adabtarkan waxaa loogu talagalay macaamiisha ku hadla stdio oo keliya. Wuxuu adeegsadaa Python MCP SDK-ga rasmiga ah, wuxuuna u turjumaa wicitaannada qalabka inay noqdaan HTTPS API-ga plugin-ka (heshiiska awoodaha v2, oo laga bixiyo waddooyinka `/v1/`, iyadoo la adeegsanayo bearer token oo keliya).
Cacti ayaa leh aqoonsiga (authentication), oggolaanshaha (authorization), xaqiijinta, iyo fulinta.

**Xaaladda: waa la horumarinayaa, ka hor 1.0.** Nooca 0.1.0 wuxuu taageeraa liiska aaladaha ee akhriska keliya iyo noocyada rakibidda iyadoo la adeegsanayo wehelka [Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp).
Weli ma jiro sii-deyn la calaamadeeyay (tagged release). Baaritaannada Doctor iyo dayactirku waa shaqo mustaqbalka ah.

## Waxa uu soo bandhigo

| Hawlgalka | Qalabka MCP ee uu bixiyo Cacti MCP plugin |
|---|---|
| Liis garee aaladaha uu arki karo milkiilaha token-ka | `cacti-list-devices` |
| Akhri hal aalad oo la oggol yahay | `cacti-get-device` |
| Akhri noocyada Cacti, plugin-ka, iyo API-ga | `cacti-get-system-info` |

Magacyada, sharraxaadaha, iyo qaababka gelinta (input schemas) waxay ka yimaadaan jawaabta daahfurka (discovery) ee Cacti ee lagu shaandheeyay oggolaanshaha. Bixiyeyaal kale oo akhris keliya ah oo la oggol yahay waa la ogaan karaa iyadoon lagu darin hawl-wadeenno qalab oo Python ah.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Kiisaska isticmaalka

Ku xir macmiil MCP si aad u liis garayso aaladaha Cacti ee uu isticmaalihiisa gaarka ahi arki karo, u eegto hal aalad oo la oggol yahay, ama u soo saarto noocyada rakibidda marka isticmaaluhu leeyahay awoodda maamul (administrative realm) ee loo baahan yahay. Magacyada iyo qaababka gelintu waxay ka yimaadaan jawaabta daahfurka ee plugin-ka, sidaas darteed adabtarku ma nuqulo bixiye kasta. Eeg [xeerarka diiwaangelinta awoodaha](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) ee plugin-ka si aad u aragto qaabka diiwaangelinta iyo xaddidaadaha hadda jira.

## Khariidadda koodka iyo tijaabooyinka

| Dhaqanka | Hirgelinta | Caddaynta tijaabada ee kaydkan |
|---|---|---|
| Xaqiijinta HTTPS, xuduudaha, aqoonsiga bearer-only, iyo bog-u-qaybinta v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Daahfurka MCP, wicitaannada, iyo isbeddellada oggolaanshaha | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Caawimaadda khadka amarka, nooca, iyo habaynta maqan | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Tijaabada hab-hoosaadka (subprocess test) waxay adeegsataa macmiil iyo seerfar SDK oo dhab ah oo leh barta dhammaadka HTTP oo tijaabo ah (fixture). Uma baahna mana beddesho hubin is-dhexgal oo Cacti oo toos ah.

## Sida uu ammaan ugu ahaado

- Wuxuu adeegsadaa [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) oo rasmi ah bilowga, daahfurka qalabka, wicitaannada, iyo qaabaynta stdio.
- Wuxuu soo bandhigaa oo keliya awoodaha calaamadahoodu (annotations) si sax ah u yihiin akhris keliya (read-only), aan waxba burburin (non-destructive), oo isku mid ah marka lagu celceliyo (idempotent). Qaababka (schemas) iyo magacyadu waxay ka yimaadaan Cacti; adabtarku ma laha wax SQL ah, aqoonsi aaladeed, ama amarro dayactir.
- Wuxuu diraa oo keliya bearer token-ka: ma jiraan cookies, mana jiro tallaabo CSRF ah. Plugin-ku wuxuu dib u hubiyaa ansaxnimada token-ka iyo oggolaanshaha codsi kasta.
- Wuxuu adeegsadaa HTTPS la xaqiijiyay, weligiis ma kaydiyo cookies, wuu diidaa u-weecinta (redirects), wuuna iska indhatiraa doorsoomayaasha deegaanka ee proxy-ga. HTTP wuxuu u baahan yahay `--allow-loopback-http` iyo cinwaan loopback ah oo toos ah ama `localhost`.
- Wuxuu xaddidaa wicitaannada API-ga ilaa 35 ilbiriqsi guud ahaan, 5 ilbiriqsi si uu u xirmo, 30 ilbiriqsi oo hawl-la'aan shabakad ah, iyo qiyaastii 1 MB jawaabkiiba (1,100,000 bytes). Jirka codsiyadu (request bodies) wuxuu ku xaddidan yahay 16,384 bytes. Wicitaannada waxaa loo taxaa mid-mid kalfadhiga macmiilka kasta.
- Wuxuu hubiyaa doodyada qalabka isagoo la barbardhigaya qaabka gelinta ee daahfurkii ugu dambeeyay ka hor inta uusan dirin, wuxuuna fuliyaa oo keliya aqoonsiyada (ids) ka yimid liiskaas la xaqiijiyay. Isku-habboonaan la'aan, ama qaab xun oo ka yimid seerfarka, wuxuu ku soo noqdaa qalad qalab ahaan, ee ma aha burbur barnaamij.
- Si toos ah iskuguma dayo inuu mar kale fuliyo wicitaanka. Khaladaadka qalabku waxay xambaarsan yihiin oo keliya xaaladda HTTP, AIP-193 `status`, iyo ErrorInfo `reason`; weligood ma xambaarsana qoraalka farriinta seerfarka, jirka jawaabaha, ama aqoonsiyada sirta ah. Stdout waxaa loo gaar yeelay farriimaha MCP oo keliya.

Nooca SDK-ga waxaa ku xira `uv.lock` (`mcp>=2.3,<3` gudaha `pyproject.toml`). Adabtarkan wuxuu adeegsadaa seerfarkiisa heerka hoose ee 2.x oo wata gaadiidka stdio; ma hirgeliyo barta dhammaadka HTTP ee MCP ee fog, OAuth, kheyraadka (resources), tilmaamaha (prompts), is-diiwaangelinta (subscriptions), ama hawlaha gadaal ka socda (background tasks).

Eeg [heshiiska API-ga](../../../docs/api.md) iyo [qorshaha hirgelinta](../../../docs/plan.md).

## Rakibidda iyo khadka amarka

Waxay u baahan tahay Python 3.12 ama ka sareeya iyo [uv](https://docs.astral.sh/uv/).
Laga bilaabo nuqul ka mid ah kaydkan:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Rakib oo shid PHP plugin-ka, sii awoodda (realm) isticmaale Cacti oo gaar ah, una samee token gelitaan oo shakhsiyeed isticmaalahaas (qaabka `cmcp_pat_` oo ay ku xigaan 64 lambar oo hex yar-yar ah) gudaha koonsalka plugin-ka, boggiisa My MCP Tokens, ama amarkiisa `tokens.php`.
Awoodaha Cacti ee hadda jira ee isticmaalaha iyo oggolaanshaha aaladuhu weli way shaqaynayaan.

Ku bixi token-ka maamulahaaga sirta (secret manager) sidii `CACTI_MCP_TOKEN`; weligaa ha ku darin kaydka koodka ama doodyada khadka amarka. Si gooni ah u deji barta dhammaadka (endpoint). Waa inay noqotaa URL HTTPS ah oo ku dhammaata `/plugins/mcp/api.php`, iyadoon lahayn wax aqoonsi ah, weydiin (query), ama qayb (fragment):

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` waxay dejisaa barta dhammaadka halkii laga adeegsan lahaa `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` waxay u oggolaataa HTTP caadi ah inuu ku xirmo `localhost`, `127.0.0.1`, ama `::1` tijaabinta maxalliga ah, `--lang LOCALE` waxay beddeshaa luqadda farriimaha CLI, `--version` waxayna daabacdaa nooca. Haddii midkoodna maqan yahay barta dhammaadka ama `CACTI_MCP_TOKEN`, amarku wuxuu ku baxaa qalad isticmaal.

### Luqadeynta

Caawimaadda CLI iyo farriimaha qaladka adabtarku waxay ku yimaadaan 45 luqadood (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) iyadoon loo baahnayn ku-tiirsanaan dheeraad ah. Xallinta luqaddu waxay hubisaa `--lang`, ka dib `LC_ALL`, `LC_MESSAGES`, iyo `LANG`, iyadoo ku noqonaysa `en` (`C`/`POSIX` iyo calaamadaha aan la aqoon iyaguna waxay ku noqdaan `en`). Magacyada qalabka MCP, qaababka (schemas), iyo xogta JSON ee qalabka ee guuleysata lama taabto; farriimaha qaladka adabtarka ee lagu soo celiyo `is_error=True` waxay raacaan luqadda firfircoon.

Habku wuxuu ku sugaa farriimaha MCP dhanka stdin. Macmiil MCP ah ayaa caadi ahaan bilaaba.
Macaamiisha aqbala qaabka habaynta caanka ah ee `mcpServers`:

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

U habeey macmiilka inuu u gudbiyo `CACTI_MCP_ENDPOINT` iyo `CACTI_MCP_TOKEN` hab-hoosaadka iyadoo loo marayo deegaankiisa (environment) ama qaybtiisa sirta. Dhaxalka deegaanku wuxuu ku xiran yahay macmiilka. Ma jiro calan khad amareed (command-line flag) oo loogu talagalay token-ka.

Qaybinta Python ee si gooni ah loo rakibi karo waxay bixisaa amarka koonsalka `cacti-mcp`. Looma baahna daabacaad PyPI si loo socodsiiyo nuqulka kaydka. PHP plugin-ku kuma tiirsana Python.

## Sii-deynta

Nooca qaybinta waxaa lagu diiwaangeliyay [pyproject.toml](../../../pyproject.toml).
Ilaa laga helayo sii-deyn la calaamadeeyay, adeegso nuqulka koodka isha (source checkout) ama agabka `python-distributions` ee ka soo baxa [orod CI ah oo guulaystay](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Agabku wuxuu ka kooban yahay wheel iyo kaydka koodka isha (source archive). Xirmada la rakibay waxay bixisaa labada amar ee `cacti-mcp` iyo `python -m cacti_mcp`; kuma jiro PHP plugin-ku.

## Horumarinta iyo tijaabooyinka

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Tijaabooyinku waxay daboolaan xaqiijinta HTTP, kala-soocidda aqoonsiyada sirta ah, codsiyada bearer-only, bog-u-qaybinta, qarinta qaladaadka (error redaction), iyo is-dhaafsi dhab ah oo hab-hoosaad ah oo u dhexeeya macmiilka iyo seerfarka SDK iyadoo la adeegsanayo seerfar HTTP oo tijaabo ah. Uma baahna rakibid Cacti oo toos ah.

Kaydku wuxuu adeegsadaa `src/cacti_mcp/`, pytest, Ruff, uv, iyo Hatchling. CI wuxuu tijaabiyaa Python 3.12, 3.13, iyo 3.14. Shaqo baakadeed oo gooni ah ayaa dhista wheel-ka iyo kaydka koodka isha, ku rakibta wheel-ka meel ka baxsan nuqulka kaydka, oo hubisa labada barta gelitaanka (smoke-tests). Qaybinnada iyo natiijooyinka tijaabooyinku waa agabyada socodka shaqada (workflow artifacts).

## Ka-qaybqaadashada

Codsiyada isbeddelka (Pull requests) waxay aadaan laanta `develop`. U ilaali adabtarka inuu la jaanqaado Python 3.12, raac habaynta Ruff ee jirta iyo qaab-dhismeedka xirmada `src/cacti_mcp/`, una gaar yeel stdout farriimaha MCP. Ku dar tijaabooyin dhaqanka gaadiidka ama qalabka ee la beddelay, socodsii hubinnada kor ku xusan, oo saxiix commit-yada adigoo adeegsanaya `git commit -s`.
La isku dubbarid isbeddellada API-ga ee Cacti MCP plugin oo cusboonaysii [docs/api.md](../../../docs/api.md).

## Shatiga

Xuquuqda daabacaadda (C) 2026 Thomas Vincent. Waxaa lagu sii daayay iyadoo la raacayo GNU General Public License, nooca 2 ama ka dambeeya. Eeg [LICENSE](../../../LICENSE).
