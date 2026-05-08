from random import randint
from time import sleep
print(f'{10 * '='} JOGO DO PAR OU ÍMPAR {10 * '='}')
numHumano = 0
vitoria = 0
while True:
    numHumano = int(input('Digite um número: '))
    resHumano = str(input('Digite a opção desejada: [P / I]: ')).upper().strip()
    numComputador = randint(0,10)
    soma = numComputador + numHumano
    if soma % 2 == 0 and resHumano == 'P':
        print(f'Você escolheu [ PAR ] e o numero {numHumano} e o computador o numero {numComputador}')
        print(f'A soma dos numeros deu {soma} é PAR')
        print('VOCÊ VENCEU !!!! ')
        vitoria += 1
    elif soma % 2 == 1 and resHumano == 'I':
        print(f'Você escolheu [ IMPAR ] e o numero {numHumano} e o computador o numero {numComputador}')
        print(f'A soma dos numeros deu {soma} é ÍMPAR')
        print('VOCÊ VENCEU !!!! ')
        vitoria += 1
    elif soma % 2 == 0 and resHumano == 'I':
        print(f'Você escolheu [ IMPAR ] e o numero {numHumano} e o computador o numero {numComputador}')
        print(f'A soma dos numeros deu {soma} é PAR')
        print(f'{48 * '='}')
        print('GAME OVER - VOCÊ PERDEU !!!! ')  
        break
    elif soma % 2 == 1 and resHumano == 'P':
        print(f'Você escolheu [ PAR ] e o numero {numHumano} e o computador o numero {numComputador}')
        print(f'A soma dos numeros deu {soma} é ÍMPAR')
        print(f'{48 * '='}')
        print('GAME OVER - VOCÊ PERDEU !!!! ')
        break
print(f'Você ganhou {vitoria} Vezes !!! ')
print('FIM DO JOGO')