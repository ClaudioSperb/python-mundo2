print(40 * '=')
print(f'< BOLETIM ESCOLAR >'.center(40))
print(40 * '=')

dados_alunos = []

while True:
    nome = str(input('Nome: ')).capitalize().strip()
    nota_1 = float(input('Nota 1: '))
    nome_2 = float(input('Nota 2: '))
    res = str(input('Quer continuar [S / N]: ')).capitalize().strip()
    dados_alunos.append(nome)
    dados_alunos.append(nota_1)
    dados_alunos.append(nome_2)
    
    if res == 'N':
        break
    
print(dados_alunos)