numeros = []
numeros.append(1)
numeros.append(5)
numeros.append(9)

for c in numeros:
    print(f'{c}...')
    
for p, c in enumerate(numeros):
    print(f'Na posição {p} esta o numero {c}')
print('FIM')

for cont in range(0, 5):
    numeros.append(int(input('Digite um Numero: ')))
print(f'Na posição {p} esta o numero {c}')