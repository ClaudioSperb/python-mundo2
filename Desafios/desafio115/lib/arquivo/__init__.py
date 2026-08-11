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
        cabecalho('Opção 1 - \033[34mRELATÓRIO DE CADASTRO\033[m')
        print(a.read())
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()