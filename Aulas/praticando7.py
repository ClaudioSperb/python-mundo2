vogais = ['a', 'e', 'i', 'o', 'u']
numeros = [1, 2, 3, 4, 5]
for i in vogais:
    print(i, end='')
    print('')
for i in range(len(vogais)):
    print(f'A vogal {vogais[i].upper()} é o número {numeros[i]}')