from time import sleep
loginCorreto = 'Claudio'
senhaCorreta = 999019528
login = ''
senha = ''
while True:
    while login != loginCorreto:
        login = str(input('Digite seu usuario: ')).capitalize().strip()
        senha = ''
    while senha != senhaCorreta:
        senha = int(input('senha: '))
    print('LOGIN CONCLUIDO')
    sleep(1)
    print('. . .')
    if login == loginCorreto and senha == senhaCorreta:
        print('SEJA BEM VINDO')
        break
print('LOADING . . .')
sleep(1)
print('LOGIN EFETUADO COM SUCESSO')