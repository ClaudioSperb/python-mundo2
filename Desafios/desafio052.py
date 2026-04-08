from time import sleep
from colorama import Fore
print(f'{Fore.LIGHTMAGENTA_EX}{10 * '='} TESTANDO NÚMEROS PRIMOS {10 * '='}{Fore.RESET}')
tot = 0
num = int(input('Digite um numero inteiro: '))
sleep(0.5)
print('Valindando número .... ')
for c in range (1, num + 1):
    if num % c == 0:
        print(f'{Fore.LIGHTGREEN_EX}{c}{Fore.RESET}', end=' ')
        tot += 1
    else:
        print(f'{Fore.LIGHTRED_EX}{c}{Fore.RESET}', end=' ')
print(f'\nO numero {num} foi -- DIVISIVEL -- {tot} vezes', end=' ')
if tot == 2:
    print(f'\nEle é um número {Fore.LIGHTCYAN_EX}PRIMO{Fore.RESET}')
else:
    print(f'\nEle não é um número {Fore.LIGHTRED_EX}PRIMO{Fore.RESET}')
