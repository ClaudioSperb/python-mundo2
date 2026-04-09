from colorama import Fore
from datetime import date
anoAtual = date.today().year
print(f'{Fore.LIGHTWHITE_EX}{15 * '='} TESTE DE MAIOR IDADE {15 * '='}{Fore.RESET}')
totMaior = 0
totMenor = 0
for c in range (0, 7):
    anoNasc = int(input(f'Digite o ano de nascimento da {c + 1}ª pessoa: '))
    idade = anoAtual - anoNasc
    if idade >= 21:
        totMaior += 1
    else:
        totMenor += 1
print(f'Temos {totMaior} pessoas maior de idade! ')
print(f'Temos {totMenor} pessoas menor de idade! ')