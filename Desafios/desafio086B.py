from colorama import Fore
from time import sleep

print(40 * '=')
print(f'MATRIZ'.center(40))
print(40 * '=')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} e {c}]: '))
print('=-' * 20)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
    