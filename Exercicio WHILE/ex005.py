from colorama import Fore
from time import sleep
print(f'{50 * '='}')
print(f'{15 * '='} LOGIN / SENHA {15 * '='}')
print(f'{15 * '='} CLAUDIO SISTEMAS {15 * '='}')
nome = ''
senha = ''
while nome != 'CLAUDIO':
    nome = str(input('Usuário: ')).upper()
    if nome != 'CLAUDIO':
        print(f'{Fore.LIGHTRED_EX}‼️  Usuário nao encontrado  ‼️{Fore.RESET}')
        print(f'{Fore.LIGHTRED_EX}Digite um Usuário Válido{Fore.RESET}')
print(f'{Fore.LIGHTGREEN_EX}USUÁRIO ENCONTRADO ✅ {Fore.RESET}')
while senha != 12345678:
    senha = int(input('Senha (8 caracteres): '))
    if senha != 12345678:
        print(f'{Fore.LIGHTRED_EX}‼️  Senha incorreta  ‼️{Fore.RESET}')
        print(f'{Fore.LIGHTRED_EX}Digite uma senha válida! {Fore.RESET}')
print('LOADING . . .')
sleep(1)
print(f'{Fore.LIGHTGREEN_EX}✅ LOGIN EFETUADO COM SUCESSO ✅{Fore.RESET}')
print(f'Seja bem vindo {Fore.CYAN}{nome}{Fore.RESET}')
