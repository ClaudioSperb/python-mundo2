print(f'{10 * '-'} SOMANDO NÚMEROS {10 * '-'}')
soma = 0
while True:
    num = int(input('Digite um número inteiro [0 PARA SAIR]: '))
    if num == 0:
        break
    soma += num
print(f'A soma dos números digitados foi {soma}')