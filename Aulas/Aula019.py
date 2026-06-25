print('DICIONÁRIOS "{}"')
dados = dict(
    nome = 'Claudio',
    idade = 36,
    peso = 98
)

print('=-' * 30)

print(dados.keys()) # Pega somente as Keys (chaves)
print(dados.items()) # Pega tudo que tem no dicionario
print(dados.values()) # Pega somente os valores das Keys

print('=-' * 30)
for k, v in dados.items():
    print(f'Na chave {k} temos o valor -> {v}')
print('=-' * 30)
    