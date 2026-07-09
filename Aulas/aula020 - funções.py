def area_triangulo(x, y, z):
    a = (x * y) / z
    print(f'A área total do triângulo é {a}')

x = float(input('Digite o valor: '))
y = float(input('Digite o valor: '))
z = float(input('Digite o valor: '))

print(f'Voce digitou {x}, {y} e {z}.', end=' ')

area_triangulo(x, y, z)