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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · **Türkçe** · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP, [Cacti MCP eklentisinin](https://github.com/somethingwithproof/plugin_mcp)
yeteneklerini stdio üzerinden MCP araçları olarak sunan bir Python bağdaştırıcısıdır.
Eklenti halihazırda MCP'yi doğrudan HTTP üzerinden sunmaktadır; bu nedenle istemciniz
uzak bir sunucuya bağlanabiliyorsa doğrudan onu kullanın. Bu bağdaştırıcı, yalnızca
stdio ile konuşabilen istemciler içindir. Resmi Python MCP SDK'sını kullanır ve
araç çağrılarını eklentinin HTTPS API'sine (yetenek sözleşmesi v2, `/v1/` yolları
altında sunulur, yalnızca bearer token) çevirir.
Kimlik doğrulama, yetkilendirme, doğrulama ve yürütme işlemleri Cacti'ye aittir.

**Durum: geliştirme aşamasında, 1.0 öncesi.** 0.1.0 sürümü, eşlik eden
[Cacti MCP eklentisi](https://github.com/somethingwithproof/plugin_mcp) aracılığıyla
salt okunur cihaz envanterini ve kurulum sürümlerini destekler.
Henüz etiketlenmiş bir sürüm yoktur. Doctor tanılama ve onarım özellikleri gelecekteki
çalışmalar kapsamındadır.

## Neleri dışa açar

| İşlem | Cacti MCP eklentisi tarafından sağlanan MCP aracı |
|---|---|
| Belirteç sahibinin görebildiği cihazları listele | `cacti-list-devices` |
| İzin verilen bir cihazı oku | `cacti-get-device` |
| Cacti, eklenti ve API sürümlerini oku | `cacti-get-system-info` |

Adlar, açıklamalar ve girdi şemaları Cacti'nin izinlere göre filtrelenmiş keşif
yanıtından gelir. Python araç işleyicileri eklenmeden diğer izinli salt okunur
sağlayıcılar da keşfedilebilir.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Kullanım senaryoları

Ayrılmış kullanıcısının görebildiği Cacti cihazlarını listelemek, izin verilen bir
cihazı sorgulamak veya kullanıcı gerekli yönetici yetki alanına (realm) sahip
olduğunda kurulum sürümlerini almak için bir MCP istemcisi bağlayın. Adlar ve girdi
şemaları eklentinin keşif yanıtından geldiği için bağdaştırıcı her sağlayıcıyı
ayrıca yinelemez. Kayıt modeli ve mevcut sınırlar için eklentinin
[yetenek kayıt kurallarına](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
bakın.

## Kod ve test haritası

| Davranış | Uygulama | Bu depodaki test kanıtı |
|---|---|---|
| HTTPS doğrulama, sınırlar, yalnızca bearer kimlik doğrulama ve v2 sayfalama | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| MCP keşfi, çağrılar ve izin değişiklikleri | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Komut satırı yardımı, sürüm ve eksik yapılandırma | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Alt süreç testi, bir test (fixture) HTTP uç noktasıyla gerçek bir SDK istemcisi ve
sunucusu kullanır. Canlı bir Cacti entegrasyon denetiminin yerini almaz ve bunu
gerektirmez.

## Güvenliği nasıl sağlar

- Başlatma, araç keşfi, çağrılar ve stdio çerçeveleme için resmi
  [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) paketini kullanır.
- Yalnızca ek açıklamaları kesin olarak salt okunur, yıkıcı olmayan ve eşgüçlü (idempotent)
  olan yetenekleri dışa açar. Şemalar ve adlar Cacti'den gelir; bağdaştırıcı hiçbir
  SQL, cihaz kimlik bilgisi veya onarım komutu içermez.
- Yalnızca bearer token gönderir: çerez yok, CSRF adımı yok. Eklenti, her istekte
  belirteç geçerliliğini ve izinleri yeniden denetler.
- Doğrulanmış HTTPS kullanır, asla çerez saklamaz, yönlendirmeleri reddeder ve vekil
  sunucu (proxy) ortam değişkenlerini yoksayar. HTTP, `--allow-loopback-http`
  seçeneğini ve birebir bir loopback adresini veya `localhost` değerini gerektirir.
- API çağrılarını toplamda 35 saniye, bağlantı için 5 saniye, ağ hareketsizliği
  için 30 saniye ve yanıt başına yaklaşık 1 MB (1.100.000 bayt) ile sınırlar.
  İstek gövdeleri 16.384 bayt ile sınırlıdır. Çağrılar istemci oturumu başına
  sıralı olarak işlenir.
- Araç argümanlarını göndermeden önce son keşiften gelen girdi şemasına göre
  denetler ve yalnızca o doğrulanmış katalogdaki kimlikleri çalıştırır. Bir
  uyumsuzluk veya sunucudan gelen bozuk bir şema, çökme yerine araç hatası olarak döner.
- Yürütmeyi otomatik olarak yeniden denemez. Araç hataları yalnızca HTTP
  durumunu, AIP-193 `status` değerini ve ErrorInfo `reason` alanını taşır; asla
  sunucu mesaj metnini, yanıt gövdelerini veya kimlik bilgilerini içermez. Stdout,
  MCP mesajları için ayrılmıştır.

SDK sürümü `uv.lock` tarafından sabitlenmiştir (`pyproject.toml` içinde `mcp>=2.3,<3`).
Bu bağdaştırıcı stdio aktarımıyla 2.x düşük düzey sunucusunu kullanır; uzak bir MCP
HTTP uç noktası, OAuth, kaynaklar, istemler (prompts), abonelikler veya arka plan
görevleri uygulamaz.

[API sözleşmesine](../../../docs/api.md) ve [uygulama planına](../../../docs/plan.md) bakın.

## Kurulum ve komut satırı

Python 3.12 veya üzerini ve [uv](https://docs.astral.sh/uv/) aracını gerektirir.
Bu deponun yerel bir kopyasından:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

PHP eklentisini kurup etkinleştirin, yetki alanını (realm) ayrılmış bir Cacti
kullanıcısına verin ve eklentinin konsolunda, My MCP Tokens sayfasında veya
`tokens.php` komutuyla bu kullanıcı için bir kişisel erişim belirteci (`cmcp_pat_`
ardından 64 küçük harf onaltılık basamak biçiminde) oluşturun.
Kullanıcının mevcut Cacti yetki alanları ve cihaz izinleri geçerliliğini korur.

Belirteci gizli anahtar yöneticiniz üzerinden `CACTI_MCP_TOKEN` olarak sağlayın;
asla kaynak denetimine veya komut argümanlarına eklemeyin. Uç noktayı ayrı olarak
ayarlayın. Kimlik bilgisi, sorgu veya parça (fragment) içermeyen ve `/plugins/mcp/api.php`
ile biten bir HTTPS URL'si olmalıdır:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL`, `CACTI_MCP_ENDPOINT` yerine uç noktayı ayarlar.
`--allow-loopback-http` yerel testler için `localhost`, `127.0.0.1` veya `::1`
adreslerine düz HTTP kullanımına izin verir, `--lang LOCALE` CLI mesaj
yerelleştirmesini geçersiz kılar ve `--version` sürümü yazdırır. Hem uç nokta
hem de `CACTI_MCP_TOKEN` olmadan komut bir kullanım hatasıyla sonlanır.

### Yerelleştirme

CLI yardımı ve bağdaştırıcı hata mesajları sıfır ek bağımlılıkla 45 yerel ayarda
(`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) sunulur. Yerel ayar çözümlemesi önce `--lang`, ardından `LC_ALL`, `LC_MESSAGES` ve `LANG` değişkenlerini denetler; hiçbiri yoksa `en` değerine geri döner (`C`/`POSIX` ve bilinmeyen etiketler de `en` olarak çözümlenir). MCP araç adları, şemalar ve başarılı JSON araç yükleri etkilenmez; `is_error=True` ile döndürülen bağdaştırıcı hata mesajları etkin yerel ayarı izler.

Süreç, stdin üzerinde MCP mesajlarını bekler. Normalde bunu bir MCP istemcisi başlatır.
Yaygın `mcpServers` yapılandırma biçimini kabul eden istemciler için:

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

İstemciyi, `CACTI_MCP_ENDPOINT` ve `CACTI_MCP_TOKEN` değişkenlerini ortamı veya
gizli anahtar mekanizması aracılığıyla alt sürece aktaracak şekilde yapılandırın.
Ortam mirası istemciye bağlıdır. Komut satırında belirteç bayrağı yoktur.

Ayrı olarak kurulabilen Python dağıtımı `cacti-mcp` konsol komutunu sağlar.
Yerel kopyayı çalıştırmak için PyPI yayını gerekmez. PHP eklentisinin Python
bağımlılığı yoktur.

## Sürümler

Dağıtım sürümü [pyproject.toml](../../../pyproject.toml) içinde kayıtlıdır.
Etiketlenmiş sürümler yayımlanana kadar bir kaynak kopyası veya başarılı bir
[CI çalıştırmasından](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml)
elde edilen `python-distributions` yapıtını kullanın.
Yapıt bir wheel ve kaynak arşivi içerir. Kurulan paket hem `cacti-mcp` komutunu
hem de `python -m cacti_mcp` komutunu sağlar; PHP eklentisini içermez.

## Geliştirme ve testler

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Testler HTTP doğrulamasını, kimlik bilgisi yalıtımını, yalnızca bearer isteklerini,
sayfalamayı, hata gizlemeyi (redaction) ve bir test (fixture) HTTP sunucusuna karşı
gerçek bir SDK istemci/sunucu alt süreç alışverişini kapsar. Canlı bir Cacti
kurulumu gerektirmezler.

Depo `src/cacti_mcp/`, pytest, Ruff, uv ve Hatchling kullanır. CI, Python 3.12,
3.13 ve 3.14 sürümlerini test eder. Ayrı bir paketleme işi wheel ve kaynak arşivini
derler, wheel paketini yerel kopya dışında kurar ve her iki giriş noktasını duman
testine tabi tutar. Dağıtımlar ve test sonuçları iş akışı yapıtlarıdır.

## Katkıda bulunma

Çekme istekleri (pull request) `develop` dalına gönderilir. Bağdaştırıcıyı Python 3.12
ile uyumlu tutun, mevcut Ruff yapılandırmasına ve `src/cacti_mcp/` paket düzenine
uyun ve stdout'u MCP mesajları için ayrılmış olarak bırakın. Değiştirilen aktarım
veya araç davranışı için testler ekleyin, yukarıdaki denetimleri çalıştırın ve
commit'leri `git commit -s` ile imzalayın. API değişikliklerini Cacti MCP eklentisiyle
koordine edin ve [docs/api.md](../../../docs/api.md) dosyasını güncelleyin.

## Lisans

Telif Hakkı (C) 2026 Thomas Vincent. GNU Genel Kamu Lisansı, sürüm 2 veya sonrası
kapsamında yayımlanmıştır. Bkz. [LICENSE](../../../LICENSE).
