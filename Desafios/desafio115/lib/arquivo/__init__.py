from Desafios.desafio115.lib.interface import cabecalho


def validando_arquivo(nome):
    try:
        a = open(nome, 'rt')
        # O 'rt' é de read text - ler arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        #Escrever arquivo de texto e adicionar/criar no sistema
        #O 'w' é de write - ler, O 't' é de text e o '+' - cria o arquivo
        a.close()
    except:
        print('Houve um ERRO inesperado. Tente mais tarde!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def relatorio_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabecalho(a.readlines())