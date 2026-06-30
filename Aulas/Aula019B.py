print('Adicionando direto em listas dentro do Dicionário')
# Inicializamos o dicionário já com as chaves e listas vazias
estados = {
    'uf': [],
    'sigla': []
}

for c in range(3):
    # Dá um .append() direto na lista interna correspondente à chave
    estados['uf'].append(str(input('UF: ')).upper())
    estados['sigla'].append(str(input('Sigla: ')).upper())

print("\nDicionário final:")
print(estados)
