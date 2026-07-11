from time import sleep
from random import randint

def titulo(palavra):
    tam = len(palavra)
    print('=-'* tam)
    print(f'{palavra}'.center(tam * 2))
    print('=-'* tam)
titulo('SORTEANDO NUMEROS E ANALISANDO')

numeros = []

def sorteio():
    for c in range(5):
        num = randint(0, 5)
        numeros.append(num)
    print('Sorteando 5 numeros => ', end=' ', flush=True)
    for c in numeros:
        print(c, end=' ', flush=True)
        sleep(0.3)
    print('')
sorteio()

def par():
    tot = 0
    for n in numeros:
        if n % 2 == 0:
            tot += n
    print(f'Na lista {numeros} a soma dos pares é {tot}')   
par()
print('=-' * 30)