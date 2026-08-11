from Desafios.desafio115.lib.interface import *
from Desafios.desafio115.lib.arquivo import *
from time import sleep

arq = 'arquivo_cadastro.txt'
if not validando_arquivo(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Relatorio de Cadastro', 'Novo Cadastro' ,'Sair do Sistema'])

    if resposta == 1:
        sleep(1)
        relatorio_arquivo(arq)
        sleep(2)

    elif resposta == 2:
        cabecalho('Opção 2 - \033[34mNOVO CADASTRO\033[m')
        nome = str(input('Nome:')).title()
        idade = validando_numero_inteiro('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Encerrando o Sistema - Volte Sempre!')
        sleep(1)
        break
    else:
        cabecalho(f'\033[31m[ERRO]! - Digite uma opção válida!\033[m'.center(48))
