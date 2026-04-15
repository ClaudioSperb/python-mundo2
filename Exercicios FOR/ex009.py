from time import sleep
from colorama import Fore
print(f'{15 * '='} MOSTRANDO PALAVRAS COM FOR {15 * '='}')
palavra = str(input('Digite uma palavra qualquer: ')).upper().strip()
print(f'A palavra digitada foi {Fore.LIGHTGREEN_EX}{palavra}{Fore.RESET} >>> ')
print('')
sleep(1)
for i in range(len(palavra)):
    print(f' {Fore.CYAN}{palavra[i]}{Fore.RESET} ')
    print('---')
print('')
print('FIM DO PROGRAMA')