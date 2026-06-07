print(f'{40 * '='}')
print('COLOCANDO TUDO EM ORDEM'.center(40))
print(f'{40 * '='}')
lista_numeros = []

for c in range(5):
    num = int(input('Digite um numero: '))
    if c == 0 or num > lista_numeros[-1]:
        lista_numeros.append(num)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista_numeros):
            if num <= lista_numeros[pos]:
                lista_numeros.insert(pos, num)
                print(f'Valor adicionado na posição {pos} da lista ...')
                break
            pos += 1
print(f'Os valores digitados foram {lista_numeros}')