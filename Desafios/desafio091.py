from random import randint
from time import sleep

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

numeros.append(num1)
numeros.append(num2)
numeros.append(num3)
numeros.append(num4)


for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
    
print('=-' * 20)

print('RANKING DOS JOGADORES')
numeros.sort()

