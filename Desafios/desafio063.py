from time import sleep
print(f'{50 * '-'}')
print(f'{10 * '='}SEQUENCIA DE FIBONACCI{10 * '='}')
numero = int(input('Quantos termos você quer mostrar:  '))
print(f'{50 * '-'}')
t1 = 0
t2 = 1
cont = 3
print('GERANDO SEQUENCIA >>> ')
sleep(1)
print(f'{t1} -> {t2}', end=' ')
while cont <= numero:
    t3 = t1 + t2
    cont += 1
    t1 = t2
    t2 = t3
    print(f' -> {t3}', end=' ')