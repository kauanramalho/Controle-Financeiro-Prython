import movimentacoes

while True:
    n = 0
    print ('====== CONTROLE FINANCEIRO ======')
    print('1 - Cadastrar Receita')
    print('2 - Cadastrar gasto')
    print('3 - Listar movimentações')
    print('4 - Ver saldo atual')
    print('5 - Ver gastos por categori')
    print('6 - Buscar movimentação por data')
    print('0 - Sair')
    print('============================')

    try:
        n = int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite apenas NUMEROS!')
        continue

    if n == 1:
        movimentacoes.cadastrar_receitas()

    elif n == 2: 
        movimentacoes.cadastrar_gastos()

    elif n == 3:
        movimentacoes.listar_movimentacoes()

    elif n == 4:
        movimentacoes.ver_saldo()

    elif n == 5:
        movimentacoes.saldo_cadegoria()

    elif n == 6:
        movimentacoes.movimentacao_data()

    elif n == 0
        print('FINALIZANDO SERVIÇOS.....')
        print('ENCERRADO!')
        break

    else:
        print('Opçao INVALIDA!')
        print('Digite uma opção valida.')