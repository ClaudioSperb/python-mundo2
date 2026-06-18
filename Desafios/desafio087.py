print(40 * '=')
print(f'COLETANDO DADOS DA MATRIZ'.center(40))
print(40 * '=')
soma = 0
matriz = []
maior = []
for l in range(9):  
    num = int(input(f'Digite o {l + 1}º Número: '))
    matriz.append(num)
    if num % 2 == 0:
        soma += num

print(15 * '=-')
print(f'[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]')
print(f'[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]')
print(f'[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]')
print(15 * '=-')

maior.append(matriz[3])
maior.append(matriz[4])
maior.append(matriz[5])
maior_numero = max(maior)


print(f'A soma dos numeros pares na matriz é de {soma}')
print(f'A soma dos numeros da 3ª coluna é {matriz[2] + matriz[5] + matriz[8]}')
print(f'O maior valor da linha 2 é o numero {maior_numero}')