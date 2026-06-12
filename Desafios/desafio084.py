print(40 * '=')
print(f'LISTAGEM DE PESOS'.center(40))
print(40 * '=')

lista_usuarios = []
lista_pesados = []
lista_leves = []

while True:
    nome = str(input('Qual seu nome: '))
    peso = float(input('Qual seu peso: Kg'))
    res = str(input('Quer continuar [S / N]: ')).upper().strip()
    lista_usuarios.append(nome)
    lista_usuarios.append(peso)
    
    
    
    if res == 'N':
        print('ENCERRANDO . . .')
        break
        
    
    
print(lista_usuarios)