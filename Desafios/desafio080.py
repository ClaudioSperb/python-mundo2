print(f'{40 * '='}')
print('COLOCANDO TUDO EM ORDEM'.center(40))
print(f'{40 * '='}')
lista_numeros = []
for c in range(5):
    num = int(input('Digite um numero: '))
    lista_numeros.append(num)
    maior_numero = max(lista_numeros)
    if num > maior_numero:
        lista_numeros.insert(-1, num)
        
