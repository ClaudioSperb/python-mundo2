from colorama import Fore
print(f'{15 * '='} PRATICANDO FOR {15 * '='}')
num = int(input('Digite um número para descobrir sua TABUADA >>> '))
print(f'O número que voce digitou foi {Fore.CYAN}{num}{Fore.RESET} e sua tabuada é >>>')
print(f'{Fore.GREEN}{50 * '='}{Fore.RESET}')

for c in range(0, 11):
    print(num * c)
print(f'{Fore.RED}<<< FIM DO PROGRAMA >>>{Fore.RESET}')