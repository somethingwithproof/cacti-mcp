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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · **Українська** · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP це Python-адаптер, який надає можливості
[плагіна Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) як інструменти MCP
через stdio. Плагін уже обслуговує MCP безпосередньо через HTTP, тому використовуйте
цей варіант, якщо ваш клієнт може підключатися до віддаленого сервера. Цей адаптер призначений для
клієнтів, які підтримують лише stdio. Він використовує офіційний Python MCP SDK і
перетворює виклики інструментів на запити до HTTPS API плагіна (контракт можливостей v2, що
обслуговується за шляхами `/v1/`, лише з bearer-токеном).
Автентифікацію, авторизацію, валідацію та виконання забезпечує Cacti.

**Статус: у розробці, до версії 1.0.** Версія 0.1.0 підтримує отримання переліку пристроїв у режимі лише для читання
та версій інсталяції через супутній
[плагін Cacti MCP](https://github.com/somethingwithproof/plugin_mcp).
Тегованого релізу ще немає. Діагностика та виправлення (doctor) заплановані на майбутнє.

## Що він надає

| Операція | Інструмент MCP, що надається плагіном Cacti MCP |
|---|---|
| Перелік пристроїв, які може бачити власник токена | `cacti-list-devices` |
| Читання даних одного дозволеного пристрою | `cacti-get-device` |
| Читання версій Cacti, плагіна та API | `cacti-get-system-info` |

Назви, описи та схеми вхідних даних надходять із відфільтрованої за правами доступу
відповіді виявлення (discovery) від Cacti. Додаткові дозволені провайдери в режимі лише для читання можуть виявлятися
без додавання обробників інструментів на Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Сценарії використання

Підключіть клієнт MCP, щоб отримати список пристроїв Cacti, доступних для його виділеного користувача,
переглянути один дозволений пристрій або отримати версії інсталяції, якщо користувач
має необхідний адміністративний дозвіл (realm). Назви та схеми вхідних даних надходять із
відповіді виявлення плагіна, тому адаптер не дублює кожного провайдера.
Дивіться [правила реєстрації можливостей](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
плагіна, щоб дізнатися про модель реєстрації та поточні обмеження.

## Карта коду та тестів

| Поведінка | Реалізація | Тестове покриття в цьому репозиторії |
|---|---|---|
| Валідація HTTPS, обмеження, автентифікація лише за bearer-токеном і пагінація v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Виявлення MCP, виклики та зміни прав доступу | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Довідка командного рядка, версія та відсутня конфігурація | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Тест підпроцесу використовує справжні клієнт і сервер SDK із фікстурною кінцевою точкою HTTP.
Він не вимагає та не замінює інтеграційну перевірку з реальним екземпляром Cacti.

## Як забезпечується безпека

- Використовує офіційний [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  для ініціалізації, виявлення інструментів, викликів і кадрування stdio.
- Надає лише можливості, анотації яких є строго лише для читання, недеструктивними та ідемпотентними. Схеми та назви
  надходять із Cacti; адаптер не містить SQL, облікових даних пристроїв чи команд відновлення.
- Надсилає лише bearer-токен: жодних файлів cookie, жодного кроку CSRF. Плагін повторно перевіряє
  дійсність токена та права доступу при кожному запиті.
- Використовує перевірений HTTPS, ніколи не зберігає cookie, відхиляє перенаправлення та
  ігнорує змінні середовища проксі. HTTP потребує `--allow-loopback-http`
  і буквальної loopback-адреси або `localhost`.
- Обмежує виклики API до 35 секунд загалом, 5 секунд на з'єднання, 30 секунд
  мережевої неактивності та приблизно 1 МБ на відповідь (1 100 000 байтів).
  Тіла запитів обмежено 16 384 байтами. Виклики виконуються послідовно в межах кожної
  сесії клієнта.
- Перевіряє аргументи інструменту за схемою вхідних даних з останнього виявлення перед
  надсиланням і виконує лише ідентифікатори з цього перевіреного каталогу. Невідповідність або
  некоректна схема від сервера повертається як помилка інструменту, а не аварійне завершення.
- Не повторює виконання автоматично. Помилки інструментів містять лише статус
  HTTP, `status` за AIP-193 та `reason` з ErrorInfo; ніколи не передають текст
  повідомлень сервера, тіла відповідей або облікові дані. Stdout зарезервовано для повідомлень MCP.

Версію SDK зафіксовано у файлі `uv.lock` (`mcp>=2.3,<3` у `pyproject.toml`). Цей
адаптер використовує низькорівневий сервер версії 2.x із транспортом stdio; він не
реалізує віддалену кінцеву точку MCP HTTP, OAuth, ресурси,
промпти, підписки чи фонові завдання.

Дивіться [контракт API](../../../docs/api.md) та [план реалізації](../../../docs/plan.md).

## Встановлення та командний рядок

Потрібні Python 3.12 або новішої версії та [uv](https://docs.astral.sh/uv/).
Із локальної копії цього репозиторію:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Встановіть і ввімкніть PHP-плагін, надайте відповідний дозвіл (realm) виділеному користувачу Cacti
та створіть для цього користувача персональний токен доступу (формат `cmcp_pat_`, за яким
ідуть 64 шістнадцяткові цифри в нижньому регістрі) у консолі плагіна, на сторінці My MCP Tokens
або за допомогою команди `tokens.php`.
Наявні дозволи (realms) Cacti та права доступу користувача до пристроїв залишаються чинними.

Передавайте токен через менеджер секретів як змінну `CACTI_MCP_TOKEN`; ніколи не додавайте його
до системи контролю версій або аргументів командного рядка. Окремо вкажіть кінцеву точку. Це має бути
HTTPS URL, що закінчується на `/plugins/mcp/api.php`, без облікових даних, параметрів запиту або
фрагмента:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` задає кінцеву точку замість `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` дозволяє звичайний HTTP для `localhost`, `127.0.0.1` або `::1`
для локального тестування, `--lang LOCALE` перевизначає локалізацію повідомлень CLI, а
`--version` виводить версію. Без одночасної наявності кінцевої точки та `CACTI_MCP_TOKEN`
команда завершується з помилкою використання.

### Локалізація

Довідка CLI та повідомлення про помилки адаптера постачаються 45 мовами (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) без жодних додаткових залежностей. Визначення
локалі перевіряє `--lang`, далі `LC_ALL`, `LC_MESSAGES` і `LANG`, із переходом
до `en` за замовчуванням (`C`/`POSIX` та невідомі теги також зводяться до `en`). Назви інструментів MCP,
схеми та успішні JSON-відповіді інструментів залишаються незмінними; повідомлення про помилки
адаптера, повернуті з `is_error=True`, відповідають активній локалі.

Процес очікує повідомлень MCP через stdin. Зазвичай його запускає клієнт MCP.
Для клієнтів, які підтримують поширений формат конфігурації `mcpServers`:

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

Налаштуйте клієнт так, щоб він передавав `CACTI_MCP_ENDPOINT` і `CACTI_MCP_TOKEN` до
підпроцесу через змінні середовища або систему керування секретами. Успадкування середовища
залежить від клієнта. Прапорця командного рядка для токена немає.

Окремо встановлюваний дистрибутив Python надає консольну команду `cacti-mcp`.
Для запуску з локальної копії публікація в PyPI не потрібна. PHP-плагін не
залежить від Python.

## Релізи

Версія дистрибутива вказана у [pyproject.toml](../../../pyproject.toml).
Доки не з'являться теговані релізи, використовуйте локальну копію вихідного коду або
артефакт `python-distributions` з успішного
[запуску CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
Артефакт містить wheel-пакет і архів вихідного коду. Встановлений пакет надає
як команду `cacti-mcp`, так і `python -m cacti_mcp`; він не містить
PHP-плагін.

## Розробка та тести

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Тести охоплюють валідацію HTTP, ізоляцію облікових даних, запити лише з bearer-токеном,
пагінацію, приховування конфіденційних даних у помилках і реальний обмін повідомленнями між клієнтом і сервером SDK
у підпроцесі з фікстурним HTTP-сервером. Вони не потребують робочої інсталяції Cacti.

Репозиторій використовує `src/cacti_mcp/`, pytest, Ruff, uv та Hatchling. CI тестує
Python 3.12, 3.13 та 3.14. Окреме завдання пакування збирає wheel
і архів вихідного коду, встановлює wheel поза локальною копією репозиторію та виконує димове тестування
обох точок входу. Дистрибутиви та результати тестів зберігаються як артефакти робочого процесу.

## Участь у розробці

Pull-запити надсилайте в гілку `develop`. Зберігайте сумісність адаптера з Python 3.12,
дотримуйтеся наявної конфігурації Ruff і структури пакета `src/cacti_mcp/`, а також
залишайте stdout зарезервованим для повідомлень MCP. Додавайте тести для зміненої поведінки транспорту або
інструментів, запускайте наведені вище перевірки та підписуйте коміти за допомогою `git commit -s`.
Узгоджуйте зміни API із плагіном Cacti MCP та оновлюйте [docs/api.md](../../../docs/api.md).

## Ліцензія

Copyright (C) 2026 Thomas Vincent. Випущено під ліцензією GNU General Public
License версії 2 або пізнішої. Дивіться [LICENSE](../../../LICENSE).
