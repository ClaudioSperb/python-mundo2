from colorama import Fore
from time import sleep
print(f'{15 * '='} {Fore.GREEN}Classificação{Fore.RESET} do {Fore.YELLOW}Brasileirão{Fore.RESET} {Fore.LIGHTCYAN_EX}2026{Fore.RESET} {15 * '='}')
timesSerieA = ('Palmeiras', 'Flamengo', 'Fliuminense', 'Altlético Paranaense', 'São Paulo', 'Bragantino', 'Coritiba', 'Bahia', 'Cruzeiro', 'Botafogo', 'EC Vitória', 'Atletico-MG', 'Internacional', 'Grêmio', 'Vasco da Gama', 'Corinthians', 'Santos', 'Mirassol', 'Remo', 'Chapecoense')

for pos,time in enumerate(timesSerieA):
    print(f'{pos + 1}º - {time}')
print('')
print(f'Os primeiros cinco Colocados da tabela são: {timesSerieA[0:5]}')
print(f'{136 * '~'}')
print(f'Os quatro últimos Colocados da tabela são: {timesSerieA[-4:]}')
print(f'{88 * '~'}')
print(f'Times em ordem Alfabética: {Fore.CYAN}{sorted(timesSerieA)}{Fore.RESET}')
print(f'O {timesSerieA[-1]} está na {Fore.LIGHTRED_EX}{timesSerieA.index('Chapecoense') + 1}ª Posição{Fore.RESET}')