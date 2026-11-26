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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · **Español** · [Français](../fr/README.md) · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP es un adaptador en Python que expone las capacidades del
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) como herramientas
MCP sobre stdio. El plugin ya sirve MCP sobre HTTP directamente, así que úsalo
cuando tu cliente pueda conectarse a un servidor remoto. Este adaptador es para
clientes que solo hablan stdio. Utiliza el SDK oficial de MCP para Python y
traduce las llamadas a herramientas a la API HTTPS del plugin (contrato de capacidades v2,
servido bajo rutas `/v1/`, únicamente con bearer token).
Cacti se encarga de la autenticación, la autorización, la validación y la ejecución.

**Estado: en desarrollo, previo a la versión 1.0.** La versión 0.1.0 admite el inventario
de dispositivos de solo lectura y las versiones de instalación a través del
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) complementario.
Todavía no hay una versión etiquetada. Los diagnósticos tipo doctor y las reparaciones quedan para trabajo futuro.

## Qué expone

| Operación | Herramienta MCP proporcionada por el plugin Cacti MCP |
|---|---|
| Listar los dispositivos que el propietario del token puede ver | `cacti-list-devices` |
| Leer un dispositivo permitido | `cacti-get-device` |
| Leer las versiones de Cacti, del plugin y de la API | `cacti-get-system-info` |

Los nombres, las descripciones y los esquemas de entrada provienen de la respuesta de descubrimiento
filtrada por permisos de Cacti. Se pueden descubrir proveedores adicionales de solo lectura
permitidos sin añadir manejadores de herramientas en Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Casos de uso

Conecta un cliente MCP para listar los dispositivos de Cacti que su usuario dedicado puede ver,
consultar un dispositivo permitido u obtener las versiones de la instalación cuando el usuario
tiene el dominio administrativo requerido. Los nombres y los esquemas de entrada provienen de
la respuesta de descubrimiento del plugin, por lo que el adaptador no duplica cada proveedor.
Consulta las
[reglas de registro de capacidades](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
del plugin para ver el modelo de registro y los límites actuales.

## Mapa de código y pruebas

| Comportamiento | Implementación | Evidencia de pruebas en este repositorio |
|---|---|---|
| Validación HTTPS, límites, autenticación solo por bearer y paginación v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Descubrimiento MCP, llamadas y cambios de permisos | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Ayuda de línea de comandos, versión y configuración faltante | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

La prueba de subproceso utiliza un cliente y un servidor reales del SDK con un punto de enlace HTTP
de prueba. No requiere ni sustituye a una comprobación de integración contra un Cacti en vivo.

## Cómo se mantiene seguro

- Utiliza el [SDK oficial de Python para `mcp`](https://github.com/modelcontextprotocol/python-sdk)
  para la inicialización, el descubrimiento de herramientas, las llamadas y el entramado stdio.
- Expone únicamente capacidades cuyas anotaciones son exactamente de solo lectura, no destructivas e idempotentes. Los esquemas y nombres provienen
  de Cacti; el adaptador no contiene SQL, credenciales de dispositivos ni comandos de reparación.
- Envía solo el bearer token: sin cookies y sin paso CSRF. El plugin vuelve a comprobar
  la validez del token y los permisos en cada solicitud.
- Utiliza HTTPS verificado, nunca almacena cookies, rechaza redirecciones e
  ignora las variables de entorno de proxy. HTTP requiere `--allow-loopback-http`
  y una dirección loopback literal o `localhost`.
- Limita las llamadas a la API a 35 segundos en total, 5 segundos para conectar, 30 segundos de
  inactividad de red y aproximadamente 1 MB por respuesta (1,100,000 bytes).
  Los cuerpos de solicitud están limitados a 16,384 bytes. Las llamadas se serializan por sesión
  de cliente.
- Comprueba los argumentos de las herramientas contra el esquema de entrada del último descubrimiento antes
  de enviarlos, y ejecuta solo identificadores de ese catálogo verificado. Una discrepancia, o
  un esquema mal formado del servidor, se devuelve como un error de herramienta, no como un fallo inesperado.
- No reintenta la ejecución automáticamente. Los errores de herramienta solo incluyen el estado
  HTTP, el `status` de AIP-193 y la `reason` de ErrorInfo; nunca el texto del mensaje del
  servidor, los cuerpos de respuesta ni las credenciales. Stdout está reservado para los mensajes MCP.

La versión del SDK está fijada en `uv.lock` (`mcp>=2.3,<3` en `pyproject.toml`). Este
adaptador utiliza su servidor de bajo nivel 2.x con el transporte stdio; no
implementa un punto de enlace HTTP MCP remoto, OAuth, recursos,
prompts, suscripciones ni tareas en segundo plano.

Consulta [el contrato de la API](../../../docs/api.md) y el [plan de implementación](../../../docs/plan.md).

## Instalación y línea de comandos

Requiere Python 3.12 o posterior y [uv](https://docs.astral.sh/uv/).
Desde una copia local de este repositorio:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Instala y habilita el plugin PHP, concede su dominio a un usuario dedicado de Cacti
y crea un token de acceso personal para ese usuario (formato `cmcp_pat_` seguido
de 64 dígitos hexadecimales en minúsculas) en la consola del plugin, en su página My MCP Tokens
o con su comando `tokens.php`.
Los dominios de Cacti y permisos de dispositivos existentes del usuario siguen aplicándose.

Proporciona el token a través de tu gestor de secretos como `CACTI_MCP_TOKEN`; nunca lo añadas
al control de versiones ni a los argumentos de línea de comandos. Configura el punto de enlace por separado. Debe ser una
URL HTTPS que termine en `/plugins/mcp/api.php`, sin credenciales, consulta ni
fragmento:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` establece el punto de enlace en lugar de `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` permite HTTP plano hacia `localhost`, `127.0.0.1` o `::1`
para pruebas locales, `--lang LOCALE` sobrescribe la localización de mensajes de la CLI y
`--version` imprime la versión. Sin tanto el punto de enlace como `CACTI_MCP_TOKEN`,
el comando finaliza con un error de uso.

### Localización

La ayuda de la CLI y los mensajes de error del adaptador se distribuyen en 45 configuraciones regionales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) sin dependencias adicionales. La resolución
de configuración regional comprueba `--lang`, luego `LC_ALL`, `LC_MESSAGES` y `LANG`, recurriendo
a `en` (`C`/`POSIX` y las etiquetas desconocidas también se resuelven a `en`). Los nombres de herramientas
MCP, los esquemas y las cargas útiles JSON exitosas de las herramientas no se ven afectados; los mensajes de error
del adaptador devueltos con `is_error=True` siguen la configuración regional activa.

El proceso espera mensajes MCP en stdin. Normalmente lo inicia un cliente MCP.
Para clientes que aceptan el formato de configuración habitual `mcpServers`:

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

Configura el cliente para pasar `CACTI_MCP_ENDPOINT` y `CACTI_MCP_TOKEN` al
subproceso mediante su entorno o sistema de secretos. La herencia del entorno
depende del cliente. No existe ninguna opción de línea de comandos para el token.

La distribución de Python instalable por separado proporciona el comando de consola
`cacti-mcp`. No se requiere publicación en PyPI para ejecutar la copia del repositorio. El plugin PHP no
tiene dependencias de Python.

## Versiones

La versión de la distribución está registrada en [pyproject.toml](../../../pyproject.toml).
Hasta que haya versiones etiquetadas disponibles, usa una copia del código fuente o el
artefacto `python-distributions` de una
[ejecución de CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml) exitosa.
El artefacto contiene un wheel y un archivo de código fuente. El paquete instalado proporciona
tanto el comando `cacti-mcp` como `python -m cacti_mcp`; no contiene el
plugin PHP.

## Desarrollo y pruebas

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Las pruebas cubren la validación HTTP, el aislamiento de credenciales, las solicitudes solo con bearer,
la paginación, la censura de errores y un intercambio real de subproceso cliente/servidor del SDK contra
un servidor HTTP de prueba. No requieren una instalación de Cacti en vivo.

El repositorio utiliza `src/cacti_mcp/`, pytest, Ruff, uv y Hatchling. La CI prueba
Python 3.12, 3.13 y 3.14. Un trabajo de empaquetado separado compila el wheel
y el archivo de código fuente, instala el wheel fuera de la copia del repositorio y realiza pruebas básicas
en ambos puntos de entrada. Las distribuciones y los resultados de las pruebas son artefactos del flujo de trabajo.

## Contribución

Los pull requests van a `develop`. Mantén el adaptador compatible con Python 3.12,
sigue la configuración existente de Ruff y la estructura de paquetes `src/cacti_mcp/`, y
mantén stdout reservado para los mensajes MCP. Añade pruebas para cualquier cambio en el transporte o en las
herramientas, ejecuta las comprobaciones anteriores y firma los commits con `git commit -s`.
Coordina los cambios de la API con el plugin Cacti MCP y actualiza [docs/api.md](../../../docs/api.md).

## Licencia

Copyright (C) 2026 Thomas Vincent. Publicado bajo la Licencia Pública General de GNU,
versión 2 o posterior. Consulta [LICENSE](../../../LICENSE).
