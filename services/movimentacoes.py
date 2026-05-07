from datetime import datetime

from tabulate import tabulate

from db.conexao import conexao, cursor


def formatar_data_para_banco(data_texto):
    return datetime.strptime(data_texto, "%d-%m-%Y").strftime("%Y-%m-%d")


def formatar_data_para_exibicao(data_valor):
    if isinstance(data_valor, str):
        try:
            data_valor = datetime.strptime(data_valor, "%Y-%m-%d")
        except ValueError:
            return data_valor

    return data_valor.strftime("%d-%m-%Y")


def cadastrar_movimentacoes(tipo):
    print("--------------------")
    print("Categoria")
    print("1 - Alimentacao")
    print("2 - Transporte")
    print("3 - Lazer")
    print("4 - Contas")
    print("--------------------")

    try:
        categoria_opcoes = int(input("-> Selecione Categoria: "))
    except ValueError:
        print("Digite apenas numeros inteiros.")
        return

    if categoria_opcoes == 1:
        categoria = "Alimentacao"
    elif categoria_opcoes == 2:
        categoria = "Transporte"
    elif categoria_opcoes == 3:
        categoria = "Lazer"
    elif categoria_opcoes == 4:
        categoria = "Contas"
    else:
        print("Opcao invalida!")
        return

    descricao = input("-> Descricao: ")

    while descricao == "":
        print("Insira uma descricao!")
        descricao = input("-> Descricao: ")

    try:
        valor = float(input("-> Valor: ").replace(",", "."))
    except ValueError:
        print("Valor invalido. Digite apenas numeros!")
        return

    while valor < 0:
        print("Valores negativos nao sao permitidos.")
        print("Digite valores >= 0")
        try:
            valor = float(input("-> Valor: ").replace(",", "."))
        except ValueError:
            print("Valor invalido. Digite apenas numeros!")
            return

    data = input("-> Insira a data (dd-mm-yyyy): ").strip()

    if data == "":
        data = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            data = formatar_data_para_banco(data)
        except ValueError:
            print("Data invalida. Use o formato dd-mm-yyyy.")
            return

    sql = """
INSERT INTO movimentacoes
(tipo, descricao, valor, categoria, data_movimentacao)
VALUES (%s, %s, %s, %s, %s)
"""

    valores = (tipo, descricao, valor, categoria, data)

    cursor.execute(sql, valores)
    conexao.commit()

    print("\nCADASTRO SALVO!")


def listar_movimentacao():
    cursor.execute("SELECT * FROM movimentacoes")
    dados = cursor.fetchall()

    if not dados:
        print("Nenhuma movimentacao cadastrada.")
        return

    cabecalho = ["ID", "Tipo", "Descricao", "Valor(R$)", "Categoria", "Data"]
    tabela = []

    for m in dados:
        tabela.append([
            m[0],
            m[1],
            m[2],
            f"R${m[3]:.2f}",
            m[4],
            formatar_data_para_exibicao(m[5]),
        ])

    print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))


def ver_saldo():
    cursor.execute("SELECT * FROM movimentacoes")
    dados = cursor.fetchall()

    total_receita = 0
    total_gasto = 0

    for m in dados:
        if m[1] == "Receita":
            total_receita += m[3]
        elif m[1] == "Gastos":
            total_gasto += m[3]
        else:
            print(f"Tipo invalido encontrado: {m[1]}, Valor: {m[2]}")

    saldo = total_receita - total_gasto

    print(f"\n-> Valor de Receita Total: R${total_receita:.2f}")
    print(f"-> Valor de Gasto Total: R${total_gasto:.2f}")

    if saldo > 0:
        print(f"-> SALDO TOTAL RESTANTE: R${saldo:.2f}\n")
    else:
        print("CUIDADO com seu planejamento, seu saldo esta NEGATIVO!")
        print(f"-> SALDO NEGATIVO TOTAL : R${saldo:.2f}\n")


def gasto_categoria():
    cursor.execute("""
        SELECT categoria, SUM(valor)
        FROM movimentacoes
        WHERE tipo = 'Gastos'
        GROUP BY categoria
    """)

    resultados = cursor.fetchall()

    if not resultados:
        print("Nenhum gasto registrado.")
        return

    for categoria, total in resultados:
        print(f"{categoria}: R${total:.2f}")


def movimentacao_data():
    data_busca = input("Digite a data que deseja encontrar (dd-mm-yyyy): ").strip()

    if not data_busca:
        print("A data nao pode ser vazia.")
        return

    try:
        data_busca_banco = formatar_data_para_banco(data_busca)
    except ValueError:
        print("Data invalida. Use o formato dd-mm-yyyy.")
        return

    cursor.execute(
        "SELECT * FROM movimentacoes WHERE data_movimentacao = %s",
        (data_busca_banco,),
    )
    resultado = cursor.fetchall()

    if not resultado:
        print(f"Data {data_busca} nao foi encontrada.\n")
        return

    cabecalho = ["ID", "Tipo", "Descricao", "Valor", "Categoria", "Data"]
    tabela = []

    for m in resultado:
        tabela.append([
            m[0],
            m[1],
            m[2],
            f"R${m[3]:.2f}",
            m[4],
            formatar_data_para_exibicao(m[5]),
        ])

    print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))


def apagar_movimentacoes_completas():
    cursor.execute("SELECT COUNT(*) FROM movimentacoes")
    total_registros = cursor.fetchone()[0]

    if total_registros == 0:
        print("Nenhuma movimentacao cadastrada para apagar.")
        return

    confirmacao = input(
        "Tem certeza que deseja apagar TODAS as movimentacoes? (S/N): "
    ).strip().upper()

    if confirmacao != "S":
        print("Operacao cancelada.")
        return

    cursor.execute("DELETE FROM movimentacoes")
    cursor.execute("ALTER TABLE movimentacoes AUTO_INCREMENT = 1")
    conexao.commit()

    print(f"{total_registros} movimentacao(oes) apagada(s) com sucesso.")

def apagar_movimentacoes_expecificas():
    try:
        id_movimentacao = int(input("Digite o ID da movimentacao que deseja apagar: "))
    except ValueError:
        print("Digite um ID numerico valido.")
        return

    cursor.execute(
        "SELECT id, tipo, descricao, valor, categoria, data_movimentacao "
        "FROM movimentacoes WHERE id = %s",
        (id_movimentacao,),
    )
    movimentacao = cursor.fetchone()

    if not movimentacao:
        print(f"Nenhuma movimentacao foi encontrada com o ID {id_movimentacao}.")
        return

    print("\nMovimentacao encontrada:")
    tabela = [[
        movimentacao[0],
        movimentacao[1],
        movimentacao[2],
        f"R${movimentacao[3]:.2f}",
        movimentacao[4],
        formatar_data_para_exibicao(movimentacao[5]),
    ]]
    cabecalho = ["ID", "Tipo", "Descricao", "Valor", "Categoria", "Data"]
    print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))

    confirmacao = input("Confirmar exclusao desta movimentacao? (S/N): ").strip().upper()

    if confirmacao != "S":
        print("Operacao cancelada.")
        return

    cursor.execute("DELETE FROM movimentacoes WHERE id = %s", (id_movimentacao,))
    conexao.commit()

    print("Movimentacao apagada com sucesso.")
