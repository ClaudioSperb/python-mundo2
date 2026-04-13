from colorama import Fore
from time import sleep
print(f'{15 * '='} {Fore.LIGHTWHITE_EX}SOMANDO TODAS AS NOTAS{Fore.RESET} {15 * '='}')
lista_notas = []
for notas in range(1 , 6):
    nota = float(input(f'Digite a {notas}ª Nota: '))
    lista_notas.append(nota)
print('ANALISANDO NOTAS')
print(f'{15 * '='}')
sleep(0.8)
print(f'{15 * '='}')
print(f'Suas notas foram: ')
print(lista_notas)
media = sum(lista_notas) / 5
if media < 6:
    print(f'Sua média foi de {Fore.RED}{media:.1f}{Fore.RESET} e voce está {Fore.RED}REPROVADO{Fore.RESET}')
elif media < 8:
    print(f'Sua média foi de {Fore.YELLOW}{media:.1f}{Fore.RESET} e você está de {Fore.YELLOW}RECUPERAÇÃO{Fore.RESET}')
else:
    print(f'Sua média foi de {Fore.GREEN}{media:.1f}{Fore.RESET} e voce está {Fore.LIGHTGREEN_EX}APROVADO{Fore.RESET}')
print('')
print('FIM DO PROGRAMA')
print(f'{15 * '='}')