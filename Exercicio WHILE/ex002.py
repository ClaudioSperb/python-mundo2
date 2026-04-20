from colorama import Fore
from time import sleep
print(f'{50 * '='}')
print(f'{15 * '='} SOMANDO TODOS OS NÚMEROS {15 * '='}')
print(f'{50 * '='}')
lista_numeros = []
pergunta = 0
res ='S'
while res == 'S':
    pergunta += 1
    num = int(input(f'Digite o {pergunta}º número: '))
    res = str(input('Quer adicionar mais números: [S / N]' )).upper()
    lista_numeros.append(num)
soma = sum(lista_numeros)
print(f'Você digitou esses números -> {lista_numeros}')
print(f'A soma dos valores digitados é {soma}')


    