from random import randint
from colorama import Fore
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('======== VAMOS JOGAR ========')
computador = randint(0, 2)
print(F'''{Fore.LIGHTGREEN_EX}SUAS OPÇÕES :{Fore.RESET} 
{Fore.LIGHTBLUE_EX}[0] - PEDRA ✊🏻{Fore.RESET}
{Fore.LIGHTCYAN_EX}[1] - PAPEL 🧻{Fore.RESET}
{Fore.LIGHTRED_EX}[2] - TESOURA ✂️{Fore.RESET}
''')
jogador = int(input('Qual é a sua escolha: '))
print('-=' * 10)
sleep(0.8)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOOO !!!')
print('')
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador escolheu {itens[jogador]}')
print('-=' * 10)
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print(f'{Fore.LIGHTYELLOW_EX}EMPATE 😶 !!!{Fore.RESET}')
    elif jogador == 1:
        print(f'{Fore.LIGHTGREEN_EX}VOCÊ GANHOU 🤩 !!!{Fore.RESET}')
    elif jogador == 2:
        print(f'{Fore.LIGHTRED_EX}VOCÊ PERDEU 😭 !!!{Fore.RESET}')
    else:
        print(f'{Fore.LIGHTRED_EX}OPÇÃO INVÁLIDA ⚠️⚠️⚠️ {Fore.RESET}')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print(f'{Fore.LIGHTRED_EX}VOCÊ PERDEU 😭 !!! {Fore.RESET}')
    elif jogador == 1:
        print(f'{Fore.LIGHTYELLOW_EX}EMPATE 😶 !!!{Fore.RESET}')
    elif jogador == 2:
        print(f'{Fore.LIGHTGREEN_EX}VOCÊ GANHOU 🤩 !!!{Fore.RESET}')
    else:
        print(f'{Fore.LIGHTRED_EX}OPÇÃO INVÁLIDA ⚠️⚠️⚠️ {Fore.RESET}')

elif computador ==2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print(f'{Fore.LIGHTGREEN_EX}VOCÊ GANHOU 🤩 !!!{Fore.RESET}')
    elif jogador == 1:
        print(f'{Fore.LIGHTRED_EX}VOCÊ PERDEU 😭 !!!{Fore.RESET}')
    elif jogador == 2:
        print(f'{Fore.LIGHTYELLOW_EX}EMPATE 😶 !!!{Fore.RESET}')
    else:
        print(f'{Fore.LIGHTRED_EX}OPÇÃO INVÁLIDA ⚠️⚠️⚠️ {Fore.RESET}')