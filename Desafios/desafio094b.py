print(30 * '=')
print(f'CADASTROS'.center(30))
print(30 * '=')

cadastro_geral = []
pessoa = dict()
soma = media = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).upper().strip()
    while True:
        pessoa['sexo'] = str(input('Sexo [M / F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Opção inválida ! Responda com M ou F. Tente novamente.')
    pessoa['idade'] = int(input('Idade: '))
    cadastro_geral.append(pessoa.copy())
    soma += pessoa['idade']
    while True:
        resp = str(input('Quer continuar [S / N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Opção inválida. Responda S ou N. Tente Novamente')
    if resp == 'N':
        break
media = soma / len(cadastro_geral)
print(' ')
print(f'A)  Ao todo, temos {len(cadastro_geral)} pessoas cadastradas.')
print('=-' * 30)
print(f'B)  A média de idade das pessoas cadastradas é de {media:.0f} anos.')
print('=-' * 30)
print(f'C)  As mulheres cadastradas foram => ', end=' ')
for p in cadastro_geral:
    if p['sexo'] == 'F':
        print(f'{p['nome']}', end=' ')
print('')
print('=-' * 30)
print('D)  Lista das pessoas com idade acima da média => ')
for p in cadastro_geral:
    if p['idade'] >= media:
        print('    ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v} ; ', end=' ')
        print()
print('=-' * 30)
print('FIM DO CADASTRO'.center(60))
print()
