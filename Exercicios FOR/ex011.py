print(f'{10 * '='} APLICANDO TAXAS DE AUMENTO {10 * '='}')
lista_valores = [1000, 500, 300, 700, 1000, 50, 65, 80, 900, 440]
aumento = 0.05
limite_preco = 500

for preco in lista_valores:
    if preco < limite_preco:
        novo_preco = preco * (1 + aumento)
    else:
        novo_preco = preco
    print(f'R${novo_preco:.2f}', end=' ')
