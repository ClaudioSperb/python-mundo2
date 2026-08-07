from Desafios.desafio115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Relatorio de Cadastro', 'Novo Cadastro' ,'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1 - \033[34mRELATÓRIO DE CADASTRO\033[m')
    elif resposta == 2:
        cabecalho('Opção 2 - \033[34mNOVO CADASTRO\033[m')
    elif resposta == 3:
        cabecalho('Encerrando o Sistema - Volte Sempre!')
        break
    else:
        print(f'\033[31m[ERRO]! - Digite uma opção válida!\033[m')
    sleep(1)