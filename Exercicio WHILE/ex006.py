from colorama import Fore
from time import sleep
print(f'{50 * '='}')
print(f'{15 * '='} CAIXA ELETRÔNICO {17 * '='}')
opc = 0
saldo = float(1500)
while opc != 4:
    print(f'''
        Seja Bem-Vindo
        
        Esolha a opção desejada:
        [1] - DEPOSITAR
        [2] - SACAR
        [3] - SALDO NA TELA
        [4] - SAIR
      
      ''')
    opc = int(input('Digite a opção desejada: '))
    if opc == 1:
        print(f'SALDO ATUAL -> R${saldo}')
        deposito = float(input('Qual valor a ser depositado: R$ '))
        saldo += deposito
        print('Depositando...')
        sleep(1)
        print(f'Tudo certo, seu saldo atualizado é {saldo}')
        