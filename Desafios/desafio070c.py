from colorama import Fore
from time import sleep
print(f'{15 * "~"} MERCADO DO CLAUDIO {15 * "~"}')
listaValores = []
listaProdutos = []
ValoresMil = 0
while True:
    produto = str(input('Nome do Produto: ')).title().strip()
    valor = float(input('Valor do Produto: '))
    listaProdutos.append(produto)
    listaValores.append(valor)

    if valor > 1000:
        ValoresMil += 1
        
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Continuar comprando? [S / N] ')).upper().strip()[0]
    if saida == 'N':
        break
somaCompras = sum(listaValores)

print(listaProdutos)
print(listaValores)
print(ValoresMil)
print(somaCompras)