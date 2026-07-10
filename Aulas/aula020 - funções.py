def soma(a, b):



    s = a + b
    print('=-' * 30)
    print(f'A soma dos valores digitados é {s}'.center(60))
    print('=-' * 30)
    
def mensagem(msg):



    print('-=' * 30)
    print(f'{msg}'.center(60))
    print('-=' * 30)

lista_resultados = []
while True:
    a = float(input('Digite o valor para A: '))
    b = float(input('Digite o valor para B: '))
    
    soma(a, b)
    res = str(input('Quer continuar: S / N ')).upper()[0]

    if res == 'N':
        break
mensagem('FIM DO PROGRAMA')