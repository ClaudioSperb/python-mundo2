from colorama import Fore
from time import sleep
print(f'{Fore.LIGHTMAGENTA_EX}{15 * '='} DETECTOR DE PALÍNDROMO {15 * '='}{Fore.RESET}')
frase = str(input('Digite uma palavra ou uma frase: ')).strip().upper()
fraseTrasnformada = ''.join(frase.split())
inverso = ''
for l in range (len(fraseTrasnformada) -1, -1, -1):
    print(fraseTrasnformada[l], end='')
    inverso += fraseTrasnformada[l]
if inverso == fraseTrasnformada:
    print(f' É um POLINDROMO')
else:
    print(' Não é um POLINDROMO')