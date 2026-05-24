lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(f'{lanche[::-1]}') # Inverte a ordem de trás pra frente
print(len(lanche)) # Tamanho da Tupla -> 4

# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi demais !!! ')

# for c in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[c]} {c + 1}º')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')