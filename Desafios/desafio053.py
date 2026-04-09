from colorama import Fore
from time import sleep
print(f'{Fore.LIGHTMAGENTA_EX}{15 * '='} DETECTOR DE PALÍNDROMO {15 * '='}{Fore.RESET}')
frase = str(input('Digite uma palavra ou uma frase: ')).strip().upper()
fraseTrasnformada = ''.join(frase.split())
testeFrase = fraseTrasnformada[::-1]
if fraseTrasnformada == testeFrase:
    print(f'a frase digitada foi {Fore.LIGHTCYAN_EX}{frase}{Fore.RESET}, ela ao contrário é {Fore.LIGHTBLUE_EX}{testeFrase}{Fore.RESET}')
    print('Verificando se é PALINDROMO >>> ')
    sleep(0.5)
    print('............')
    sleep(0.5)
    print(f'{Fore.GREEN}CONFIRMADO{Fore.RESET}, é um PALINDROMO !!! ')
else:
    print(f'a frase digitada foi {Fore.LIGHTCYAN_EX}{frase}{Fore.RESET}, ela ao contrário é {Fore.LIGHTBLUE_EX}{testeFrase}{Fore.RESET}')
    print('Verificando se é PALINDROMO >>> ')
    sleep(0.5)
    print('............')
    sleep(0.5)
    print(f'{Fore.LIGHTRED_EX}NEGADO{Fore.RESET}, NÃO é um PALINDROMO !!! ')