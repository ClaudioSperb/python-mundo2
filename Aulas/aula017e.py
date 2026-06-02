numeros = []

for c in numeros:
    print(f'{c}...')
    
for cont in range(0, 5):
    numeros.append(int(input('Digite um Numero: ')))
    
for p, c in enumerate(numeros):
    print(f'Na posição {p} esta o numero {c}')
print('FIM')
