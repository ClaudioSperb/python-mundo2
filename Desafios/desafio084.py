print(40 * '=')
print(f'LISTAGEM DE PESOS'.center(40))
print(40 * '=')

lista_usuarios = []
lista_pesados = []
lista_leves = []

while True:
    nome = str(input('Qual seu nome: '))
    peso = float(input('Qual seu peso: '))
    res = str(input('Quer continuar [S / N]: ')).upper().strip()
    lista_usuarios.append(nome)
    lista_usuarios.append(peso)
    
    if peso >= 100 :
        lista_pesados.append(nome)
        lista_pesados.append(peso)
    else:
        lista_leves.append(nome)
        lista_leves.append(peso)
        
    if res == 'N':
        print('ENCERRANDO . . .')
        break
    
print(lista_usuarios)
print(lista_leves)
print(lista_pesados)