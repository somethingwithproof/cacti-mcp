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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · **ไทย** · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP เป็นอะแดปเตอร์ภาษา Python ที่เปิดใช้งานความสามารถของ
[ปลั๊กอิน Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) ในรูปแบบเครื่องมือ MCP
ผ่าน stdio ตัวปลั๊กอินให้บริการ MCP ผ่าน HTTP โดยตรงอยู่แล้ว ดังนั้นให้ใช้วิธีนั้นเมื่อไคลเอนต์ของคุณสามารถเชื่อมต่อกับเซิร์ฟเวอร์ระยะไกลได้ อะแดปเตอร์นี้มีไว้สำหรับไคลเอนต์ที่สื่อสารผ่าน stdio เท่านั้น โดยใช้ Python MCP SDK อย่างเป็นทางการ และแปลงการเรียกใช้เครื่องมือให้เป็น HTTPS API ของปลั๊กอิน (ข้อตกลงความสามารถ v2 ซึ่งให้บริการภายใต้พาธ `/v1/` และใช้ bearer token เท่านั้น)
Cacti เป็นผู้ดูแลการยืนยันตัวตน การให้สิทธิ์ การตรวจสอบความถูกต้อง และการประมวลผลทั้งหมด

**สถานะ: กำลังพัฒนา ยังไม่ถึงเวอร์ชัน 1.0** เวอร์ชัน 0.1.0 รองรับการดูรายการอุปกรณ์แบบอ่านอย่างเดียวและเวอร์ชันของการติดตั้งผ่าน
[ปลั๊กอิน Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) ที่ใช้งานร่วมกัน
ยังไม่มีรีลีสที่ติดแท็กอย่างเป็นทางการ ส่วนการวินิจฉัยปัญหาและระบบซ่อมแซม (Doctor) เป็นงานในอนาคต

## สิ่งที่เปิดให้ใช้งาน

| การดำเนินการ | เครื่องมือ MCP ที่ปลั๊กอิน Cacti MCP จัดเตรียมให้ |
|---|---|
| แสดงรายการอุปกรณ์ที่เจ้าของโทเคนมีสิทธิ์มองเห็น | `cacti-list-devices` |
| อ่านข้อมูลอุปกรณ์ที่ได้รับอนุญาตหนึ่งรายการ | `cacti-get-device` |
| อ่านเวอร์ชันของ Cacti, ปลั๊กอิน และ API | `cacti-get-system-info` |

ชื่อ คำอธิบาย และ input schema มาจากการตอบกลับการค้นพบ (discovery) ที่ผ่านการกรองสิทธิ์จาก Cacti แล้ว สามารถค้นพบผู้ให้บริการแบบอ่านอย่างเดียวเพิ่มเติมที่ได้รับอนุญาตได้โดยไม่ต้องเพิ่มตัวจัดการเครื่องมือใน Python

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## กรณีการใช้งาน

เชื่อมต่อไคลเอนต์ MCP เพื่อแสดงรายการอุปกรณ์ Cacti ที่ผู้ใช้เฉพาะกิจมีสิทธิ์มองเห็น ค้นหาข้อมูลอุปกรณ์ที่ได้รับอนุญาตหนึ่งรายการ หรือดึงข้อมูลเวอร์ชันการติดตั้งเมื่อผู้ใช้มี realm ระดับผู้ดูแลระบบที่กำหนด ชื่อและ input schema มาจากการตอบกลับการค้นพบของปลั๊กอิน ดังนั้นอะแดปเตอร์จึงไม่สร้างข้อมูลซ้ำซ้อนสำหรับแต่ละผู้ให้บริการ
ดู[กฎการลงทะเบียนความสามารถ](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)ของปลั๊กอินสำหรับรูปแบบการลงทะเบียนและข้อจำกัดปัจจุบัน

## แผนผังโค้ดและการทดสอบ

| พฤติกรรม | การนำไปใช้งาน | หลักฐานการทดสอบในรีโพซิทอรีนี้ |
|---|---|---|
| การตรวจสอบ HTTPS, ขอบเขตจำกัด, การยืนยันตัวตนด้วย bearer เท่านั้น และการแบ่งหน้า v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| การค้นพบ MCP, การเรียกใช้ และการเปลี่ยนแปลงสิทธิ์ | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| วิธีใช้บนบรรทัดคำสั่ง, เวอร์ชัน และการตั้งค่าที่ขาดหายไป | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

การทดสอบโปรเซสย่อยใช้ไคลเอนต์และเซิร์ฟเวอร์ SDK จริงร่วมกับ HTTP endpoint จำลอง (fixture) ทั้งนี้ไม่ได้ต้องใช้หรือทดแทนการทดสอบการบูรณาการกับ Cacti จริง

## แนวทางการรักษาความปลอดภัย

- ใช้ [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) อย่างเป็นทางการสำหรับการเริ่มต้นระบบ การค้นพบเครื่องมือ การเรียกใช้งาน และการจัดเฟรมผ่าน stdio
- เปิดเผยเฉพาะความสามารถที่มีคำอธิบายประกอบ (annotations) เป็นแบบอ่านอย่างเดียว ไม่ทำลายข้อมูล และ idempotent เท่านั้น schema และชื่อมาจาก Cacti โดยตรง ตัวอะแดปเตอร์ไม่มี SQL ข้อมูลรับรองอุปกรณ์ หรือคำสั่งซ่อมแซมใดๆ
- ส่งเฉพาะ bearer token เท่านั้น ไม่มีคุกกี้และไม่มีขั้นตอน CSRF ปลั๊กอินจะตรวจสอบความถูกต้องของโทเคนและสิทธิ์ใหม่ในทุกคำขอ
- ใช้ HTTPS ที่ผ่านการตรวจสอบแล้ว ไม่จัดเก็บคุกกี้ ปฏิเสธการเปลี่ยนเส้นทาง (redirects) และไม่สนใจตัวแปรสภาพแวดล้อมของพร็อกซี การใช้ HTTP ต้องระบุ `--allow-loopback-http` และเป็นแอดเดรส loopback โดยตรงหรือ `localhost`
- จำกัดการเรียกใช้ API ไว้ที่ 35 วินาทีโดยรวม, 5 วินาทีสำหรับการเชื่อมต่อ, 30 วินาทีสำหรับการไม่มีกิจกรรมบนเครือข่าย และประมาณ 1 MB ต่อการตอบกลับ (1,100,000 ไบต์) เนื้อหาคำขอจำกัดไว้ที่ 16,384 ไบต์ การเรียกใช้งานจะถูกจัดลำดับแบบทีละรายการต่อเซสชันไคลเอนต์
- ตรวจสอบอาร์กิวเมนต์ของเครื่องมือเทียบกับ input schema จากการค้นพบครั้งล่าสุดก่อนส่ง และประมวลผลเฉพาะ id ที่อยู่ในรายการที่ตรวจสอบแล้วเท่านั้น หากข้อมูลไม่ตรงกันหรือ schema จากเซิร์ฟเวอร์ไม่ถูกต้อง ระบบจะส่งกลับเป็นข้อผิดพลาดของเครื่องมือ ไม่ใช่การแครช
- ไม่ลองเรียกใช้งานซ้ำโดยอัตโนมัติ ข้อผิดพลาดของเครื่องมือจะส่งกลับเฉพาะสถานะ HTTP, `status` ตามมาตรฐาน AIP-193 และ `reason` ของ ErrorInfo เท่านั้น โดยไม่ส่งข้อความจากเซิร์ฟเวอร์ เนื้อหาการตอบกลับ หรือข้อมูลรับรอง โดยสงวน stdout ไว้สำหรับข้อความ MCP เท่านั้น

เวอร์ชันของ SDK ถูกตรึงไว้โดย `uv.lock` (`mcp>=2.3,<3` ใน `pyproject.toml`) อะแดปเตอร์นี้ใช้เซิร์ฟเวอร์ระดับล่างในเวอร์ชัน 2.x ร่วมกับการขนส่งผ่าน stdio โดยไม่ได้รองรับ MCP HTTP endpoint ระยะไกล, OAuth, resources, prompts, subscriptions หรือ background tasks

ดูเพิ่มเติมที่[ข้อกำหนด API](../../../docs/api.md) และ[แผนการพัฒนา](../../../docs/plan.md)

## การติดตั้งและบรรทัดคำสั่ง

ต้องใช้ Python 3.12 ขึ้นไป และ [uv](https://docs.astral.sh/uv/)
จากไดเรกทอรีที่โคลนรีโพซิทอรีนี้:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

ติดตั้งและเปิดใช้งานปลั๊กอิน PHP ให้สิทธิ์ realm แก่ผู้ใช้ Cacti เฉพาะกิจ และสร้าง personal access token สำหรับผู้ใช้นั้น (รูปแบบ `cmcp_pat_` ตามด้วยเลขฐานสิบหกตัวพิมพ์เล็ก 64 หลัก) ในคอนโซลของปลั๊กอิน บนหน้า My MCP Tokens หรือผ่านคำสั่ง `tokens.php`
สิทธิ์ realm ของ Cacti และสิทธิ์การเข้าถึงอุปกรณ์ที่มีอยู่เดิมของผู้ใช้ยังคงมีผลตามปกติ

ส่งต่อโทเคนผ่านตัวจัดการความลับของคุณในชื่อ `CACTI_MCP_TOKEN` ห้ามเพิ่มโทเคนลงในซอร์สคอนโทรลหรืออาร์กิวเมนต์ของคำสั่งโดยเด็ดขาด ตั้งค่า endpoint แยกต่างหาก โดยต้องเป็น URL แบบ HTTPS ที่ลงท้ายด้วย `/plugins/mcp/api.php` และไม่มีข้อมูลรับรอง, query หรือ fragment:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` ใช้ตั้งค่า endpoint แทน `CACTI_MCP_ENDPOINT`
`--allow-loopback-http` อนุญาตให้ใช้ HTTP ธรรมดากับ `localhost`, `127.0.0.1` หรือ `::1` สำหรับการทดสอบในเครื่อง, `--lang LOCALE` ใช้กำหนดภาษาของข้อความ CLI เอง และ `--version` ใช้แสดงเวอร์ชัน หากขาดทั้ง endpoint หรือ `CACTI_MCP_TOKEN` อย่างใดอย่างหนึ่ง คำสั่งจะจบการทำงานพร้อมแจ้งข้อผิดพลาดการใช้งาน

### การรองรับหลายภาษา (Localization)

ข้อความช่วยเหลือของ CLI และข้อความแสดงข้อผิดพลาดของอะแดปเตอร์รองรับ 45 ภาษา (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) โดยไม่ต้องติดตั้งแพ็กเกจเพิ่มเติม ลำดับการตรวจสอบภาษาจะดูจาก `--lang`, `LC_ALL`, `LC_MESSAGES` และ `LANG` ตามลำดับ และใช้ `en` เป็นค่าเริ่มต้น (`C`/`POSIX` และแท็กที่ไม่รู้จักจะใช้เป็น `en` เช่นกัน) ชื่อเครื่องมือ MCP, schema และ JSON payload ของเครื่องมือที่ทำงานสำเร็จจะไม่ได้รับผลกระทบ ส่วนข้อความแสดงข้อผิดพลาดของอะแดปเตอร์ที่ส่งคืนพร้อม `is_error=True` จะเป็นไปตามภาษาที่ใช้งานอยู่

โปรเซสจะรอรับข้อความ MCP บน stdin โดยปกติไคลเอนต์ MCP จะเป็นผู้เปิดใช้งานโปรเซสนี้
สำหรับไคลเอนต์ที่รองรับรูปแบบการตั้งค่า `mcpServers` ทั่วไป:

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

ตั้งค่าไคลเอนต์ให้ส่งผ่าน `CACTI_MCP_ENDPOINT` และ `CACTI_MCP_TOKEN` ไปยังโปรเซสย่อยผ่านตัวแปรสภาพแวดล้อมหรือระบบจัดการความลับ การสืบทอดตัวแปรสภาพแวดล้อมขึ้นอยู่กับแต่ละไคลเอนต์ และไม่มีแฟล็กสำหรับส่งโทเคนทางบรรทัดคำสั่ง

แพ็กเกจ Python ที่ติดตั้งแยกต่างหากจะให้คำสั่งคอนโซล `cacti-mcp` ไม่จำเป็นต้องเผยแพร่บน PyPI ก็สามารถรันจากซอร์สโค้ดได้ ทั้งนี้ปลั๊กอิน PHP ไม่ได้พึ่งพา Python แต่อย่างใด

## รีลีส (Releases)

เวอร์ชันของแพ็กเกจถูกบันทึกไว้ใน [pyproject.toml](../../../pyproject.toml)
ระหว่างที่ยังไม่มีรีลีสที่ติดแท็ก ให้ใช้ซอร์สโค้ดที่โคลนมาหรือใช้อาร์ติแฟกต์ `python-distributions` จาก[การรัน CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) ที่ผ่านการทดสอบแล้ว
อาร์ติแฟกต์ประกอบด้วยไฟล์ wheel และไฟล์ซอร์ส แพ็กเกจที่ติดตั้งแล้วมีทั้งคำสั่ง `cacti-mcp` และ `python -m cacti_mcp` แต่ไม่ได้รวมปลั๊กอิน PHP ไว้ด้วย

## การพัฒนาและการทดสอบ

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

การทดสอบครอบคลุมถึงการตรวจสอบ HTTP, การแยกส่วนข้อมูลรับรอง, คำขอแบบใช้ bearer เท่านั้น, การแบ่งหน้า, การปกปิดข้อมูลสำคัญในข้อผิดพลาด และการแลกเปลี่ยนข้อมูลจริงระหว่างไคลเอนต์และเซิร์ฟเวอร์ SDK ผ่านโปรเซสย่อยกับเซิร์ฟเวอร์ HTTP จำลอง โดยไม่จำเป็นต้องติดตั้ง Cacti จริง

รีโพซิทอรีนี้ใช้ `src/cacti_mcp/`, pytest, Ruff, uv และ Hatchling ระบบ CI ทดสอบบน Python 3.12, 3.13 และ 3.14 และมีงานสร้างแพ็กเกจแยกต่างหากเพื่อสร้างไฟล์ wheel และซอร์ส ติดตั้ง wheel นอกไดเรกทอรีโค้ด และทดสอบจุดเข้าใช้งานทั้งสองแบบ อาร์ติแฟกต์ของเวิร์กโฟลว์จะเก็บทั้งแพ็กเกจและผลการทดสอบ

## การมีส่วนร่วม

ส่ง Pull Request ไปยังบรานช์ `develop` รักษาความเข้ากันได้ของอะแดปเตอร์กับ Python 3.12 ปฏิบัติตามการตั้งค่า Ruff และโครงสร้างแพ็กเกจ `src/cacti_mcp/` ที่มีอยู่ และสงวน stdout ไว้สำหรับข้อความ MCP เท่านั้น เพิ่มการทดสอบเมื่อมีการแก้ไขพฤติกรรมการขนส่งข้อมูลหรือเครื่องมือ รันการตรวจสอบข้างต้นทั้งหมด และเซ็นรับรองคอมมิตด้วย `git commit -s`
ประสานงานการเปลี่ยนแปลง API ร่วมกับปลั๊กอิน Cacti MCP และอัปเดต [docs/api.md](../../../docs/api.md) ด้วย

## สัญญาอนุญาต

Copyright (C) 2026 Thomas Vincent เผยแพร่ภายใต้สัญญาอนุญาต GNU General Public License เวอร์ชัน 2 หรือใหม่กว่า ดูรายละเอียดที่ [LICENSE](../../../LICENSE)
