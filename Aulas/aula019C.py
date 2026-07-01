print('Experimentos com Dicionários')
estado = dict()
brasil = list()
for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: ')).upper()
    estado['sigla'] = str(input('Sigla: ')).upper()

    brasil.append(estado.copy())
#print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')
        print()