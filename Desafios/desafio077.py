from colorama import Fore
palavras = ('claudio', 'josiane', 'briana', 'duda', 'renato', 'marcia',
            'anderson', 'rek', 'impressao', 'maquina', 'python')
vogais = ('AEIOUaeiou')
print(f'{20 * '='} ANALISANDO AS PALAVRAS {20 * '='}')
print()
for palavra in palavras:
    print(f'Na palavra {Fore.GREEN}{palavra}{Fore.RESET} contém as seguintes vogais => ', end='')
    for letra in palavra:
        if letra in vogais:
            print(f'{Fore.CYAN}{letra}{Fore.RESET}', end=' ')
    print('')
print(f'{64 * '='}')