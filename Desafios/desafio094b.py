print(30 * '=')
print(f'CADASTROS'.center(30))
print(30 * '=')

cadastro_geral = []
pessoa = dict()


while True:
    pessoa['nome'] = (str(input('Nome: ')).upper().strip())
    pessoa['sexo'] = (str(input('Sexo: ')).upper().strip())
    pessoa['idade'] = (int(input('idade: ')))
    res = str(input('Quer continuar [S / N]: ')).upper().strip()
    
    cadastro_geral.append(pessoa.copy())
    
    
    if res == 'N':
        break
    
total_pessoas = len(cadastro_geral)

tot_idade = 0

for i, v in enumerate(cadastro_geral):
    tot_idade += v['idade']
    
media_idade = tot_idade / total_pessoas

        
print('=-' * 30)
print(cadastro_geral)
print('=-' * 30)
print(f'No total foram {total_pessoas} cadastradas.')
print(f'A media de idade das pessoas cadastradas é {media_idade:.1f} anos.')
print('=-' * 30)
#pegando somente as Mulheres
print('As mulheres cadastradas foram: ', end=' ')
for i, v in enumerate(cadastro_geral):
    if v['sexo'] == 'F':
        print(f'{v['nome']}', end=' ')
print('')
print('=-' * 30)

print('Pessoa com idade a cima da média => ', end=' ')
for c in cadastro_geral:
    if c['idade'] >= media_idade:
        print(c['nome'], end=' ')
print()
print('=-' * 30)
print('FIM DO CADASTRO'.center(60))
print()
