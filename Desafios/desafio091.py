from random import randint
from time import sleep

print('JOGO DOS NUMEROS')
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
for c in range(1):
    numeros.append(jogadores.values())

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
numeros.sort()
print('RANKING DOS JOGADORES')
for c in (numeros):
    print(f'{c + 1}º Lugar - ')



