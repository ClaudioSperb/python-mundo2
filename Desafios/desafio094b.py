print(30 * '=')
print(f'CADASTROS'.center(30))
print(30 * '=')

cadastro_geral = {}
pessoa = []

while True:
    pessoa.append(str(input('Nome: ')).upper())
    pessoa.append(str(input('Sexo: ')).upper())
    pessoa.append(int(input('Ano Nascimento: ')))
    cadastro_geral['pessoa'] = pessoa.copy()
    
    res = str(input('Quer continuar [S / N]: ')).upper()
    
    
    if res == 'N':
        break
    
print()
print(cadastro_geral)