from colorama import Fore
from time import sleep

print(f'{15 * "~"} MERCADO DO CLAUDIO {15 * "~"}')
print('Seja Bem vindo ao nosso Mercado\n')

soma = 0
valor_maior = 0
menor_preco = 0
produto_barato = ''
cont = 0 # Contador para saber qual é o primeiro produto

while True:
    produto = str(input('Digite o nome do Produto: ')).title().strip()
    valor = float(input('Valor do Produto: R$'))
    cont += 1
    soma += valor

    # Lógica para contar produtos acima de R$1000
    if valor > 1000:
        valor_maior += 1

    # Lógica para descobrir o mais barato
    if cont == 1 or valor < menor_preco:
        menor_preco = valor
        produto_barato = produto

    off = ' '
    while off not in 'SN':
        off = str(input('Deseja continuar comprando [S/N]: ')).upper().strip()[0]
    
    if off == 'N':
        break

print("-" * 40)
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {valor_maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${menor_preco:.2f}')
print('FIM')