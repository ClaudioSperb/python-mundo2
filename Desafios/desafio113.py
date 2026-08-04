from colorama import Fore

def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except Exception as erro:
            print(f'{Fore.LIGHTRED_EX}[ERRO]: Por favor digite um valor inteiro válido{Fore.RESET}')
        else:
            print(f'O valor inteiro digitado foi {n1}')
            break

def leiaFloat(msg):
    while True:
        try:
            n1 = float(input(msg))
        except Exception as erro:
            print(f'{Fore.LIGHTRED_EX}[ERRO]: Por favor digite um valor Real válido{Fore.RESET}')
        else:
            print(f'O valor real  digitado foi {n1}')
            break


leiaInt('Digite um numero inteiro: ')
leiaFloat('Digite um numero real: ')