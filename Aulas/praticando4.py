print(f'{15 * '='} NOTAS ALUNOS {15 * '='}')
nomeAluno = str(input('Digite o nome do Aluno: ')).upper()
disciplinas = ['Matemática', 'Português', 'Filosofia', 'História', 'Física', 'Geografia', 'Química', 'Biologia']

notas = [7.8, 8.2, 9.5, 5.7, 9.8, 10, 6.4, 7.0]
for i in range(len(notas)):
    print(f'As notas do aluno {nomeAluno} na disciplina {disciplinas[i]} é {notas[i]}')
    
