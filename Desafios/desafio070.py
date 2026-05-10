from colorama import Fore
from time import sleep
print(f'{15 * '~'} MERCADO DO CLAUDIO {15 * '~'}')
print('Seja Bem vindo ao nosso Mercado')
print('')
lista_Produtos = []
lista_valores =[]
Valores_Produtos = 0
soma_produtos = 0
valor_maior = 0
res = ''
while res != 'N':
    print(f'{15 * '='} PAGINA DE COMPRA {15 * '='}')
    produto = str(input('Nome do Produto: ')).title().strip()
    valor = float(input('Valor do Produto: R$'))
    res = ''
    while res != 'S' and res != 'N':
        res = str(input('Continuar comprando [S / N] ? ')).title().strip()
    soma_produtos += valor
    lista_Produtos.append(produto)
    lista_valores.append(valor)

    if res == 'N':
        valor_maior += 1
        print(f'{Fore.LIGHTRED_EX}ENCERRANDO ...{Fore.RESET}')
        sleep(1)
        break

    if valor > 1000:
        valor_maior += 1
valor_barato = min(lista_valores)

print(f'{valor_barato}')
print(f'O valor total da sua compra foi de R${soma_produtos:.2f}')
print(f'Na sua compra tem {valor_maior} produtos a cima de R$1.000,00 reais')
print(f'{lista_Produtos}')
print(f'{lista_valores}')