from random import randint

from colorama import Fore
from time import sleep
import random
print('Vamos jogar ? O Jogo será - Pedra , Papel e Tesoura.')
sleep(1)
print(f'Escolha - {Fore.LIGHTCYAN_EX}[0] - PEDRA{Fore.RESET}, {Fore.LIGHTBLUE_EX}[1] - PAPEL{Fore.RESET}, {Fore.LIGHTMAGENTA_EX}[2] - TESOURA{Fore.RESET}')

jogo = int(input('Digite o numero da sua escolha: '))
jogoPc = randint(0, 2)
print(f'Voce escolheu {jogo} e o PC escolheu {jogoPc}')
#print(jogo)
if jogo == 0 and jogoPc == 0:
    print(f'{Fore.YELLOW}EMPATE - Os dois escolheram Pedra')
elif jogo == 0 and jogoPc == 1:
    print(f'{Fore.LIGHTRED_EX}Você perdeu, Papel enrola Pedra')
elif jogo == 0 and jogoPc == 2:
    print(f'{Fore.LIGHTGREEN_EX}Você ganhou, Pedra quebra Tesoura')
elif jogo == 1 and jogoPc == 0:
    print(f'{Fore.LIGHTGREEN_EX}Você ganhou, Papel enrola Pedra')
elif jogo == 1 and jogoPc == 1:
    print(f'{Fore.YELLOW}EMPATE, os dois escolheram Papel')
elif jogo == 1 and jogoPc == 2:
    print(f'{Fore.LIGHTRED_EX}Você perdeu, Tesoura corta Papel')
elif jogo == 2 and jogoPc == 0:
    print(f'{Fore.LIGHTRED_EX}Você PERDEU, Pedra quebra Tesoura')
elif jogo == 2 and jogoPc == 1:
    print(f'{Fore.LIGHTGREEN_EX}Você ganhou, Tesoura corta Papel')
else:
    print(f'{Fore.YELLOW}EMPATE, os dois escolheram Tesoura')
