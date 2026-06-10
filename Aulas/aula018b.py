pessoas = []
dados = []
for p in range(3):
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Idade: ')))
    dados.append(pessoas.copy())
    pessoas.clear()
soma_maior = 0
soma_menor = 0
for p in dados:
    if p[1] >= 21:
        print(f'A pessoa {p[0]} tem {p[1]} anos de idade')
        print('É maior de idade!')
        print('')
        soma_maior += 1
    else:
        print(f'A pessoa {p[0]} tem {p[1]} anos de idade')
        print('É de menor idade!')
        print('')
        soma_menor += 1
print(f'No total, temos {soma_maior} pessoa maior de idade e {soma_menor} pessoas menor de idade')