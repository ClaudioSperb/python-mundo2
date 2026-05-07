print(f'{10 * '='} VARIOS NÚMEROS COM FLAGS {10 * '='}')
num = res = soma = 0
while num != 999:
    res = int(input('Digite um número: [<<< Digite 999 para sair >>>] '))
    if res == 999:
        break
    soma += res
    num += 1
print(f'Você digitou {num} números e a soma entre eles {soma}.')
print('FIM')