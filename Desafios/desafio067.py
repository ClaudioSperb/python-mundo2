from time import sleep
print(f'{10 * '='} GERANDO TABUADAS {10 * '='}')
mult = c = 1
print(f'{38 * '='}')
while True:
    num = int(input('Digite um número para ver a sua tabuada: '))
    for c in range(1, 11):
        mult = num * c
        if num < 0:
            break
        print(f'{num} x {c} = {mult}')
    if num < 0:
        break
    print(f'{38 * '='}')
sleep(1)
print('Encerrando o programa')