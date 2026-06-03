from time import sleep
from colorama import Fore
print(f'{15 * '='} MAIOR E MENOR VALOR {15 * '='}')
print()
lista_numeros = []
for n in range(5):
    num = int(input(f'Digite o numero para a posição {n}: '))
    lista_numeros.append(num)
print('Analisando Numeros Digitados ... ')
sleep(1)
print(f'Você digitou os valores -> {Fore.LIGHTGREEN_EX}{lista_numeros}{Fore.RESET}')
maior = max(lista_numeros)
menor = min(lista_numeros)
print(f'{51 * '~'}')
print(f'O maior valor digitado foi o {Fore.CYAN}{maior}{Fore.RESET} e está nas posições -> ', end=' ')
for p, v in enumerate(lista_numeros):
    if v == maior:
        print(f'... {p}', end=' ')
print()
print(f'O menor valor digitado foi o {Fore.LIGHTRED_EX}{menor}{Fore.RESET} e está nas posições -> ', end=' ')
for p, v in enumerate(lista_numeros):
    if v == menor:
        print(f'... {p}', end=' ')
print()
print(f'{51 * '~'}')