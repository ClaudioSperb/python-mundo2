from time import sleep

from colorama import Fore

print(f'{15 * '='} {Fore.LIGHTGREEN_EX}TABUADA{Fore.RESET} {15 * '='}')
num = int(input('Digite um número para ver sua Tabuada: '))
sleep(0.5)
print('Gerando Tabuada ...')
sleep(1)
for c in range (0, 11):
    sleep(0.2)
    m = num * c
    print(f'{num} * {c} = {m}')
print('FIM DO PROGRAMA')