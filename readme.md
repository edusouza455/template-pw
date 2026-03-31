# Case de testes Base

Este repositório serve como um template base para projetos de automação de testes web utilizando **Python**, **Playwright** e o gerenciador de pacotes **uv**

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Playwright](https://playwright.dev/python/) (Framework de testes E2E)
- [Pytest](https://docs.pytest.org/) (Executor de testes)
- [uv](https://github.com/astral-sh/uv) (Gerenciador de pacotes e ambientes virtuais ultrarrápido)

## Pré-requisitos

Antes de começar, você precisa ter o **uv** instalado.

### Instalação do uv (Windows)
Execute o seguinte comando no PowerShell (como Administrador, se necessário):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.9.23/install.ps1 | iex"
```

> **Nota:** Para outros sistemas operacionais (macOS/Linux), consulte a [documentação oficial do uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer).

## Configuração do Projeto

1. **Clone este repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd <nome-da-pasta>
   ```

2. **Instale as dependências:**
   O `uv` criará automaticamente o ambiente virtual e instalará tudo o que está definido no `pyproject.toml`.
   ```bash
   uv sync
   ```

3. **Instale os navegadores do Playwright:**
   Necessário para rodar os testes nos motores do Chromium, Firefox e WebKit.
   ```bash
   uv run playwright install
   ```

## Executando os Testes

Como estamos usando o `uv`, sempre prefixamos os comandos com `uv run` para garantir que estamos usando o ambiente virtual do projeto.

### Execução Básica
#### Rodar todos os testes (Headless - sem interface visual)
```bash
uv run pytest
```

### Rodar com interface visual (Headed)
Útil para debugar e ver o navegador abrindo.
```bash
uv run pytest --headed
```

### Rodar em um navegador específico
```bash
uv run pytest --browser firefox
```

### Modo Slow Motion (Câmera Lenta)
Adiciona um atraso (em milissegundos) entre as ações. Ótimo para demos ou entender fluxos rápidos.
```bash
uv run pytest --headed --slowmo 1000
```

### Debug e Trace Viewer (Essencial)
O Trace Viewer é a ferramenta mais poderosa do Playwright. Ele grava vídeo, snapshots, console log e requisições de rede.

1. Gerar Trace apenas em falhas (Recomendado) Se o teste passar, nada é salvo. Se falhar, o trace é gerado na pasta test-results/
```bash
uv run pytest --tracing=retain-on-failure
```
2. Forçar Trace em todos os testes Gera o arquivo de debug independente se o teste passou ou falhou.
```bash
uv run pytest --tracing=on
```
3. Como visualizar o Trace Após rodar o teste (e se houver falha/trace gerado), use o comando abaixo apontando para o arquivo .zip criado na pasta test-results:
```bash
uv run playwright show-trace test-results/nome-da-pasta-do-teste/trace.zip
```
4. Exibir degub 
```bash
$env:PWDEBUG=1

pytest -s
```

### Filtros e Seleção

Não precisa rodar tudo toda vez. Seja específico:

### Rodar um arquivo específico
```bash
uv run pytest tests/test_login_example.py
```

#### Rodar por nome do teste (Keyword) Roda apenas os testes que contenham "login" no nome da função.
```bash
uv run pytest -k "login"
```
#### Escolher o Navegador Por padrão roda no Chromium. Para mudar:
```Bash
uv run pytest --browser firefox

```
ou

```Bash
uv run pytest --browser webkit
```
#### Execução dos Testes - *Allure*
Corre os testes e gera os ficheiros de dados na pasta results:
*EX:*

```bash
uv run pytest tests/test_login_example.py --alluredir=results
```

## Visualização do Relatório
Transforma os dados num site interativo e abre o navegador automaticamente:

```bash
allure serve results
``` 

## Manutenção de Dependências

Se precisar adicionar uma nova biblioteca (ex: `faker` para gerar dados):

```bash
uv add faker
```

Para atualizar as dependências existentes:

```bash
uv lock --upgrade
```



## Autor

Criado e desenvolvido por **Eduardo Souza**.

uv run playwright codegen https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

$env:PWDEBUG=1