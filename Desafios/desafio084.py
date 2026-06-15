print(40 * '=')
print(f'LISTAGEM DE PESOS'.center(40))
print(40 * '=')
dados = []
pessoa = []
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(str(input('Peso: ')))
    res = str(input('Quer continuar [S / N]? ')).upper().strip()
    
    dados.append(pessoa.copy())
    pessoa.clear()
    
    if res == 'N':
        break
    
print(dados)