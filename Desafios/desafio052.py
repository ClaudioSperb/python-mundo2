from time import sleep
from colorama import Fore
print(f'{10 * '='} TESTANDO NÚMEROS PRIMOS {10 * '='}')
num = int(input('Digite um numero inteiro: '))
sleep(0.5)
print('Valindando número .... ')
for c in range(1, num + 1):
    if num % c == 0:
        print(f'{Fore.LIGHTBLUE_EX}{c}{Fore.RESET}', end=' ')
    else:
        print(f'{Fore.LIGHTRED_EX}{c}{Fore.RESET}', end=' ')
    #print(f'{c}', end=' ')
