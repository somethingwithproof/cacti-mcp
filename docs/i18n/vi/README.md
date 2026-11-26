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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · **Tiếng Việt** · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP là một bộ chuyển đổi (adapter) bằng Python giúp cung cấp các khả năng của
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) dưới dạng các công cụ MCP
qua stdio. Bản thân plugin đã phục vụ trực tiếp MCP qua HTTP, vì vậy hãy sử dụng
cách đó khi client của bạn có thể kết nối tới máy chủ từ xa. Bộ chuyển đổi này dành cho
các client chỉ giao tiếp qua stdio. Nó sử dụng Python MCP SDK chính thức và
chuyển đổi các lời gọi công cụ thành HTTPS API của plugin (hợp đồng abilities v2, phục vụ
dưới đường dẫn `/v1/`, chỉ dùng bearer token).
Cacti đảm nhiệm việc xác thực, phân quyền, kiểm tra hợp lệ và thực thi.

**Trạng thái: đang phát triển, trước bản 1.0.** Phiên bản 0.1.0 hỗ trợ xem danh sách
thiết bị chỉ đọc và phiên bản cài đặt thông qua
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) đi kèm.
Hiện chưa có bản phát hành gắn thẻ (tagged release). Các tính năng chẩn đoán Doctor và sửa chữa sẽ được phát triển trong tương lai.

## Những gì được cung cấp

| Thao tác | Công cụ MCP do plugin Cacti MCP cung cấp |
|---|---|
| Liệt kê các thiết bị mà chủ sở hữu token được phép xem | `cacti-list-devices` |
| Đọc thông tin một thiết bị được phép | `cacti-get-device` |
| Đọc phiên bản Cacti, plugin và API | `cacti-get-system-info` |

Tên, mô tả và schema đầu vào lấy từ phản hồi khám phá (discovery) đã được lọc theo quyền của Cacti.
Các nhà cung cấp chỉ đọc được phép bổ sung có thể được khám phá tự động
mà không cần thêm trình xử lý công cụ Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Trường hợp sử dụng

Kết nối một client MCP để liệt kê các thiết bị Cacti mà người dùng chuyên biệt của nó được phép xem,
tra cứu một thiết bị được phép, hoặc lấy thông tin phiên bản cài đặt khi người dùng
có quyền quản trị (administrative realm) cần thiết. Tên và schema đầu vào lấy từ
phản hồi khám phá của plugin, do đó bộ chuyển đổi không sao chép lại từng nhà cung cấp.
Xem [quy tắc đăng ký ability](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
của plugin để biết mô hình đăng ký và các giới hạn hiện tại.

## Sơ đồ mã nguồn và kiểm thử

| Hành vi | Triển khai | Bằng chứng kiểm thử trong kho lưu trữ này |
|---|---|---|
| Kiểm tra hợp lệ HTTPS, giới hạn, xác thực chỉ dùng bearer và phân trang v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Khám phá MCP, gọi công cụ và thay đổi quyền | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Trợ giúp dòng lệnh, phiên bản và thiếu cấu hình | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Bài kiểm thử tiến trình con sử dụng client và server SDK thực tế cùng với một endpoint HTTP
giả lập (fixture). Nó không yêu cầu hay thay thế cho kiểm tra tích hợp với hệ thống Cacti thực tế.

## Cơ chế đảm bảo an toàn

- Sử dụng [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk) chính thức
  cho việc khởi tạo, khám phá công cụ, gọi công cụ và đóng khung stdio.
- Chỉ cung cấp các ability có chú thích chính xác là chỉ đọc, không phá hủy và bất biến (idempotent). Schema và tên đến
  từ Cacti; bộ chuyển đổi không chứa câu lệnh SQL, thông tin đăng nhập thiết bị hay lệnh sửa chữa.
- Chỉ gửi bearer token: không cookie, không bước CSRF. Plugin kiểm tra lại
  tính hợp lệ của token và quyền trên mọi yêu cầu.
- Sử dụng HTTPS đã xác minh, không bao giờ lưu cookie, từ chối chuyển hướng (redirect) và
  bỏ qua các biến môi trường proxy. HTTP yêu cầu `--allow-loopback-http`
  và địa chỉ loopback dạng ký tự hoặc `localhost`.
- Giới hạn lời gọi API tối đa 35 giây tổng thể, 5 giây để kết nối, 30 giây không
  hoạt động mạng và khoảng 1 MB mỗi phản hồi (1.100.000 byte).
  Phần thân yêu cầu (request body) giới hạn ở 16.384 byte. Các lời gọi được tuần tự hóa theo từng phiên
  client.
- Kiểm tra đối số công cụ dựa trên schema đầu vào từ lần khám phá gần nhất trước khi
  gửi, và chỉ thực thi các ID nằm trong danh mục đã xác minh đó. Nếu không khớp hoặc
  schema từ máy chủ bị lỗi định dạng, hệ thống sẽ trả về lỗi công cụ thay vì sập (crash).
- Không tự động thử lại việc thực thi. Lỗi công cụ chỉ mang mã trạng thái HTTP,
  `status` theo chuẩn AIP-193 và `reason` trong ErrorInfo; không bao giờ chứa nội dung
  thông báo của máy chủ, phần thân phản hồi hay thông tin xác thực. Stdout được dành riêng cho các thông điệp MCP.

Phiên bản SDK được cố định bởi `uv.lock` (`mcp>=2.3,<3` trong `pyproject.toml`). Bộ chuyển đổi
này sử dụng máy chủ cấp thấp (low-level server) 2.x của SDK cùng giao thức truyền tải stdio; nó không
triển khai endpoint MCP HTTP từ xa, OAuth, resources,
prompts, subscriptions hay tác vụ nền.

Xem [đặc tả API](../../../docs/api.md) và [kế hoạch triển khai](../../../docs/plan.md).

## Cài đặt và dòng lệnh

Yêu cầu Python 3.12 trở lên và [uv](https://docs.astral.sh/uv/).
Từ bản sao cục bộ của kho lưu trữ này:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Cài đặt và kích hoạt plugin PHP, cấp quyền realm của plugin cho một người dùng Cacti chuyên biệt,
và tạo personal access token cho người dùng đó (định dạng `cmcp_pat_` theo sau
là 64 ký tự hex viết thường) trong bảng điều khiển của plugin, trên trang My MCP Tokens,
hoặc bằng lệnh `tokens.php`.
Các quyền realm Cacti và quyền thiết bị hiện có của người dùng vẫn được áp dụng.

Cung cấp token thông qua trình quản lý bí mật dưới dạng `CACTI_MCP_TOKEN`; không bao giờ đưa nó
vào hệ thống quản lý mã nguồn hay đối số dòng lệnh. Thiết lập endpoint riêng biệt. Nó phải là
một URL HTTPS kết thúc bằng `/plugins/mcp/api.php`, không chứa thông tin đăng nhập, chuỗi truy vấn (query) hay
đoạn neo (fragment):

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` thiết lập endpoint thay cho `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` cho phép HTTP thuần tới `localhost`, `127.0.0.1` hoặc `::1`
để kiểm thử cục bộ, `--lang LOCALE` ghi đè ngôn ngữ bản địa hóa cho thông báo CLI, và
`--version` in ra số phiên bản. Nếu thiếu cả endpoint hoặc `CACTI_MCP_TOKEN`,
lệnh sẽ thoát với lỗi sử dụng (usage error).

### Bản địa hóa

Trợ giúp CLI và các thông báo lỗi của bộ chuyển đổi hỗ trợ 45 ngôn ngữ/vùng (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) mà không cần thêm phụ thuộc nào. Thứ tự
ưu tiên phân giải ngôn ngữ kiểm tra `--lang`, sau đó đến `LC_ALL`, `LC_MESSAGES` và `LANG`, rồi dự phòng
về `en` (`C`/`POSIX` và các thẻ không xác định cũng phân giải về `en`). Tên công cụ MCP,
schema và payload JSON trả về khi thành công không bị ảnh hưởng; thông báo lỗi của bộ chuyển đổi
trả về với `is_error=True` sẽ tuân theo ngôn ngữ đang kích hoạt.

Tiến trình chờ các thông điệp MCP trên stdin. Thông thường một client MCP sẽ khởi chạy nó.
Đối với các client chấp nhận định dạng cấu hình `mcpServers` phổ biến:

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

Cấu hình client để truyền `CACTI_MCP_ENDPOINT` và `CACTI_MCP_TOKEN` vào
tiến trình con thông qua môi trường hoặc công cụ quản lý bí mật của nó. Việc kế thừa biến môi trường
phụ thuộc vào từng client. Không có cờ dòng lệnh nào cho token.

Bản phân phối Python có thể cài đặt riêng biệt cung cấp lệnh console `cacti-mcp`.
Không cần phát hành lên PyPI để chạy bản sao từ mã nguồn. Plugin PHP không có
phụ thuộc Python nào.

## Phát hành

Phiên bản phân phối được ghi trong [pyproject.toml](../../../pyproject.toml).
Cho đến khi có các bản phát hành gắn thẻ, hãy sử dụng mã nguồn trực tiếp hoặc
artifact `python-distributions` từ một
[lần chạy CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) thành công.
Artifact này chứa tệp wheel và gói lưu trữ mã nguồn. Gói đã cài đặt cung cấp
cả lệnh `cacti-mcp` lẫn `python -m cacti_mcp`; nó không chứa
plugin PHP.

## Phát triển và kiểm thử

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Các bài kiểm thử bao gồm kiểm tra hợp lệ HTTP, cô lập thông tin xác thực, yêu cầu chỉ dùng bearer,
phân trang, ẩn thông tin nhạy cảm trong lỗi, và trao đổi thực tế giữa tiến trình con client/server SDK với
một máy chủ HTTP giả lập. Chúng không yêu cầu một bản cài đặt Cacti thực tế.

Kho lưu trữ sử dụng `src/cacti_mcp/`, pytest, Ruff, uv và Hatchling. CI kiểm thử trên
Python 3.12, 3.13 và 3.14. Một tác vụ đóng gói riêng biệt sẽ dựng tệp wheel
và gói lưu trữ mã nguồn, cài đặt wheel bên ngoài thư mục mã nguồn và kiểm tra nhanh (smoke-test)
cả hai điểm vào. Các bản phân phối và kết quả kiểm thử là artifact của workflow.

## Đóng góp

Các Pull Request gửi vào nhánh `develop`. Hãy giữ cho bộ chuyển đổi tương thích với Python 3.12,
tuân thủ cấu hình Ruff hiện có và cấu trúc gói `src/cacti_mcp/`, đồng thời
luôn dành riêng stdout cho các thông điệp MCP. Bổ sung bài kiểm thử cho các thay đổi về truyền tải hoặc
hành vi công cụ, chạy các bước kiểm tra ở trên và ký xác nhận commit bằng `git commit -s`.
Phối hợp các thay đổi API với plugin Cacti MCP và cập nhật [docs/api.md](../../../docs/api.md).

## Giấy phép

Bản quyền (C) 2026 Thomas Vincent. Phát hành theo Giấy phép Công cộng GNU
(GNU General Public License), phiên bản 2 hoặc mới hơn. Xem [LICENSE](../../../LICENSE).
