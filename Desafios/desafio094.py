print(30 * '=')
print(f'CADASTROS'.center(30))
print(30 * '=')

#LISTA GERAL - Onde quero guardar todos os dados do Dicionário.
lista_geral = []

#Dicionario de cadastro -Onde quero colocar os dados das pessoas antes de largar na lista Geral.
cadastro_pessoas = {}

while True:
    cadastro_pessoas['nome'] = str(input('Nome: ')).upper().strip()
    cadastro_pessoas['sexo'] = str(input('Sexo: [M / F] ')).upper().strip()
    cadastro_pessoas['idade'] = int(input('Idade: '))
    res = str(input('Quer continuar? [S / N] ')).upper().strip()
    lista_geral.append(cadastro_pessoas.copy())
    
    if res == 'N':
        print('Finalizando . . .')
        break
    
#Pegando o tamanho da lista
tot_pessoas = len(lista_geral)

#Somando as idades totais da lista geral
soma_idade = 0
for idade in lista_geral:
    soma_idade += idade['idade']

#Pegando a media da idade das pessoas cadastradas
media_idade = soma_idade / tot_pessoas

print(30 * '-=')
print(lista_geral)
print(30 * '-=')

print(f'Foram cadastradas {tot_pessoas} pessoas no total.')
print(f'A média de idade das pessoas cadastradas foi de {media_idade:.1f} anos')
    
print(f'As mulheres cadastradas foram: ', end=' ')
for pessoa in lista_geral:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
print()

print(30 * '-=')

print('Lista das pessoas com idade acima da média:')
for pessoa in lista_geral:
    if pessoa['idade'] >= media_idade:
        print(f'{pessoa['nome']} -> {pessoa['idade']} anos -> {pessoa['sexo']}')
        print(30 * '~~')
print('FIM DO CADASTRO - VOLTE SEMPRE')