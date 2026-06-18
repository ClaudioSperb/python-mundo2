from colorama import Fore
from time import sleep
from random import randint

print(40 * '=')
print(f'< MEGA-SENA >'.center(40))
print(40 * '=')

todos_os_palpites = []
palpites = []
res = int(input('Quantos palpites voce quer criar: '))
print(40 * '=')
print('GERANDO PALPITES . . .')
sleep(0.3)
print('Aguarde..')
sleep(1)
print(f'{res} Palpites solicitados >>>> ')
for c in range(res):
    while len(palpites) < 6:
        numero = randint(1, 60)
        if numero not in palpites:
            palpites.append(numero)
            palpites.sort()
    todos_os_palpites.append(palpites.copy())
    palpites.clear()
for c in todos_os_palpites:
    sleep(0.5)
    print(c)
    print(25 * '~')