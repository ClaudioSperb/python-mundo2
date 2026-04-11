alunos = ('Briana', 'Josiane', 'Claudio', 'Maria', 'Pedro')
for aluno in alunos:
    print(f'Ola {aluno}, seja bem-vindo')
    print(f'{15 * '='}')
print('Boa Aula')

# for numero in range(0, 100, 3):
#     print(numero, end=' ')

for idx in range(len(alunos)):
    print(alunos[idx], end=' ')