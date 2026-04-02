from colorama import Fore

print(f'{Fore.LIGHTCYAN_EX}{10 * '='} MOSTRANDO NÚMEROS PARES DE 1 A 50 {10 * '='}{Fore.RESET}')
print(f'Digite o numero correspondente a sua Opção -> ')
print('Para ver os números pares aperte [1] - Para encerrar o programa [2]')
num = int(input(f'{Fore.GREEN}[1] SIM{Fore.RESET} - {Fore.LIGHTRED_EX}[2] NÃO{Fore.RESET} >> '))
print('')
if num == 1:
    for c in range (2, 51, 2):
        print(c)
elif num == 2:
    print('ENCERRANDO PROGRAMA')
else:
    print(f'{Fore.RED}OPÇÃO INVÁLIDA')
print('FIM DO PROGRAMA')
