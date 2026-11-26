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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · **বাংলা** · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP হলো একটি Python অ্যাডাপ্টার, যা stdio-এর মাধ্যমে [Cacti MCP প্লাগইন](https://github.com/somethingwithproof/plugin_mcp)-এর সক্ষমতাগুলোকে MCP টুল হিসেবে উপস্থাপন করে। প্লাগইনটি আগে থেকেই সরাসরি HTTP-এর মাধ্যমে MCP সেবা প্রদান করে, তাই আপনার ক্লায়েন্ট যদি রিমোট সার্ভারে সংযোগ করতে পারে তবে সেটিই ব্যবহার করুন। এই অ্যাডাপ্টারটি সেইসব ক্লায়েন্টের জন্য তৈরি যারা কেবল stdio-তে কাজ করে। এটি অফিশিয়াল Python MCP SDK ব্যবহার করে এবং টুল কলগুলোকে প্লাগইনের HTTPS API-তে (abilities contract v2, যা `/v1/` পাথের অধীনে পরিবেশিত হয়, কেবল bearer টোকেন) রূপান্তর করে।
প্রমাণীকরণ (authentication), অনুমোদন (authorization), যাচাইকরণ এবং সম্পাদনের দায়িত্ব Cacti-এর।

**অবস্থা: উন্নয়নাধীন, 1.0-এর পূর্ববর্তী।** সংস্করণ 0.1.0 সহযোগী [Cacti MCP প্লাগইন](https://github.com/somethingwithproof/plugin_mcp)-এর মাধ্যমে কেবল পঠনযোগ্য (read-only) ডিভাইস ইনভেন্টরি এবং ইনস্টলেশন সংস্করণ সমর্থন করে। এখনও কোনো ট্যাগ করা রিলিজ নেই। Doctor ডায়াগনস্টিকস এবং মেরামত ভবিষ্যতের কাজ।

## এটি কী কী প্রকাশ করে

| অপারেশন | Cacti MCP প্লাগইন দ্বারা প্রদত্ত MCP টুল |
|---|---|
| টোকেনের মালিক যে ডিভাইসগুলো দেখতে পারেন তার তালিকা | `cacti-list-devices` |
| অনুমোদিত একটি ডিভাইস পড়া | `cacti-get-device` |
| Cacti, প্লাগইন এবং API সংস্করণ পড়া | `cacti-get-system-info` |

নাম, বিবরণ এবং ইনপুট স্কিমা Cacti-এর অনুমতি-ফিল্টারকৃত ডিসকভারি রেসপন্স থেকে আসে। নতুন Python টুল হ্যান্ডলার যোগ না করেই অতিরিক্ত অনুমোদিত read-only প্রোভাইডার ডিসকভার করা যায়।

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## ব্যবহারের ক্ষেত্র

একটি MCP ক্লায়েন্ট সংযুক্ত করে তার নির্ধারিত ব্যবহারকারী যে Cacti ডিভাইসগুলো দেখতে পারেন তার তালিকা দেখুন, অনুমোদিত একটি ডিভাইস খুঁজুন, অথবা ব্যবহারকারীর প্রয়োজনীয় প্রশাসনিক রিয়েলম (realm) থাকলে ইনস্টলেশন সংস্করণ সংগ্রহ করুন। নাম এবং ইনপুট স্কিমা প্লাগইনের ডিসকভারি রেসপন্স থেকে আসে, তাই অ্যাডাপ্টারটি প্রতিটি প্রোভাইডারের তথ্য পুনরাবৃত্তি করে না। রেজিস্ট্রেশন মডেল এবং বর্তমান সীমাবদ্ধতার জন্য প্লাগইনের [সক্ষমতা নিবন্ধন নিয়মাবলি](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) দেখুন।

## কোড এবং টেস্ট মানচিত্র

| আচরণ | বাস্তবায়ন | এই রিপোজিটরিতে টেস্টের প্রমাণ |
|---|---|---|
| HTTPS যাচাইকরণ, সীমা, কেবল bearer-ভিত্তিক auth এবং v2 পেজিং | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP ডিসকভারি, কল এবং অনুমতির পরিবর্তন | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| কমান্ড-লাইন সাহায্য, সংস্করণ এবং অনুপস্থিত কনফিগারেশন | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

সাবপ্রসেস টেস্টটি একটি ফিক্সচার HTTP এন্ডপয়েন্টের সাথে প্রকৃত SDK ক্লায়েন্ট ও সার্ভার ব্যবহার করে। এর জন্য কোনো লাইভ Cacti ইনস্টলেশনের প্রয়োজন হয় না এবং এটি লাইভ ইন্টিগ্রেশন পরীক্ষার বিকল্পও নয়।

## এটি কীভাবে নিরাপদ থাকে

- ইনিশিয়ালাইজেশন, টুল ডিসকভারি, কল এবং stdio ফ্রেমিংয়ের জন্য অফিশিয়াল [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) ব্যবহার করে।
- কেবল সেইসব সক্ষমতাই প্রকাশ করে যেগুলোর অ্যানোটেশন সম্পূর্ণভাবে read-only, non-destructive এবং idempotent। স্কিমা এবং নাম Cacti থেকে আসে; অ্যাডাপ্টারটিতে কোনো SQL, ডিভাইসের শংসাপত্র বা মেরামতের কমান্ড থাকে না।
- কেবল bearer টোকেন পাঠায়: কোনো কুকি বা CSRF ধাপ নেই। প্লাগইনটি প্রতিটি রিকোয়েস্টে টোকেনের বৈধতা এবং অনুমতি পুনরায় যাচাই করে।
- যাচাইকৃত HTTPS ব্যবহার করে, কখনোই কুকি সংরক্ষণ করে না, রিডাইরেক্ট প্রত্যাখ্যান করে এবং প্রক্সি এনভায়রনমেন্ট ভেরিয়েবল উপেক্ষা করে। HTTP-এর জন্য `--allow-loopback-http` এবং একটি আক্ষরিক লুপব্যাক ঠিকানা বা `localhost` প্রয়োজন।
- API কলগুলোকে সামগ্রিকভাবে ৩৫ সেকেন্ড, সংযোগের জন্য ৫ সেকেন্ড, নেটওয়ার্ক নিষ্ক্রিয়তার জন্য ৩০ সেকেন্ড এবং প্রতি রেসপন্সে প্রায় 1 MB (1,100,000 বাইট)-এর মধ্যে সীমাবদ্ধ রাখে। রিকোয়েস্ট বডি 16,384 বাইটে সীমাবদ্ধ। প্রতি ক্লায়েন্ট সেশনে কলগুলো ক্রমানুসারে সম্পন্ন হয়।
- পাঠানোর আগে সর্বশেষ ডিসকভারি থেকে প্রাপ্ত ইনপুট স্কিমার বিপরীতে টুল আর্গুমেন্টগুলো যাচাই করে এবং কেবল সেই যাচাইকৃত ক্যাটালগের id-গুলোই চালায়। অসঙ্গতি বা সার্ভার থেকে আসা ত্রুটিপূর্ণ স্কিমা ক্র্যাশ না হয়ে টুল ত্রুটি হিসেবে ফিরে আসে।
- স্বয়ংক্রিয়ভাবে পুনরায় চালানোর চেষ্টা করে না। টুল ত্রুটিগুলোতে কেবল HTTP স্ট্যাটাস, AIP-193 `status` এবং ErrorInfo `reason` থাকে; কখনোই সার্ভারের বার্তার টেক্সট, রেসপন্স বডি বা শংসাপত্র থাকে না। Stdout কেবল MCP বার্তার জন্য সংরক্ষিত।

SDK সংস্করণটি `uv.lock` দ্বারা পিন করা আছে (`pyproject.toml`-এ `mcp>=2.3,<3`)। এই অ্যাডাপ্টারটি stdio ট্রান্সপোর্টসহ এর 2.x লো-লেভেল সার্ভার ব্যবহার করে; এটি কোনো রিমোট MCP HTTP এন্ডপয়েন্ট, OAuth, রিসোর্স, প্রম্পট, সাবস্ক্রিপশন বা ব্যাকগ্রাউন্ড টাস্ক বাস্তবায়ন করে না।

[API চুক্তি](../../../docs/api.md) এবং [বাস্তবায়ন পরিকল্পনা](../../../docs/plan.md) দেখুন।

## ইনস্টলেশন এবং কমান্ড লাইন

Python 3.12 বা তার পরবর্তী সংস্করণ এবং [uv](https://docs.astral.sh/uv/) প্রয়োজন।
এই রিপোজিটরির একটি চেকআউট থেকে:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

PHP প্লাগইনটি ইনস্টল ও সক্রিয় করুন, একটি নির্ধারিত Cacti ব্যবহারকারীকে এর রিয়েলম প্রদান করুন এবং প্লাগইনের কনসোলে, এর My MCP Tokens পৃষ্ঠায় অথবা এর `tokens.php` কমান্ডের মাধ্যমে সেই ব্যবহারকারীর জন্য একটি পার্সোনাল অ্যাক্সেস টোকেন তৈরি করুন (ফরম্যাট `cmcp_pat_` এবং তারপরে ৬৪টি ছোট হাতের হেক্স অঙ্ক)। ব্যবহারকারীর বিদ্যমান Cacti রিয়েলম এবং ডিভাইসের অনুমতিগুলো তখনও প্রযোজ্য থাকবে।

আপনার সিক্রেট ম্যানেজারের মাধ্যমে টোকেনটি `CACTI_MCP_TOKEN` হিসেবে সরবরাহ করুন; কখনোই এটিকে সোর্স কন্ট্রোল বা কমান্ড আর্গুমেন্টে যোগ করবেন না। এন্ডপয়েন্টটি আলাদাভাবে সেট করুন। এটি অবশ্যই `/plugins/mcp/api.php` দিয়ে শেষ হওয়া একটি HTTPS URL হতে হবে, যেখানে কোনো শংসাপত্র, কোয়েরি বা ফ্র্যাগমেন্ট থাকবে না:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` ব্যবহার করলে `CACTI_MCP_ENDPOINT`-এর পরিবর্তে সেই এন্ডপয়েন্ট সেট হয়।
স্থানীয় পরীক্ষার জন্য `--allow-loopback-http` ফ্ল্যাগটি `localhost`, `127.0.0.1` বা `::1`-এ সাধারণ HTTP অনুমোদন করে, `--lang LOCALE` CLI বার্তার লোকালাইজেশন ওভাররাইড করে এবং `--version` সংস্করণ প্রিন্ট করে। এন্ডপয়েন্ট এবং `CACTI_MCP_TOKEN` উভয়ই ছাড়া কমান্ডটি একটি ব্যবহার সংক্রান্ত ত্রুটি দিয়ে প্রস্থান করে।

### লোকালাইজেশন

CLI সাহায্য এবং অ্যাডাপ্টারের ত্রুটি বার্তাগুলো কোনো অতিরিক্ত ডিপেন্ডেন্সি ছাড়াই ৪৫টি লোকেলে (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) সরবরাহ করা হয়। লোকেল নির্ধারণে প্রথমে `--lang`, তারপর `LC_ALL`, `LC_MESSAGES` এবং `LANG` পরীক্ষা করা হয়, এবং না পাওয়া গেলে `en`-এ ফিরে যায় (`C`/`POSIX` এবং অজানা ট্যাগগুলোও `en`-এ নির্ধারিত হয়)। MCP টুলের নাম, স্কিমা এবং সফল JSON টুল পেলোড অপরিবর্তিত থাকে; `is_error=True` সহ ফেরত আসা অ্যাডাপ্টার ত্রুটি বার্তাগুলো সক্রিয় লোকেল অনুসরণ করে।

প্রক্রিয়াটি stdin-এ MCP বার্তার জন্য অপেক্ষা করে। সাধারণত একটি MCP ক্লায়েন্ট এটি চালু করে। প্রচলিত `mcpServers` কনফিগারেশন ফরম্যাট গ্রহণকারী ক্লায়েন্টগুলোর জন্য:

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

সাবপ্রসেসে এনভায়রনমেন্ট বা সিক্রেট সুবিধার মাধ্যমে `CACTI_MCP_ENDPOINT` এবং `CACTI_MCP_TOKEN` পাঠানোর জন্য ক্লায়েন্টটি কনফিগার করুন। এনভায়রনমেন্ট ইনহেরিট্যান্স ক্লায়েন্টের ওপর নির্ভর করে। কোনো টোকেন কমান্ড-লাইন ফ্ল্যাগ নেই।

আলাদাভাবে ইনস্টলযোগ্য Python ডিস্ট্রিবিউশনটি `cacti-mcp` কনসোল কমান্ড সরবরাহ করে। চেকআউটটি চালানোর জন্য PyPI-তে প্রকাশের প্রয়োজন নেই। PHP প্লাগইনটির কোনো Python ডিপেন্ডেন্সি নেই।

## রিলিজসমূহ

ডিস্ট্রিবিউশন সংস্করণটি [pyproject.toml](../../../pyproject.toml)-এ নথিভুক্ত আছে। ট্যাগ করা রিলিজ উপলব্ধ না হওয়া পর্যন্ত, একটি সোর্স চেকআউট অথবা সফল [CI রান](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) থেকে প্রাপ্ত `python-distributions` আর্টিফ্যাক্ট ব্যবহার করুন। আর্টিফ্যাক্টটিতে একটি হুইল (wheel) এবং সোর্স আর্কাইভ থাকে। ইনস্টল করা প্যাকেজটি `cacti-mcp` কমান্ড এবং `python -m cacti_mcp` উভয়ই সরবরাহ করে; এতে PHP প্লাগইনটি অন্তর্ভুক্ত থাকে না।

## উন্নয়ন এবং টেস্ট

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

টেস্টগুলো HTTP যাচাইকরণ, শংসাপত্র বিচ্ছিন্নতা, কেবল bearer রিকোয়েস্ট, পেজিং, ত্রুটি সংশোধন (redaction) এবং একটি ফিক্সচার HTTP সার্ভারের বিপরীতে প্রকৃত SDK ক্লায়েন্ট/সার্ভার সাবপ্রসেস বিনিময় কভার করে। এগুলোর জন্য কোনো লাইভ Cacti ইনস্টলেশনের প্রয়োজন হয় না।

রিপোজিটরিটি `src/cacti_mcp/`, pytest, Ruff, uv এবং Hatchling ব্যবহার করে। CI পরিবেশে Python 3.12, 3.13 এবং 3.14 পরীক্ষা করা হয়। একটি পৃথক প্যাকেজিং জব হুইল এবং সোর্স আর্কাইভ তৈরি করে, চেকআউটের বাইরে হুইলটি ইনস্টল করে এবং উভয় এন্ট্রি পয়েন্টের স্মোক-টেস্ট চালায়। ডিস্ট্রিবিউশন এবং টেস্টের ফলাফলগুলো ওয়ার্কফ্লো আর্টিফ্যাক্ট হিসেবে থাকে।

## অবদান রাখা

পুল রিকোয়েস্টগুলো `develop` শাখায় পাঠান। অ্যাডাপ্টারটিকে Python 3.12-এর সাথে সামঞ্জস্যপূর্ণ রাখুন, বিদ্যমান Ruff কনফিগারেশন এবং `src/cacti_mcp/` প্যাকেজ লেআউট অনুসরণ করুন এবং stdout কেবল MCP বার্তার জন্য সংরক্ষিত রাখুন। পরিবর্তিত ট্রান্সপোর্ট বা টুল আচরণের জন্য টেস্ট যোগ করুন, উপরের চেকগুলো চালান এবং `git commit -s` ব্যবহার করে কমিটগুলোতে সাইন অফ করুন। Cacti MCP প্লাগইনের সাথে API পরিবর্তনগুলোর সমন্বয় করুন এবং [docs/api.md](../../../docs/api.md) আপডেট করুন।

## লাইসেন্স

কপিরাইট (C) 2026 Thomas Vincent। GNU General Public License, সংস্করণ ২ বা তার পরবর্তী সংস্করণের অধীনে প্রকাশিত। বিস্তারিত জানতে [LICENSE](../../../LICENSE) দেখুন।
