from colorama import Fore
from time import sleep

print(40 * '=')
print(f'LISTAGEM DE PARES E ÍMPARES'.center(40))
print(40 * '=')

numeros = [[], []]
num = 0

for n in range(7):
    num = int(input(f'Digite o {n + 1}º Número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os Valore pares digitados foram -> {numeros[0]}')    
print(f'Os Valore ímpares digitados foram -> {numeros[1]}')    