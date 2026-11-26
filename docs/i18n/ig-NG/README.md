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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · **Igbo** · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP bụ ngwa njikọ Python nke na-ekpughe ikike nke
[ngwa mgbakwụnye Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) dị ka ngwaọrụ MCP
site na stdio. Ngwa mgbakwụnye ahụ na-enye MCP ozugbo site na HTTP, ya mere jiri
nke ahụ mgbe ngwa ahịa gị nwere ike ijikọ na seva dịpụrụ adịpụ. Ngwa njikọ a bụ maka
ngwa ahịa ndị na-ekwu okwu naanị site na stdio. Ọ na-eji Python MCP SDK nke a kwadoro ma
na-atụgharị oku ngwaọrụ ka ọ bụrụ HTTPS API nke ngwa mgbakwụnye ahụ (nkwekọrịta ikike v2, a na-enye
n'okpuru ụzọ `/v1/`, naanị bearer token).
Cacti nwe nkwenye njirimara, ikike nnweta, nyocha izi ezi, na mmejupụta.

**Ọkwa: a ka na-emepe ya, tupu 1.0.** Ụdị 0.1.0 na-akwado ndekọ ngwa naanị maka ọgụgụ
na ụdị nwụnye site na nke so ya bụ
[ngwa mgbakwụnye Cacti MCP](https://github.com/somethingwithproof/plugin_mcp).
Ọ dịghị mbipụta akara aha dị ugbu a. Nnyocha Doctor na ndozigharị bụ ọrụ n'ọdịnihu.

## Ihe ọ na-ekpughe

| Ọrụ | Ngwaọrụ MCP nke ngwa mgbakwụnye Cacti MCP na-enye |
|---|---|
| Depụta ngwa ndị onye nwe token nwere ike ịhụ | `cacti-list-devices` |
| Gụọ otu ngwa e nyere ikike | `cacti-get-device` |
| Gụọ ụdị Cacti, ngwa mgbakwụnye, na API | `cacti-get-system-info` |

Aha, nkọwa, na schema ntinye na-esite na nzaghachi nchọpụta nke Cacti nke e ji ikike yọchaa.
Enwere ike ịchọpụta ndị na-enye ọrụ naanị maka ọgụgụ ọzọ e nyere ikike
na-agbakwụnyeghị njikwa ngwaọrụ Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Ọnọdụ ojiji

Jikọọ ngwa ahịa MCP iji depụta ngwa Cacti nke onye ọrụ ya pụrụ iche nwere ike ịhụ,
chọọ otu ngwa e nyere ikike, ma ọ bụ nweta ụdị nwụnye mgbe onye ọrụ ahụ
nwere mpaghara nchịkwa achọrọ. Aha na schema ntinye na-esite na
nzaghachi nchọpụta nke ngwa mgbakwụnye ahụ, ya mere ngwa njikọ ahụ anaghị emegharị onye na-enye ọrụ ọ bụla.
Lee
[iwu ndebanye aha ikike](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
nke ngwa mgbakwụnye ahụ maka ụdị ndebanye aha na oke dị ugbu a.

## Map koodu na nnwale

| Omume | Mmejupụta | Ihe akaebe nnwale n'ebe nchekwa koodu a |
|---|---|---|
| Nyocha izi ezi HTTPS, oke, nkwenye naanị bearer, na paging v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Nchọpụta MCP, oku, na mgbanwe ikike | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Enyemaka ahịrị iwu, ụdị, na nhazi na-efu efu | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Nnwale usoro okpuru (subprocess) na-eji ezigbo ngwa ahịa na seva SDK nwere ebe njedebe HTTP nnwale.
Ọ chọghị ma ọ bụ dochie nnyocha njikọta Cacti dị ndụ.

## Otu o si anọ na nchekwa

- Ọ na-eji [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) nke a kwadoro
  maka mmalite, nchọpụta ngwaọrụ, oku, na nhazi okpokolo stdio.
- Ọ na-ekpughe naanị ikike ndị nkọwa ha bụ kpọmkwem naanị maka ọgụgụ, anaghị emebi ihe, ma na-eweta otu nsonaazụ mgbe ọ bụla (idempotent). Schema na aha na-esite
  na Cacti; ngwa njikọ ahụ enweghị SQL, nzuzo ngwa, ma ọ bụ iwu ndozigharị.
- Ọ na-eziga naanị bearer token: enweghị kuki, enweghị nzọụkwụ CSRF. Ngwa mgbakwụnye ahụ na-enyochagharị
  izi ezi token na ikike na arịrịọ ọ bụla.
- Ọ na-eji HTTPS a kwadoro, anaghị echekwa kuki ma ọlị, na-ajụ ntụgharị ụzọ (redirects), ma
  na-eleghara mgbanwe gburugburu proxy anya. HTTP chọrọ `--allow-loopback-http`
  na adreesị loopback nkịtị ma ọ bụ `localhost`.
- Ọ na-egbochi oku API ka ọ ghara ịgafe sekọnd 35 n'ozuzu, sekọnd 5 iji jikọọ, sekọnd 30 nke
  enweghị ọrụ netwọk, na ihe dị ka 1 MB kwa nzaghachi (1,100,000 bytes).
  Ahụ arịrịọ nwere oke nke 16,384 bytes. A na-ahazi oku n'usoro otu otu maka oge ngwa ahịa ọ bụla.
- Ọ na-enyocha arụmụka ngwaọrụ megide schema ntinye sitere na nchọpụta ikpeazụ tupu
  iziga ha, ma na-emejupụta naanị ID sitere na katalọgụ ahụ a kwadoro. Ndakọrịtaghị, ma ọ bụ
  schema e mebiri emebi sitere na seva, na-alọghachi dị ka njehie ngwaọrụ, ọ bụghị ndakpọ.
- Ọ naghị anwale mmejupụta ọzọ na-akpaghị aka. Njehie ngwaọrụ na-ebu naanị ọkwa HTTP,
  AIP-193 `status`, na ErrorInfo `reason`; ọ dịghị mgbe ọ na-ebu ederede ozi seva,
  ahụ nzaghachi, ma ọ bụ nzuzo nbanye. E debere stdout naanị maka ozi MCP.

A kwụnyere ụdị SDK site na `uv.lock` (`mcp>=2.3,<3` dị na `pyproject.toml`). Ngwa njikọ a
na-eji seva ọkwa dị ala 2.x ya nwere ụgbọ njem stdio; ọ naghị
emejupụta ebe njedebe MCP HTTP dịpụrụ adịpụ, OAuth, akụrụngwa,
ntuziaka (prompts), ndenye aha, ma ọ bụ ọrụ ndabere.

Lee [nkwekọrịta API](../../../docs/api.md) na [atụmatụ mmejupụta](../../../docs/plan.md).

## Nwụnye na ahịrị iwu

Chọrọ Python 3.12 ma ọ bụ nke ọhụrụ na [uv](https://docs.astral.sh/uv/).
Site na mbudata nke ebe nchekwa koodu a:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Wụnye ma gbanye ngwa mgbakwụnye PHP ahụ, nye onye ọrụ Cacti pụrụ iche mpaghara ya,
ma mepụta token nnweta nkeonwe maka onye ọrụ ahụ (ụdị `cmcp_pat_` nke
ọnụọgụ hex dị nta 64 sochiri) na kọnsọl ngwa mgbakwụnye ahụ, na ibe My MCP Tokens ya,
ma ọ bụ site na iwu `tokens.php` ya.
Mpaghara Cacti na ikike ngwa nke onye ọrụ ahụ dịbu ka na-arụ ọrụ.

Nye token ahụ site na ngwa njikwa ihe nzuzo gị dị ka `CACTI_MCP_TOKEN`; etinyela ya
na njikwa koodu isi ma ọ bụ arụmụka iwu. Tọọ ebe njedebe ahụ iche. Ọ ga-abụrịrị
URL HTTPS nke na-agwụ na `/plugins/mcp/api.php`, na-enweghị nzuzo nbanye, ajụjụ (query), ma ọ bụ
iberibe (fragment):

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` na-atọ ebe njedebe kama `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` na-ekwe ka HTTP nkịtị gaa na `localhost`, `127.0.0.1`, ma ọ bụ `::1`
maka nnwale mpaghara, `--lang LOCALE` na-agbanwe ntụgharị asụsụ mpaghara ozi CLI, na
`--version` na-ebipụta ụdị ya. Na-enweghị ma ebe njedebe ma `CACTI_MCP_TOKEN`,
iwu ahụ na-apụ na njehie ojiji.

### Nhazi asụsụ mpaghara

Enyemaka CLI na ozi njehie ngwa njikọ na-abịa n'asụsụ mpaghara 45 (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) na-enweghị ihe ndabere ọzọ ọ bụla. Mkpebi asụsụ mpaghara
na-enyocha `--lang`, wee `LC_ALL`, `LC_MESSAGES`, na `LANG`, wee laghachi
na `en` (`C`/`POSIX` na mkpado a na-amaghị na-alaghachikwa na `en`). Aha ngwaọrụ MCP,
schema, na ibu data JSON ngwaọrụ gara nke ọma anaghị agbanwe; ozi njehie ngwa njikọ
e weghachiri na `is_error=True` na-agbaso asụsụ mpaghara na-arụ ọrụ.

Usoro ahụ na-echere ozi MCP na stdin. Ngwa ahịa MCP na-amalitekarị ya.
Maka ngwa ahịa ndị na-anabata ụdị nhazi `mcpServers` a na-ejikarị:

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

Hazie ngwa ahịa ahụ ka o nyefee `CACTI_MCP_ENDPOINT` na `CACTI_MCP_TOKEN` n'ime
usoro okpuru ahụ site na gburugburu ya ma ọ bụ ebe nchekwa ihe nzuzo ya. Nketagharị gburugburu
dabere na ngwa ahịa ahụ. Ọ dịghị nhọrọ ahịrị iwu maka token.

Nkesa Python a na-awụnye iche na-enye iwu kọnsọl `cacti-mcp`.
Ọ dịghị mkpa mbipụta PyPI iji gbaa mbudata koodu ahụ. Ngwa mgbakwụnye PHP ahụ
enweghị ndabere Python.

## Mbipụta

E dekọrọ ụdị nkesa ahụ na [pyproject.toml](../../../pyproject.toml).
Ruo mgbe mbipụta akara aha dị, jiri mbudata koodu isi ma ọ bụ
ihe e mepụtara `python-distributions` sitere na
[ọrụ CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) gara nke ọma.
Ihe e mepụtara ahụ nwere wheel na ebe nchekwa koodu isi. Ngwugwu a wụnyere na-enye
ma iwu `cacti-mcp` ma `python -m cacti_mcp`; ọ naghị enwe
ngwa mgbakwụnye PHP ahụ.

## Mmepe na nnwale

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Nnwale na-ekpuchi nyocha izi ezi HTTP, nkewa nzuzo nbanye, arịrịọ naanị bearer,
paging, nhichapụ ozi njehie, na mgbanwe usoro okpuru ngwa ahịa/seva SDK n'ezie megide
seva HTTP nnwale. Ha anaghị achọ nwụnye Cacti dị ndụ.

Ebe nchekwa koodu ahụ na-eji `src/cacti_mcp/`, pytest, Ruff, uv, na Hatchling. CI na-anwale
Python 3.12, 3.13, na 3.14. Ọrụ nkwakọba dị iche na-arụ wheel
na ebe nchekwa koodu isi, na-awụnye wheel ahụ n'ezi mbudata koodu ahụ, ma na-eme nnwale ngwa ngwa
maka ebe nbanye abụọ ahụ. Nkesa na nsonaazụ nnwale bụ ihe e mepụtara n'usoro ọrụ (workflow artifacts).

## Inye aka

Arịrịọ Pull Request na-aga na `develop`. Debe ngwa njikọ ahụ ka ọ dakọọ na Python 3.12,
gbasoo nhazi Ruff dị ugbu a na nhazi ngwugwu `src/cacti_mcp/`, ma
debe stdout naanị maka ozi MCP. Tinye nnwale maka omume ụgbọ njem ma ọ bụ ngwaọrụ
a gbanwere, gbaa nnyocha ndị dị n'elu, ma jiri `git commit -s` bịanye aka na kọmit.
Hazie mgbanwe API na ngwa mgbakwụnye Cacti MCP ma melite [docs/api.md](../../../docs/api.md).

## Ikikere

Ikike nwebisiinka (C) 2026 Thomas Vincent. E wepụtara ya n'okpuru GNU General Public
License, ụdị 2 ma ọ bụ nke ọhụrụ. Lee [LICENSE](../../../LICENSE).
