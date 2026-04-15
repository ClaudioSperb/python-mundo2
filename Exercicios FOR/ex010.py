from time import sleep
from colorama import Fore
print(f'{15 * '='} MOSTRANDO PALAVRAS COM FOR {15 * '='}')
palavra = str(input('Digite uma palavra qualquer: ')).upper().strip()
print(f'A palavra digitada foi {Fore.LIGHTGREEN_EX}{palavra}{Fore.RESET} >>> ')
palavraLoop = ''
for letra in palavra:
    palavraLoop += letra
    print(palavraLoop)