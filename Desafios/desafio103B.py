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
titulo('FICHA DO JOGADOR')

def ficha(jog = '< Desconhecido >', gol = 0):
    print(f'O jogador {jog} fez {gol} gol(s) na partida.')
    
#Programa Principal
n = str(input('Nome do Jogador: '))
g = str(input(f'Quantos gols {n} fez: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)