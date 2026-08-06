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

def linha(tam=42):
    return '=' * tam

def cabecalho(txt):
    print(linha())
    print(f'{txt}'.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \t\033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = validando_numero_inteiro(f'\033[32mSua opção: \033[m')
    return opc