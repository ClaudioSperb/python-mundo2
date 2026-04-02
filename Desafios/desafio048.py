from colorama import Fore
print(f'{Fore.CYAN}===== MULTIMOS DE 3 ====={Fore.RESET}')
soma = 0
for c in range (1, 500, 2):
    if c % 3 == 0:
        soma += c
        print(c)
print(f'A soma entre os numeros ímpares e multiplos de 3 é {Fore.LIGHTRED_EX}{soma}')

