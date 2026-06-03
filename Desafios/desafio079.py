from time import sleep
from colorama import Fore
print(f'{15 * '='} CADASTRANDO VALORES {15 * '='}')
listaNumeros = []
res = 'N'
while True:
    num = int(input('Digite um valor?'))
    if num in listaNumeros:
        print('Numero ja adicionado. Digite um valor válido')
        continue
    else:
        listaNumeros.append(num)
        print('Numero ADICIONADO.')
    res = str(input('Quer continuar [S / N]: ')).strip().upper()
    if res != 'S':
        break
listaNumeros.sort()
print(f'Você digitou os numeros -> {listaNumeros}')
