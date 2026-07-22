
from colorama import Fore
from time import sleep
def titulo(palavra):
    """
    -> Esse parametro serve para mudar o titulo dependendo do assunto.
    Já esta configurado para ficar centralizado e entre '=-' conforme o
    tamanho da frase ou palavra.
    """
    tam = len(palavra)
    print('=-'* tam)
    print(f'{palavra}'.center(tam * 2))
    print('=-'* tam)
titulo('VALIDANDO ENTRADAS')

def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            print(f'{Fore.GREEN}VERIFICANDO . . .{Fore.RESET}')
            sleep(0.5)
            return int(n)
        else:
            print(f'{Fore.GREEN}VERIFICANDO . . .{Fore.RESET}')
            sleep(0.5)
            print(f'{Fore.RED}[ERRO] - digite um numero válido{Fore.RESET}')
            
       
#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')