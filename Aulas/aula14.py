from tkinter import font
print(f'{10 * '='} ESTRUTURA WHILE {10 * '='}')

num = 1
par = 0
impar = 0
lista_par = []
lista_impar = []
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
            lista_par.append(num)
        else:
            impar += 1
            lista_impar.append(num)
print(f'Você digitou esses números pares -> {lista_par}')
print(f'Você digitou esses números ímpares -> {lista_impar}')