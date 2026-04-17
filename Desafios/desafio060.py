from time import sleep
from colorama import Fore
print(f'{10 * '='} GERANDO O FATORIAL DE UM NÚMERO {10 * '='}')
num = int(input('Digite um número para descobrir seu FATORIAL: '))
print(f'{Fore.CYAN}GERANDO O FATORIAL . . .{Fore.RESET}')
sleep(1.5)
lista_numeros = []
sleep(0.5)
n = num
fat = 1
while n > 1:
    fat *= n
    n -= 1
    lista_numeros.append(fat)

print(f'O fatorial do número [{Fore.LIGHTGREEN_EX}{num}{Fore.RESET}] -> {lista_numeros} -> [{Fore.RED}{fat}{Fore.RESET}]')