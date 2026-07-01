from colorama import Fore
print(f'SITUAÇÃO ALUNO')
aluno = {}
aluno['nome'] = str(input('Nome: ')).upper()
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
print('=-' * 15)
for k, v in aluno.items():
    print(f'{k} é -> {v}')

if aluno['media'] > 6:
    aluno['situação'] = 'Aprovado'
    print(f'A situação é -> {Fore.GREEN}APROVADO{Fore.RESET}')
else:
    aluno['situação'] = 'Reprovado'
    print(f'A situação é -> {Fore.RED}REPROVADO{Fore.RESET}')
print('=-' * 15)