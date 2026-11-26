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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · **العربية (مصر)** · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP ده محول (adapter) مكتوب بـ Python بيعرض قدرات [إضافة Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) كأدوات MCP عن طريق stdio. الإضافة نفسها بتقدم MCP على HTTP مباشرة، فالأفضل تستخدم ده لو العميل بتاعك يقدر يتصل بسيرفر بعيد. المحول ده معمول للعملاء اللي بيتكلموا stdio بس. بيستخدم الـ Python MCP SDK الرسمي وبيحول استدعاءات الأدوات لطلبات على الـ HTTPS API بتاع الإضافة (عقد القدرات v2، شغال تحت مسارات `/v1/`، بـ bearer token بس). Cacti هو اللي مسؤول عن التحقق من الهوية، الصلاحيات، الفحص، والتنفيذ.

**الحالة: لسه تحت التطوير، قبل إصدار 1.0.** الإصدار 0.1.0 بيدعم جرد الأجهزة للقراءة بس ومعرفة إصدارات التثبيت عن طريق [إضافة Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) المصاحبة ليه. مفيش إصدار رسمي متعلم بـ tag لحد دلوقتي. فحوصات التشخيص (Doctor diagnostics) والإصلاحات لسه شغل مستقبلي.

## إيه اللي بيعرضه

| العملية | أداة MCP اللي بتوفرها إضافة Cacti MCP |
|---|---|
| عرض قايمة الأجهزة اللي صاحب التوكن مسموح له يشوفها | `cacti-list-devices` |
| قراءة بيانات جهاز واحد مسموح بيه | `cacti-get-device` |
| قراءة إصدارات Cacti والإضافة والـ API | `cacti-get-system-info` |

الأسماء والأوصاف ومخططات الإدخال (input schemas) بتيجي من استجابة الاكتشاف المتفلترة حسب الصلاحيات من Cacti. وممكن اكتشاف مزودين إضافيين للقراءة بس ومسموح بيهم من غير ما تحتاج تضيف معالجات أدوات جديدة في Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## حالات الاستخدام

اربط عميل MCP عشان تعرض أجهزة Cacti اللي المستخدم المخصص ليه مسموح له يشوفها، أو تدور على جهاز واحد مسموح بيه، أو تجيب إصدارات التثبيت لما المستخدم يكون معاه الصلاحية الإدارية المطلوبة (realm). الأسماء ومخططات الإدخال بتيجي من استجابة الاكتشاف بتاعة الإضافة، فالمحول مش بيكرر تعريف كل مزود. شوف [قواعد تسجيل القدرات](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors) الخاصة بالإضافة عشان تعرف نموذج التسجيل والحدود الحالية.

## خريطة الكود والاختبارات

| السلوك | التنفيذ | دليل الاختبار في المستودع ده |
|---|---|---|
| التحقق من HTTPS، الحدود، المصادقة بـ bearer بس، وترقيم صفحات v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| اكتشاف MCP، الاستدعاءات، وتغييرات الصلاحيات | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| مساعدة سطر الأوامر، الإصدار، والإعدادات الناقصة | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

اختبار العملية الفرعية (subprocess) بيستخدم عميل وسيرفر حقيقيين من الـ SDK مع نقطة نهاية HTTP تجريبية (fixture). الاختبار ده مش محتاج Cacti شغال فعلياً ومش بديل لاختبار التكامل المباشر مع Cacti.

## إزاي بيحافظ على الأمان

- بيستخدم [حزمة `mcp` الرسمية لـ Python](https://github.com/modelcontextprotocol/python-sdk) في التهيئة، اكتشاف الأدوات، الاستدعاءات، وتأطير stdio.
- بيعرض بس القدرات اللي توصيفاتها (annotations) بالظبط للقراءة فقط، غير مدمرة (non-destructive)، ومتكافئة عند التكرار (idempotent). المخططات والأسماء بتيجي من Cacti؛ المحول مفيهوش أي SQL أو بيانات دخول أجهزة أو أوامر إصلاح.
- بيبعت الـ bearer token بس: مفيش كوكيز، ومفيش خطوة CSRF. الإضافة بتتأكد تاني من صلاحية التوكن والأذونات مع كل طلب.
- بيستخدم HTTPS متحقق منه، عمره ما بيخزن كوكيز، بيرفض عمليات إعادة التوجيه (redirects)، وبيتجاهل متغيرات بيئة البروكسي. استخدام HTTP محتاج `--allow-loopback-http` وعنوان loopback حرفي أو `localhost`.
- بيحط حدود لطلبات الـ API: 35 ثانية إجمالاً، 5 ثواني للاتصال، 30 ثانية لخمول الشبكة، وحوالي 1 ميجابايت لكل استجابة (1,100,000 بايت). حجم جسم الطلب محدود بـ 16,384 بايت. والطلبات بتتنفذ بالتتابع لكل جلسة عميل.
- بيراجع معاملات الأداة قدام مخطط الإدخال من آخر عملية اكتشاف قبل ما يبعتها، وبينفذ بس المعرفات (ids) اللي موجودة في الكتالوج المتحقق منه ده. أي عدم تطابق، أو مخطط غير سليم جاي من السيرفر، بيرجع كخطأ أداة مش كـ crash.
- مش بيعيد محاولة التنفيذ تلقائياً. أخطاء الأدوات بتشيل بس كود حالة HTTP، و`status` بتاع AIP-193، و`reason` بتاع ErrorInfo؛ عمرها ما بتشيل نص رسالة السيرفر أو جسم الاستجابة أو بيانات الدخول. والـ stdout محجوز لرسائل MCP بس.

إصدار الـ SDK متثبت في `uv.lock` (`mcp>=2.3,<3` في `pyproject.toml`). المحول ده بيستخدم السيرفر منخفض المستوى من إصدار 2.x مع نقل stdio؛ مش بينفذ نقطة نهاية MCP HTTP بعيدة، ولا OAuth، ولا resources، ولا prompts، ولا subscriptions، ولا مهام خلفية.

شوف [عقد الـ API](../../../docs/api.md) و[خطة التنفيذ](../../../docs/plan.md).

## التثبيت وسطر الأوامر

محتاج Python 3.12 أو أحدث و[uv](https://docs.astral.sh/uv/).
من نسخة محلية (checkout) من المستودع ده:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

ثبت وفعل إضافة PHP، وادي الصلاحية (realm) بتاعتها لمستخدم Cacti مخصص، واعمل personal access token للمستخدم ده (بالصيغة `cmcp_pat_` وبعدها 64 رقم سداسي عشري بحروف صغيرة) من لوحة تحكم الإضافة، أو من صفحة My MCP Tokens، أو باستخدام أمر `tokens.php`.
صلاحيات Cacti وأذونات الأجهزة الحالية بتاعة المستخدم بتفضل سارية زي ما هي.

مرر التوكن عن طريق مدير الأسرار بتاعك في `CACTI_MCP_TOKEN`؛ إوعى تحطه في الـ source control أو في معاملات سطر الأوامر. واضبط نقطة النهاية لوحدها. لازم تكون رابط HTTPS بينتهي بـ `/plugins/mcp/api.php`، من غير بيانات دخول أو query أو fragment:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` بيحدد نقطة النهاية بدل `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` بيسمح بـ HTTP عادي لـ `localhost` أو `127.0.0.1` أو `::1` للاختبار المحلي، و`--lang LOCALE` بيغير لغة رسائل سطر الأوامر، و`--version` بيطبع الإصدار. لو نقطة النهاية و`CACTI_MCP_TOKEN` الاتنين مش موجودين، الأمر بيخرج بخطأ استخدام.

### الترجمة واللغات (Localization)

مساعدة سطر الأوامر ورسائل خطأ المحول بتيجي بـ 45 لغة ومحلية (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) من غير أي اعتماديات إضافية. تحديد اللغة بيدور الأول في `--lang`، بعد كده `LC_ALL` و`LC_MESSAGES` و`LANG`، وبيرجع لـ `en` لو مفيش (`C`/`POSIX` والرموز غير المعروفة بترجع برضه لـ `en`). أسماء أدوات MCP ومخططاتها وبيانات JSON الناجحة اللي بترجعها الأدوات مش بتتأثر؛ رسائل خطأ المحول اللي بترجع مع `is_error=True` بتمشي على اللغة النشطة.

العملية بتستنى رسائل MCP على stdin. عادةً عميل MCP هو اللي بيشغلها.
للعملاء اللي بيقبلوا صيغة الإعداد المشهورة `mcpServers`:

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

اضبط العميل إنه يبعت `CACTI_MCP_ENDPOINT` و`CACTI_MCP_TOKEN` للعملية الفرعية عن طريق متغيرات البيئة أو أداة إدارة الأسرار بتاعته. وراثة متغيرات البيئة بتعتمد على العميل نفسه. مفيش خيار (flag) في سطر الأوامر للتوكن.

حزمة Python اللي بتتثبت لوحدها بتوفر أمر الكونسول `cacti-mcp`. مش محتاج نشر على PyPI عشان تشغل النسخة المحلية. وإضافة PHP ملهاش أي اعتمادية على Python.

## الإصدارات

إصدار التوزيعة متسجل في [pyproject.toml](../../../pyproject.toml).
لحد ما تنزل إصدارات متعلمة بـ tag، استخدم نسخة من الكود المصدري أو الـ artifact اللي اسمه `python-distributions` من [تشغيل CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) ناجح.
الـ artifact فيه ملف wheel وأرشيف الكود المصدري. الحزمة المثبتة بتوفر الأمرين `cacti-mcp` و`python -m cacti_mcp`؛ ومفيهاش إضافة PHP.

## التطوير والاختبارات

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

الاختبارات بتغطي التحقق من HTTP، عزل بيانات الدخول، طلبات bearer بس، ترقيم الصفحات، إخفاء تفاصيل الأخطاء، وتبادل فعلي بين عميل وسيرفر SDK كعملية فرعية قدام سيرفر HTTP تجريبي. مش محتاجين تثبيت Cacti فعلي.

المستودع بيستخدم `src/cacti_mcp/` وpytest وRuff وuv وHatchling. الـ CI بيختبر على Python 3.12 و3.13 و3.14. وفي مهمة تجميع (packaging job) منفصلة بتبني الـ wheel وأرشيف المصدر، وبتثبت الـ wheel بره مجلد الكود، وبتعمل اختبار سريع (smoke test) لنقطتين الدخول. التوزيعات ونتائج الاختبارات بتطلع كـ workflow artifacts.

## المساهمة

طلبات الدمج (Pull requests) بتروح على فرع `develop`. خلي المحول متوافق مع Python 3.12، وامشي على إعدادات Ruff الموجودة وتنظيم حزمة `src/cacti_mcp/`، وخلي stdout محجوز لرسائل MCP بس. ضيف اختبارات لأي تغيير في النقل أو سلوك الأدوات، شغل الفحوصات اللي فوق، ووقع الـ commits باستخدام `git commit -s`.
نسق تغييرات الـ API مع إضافة Cacti MCP وحدث [docs/api.md](../../../docs/api.md).

## الرخصة

حقوق النشر (C) 2026 Thomas Vincent. منشور تحت رخصة GNU General Public License، الإصدار 2 أو أحدث. شوف [LICENSE](../../../LICENSE).
