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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · **العربية** · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP هو محوّل مكتوب بلغة Python يتيح قدرات [إضافة Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) كأدوات MCP عبر الدخل والخرج القياسي (stdio). توفّر الإضافة بالفعل خادم MCP عبر HTTP مباشرة، لذا استخدم هذا الخيار عندما يتمكن عميلك من الاتصال بخادم بعيد. أما هذا المحوّل فهو مخصص للعملاء الذين يدعمون stdio فقط. يعتمد المحوّل على حزمة تطوير MCP الرسمية للغة Python، ويحوّل استدعاءات الأدوات إلى واجهة برمجة التطبيقات عبر HTTPS الخاصة بالإضافة (عقد القدرات الإصدار 2، ويُقدَّم تحت مسارات `/v1/` باستخدام رمز bearer token فقط). تتولى Cacti عمليات المصادقة والتخويل والتحقق والتنفيذ.

**الحالة: قيد التطوير، قبل الإصدار 1.0.** يدعم الإصدار 0.1.0 جرد الأجهزة للقراءة فقط وإصدارات التثبيت من خلال [إضافة Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) المرافقة. لا يوجد إصدار موسوم (tagged release) حتى الآن. وتشخيصات Doctor والإصلاحات هي أعمال مستقبلية.

## ما يوفّره

| العملية | أداة MCP التي توفّرها إضافة Cacti MCP |
|---|---|
| سرد الأجهزة التي يحق لمالك الرمز رؤيتها | `cacti-list-devices` |
| قراءة جهاز واحد مصرح به | `cacti-get-device` |
| قراءة إصدارات Cacti والإضافة وواجهة برمجة التطبيقات | `cacti-get-system-info` |

تأتي الأسماء والأوصاف ومخططات الإدخال من استجابة الاكتشاف المُرشَّحة حسب الصلاحيات في Cacti. ويمكن اكتشاف مزودي القراءة فقط الإضافيين المصرح بهم دون الحاجة إلى إضافة معالجات أدوات جديدة بلغة Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## حالات الاستخدام

اربط عميل MCP لسرد أجهزة Cacti التي يحق للمستخدم المخصص له رؤيتها، أو البحث عن جهاز واحد مصرح به، أو استرداد إصدارات التثبيت عندما يمتلك المستخدم النطاق الإداري (realm) المطلوب. تأتي الأسماء ومخططات الإدخال من استجابة الاكتشاف الخاصة بالإضافة، لذلك لا يكرر المحوّل تعريف كل مزوّد. راجع [قواعد تسجيل القدرات](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) الخاصة بالإضافة للاطلاع على نموذج التسجيل والحدود الحالية.

## خريطة الشيفرة والاختبارات

| السلوك | التنفيذ | أدلة الاختبار في هذا المستودع |
|---|---|---|
| التحقق من HTTPS، والحدود، والمصادقة بالرمز الحامل فقط، وتصفح الصفحات v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| اكتشاف MCP، والاستدعاءات، وتغييرات الصلاحيات | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| مساعدة سطر الأوامر، والإصدار، والإعدادات المفقودة | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

يستخدم اختبار العملية الفرعية عميلاً وخادماً فعليين من حزمة SDK مع نقطة نهاية HTTP تجريبية (fixture). وهو لا يتطلب فحص تكامل حياً مع Cacti ولا يغني عنه.

## كيف يحافظ على الأمان

- يستخدم حزمة [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) الرسمية للتهيئة واكتشاف الأدوات والاستدعاءات وتأطير stdio.
- يعرض فقط القدرات التي تكون تعليقاتها التوضيحية للقراءة فقط، وغير تدميرية، ومتكررة النتائج بشكل مطابق (idempotent). تأتي المخططات والأسماء من Cacti؛ ولا يحتوي المحوّل على استعلامات SQL أو بيانات اعتماد أجهزة أو أوامر إصلاح.
- يرسل رمز bearer token فقط: دون ملفات تعريف ارتباط (cookies) ودون خطوة CSRF. تعيد الإضافة التحقق من صلاحية الرمز والأذونات في كل طلب.
- يستخدم HTTPS مُتحقَّقاً منه، ولا يخزن ملفات تعريف الارتباط أبداً، ويرفض إعادة التوجيه، ويتجاهل متغيرات بيئة الوكيل (proxy). يتطلب استخدام HTTP تمرير `--allow-loopback-http` وعنوان استرجاع حلقي (loopback) حرفياً أو `localhost`.
- يقيّد استدعاءات واجهة برمجة التطبيقات بـ 35 ثانية إجمالاً، و5 ثوانٍ للاتصال، و30 ثانية من خمول الشبكة، وحوالي 1 ميجابايت لكل استجابة (1,100,000 بايت). وتقتصر أجسام الطلبات على 16,384 بايت. كما تُنفَّذ الاستدعاءات تسلسلياً لكل جلسة عميل.
- يتحقق من وسائط الأداة مقابل مخطط الإدخال من آخر عملية اكتشاف قبل إرسالها، وينفذ فقط المعرّفات الواردة في ذلك الفهرس المُتحقَّق منه. أي عدم تطابق، أو مخطط غير سليم من الخادم، يعود كخطأ أداة لا كانهيار.
- لا يعيد محاولة التنفيذ تلقائياً. تحمل أخطاء الأدوات فقط حالة HTTP، وحالة AIP-193 (`status`)، وسبب ErrorInfo (`reason`)؛ ولا تحمل أبداً نص رسالة الخادم أو أجسام الاستجابة أو بيانات الاعتماد. كما أن الخرج القياسي (stdout) مخصص لرسائل MCP.

إصدار حزمة SDK مثبّت في `uv.lock` (`mcp>=2.3,<3` في `pyproject.toml`). يستخدم هذا المحوّل خادمها منخفض المستوى للإصدار 2.x مع نقل stdio؛ وهو لا ينفذ نقطة نهاية MCP HTTP بعيدة، أو OAuth، أو الموارد (resources)، أو المطالبات (prompts)، أو الاشتراكات، أو مهام الخلفية.

راجع [عقد واجهة برمجة التطبيقات](../../../docs/api.md) و[خطة التنفيذ](../../../docs/plan.md).

## التثبيت وسطر الأوامر

يتطلب Python 3.12 أو أحدث وأداة [uv](https://docs.astral.sh/uv/). انطلاقاً من نسخة محلية لهذا المستودع:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

ثبّت إضافة PHP وفعّلها، وامنح نطاقها (realm) لمستخدم Cacti مخصص، وأنشئ رمز وصول شخصي لذلك المستخدم (بصيغة `cmcp_pat_` متبوعاً بـ 64 رقماً سداسياً عشرياً بأحرف صغيرة) من وحدة تحكم الإضافة، أو من صفحة My MCP Tokens، أو باستخدام أمر `tokens.php`. وتظل نطاقات Cacti الحالية وأذونات الأجهزة الخاصة بالمستخدم سارية.

زوّد الرمز عبر مدير الأسرار الخاص بك باسم `CACTI_MCP_TOKEN`؛ ولا تضفه أبداً إلى نظام التحكم بالمصادر أو وسائط الأوامر. حدد نقطة النهاية بشكل منفصل. يجب أن تكون عنوان URL بصيغة HTTPS ينتهي بـ `/plugins/mcp/api.php`، دون بيانات اعتماد أو سلسلة استعلام (query) أو جزء تجزئة (fragment):

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

يحدد الخيار `--endpoint URL` نقطة النهاية بدلاً من `CACTI_MCP_ENDPOINT`. ويسمح `--allow-loopback-http` باستخدام HTTP العادي مع `localhost` أو `127.0.0.1` أو `::1` للاختبار المحلي، كما يتجاوز `--lang LOCALE` توطين رسائل سطر الأوامر، ويطبع `--version` رقم الإصدار. ودون توفر كل من نقطة النهاية و`CACTI_MCP_TOKEN`، ينهي الأمر تنفيذه بخطأ في الاستخدام.

### التوطين

تتوفّر مساعدة سطر الأوامر ورسائل خطأ المحوّل بـ 45 لغة محلية (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) دون أي اعتماديات إضافية. يتحقق تحديد اللغة المحلية من `--lang`، ثم `LC_ALL` و`LC_MESSAGES` و`LANG`، مع الرجوع إلى `en` (كما تُحلّ `C`/`POSIX` والوسوم غير المعروفة إلى `en`). لا تتأثر أسماء أدوات MCP والمخططات وحمولات JSON الناجحة للأدوات؛ بينما تتبع رسائل خطأ المحوّل المُرجعة مع `is_error=True` اللغة المحلية النشطة.

تنتظر العملية رسائل MCP على الدخل القياسي (stdin)، وعادةً ما يشغّلها عميل MCP. وبالنسبة للعملاء الذين يقبلون صيغة الإعداد الشائعة `mcpServers`:

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

اضبط العميل لتمرير `CACTI_MCP_ENDPOINT` و`CACTI_MCP_TOKEN` إلى العملية الفرعية عبر بيئته أو أداة إدارة الأسرار لديه. يعتمد وراثة البيئة على العميل نفسه. ولا يوجد خيار سطر أوامر لتمرير الرمز.

توفّر حزمة Python القابلة للتثبيت بشكل منفصل أمر الطرفية `cacti-mcp`. لا يلزم النشر على PyPI لتشغيل النسخة المستنسخة. ولا تعتمد إضافة PHP على Python.

## الإصدارات

إصدار الحزمة مسجّل في [pyproject.toml](../../../pyproject.toml). وإلى أن تتوفر إصدارات موسومة، استخدم نسخة مصدرية أو حزمة `python-distributions` من [تشغيل CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) ناجح. تحتوي الحزمة على ملف wheel وأرشيف مصدري. وتوفّر الحزمة المثبتة كلاً من الأمر `cacti-mcp` و`python -m cacti_mcp`؛ ولا تحتوي على إضافة PHP.

## التطوير والاختبارات

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

تغطي الاختبارات التحقق من HTTP، وعزل بيانات الاعتماد، والطلبات المعتمدة على الرمز الحامل فقط، وتصفح الصفحات، وتنقيح الأخطاء، وتبادلاً فعلياً بين عميل وخادم SDK عبر عملية فرعية أمام خادم HTTP تجريبي. ولا تتطلب وجود تثبيت حي لـ Cacti.

يستخدم المستودع `src/cacti_mcp/` وpytest وRuff وuv وHatchling. وتختبر بيئة CI إصدارات Python 3.12 و3.13 و3.14. كما تبني مهمة تحزيم منفصلة ملف wheel والأرشيف المصدري، وتثبّت ملف wheel خارج نسخة المستودع، وتجري اختبار تشغيل أولي (smoke-test) لكلتا نقطتي الدخول. وتُعد التوزيعات ونتائج الاختبارات مخرجات لسير العمل (workflow artifacts).

## المساهمة

تُوجَّه طلبات السحب (Pull requests) إلى الفرع `develop`. حافظ على توافق المحوّل مع Python 3.12، واتبع إعدادات Ruff الحالية وبنية الحزمة `src/cacti_mcp/`، وأبقِ stdout مخصصاً لرسائل MCP. أضف اختبارات عند تغيير سلوك النقل أو الأدوات، وشغّل الفحوصات المذكورة أعلاه، ووقّع الالتزامات باستخدام `git commit -s`. نسّق تغييرات واجهة برمجة التطبيقات مع إضافة Cacti MCP وحدّث [docs/api.md](../../../docs/api.md).

## الترخيص

حقوق النشر (C) 2026 Thomas Vincent. منشور بموجب رخصة GNU العمومية العامة، الإصدار 2 أو ما بعده. راجع [LICENSE](../../../LICENSE).
