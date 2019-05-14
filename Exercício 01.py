def ValorRetornado():
    if valor == 'bolo':
        print('O valor é de 4,50')
    elif valor == 'salgado':
        print('O valor é de R$ 4,00')
    elif valor == 'refrigerante':
        print('O valor é de R$ 4,50')
    elif valor == 'suco':
        print('O valor é de R$ 5,00')
    elif valor == 'sorvete':
        print('O valor é de R$ 6,00')
    elif valor == 'cafe':
        print('O valor é de R$ 4,00')
    elif valor == 'capuccino':
        print('O valor é de R$ 6,00')
    elif valor == 'dadinho':
        print('O valor é de R$ 0,50')
        
valor = str(input('O que deseja: '))

ValorRetornado()
