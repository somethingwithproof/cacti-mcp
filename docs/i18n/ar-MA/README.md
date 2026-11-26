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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · **العربية (المغرب)** · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP هو adapter ديال Python كيبين القدرات ديال
[إضافة Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) كأدوات MCP
عبر stdio. الإضافة ديجا كتقدم MCP عبر HTTP مباشرة، يعني استعملها
فاش الكليان ديالك يقدر يتكونيكطا مع سيرفر بعيد. هاد الـ adapter مخصص
للكليانات اللي كيهضرو غير بـ stdio. كيستعمل الـ SDK الرسمي ديال MCP لـ Python
وكيحول استدعاءات الأدوات لـ API ديال HTTPS الخاص بالإضافة (عقد القدرات v2، كيتقدم
تحت مسارات `/v1/`، بـ bearer token غير بوحدو).
Cacti هو اللي كيتكلف بالمصادقة، الصلاحيات، التحقق، والتنفيذ.

**الحالة: باقي فالتطوير، قبل 1.0.** النسخة 0.1.0 كتدعم جرد الأجهزة للقراءة فقط
وإصدارات التثبيت عن طريق
[إضافة Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) المرافقة.
مازال ما كاينش شي إصدار معلم بـ tag لحد الآن. تشخيصات Doctor والإصلاحات غتكون فخدمة جاية من بعد.

## شنو كيوفر

| العملية | أداة MCP اللي كتقدمها إضافة Cacti MCP |
|---|---|
| عرض لائحة الأجهزة اللي يقدر مول التوكن يشوفها | `cacti-list-devices` |
| قراءة جهاز واحد مسموح به | `cacti-get-device` |
| قراءة إصدارات Cacti والإضافة والـ API | `cacti-get-system-info` |

السميات، الأوصاف، وschemas ديال المدخلات كيجيو من رد الاستكشاف المفلتر على حساب الصلاحيات
فـ Cacti. يمكن اكتشاف مزودين إضافيين للقراءة فقط ومسموح بهم
بلا ما نزيدو معالجات أدوات جديدة بـ Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## حالات الاستعمال

ربط شي كليان MCP باش تليستي الأجهزة ديال Cacti اللي يقدر المستخدم المخصص ديالو يشوفها،
تقلب على جهاز واحد مسموح به، ولا تجيب إصدارات التثبيت فاش يكون المستخدم
عندو الصلاحية الإدارية المطلوبة. السميات وschemas ديال المدخلات كيجيو من
رد الاستكشاف ديال الإضافة، يعني الـ adapter ما كيعاودش يكرر كل مزود.
شوف [قواعد تسجيل القدرات](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
ديال الإضافة باش تعرف نموذج التسجيل والحدود الحالية.

## خريطة الكود والاختبارات

| السلوك | التنفيذ | أدلة الاختبار فهاد المستودع |
|---|---|---|
| التحقق من HTTPS، الحدود، المصادقة بـ bearer فقط، والترقيم v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| استكشاف MCP، الاستدعاءات، وتغييرات الصلاحيات | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| مساعدة سطر الأوامر، الإصدار، والإعدادات اللي ناقصة | [server.py](../../../src/cacti_mcp/server.py)، [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

اختبار الـ subprocess كيستعمل كليان وسيرفر حقيقيين من الـ SDK مع نقطة نهاية HTTP
تجريبية (fixture). ما كيحتاجش وما كيعوضش اختبار التكامل المباشر مع Cacti حي.

## كيفاش كيبقى آمن

- كيستعمل [Python SDK الرسمي ديال `mcp`](https://github.com/modelcontextprotocol/python-sdk)
  للتهيئة، استكشاف الأدوات، الاستدعاءات، وتأطير stdio.
- كيبين غير القدرات اللي التوصيفات ديالها مضبوطة بالضبط للقراءة فقط، غير مدمرة، ومحايدة للتكرار (idempotent). الـ schemas والسميات كيجيو
  من Cacti؛ الـ adapter ما فيه لا SQL، لا بيانات دخول للأجهزة، ولا أوامر إصلاح.
- كيصيفط غير الـ bearer token بوحدو: بلا كوكيز، وبلا مرحلة CSRF. الإضافة كتعاود تتحقق
  من صلاحية التوكن والأذونات فكل طلب.
- كيستعمل HTTPS متحقق منه، عمرو ما كيخزن الكوكيز، كيرفض إعادة التوجيه (redirects)،
  وكيتجاهل متغيرات البيئة ديال البروكسي. HTTP كيحتاج `--allow-loopback-http`
  وعنوان loopback حرفي ولا `localhost`.
- كيحدد استدعاءات الـ API فـ 35 ثانية إجمالا، 5 ثواني للاتصال، 30 ثانية ديال
  عدم نشاط الشبكة، وتقريبا 1 MB لكل رد (1,100,000 بايت).
  حجم جسم الطلب محدود فـ 16,384 بايت. الاستدعاءات كيتنفذو بالترتيب واحد مورا واحد
  لكل جلسة كليان.
- كيتحقق من وسائط الأداة مقابل schema ديال المدخلات من آخر استكشاف قبل ما
  يصيفطها، وكينفذ غير المعرفات اللي كاينة فداك الكاطالوغ المتحقق منه. أي عدم تطابق،
  ولا schema خاسرة من السيرفر، كيرجع كخطأ أداة وماشي كـ crash.
- ما كيعاودش المحاولة ديال التنفيذ أوتوماتيكيا. أخطاء الأدوات كتحمل غير حالة HTTP،
  و`status` ديال AIP-193، و`reason` ديال ErrorInfo؛ عمرو ما كيكون فيها نص
  رسالة السيرفر، ولا جسم الرد، ولا بيانات الدخول. Stdout محجوز غير لرسائل MCP.

نسخة الـ SDK متبتة بـ `uv.lock` (`mcp>=2.3,<3` فـ `pyproject.toml`). هاد
الـ adapter كيستعمل السيرفر منخفض المستوى 2.x ديالو مع نقل stdio؛ ما كينفذش
نقطة نهاية MCP HTTP بعيدة، ولا OAuth، ولا resources،
ولا prompts، ولا اشتراكات، ولا مهام فالخلفية.

شوف [عقد الـ API](../../../docs/api.md) و[خطة التنفيذ](../../../docs/plan.md).

## التثبيت وسطر الأوامر

كيحتاج Python 3.12 ولا فوق و[uv](https://docs.astral.sh/uv/).
من نسخة محلية ديال هاد المستودع:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

تبت وفعل إضافة PHP، عطي الصلاحية (realm) ديالها لمستخدم Cacti مخصص،
وصاوب personal access token لداك المستخدم (بالصيغة `cmcp_pat_` متبوعة
بـ 64 رقم سداسي عشري صغير) فلوحة التحكم ديال الإضافة، فصفحة My MCP Tokens ديالها،
ولا بأمر `tokens.php` ديالها.
صلاحيات Cacti وأذونات الأجهزة اللي ديجا عند المستخدم كيبقاو خدامين.

عطي التوكن عبر مدير الأسرار ديالك كمتغير `CACTI_MCP_TOKEN`؛ عمرك ما تزيدو
فـ source control ولا فوسائط الأوامر. حدد نقطة النهاية بوحدها. خاصها تكون
رابط HTTPS كيسالي بـ `/plugins/mcp/api.php`، بلا بيانات دخول، ولا query،
ولا fragment:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` كيحدد نقطة النهاية فبلاصة `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` كيسمح بـ HTTP عادي لـ `localhost`، ولا `127.0.0.1`، ولا `::1`
للتجريب المحلي، و`--lang LOCALE` كيبدل لغة رسائل سطر الأوامر،
و`--version` كيفيشي الإصدار. بلا ما يكونو بجوج نقطة النهاية و`CACTI_MCP_TOKEN`،
الأمر كيخرج بخطأ استعمال.

### التوطين واللغات

مساعدة سطر الأوامر ورسائل الأخطاء ديال الـ adapter كيجيو بـ 45 لغة محلية (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) بلا حتى شي اعتماديات إضافية. اختيار اللغة
كيقلب أولاً فـ `--lang`، من بعد فـ `LC_ALL`، و`LC_MESSAGES`، و`LANG`، وكيرجع
لـ `en` إلا ما لقاش (`C`/`POSIX` والوسوم اللي ما معروفاش حتى هما كيرجعو لـ `en`). سميات أدوات MCP،
والـ schemas، وحمولات JSON الناجحة ديال الأدوات ما كيتبدلوش؛ رسائل الأخطاء ديال الـ adapter
اللي كيرجعو مع `is_error=True` كيتبعو اللغة اللي خدامة.

العملية كتسنى رسائل MCP فـ stdin. فالعادة كليان MCP هو اللي كيلونسيها.
بالنسبة للكليانات اللي كتقبل صيغة الإعدادات المعروفة `mcpServers`:

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

ريكل الكليان باش يدوز `CACTI_MCP_ENDPOINT` و`CACTI_MCP_TOKEN` للـ
subprocess عبر البيئة ديالو ولا أداة الأسرار ديالو. وراثة متغيرات البيئة
كتعتمد على الكليان. ما كاينش شي flag فسطر الأوامر ديال التوكن.

توزيعة Python اللي كتثبت بوحدها كتوفر أمر الكونسول `cacti-mcp`.
ما كيحتاجش النشر على PyPI باش تخدم النسخة المحلية. إضافة PHP ما عندها
حتى شي اعتماد على Python.

## الإصدارات

إصدار التوزيعة مسجل فـ [pyproject.toml](../../../pyproject.toml).
حتى يوجدو إصدارات معلمة بـ tags، استعمل نسخة مصدرية محلية ولا
أرتيفاكت `python-distributions` من شي
[تشغيل CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) ناجح.
الأرتيفاكت فيه wheel وأرشيف مصدري. الحزمة المثبتة كتوفر
بجوج أمر `cacti-mcp` و`python -m cacti_mcp`؛ وما فيهاش
إضافة PHP.

## التطوير والاختبارات

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

الاختبارات كتغطي التحقق من HTTP، عزل بيانات الدخول، الطلبات بـ bearer فقط،
الترقيم، إخفاء الأخطاء الحساسة، وتبادل subprocess حقيقي بين كليان وسيرفر من الـ SDK قدام
سيرفر HTTP تجريبي (fixture). ما كيحتاجوش تثبيت حي ديال Cacti.

المستودع كيستعمل `src/cacti_mcp/`، وpytest، وRuff، وuv، وHatchling. الـ CI كيتستي
Python 3.12، و3.13، و3.14. مهمة تحزيم مستقلة كتبني الـ wheel
والأرشيف المصدري، كتثبت الـ wheel برا النسخة المحلية، وكتدير اختبار دخاني (smoke-test)
لنقط الدخول بجوج. التوزيعات ونتائج الاختبارات كيتحفظو كأرتيفاكتات ديال الـ workflow.

## المساهمة

طلبات الدمج (Pull requests) كيمشيو لـ `develop`. خلي الـ adapter متوافق مع Python 3.12،
تبع إعدادات Ruff اللي كاينة وهيكلة الحزمة `src/cacti_mcp/`،
وخلي stdout محجوز لرسائل MCP. زيد اختبارات لأي تغيير فالنقل ولا فسلوك
الأدوات، دوز الفحوصات اللي الفوق، ووقع الـ commits بـ `git commit -s`.
نسق تغييرات الـ API مع إضافة Cacti MCP وحدث [docs/api.md](../../../docs/api.md).

## الرخصة

حقوق النشر (C) 2026 Thomas Vincent. منشور تحت رخصة GNU General Public
License، الإصدار 2 ولا أحدث. شوف [LICENSE](../../../LICENSE).
