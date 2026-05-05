from db.conexao import cursor, conexao

from datetime import datetime
from tabulate import tabulate 

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

    descricao = str(input('-> Descrição: '))
    
    while descricao == "":
        print('Insira uma Descrição!')
        descricao = str(input('-> Descrição: '))
        
    try:
        valor = float(input('-> Valor: ').replace(",","."))
    except ValueError:
        print('"Valor invalido. Digite apenas números!') 
        return
    
    while valor < 0:
        print('Valores NEGATIVOS não são permitido.')
        print('Digite valores >= 0')
        valor = float(input('-> Valor: '))
    
    data = str(input('-> Insira a data (dd/mm/yyyy): '))
    if data == "":
        data = datetime.now().strftime("%d-%m-%Y") 
        #Atribui a Data de Hoje se data ficar vazia
    
    print('\nCADASTRO SALVO!')

    sql = """
INSERT INTO movimentacoes
(tipo, descricao, valor, categoria, data_movimentacao)
VALUES (%s, %s, %s, %s, %s)
"""

    valores = (tipo, descricao, valor, categoria, data)

    cursor.execute(sql, valores)
    conexao.commit()
    
def listar_movimentacao():
    cursor.execute("SELECT * FROM movimentacoes") #Busca no Banco SQL
    dados = cursor.fetchall() # Pega os resultados no banco SQL
    
    tabela = [] #Tabela para organizar os dados brutos da lista movimentacoes
    for i, m in enumerate(dados, start = 1):
        tabela.append([
                        m[0],
                        m[1],
                        m[2],
                        f'R${m[3]:.2f}',
                        m[4],
                        m[5]
        ])

        cabecalho = ["ID", "Tipo", "Descrição", "Valor(R$)", "Categoria", "Data"]

    print(tabulate(tabela, headers=cabecalho, tablefmt="grid"))
    # usa a biblioteca tabulate para exibir a tabela
    # tabela = dados (linhas)
    # headers = nomes das colunas
    # tablefmt = define o formato visual da tabela

def ver_saldo():
    cursor.execute("SELECT * FROM movimentacoes")
    dados = cursor.ferchall()
    
    total_receita = 0
    total_gasto = 0

    for m in dados:
        if m[1] == "Receita":
            total_receita += m[3] 

        elif m[1] == "Gastos":
            total_gasto += m[3] 

        else:
            print(f'Tipo invalido encontrado: {m[1]}, Valor: {m[2]}')

    saldo = total_receita - total_gasto

    print(f'\n-> Valor de Receita Total: R${total_receita:.2f}')
    print(f'-> Valor de Gasto Total: R${total_gasto:.2f}')
    
    if saldo > 0:
        print(f'-> SALDO TOTAL RESTANTE: R${saldo:.2f}\n')

    else:
        print(f'CUIDADO com seu planejamento, seu saldo esta NEGATIVO!')
        print(f'-> SALDO NEGATIVO TOTAL : R${saldo:.2f}\n')
     
def gasto_cadegoria():
    cursor.execute("""
        SELECT categoria, SUM(valor)
        FROM movimentacoes
        WHERE tipo = 'Gastos'
        GROUP BY categoria
    """)# Pega os resultados no banco SQL

    resultados = cursor.fetchall() # Pega os resultados no banco SQL

    if not resultados:
        print("Nenhum gasto registrado.")
        return

    for categoria, total in resultados:
        print(f"{categoria}: R${total:.2f}")

    
def movimentacao_data():
    data_busca = str(input('Digite a data que deseja encotrar: (dd/mm/yyyy): '))

    if not data_busca: #Verifica se o input do usuário esta Vazio.
        print('A data nao pode ser vazia.')
        return
    
    resultado = []

    if data_busca == m[5]:
        resultado.append(m)

    if not resultado:
        print(f'Data {data_busca} nao foi encontrada.\n')
        return

    tabela = []
    # percorre resultado gerando numero de linha (i) e a movimentacao (m), contador começa em 1
    for i, m in enumerate(resultado, start = 1):
        tabela.append([
                        i,
                        m[1],
                        m[2],
                        f'R${m[3]:.2f}',
                        m[4],
                        m[5]
        ])
        
        cabecalho = ["ID", "Tipo", "Descrição", "Valor", "Categoria", "Data"]
    
    print(tabulate(tabela, headers = cabecalho, tablefmt ="grid"))   
        

    


