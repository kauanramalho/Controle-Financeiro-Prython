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
        data = datetime.now().strftime("%d/%m/%Y") 
        #Atribui a Data de Hoje se data ficar vazia
    
    print('\nCADASTRO SALVO!')

    movimentacoes.append({"tipo": tipo,
                         "descricao": descricao,
                         "valor": valor,
                         "categoria": categoria, 
                         "data": data})
    
def listar_movimentacao():
    tabela = [] #Tabela para organizar os dados brutos da lista movimentacoes
    for i, m in enumerate(movimentacoes, start = 1):
        tabela.append([
                        i,
                        m["tipo"],
                        m["descricao"],
                        f'R${m["valor"]:.2f}',
                        m["categoria"],
                        m["data"]
        ])

        cabecalho = ["ID", "Tipo", "Descrição", "Valor(R$)", "Categoria", "Data"]

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
            total_receita += m["valor"] 

        elif m["tipo"] == "Gastos":
            total_gasto += m["valor"] 

        else:
            print(f'Tipo invalido encontrado: {m["tipo"]}, Valor: {m["valor"]}')

    saldo = total_receita - total_gasto

    print(f'\n-> Valor de Receita Total: R${total_receita:.2f}')
    print(f'-> Valor de Gasto Total: R${total_gasto:.2f}')
    
    if saldo > 0:
        print(f'-> SALDO TOTAL RESTANTE: R${saldo:.2f}\n')

    else:
        print(f'CUIDADO com seu planejamento, seu saldo esta NEGATIVO!')
        print(f'-> SALDO NEGATIVO TOTAL : R${saldo:.2f}\n')
   

    
def gasto_cadegoria():
    gasto_alimentacao = 0
    gasto_transporte = 0
    gasto_lazer = 0
    gasto_contas = 0
   
    for m in movimentacoes:
        if m["tipo"] != "Gastos":
            continue

        if m["categoria"] == "Alimentação": 
            gasto_alimentacao += m["valor"]

        elif m["categoria"] == "Transporte":
            gasto_transporte += m["valor"]

        elif m["categoria"] == "Lazer":
            gasto_lazer += m["valor"]

        elif m["categoria"] == "Contas":
            gasto_contas += m["valor"]

    if (
    gasto_alimentacao == 0 and
    gasto_transporte == 0 and
    gasto_lazer == 0 and
    gasto_contas == 0
    ):
        print("Você ainda nao registou NENHUM Gasto!")

    else:
        print(f'\n-> Total gasto com ALIMENTAÇÃO: R${gasto_alimentacao:.2f}')
        print(f'-> Total gasto com TRANSPORTE: R${gasto_transporte:.2f}')
        print(f'-> Total gasto com LAZER: R${gasto_lazer:.2f}')
        print(f'-> Total gasto com CONTAS: R${gasto_contas:.2f}\n')

    
def movimentacao_data():
    data_busca = str(input('Digite a data que deseja encotrar: (dd/mm/yyyy): '))

    if not data_busca: #Verifica se o input do usuário esta Vazio.
        print('A data nao pode ser vazia.')
        return
    
    resultado = []

    for m in movimentacoes:
        if data_busca == m["data"]:
            resultado.append(m)

    if not resultado:
        print(f'Data {data_busca} nao foi encontrada.\n')
        return

    tabela = []
    # percorre resultado gerando numero de linha (i) e a movimentacao (m), contador começa em 1
    for i, m in enumerate(resultado, start = 1):
        tabela.append([
                        i,
                        m["tipo"],
                        m["descricao"],
                        f'R${m["valor"]:.2f}',
                        m["categoria"],
                        m["data"]
        ])
        
        cabecalho = ["ID", "Tipo", "Descrição", "Valor", "Categoria", "Data"]
    
    print(tabulate(tabela, headers = cabecalho, tablefmt ="grid"))   
        

    


