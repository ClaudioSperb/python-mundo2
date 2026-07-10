from time import sleep
def titulo(palavra):
    tam = len(palavra)
    print('=-'* tam)
    print(f'{palavra}'.center(tam * 2))
    print('=-'* tam)
titulo('PASSANDO NUMEROS E PEGANDO O MAIOR')

def maior(lista):
    for c in lista:
        print(c, end=' ')
        sleep(0.5)
    
    print('\nAnalisando os valores passados...')
    print(f'Foram informados {len(lista)} valores.')
    print(f'O maior numero é o {max(lista)}')
    print('=-' * 20)

nums = [9 , 8 , 5, 4, 2]
maior(nums)

nums = [5, 3, 7]
maior(nums)

nums = [2, 8]
maior(nums)

nums = []
if not nums:
    print('Nenhum numero encontrado')

