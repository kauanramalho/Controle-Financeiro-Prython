from datetime import datetime
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
    categoria_opcoes = int(input('-> Selecione Categoria: '))
    
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
        
    
    valor = float(input('-> Valor: '))
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
    #Só para testar a main
def listar_movimentacoes():
    pass
def ver_saldo():
    pass
def saldo_cadegoria():
    pass
def movimentacao_data():
    pass
    
    print('CADASTRO SALVO!')


