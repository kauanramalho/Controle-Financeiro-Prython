from datetime import datetime
from tabulate import tabulate 
movimentacoes = []
categoria = 0

def cadastrar_movimentacoes(tipo):
    
    print("--------------------")
    print('Categoria')
    print('1 - Alimentação')
    print('2 - Transporte')
    print('3 - Lazer')
    print('4 - Contas')
    print("--------------------")
    
    try:
        categoria_opcoes = int(input('-> Selecione Categoria: '))
    except ValueError:
        print('Digite apenas Numeros interios.')
        return
    
    if categoria_opcoes == 1:
        categoria = "Alimentação"
    elif categoria_opcoes == 2:
        categoria = "Transporte"
    elif categoria_opcoes == 3:
        categoria = "Lazer"
    elif categoria_opcoes == 4:
        categoria = "Contas"
    else:
        print('Opação invalida!')
        return

    descricao = str(input('-> Descrição de gasto: '))
    while descricao == "":
        print('Insira uma Descrição!')
        descricao = str(input('-> Descrição de gasto: '))
        
    try:
        valor = float(input('-> Valor: ').replace(",","."))
    except ValueError:
        print('"Valor invalido. Digite apenas números!') 
        return
    
    while valor < 0:
        print('Valores NEGATIVOS não são permitidos')
        print('Digite valores >= 0')
        valor = float(input('-> Valor: '))
    
    data = str(input('-> Insira a data (dd/mm/aa): '))
    if data == "":
        data = datetime.now().strftime("%d/%m/%Y")

    movimentacoes.append({"tipo": tipo,
                         "descricao": descricao,
                         "valor": valor,
                         "categoria": categoria, 
                         "data": data})
    
def listar_movimentacoes():
    tabela = [] #Tabela para organizar os dados brutos da lista movimentacoes
    for i, m in enumerate(movimentacoes, start=1):
        tabela.append([
                        i,
                        m["tipo"],
                        m["descricao"],
                        f'{m["valor"]:.2f}',
                        m["categoria"],
                        m["data"]
        ])

        cabecalho = ["ID", "Tipo", "Descrição", "Valor", "Categoria", "Data"]

    print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))
    # usa a biblioteca tabulate para exibir a tabela
    # tabela = dados (linhas)
    # headers = nomes das colunas
    # tablefmt = define o formato visual da tabela

def ver_saldo():
    total_receita = 0
    total_gasto = 0

    for m in movimentacoes:
        if m["tipo"] == "Receita":
            m["tipo"] += m["valor"]

        elif m["tipo"] == "Gastos":
            m["tipo"] += m["valor"]

        else:
            print(f'Tipo invalido encontrado: {m["tipo"] ', Valor:' m["valor"]}')

    saldo = total_receita - total_gasto

    print(f'Valor de Receita Total: {total_receita:.2f}')
    print(f'Valor de Gasto Total: {total_gasto:.2f}')
    print(f'Saldo Total Restante: {saldo:.2f}')

    
def saldo_cadegoria():
    pass
def movimentacao_data():
    pass
    
    print('CADASTRO SALVO!')


