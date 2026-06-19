print(40 * '=')
print(f'< BOLETIM ESCOLAR >'.center(40))
print(40 * '=')


while True:
    nome = str(input('Nome: ')).capitalize().strip()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    res = str(input('Quer continuar [S / N]: ')).capitalize().strip()
    media_nota = (nota_1 + nota_2 ) / 2
    
    dados_alunos = [nome,[nota_1, nota_2], [media_nota] ]
    dados_alunos.append(nome)
    dados_alunos.append(nota_1)
    dados_alunos.append(nota_2)
    dados_alunos.append(media_nota)
    
    
    if res == 'N':
        break
    

print(dados_alunos)
for n in dados_alunos:
    print(dados_alunos[0])
    print(dados_alunos[1])
    print(dados_alunos[2])