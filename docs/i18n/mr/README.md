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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · **मराठी** · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP हा एक Python अडॅप्टर आहे जो
[Cacti MCP प्लगइन](https://github.com/somethingwithproof/plugin_mcp) च्या क्षमता stdio द्वारे MCP
साधने म्हणून उपलब्ध करून देतो. हे प्लगइन आधीच थेट HTTP वर MCP सेवा देते, त्यामुळे
जेव्हा तुमचा क्लायंट रिमोट सर्व्हरशी कनेक्ट होऊ शकतो तेव्हा ते वापरा. हा अडॅप्टर
केवळ stdio बोलणाऱ्या क्लायंटसाठी आहे. हे अधिकृत Python MCP SDK वापरते आणि
टूल कॉल्सचे प्लगइनच्या HTTPS API मध्ये (abilities contract v2, `/v1/` मार्गांखाली सेवा दिली जाते, फक्त bearer token) भाषांतर करते.
प्रमाणीकरण, अधिकृतता, पडताळणी आणि अंमलबजावणीची जबाबदारी Cacti कडे असते.

**स्थिती: विकासाधीन, 1.0 पूर्वीची आवृत्ती.** आवृत्ती 0.1.0 सहचर
[Cacti MCP प्लगइन](https://github.com/somethingwithproof/plugin_mcp) द्वारे केवळ-वाचनीय (read-only) डिव्हाइस
इन्व्हेंटरी आणि इंस्टॉलेशन आवृत्त्यांना समर्थन देते.
अद्याप कोणतीही टॅग केलेली रिलीझ नाही. Doctor निदान आणि दुरुस्ती हे भविष्यातील काम आहे.

## हे काय उपलब्ध करून देते

| कार्य | Cacti MCP प्लगइनद्वारे पुरवलेले MCP साधन |
|---|---|
| टोकन मालक पाहू शकत असलेली डिव्हाइसेस सूचीबद्ध करा | `cacti-list-devices` |
| एक परवानगी असलेले डिव्हाइस वाचा | `cacti-get-device` |
| Cacti, प्लगइन आणि API आवृत्त्या वाचा | `cacti-get-system-info` |

नावे, वर्णने आणि इनपुट स्कीमा Cacti च्या परवानगी-फिल्टर केलेल्या
डिस्कव्हरी प्रतिसादातून येतात. Python टूल हँडलर्स न जोडता
अतिरिक्त परवानगी असलेले केवळ-वाचनीय प्रदाते शोधले जाऊ शकतात.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## वापराची उदाहरणे

समर्पित वापरकर्ता पाहू शकत असलेली Cacti डिव्हाइसेस सूचीबद्ध करण्यासाठी,
एक परवानगी असलेले डिव्हाइस शोधण्यासाठी किंवा वापरकर्त्याकडे आवश्यक प्रशासकीय क्षेत्र (realm) असताना इंस्टॉलेशन आवृत्त्या मिळवण्यासाठी MCP क्लायंट कनेक्ट करा.
नावे आणि इनपुट स्कीमा प्लगइनच्या डिस्कव्हरी प्रतिसादातून येतात, त्यामुळे अडॅप्टर प्रत्येक प्रदात्याची पुनरावृत्ती करत नाही.
नोंदणी मॉडेल आणि सद्य मर्यादांसाठी प्लगइनचे
[क्षमता नोंदणी नियम](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
पहा.

## कोड आणि चाचणी नकाशा

| वर्तन | अंमलबजावणी | या रिपॉझिटरीमधील चाचणी पुरावा |
|---|---|---|
| HTTPS पडताळणी, मर्यादा, फक्त-bearer प्रमाणीकरण आणि v2 पेजिंग | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP डिस्कव्हरी, कॉल्स आणि परवानगी बदल | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| कमांड-लाइन मदत, आवृत्ती आणि गहाळ कॉन्फिगरेशन | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

सबप्रोसेस चाचणी फिक्स्चर HTTP एंडपॉइंटसह वास्तविक SDK क्लायंट आणि सर्व्हर वापरते.
यासाठी थेट Cacti एकत्रीकरण तपासणीची आवश्यकता नाही किंवा ती त्याची जागा घेत नाही.

## हे कसे सुरक्षित राहते

- आरंभ, टूल डिस्कव्हरी, कॉल्स आणि stdio फ्रेमिंगसाठी अधिकृत [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  वापरते.
- केवळ अशा क्षमता उपलब्ध करून देते ज्यांचे भाष्य तंतोतंत केवळ-वाचनीय (read-only), अविनष्टकारी (non-destructive) आणि idempotent आहेत. स्कीमा आणि नावे
  Cacti कडून येतात; अडॅप्टरमध्ये कोणतेही SQL, डिव्हाइस क्रेडेन्शियल्स किंवा दुरुस्ती कमांड्स नाहीत.
- फक्त bearer token पाठवते: कोणतीही कुकी नाही, कोणतीही CSRF पायरी नाही. प्लगइन प्रत्येक विनंतीवर
  टोकन वैधता आणि परवानग्या पुन्हा तपासते.
- सत्यापित HTTPS वापरते, कधीही कुकी साठवत नाही, रीडायरेक्ट्स नाकारते आणि
  प्रॉक्सी एन्व्हायर्नमेंट व्हेरिएबल्सकडे दुर्लक्ष करते. HTTP साठी `--allow-loopback-http`
  आणि लिटरल लूपबॅक पत्ता किंवा `localhost` आवश्यक आहे.
- API कॉल्सना एकूण 35 सेकंद, कनेक्ट होण्यासाठी 5 सेकंद, 30 सेकंदांची
  नेटवर्क निष्क्रियता आणि प्रति प्रतिसाद अंदाजे 1 MB (1,100,000 बाइट्स) पर्यंत मर्यादित करते.
  विनंती बॉडी 16,384 बाइट्सपर्यंत मर्यादित आहेत. कॉल्स प्रत्येक क्लायंट
  सेशननुसार अनुक्रमित (serialized) केले जातात.
- टूल आर्ग्युमेंट्स पाठवण्यापूर्वी शेवटच्या डिस्कव्हरीमधील इनपुट स्कीमाविरुद्ध तपासते
  आणि केवळ त्या सत्यापित कॅटलॉगमधील आयडी अंमलात आणते. विसंगती किंवा
  सर्व्हरकडून आलेला सदोष स्कीमा क्रॅशऐवजी टूल त्रुटी म्हणून परत येतो.
- अंमलबजावणीची आपोआप पुनरावृत्ती करत नाही. टूल त्रुटींमध्ये केवळ HTTP
  स्थिती, AIP-193 `status`, आणि ErrorInfo `reason` असते; सर्व्हर
  संदेश मजकूर, प्रतिसाद बॉडी किंवा क्रेडेन्शियल्स कधीही नसतात. Stdout हे MCP संदेशांसाठी राखीव आहे.

SDK आवृत्ती `uv.lock` द्वारे पिन केलेली आहे (`pyproject.toml` मध्ये `mcp>=2.3,<3`). हा
अडॅप्टर stdio ट्रान्सपोर्टसह त्याचा 2.x लो-लेव्हल सर्व्हर वापरतो; तो रिमोट MCP HTTP एंडपॉइंट, OAuth, संसाधने,
प्रॉम्प्ट्स, सबस्क्रिप्शन्स किंवा पार्श्वभूमी कार्ये लागू करत नाही.

[API करार](../../../docs/api.md) आणि [अंमलबजावणी योजना](../../../docs/plan.md) पहा.

## इंस्टॉलेशन आणि कमांड लाइन

Python 3.12 किंवा नंतरची आवृत्ती आणि [uv](https://docs.astral.sh/uv/) आवश्यक आहे.
या रिपॉझिटरीच्या चेकआउटमधून:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

PHP प्लगइन स्थापित आणि सक्षम करा, त्याचे क्षेत्र एका समर्पित Cacti वापरकर्त्याला द्या,
आणि त्या वापरकर्त्यासाठी प्लगइनच्या कन्सोलमध्ये, त्याच्या My MCP Tokens पृष्ठावर,
किंवा त्याच्या `tokens.php` कमांडसह वैयक्तिक प्रवेश टोकन तयार करा (फॉरमॅट `cmcp_pat_` आणि त्यानंतर
64 लोअरकेस हेक्स अंक).
वापरकर्त्याचे विद्यमान Cacti क्षेत्र आणि डिव्हाइस परवानग्या अजूनही लागू राहतात.

तुमच्या सीक्रेट मॅनेजरद्वारे `CACTI_MCP_TOKEN` म्हणून टोकन प्रदान करा; ते कधीही
सोर्स कंट्रोल किंवा कमांड आर्ग्युमेंट्समध्ये जोडू नका. एंडपॉइंट स्वतंत्रपणे सेट करा. तो एक
HTTPS URL असणे आवश्यक आहे जो `/plugins/mcp/api.php` ने समाप्त होतो, ज्यामध्ये कोणतीही क्रेडेन्शियल्स, क्वेरी किंवा
फ्रॅगमेंट नसावेत:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` हे `CACTI_MCP_ENDPOINT` ऐवजी एंडपॉइंट सेट करते.
`--allow-loopback-http` स्थानिक चाचणीसाठी `localhost`, `127.0.0.1`, किंवा `::1` वर साध्या HTTP ला परवानगी देते,
`--lang LOCALE` CLI संदेश स्थानिकीकरण ओव्हरराइड करते आणि
`--version` आवृत्ती प्रिंट करते. एंडपॉइंट आणि `CACTI_MCP_TOKEN` दोन्हीशिवाय,
कमांड वापर त्रुटीसह (usage error) बाहेर पडते.

### स्थानिकीकरण

CLI मदत आणि अडॅप्टर त्रुटी संदेश कोणत्याही अतिरिक्त अवलंबित्वाशिवाय 45 लोकेल्स (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) मध्ये उपलब्ध आहेत. लोकेल
रिझोल्यूशन `--lang`, नंतर `LC_ALL`, `LC_MESSAGES`, आणि `LANG` तपासते आणि शेवटी
`en` वर परत येते (`C`/`POSIX` आणि अज्ञात टॅग देखील `en` वर सोडवले जातात). MCP टूलची
नावे, स्कीमा आणि यशस्वी JSON टूल पेलोड प्रभावित होत नाहीत; `is_error=True` सह परत आलेले अडॅप्टर त्रुटी
संदेश सक्रिय लोकेलचे अनुसरण करतात.

प्रक्रिया stdin वर MCP संदेशांची प्रतीक्षा करते. MCP क्लायंट सामान्यतः ती सुरू करतो.
सामान्य `mcpServers` कॉन्फिगरेशन फॉरमॅट स्वीकारणाऱ्या क्लायंटसाठी:

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

क्लायंटला त्याच्या एन्व्हायर्नमेंट किंवा सीक्रेट सुविधेद्वारे सबप्रोसेसला `CACTI_MCP_ENDPOINT` आणि `CACTI_MCP_TOKEN` पास करण्यासाठी
कॉन्फिगर करा. एन्व्हायर्नमेंट इनहेरिटन्स
क्लायंटवर अवलंबून असते. टोकनसाठी कोणताही कमांड-लाइन फ्लॅग नाही.

स्वतंत्रपणे इंस्टॉल करण्यायोग्य Python वितरण `cacti-mcp` कन्सोल
कमांड प्रदान करते. चेकआउट चालवण्यासाठी PyPI प्रकाशनाची आवश्यकता नाही. PHP प्लगइनला
कोणतेही Python अवलंबित्व नाही.

## रिलीझ

वितरण आवृत्ती [pyproject.toml](../../../pyproject.toml) मध्ये नोंदवलेली आहे.
टॅग केलेल्या रिलीझ उपलब्ध होईपर्यंत, सोर्स चेकआउट किंवा यशस्वी
[CI रन](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) मधील `python-distributions` आर्टिफॅक्ट वापरा.
आर्टिफॅक्टमध्ये व्हील (wheel) आणि सोर्स आर्काइव्ह असते. इंस्टॉल केलेले पॅकेज
`cacti-mcp` कमांड आणि `python -m cacti_mcp` दोन्ही पुरवते; त्यामध्ये
PHP प्लगइन समाविष्ट नाही.

## विकास आणि चाचण्या

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

चाचण्या HTTP पडताळणी, क्रेडेन्शियल आयसोलेशन, फक्त-bearer विनंत्या,
पेजिंग, त्रुटी लपवणे (redaction) आणि फिक्स्चर HTTP सर्व्हरविरुद्ध वास्तविक SDK क्लायंट/सर्व्हर सबप्रोसेस एक्सचेंज
कव्हर करतात. त्यांना थेट Cacti इंस्टॉलेशनची आवश्यकता नाही.

रिपॉझिटरी `src/cacti_mcp/`, pytest, Ruff, uv, आणि Hatchling वापरते. CI
Python 3.12, 3.13, आणि 3.14 ची चाचणी करते. एक वेगळे पॅकेजिंग कार्य व्हील
आणि सोर्स आर्काइव्ह तयार करते, चेकआउटच्या बाहेर व्हील इंस्टॉल करते आणि दोन्ही
एंट्री पॉइंट्सची स्मोक-टेस्ट करते. वितरणे आणि चाचणी परिणाम हे वर्कफ्लो आर्टिफॅक्ट्स आहेत.

## योगदान

पुल रिक्वेस्ट्स `develop` वर जातात. अडॅप्टर Python 3.12 शी सुसंगत ठेवा,
विद्यमान Ruff कॉन्फिगरेशन आणि `src/cacti_mcp/` पॅकेज लेआउटचे अनुसरण करा आणि
stdout हे MCP संदेशांसाठी राखीव ठेवा. बदललेल्या ट्रान्सपोर्ट किंवा टूल
वर्तनासाठी चाचण्या जोडा, वरील तपासण्या चालवा आणि `git commit -s` ने कमिट्स साइन ऑफ करा.
Cacti MCP प्लगइनसोबत API बदलांचे समन्वय साधा आणि [docs/api.md](../../../docs/api.md) अपडेट करा.

## परवाना

कॉपीराइट (C) 2026 Thomas Vincent. GNU General Public
License, आवृत्ती 2 किंवा त्यानंतरच्या आवृत्तीअंतर्गत प्रकाशित. [LICENSE](../../../LICENSE) पहा.
