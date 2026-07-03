print(30 * '=')
print(f'CADASTROS'.center(30))
print(30 * '=')

#LISTA GERAL - Onde quero guardar todos os dados do Dicionário.
lista_geral = []

#Dicionario de cadastro -Onde quero colocar os dados das pessoas antes de largar na lista Geral.
cadastro_pessoas = {}

while True:
    cadastro_pessoas['nome'] = str(input('Nome: '))
    cadastro_pessoas['sexo'] = str(input('Sexo: [M / F] ')).upper().strip()
    cadastro_pessoas['idade'] = int(input('Idade: '))
    res = str(input('Quer continuar? [S / N] ')).upper().strip()
    lista_geral.append(cadastro_pessoas.copy())
    
    if res == 'N':
        print('Finalizando . . .')
        break
    
print(lista_geral)
