from time import sleep

def titulo(palavra):
    tam = len(palavra)
    print('=-'* tam)
    print(f'{palavra}'.center(tam * 2))
    print('=-'* tam)
titulo('Contagem de 1 até 10 de 1 em 1: ')

def contador_1():
    c = 1
    for c in range(1, 11):
        print(c, end='  ')
        sleep(0.5)
        c += 1
    print(' -> FIM')   
def contador_2():
    c = 0
    for c in range(10, -2, -2):
        print(c, end='  ')
        sleep(0.5)
    print(' -> FIM')
def contagem_personalizada(inicio, fim, passo):
    if passo == 0:
        passo = 1
        print('[ ATENÇÃO ] - Nao existe o passo 0 ! Automaticamente adicionado passo 1.')
    if fim < inicio:
        for c in range(inicio, fim - passo, - passo):
            print(c, end='  ')
            sleep(0.3)
    else:
        for c in range(inicio, fim + passo, passo):
            print(c, end='  ')
            sleep(0.3)
    print(' => FIM')

contador_1()
print('=-' * 32)
titulo('Contagem de 10 até 0 de 2 em 2: ')
contador_2()
print('=-' * 32)

print('Agora é a sua vez de personalizar a Contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))


contagem_personalizada(i, f, p)