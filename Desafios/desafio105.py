from colorama import Fore
from time import sleep

def titulo(palavra):
    """
    -> Esse parametro serve para mudar o titulo dependendo do assunto.
    Já esta configurado para ficar centralizado e entre '=-' conforme o
    tamanho da frase ou palavra.
    """
    tam = len(palavra)
    print('=-'* tam)
    print(f'{palavra}'.center(tam * 2))
    print('=-'* tam)
titulo('NOTAS ALUNOS')

def notas(*num, sit = True):
    """
    notas(*num, sit = True/False)
    -> Função que analisa as notas e a situação do aluno
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    :parametro num -> aceita 1 ou mais argumentos
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    :parametro sit -> aceita True ou False
    Para True - Mostra a situação do Aluno
    Para False - Mostra somente as notas e a média do Aluno
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    :return -> Retorna um dicionário com dados da maior nota, menor nota e media, quando True a situação do Aluno
    (APROVADO, RECUPERAÇÃO ou APROVADO)
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """
    resp = dict()
    resp['total'] = len(num)
    resp['maior_nota'] = max(num)
    resp['menor_nota'] = min(num)
    resp['media_aluno'] = sum(num) / resp['total']
    if sit == True:
        if resp['media_aluno'] < 6:
            print('Aguarde. . .')
            sleep(0.5)
            resp['situação_aluno'] = 'REPROVADO'
        elif resp['media_aluno'] < 8:
            print('Aguarde. . .')
            sleep(0.5)
            resp['situação_aluno'] = 'APROVADO - NA MÉDIA'
        else:
            print('Aguarde. . .')
            sleep(0.5)
            resp['situação_aluno'] = 'APROVADO'
    return resp

print()

#Programa Principal
print(notas(9.0, 8.0, 7.2, 8, 5, 7, 8.6, 10))
print('=-' * 30)
help(notas)