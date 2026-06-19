print(40 * '=')
print(f'< BOLETIM ESCOLAR >'.center(40))
print(40 * '=')

lista_geral = []

while True:
    nome = str(input('Nome: ')).capitalize().strip()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    res = str(input('Quer continuar [S / N]: ')).capitalize().strip()
    media_nota = (nota_1 + nota_2 ) / 2
    
    dados_alunos = [nome,[nota_1, nota_2], media_nota ]
    lista_geral.append(dados_alunos)
 
    
    
    if res == 'N':
        break
    

for p , n in enumerate(lista_geral):
    print(p, n[0], n[2])
    