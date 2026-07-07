from time import sleep
print(30 * '=')
print(f'ESTATÍSTICAS DE UM JOGADOR'.center(30))
print(30 * '=')

jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
tot = int(input(f'Quantas partidas {jogador["nome"]} Jogou: '))

for c in range(tot):
    partidas.append(int(input(f'Gols na partida {c + 1}: ')))
    
jogador['gols'] = partidas.copy()
jogador['total'] = sum(partidas)

print('=-' * 30)
print(jogador)
print('=-' * 30)

for k, v in jogador.items():
    print(f'No campo {k} tem o valor {v}')
    sleep(0.5)
    
print('=-' * 30)

print(f'O jogador {jogador["nome"]}, jogou no total {len(jogador['gols'])} partidas.')

print('=-' * 30)

for i, v in enumerate(partidas):
    print(f'     => Na partida {i + 1} fez {v} gols')
    sleep(0.5)
print(f'No total o jogador {jogador['nome']} fez {jogador['total']} gols.')
print('')