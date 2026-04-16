from colorama import Fore
from time import sleep
print(f'{15 * '='} CRIANDO UM MENU DE OPÇÕES {15 * '='}')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro Número: '))
opção = 0
while opção != 5:
    print('''
    ========== MENU ==============
    |     [1] - SOMAR            |
    |     [2] - MULTIPLICAR      |
    |     [3] - MUDAR NÚMEROS    |
    |     [4] - MAIOR NÚMERO     |
    |     [5] - SAIR DO PROGRAMA |
    ____________________________
    ''')
    opção = int(input('Escolha a opção desejada: '))
    numeros = [num1, num2]
        
    if opção == 1:
        soma = num1 + num2
        print(f'Você escolheu somar os valores: ')
        print('somando . . .')
        sleep(1)
        print(f'O resultado da soma é - {soma}')
    elif opção == 2:
        mult = num1 * num2
        print(f'Você escolheu multiplicar os valores: ')
        print('Multiplicando . . .')
        sleep(1)
        print(f'O resultado da Multiplicação é {mult}')
    elif opção == 3:
        print('AGUARDE .... ')
        sleep(1)
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro Número: '))
    elif opção == 4:
        numeros.append(num1)
        numeros.append(num2)
        maiorNumero = max(numeros)
        print('ANALISANDO O MAIOR NUMERO DIGITADO >>> ')
        sleep(1)
        print(f'O maior número digitado foi o {maiorNumero}')
    elif opção == 5:
        print('FINALIZANDO O PROGRAMA . . .')
        sleep(1)