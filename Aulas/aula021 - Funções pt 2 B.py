def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um numero: '))
if par(num):
    print('É Par')
else:
    print('É Impar')


# def somar(a=0, b=0):
#     s = a + b
#     return s
# # a1 = int(input('Digite um numero: '))
# # a2 = int(input('Digite um numero: '))

# # print(f'A soma de {a1} + {a2} é {somar(a1, a2)}')

# print(somar(2, 6))