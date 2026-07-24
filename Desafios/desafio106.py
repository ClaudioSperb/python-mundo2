from time import sleep

# Lista/Tupla de cores ANSI

c = (
    '\033[0m',        # 0 - Sem cor (Reset)
    '\033[0;30;41m',  # 1 - Fundo Vermelho
    '\033[0;30;42m',  # 2 - Fundo Verde
    '\033[0;30;43m',  # 3 - Fundo Amarelo
    '\033[0;30;44m',  # 4 - Fundo Azul
    '\033[0;30;45m',  # 5 - Fundo Roxo
    '\033[7;30m'      # 6 - Fundo Branco (Invertido)
)

def titulo(palavra, cor=0):
    """
    -> Esse parametro serve para mudar o titulo e cor dependendo do assunto.
    Já esta configurado para ficar centralizado e entre '=-' conforme o
    tamanho da frase ou palavra.
    """
    tam = len(palavra)
    print(c[cor], end='')
    print('=-' * tam)
    print(f'{palavra}'.center(tam * 2))
    print('=-' * tam)
    print(c[0], end='')
    sleep(0.5)

def helpPython(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'')
    help(comando)
    print(c[0], end='')
    sleep(0.5)
    
#PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo('SISTEMA DE CONSULTAS DO PYTHON', 2)
    
    comando = str(input('Digite a Função ou Biblioteca: ')).strip().lower()
    if comando.upper() == 'FIM':
        print('FINALIZANDO CONSULTAS...')
        sleep(0.3)
        break
    else:
        print('Consultando...')
        sleep(0.5)
        helpPython(comando)
    
titulo('ATÉ LOGO', 1)