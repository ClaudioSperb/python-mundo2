from colorama import Fore
from time import sleep
nome = str(input('Qual seu nome: ')).strip().title()
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
#print(f'{imc:.2f}')
if imc < 18.5:
    print(f'{nome} seu IMC é de {imc:.2f} , você está abaixo do peso.')
elif imc < 25:
    print(f'{nome} seu IMC é de {imc:.2f} , você está com peso ideal.')
elif imc < 30:
    print(f'{nome} seu IMC é de {imc:.2f} , você está com sobrepeso.')
elif imc < 40:
    print(f'{nome} seu IMC é de {imc:.2f} , você está com obesidade grau 1.')
else:
    print(f'{nome} seu IMC é de {imc:.2f} , você está com obesidade grau 2.')