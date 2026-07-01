from random import randint
from time import sleep
from operator import itemgetter

print('JOGO DOS NUMEROS')
print('=-' * 20)
numeros = []
num1 = randint(1, 6)
num2 = randint(1, 6)
num3 = randint(1, 6)
num4 = randint(1, 6)

jogadores = {
    'jogador1': num1,
    'jogador2': num2,
    'jogador3': num3,
    'jogador4': num4
}


for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
    
print('=-' * 20)

print('RANKING DOS JOGADORES')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for c, v in enumerate(ranking):
    print(f'O {c + 1}º Lugar: {v}')
    sleep(0.5)