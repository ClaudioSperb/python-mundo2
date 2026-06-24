from time import sleep
from colorama import Fore

print(40 * '=')
print(f'< BOLETIM ESCOLAR >'.center(40))
print(40 * '=')
dados_alunos = []

while True:
    nome = str(input('Nome: ')).upper().strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados_alunos.append([nome, [nota1, nota2], media])
    res = str(input('Quer continuar? [S / N] ')).upper().strip()
    
    if res == 'N':
        break
    
print(30 * '=-')

print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
for i, a in enumerate(dados_alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print(30 * '=-')
    opc = int(input('Mostrar nota de qual Aluno: [999 PARAR] '))
    if opc == 999:
        print('FINALIZANDO . . .')
        break
    if opc <= len(dados_alunos) - 1:
        print(f'Notas de {dados_alunos[opc][0]} são {dados_alunos[opc][1]}')
print('FIM DO PROGRAMA')