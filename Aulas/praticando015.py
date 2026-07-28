from colorama import Fore
from time import sleep

def titulo(msg):
    tam = len(msg)
    print('=-' * tam)
    print(msg.center(tam * 2))
    print('=-' * tam)
titulo('<< É PAR OU ÍMPAR? >>')

def par_impar(n):

    if n % 2 == 0:
        return f'{Fore.GREEN}É PAR{Fore.RESET}'
    else:
        return f'{Fore.RED}É IMPAR{Fore.RESET}'
#PROGRAMA PRINCIPAL
while True:
    num = int(input('Digite um número: '))
    teste = par_impar(num)
    print(f'Você digitou o numero {num} =>', end=' ')
    print(f'{teste}')
    res = str(input('Quer testar mais números [S / N]: ')).upper()[0]
    if res == 'N':
        sleep(0.5)
        print('FINALIZANDO . . .', flush=True)
        break
titulo('<<< FIM DO PROGRAMA >>>')