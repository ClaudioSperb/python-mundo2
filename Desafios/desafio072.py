from colorama import Fore
from time import sleep

numeros = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um Número de 0 a 20 [999 Para Sair -> ]: '))
    print(f'{50 * '~'}')
    print('Processando Número . . .')
    sleep(1)
    if numero == 999:
        print(f'Saindo . . .')
        break
    if numero < 0 or numero > 20:
        print(f'{Fore.RED}Numero inválido{Fore.RESET}. Digite um numero de 0 a 20')
        numero = int(input('Digite um Número de 0 a 20: '))
    if numero == 999:
        print(f'Saindo . . .')
        break
    print(f'Você digitou o numero {Fore.GREEN}{numeros[numero]}{Fore.RESET}')
    print(f'{50 * '='}')
print('Obrigado por Participar !!!')
    