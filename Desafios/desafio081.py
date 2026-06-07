from time import sleep
print(f'{40 * '='}')
print('EXTRAINDO DADOS DE UMA LISTA'.center(40))
print(f'{40 * '='}')
lista_numeros = []
num = ''
while True:
    num = int(input('Digite um NUMERO: '))
    lista_numeros.append(num)
    pergunta = str(input('Quer continuar [S / N]? ')).upper().strip()
    if pergunta == 'N':
        print('Saindo ...')
        sleep(1)
        break
lista_numeros.sort(reverse=True)
print(f'{40 * '='}')
if 5 not in lista_numeros:
    print('O numero 5 não foi digitado')
else:
    print('Em sua lista contem o Número [5]')
print(f'Você digitou {len(lista_numeros)} numeros.')
print(lista_numeros)



