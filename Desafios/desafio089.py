print(40 * '=')
print(f'< BOLETIM ESCOLAR >'.center(40))
print(40 * '=')

lista_geral = []

while True:
    nome = str(input('Nome: ')).upper().strip()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    res = str(input('Quer continuar [S / N]: ')).capitalize().strip()
    media_nota = (nota_1 + nota_2 ) / 2
    
    dados_alunos = [nome,[nota_1, nota_2], media_nota ]
    lista_geral.append(dados_alunos)
 
    
    
    if res == 'N':
        break
print(40 * '=')
print(f'< BOLETIM ESCOLAR >'.center(40))
print(40 * '=')
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
for p , n in enumerate(lista_geral):
    print(f'{p:<4}{n[0]:<10}{n[2]:>8.1f}')
    print(30 * '-')

while True:
    aluno = int(input('Mostrar notas de qual aluno [ 999 ] para sair]: '))
    for n, a in enumerate(dados_alunos):
        if n == aluno:
            print(f'A nota do alunoª {dados_alunos[0]} >>> {dados_alunos[1]}')
    if aluno == 999:
        break