from time import sleep

print(20 * '-=')
print(f'{'CONTAGEM'}'.center(40))
print(20 * '-=')

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            cont += p
            sleep(0.3)
        print('=> FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            cont -= p
            sleep(0.3)
        print('=> FIM')
#PROGRAMA PRINCIPAL
contador(1, 10, 1)
print(20 * '-=')
contador(10, 0, 2)
print(20 * '-=')

print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('passo: '))
contador(ini, fim, pas)