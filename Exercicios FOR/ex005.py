from time import sleep
print(f'{15 * '='} ARMAZENANDO DADOS {15 * '='}')
lista_pessoas = []
for pessoa in range(0, 5):
    nome = str(input(f'Digite o nome do {pessoa + 1}º aluno: ')).capitalize()
    lista_pessoas.append(nome)
sleep(1)
print(f'Criando a lista ...')
print(f'{20 * '='}')
print(lista_pessoas)
print(' ')