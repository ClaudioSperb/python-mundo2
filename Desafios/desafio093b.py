from time import sleep
print(30 * '=')
print(f'ESTATÍSTICAS DE UM JOGADOR'.center(30))
print(30 * '=')

jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} Jogou: '))
    partidas.clear()
    for c in range(tot):
        partidas.append(int(input(f'Gols na partida {c + 1}: ')))
        
    jogador['gols'] = partidas.copy()
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S / N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)