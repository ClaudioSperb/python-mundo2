def mensagem(msg):
    print('-=' * 30)
    print(f'{msg}'.center(60))
    print('-=' * 30)

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')



mensagem('EMPACOTAMENTO NO PYTHON')

contador(1,2,3,4,5)
contador(1, 2 ,4, 5, 7)
contador(3, 5, 6, 3, 7, 5)
