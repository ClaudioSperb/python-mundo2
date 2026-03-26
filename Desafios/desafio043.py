from colorama import Fore
from time import sleep
nome = str(input('Qual seu nome: ')).strip().title()
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
#print(f'{imc:.2f}')
if imc < 18.5:
    print(f'{nome} seu IMC é de {Fore.LIGHTCYAN_EX}{imc:.2f}{Fore.RESET} , você está {Fore.LIGHTYELLOW_EX}ABAIXO DO PESO.{Fore.RESET}')
elif imc < 25:
    print(f'{nome} seu IMC é de {Fore.LIGHTCYAN_EX}{imc:.2f}{Fore.RESET} , você está com {Fore.LIGHTGREEN_EX}PESO IDEAL.{Fore.RESET}')
elif imc < 30:
    print(f'{nome} seu IMC é de {Fore.LIGHTCYAN_EX}{imc:.2f}{Fore.RESET} , você está com {Fore.LIGHTYELLOW_EX}SOBREPESO.{Fore.RESET}')
elif imc < 40:
    print(f'{nome} seu IMC é de {Fore.LIGHTCYAN_EX}{imc:.2f}{Fore.RESET} , você está com {Fore.LIGHTRED_EX}OBESIDADE GRAU 1.{Fore.RESET}')
else:
    print(f'{nome} seu IMC é de {Fore.LIGHTCYAN_EX}{imc:.2f}{Fore.RESET} , você está com {Fore.LIGHTRED_EX}OBESIDADE GRAU 2.{Fore.RESET}')