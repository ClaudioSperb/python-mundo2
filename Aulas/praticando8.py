valores_linha1 = []
valores_linha2 = []
valores_linha3 = []
for i in range(0, 3):
    numEscolha = int(input('Digite um numero: '))
    valores_linha1.append(numEscolha)
for i in range(0, 3):
    numEscolha = int(input('Digite um numero: '))
    valores_linha2.append(numEscolha)
for i in range(0, 3):
    numEscolha = int(input('Digite um numero: '))
    valores_linha3.append(numEscolha)
matriz = [valores_linha1, valores_linha2, valores_linha3]
    
print(f'{valores_linha1}')
print(f'{valores_linha2}')
print(f'{valores_linha3}')
