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

print("\n--- MATRIZ FORMATADA ---")
for linha in matriz:
    print(linha)
    
soma = sum(valores_linha1 + valores_linha2 + valores_linha3)
print(f'O valor total dos valores da matriz é {soma}')
