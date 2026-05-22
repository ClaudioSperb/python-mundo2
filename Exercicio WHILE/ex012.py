print(f'{10 * '='} EXERCITANDO UM POUCO {10 * '='}')
print('Digite quantos números quiser, para sair digite [N] ')
listaNumeros = []
resposta = ''
while True:
    n1 = int(input('Digite um Número: '))
    resposta = ''
    while resposta != 'N' and resposta != 'S':
        resposta = str(input('Quer continuar? [S / N]')).upper().strip()[0]
    listaNumeros.append(n1)
    if resposta == 'N':
        break
soma = sum(listaNumeros)
print(f'Você digitou esses números -> {listaNumeros}')
print(f'A Soma total dos números digitados é {soma}')
if soma % 2 == 0:
    print(f'O valor da soma é PAR')
else:
    print(f'O valor da soma é ÍMPAR')
maiorNumero = max(listaNumeros)
print(f'O maior número digitado é {maiorNumero}')