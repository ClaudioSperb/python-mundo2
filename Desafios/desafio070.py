from colorama import Fore
from time import sleep
print(f'{15 * '~'} MERCADO DO CLAUDIO {15 * '~'}')
print('Seja Bem vindo ao nosso Mercado')
print('')
lista_Produtos = []
Valores_Produtos = []
while True:
    print(f'{15 * '='} PAGINA DE COMPRA {15 * '='}')
    produto = str(input('Nome do Produto: ')).title().strip()
    valor = float(input('Valor do Produto: R$'))
    res = str(input('Continuar comprando [S / N] ? ')).capitalize().strip()
    lista_Produtos.append(produto)
    Valores_Produtos.append(valor)
    if res == 'N':
        print(f'{Fore.LIGHTRED_EX}ENCERRANDO ...{Fore.RESET}')
        sleep(1)
        break
soma_produtos = sum(Valores_Produtos)
print(f'{soma_produtos}')
print(f'{lista_Produtos}')
print(f'{Valores_Produtos}')