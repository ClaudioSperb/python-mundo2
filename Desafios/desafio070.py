from colorama import Fore
from time import sleep
print(f'{15 * '~'} MERCADO DO CLAUDIO {15 * '~'}')
print('Seja Bem vindo ao nosso Mercado')
print('')
lista_Produtos = []
lista_valores =[]
Valores_Produtos = 0
soma_produtos = 0
while True:
    print(f'{15 * '='} PAGINA DE COMPRA {15 * '='}')
    produto = str(input('Nome do Produto: ')).title().strip()
    valor = float(input('Valor do Produto: R$'))
    res = str(input('Continuar comprando [S / N] ? ')).title().strip()
    soma_produtos += valor
    lista_Produtos.append(produto)
    lista_valores.append(valor)

    if res == 'N':
        print(f'{Fore.LIGHTRED_EX}ENCERRANDO ...{Fore.RESET}')
        sleep(1)
        break

print(f'{soma_produtos}')
print(f'{lista_Produtos}')
print(f'{lista_valores}')