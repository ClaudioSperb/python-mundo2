from time import sleep
print(f'{15 * '='} MOSTRANDO O MAIOR NÚMERO {15 * '='}')
lista_numeros = []
for n in range(1, 6):
    num = int(input(f'Digite o {n}º Número: '))
    lista_numeros.append(num)
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)
indice_menor = lista_numeros.index(menor_numero)
indice_maior = lista_numeros.index(maior_numero)
print(f'Os números digitados foram {lista_numeros}')
sleep(1)
print('ANALISANDO .... ')
sleep(1)
print(f'O maior número digitado foi o {maior_numero}')
print(f'O número menor foi o {menor_numero}')