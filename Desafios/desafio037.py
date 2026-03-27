from colorama import Fore
from time import sleep
num = int(input('Digite um numero inteiro qualquer: '))
print('Para escolher a CONVERSÃO da base desejada, digite o codigo das respectivas bases: ')
print(f'{Fore.LIGHTGREEN_EX}[1] - BINARIO')
print(f'{Fore.LIGHTRED_EX}[2] - OCTAL')
print(f'{Fore.LIGHTBLUE_EX}[3] - HEXADECIMAL{Fore.RESET}')
escolha = str(input('Digite sua escolha: '))
sleep(1)
print('.'* 30)
sleep(1.5)
numBin = bin(num)
numHex = hex(num)
numOctal = oct(num)
if escolha == '1':
    print(f'A converão de {num} em Binario fica {Fore.LIGHTGREEN_EX}{numBin[2:]}')
elif escolha == '2':
    print(f'A conversão de {num} em Octadecimal fica {Fore.LIGHTRED_EX}{numOctal[2:]}')
else:
    print(f'A conversão de {num} para Hexadecimal fica {Fore.LIGHTBLUE_EX}{numHex[2:]}')

