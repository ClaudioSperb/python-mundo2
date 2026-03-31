from random import randint
from colorama import Fore
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('======== VAMOS JOGAR ========')
computador = randint(0, 2)
print(F'''{Fore.LIGHTGREEN_EX}SUAS OPÇÕES :{Fore.RESET} 
{Fore.LIGHTBLUE_EX}[0] - PEDRA 🪨{Fore.RESET}
{Fore.LIGHTCYAN_EX}[1] - PAPEL 🧻{Fore.RESET}
{Fore.LIGHTRED_EX}[2] - TESOURA ✂️{Fore.RESET}
''')
jogador = int(input('Qual é a sua escolha: '))
print('-=' * 10)
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador escolheu {itens[jogador]}')
print('-=' * 10)
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE 😶 !!!')
    elif jogador == 1:
        print('VOCÊ GANHOU 🤩 !!!')
    elif jogador == 2:
        print('VOCÊ PERDEU 😭 !!!')
    else:
        print('OPÇÃO INVÁLIDA ⚠️⚠️⚠️ ')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('VOCÊ PERDEU 😭 !!! ')
    elif jogador == 1:
        print('EMPATE 😶 !!!')
    elif jogador == 2:
        print('VOCÊ GANHOU 🤩 !!!')
    else:
        print('OPÇÃO INVÁLIDA ⚠️⚠️⚠️ ')

elif computador ==2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('VOCÊ GANHOU 🤩 !!!')
    elif jogador == 1:
        print('VOCÊ PERDEU 😭 !!!')
    elif jogador == 2:
        print('EMPATE 😶 !!!')
    else:
        print('OPÇÃO INVÁLIDA ⚠️⚠️⚠️ ')