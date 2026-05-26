import random
from time import sleep
while True:
    pergunta = str(input('Digite [0] para iniciar ou [999] para sair: '))
    print('Aguarde . . .')
    sleep(1)
    if pergunta == '999':
        print('Encerrando o Programa. Aguarde . . .')
        sleep(1)
        break
    numeros_aleatorios = tuple(random.randint(1, 10) for _ in range(5))
    maior_numero = max(numeros_aleatorios)
    menor_numero = min(numeros_aleatorios)
    print(f'Os números são -> {numeros_aleatorios}')
    print(f'{30 * '~'}')
    print(f'O numero maior foi o {maior_numero}')
    print(f'{30 * '~'}')
    print(f'O menor numero foi o {menor_numero}')
    print(f'{30 * '='}')
print('Obrigado por Participar !!! ')