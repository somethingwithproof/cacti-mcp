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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · **हिन्दी** · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP एक Python एडाप्टर है जो [Cacti MCP प्लगइन](https://github.com/somethingwithproof/plugin_mcp) की क्षमताओं को stdio पर MCP टूल के रूप में उपलब्ध कराता है। यह प्लगइन पहले से ही सीधे HTTP पर MCP सेवा प्रदान करता है, इसलिए जब आपका क्लाइंट किसी रिमोट सर्वर से जुड़ सकता हो तो उसका उपयोग करें। यह एडाप्टर उन क्लाइंट के लिए है जो केवल stdio का उपयोग करते हैं। यह आधिकारिक Python MCP SDK का उपयोग करता है और टूल कॉल को प्लगइन के HTTPS API (क्षमता अनुबंध v2, `/v1/` पथों के अंतर्गत सेवित, केवल bearer token) में अनुवादित करता है। प्रमाणीकरण, प्राधिकरण, सत्यापन और निष्पादन Cacti के पास रहते हैं।

**स्थिति: निर्माणाधीन, 1.0 से पहले।** संस्करण 0.1.0 सहयोगी [Cacti MCP प्लगइन](https://github.com/somethingwithproof/plugin_mcp) के माध्यम से केवल-पठनीय डिवाइस इन्वेंटरी और इंस्टॉलेशन संस्करणों का समर्थन करता है। अभी तक कोई टैग की गई रिलीज़ नहीं है। Doctor डायग्नोस्टिक्स और मरम्मत भविष्य के कार्य हैं।

## यह क्या उपलब्ध कराता है

| कार्य | Cacti MCP प्लगइन द्वारा प्रदान किया गया MCP टूल |
|---|---|
| उन डिवाइसों की सूची बनाना जिन्हें टोकन स्वामी देख सकता है | `cacti-list-devices` |
| एक अनुमत डिवाइस को पढ़ना | `cacti-get-device` |
| Cacti, प्लगइन और API संस्करण पढ़ना | `cacti-get-system-info` |

नाम, विवरण और इनपुट स्कीमा Cacti की अनुमति-फ़िल्टर की गई डिस्कवरी प्रतिक्रिया से आते हैं। Python टूल हैंडलर जोड़े बिना अतिरिक्त अनुमत केवल-पठनीय प्रदाताओं को खोजा जा सकता है।

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## उपयोग के मामले

एक MCP क्लाइंट को कनेक्ट करें ताकि उन Cacti डिवाइसों की सूची देखी जा सके जिन्हें उसका समर्पित उपयोगकर्ता देख सकता है, किसी एक अनुमत डिवाइस की जानकारी देखी जा सके, या जब उपयोगकर्ता के पास आवश्यक प्रशासनिक क्षेत्र हो तो इंस्टॉलेशन संस्करण प्राप्त किए जा सकें। नाम और इनपुट स्कीमा प्लगइन की डिस्कवरी प्रतिक्रिया से आते हैं, इसलिए एडाप्टर प्रत्येक प्रदाता की नकल नहीं करता है। पंजीकरण मॉडल और वर्तमान सीमाओं के लिए प्लगइन के [क्षमता पंजीकरण नियम](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) देखें।

## कोड और परीक्षण मानचित्र

| व्यवहार | कार्यान्वयन | इस रिपॉजिटरी में परीक्षण प्रमाण |
|---|---|---|
| HTTPS सत्यापन, सीमाएं, केवल-bearer प्रमाणीकरण और v2 पेजिंग | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP डिस्कवरी, कॉल और अनुमति परिवर्तन | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| कमांड-लाइन सहायता, संस्करण और अनुपलब्ध कॉन्फ़िगरेशन | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

सबप्रोसेस परीक्षण एक फिक्स्चर HTTP एंडपॉइंट के साथ वास्तविक SDK क्लाइंट और सर्वर का उपयोग करता है। इसके लिए लाइव Cacti एकीकरण जांच की आवश्यकता नहीं है और न ही यह उसका स्थान लेता है।

## यह सुरक्षित कैसे रहता है

- प्रारंभिकरण, टूल डिस्कवरी, कॉल और stdio फ्रेमिंग के लिए आधिकारिक [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) का उपयोग करता है।
- केवल उन क्षमताओं को उपलब्ध कराता है जिनके एनोटेशन बिल्कुल केवल-पठनीय, गैर-विनाशकारी और आइडम्पोटेंट हैं। स्कीमा और नाम Cacti से आते हैं; एडाप्टर में कोई SQL, डिवाइस क्रेडेंशियल या मरम्मत कमांड नहीं हैं।
- केवल bearer token भेजता है: कोई कुकी नहीं, कोई CSRF चरण नहीं। प्लगइन प्रत्येक अनुरोध पर टोकन की वैधता और अनुमतियों की पुनः जांच करता है।
- सत्यापित HTTPS का उपयोग करता है, कभी कुकी संग्रहीत नहीं करता, रीडायरेक्ट को अस्वीकार करता है और प्रॉक्सी पर्यावरण चरों को अनदेखा करता है। HTTP के लिए `--allow-loopback-http` और एक शाब्दिक लूपबैक पता या `localhost` आवश्यक है।
- API कॉल को कुल 35 सेकंड, कनेक्ट करने के लिए 5 सेकंड, नेटवर्क निष्क्रियता के 30 सेकंड और प्रति प्रतिक्रिया लगभग 1 MB (1,100,000 बाइट्स) तक सीमित करता है। अनुरोध बॉडी 16,384 बाइट्स तक सीमित हैं। प्रति क्लाइंट सत्र कॉल क्रमिक रूप से किए जाते हैं।
- टूल तर्कों को भेजने से पहले अंतिम डिस्कवरी के इनपुट स्कीमा से जांचता है और केवल उस सत्यापित कैटलॉग से आईडी निष्पादित करता है। बेमेल होने या सर्वर से विकृत स्कीमा आने पर क्रैश के बजाय टूल त्रुटि वापस आती है।
- निष्पादन को स्वचालित रूप से पुनः प्रयास नहीं करता। टूल त्रुटियों में केवल HTTP स्थिति, AIP-193 `status` और ErrorInfo `reason` शामिल होते हैं; सर्वर संदेश पाठ, प्रतिक्रिया बॉडी या क्रेडेंशियल कभी नहीं। stdout MCP संदेशों के लिए आरक्षित है।

SDK संस्करण `uv.lock` (`pyproject.toml` में `mcp>=2.3,<3`) द्वारा पिन किया गया है। यह एडाप्टर stdio ट्रांसपोर्ट के साथ अपने 2.x निम्न-स्तरीय सर्वर का उपयोग करता है; यह रिमोट MCP HTTP एंडपॉइंट, OAuth, संसाधन, प्रॉम्प्ट, सदस्यता या पृष्ठभूमि कार्य कार्यान्वित नहीं करता है।

[API अनुबंध](../../../docs/api.md) और [कार्यान्वयन योजना](../../../docs/plan.md) देखें।

## स्थापना और कमांड लाइन

Python 3.12 या उसके बाद का संस्करण और [uv](https://docs.astral.sh/uv/) आवश्यक है। इस रिपॉजिटरी के चेकआउट से:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

PHP प्लगइन को स्थापित और सक्षम करें, एक समर्पित Cacti उपयोगकर्ता को इसका क्षेत्र प्रदान करें, और प्लगइन के कंसोल में, इसके My MCP Tokens पृष्ठ पर, या इसके `tokens.php` कमांड से उस उपयोगकर्ता के लिए एक व्यक्तिगत एक्सेस टोकन (प्रारूप `cmcp_pat_` जिसके बाद 64 छोटे अक्षर के हेक्स अंक हों) बनाएं। उपयोगकर्ता के मौजूदा Cacti क्षेत्र और डिवाइस अनुमतियां अभी भी लागू होती हैं।

अपने सीक्रेट मैनेजर के माध्यम से `CACTI_MCP_TOKEN` के रूप में टोकन प्रदान करें; इसे कभी भी सोर्स कंट्रोल या कमांड तर्कों में न जोड़ें। एंडपॉइंट को अलग से सेट करें। यह एक HTTPS URL होना चाहिए जो `/plugins/mcp/api.php` पर समाप्त होता हो, जिसमें कोई क्रेडेंशियल, क्वेरी या फ्रैगमेंट न हो:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL`, `CACTI_MCP_ENDPOINT` के बजाय एंडपॉइंट सेट करता है। `--allow-loopback-http` स्थानीय परीक्षण के लिए `localhost`, `127.0.0.1`, या `::1` पर सामान्य HTTP की अनुमति देता है, `--lang LOCALE` CLI संदेश स्थानीयकरण को ओवरराइड करता है, और `--version` संस्करण प्रिंट करता है। एंडपॉइंट और `CACTI_MCP_TOKEN` दोनों के बिना, कमांड उपयोग त्रुटि के साथ बाहर निकलता है।

### स्थानीयकरण

CLI सहायता और एडाप्टर त्रुटि संदेश बिना किसी अतिरिक्त निर्भरता के 45 लोकेल (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) में आते हैं। लोकेल रिज़ॉल्यूशन `--lang`, फिर `LC_ALL`, `LC_MESSAGES`, और `LANG` की जांच करता है, और कुछ न मिलने पर `en` पर वापस आ जाता है (`C`/`POSIX` और अज्ञात टैग भी `en` पर ही जाते हैं)। MCP टूल के नाम, स्कीमा और सफल JSON टूल पेलोड अप्रभावित रहते हैं; `is_error=True` के साथ लौटाए गए एडाप्टर त्रुटि संदेश सक्रिय लोकेल का पालन करते हैं।

प्रक्रिया stdin पर MCP संदेशों की प्रतीक्षा करती है। आमतौर पर एक MCP क्लाइंट इसे लॉन्च करता है। सामान्य `mcpServers` कॉन्फ़िगरेशन प्रारूप स्वीकार करने वाले क्लाइंट के लिए:

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

क्लाइंट को उसके पर्यावरण या सीक्रेट सुविधा के माध्यम से सबप्रोसेस को `CACTI_MCP_ENDPOINT` और `CACTI_MCP_TOKEN` पास करने के लिए कॉन्फ़िगर करें। पर्यावरण वंशानुक्रम क्लाइंट पर निर्भर करता है। कोई टोकन कमांड-लाइन फ़्लैग नहीं है।

अलग से स्थापित होने वाला Python वितरण `cacti-mcp` कंसोल कमांड प्रदान करता है। चेकआउट को चलाने के लिए किसी PyPI प्रकाशन की आवश्यकता नहीं है। PHP प्लगइन की कोई Python निर्भरता नहीं है।

## रिलीज़

वितरण संस्करण [pyproject.toml](../../../pyproject.toml) में दर्ज है। जब तक टैग की गई रिलीज़ उपलब्ध न हों, तब तक सोर्स चेकआउट या एक सफल [CI रन](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) से `python-distributions` आर्टिफैक्ट का उपयोग करें। आर्टिफैक्ट में एक wheel और सोर्स आर्काइव शामिल है। स्थापित पैकेज `cacti-mcp` कमांड और `python -m cacti_mcp` दोनों प्रदान करता है; इसमें PHP प्लगइन शामिल नहीं है।

## विकास और परीक्षण

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

परीक्षण एक फिक्स्चर HTTP सर्वर के विरुद्ध HTTP सत्यापन, क्रेडेंशियल अलगाव, केवल-bearer अनुरोध, पेजिंग, त्रुटि संशोधन और एक वास्तविक SDK क्लाइंट/सर्वर सबप्रोसेस विनिमय को कवर करते हैं। इनके लिए लाइव Cacti इंस्टॉलेशन की आवश्यकता नहीं है।

रिपॉजिटरी `src/cacti_mcp/`, pytest, Ruff, uv, और Hatchling का उपयोग करती है। CI Python 3.12, 3.13, और 3.14 का परीक्षण करता है। एक अलग पैकेजिंग कार्य wheel और सोर्स आर्काइव बनाता है, चेकआउट के बाहर wheel स्थापित करता है, और दोनों प्रवेश बिंदुओं का स्मोक-टेस्ट करता है। वितरण और परीक्षण परिणाम वर्कफ़्लो आर्टिफैक्ट हैं।

## योगदान

पुल अनुरोध `develop` पर जाएं। एडाप्टर को Python 3.12 के साथ संगत रखें, मौजूदा Ruff कॉन्फ़िगरेशन और `src/cacti_mcp/` पैकेज लेआउट का पालन करें, और stdout को MCP संदेशों के लिए आरक्षित रखें। बदले गए ट्रांसपोर्ट या टूल व्यवहार के लिए परीक्षण जोड़ें, ऊपर दिए गए जांच चलाएं, और `git commit -s` के साथ कमिट पर हस्ताक्षर करें। Cacti MCP प्लगइन के साथ API परिवर्तनों का समन्वय करें और [docs/api.md](../../../docs/api.md) को अपडेट करें।

## लाइसेंस

कॉपीराइट (C) 2026 Thomas Vincent। GNU General Public License, संस्करण 2 या बाद के संस्करण के तहत जारी। [LICENSE](../../../LICENSE) देखें।
