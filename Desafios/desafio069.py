from time import sleep
from colorama import Fore
total_pessoas_maior = total_mulheres = total_mulheres_menor = total_homens = 0
sexo = ''
pergunta = ''
while pergunta != 'N':
    print(f'{15 * '='} CADASTRO EM ANDAMENTO {15 * '='}')
    idade = int(input('Digite sua idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite seu Sexo [F / M]: ')).upper().strip()
    while pergunta != 'S' and pergunta != 'N':
        pergunta = str(input('Você quer continuar [S / N]: ')).upper().strip()

    if pergunta == 'N' and idade >= 18 and sexo == 'M':
        print(f'{Fore.RED}FINALIZANDO O CADASTRO ...{Fore.RESET}')
        sleep(1)
        total_pessoas_maior += 1
        total_homens += 1
        break
    elif pergunta == 'N' and idade >= 18 and sexo == 'F':
        print(f'{Fore.RED}FINALIZANDO O CADASTRO ...{Fore.RESET}')
        sleep(1)
        total_pessoas_maior += 1
        total_mulheres += 1
        break
    elif pergunta == 'N' and idade < 18 and sexo == 'F':
        print(f'{Fore.RED}FINALIZANDO O CADASTRO ...{Fore.RESET}')
        sleep(1)
        total_mulheres_menor += 1
        break

    #VALIDANDO A MAIORIDADE
    if idade >= 18:
        total_pessoas_maior += 1
    #VALIDANDO SE É DO SEXO MASCULINO
    if sexo == 'M':
        total_homens += 1

    #VALIDANDO SE É MENOR E DO SEXO FEMININO
    if sexo == 'F' and idade < 18:
        total_mulheres_menor += 1
print(f'{86 * '='}')
print(f'O total de pessoas cadastrados de maior idade foi de {total_pessoas_maior}.')
print(f'O total de pessoas do {Fore.LIGHTBLUE_EX}sexo Masculino{Fore.RESET} cadastrados foram de {total_homens} homens')
print(f'O total de pessoas do {Fore.LIGHTMAGENTA_EX}sexo Feminino{Fore.RESET} menores de 18 anos cadastrados foram de {total_mulheres_menor} mulheres')