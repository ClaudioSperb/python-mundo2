from colorama import Fore

def titulo(palavra):
    """
    -> Esse parametro serve para mudar o titulo dependendo do assunto.
    Já esta configurado para ficar centralizado e entre '=-' conforme o
    tamanho da frase ou palavra.
    """
    tam = len(palavra)
    print('=-'* tam)
    print(f'{palavra}'.center(tam * 2))
    print('=-'* tam)
titulo('FATORIAL')

#Criando uma função que pega o Fatorial usando o FOR.
def fatorial(num = 1, show=False):
    """
    A função fatorial(num) retorna o fatorial de 'n' vinda do Input.
    -> Esse parametro é obrigatorio para o sistema prosseguir.
    -> O parametro show é opcional, se for True - ele mostra a sequencia de numeros antes do valor final, se for False - ele retorna somente o fatorial.

    """
    f = 1
    for c in range(num, 0, -1):
        if show == True:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#Programa principal
n = int(input('Digite um número: '))
print(f'{fatorial(n, True)}')

help(titulo)
help(fatorial)