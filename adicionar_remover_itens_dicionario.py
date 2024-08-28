lista_de_compras = {}

while True:
    print()

    print('1 Adicionar item')
    print('2 Remover item')
    print('3 Ver lista')
    print('4 Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        item = input('Digite um item: ').lower()
        quantidade = int(input('Digite a quantidade: '))
        if item in lista_de_compras:
            lista_de_compras[item] += quantidade
        else:
            lista_de_compras[item] = quantidade
    elif escolha == '2':
        item = input('Remover item: ').lower()
        quantidade = int(input('Digite a quantidade: '))
        if quantidade >= lista_de_compras[item]:
            del lista_de_compras[item]
        else:
            lista_de_compras[item] -= quantidade
    elif escolha == '3':
        print(lista_de_compras)
    elif escolha == '4':
        break



