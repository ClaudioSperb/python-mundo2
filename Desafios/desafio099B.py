from time import sleep
def titulo(palavra):
    tam = len(palavra)
    print('=-'* tam)
    print(f'{palavra}'.center(tam * 2))
    print('=-'* tam)
titulo('PASSANDO NUMEROS E PEGANDO O MAIOR')

def maior(* num):
    cont = maior = 0
    print(f'Analisando os valores passados.')
    for c in num:
        print(f'{c}', end=' ', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
        
    print(f'No total temos {cont} numeros cadastrados')
    print(f'O maior valor informado foi o {maior}')
    print()
    
maior(5, 8, 6, 1, 9)
maior(1, 5, 7, 2)
maior(2, 9, 4)
maior(0, 5)
maior(5)
maior()