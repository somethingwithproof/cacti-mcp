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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · **עברית** · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP הוא מתאם Python החושף את היכולות של
[תוסף Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) ככלי MCP
מעל stdio. התוסף כבר מגיש MCP ישירות מעל HTTP, לכן השתמשו בכך כשהלקוח שלכם יכול
להתחבר לשרת מרוחק. מתאם זה מיועד ללקוחות המדברים stdio בלבד. הוא משתמש
ב-Python MCP SDK הרשמי ומתרגם קריאות כלים ל-API של התוסף מעל HTTPS (חוזה יכולות v2,
המוגש תחת נתיבי `/v1/`, עם bearer token בלבד).
Cacti אחראית על אימות, הרשאות, ולידציה וביצוע.

**סטטוס: בפיתוח, לפני 1.0.** גרסה 0.1.0 תומכת במלאי מכשירים לקריאה בלבד
ובגרסאות התקנה דרך [תוסף Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) הנלווה.
אין עדיין גרסה מתויגת. אבחון Doctor ותיקונים הם עבודה עתידית.

## מה המתאם חושף

| פעולה | כלי MCP המסופק על ידי תוסף Cacti MCP |
|---|---|
| הצגת המכשירים שבעל האסימון מורשה לראות | `cacti-list-devices` |
| קריאת מכשיר מורשה אחד | `cacti-get-device` |
| קריאת גרסאות Cacti, התוסף וה-API | `cacti-get-system-info` |

שמות, תיאורים וסכמות קלט מגיעים מתגובת הגילוי המסוננת לפי הרשאות של Cacti.
ניתן לגלות ספקי קריאה בלבד מורשים נוספים מבלי להוסיף מטפלי כלים ב-Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## מקרי שימוש

חברו לקוח MCP כדי להציג את מכשירי ה-Cacti שהמשתמש הייעודי שלו מורשה לראות,
לאתר מכשיר מורשה אחד, או לשלוף גרסאות התקנה כאשר למשתמש יש את תחום הניהול
הנדרש (administrative realm). השמות וסכמות הקלט מגיעים מתגובת הגילוי של התוסף,
כך שהמתאם אינו משכפל כל ספק בנפרד.
ראו את
[כללי רישום היכולות](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
של התוסף עבור מודל הרישום והמגבלות הנוכחיות.

## מיפוי קוד ובדיקות

| התנהגות | מימוש | ראיות בדיקה במאגר זה |
|---|---|---|
| ולידציית HTTPS, גבולות, אימות bearer בלבד ועימוד v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| גילוי MCP, קריאות ושינויי הרשאות | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| עזרה בשורת הפקודה, גרסה ותצורה חסרה | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

בדיקת תת-התהליך משתמשת בלקוח ובשרת SDK אמיתיים מול נקודת קצה מדומה (fixture) של HTTP.
היא אינה דורשת או מחליפה בדיקת אינטגרציה מול מערכת Cacti חיה.

## כיצד נשמרת הבטיחות

- שימוש ב-[`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) הרשמי
  לאתחול, גילוי כלים, קריאות ומסגור (framing) של stdio.
- חשיפה אך ורק של יכולות שההערות (annotations) שלהן הן בדיוק לקריאה בלבד, לא הרסניות
  ואידמפוטנטיות. הסכמות והשמות מגיעים מ-Cacti; המתאם אינו מכיל SQL, פרטי גישה
  של מכשירים או פקודות תיקון.
- שליחת ה-bearer token בלבד: ללא קובצי cookie וללא שלב CSRF. התוסף בודק מחדש
  את תוקף האסימון וההרשאות בכל בקשה.
- שימוש ב-HTTPS מאומת, ללא שמירת קובצי cookie, סירוב להפניות מחדש (redirects),
  והתעלמות ממשתני סביבה של פרוקסי. HTTP רגיל מחייב `--allow-loopback-http`
  וכתובת loopback מילולית או `localhost`.
- הגבלת קריאות API ל-35 שניות בסך הכול, 5 שניות לחיבור, 30 שניות של חוסר פעילות
  ברשת, וכ-1 MB לתגובה (1,100,000 בתים). גוף הבקשה מוגבל ל-16,384 בתים. קריאות
  מבוצעות בטור (serialized) עבור כל סשן לקוח.
- בדיקת ארגומנטי הכלי מול סכמת הקלט מהגילוי האחרון לפני השליחה, והרצה אך ורק
  של מזהים מתוך הקטלוג המאומת. אי-התאמה, או סכמה פגומה מהשרת, חוזרות כשגיאת כלי,
  לא כקריסה.
- ללא ניסיון חוזר אוטומטי לביצוע. שגיאות כלי נושאות רק את קוד ה-HTTP,
  ה-`status` לפי AIP-193 וה-`reason` של ErrorInfo; לעולם לא טקסט הודעה מהשרת,
  גופי תגובה או פרטי גישה. Stdout שמור להודעות MCP.

גרסת ה-SDK מקובעת ב-`uv.lock` (`mcp>=2.3,<3` ב-`pyproject.toml`). מתאם זה
משתמש בשרת ברמה הנמוכה (low-level server) של גרסה 2.x עם תעבורת stdio; הוא אינו
מממש נקודת קצה מרוחקת של MCP מעל HTTP, OAuth, משאבים (resources), הנחיות (prompts),
מנויים (subscriptions) או משימות רקע.

ראו את [חוזה ה-API](../../../docs/api.md) ואת [תוכנית המימוש](../../../docs/plan.md).

## התקנה ושורת הפקודה

נדרש Python 3.12 ומעלה ו-[uv](https://docs.astral.sh/uv/).
מתוך עותק מקומי של מאגר זה:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

התקינו והפעילו את תוסף ה-PHP, העניקו את ה-realm שלו למשתמש Cacti ייעודי,
וצרו עבורו אסימון גישה אישי (בפורמט `cmcp_pat_` ואחריו 64 ספרות הקסדצימליות
באותיות קטנות) במסוף התוסף, בדף My MCP Tokens שלו, או באמצעות הפקודה `tokens.php`.
תחום ההרשאות (realms) והרשאות המכשירים הקיימות של המשתמש ב-Cacti עדיין חלים.

ספקו את האסימון דרך מנהל הסודות שלכם כ-`CACTI_MCP_TOKEN`; לעולם אל תוסיפו אותו
לבקרת התצורה או לארגומנטים של הפקודה. הגדירו את נקודת הקצה בנפרד. עליה להיות
כתובת HTTPS המסתיימת ב-`/plugins/mcp/api.php`, ללא פרטי גישה, פרמטרי שאילתה או
מקטע (fragment):

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` מגדיר את נקודת הקצה במקום `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` מתיר HTTP רגיל אל `localhost`, `127.0.0.1`, או `::1`
לצורך בדיקות מקומיות, `--lang LOCALE` עוקף את לוקליזציית הודעות ה-CLI, ו-
`--version` מדפיס את הגרסה. ללא שניהם (נקודת הקצה ו-`CACTI_MCP_TOKEN`),
הפקודה יוצאת עם שגיאת שימוש.

### לוקליזציה

עזרת ה-CLI והודעות השגיאה של המתאם מסופקות ב-45 לוקאלים (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) ללא תלויות נוספות.
זיהוי הלוקאל בודק את `--lang`, לאחר מכן `LC_ALL`, `LC_MESSAGES`, ו-`LANG`, וחוזר
לברירת המחדל `en` (`C`/`POSIX` ותגים לא מוכרים נפתרים גם הם ל-`en`). שמות כלי ה-MCP,
הסכמות ומטעני ה-JSON של כלים מוצלחים אינם מושפעים; הודעות שגיאה של המתאם
המוחזרות עם `is_error=True` פועלות לפי הלוקאל הפעיל.

התהליך ממתין להודעות MCP ב-stdin. בדרך כלל לקוח MCP מפעיל אותו.
עבור לקוחות המקבלים את פורמט התצורה הנפוץ `mcpServers`:

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

הגדירו את הלקוח כך שיעביר את `CACTI_MCP_ENDPOINT` ואת `CACTI_MCP_TOKEN` לתת-התהליך
דרך הסביבה או מנגנון הסודות שלו. ירושת משתני הסביבה תלויה בלקוח. אין דגל שורת פקודה
עבור האסימון.

חבילת ה-Python הניתנת להתקנה בנפרד מספקת את פקודת המסוף `cacti-mcp`.
אין צורך בפרסום ב-PyPI כדי להריץ מתוך עותק המקור. לתוסף ה-PHP אין תלות ב-Python.

## גרסאות ושחרורים

גרסת ההפצה מתועדת ב-[pyproject.toml](../../../pyproject.toml).
עד שיהיו זמינות גרסאות מתויגות, השתמשו בעותק מקור או בארטיפקט
`python-distributions` מתוך
[הרצת CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) מוצלחת.
הארטיפקט מכיל wheel וארכיון מקור. החבילה המותקנת מספקת הן את הפקודה `cacti-mcp`
והן את `python -m cacti_mcp`; היא אינה מכילה את תוסף ה-PHP.

## פיתוח ובדיקות

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

הבדיקות מכסות ולידציית HTTP, בידוד פרטי גישה, בקשות bearer בלבד,
עימוד, הסתרת פרטי שגיאות (redaction) והחלפת הודעות אמיתית בתת-תהליך בין לקוח ושרת SDK
מול שרת HTTP מדומה. הן אינן דורשות התקנת Cacti חיה.

המאגר משתמש ב-`src/cacti_mcp/`, pytest, Ruff, uv, ו-Hatchling. ה-CI בודק את
Python 3.12, 3.13, ו-3.14. משימת אריזה נפרדת בונה את ה-wheel ואת ארכיון המקור,
מתקינה את ה-wheel מחוץ לתיקיית הקוד, ומבצעת בדיקת עשן לשתי נקודות הכניסה.
ההפצות ותוצאות הבדיקות הן ארטיפקטים של ה-workflow.

## תרומה לפרויקט

בקשות מיזוג (Pull requests) נשלחות לענף `develop`. שמרו על תאימות המתאם ל-Python 3.12,
פעלו לפי תצורת Ruff הקיימת ומבנה החבילה `src/cacti_mcp/`, ושמרו על stdout מוקצה
להודעות MCP בלבד. הוסיפו בדיקות עבור שינויים בהתנהגות התעבורה או הכלים, הריצו
את הבדיקות שלמעלה, וחתמו על commits באמצעות `git commit -s`.
תאמו שינויי API עם תוסף Cacti MCP ועדכנו את [docs/api.md](../../../docs/api.md).

## רישיון

זכויות יוצרים (C) 2026 Thomas Vincent. משוחרר תחת הרישיון GNU General Public License,
גרסה 2 ומעלה. ראו [LICENSE](../../../LICENSE).
