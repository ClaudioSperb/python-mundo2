from time import sleep
from colorama import Fore
print(f'{Fore.LIGHTGREEN_EX}========= CONTAGEM REGRESSIVA =========={Fore.RESET}')
print('')
print('PARA INICIAR A CONTAGEM DIGITE [0]: ')
contagem = int(input('PODE DIGITAR AGORA: '))
if contagem == 0 :
    for i in range(10, 0, -1):
        sleep(1)
        print(i)
    print(f'{Fore.LIGHTYELLOW_EX}🎆 FELIZ ANO NOVO !!!! 🎆{Fore.RESET} ')
else:
    print('CONTAGEM CANCELADA')
