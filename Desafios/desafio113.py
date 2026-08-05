from colorama import Fore


def validando_numero_inteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except InterruptedError:
            print('O Usuário não informou um dos valores solicitados')
        except(TypeError, ValueError):
            print(f'{Fore.LIGHTRED_EX}[ERRO]: Por favor digite um valor inteiro válido{Fore.RESET}')
        except KeyboardInterrupt:
            print(f'{Fore.RED}Usuario nao informou algum dos campos do sistema!{Fore.RESET}')
            return 0
        else:
            return n


def validando_numero_real(msg):
    while True:
        try:
            n = float(input(msg))
        except InterruptedError:
            print('O Usuário nao informou um dos valores solicitados')
        except (TypeError, ValueError):
            print(f'{Fore.LIGHTRED_EX}[ERRO]: Por favor digite um valor Real válido{Fore.RESET}')
        except KeyboardInterrupt:
            print(f'{Fore.RED}Usuario nao informou algum dos campos do sistema!{Fore.RESET}')
            return 0

        else:
            return n


n1 = validando_numero_inteiro('Digite um numero inteiro: ')
n2 = validando_numero_real('Digite um numero real: ')
print(f'O valor inteiro é {n1} e o valor real é {n2}')