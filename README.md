# 💰 Controle Financeiro em Python

Um sistema completo de controle financeiro desenvolvido em Python com integração a banco de dados SQL.
Este projeto permite o gerenciamento de receitas e despesas, oferecendo relatórios e análises para melhor controle financeiro pessoal.

---

## 📌 Sobre o Projeto

O **Controle Financeiro em Python** é uma aplicação em linha de comando (CLI) que tem como objetivo auxiliar usuários a registrarem e acompanharem suas movimentações financeiras de forma simples e eficiente.

O sistema foi desenvolvido com foco em:

* Prática de **Python**
* Integração com **banco de dados SQL**
* Uso de **bibliotecas externas**
* Aplicação de conceitos de **CRUD**
* Organização de código em módulos

---

## 🚀 Funcionalidades

### ✔️ Funcionalidades principais

* Cadastro de **receitas**
* Cadastro de **despesas**
* Listagem de movimentações
* Cálculo de saldo atual
* Organização por categorias
* Registro automático de data
* Exclusão de movimentações

---

### 📊 Funcionalidades de análise

* Total de gastos
* Total de receitas
* Saldo final
* Gastos por categoria
* Histórico completo
* Filtro por data

---

### ⭐ Funcionalidades extras (Em desenvolvimento...)

* Edição de movimentações
* Filtro por mês
* Exportação para CSV
* Geração de gráficos
* Sistema de login

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **SQLite** (banco de dados local)
* Biblioteca padrão:

  * `sqlite3`
  * `datetime`
* Bibliotecas externas:

  * `tabulate` (exibição de tabelas)
  * `matplotlib` (gráficos - opcional) - (Em desenvolvimento...)

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/controle-financeiro-python.git
cd controle-financeiro-python
```

---

### 2. Instale as dependências

```bash
pip install tabulate matplotlib
```

---

### 3. Execute o projeto

```bash
python main.py
```

---

## 🗄️ Estrutura do Projeto

```bash
controle_financeiro/
│
├── main.py               # Menu principal
├── banco.py              # Conexão com banco de dados
├── movimentacoes.py      # CRUD das movimentações
├── relatorios.py         # Funções de análise
└── financeiro.db         # Banco de dados SQLite
```

---

## 🧠 Estrutura do Banco de Dados MySQL

Tabela principal:

```sql
CREATE TABLE movimentacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    categoria TEXT NOT NULL,
    data TEXT NOT NULL
);
```

---

## 🧾 Exemplo de Uso

```text
===== CONTROLE FINANCEIRO =====

1 - Cadastrar receita
2 - Cadastrar gasto
3 - Listar movimentações
4 - Ver saldo atual
5 - Ver gastos por categoria
6 - Buscar movimentação por data
7 - Apagar movimentação COMPLETA
8- Apagar movimentação ESPECÍFICA
0 - Sair
```

---

## 📊 Exemplo de saída

```text
+----+---------+-------------+-------+-------------+------------+
| ID | Tipo    | Descrição   | Valor | Categoria   | Data       |
+----+---------+-------------+-------+-------------+------------+
| 1  | Gasto   | Lanche      | 25.00 | Alimentação | 2026/04/23 |
+----+---------+-------------+-------+-------------+------------+
```

---

## ⚠️ Validações Implementadas

* Não permite valores negativos
* Campos obrigatórios não podem ficar vazios
* Tipos válidos: Receita ou Gasto
* Validação de formato de data
* Tratamento de erros de entrada

---

## 🎯 Objetivos de Aprendizado

Este projeto foi desenvolvido com o objetivo de praticar:

* Integração com banco de dados SQL
* Manipulação de dados com Python
* Estruturação de projetos reais
* Uso de bibliotecas externas
* Boas práticas de programação

---

## 📌 Melhorias Futuras

* Interface gráfica (GUI)
* API com Flask ou FastAPI
* Autenticação de usuários
* Dashboard interativo

---

## 👨‍💻 Autor

Desenvolvido por **Kauan Ramalho de Oliveira** 🚀
[LinkedIn](https://www.linkedin.com/in/kauan-ramalho-de-oliveira-980a81346)

---
