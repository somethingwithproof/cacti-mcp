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

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · **Bahasa Melayu** · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP ialah penyesuai Python yang mendedahkan keupayaan
[pemalam Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) sebagai alat MCP
melalui stdio. Pemalam tersebut sudah menyediakan MCP melalui HTTP secara langsung, jadi gunakan
cara itu apabila klien anda boleh menyambung ke pelayan jauh. Penyesuai ini adalah untuk
klien yang hanya menggunakan stdio. Ia menggunakan SDK Python MCP rasmi dan
menterjemahkan panggilan alat kepada API HTTPS pemalam (kontrak keupayaan v2, disediakan
di bawah laluan `/v1/`, token pembawa sahaja).
Cacti menguruskan pengesahan, keizinan, pengesahan input, dan pelaksanaan.

**Status: dalam pembangunan, sebelum 1.0.** Versi 0.1.0 menyokong inventori peranti baca sahaja
dan versi pemasangan melalui
[pemalam Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) pasangannya.
Belum ada keluaran bertag lagi. Diagnostik Doctor dan pembaikan ialah kerja masa hadapan.

## Apa yang didedahkan

| Operasi | Alat MCP yang dibekalkan oleh pemalam Cacti MCP |
|---|---|
| Senaraikan peranti yang boleh dilihat oleh pemilik token | `cacti-list-devices` |
| Baca satu peranti yang dibenarkan | `cacti-get-device` |
| Baca versi Cacti, pemalam, dan API | `cacti-get-system-info` |

Nama, huraian, dan skema input datang daripada respons penemuan Cacti yang ditapis mengikut
kebenaran. Pembekal baca sahaja tambahan yang dibenarkan boleh ditemui
tanpa menambah pengendali alat Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Kes penggunaan

Sambungkan klien MCP untuk menyenaraikan peranti Cacti yang boleh dilihat oleh pengguna khusus,
mencari satu peranti yang dibenarkan, atau mendapatkan semula versi pemasangan apabila pengguna
mempunyai realm pentadbiran yang diperlukan. Nama dan skema input datang daripada
respons penemuan pemalam, jadi penyesuai tidak menduplikasi setiap pembekal.
Lihat
[peraturan pendaftaran keupayaan](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
pemalam tersebut untuk model pendaftaran dan had semasa.

## Peta kod dan ujian

| Kelakuan | Pelaksanaan | Bukti ujian dalam repositori ini |
|---|---|---|
| Pengesahan HTTPS, had, pengesahan pembawa sahaja, dan penghalaman v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Penemuan MCP, panggilan, dan perubahan kebenaran | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Bantuan baris arahan, versi, dan konfigurasi yang hilang | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Ujian subproses menggunakan klien dan pelayan SDK sebenar dengan titik akhir HTTP
lekapan. Ia tidak memerlukan atau menggantikan semakan penyepaduan Cacti secara langsung.

## Bagaimana ia kekal selamat

- Menggunakan [SDK Python `mcp` rasmi](https://github.com/modelcontextprotocol/python-sdk)
  untuk permulaan, penemuan alat, panggilan, dan pembingkaian stdio.
- Hanya mendedahkan keupayaan yang anotasinya betul-betul baca sahaja, tidak memusnahkan, dan idempoten. Skema dan nama datang
  daripada Cacti; penyesuai tidak mengandungi SQL, kelayakan peranti, atau arahan pembaikan.
- Hanya menghantar token pembawa: tiada kuki, tiada langkah CSRF. Pemalam menyemak semula
  kesahan token dan kebenaran pada setiap permintaan.
- Menggunakan HTTPS yang disahkan, tidak pernah menyimpan kuki, menolak ubah hala, dan
  mengabaikan pembolehubah persekitaran proksi. HTTP memerlukan `--allow-loopback-http`
  dan alamat gelung balik literal atau `localhost`.
- Mengehadkan panggilan API kepada 35 saat keseluruhan, 5 saat untuk menyambung, 30 saat
  ketidakaktifan rangkaian, dan kira-kira 1 MB bagi setiap respons (1,100,000 bait).
  Isi permintaan dihadkan kepada 16,384 bait. Panggilan disirikan bagi setiap sesi
  klien.
- Menyemak argumen alat berbanding skema input daripada penemuan terakhir sebelum
  menghantarnya, dan hanya melaksanakan id daripada katalog yang disahkan itu. Ketidakpadanan, atau
  skema yang cacat daripada pelayan, kembali sebagai ralat alat, bukan ranap.
- Tidak mencuba semula pelaksanaan secara automatik. Ralat alat hanya membawa status HTTP,
  `status` AIP-193, dan `reason` ErrorInfo; tidak pernah membawa teks mesej pelayan,
  isi respons, atau kelayakan. Stdout dikhaskan untuk mesej MCP.

Versi SDK dipinkan oleh `uv.lock` (`mcp>=2.3,<3` dalam `pyproject.toml`). Penyesuai
ini menggunakan pelayan aras rendah 2.x dengan pengangkutan stdio; ia tidak
melaksanakan titik akhir HTTP MCP jauh, OAuth, sumber,
gesaan, langganan, atau tugasan latar belakang.

Lihat [kontrak API](../../../docs/api.md) dan [pelan pelaksanaan](../../../docs/plan.md).

## Pemasangan dan baris arahan

Memerlukan Python 3.12 atau lebih baharu dan [uv](https://docs.astral.sh/uv/).
Daripada salinan repositori ini:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Pasang dan dayakan pemalam PHP, berikan realmnya kepada pengguna Cacti khusus,
dan cipta token akses peribadi untuk pengguna tersebut (format `cmcp_pat_` diikuti
oleh 64 digit heksadesimal huruf kecil) dalam konsol pemalam, pada halaman My MCP Tokens,
atau dengan arahan `tokens.php`.
Realm Cacti dan kebenaran peranti sedia ada pengguna tersebut masih terpakai.

Bekalkan token melalui pengurus rahsia anda sebagai `CACTI_MCP_TOKEN`; jangan sekali-kali menambahkannya
ke dalam kawalan sumber atau argumen arahan. Tetapkan titik akhir secara berasingan. Ia mestilah
URL HTTPS yang berakhir dengan `/plugins/mcp/api.php`, tanpa kelayakan, pertanyaan, atau
serpihan:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` menetapkan titik akhir dan bukannya `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` membenarkan HTTP biasa ke `localhost`, `127.0.0.1`, atau `::1`
untuk ujian setempat, `--lang LOCALE` mengatasi penyetempatan mesej CLI, dan
`--version` mencetak versi. Tanpa kedua-dua titik akhir dan `CACTI_MCP_TOKEN`,
arahan akan keluar dengan ralat penggunaan.

### Penyetempatan

Bantuan CLI dan mesej ralat penyesuai disediakan dalam 45 lokal (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) tanpa kebergantungan tambahan. Penyelesaian
lokal menyemak `--lang`, kemudian `LC_ALL`, `LC_MESSAGES`, dan `LANG`, berbalik
kepada `en` (`C`/`POSIX` dan tag yang tidak diketahui juga diselesaikan kepada `en`). Nama alat MCP,
skema, dan muatan JSON alat yang berjaya tidak terjejas; mesej ralat penyesuai
yang dikembalikan dengan `is_error=True` mengikut lokal yang aktif.

Proses ini menunggu mesej MCP pada stdin. Klien MCP biasanya melancarkannya.
Untuk klien yang menerima format konfigurasi `mcpServers` yang lazim:

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

Konfigurasikan klien untuk menghantar `CACTI_MCP_ENDPOINT` dan `CACTI_MCP_TOKEN` kepada
subproses melalui persekitaran atau kemudahan rahsianya. Pewarisan persekitaran
bergantung pada klien. Tiada bendera baris arahan untuk token.

Pengedaran Python yang boleh dipasang secara berasingan membekalkan arahan konsol
`cacti-mcp`. Tiada penerbitan PyPI diperlukan untuk menjalankan salinan setempat. Pemalam PHP
tidak mempunyai kebergantungan Python.

## Keluaran

Versi pengedaran direkodkan dalam [pyproject.toml](../../../pyproject.toml).
Sehingga keluaran bertag tersedia, gunakan salinan sumber atau artifak
`python-distributions` daripada [larian CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml)
yang berjaya.
Artifak tersebut mengandungi fail wheel dan arkib sumber. Pakej yang dipasang membekalkan
kedua-dua arahan `cacti-mcp` dan `python -m cacti_mcp`; ia tidak mengandungi
pemalam PHP.

## Pembangunan dan ujian

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Ujian meliputi pengesahan HTTP, pengasingan kelayakan, permintaan pembawa sahaja,
penghalaman, penapisan ralat, dan pertukaran subproses klien/pelayan SDK sebenar terhadap
pelayan HTTP lekapan. Ia tidak memerlukan pemasangan Cacti secara langsung.

Repositori ini menggunakan `src/cacti_mcp/`, pytest, Ruff, uv, dan Hatchling. CI menguji
Python 3.12, 3.13, dan 3.14. Tugasan pempakejan berasingan membina fail wheel
dan arkib sumber, memasang fail wheel di luar salinan setempat, dan menguji kedua-dua
titik masuk secara asas. Pengedaran dan keputusan ujian ialah artifak aliran kerja.

## Menyumbang

Permintaan tarik dihantar ke `develop`. Pastikan penyesuai serasi dengan Python 3.12,
ikuti konfigurasi Ruff sedia ada dan susun atur pakej `src/cacti_mcp/`, serta
pastikan stdout dikhaskan untuk mesej MCP. Tambahkan ujian untuk perubahan kelakuan pengangkutan atau alat,
jalankan semakan di atas, dan tandatangani komit dengan `git commit -s`.
Selaraskan perubahan API dengan pemalam Cacti MCP dan kemas kini [docs/api.md](../../../docs/api.md).

## Lesen

Hak Cipta (C) 2026 Thomas Vincent. Dikeluarkan di bawah GNU General Public
License, versi 2 atau lebih baharu. Lihat [LICENSE](../../../LICENSE).
