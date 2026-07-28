from colorama import Fore
from time import sleep

def titulo(msg):
    tam = len(msg)
    print('=-' * tam)
    print(msg.center(tam * 2))
    print('=-' * tam)
titulo('<< PEGANDO AS VOGAIS >>')

def vogais(texto):
    '''
    Função que escreve as vogais, e mostra na tela.
    :param texto: Recebe o argumento vinda da variavel palavra
    :return: Quantidade de vogais
    '''
    contador = 0
    print(f'Voce digitou a palavra {texto}. Temos as vogais => ', end=' ')
    for letra in texto:
        if letra in 'aeiou':
            print(f'{Fore.RED}{letra}{Fore.RESET}', end=' ')
            contador += 1
    return contador

#PROGRAMA PRINCIPAL
palavra = str(input('Digite uma palavra: ')).lower().strip()
total = vogais(palavra)
print(f'\nTemos {total} vogais no total')
