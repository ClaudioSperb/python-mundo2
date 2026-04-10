print(f'{10 * '='} ANALISADOR COMPLETO {10 * '='}')
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'{5 * '-'} {p}ª PESSOA {5 * '-'}')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip().upper()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'fF' and idade < 20:
            totmulher20 += 1
mediaIdade = somaIdade / 4
print(f'A média de idade do Grupo é {mediaIdade}')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
print('Fim do Programa')