from colorama import Fore
print(f'{10 * '='} {Fore.CYAN}DESAFIO 050{Fore.RESET} {10 * '='}')
soma = 0
for num in range (0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0: soma += n
print(f'A soma dos números pares ficou {Fore.LIGHTBLUE_EX}{soma}{Fore.RESET}')