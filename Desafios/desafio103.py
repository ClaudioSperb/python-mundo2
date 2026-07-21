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


def ficha(nome, gols):
    return f'O jogador {nome} fez {gols} gols no campeonato'


jogador = str(input('Nome do Jogador: '))
gol_jogador = str(input(f'Quantos gol {jogador} fez: '))

if not jogador:
    jogador = '<DESCONHECIDO>'
if not gol_jogador:
    gol_jogador = '0'

print(ficha(jogador, gol_jogador))