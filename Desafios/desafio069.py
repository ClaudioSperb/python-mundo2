from time import sleep
from colorama import Fore
pergunta = 'S'
total_pessoas = 0
total_homens = 0
total_mulheres = 0

while pergunta != 'N':
    print(f'{10 * '='} CADASTRO DE PESSOAS {10 * '='}')
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu Sexo: [F / M] -> ')).upper().strip()
    pergunta = str(input('Quer continuar? [S / N] ')).upper().strip()
    if idade > 17 and sexo == 'M' or sexo == 'F':
        total_pessoas += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 18:
        total_mulheres += 1
print(f'{Fore.RED}ANALISANDO DADOS ... {Fore.RESET}')
sleep(1)
print(f'Ao todo temos {Fore.CYAN}{total_pessoas}{Fore.RESET} pessoas cadastradas maiores de 18 anos. ')
print(f'Ao total, foram cadastrados {Fore.BLUE}{total_homens}{Fore.RESET} pessoas do sexo Masculino no programa.')
print(f'Ao total, foram cadastrados {Fore.MAGENTA}{total_mulheres}{Fore.RESET} pessoas do sexo Feminino menores de 18 Anos. ')
print('FIM DO CADASTRO')