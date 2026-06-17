from colorama import Fore
from time import sleep

print(40 * '=')
print(f'LISTAGEM DE PESOS'.center(40))
print(40 * '=')
dados = []
pessoa = []
peso_leve = []
peso_pesado = []


while True:
    nome = str(input('Nome: ')).upper()
    peso = float(input('Peso: '))
    res = str(input('Quer continuar [S / N]? ')).upper().strip()
    
    pessoa.append(nome)
    pessoa.append(peso)
    dados.append(pessoa.copy())
    pessoa.clear()
    
    #Adicionando os pesos nas listas conforme a condição
    # peso > 70 - lista - peso_pesado
    # peso <= 70 - lista - peso_leve
    
    if peso > 70:
        peso_pesado.append(peso)
    else:
        peso_leve.append(peso)
        
    
    if res == 'N':
        print('FINALIZANDO PROGRAMA . . .')
        sleep(1)
        break
    
menor = min(peso_leve)
maior = max(peso_pesado)
print(40 * '=')
#Pegando o nome e o menor peso da lista principal
print(f'A pessoa com menor peso foi', end=' ')
for n in dados:
    if menor == n[1]:
        print(f'{Fore.LIGHTGREEN_EX}[{n[0]}]{Fore.RESET}', end=' ')
print(f'com {menor}Kg')

#Pegando o nome e o maior peso da lista principal
print(f'A pessoa com maior peso foi', end=' ')
for n in dados:
    if maior == n[1]:
        print(f'{Fore.LIGHTRED_EX}[{n[0]}]{Fore.RESET}', end=' ')
print(f'com {maior}Kg')
print(40 * '=')
print(f'No total, temos {len(dados)} pessoas cadastradas. ')
