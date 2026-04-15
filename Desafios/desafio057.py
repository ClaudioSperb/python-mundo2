from colorama import Fore
from time import sleep
print(f'{15 * '='} VALIDAÇÃO DE DADOS {15 * '='}')
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input(f'Digite o seu sexo {Fore.LIGHTBLUE_EX}[M]{Fore.RESET} - {Fore.MAGENTA}[F]{Fore.RESET} >>> ')).upper()
    print('ANALISANDO ...')
    sleep(1)
    if sexo != 'F' and sexo != 'M':
        print(f'{Fore.LIGHTRED_EX}Opção inválida. Tente novamente !!!{Fore.RESET} ')
    elif sexo == 'M':
        print(f'Você digitou [{sexo}] - Voce é do Sexo {Fore.LIGHTBLUE_EX}MASCULINO{Fore.RESET}')
    elif sexo == 'F':
        print(f'Você digitou [{sexo}] - Voce é do Sexo {Fore.MAGENTA}FEMININO{Fore.RESET}')
print(f'{50 * '='}')
print(f'{Fore.GREEN}Obrigado por participar da pesquisa !!!{Fore.RESET} ')
print('FIM DO PROGRAMA')
    