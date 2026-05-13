senha_correta = 9742
senha = ''
while senha != senha_correta:
    senha = int(input('Digite sua senha: '))
    if senha != senha_correta:
        print('Acesso negado. Tente novamente')
        senha = int(input('Digite sua senha: '))
print('Acesso permitido')