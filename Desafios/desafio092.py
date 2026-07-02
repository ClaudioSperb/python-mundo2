from time import sleep
from colorama import Fore
from datetime import date

ano_atual = date.today().year

print(15 * '=-')
print(f'DADOS PESSAIS CLT'.center(30))
print(15 * '=-')

cadastro = {}
cadastro['nome'] = str(input('Nome: ')).upper()
cadastro['ano_nascimento'] = int(input('Ano Nascimento: '))
cadastro['clt'] = str(input('Possui Carteira de Trabalho (CLT): [S / N] ')).upper().strip()

if cadastro['clt'] == 'N':
    print('FINALIZANDO')
    sleep(0.5)
else:
    cadastro['ano_contratação'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Sálario: R$ '))
    cadastro['tempo_de_carteira'] = ano_atual - cadastro['ano_contratação']
    cadastro['tempo_para_se_aposentar'] = 35 - cadastro['tempo_de_carteira']
print('')
for k, v in cadastro.items():
    print(f'{Fore.LIGHTGREEN_EX}{k}{Fore.RESET} tem o valor {Fore.RED}{v}{Fore.RESET}')
    print(30 * '-')
    sleep(0.3)
    
print('')
print(f'==== FIM DO PROGRAMA ===='.center(30))
print('')