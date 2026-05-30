nome = 'LISTAGEM DE PREÇOS'
print(f'{40 * '='}')
print(f'{nome:^40}')
print(f'{40 * '='}')
listaProdutos = ('TV 50 Pol.',2800,'COMPUTADOR',2500 ,'NOTEBOOK',3200 , 'CELULAR' ,1800 ,'AR-CONDICIONADO',1900, 'CHROMECAST', 2380, 'MICROONDAS', 1850, 'FORNO ELETRICO', 1400,
                 'IPHONE 17', 7500, 'MACBOOK', 8900, 'SANSUNG S24', 4400)
for pos in range(len(listaProdutos)):
    if pos % 2 == 0:
        print(f'{listaProdutos[pos]:.<30}', end=' ')
    else:
        print(f'R${listaProdutos[pos]:.>4.2f}')
print('')