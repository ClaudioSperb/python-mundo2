print(40 * '=')
print(f'LISTAGEM DE PESOS'.center(40))
print(40 * '=')
dados = []
pessoa = []
lista_leve = []
lista_pesado = []
pesos = []

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    res = str(input('Quer continuar [S / N]? ')).upper().strip()
    
    pessoa.append(nome)
    pessoa.append(peso)
    dados.append(pessoa.copy())
    pessoa.clear()
    
    
    if peso <= 70:
        lista_leve.append(nome)
        lista_leve.append(peso)
    else:
        lista_pesado.append(nome)
        lista_pesado.append(peso)
        
    if res == 'N':
        break


# print(f'No total, temos {len(dados)}pessoas cadastradas. ')
# print(f'Lista de pessoas a baixo de 70Kg >>>> {lista_leve}')
# print(f'Lista de pessoas a cima de 70Kg >>>> {lista_pesado}')