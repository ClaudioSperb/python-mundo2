from time import sleep
from colorama import Fore
print(f'{15 * '='} GERANDO TABUADA {15 * '='}')
num = int(input('Digite um Número: '))
print(f'Você digitou o numero {num} - GERANDO SUA TABUADA - AGUARDE . . . ')
sleep(1)

for c in range(0 , 11):
    res = num * c
    print(f'{num} x {c} = {res}')
print(f'{25 * '='}')
print('FIM DO PROGRAMA')