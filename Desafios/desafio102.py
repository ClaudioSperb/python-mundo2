from colorama import Fore

def titulo(palavra):
    tam = len(palavra)
    print('=-'* tam)
    print(f'{palavra}'.center(tam * 2))
    print('=-'* tam)
titulo('FATORIAL')

#Criando uma função que pega o Fatorial usando o FOR.
def fatorial(num = 1, show=False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual {fatorial(n)}')
