from colorama import Fore
from time import sleep

print(40 * '=')
print(f'MATRIZ'.center(40))
print(40 * '=')

lista_1 = []
lista_2 = []
lista_3 = []

#LINHA 1
for n in range(1):
    num1 = int(input('Digite um número para a posição [0, 0]: '))
    num2 = int(input('Digite um número para a posição [0, 1]: '))
    num3 = int(input('Digite um número para a posição [0, 2]: '))
    lista_1.append(num1)
    lista_1.append(num2)
    lista_1.append(num3)
    
#LINHA 2 
for n in range(1):
    num1 = int(input('Digite um número para a posição [1, 0]: '))
    num2 = int(input('Digite um número para a posição [1, 1]: '))
    num3 = int(input('Digite um número para a posição [1, 2]: '))
    lista_2.append(num1)
    lista_2.append(num2)
    lista_2.append(num3)
    
#LINHA 3
for n in range(1):
    num1= int(input('Digite um número para a posição [2, 0]: '))
    num2 = int(input('Digite um número para a posição [2, 1]: '))
    num3 = int(input('Digite um número para a posição [2, 2]: '))
    lista_3.append(num1)
    lista_3.append(num2)
    lista_3.append(num3)

print(lista_1)
print(lista_2)
print(lista_3)
    