from colorama import Fore
from time import sleep

print(40 * '=')
print(f'MATRIZ'.center(40))
print(40 * '=')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = maior = soma_coluna = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} e {c}]: '))
print('=-' * 20)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print('=-' * 20)
print(f'A soma dos numeros Pares digitados foi de {soma_par}')
for l in range(3):
    soma_coluna += matriz[l][2]
print(f'A soma da terceira coluna é {soma_coluna}')
for c in range(3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha da matriz é {maior}')