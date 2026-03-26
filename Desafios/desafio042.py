from time import sleep
from colorama import Fore

ladoA = int(input('Digite o primeiro numero inteiro: '))
ladoB = int(input('Digite o segundo numero inteiro: '))
ladoC = int(input('Digite o terceiro numero inteiro: '))
print('')
print('Verificando as medidas ...')
sleep(1.5)
print('')
if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print(f'Com os numeros digitados {Fore.LIGHTGREEN_EX}É POSSÍVEL{Fore.RESET} formar um triângulo')
else:
    print(f'Com os numeros digitados, {Fore.LIGHTRED_EX}NÃO È POSSIVEL{Fore.RESET} formar um triângulo')

print('_--_' * 10)

if ladoA == ladoB == ladoC and ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print(f'{Fore.LIGHTCYAN_EX}Triângulo Equilatero{Fore.RESET}, pois todos os Lados são iguais')
elif ladoA == ladoB and ladoA == ladoC and ladoB == ladoC and ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print(f'{Fore.LIGHTCYAN_EX}Triângulo Isósceles{Fore.RESET}, pois possuem 2 lados iguais')
elif ladoA != ladoB and ladoC and ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print(f'{Fore.LIGHTCYAN_EX}Triângulo Escaleno{Fore.RESET}, pois tem os 3 lados diferentes')


