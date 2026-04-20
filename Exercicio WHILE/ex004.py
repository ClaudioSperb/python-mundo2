from colorama import Fore
from time import sleep
print(f'{50 * '='}')
print(f'{15 * '='} DESCOBRINDO QUE É O MAIOR {15 * '='}')
print(f'{50 * '='}')
lista_numeros = []
maiorNumero = 0
num = 0
while num <= 9:
    num += 1
    n = int(input(f'Digite o {num}º número: '))
    lista_numeros.append(n)
    if n > maiorNumero:
        maiorNumero = n
print(maiorNumero)

print('PRECESSANDO OS NÚMEROS . . .')
sleep(1)
print(f'Esses são os números digitados -> {lista_numeros}')
print(f'{50 * '='}')
#print(f'O maior valor da lista é ⬆️  {maiorNumero} ⬆️  e o menor é ⬇️  {menorNumero} ⬇️')
print(f'{50 * '='}')
print('FIM DO PROGRAMA')