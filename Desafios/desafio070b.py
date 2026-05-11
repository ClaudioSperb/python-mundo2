from colorama import Fore
from time import sleep
print(f'{15 * "~"} MERCADO DO CLAUDIO {15 * "~"}')
print('Seja Bem vindo ao nosso Mercado\n')
total = totmil = menor = cont = 0
barato = ' '

while True:
    produto = str(input('Nome do Produto: ')).title().strip()
    preço = float(input('Valor: R$'))
    total += preço
    cont += 1
    
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S / N] ')).upper().strip()[0]
    if resp == 'N':
        break
    
print(f'{20 * '='} FIM DO PROGRAMA {20 * '='}')
print(f'O total da sua compra foi de R${total:.2f} Reais')
print(f'Temos {totmil} produtos em sua compra a cima de $1000,00 reais.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')