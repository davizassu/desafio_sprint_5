# desafio_sprint_5

# 📊 Sistema de Análise e Validação de Dados

Projeto prático focado na leitura segura de arquivos, validação robusta de textos e tratamento avançado de erros em Python.

## 🧠 O que eu aprendi neste projeto

### 1. Manipulação de Arquivos e Context Managers
* **Segurança com `with open()`:** Aprendi que abrir arquivos usando a estrutura `with` garante que o arquivo será fechado automaticamente ao final do bloco, mesmo que o programa quebre no meio da leitura. Isso previne corrupção de dados e travamento do sistema operacional.
* **Leitura Estruturada:** O uso do `csv.DictReader()` facilita a manipulação de planilhas porque transforma cada linha do CSV em um dicionário, me permitindo acessar os dados pelo nome da coluna (ex: `linha['cpf']`) em vez do índice numérico.

### 2. Expressões Regulares (Regex)
* **Validação à prova de balas:** Substituí milhares de `if/else` complexos por padrões matemáticos de texto. Aprendi metacaracteres como:
  * `^` e `$` (Início e fim da string)
  * `\d` (Apenas dígitos numéricos)
  * `\w` (Caracteres alfanuméricos)
  * `\s` (Espaços em branco)
* Entendi a diferença crucial de usar `r""` (Raw Strings) no Python para que as barras invertidas do Regex não entrem em conflito com os caracteres de escape normais da linguagem (como `\n` ou `\t`).

### 3. Tratamento Avançado de Exceções (Try / Except / Else / Finally)
* **Prevenção de Quebras (Crash):** Aprendi a envolver o código "arriscado" no bloco `try`. Se um arquivo não existir, o sistema não desliga bruscamente, ele é capturado pelo `except FileNotFoundError`.
* **Classes de Erro Customizadas:** Criei minha própria exceção, `FormatoInvalidoError`, herdando da classe base `Exception`. Isso me permite separar erros lógicos do meu negócio (como um CPF sem ponto) de erros nativos da linguagem.
* **O Fluxo Completo:** Compreendi que o bloco `else` só roda se tudo der certo no `try`, e que o `finally` é invencível — ele sempre rodará no final, servindo como uma "vassoura" para limpar a memória ou fechar conexões com bancos de dados.
