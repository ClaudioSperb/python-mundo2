print(f'{10 * '='} ANALISADOR COMPLETO {10 * '='}')
for p in range(1, 5):
    print(f'{5 * '-'} {p}ª PESSOA {5 * '-'}')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip().upper()