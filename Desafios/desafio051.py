from time import sleep
print(f'{10 * '='} PROGRESSÃO ARITIMÉTICA {10 * '='}')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um intervalo para mostrar a sequencia: '))
print(f'Você escolheu o numero {n1} em um intervalo de {n2} >> ')
sleep(1)
if n2 < 0:
    for c in range(n1 - n2, 0, n2):
        c += n2
        print(c)
else:
    for c in range(0, n1, n2):
        c += n2
        print(c)

