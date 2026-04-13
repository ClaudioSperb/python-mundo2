matriz = []

for l in range(0 , 3):
    linha = []
    for c in range(0 , 3):
        coluna = []
        num = int(input(f"Digite o valor para [{l}, {c}]: "))
        linha.append(num)
    matriz.append(linha)
    
for linha in matriz:
    print(linha)