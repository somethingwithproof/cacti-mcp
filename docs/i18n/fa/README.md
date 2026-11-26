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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · **فارسی** · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP یک آداپتور پایتونی است که قابلیت‌های
[افزونه Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) را به‌صورت ابزارهای MCP
روی stdio ارائه می‌دهد. خود افزونه به‌طور مستقیم MCP را روی HTTP سرو می‌کند، بنابراین اگر
کلاینت شما می‌تواند به سرور راه‌دور متصل شود، از همان روش استفاده کنید. این آداپتور برای
کلاینت‌هایی است که فقط با stdio کار می‌کنند. این ابزار از SDK رسمی پایتون MCP استفاده می‌کند و
فراخوانی ابزارها را به API مبتنی بر HTTPS افزونه (قرارداد قابلیت‌های نسخه ۲، ارائه‌شده
در مسیرهای `/v1/`، صرفاً با bearer token) ترجمه می‌کند.
Cacti مسئول احراز هویت، مجوزدهی، اعتبارسنجی و اجرا است.

**وضعیت: در حال توسعه، پیش از نسخه 1.0.** نسخه 0.1.0 از فهرست دستگاه‌های فقط‌خواندنی و
نسخه‌های نصب‌شده از طریق [افزونه Cacti MCP](https://github.com/somethingwithproof/plugin_mcp)
همراه خود پشتیبانی می‌کند. هنوز هیچ نسخه تگ‌شده‌ای منتشر نشده است. عیب‌یابی Doctor و تعمیرها
در برنامه‌های آینده قرار دارند.

## چه قابلیت‌هایی ارائه می‌دهد

| عملیات | ابزار MCP ارائه‌شده توسط افزونه Cacti MCP |
|---|---|
| فهرست کردن دستگاه‌هایی که مالک توکن مجاز به دیدن آن‌هاست | `cacti-list-devices` |
| خواندن یک دستگاه مجاز | `cacti-get-device` |
| خواندن نسخه‌های Cacti، افزونه و API | `cacti-get-system-info` |

نام‌ها، توضیحات و طرح‌واره‌های ورودی از پاسخ کشف فیلترشده بر اساس مجوزهای Cacti دریافت می‌شوند.
ارائه‌دهندگان فقط‌خواندنی مجاز دیگر را می‌توان بدون افزودن هندلرهای پایتونی جدید کشف کرد.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## موارد استفاده

یک کلاینت MCP را متصل کنید تا دستگاه‌های Cacti قابل مشاهده برای کاربر اختصاصی آن را فهرست کند،
اطلاعات یک دستگاه مجاز را جست‌وجو کند، یا در صورت داشتن realm مدیریتی مورد نیاز، نسخه‌های
نصب‌شده را بازیابی کند. نام‌ها و طرح‌واره‌های ورودی از پاسخ کشف افزونه می‌آیند، بنابراین آداپتور
هر ارائه‌دهنده را تکرار نمی‌کند. برای آشنایی با مدل ثبت و محدودیت‌های فعلی،
[قوانین ثبت قابلیت](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
افزونه را ببینید.

## نقشه کد و آزمون‌ها

| رفتار | پیاده‌سازی | شواهد آزمون در این مخزن |
|---|---|---|
| اعتبارسنجی HTTPS، کران‌ها، احراز هویت فقط با bearer و صفحه‌بندی نسخه ۲ | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| کشف MCP، فراخوانی‌ها و تغییرات مجوز | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| راهنمای خط فرمان، نسخه و پیکربندی ناموجود | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

آزمون زیرفرآیند از یک کلاینت و سرور واقعی SDK همراه با یک نقطه پایانی HTTP آزمایشی (fixture)
استفاده می‌کند. این آزمون نیازی به یکپارچه‌سازی زنده با Cacti ندارد و جایگزین آن نیز نمی‌شود.

## نحوه حفظ امنیت

- برای مقداردهی اولیه، کشف ابزارها، فراخوانی‌ها و فریم‌بندی stdio از [SDK رسمی پایتون `mcp`](https://github.com/modelcontextprotocol/python-sdk) استفاده می‌کند.
- فقط قابلیت‌هایی را ارائه می‌دهد که حاشیه‌نویسی آن‌ها دقیقاً فقط‌خواندنی، غیرمخرب و هم‌توان (idempotent) باشد. طرح‌واره‌ها و نام‌ها از Cacti دریافت می‌شوند؛ آداپتور فاقد هرگونه SQL، اطلاعات ورود دستگاه یا دستور تعمیر است.
- فقط bearer token را ارسال می‌کند: بدون کوکی و بدون مرحله CSRF. افزونه اعتبار توکن و مجوزها را در هر درخواست دوباره بررسی می‌کند.
- از HTTPS تاییدشده استفاده می‌کند، هرگز کوکی ذخیره نمی‌کند، ریدایرکت‌ها را رد می‌کند و متغیرهای محیطی پروکسی را نادیده می‌گیرد. استفاده از HTTP ساده نیازمند `--allow-loopback-http` و یک نشانی loopback دقیق یا `localhost` است.
- فراخوانی‌های API را در کل به ۳۵ ثانیه، اتصال را به ۵ ثانیه، بی‌فعالی شبکه را به ۳۰ ثانیه و هر پاسخ را تقریباً به ۱ مگابایت (۱٬۱۰۰٬۰۰۰ بایت) محدود می‌کند. بدنه درخواست‌ها به ۱۶٬۳۸۴ بایت محدود است. فراخوانی‌ها به ازای هر نشست کلاینت به‌صورت متوالی (سریال) انجام می‌شوند.
- آرگومان‌های ابزار را پیش از ارسال با طرح‌واره ورودی آخرین کشف تطبیق می‌دهد و فقط شناسه‌های موجود در همان فهرست تاییدشده را اجرا می‌کند. عدم تطابق یا طرح‌واره معیوب از سمت سرور، به‌صورت خطای ابزار برگردانده می‌شود و باعث کرش نمی‌شود.
- اجرا را به‌صورت خودکار تکرار نمی‌کند. خطاهای ابزار فقط شامل وضعیت HTTP، مقدار `status` در AIP-193 و مقدار `reason` در ErrorInfo هستند؛ هرگز متن پیام سرور، بدنه پاسخ یا اطلاعات احراز هویت را شامل نمی‌شوند. Stdout به پیام‌های MCP اختصاص دارد.

نسخه SDK در `uv.lock` تثبیت شده است (`mcp>=2.3,<3` در `pyproject.toml`). این آداپتور از
سرور سطح پایین نسخه 2.x آن با انتقال stdio استفاده می‌کند؛ نقطه پایانی HTTP راه‌دور MCP،
OAuth، منابع (resources)، پرامپت‌ها، اشتراک‌ها یا کارهای پس‌زمینه را پیاده‌سازی نمی‌کند.

[قرارداد API](../../../docs/api.md) و [برنامه پیاده‌سازی](../../../docs/plan.md) را ببینید.

## نصب و خط فرمان

به Python 3.12 یا بالاتر و [uv](https://docs.astral.sh/uv/) نیاز دارد.
از درون یک نسخه کلون‌شده این مخزن:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

افزونه PHP را نصب و فعال کنید، realm آن را به یک کاربر اختصاصی Cacti بدهید و یک توکن دسترسی
شخصی برای آن کاربر (با قالب `cmcp_pat_` و به دنبال آن ۶۴ رقم هگزادسیمال با حروف کوچک) در کنسول
افزونه، در صفحه My MCP Tokens یا با دستور `tokens.php` بسازید.
realmهای فعلی Cacti و مجوزهای دستگاه کاربر همچنان اعمال می‌شوند.

توکن را از طریق مدیر محرمانه‌های خود به‌عنوان `CACTI_MCP_TOKEN` تامین کنید؛ هرگز آن را در کنترل
نسخه یا آرگومان‌های دستور قرار ندهید. نقطه پایانی را جداگانه تنظیم کنید. این نشانی باید یک URL
از نوع HTTPS باشد که به `/plugins/mcp/api.php` ختم شود و بدون اطلاعات احراز هویت، query یا fragment باشد:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

گزینه `--endpoint URL` نقطه پایانی را به‌جای `CACTI_MCP_ENDPOINT` تنظیم می‌کند.
`--allow-loopback-http` اجازه استفاده از HTTP ساده را برای `localhost`، `127.0.0.1` یا `::1`
در تست محلی می‌دهد، `--lang LOCALE` بومی‌سازی پیام‌های خط فرمان را بازنویسی می‌کند و
`--version` نسخه را چاپ می‌کند. بدون وجود هم‌زمان نقطه پایانی و `CACTI_MCP_TOKEN`، دستور با خطای
نحوه استفاده خارج می‌شود.

### بومی‌سازی

راهنمای خط فرمان و پیام‌های خطای آداپتور در ۴۵ زبان و منطقه (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) بدون هیچ وابستگی اضافه‌ای ارائه می‌شوند.
تشخیص زبان ابتدا `--lang` و سپس `LC_ALL`، `LC_MESSAGES` و `LANG` را بررسی می‌کند و در نهایت
به `en` بازمی‌گردد (`C`/`POSIX` و برچسب‌های ناشناخته نیز به `en` نگاشت می‌شوند). نام ابزارهای MCP،
طرح‌واره‌ها و خروجی‌های JSON موفق تغییر نمی‌کنند؛ پیام‌های خطای آداپتور که با `is_error=True`
برگردانده می‌شوند از زبان فعال پیروی می‌کنند.

فرآیند منتظر پیام‌های MCP روی stdin می‌ماند. معمولاً یک کلاینت MCP آن را اجرا می‌کند.
برای کلاینت‌هایی که قالب رایج پیکربندی `mcpServers` را می‌پذیرند:

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

کلاینت را طوری پیکربندی کنید که `CACTI_MCP_ENDPOINT` و `CACTI_MCP_TOKEN` را از طریق محیط یا
امکانات مدیریت محرمانه‌های خود به زیرفرآیند منتقل کند. به ارث بردن متغیرهای محیطی به کلاینت
بستگی دارد. هیچ پرچم خط فرمانی برای توکن وجود ندارد.

بسته توزیع پایتون قابل نصب جداگانه، دستور کنسولی `cacti-mcp` را فراهم می‌کند. برای اجرای کد
مخزن نیازی به انتشار در PyPI نیست. افزونه PHP هیچ وابستگی به پایتون ندارد.

## نسخه‌های منتشرشده

نسخه توزیع در [pyproject.toml](../../../pyproject.toml) ثبت شده است.
تا زمانی که نسخه‌های تگ‌شده در دسترس قرار بگیرند، از کد مخزن یا آرتیفکت `python-distributions`
از یک [اجرای CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml)
موفق استفاده کنید. این آرتیفکت شامل یک wheel و آرشیو سورس است. بسته نصب‌شده هر دو دستور
`cacti-mcp` و `python -m cacti_mcp` را فراهم می‌کند و شامل افزونه PHP نیست.

## توسعه و آزمون‌ها

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

آزمون‌ها اعتبارسنجی HTTP، جداسازی اطلاعات احراز هویت، درخواست‌های فقط با bearer، صفحه‌بندی،
حذف اطلاعات حساس از خطاها و یک تبادل واقعی زیرفرآیند کلاینت/سرور SDK را در برابر یک سرور HTTP
آزمایشی پوشش می‌دهند. این آزمون‌ها نیازی به نصب زنده Cacti ندارند.

این مخزن از `src/cacti_mcp/`، pytest، Ruff، uv و Hatchling استفاده می‌کند. CI نسخه‌های
Python 3.12، 3.13 و 3.14 را آزمایش می‌کند. یک کار بسته‌بندی جداگانه، wheel و آرشیو سورس را
می‌سازد، wheel را بیرون از مخزن نصب می‌کند و هر دو نقطه ورود را تست دود (smoke test) می‌کند.
بسته‌های توزیع و نتایج آزمون‌ها به‌عنوان آرتیفکت‌های گردش کار ذخیره می‌شوند.

## مشارکت

درخواست‌های Pull Request به شاخه `develop` ارسال می‌شوند. سازگاری آداپتور را با Python 3.12
حفظ کنید، از پیکربندی فعلی Ruff و ساختار بسته `src/cacti_mcp/` پیروی کنید و stdout را به پیام‌های
MCP اختصاص دهید. برای تغییرات رفتار انتقال یا ابزار، آزمون اضافه کنید، بررسی‌های بالا را اجرا
کنید و کامیت‌ها را با `git commit -s` امضا کنید. تغییرات API را با افزونه Cacti MCP هماهنگ کرده و
[docs/api.md](../../../docs/api.md) را به‌روزرسانی کنید.

## مجوز

حق نشر (C) 2026 توماس وینسنت. تحت مجوز GNU General Public License نسخه ۲ یا بالاتر منتشر
شده است. [LICENSE](../../../LICENSE) را ببینید.
