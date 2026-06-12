print(40 * '=')
print(f'LISTAGEM DE PESOS'.center(40))
print(40 * '=')

lista_usuarios = []
lista_pesados = []
lista_leves = []

while True:
    lista_usuarios.append(str(input('Qual seu nome: ')).capitalize())
    lista_usuarios.append(float(input('Qual seu peso: ')))
    res = str(input('Quer continuar [S / N]: ')).upper().strip()
    
    if lista_usuarios[1] >= 100:
        lista_pesados.append(lista_usuarios.copy()) 
        lista_usuarios.clear()
    else:
        lista_leves.append(lista_usuarios.copy())
        lista_usuarios.clear()
        
    if res == 'N':
        print('ENCERRANDO . . .')
        break
    
print(lista_usuarios)