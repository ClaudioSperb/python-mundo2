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

indiceBarato = listaValores.index(min(listaValores))
produtoMaisBarato = listaProdutos[indiceBarato]
valorMaisBarato = listaValores[indiceBarato]
somaCompras = sum(listaValores)

print(f'O valor total da sua compra foi de R${somaCompras:.2f}')
print(f'No total, são {ValoresMil} produtos com valor maior que R$1000,00.')
print(f'O item {produtoMaisBarato}, com valor R${valorMaisBarato:.2f} Reais, é o produto mais barato.')