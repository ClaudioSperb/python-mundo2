print(30 * '=')
print(f'CADASTROS'.center(30))
print(30 * '=')

cadastro_geral = []
pessoa = dict()


while True:
    pessoa['nome'] = (str(input('Nome: ')).upper().strip())
    pessoa['sexo'] = (str(input('Sexo: ')).upper().strip())
    pessoa['ano_nascimento'] = (int(input('Ano Nascimento: ')))
    res = str(input('Quer continuar [S / N]: ')).upper().strip()
    
    cadastro_geral.append(pessoa.copy())
    
    
    if res == 'N':
        break
print('=-' * 30)
print(cadastro_geral)
print('=-' * 30)