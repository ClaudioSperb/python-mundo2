from time import sleep
print(f'{15 * '='} TRATANDO VÁRIOS DADOS {15 * '='}')
numero = 0
lista_numeros = []
while numero != 999:
    numero = int(input('Digite um número ou [999] Para sair >>> '))
    if numero != 999:
        lista_numeros.append(numero)
soma_lista_numeros = sum(lista_numeros)
print('ANALISANDO NÚMEROS . . .')
sleep(1)
print(f'Os numeros digitados foram -> {lista_numeros}')
print(f'A soma total dos números é {soma_lista_numeros}')
print('FIM')