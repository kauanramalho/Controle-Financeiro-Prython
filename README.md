# Controle Financeiro em Python

Aplicacao de terminal para registrar receitas e gastos, consultar saldo, listar movimentacoes e apagar registros salvos em um banco MySQL.

## O que o projeto faz hoje

O sistema exibe um menu interativo no terminal com as opcoes abaixo:

1. Cadastrar receita
2. Cadastrar gasto
3. Listar movimentacoes
4. Ver saldo atual
5. Ver gastos por categorias
6. Buscar movimentacao por data
7. Apagar todas as movimentacoes
8. Apagar uma movimentacao especifica por ID
0. Encerrar o programa

## Tecnologias usadas

- Python
- MySQL
- `mysql-connector-python`
- `tabulate`

## Estrutura atual do projeto

```text
Controle -Financeiro-Python/
|- main.py
|- db/
|  |- conexao.py
|- services/
|  |- movimentacoes.py
|- database/
|  |- Controle_financeiro MySQL.sql
```

## Como o fluxo funciona

- `main.py` mostra o menu principal e chama as funcoes da camada de servicos.
- `services/movimentacoes.py` concentra as operacoes de cadastro, consulta, saldo e exclusao.
- `db/conexao.py` abre a conexao com o MySQL.
- `database/Controle_financeiro MySQL.sql` cria o banco e a tabela usados pelo sistema.

## Pre-requisitos

Antes de executar o projeto, voce precisa ter:

- Python instalado
- MySQL instalado e em execucao
- Um banco chamado `controle_financeiro`

## Configuracao do banco de dados

Execute o script SQL abaixo no MySQL:

Arquivo: [`database/Controle_financeiro MySQL.sql`](./database/Controle_financeiro%20MySQL.sql)

Esse script cria:

- o banco `controle_financeiro`
- a tabela `movimentacoes`

## Configuracao da conexao

Atualmente a conexao com o banco esta definida diretamente no arquivo:

[`db/conexao.py`](./db/conexao.py)

Os campos usados hoje sao:

- `host="localhost"`
- `user="root"`
- `password="..."`
- `database="controle_financeiro"`

Se os dados do seu MySQL forem diferentes, ajuste esse arquivo antes de rodar.

## Instalacao das dependencias

Instale as bibliotecas usadas no projeto:

```bash
pip install mysql-connector-python tabulate
```

## Como executar

No terminal, dentro da pasta do projeto, rode:

```bash
python main.py
```

## Regras e comportamentos atuais

- A descricao da movimentacao nao pode ficar vazia.
- O valor aceita virgula ou ponto e nao permite numeros negativos.
- Se a data nao for informada no cadastro, o sistema usa a data atual.
- Os gastos por categoria sao somados apenas quando o tipo da movimentacao e `Gastos`.
- A exclusao total pede confirmacao antes de apagar tudo.
- A exclusao individual busca a movimentacao por ID e pede confirmacao antes de remover.

## Categorias disponiveis hoje

O cadastro usa estas categorias:

- Alimentacao
- Transporte
- Lazer
- Contas

## Observacoes importantes

- O projeto hoje e um sistema de terminal, sem interface grafica.
- O README anterior nao estava presente no workspace atual; este arquivo foi refeito com base no codigo existente.
- O proprio codigo ja indica uma melhoria futura: receitas e gastos ainda compartilham o mesmo bloco de categorias.
- As credenciais do banco estao fixas no codigo, o que funciona para estudo local, mas nao e o ideal para producao.

## Melhorias futuras sugeridas

- Separar categorias de receitas e gastos
- Mover credenciais do banco para variaveis de ambiente
- Criar um arquivo `requirements.txt`
- Adicionar validacao de data
- Criar testes automatizados
- Adicionar `.gitignore` para evitar versionar arquivos `__pycache__`

## Autor

Projeto de Kauan Ramalho.
