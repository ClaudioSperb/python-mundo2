from time import sleep
print(f'{40 * '='}')
print('EXTRAINDO DADOS DE UMA LISTA'.center(40))
print(f'{40 * '='}')
lista_numeros = []
numeros_pares = []
numeros_ímpares = []
while True:
    num = int(input('Digite um NUMERO: '))
    print('Adicionando número . . .')
    sleep(1)
    print('Numero adicionado com sucesso !')
    lista_numeros.append(num)
    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_ímpares.append(num)
    pergunta = str(input('Quer continuar [S / N]? ')).upper().strip()
    if pergunta == 'N':
        print('Encerrando . . .')
        sleep(1)
        break
print(f'{40 * '~'}')
print(f'Os números digitados foram -> {lista_numeros}')
print(f'{40 * '~'}')
if not numeros_ímpares:
    print('Nenhum número [ÍMPAR] encontrado!')
else:
    print(f'Os números Ímpares em sua lista são -> {numeros_ímpares}')
if not numeros_pares:
    print('Nenhum número [PAR] encontrado! ')
else:
    print(f'Os números Pares em sua lista são -> {numeros_pares}')
