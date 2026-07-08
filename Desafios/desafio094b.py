print(30 * '=')
print(f'CADASTROS'.center(30))
print(30 * '=')

cadastro_geral = []
pessoa = dict()

while True:
    pessoa['nome'] = str(input('Nome: ')).upper().strip()
    while True:
        pessoa['sexo'] = str(input('Sexo [M / F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Opção inválida ! Responda com M ou F. Tente novamente.')
    pessoa['idade'] = int(input('Idade: '))
    while True:
        resp = str(input('Quer continuar [S / N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Opção inválida. Responda S ou N. Tente Novamente')
        
print(pessoa)
print('=-' * 30)
print('FIM DO CADASTRO'.center(60))
print()
