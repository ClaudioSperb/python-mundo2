print(f'{15 * '='} NOTAS ALUNOS {15 * '='}')
lista_notas = []
mediaNotas = 0
while True:
    notaPortugues = float(input('Digite sua nota de Português: '))
    notaMatematica = float(input('Digite sua nota de Matematica: '))
    notaGeografia = float(input('Digite sua nota de Geografia: '))
    notaBiologia = float(input('Digite sua nota de Biologia: '))
    notaQuimica = float(input('Digite sua nota de Quimica: '))
    res = str(input('Deseja sair? [S / N ]')).upper().strip()
    
#ADICIONANDO NA LISTA DE NOTAS
    lista_notas.append(notaMatematica)
    lista_notas.append(notaPortugues)
    lista_notas.append(notaBiologia)
    lista_notas.append(notaGeografia)
    lista_notas.append(notaQuimica)
    somaNota = sum(lista_notas)
    mediaNotas = somaNota / 5
    
    if mediaNotas < 5:
        print(f'Você está Reprovado. Sua média foi {mediaNotas}')
    if mediaNotas > 6 and mediaNotas < 8:
        print(f'Você está Aprovado, sua média foi {mediaNotas}. Estude Mais !')
    if mediaNotas > 8:
        print(f'Você foi aprovado acima da média, sua média foi {mediaNotas}. Parabens')
    if res != 'S':
        break
print('FIM DO PROGRAMA!')