print(f'{15 * '='} NOTAS ALUNOS {15 * '='}')
nomeAluno = str(input('Digite o nome do Aluno: ')).upper()
disciplinas = ['Matemática', 'Português', 'Filosofia', 'História', 'Física', 'Geografia', 'Química', 'Biologia']
nota = 0
notas = [7.8, 8.2, 9.5, 5.7, 9.8, 10, 6.4, 7.0]
for i in range(len(notas)):
    media = sum(notas) / len(notas)
    print(f'As notas do aluno {nomeAluno} na disciplina {disciplinas[i]} é {notas[i]}')
print(f'A média do aluno foi {media:.2f}')