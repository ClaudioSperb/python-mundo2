def area(x, y):
    a = x * y
    print(f'A área total é {a}')

x = float(input('Digite o valor da base: '))
y = float(input('Digite o valor da altura: '))

print(f'Voce digitou {x} e {y}.', end=' ')

area(x, y)