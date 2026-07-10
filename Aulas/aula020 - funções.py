def area_triangulo(x, y, z):
    a = (x * y) / z
    print('=-' * 30)
    print(f'A área total do triângulo é {a}'.center(60))
    print('=-' * 30)
    
def mensagem(msg):
    print('-=' * 30)
    print(f'{msg}'.center(60))
    print('-=' * 30)
    
while True:
    x = float(input('Digite o valor para X: '))
    y = float(input('Digite o valor para Y: '))
    z = float(input('Digite o valor para Z: '))
    
    area_triangulo(x, y, z)
    
    res = str(input('Quer continuar: S / N ')).upper()[0]

    if res == 'N':
        break
mensagem('FIM DO PROGRAMA')