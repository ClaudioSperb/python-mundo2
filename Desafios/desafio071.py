from colorama import Fore
from time import sleep
print(f'{15 * '='} BANCO CSP {15 * '='}')

valor = int(input('Qual valor do saque desejado R$ '))
total = valor
ced = 50
totcéd = 0
while True:
    if total >= ced:
        total -= ced
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'TOTAL DE {totcéd} CÉDULAS DE R${ced}')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totcéd = 0
            if total == 0:
                break
print(f'{15 * '='} BANCO CSP {15 * '='}')
print('')
print('Volte sempre ao BANCO CSP ! Tenha um ótimo dia !')