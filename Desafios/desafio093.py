print(30 * '=')
print(f'ESTATÍSTICAS DE UM JOGADOR'.center(30))
print(30 * '=')

estatisticas_jogador = {
    'total_gols_jogador': []
}
gols = []

estatisticas_jogador['nome'] = str(input('Nome do Jogador: ')).capitalize().strip()
estatisticas_jogador['partidas'] = int(input(f'Quantas partidas {estatisticas_jogador["nome"]} fez? '))

if estatisticas_jogador['partidas'] == 0:
    print('Finalizando o Programa.')
if estatisticas_jogador['partidas'] > 0:
    for c in range(estatisticas_jogador['partidas']):
        gols.append(int(input(f'Quantos gols no {c + 1}º jogo: ')))
        
estatisticas_jogador['total_gols_jogador'] = gols.copy()
estatisticas_jogador['total_de_gols'] = sum(gols)


print(30 * '-=')
print(estatisticas_jogador)
print(30 * '-=')
print()

print(30 * '-')
for k, v in estatisticas_jogador.items():
    print(f'No campo {k} temos o valor {v}')
print(30 * '-')

print(f'O jogador {estatisticas_jogador['nome']} jogou {estatisticas_jogador['partidas']} Partidas.')
for k, v in enumerate(gols):
    print(f'     => Na partida {k + 1}, {estatisticas_jogador['nome']} fez {v} gols')
print(f'No total, {estatisticas_jogador['nome']} fez {estatisticas_jogador["total_de_gols"]} gols.')