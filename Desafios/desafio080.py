print(f'{40 * '='}')
print('COLOCANDO TUDO EM ORDEM'.center(40))
print(f'{40 * '='}')
lista_numeros = []
lista_maior = []
lista_menor = []
for c in range(5):
    num = int(input('Digite um numero: '))
    lista_numeros.append(num)
    maior_numero = max(lista_numeros)
    menor_numero = min(lista_numeros)
    if num > maior_numero:
        lista_maior.insert(num, -1)
    elif num < maior_numero:
        lista_menor.insert(0, num)
print(lista_maior, lista_menor)
        
