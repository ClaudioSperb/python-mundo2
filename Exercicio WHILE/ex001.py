from colorama import Fore
from time import sleep
print(f'{50 * '='}')
print(f'{15 * '='} MOSTRANDO OS PARES {15 * '='}')
print(f'{50 * '='}')
num = int(input('Digite um número: '))
print(f'GERANDO LISTA ... ')
sleep(1)
lista_numerosPares = []
lista_numerosInpares = []
c = 0
while c < num:
    c += 1
    if c % 2 == 0:
        lista_numerosPares.append(c)
    else:
        lista_numerosInpares.append(c)
print(f'{50 * '='}')
print(f'Números pares de 1 a {num} -> {Fore.LIGHTGREEN_EX}{lista_numerosPares}{Fore.RESET}')
print(f'{50 * '~'}')
print(f'Números inpares de 1 a {num} -> {Fore.LIGHTRED_EX}{lista_numerosInpares}{Fore.RESET}')
print('FIM')