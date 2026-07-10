
def mensagem(msg):



    print('-=' * 30)
    print(f'{msg}'.center(60))
    print('-=' * 30)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [4, 6, 7, 3, 2]
dobra(valores)
print(valores)
mensagem('FIM DO PROGRAMA')