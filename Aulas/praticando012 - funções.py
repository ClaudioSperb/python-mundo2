from colorama import Fore
from time import sleep

numeros = []

def formar_triangulo(a, b, c):
    '''
    def formar_triangulo - Testa os numeros e retorna se pode formar um triangulo
    :param a: num1
    :param b: num2
    :param c: num3
    :return: Se forma ou nao um triangulo com os numeros passados nos parametros a, b e c
    '''


    print(f'{Fore.CYAN}ANALISANDO NÚMEROS{Fore.RESET}')
    sleep(0.5)
    print(f'Você digitou {a}, {b} e {c}')

    if a + b > c and a + c > b and b + c > a:
        return f'{Fore.GREEN}Pode formar um Triangulo{Fore.RESET}'
    else:
        return f'{Fore.RED}Não pode formar um Triângulo{Fore.RESET}'

#PROGRAMA PRINCIPAL
while True:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    num3 = int(input('Digite o último número: '))
    numeros.append(num1)
    numeros.append(num2)
    numeros.append(num3)

    #CHAMANDO A FUNÇÃO
    print(formar_triangulo(num1, num2, num3))

    res = str(input('Quer testar outros números? [S / N]: ')).upper()[0]

    if res == 'N':
        print("FINALIZANDO")
        sleep(0.5)
        break

print('FIM')
#help(formar_triangulo)