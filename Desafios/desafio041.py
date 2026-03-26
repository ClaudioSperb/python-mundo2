from datetime import date, datetime
from time import sleep

from colorama import Fore
print(f'Seja bem vindo a {Fore.CYAN}CONFEDERAÇÃO  NACIONAL DE NATAÇÃO.{Fore.RESET}')
nomeAtleta = str(input('Digite o nome do Atleta: ')).title().strip()
anoNascimento = int(input('Digite o ano de nascimento do atleta: '))

print('Validando seus dados ...')
sleep(1.5)
anoAtual = date.today().year
validandoCategoria = anoAtual - anoNascimento

if validandoCategoria <= 9:
    print(f'Ola {nomeAtleta}, sua categoria é {Fore.LIGHTBLUE_EX}MIRIM{Fore.RESET}')
elif validandoCategoria <= 14:
    print(f'Olá {nomeAtleta}, sua categoria é {Fore.LIGHTRED_EX}INFANTIL{Fore.RESET}')
elif validandoCategoria <= 19:
    print(f'Ola {nomeAtleta}, sua categoria é {Fore.LIGHTYELLOW_EX}JUNIOR{Fore.RESET}')
elif validandoCategoria <= 20:
    print(f'Ola {nomeAtleta}, sua categoria é {Fore.LIGHTWHITE_EX}SENIOR{Fore.RESET}')
else:
    print(f'Ola {nomeAtleta}, sua categoria é {Fore.LIGHTMAGENTA_EX}MASTER{Fore.RESET}')