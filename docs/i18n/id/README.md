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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · **Bahasa Indonesia**

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP adalah adaptor Python yang mengekspos kemampuan
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) sebagai alat MCP
melalui stdio. Plugin tersebut sudah menyajikan MCP melalui HTTP secara langsung, jadi gunakan
opsi itu apabila klien Anda dapat terhubung ke server jarak jauh. Adaptor ini ditujukan untuk
klien yang hanya berkomunikasi melalui stdio. Adaptor ini menggunakan SDK MCP Python resmi dan
menerjemahkan pemanggilan alat ke API HTTPS milik plugin (kontrak abilities v2, disajikan
di bawah jalur `/v1/`, hanya menggunakan token bearer).
Cacti memegang penuh autentikasi, otorisasi, validasi, dan eksekusi.

**Status: dalam pengembangan, sebelum 1.0.** Versi 0.1.0 mendukung inventaris perangkat
hanya-baca dan versi instalasi melalui pendampingnya
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp).
Belum ada rilis bertag. Diagnostik doctor dan perbaikan direncanakan untuk pengembangan mendatang.

## Kemampuan yang diekspos

| Operasi | Alat MCP yang disediakan oleh plugin Cacti MCP |
|---|---|
| Menampilkan daftar perangkat yang boleh dilihat pemilik token | `cacti-list-devices` |
| Membaca satu perangkat yang diizinkan | `cacti-get-device` |
| Membaca versi Cacti, plugin, dan API | `cacti-get-system-info` |

Nama, deskripsi, dan skema input berasal dari respons penemuan Cacti yang telah difilter
berdasarkan izin. Penyedia hanya-baca tambahan yang diizinkan dapat ditemukan
tanpa perlu menambahkan handler alat Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Kasus penggunaan

Hubungkan klien MCP untuk melihat daftar perangkat Cacti yang boleh diakses oleh pengguna khususnya,
mencari satu perangkat yang diizinkan, atau mengambil versi instalasi ketika pengguna
memiliki realm administratif yang diperlukan. Nama dan skema input berasal dari
respons penemuan plugin, sehingga adaptor tidak menduplikasi setiap penyedia.
Lihat
[aturan pendaftaran ability](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
pada plugin untuk model pendaftaran dan batasan saat ini.

## Peta kode dan pengujian

| Perilaku | Implementasi | Bukti pengujian di repositori ini |
|---|---|---|
| Validasi HTTPS, batasan, autentikasi khusus bearer, dan paginasi v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Penemuan MCP, pemanggilan, dan perubahan izin | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Bantuan baris perintah, versi, dan konfigurasi yang hilang | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Pengujian subproses menggunakan klien dan server SDK sungguhan dengan endpoint HTTP
fikstur. Pengujian ini tidak memerlukan ataupun menggantikan pemeriksaan integrasi Cacti secara langsung.

## Cara menjaga keamanan

- Menggunakan [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) resmi
  untuk inisialisasi, penemuan alat, pemanggilan, dan pembingkaian stdio.
- Hanya mengekspos ability yang anotasinya tepat bersifat hanya-baca, non-destruktif, dan idempoten. Skema dan nama berasal
  dari Cacti; adaptor ini tidak memuat SQL, kredensial perangkat, ataupun perintah perbaikan.
- Hanya mengirimkan token bearer: tanpa cookie, tanpa langkah CSRF. Plugin memeriksa ulang
  validitas token dan izin pada setiap permintaan.
- Menggunakan HTTPS terverifikasi, tidak pernah menyimpan cookie, menolak pengalihan, dan
  mengabaikan variabel lingkungan proxy. HTTP memerlukan `--allow-loopback-http`
  dan alamat loopback literal atau `localhost`.
- Membatasi panggilan API hingga 35 detik secara keseluruhan, 5 detik untuk koneksi, 30 detik
  inaktivitas jaringan, dan sekitar 1 MB per respons (1.100.000 byte).
  Body permintaan dibatasi hingga 16.384 byte. Panggilan diserialisasi per sesi
  klien.
- Memeriksa argumen alat terhadap skema input dari penemuan terakhir sebelum
  mengirimkannya, dan hanya mengeksekusi id dari katalog terverifikasi tersebut. Ketidakcocokan, atau
  skema yang cacat dari server, dikembalikan sebagai galat alat, bukan crash.
- Tidak mengulang eksekusi secara otomatis. Galat alat hanya membawa status
  HTTP, `status` AIP-193, dan `reason` ErrorInfo; tidak pernah menyertakan teks
  pesan server, body respons, ataupun kredensial. Stdout dicadangkan khusus untuk pesan MCP.

Versi SDK dikunci oleh `uv.lock` (`mcp>=2.3,<3` di `pyproject.toml`). Adaptor
ini menggunakan server tingkat rendah 2.x dengan transport stdio; adaptor ini tidak
mengimplementasikan endpoint HTTP MCP jarak jauh, OAuth, resource,
prompt, langganan, ataupun tugas latar belakang.

Lihat [kontrak API](../../../docs/api.md) dan [rencana implementasi](../../../docs/plan.md).

## Instalasi dan baris perintah

Memerlukan Python 3.12 atau lebih baru dan [uv](https://docs.astral.sh/uv/).
Dari salinan repositori ini:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Pasang dan aktifkan plugin PHP, berikan realm-nya kepada pengguna Cacti khusus,
dan buat token akses pribadi untuk pengguna tersebut (format `cmcp_pat_` diikuti
64 digit heksadesimal huruf kecil) di konsol plugin, pada halaman My MCP Tokens,
atau dengan perintah `tokens.php` miliknya.
Realm Cacti dan izin perangkat yang sudah dimiliki pengguna tersebut tetap berlaku.

Sediakan token melalui pengelola rahasia Anda sebagai `CACTI_MCP_TOKEN`; jangan pernah menambahkannya
ke kontrol sumber atau argumen perintah. Tetapkan endpoint secara terpisah. Endpoint harus berupa
URL HTTPS yang diakhiri dengan `/plugins/mcp/api.php`, tanpa kredensial, kueri, atau
fragmen:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` menetapkan endpoint alih-alih `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` mengizinkan HTTP biasa ke `localhost`, `127.0.0.1`, atau `::1`
untuk pengujian lokal, `--lang LOCALE` menimpa pelokalan pesan CLI, dan
`--version` mencetak versi. Tanpa adanya endpoint dan `CACTI_MCP_TOKEN`,
perintah akan keluar dengan galat penggunaan.

### Pelokalan

Bantuan CLI dan pesan galat adaptor tersedia dalam 45 lokal (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) tanpa dependensi tambahan. Resolusi lokal
memeriksa `--lang`, lalu `LC_ALL`, `LC_MESSAGES`, dan `LANG`, dengan fallback
ke `en` (`C`/`POSIX` dan tag yang tidak dikenal juga diarahkan ke `en`). Nama alat
MCP, skema, dan payload alat JSON yang berhasil tidak terpengaruh; pesan galat
adaptor yang dikembalikan dengan `is_error=True` mengikuti lokal yang aktif.

Proses menunggu pesan MCP di stdin. Klien MCP biasanya meluncurkannya.
Untuk klien yang menerima format konfigurasi `mcpServers` yang umum:

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

Konfigurasikan klien untuk meneruskan `CACTI_MCP_ENDPOINT` dan `CACTI_MCP_TOKEN` ke
subproses melalui lingkungan atau fasilitas rahasianya. Pewarisan lingkungan
bergantung pada klien. Tidak ada flag baris perintah untuk token.

Distribusi Python yang dapat diinstal secara terpisah menyediakan perintah konsol
`cacti-mcp`. Publikasi PyPI tidak diperlukan untuk menjalankan hasil checkout. Plugin PHP tidak
memiliki ketergantungan Python.

## Rilis

Versi distribusi dicatat di [pyproject.toml](../../../pyproject.toml).
Hingga rilis bertag tersedia, gunakan checkout sumber atau artefak
`python-distributions` dari
[proses CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) yang berhasil.
Artefak tersebut berisi arsip wheel dan sumber. Paket yang terinstal menyediakan
baik perintah `cacti-mcp` maupun `python -m cacti_mcp`; paket ini tidak berisi
plugin PHP.

## Pengembangan dan pengujian

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Pengujian mencakup validasi HTTP, isolasi kredensial, permintaan khusus bearer,
paginasi, penyensoran galat, serta pertukaran subproses klien/server SDK sungguhan terhadap
server HTTP fikstur. Pengujian tidak memerlukan instalasi Cacti langsung.

Repositori ini menggunakan `src/cacti_mcp/`, pytest, Ruff, uv, dan Hatchling. CI menguji
Python 3.12, 3.13, dan 3.14. Pekerjaan pemaketan terpisah membangun arsip wheel
dan sumber, menginstal wheel di luar checkout, dan melakukan smoke-test pada
kedua titik masuk. Distribusi dan hasil pengujian merupakan artefak alur kerja.

## Kontribusi

Pull request ditujukan ke `develop`. Pertahankan agar adaptor kompatibel dengan Python 3.12,
ikuti konfigurasi Ruff dan tata letak paket `src/cacti_mcp/` yang ada, serta
jaga agar stdout tetap dicadangkan untuk pesan MCP. Tambahkan pengujian untuk perubahan perilaku transport atau alat,
jalankan pemeriksaan di atas, dan tanda tangani commit dengan `git commit -s`.
Koordinasikan perubahan API dengan plugin Cacti MCP dan perbarui [docs/api.md](../../../docs/api.md).

## Lisensi

Hak Cipta (C) 2026 Thomas Vincent. Dirilis di bawah GNU General Public
License, versi 2 atau lebih baru. Lihat [LICENSE](../../../LICENSE).
