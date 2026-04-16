from colorama import Fore
print(f'{15 * '='} CRIANDO UM MENU DE OPÇÕES {15 * '='}')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro Número: '))
escolha = ''
print('''
 ========== MENU ==============
 |     [1] - SOMAR            |
 |     [2] - MULTIPLICAR      |
 |     [3] - MUDAR NÚMEROS    |
 |     [4] - MAIOR NÚMERO     |
 |     [5] - SAIR DO PROGRAMA |
  ____________________________
''')
opção = int(input('Escolha a opção desejada: '))
numeros = []
    
if opção == 1:
        soma = num1 + num2
        print(soma)
elif opção == 2:
        mult = num1 * num2
        print(mult)
elif opção == 4:
        numeros.append(num1,num2)
        maiorNumero = max(numeros)
        print(numeros)