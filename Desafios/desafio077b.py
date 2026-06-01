from colorama import Fore
print(f'{Fore.LIGHTGREEN_EX}{25 * '~='}{Fore.RESET}')
engates = ('GOL', 'CELTA', 'CIVIC', 'SAVEIRO', 'UNO',
           'CORSA', 'FUSION', 'CERATO', 'T-CROSS', 'NIVUS',
           'LIVINA', 'LOGUS', 'TROLLER', 'TIGGO', 'RENEGADE',
           'CRETA', 'COMMANDER', 'IX-35', 'LOGAN', 'COBALT')
for palavra in engates:
    print(f'A palavra {Fore.CYAN}{palavra.upper()}{Fore.RESET} tem as vogais -> ', end='')
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            print(f'{Fore.RED}{letra}{Fore.RESET}', end=' ')
    print()
print(f'{Fore.GREEN}{25 * '~='}{Fore.RESET}')