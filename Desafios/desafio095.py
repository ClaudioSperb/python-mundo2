print(30 * '=')
print(f'ESTATÍSTICAS DE UM JOGADOR'.center(30))
print(30 * '=')

estatisticas_jogador = {
}
jogadores = []
#Pegando os nomes dos jogadores
while True:
    estatisticas_jogador['nome'] = str(input('Nome do jogador: ')).upper().strip()
    estatisticas_jogador['partidas'] = int(input(f'Quantas partidas {estatisticas_jogador["nome"]} jogou: '))
    if estatisticas_jogador['partidas'] > 0:
        for c in range(estatisticas_jogador['partidas']):
            estatisticas_jogador['gols_na_partida'] = int(input(f'Quantos gols na {c + 1}ª partida: '))
            jogadores.append(estatisticas_jogador.copy())

         
            
    res = str(input('Quer continuar? S / N ')).upper()
    if res == 'N':
        break
print(estatisticas_jogador)
print(jogadores)
    
    
            
