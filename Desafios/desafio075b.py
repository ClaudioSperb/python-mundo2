from time import sleep
from colorama import Fore
print(f'{15 * '='} Analise de dados com {Fore.GREEN} -> TUPLA <- {Fore.RESET} {15 * '='}')
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor [9], apareceu {num.count(9)} Vezes.')
if 3 in num:
    print(f'O valor [3] apareceu na {num.index(3) + 1}ª posição.')
else:
    print('Nao existe o valor[3] na sua Tupla.')
print(f'Os valores pares digitados foram -> ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n , end=' ')