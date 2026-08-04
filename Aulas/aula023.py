print('-=' * 30)
print(f'TRATAMENTO DE ERROS E EXCESSÕES'.center(60))
print('-=' * 30)
while True:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b
    except ZeroDivisionError:
        print('Não é possivel dividir um numero por zero')
    except KeyboardInterrupt:
        print('O usuário preferiu não informar os dados')
    except (ValueError, TypeError):
        print('Tivemos um problema com os tipos de dados digitados')
    else:
        print(f'O resultado é {r:.1f}')
    finally:
        print('Volte sempre!')