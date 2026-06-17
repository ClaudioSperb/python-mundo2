from colorama import Fore
from time import sleep

print(40 * '=')
print(f'LISTAGEM DE PARES E ÍMPARES'.center(40))
print(40 * '=')

numeros = []

for n in range(7):
    num = int(input(f'Digite o {n + 1}º Número: '))
    numeros.append(num)
    
print('ANALISANDO NÚMEROS: ')
sleep(1)
print(40 * '=')
print('Os números PARES digitados foram: ', end='')
for p in numeros:
    numeros.sort()
    if p % 2 == 0:
        print(f'{Fore.CYAN}{p}{Fore.RESET}', end=' ')
  
print('\nOs números ÍMPARES digitados foram: ', end='')
for p in numeros:
    numeros.sort()
    if p % 2 == 1:
        print(f'{Fore.RED}{p}{Fore.RESET}', end=' ')
        
print('\nFIM DO PROGRAMA')
