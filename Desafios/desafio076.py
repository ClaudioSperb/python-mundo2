print(f'{40 * '='}')
print(f'LISTAGEM DE PREÇOS')
listaProdutos = ('TV 50 Pol.',2800,'COMPUTADOR',2500 ,'NOTEBOOK',3200 , 'CELULAR' ,1800 ,'AR-CONDICIONADO',1900, 'CHROMECAST', 280)
for pos in range(len(listaProdutos)):
    if pos % 2 == 0:
        print(f'{listaProdutos[pos]:.<30}', end=' ')
    else:
        print(f'R${listaProdutos[pos]:.>4.2f}')