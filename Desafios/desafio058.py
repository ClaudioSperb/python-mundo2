import random
from time import sleep
from colorama import Fore
print(f'{15 * '='} VAMOS JOGAR ? 🕹️ {15 * '='}')
sleep(1.5)
print(f'Se o número que voce Digitar for igual ao do Computador 🖥️ >>> {Fore.GREEN}VOCÊ GANHA 😃{Fore.RESET}')
sleep(1)
print(f'Se o número do computador 🖥️ for diferente >>> {Fore.RED}VOCÊ PERDE 😭{Fore.RESET}')
sleep(0.5)
print('VAMOS COMEÇAR ....')
sleep(1)
num = 0
numMaquina = random.randint(0, 10)
palpites = []
while num != numMaquina:
    numMaquina = random.randint(0, 10)
    num = int(input('Digite um numero de 0 a 10: '))
    palpites.append(num)
    print(f'{50 * '='}')
    sleep(1)
    if num != numMaquina:
        print(f'Você escolheu o número {num}')
        print(f'{50 * '='}')
        print(f'{Fore.RED}O computador 🖥️  venceu !!!{Fore.RESET}')
        print(f'O numero escolhido pela Máquina 🖥️ foi >>> {numMaquina}')
    else:
        print(f'{Fore.LIGHTGREEN_EX}Muito Bem. {Fore.GREEN}VITORIA  🎈🎈🎈  !!!!{Fore.RESET}')
        print(f'{50 * '='}')
        print(f'Você escolheu o número {num}')
        print(f'O numero escolhido pela Máquina 🖥️  foi >>> {numMaquina}')
        
print(f'Voce digitou esses numeros ate ganhar --- {palpites}')
print('FIM DO PROGRAMA')