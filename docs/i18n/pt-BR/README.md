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

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · [Français](../fr/README.md) · [Italiano](../it/README.md) · **Português (BR)** · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

O Cacti MCP é um adaptador em Python que expõe as capacidades do
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) como ferramentas
MCP via stdio. O plugin já serve MCP diretamente por HTTP, portanto use essa opção
quando o cliente puder se conectar a um servidor remoto. Este adaptador é voltado para
clientes que falam apenas stdio. Ele usa o SDK oficial de MCP para Python e
traduz chamadas de ferramentas para a API HTTPS do plugin (contrato de capacidades v2,
servido em caminhos `/v1/`, somente via token bearer).
O Cacti é responsável pela autenticação, autorização, validação e execução.

**Status: em desenvolvimento, anterior à versão 1.0.** A versão 0.1.0 oferece suporte a inventário de dispositivos
somente leitura e versões da instalação por meio do
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) complementar.
Ainda não há uma release com tag. Diagnósticos e reparos do comando doctor são trabalhos futuros.

## O que ele expõe

| Operação | Ferramenta MCP fornecida pelo plugin Cacti MCP |
|---|---|
| Listar os dispositivos que o titular do token pode ver | `cacti-list-devices` |
| Ler um dispositivo permitido | `cacti-get-device` |
| Ler versões do Cacti, do plugin e da API | `cacti-get-system-info` |

Os nomes, as descrições e os esquemas de entrada vêm da resposta de descoberta
filtrada por permissões do Cacti. Provedores adicionais permitidos e somente leitura
podem ser descobertos sem adicionar handlers de ferramentas em Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Casos de uso

Conecte um cliente MCP para listar os dispositivos do Cacti que seu usuário dedicado pode ver,
consultar um dispositivo permitido ou obter versões da instalação quando o usuário
possuir o realm administrativo necessário. Os nomes e os esquemas de entrada vêm da
resposta de descoberta do plugin, portanto o adaptador não duplica cada provedor.
Consulte as
[regras de registro de capacidades](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
do plugin para ver o modelo de registro e os limites atuais.

## Mapa de código e testes

| Comportamento | Implementação | Evidência de testes neste repositório |
|---|---|---|
| Validação HTTPS, limites, autenticação somente via bearer e paginação v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Descoberta MCP, chamadas e alterações de permissão | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Ajuda da linha de comando, versão e configuração ausente | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

O teste com subprocesso usa um cliente e um servidor reais do SDK com um endpoint HTTP
de fixture. Ele não exige nem substitui uma verificação de integração com um Cacti em produção.

## Como ele se mantém seguro

- Usa o [SDK oficial `mcp` para Python](https://github.com/modelcontextprotocol/python-sdk)
  para inicialização, descoberta de ferramentas, chamadas e enquadramento stdio.
- Expõe apenas capacidades cujas anotações sejam exatamente somente leitura, não destrutivas e idempotentes. Os esquemas e nomes vêm
  do Cacti; o adaptador não contém SQL, credenciais de dispositivos nem comandos de reparo.
- Envia apenas o token bearer: sem cookies, sem etapa de CSRF. O plugin verifica novamente
  a validade do token e as permissões a cada requisição.
- Usa HTTPS verificado, nunca armazena cookies, recusa redirecionamentos e
  ignora variáveis de ambiente de proxy. HTTP exige `--allow-loopback-http`
  e um endereço loopback literal ou `localhost`.
- Limita as chamadas à API a 35 segundos no total, 5 segundos para conectar, 30 segundos de
  inatividade de rede e aproximadamente 1 MB por resposta (1.100.000 bytes).
  Corpos de requisição são limitados a 16.384 bytes. As chamadas são serializadas por sessão
  de cliente.
- Verifica os argumentos da ferramenta em relação ao esquema de entrada da última descoberta antes de
  enviá-los e executa apenas IDs desse catálogo verificado. Uma incompatibilidade, ou
  um esquema malformado vindo do servidor, retorna como um erro da ferramenta, e não como uma falha crítica.
- Não repete a execução automaticamente. Erros de ferramenta carregam apenas o status
  HTTP, o `status` da AIP-193 e o `reason` de ErrorInfo; nunca o texto da
  mensagem do servidor, corpos de resposta ou credenciais. A saída stdout é reservada para mensagens MCP.

A versão do SDK é fixada em `uv.lock` (`mcp>=2.3,<3` em `pyproject.toml`). Este
adaptador usa seu servidor de baixo nível 2.x com o transporte stdio; ele não
implementa um endpoint HTTP MCP remoto, OAuth, resources,
prompts, subscriptions ou tarefas em segundo plano.

Veja [o contrato da API](../../../docs/api.md) e [o plano de implementação](../../../docs/plan.md).

## Instalação e linha de comando

Requer Python 3.12 ou posterior e [uv](https://docs.astral.sh/uv/).
A partir de um clone deste repositório:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Instale e habilite o plugin PHP, conceda o realm correspondente a um usuário dedicado do Cacti
e crie um token de acesso pessoal para esse usuário (formato `cmcp_pat_` seguido
de 64 dígitos hexadecimais minúsculos) no console do plugin, na página My MCP Tokens
ou com o comando `tokens.php`.
Os realms e as permissões de dispositivos existentes do usuário no Cacti continuam sendo aplicados.

Forneça o token por meio do seu gerenciador de segredos como `CACTI_MCP_TOKEN`; nunca o adicione
ao controle de versão nem a argumentos de linha de comando. Defina o endpoint separadamente. Ele deve ser uma
URL HTTPS terminada em `/plugins/mcp/api.php`, sem credenciais, query nem
fragmento:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` define o endpoint no lugar de `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` permite HTTP simples para `localhost`, `127.0.0.1` ou `::1`
para testes locais, `--lang LOCALE` substitui a localização das mensagens da CLI e
`--version` imprime a versão. Sem o endpoint e `CACTI_MCP_TOKEN`,
o comando encerra com um erro de uso.

### Localização

A ajuda da CLI e as mensagens de erro do adaptador são distribuídas em 45 idiomas (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) sem dependências adicionais. A resolução
de localidade verifica `--lang`, depois `LC_ALL`, `LC_MESSAGES` e `LANG`, recorrendo
a `en` como padrão (`C`/`POSIX` e tags desconhecidas também resolvem para `en`). Nomes de ferramentas
MCP, esquemas e payloads JSON bem-sucedidos das ferramentas não são afetados; mensagens de erro do
adaptador retornadas com `is_error=True` seguem a localidade ativa.

O processo aguarda mensagens MCP na entrada stdin. Normalmente, um cliente MCP o inicia.
Para clientes que aceitam o formato de configuração comum `mcpServers`:

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

Configure o cliente para passar `CACTI_MCP_ENDPOINT` e `CACTI_MCP_TOKEN` ao
subprocesso por meio de seu ambiente ou recurso de segredos. A herança de ambiente
depende do cliente. Não há flag de linha de comando para o token.

A distribuição Python instalável separadamente fornece o comando de console `cacti-mcp`.
Não é necessária publicação no PyPI para executar a partir do clone. O plugin PHP não tem
dependência de Python.

## Lançamentos

A versão da distribuição está registrada em [pyproject.toml](../../../pyproject.toml).
Até que haja lançamentos com tag disponíveis, use um clone do código-fonte ou o
artefato `python-distributions` de uma
[execução bem-sucedida de CI](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
O artefato contém um wheel e um pacote de código-fonte. O pacote instalado fornece
tanto o comando `cacti-mcp` quanto `python -m cacti_mcp`; ele não contém o
plugin PHP.

## Desenvolvimento e testes

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Os testes cobrem validação HTTP, isolamento de credenciais, requisições somente via bearer,
paginação, ocultação de dados sensíveis em erros e uma troca real entre cliente e servidor do SDK via subprocesso contra
um servidor HTTP de fixture. Eles não exigem uma instalação ativa do Cacti.

O repositório usa `src/cacti_mcp/`, pytest, Ruff, uv e Hatchling. A CI testa
Python 3.12, 3.13 e 3.14. Um job de empacotamento separado compila o wheel
e o pacote de código-fonte, instala o wheel fora do clone e executa smoke tests
nos dois pontos de entrada. Distribuições e resultados de testes são artefatos do workflow.

## Contribuição

Pull requests vão para `develop`. Mantenha o adaptador compatível com Python 3.12,
siga a configuração existente do Ruff e a estrutura de pacote `src/cacti_mcp/`, e
mantenha stdout reservado para mensagens MCP. Adicione testes para alterações de comportamento no transporte ou nas ferramentas,
execute as verificações acima e assine os commits com `git commit -s`.
Coordene alterações de API com o plugin Cacti MCP e atualize [docs/api.md](../../../docs/api.md).

## Licença

Copyright (C) 2026 Thomas Vincent. Distribuído sob a GNU General Public
License, versão 2 ou posterior. Consulte [LICENSE](../../../LICENSE).
