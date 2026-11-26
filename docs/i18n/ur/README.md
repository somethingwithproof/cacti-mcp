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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · **اردو** · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP ایک Python اڈاپٹر ہے جو [Cacti MCP پلگ ان](https://github.com/somethingwithproof/plugin_mcp) کی صلاحیتوں کو stdio پر بطور MCP ٹولز پیش کرتا ہے۔ یہ پلگ ان پہلے ہی براہِ راست HTTP پر MCP فراہم کرتا ہے، اس لیے جب آپ کا کلائنٹ کسی ریموٹ سرور سے جڑ سکے تو اسی کا استعمال کریں۔ یہ اڈاپٹر ان کلائنٹس کے لیے ہے جو صرف stdio استعمال کرتے ہیں۔ یہ آفیشل Python MCP SDK کا استعمال کرتا ہے اور ٹول کالز کو پلگ ان کے HTTPS API (صلاحیتوں کا معاہدہ v2، جو `/v1/` راستوں کے تحت صرف bearer ٹوکن کے ذریعے فراہم کیا جاتا ہے) میں ترجمہ کرتا ہے۔
توثیق (authentication)، اجازت نامہ (authorization)، توثیق کاری (validation)، اور عمل درآمد Cacti کے پاس ہے۔

**حالت: زیرِ تعمیر، 1.0 سے پہلے۔** ورژن 0.1.0 ساتھی [Cacti MCP پلگ ان](https://github.com/somethingwithproof/plugin_mcp) کے ذریعے صرف پڑھنے کے لیے (read-only) ڈیوائس انوینٹری اور انسٹالیشن ورژنز کی سہولت فراہم کرتا ہے۔
ابھی تک کوئی ٹیگ شدہ ریلیز موجود نہیں ہے۔ Doctor تشخیص اور مرمت مستقبل کے کام میں شامل ہیں۔

## یہ کیا فراہم کرتا ہے

| آپریشن | Cacti MCP پلگ ان کی طرف سے فراہم کردہ MCP ٹول |
|---|---|
| ٹوکن کا مالک جن ڈیوائسز کو دیکھ سکتا ہے ان کی فہرست بنائیں | `cacti-list-devices` |
| ایک مجاز ڈیوائس پڑھیں | `cacti-get-device` |
| Cacti، پلگ ان، اور API ورژنز پڑھیں | `cacti-get-system-info` |

نام، تفصیلات، اور ان پٹ اسکیماز Cacti کے اجازتوں کے لحاظ سے فلٹر کردہ ڈسکوری جواب سے آتے ہیں۔ مزید مجاز صرف پڑھنے کے قابل فراہم کنندگان (read-only providers) کو Python ٹول ہینڈلرز شامل کیے بغیر دریافت کیا جا سکتا ہے۔

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## استعمال کی صورتیں

ایک MCP کلائنٹ کو جوڑیں تاکہ وہ ان Cacti ڈیوائسز کی فہرست بنا سکے جو اس کا مخصوص صارف دیکھ سکتا ہے، ایک مجاز ڈیوائس تلاش کر سکے، یا جب صارف کے پاس مطلوبہ انتظامی دائرہ (administrative realm) ہو تو انسٹالیشن ورژنز حاصل کر سکے۔ نام اور ان پٹ اسکیماز پلگ ان کے ڈسکوری جواب سے آتے ہیں، اس لیے اڈاپٹر ہر فراہم کنندہ کو دوہراتا نہیں ہے۔
رجسٹریشن ماڈل اور موجودہ حدود کے لیے پلگ ان کے [صلاحیت رجسٹریشن قواعد](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) دیکھیں۔

## کوڈ اور ٹیسٹ کا نقشہ

| رویہ | نفاذ | اس ریپوزٹری میں ٹیسٹ شواہد |
|---|---|---|
| HTTPS توثیق، حدود، صرف bearer توثیق، اور v2 پیجنگ | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP ڈسکوری، کالز، اور اجازتوں میں تبدیلیاں | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| کمانڈ لائن مدد، ورژن، اور گمشدہ کنفیگریشن | [server.py](../../../src/cacti_mcp/server.py)، [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

سب پراسس ٹیسٹ ایک فکسچر HTTP اینڈ پوائنٹ کے ساتھ حقیقی SDK کلائنٹ اور سرور استعمال کرتا ہے۔ اسے لائیو Cacti انٹیگریشن چیک کی ضرورت نہیں ہے اور نہ ہی یہ اس کا متبادل ہے۔

## یہ محفوظ کیسے رہتا ہے

- آغاز، ٹول ڈسکوری، کالز، اور stdio فریمنگ کے لیے آفیشل [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) استعمال کرتا ہے۔
- صرف ان صلاحیتوں کو پیش کرتا ہے جن کی تشریحات (annotations) بالکل صرف پڑھنے کے قابل (read-only)، غیر تباہ کن (non-destructive)، اور idempotent ہوں۔ اسکیماز اور نام Cacti سے آتے ہیں؛ اڈاپٹر میں کوئی SQL، ڈیوائس کی اسناد (credentials)، یا مرمت کی کمانڈز موجود نہیں ہیں۔
- صرف bearer ٹوکن بھیجتا ہے: کوئی کوکیز نہیں، کوئی CSRF مرحلہ نہیں۔ پلگ ان ہر درخواست پر ٹوکن کی موزونیت اور اجازتوں کی دوبارہ جانچ کرتا ہے۔
- تصدیق شدہ HTTPS استعمال کرتا ہے، کبھی کوکیز محفوظ نہیں کرتا، ری ڈائریکٹس سے انکار کرتا ہے، اور پراکسی ماحولیاتی متغیرات (environment variables) کو نظر انداز کرتا ہے۔ HTTP کے لیے `--allow-loopback-http` اور ایک لفظی loopback پتہ یا `localhost` درکار ہوتا ہے۔
- API کالز کو مجموعی طور پر 35 سیکنڈ، کنیکٹ ہونے کے لیے 5 سیکنڈ، نیٹ ورک کی غیر فعالیت کے 30 سیکنڈ، اور فی جواب تقریباً 1 MB (1,100,000 بائٹس) تک محدود رکھتا ہے۔
  درخواست کی باڈیز 16,384 بائٹس تک محدود ہیں۔ کالز کو فی کلائنٹ سیشن ترتیب وار (serialized) چلایا جاتا ہے۔
- ٹول کے دلائل (arguments) کو بھیجنے سے پہلے آخری ڈسکوری کے ان پٹ اسکیما کے مطابق چیک کرتا ہے، اور صرف اسی تصدیق شدہ کیٹلاگ سے ids چلاتا ہے۔ کوئی عدم مطابقت، یا سرور کی طرف سے خراب اسکیما، کریش کے بجائے ٹول ایرر کے طور پر واپس آتا ہے۔
- عمل درآمد کی خودکار دوبارہ کوشش (retry) نہیں کرتا۔ ٹول کی غلطیاں صرف HTTP اسٹیٹس، AIP-193 `status`، اور ErrorInfo `reason` لے کر آتی ہیں؛ سرور کا پیغام کا متن، جوابی باڈیز، یا اسناد کبھی شامل نہیں ہوتیں۔ Stdout صرف MCP پیغامات کے لیے مختص ہے۔

SDK کا ورژن `uv.lock` کے ذریعے مقرر کیا گیا ہے (`pyproject.toml` میں `mcp>=2.3,<3`)۔ یہ اڈاپٹر stdio ٹرانسپورٹ کے ساتھ اپنا 2.x لو لیول سرور استعمال کرتا ہے؛ یہ کوئی ریموٹ MCP HTTP اینڈ پوائنٹ، OAuth، وسائل (resources)، پرامپٹس (prompts)، سبسکرپشنز، یا پس منظر کے کام (background tasks) نافذ نہیں کرتا۔

[API معاہدہ](../../../docs/api.md) اور [نفاذ کا منصوبہ](../../../docs/plan.md) دیکھیں۔

## تنصیب اور کمانڈ لائن

اس کے لیے Python 3.12 یا اس سے جدید ورژن اور [uv](https://docs.astral.sh/uv/) درکار ہیں۔
اس ریپوزٹری کے چیک آؤٹ سے:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

PHP پلگ ان انسٹال اور فعال کریں، اس کا دائرہ (realm) ایک مخصوص Cacti صارف کو تفویض کریں، اور اس صارف کے لیے پلگ ان کے کنسول، اس کے My MCP Tokens صفحے پر، یا اس کی `tokens.php` کمانڈ کے ذریعے ذاتی رسائی ٹوکن (فارمیٹ `cmcp_pat_` کے بعد 64 چھوٹے حروف والے hex ہندسے) بنائیں۔
صارف کے موجودہ Cacti دائرے اور ڈیوائس کی اجازتیں بدستور لاگو رہیں گی۔

ٹوکن کو اپنے سیکرٹ مینیجر کے ذریعے بطور `CACTI_MCP_TOKEN` فراہم کریں؛ اسے کبھی سورس کنٹرول یا کمانڈ کے دلائل میں شامل نہ کریں۔ اینڈ پوائنٹ کو الگ سے سیٹ کریں۔ یہ ایک HTTPS URL ہونا چاہیے جو `/plugins/mcp/api.php` پر ختم ہو، اور اس میں کوئی اسناد، query، یا fragment نہ ہو:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL`، `CACTI_MCP_ENDPOINT` کے بجائے اینڈ پوائنٹ سیٹ کرتا ہے۔
`--allow-loopback-http` مقامی ٹیسٹنگ کے لیے `localhost`، `127.0.0.1`، یا `::1` پر سادہ HTTP کی اجازت دیتا ہے، `--lang LOCALE` کمانڈ لائن (CLI) پیغامات کی لوکلائزیشن کو اوور رائیڈ کرتا ہے، اور `--version` ورژن پرنٹ کرتا ہے۔ اینڈ پوائنٹ اور `CACTI_MCP_TOKEN` دونوں کے بغیر، کمانڈ استعمال کی خرابی (usage error) کے ساتھ بند ہو جاتی ہے۔

### لوکلائزیشن

CLI مدد اور اڈاپٹر کے ایرر پیغامات بغیر کسی اضافی انحصار (dependencies) کے 45 لوکیلز (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) میں دستیاب ہیں۔ لوکیل کی شناخت پہلے `--lang`، پھر `LC_ALL`، `LC_MESSAGES`، اور `LANG` کو چیک کرتی ہے، اور آخر میں `en` پر واپس آتی ہے (`C`/`POSIX` اور نامعلوم ٹیگز بھی `en` پر حل ہوتے ہیں)۔ MCP ٹول کے نام، اسکیماز، اور کامیاب JSON ٹول پے لوڈز متاثر نہیں ہوتے؛ `is_error=True` کے ساتھ واپس آنے والے اڈاپٹر کے ایرر پیغامات فعال لوکیل کی پیروی کرتے ہیں۔

پراسس stdin پر MCP پیغامات کا انتظار کرتا ہے۔ عام طور پر ایک MCP کلائنٹ اسے لانچ کرتا ہے۔
ان کلائنٹس کے لیے جو عام `mcpServers` کنفیگریشن فارمیٹ قبول کرتے ہیں:

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

کلائنٹ کو کنفیگر کریں کہ وہ `CACTI_MCP_ENDPOINT` اور `CACTI_MCP_TOKEN` کو اپنے ماحول (environment) یا سیکرٹ سہولت کے ذریعے سب پراسس کو پاس کرے۔ ماحول کی وراثت (inheritance) کلائنٹ پر منحصر ہے۔ ٹوکن کے لیے کوئی کمانڈ لائن فلیگ موجود نہیں ہے۔

الگ سے انسٹال کی جانے والی Python ڈسٹری بیوشن `cacti-mcp` کنسول کمانڈ فراہم کرتی ہے۔ چیک آؤٹ کو چلانے کے لیے PyPI پر اشاعت کی ضرورت نہیں ہے۔ PHP پلگ ان کا Python پر کوئی انحصار نہیں ہے۔

## ریلیزز

ڈسٹری بیوشن ورژن [pyproject.toml](../../../pyproject.toml) میں درج ہے۔
جب تک ٹیگ شدہ ریلیزز دستیاب نہ ہوں، سورس چیک آؤٹ یا کسی کامیاب [CI رن](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) سے `python-distributions` آرٹیفیکٹ استعمال کریں۔
آرٹیفیکٹ میں ایک wheel اور سورس آرکائیو شامل ہے۔ انسٹال کردہ پیکیج `cacti-mcp` کمانڈ اور `python -m cacti_mcp` دونوں فراہم کرتا ہے؛ اس میں PHP پلگ ان شامل نہیں ہے۔

## ترقی اور ٹیسٹس

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

ٹیسٹس HTTP کی توثیق، اسناد کی تنہائی (credential isolation)، صرف bearer درخواستوں، پیجنگ، ایرر کی رازداری (redaction)، اور ایک فکسچر HTTP سرور کے خلاف حقیقی SDK کلائنٹ/سرور سب پراسس تبادلے کا احاطہ کرتے ہیں۔ انہیں لائیو Cacti انسٹالیشن کی ضرورت نہیں ہے۔

ریپوزٹری `src/cacti_mcp/`، pytest، Ruff، uv، اور Hatchling استعمال کرتی ہے۔ CI Python 3.12، 3.13، اور 3.14 کی جانچ کرتا ہے۔ ایک الگ پیکیجنگ جاب wheel اور سورس آرکائیو بناتا ہے، چیک آؤٹ سے باہر wheel انسٹال کرتا ہے، اور دونوں اینٹری پوائنٹس کا اسموک ٹیسٹ کرتا ہے۔ ڈسٹری بیوشنز اور ٹیسٹ کے نتائج ورک فلو آرٹیفیکٹس ہیں۔

## تعاون

Pull requests کو `develop` برانچ پر بھیجیں۔ اڈاپٹر کو Python 3.12 کے ساتھ ہم آہنگ رکھیں، موجودہ Ruff کنفیگریشن اور `src/cacti_mcp/` پیکیج لے آؤٹ کی پیروی کریں، اور stdout کو MCP پیغامات کے لیے مختص رکھیں۔ تبدیل شدہ ٹرانسپورٹ یا ٹول کے رویے کے لیے ٹیسٹس شامل کریں، اوپر دی گئی جانچیں چلائیں، اور کمٹس پر `git commit -s` کے ساتھ دستخط کریں۔
API کی تبدیلیوں کو Cacti MCP پلگ ان کے ساتھ مربوط کریں اور [docs/api.md](../../../docs/api.md) کو اپ ڈیٹ کریں۔

## لائسنس

کاپی رائٹ (C) 2026 Thomas Vincent۔ GNU General Public License، ورژن 2 یا اس کے بعد کے ورژن کے تحت جاری کردہ۔ [LICENSE](../../../LICENSE) دیکھیں۔
