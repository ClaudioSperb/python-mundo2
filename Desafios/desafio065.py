from time import sleep
from colorama import Fore
print(f'{10 * '-'} MAIOR E MENOR VALOR {10 * '-'}')
res = 'S'
numeros = []
while res == 'S':
    num = int(input('Digite um número: '))
    res = str(input('Quer continuar? [ S / N]: ')).upper().strip()
    numeros.append(num)
#Criei as variaveis para media, soma e quantidade
soma = sum(numeros)
qntNumeros = len(numeros)
media = soma / qntNumeros
maiorNumero = max(numeros)
menorNumero = min(numeros)
sleep(1)
print(f'Você digitou {qntNumeros} Números.')
print(f'A soma de todos os numeros digitados é {soma}')
print(f'A média dos números digitados é {media}')
print(f'O maior número é {maiorNumero} e o menor é {menorNumero}')

