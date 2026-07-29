from uteis import fatorial, dobro, triplo, titulo

titulo('MODULOS E PACOTES')
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')