from time import sleep

print(f'{"=" * 10} PROGRESSÃO ARITIMÉTICA {"=" * 10}')

n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão (intervalo): '))
qtd = int(input('Quantos termos você quer mostrar? '))

print(f'Você escolheu o número {n1} com razão {n2}')
sleep(1)

contador = 0
termo = n1

while contador < qtd:
    print(termo, end=' ')
    termo += n2
    contador += 1

print('... >>> ACABOU')