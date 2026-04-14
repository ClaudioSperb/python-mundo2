from time import sleep
from colorama import Fore
print(f'{15 * '='}{Fore.CYAN} MÉDIA DE NOTAS{Fore.RESET} {15 * '='}')
lista_notas = []
for c in range(1 , 6):
    nota = float(input(f'Digite a {c}ª Nota: '))
    lista_notas.append(nota)
somaNotas = sum(lista_notas)
media = somaNotas / 5
print(f'ANALISANDO SUAS NOTAS .... ')
sleep(1)
print(f'{15 * '='}')
print(f'Sua notas foram >>>> {lista_notas}')
if media < 6:
    print(f'Sua média foi {Fore.RED}{media:.2f}{Fore.RESET} - {Fore.RED}REPROVADO{Fore.RESET} !!! ')
elif media < 8:
    print(f'Sua média foi {Fore.YELLOW}{media:.2f}{Fore.RESET} - {Fore.YELLOW}RECUPERAÇÃO !!! ')
else:
    print(f'Sua média foi {Fore.LIGHTGREEN_EX}{media:.2f}{Fore.RESET} - {Fore.LIGHTGREEN_EX} APROVADO !!! {Fore.RESET}')
print('')
print('FIM DO PROGRAMA')