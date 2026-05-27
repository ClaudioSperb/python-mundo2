from time import sleep
from colorama import Fore
print(f'{15 * '='} Analise de dados com {Fore.GREEN} -> TUPLA <- {Fore.RESET} {15 * '='}')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
numerosPares = 0
tupla_numeros = (num1, num2, num3, num4)
print(f'Você digitou esses valores: {tupla_numeros}')

if num1 != 9 and num2 != 9 and num3 != 9 and num4 != 9:
    print('Nao existe o valor 9 na sua Tupla !')
else:
    print(f'O Valor 9 apareceu {tupla_numeros.count(9)} vezes')

if num1 != 3 and num2 != 3 and num3 != 3 and num4 != 3:
    print('Na sua tupla nao tem nunhum valor 3')
else:
    print(f'O valor 3 apareceu na {tupla_numeros.index(3) + 1}ª posição')

    if num1 % 2 == 0:
        print(num1)
    elif num2 % 2 == 0:
        print(num2)
    elif num3 % 2 == 0:
        print(num3)
    elif num4 % 2 == 0:
        print(num4)
