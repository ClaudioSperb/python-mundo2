import sys
from colorama import Fore
from datetime import date, datetime


anoAtual = date.today().year
#print(anoAtual)
nome = str(input('Digite seu nome completo: ')).strip().upper()
anoNsacimento = int(input('Digite o ano do seu nascimento: '))
print('Digite [1] - MASCULINO\nDigite [2] - FEMININO: ')
escolhaSexo = int(input('Digite a opção: '))

if escolhaSexo == 1:
    print('Analisando dados....')
elif escolhaSexo == 2:
    print('No Brasil ainda nao temos obrigatoriedade de alistamento para Mulheres.')
    sys.exit()
else:
    print('Opção invalida')
    sys.exit()


tempoAlist = anoAtual - anoNsacimento - 18
tempoFaltaAlist = anoNsacimento + 18 - anoAtual
situaçãoAlist = str(input('Você ja se alistou? ')).strip().upper()


if anoAtual - anoNsacimento > 18 and situaçãoAlist == 'SIM' and escolhaSexo == 1:
    print(f'{Fore.LIGHTGREEN_EX}Voce esta em dia com o serviço obrigatório')
elif anoAtual - anoNsacimento < 17 and escolhaSexo == 1:
    print(f'Voce ainda nao precisa se Alistar, mas fique a vontade para conhecer mais sobre o {Fore.LIGHTGREEN_EX}Exerecito Brasileiro !!{Fore.RESET}')
    print(f'Faltam {tempoFaltaAlist} anos para voce se alistar !!! ')

if anoAtual - anoNsacimento == 17 and escolhaSexo == 1:
    print(f'Olá {nome}, você esta perto de se alistar para o serviço Militar.')
elif anoAtual - anoNsacimento == 18 and escolhaSexo:
    print(f'Ola {nome}, você precisa se Alistar esse ano, nao perca essa oportunidade !')
elif anoAtual - anoNsacimento > 19 and situaçãoAlist == 'NAO' and escolhaSexo == 1:
    print(f'Olá {nome}, {Fore.LIGHTRED_EX}verifique junto a Junta Militar, pois seu prazo ja passou.')
    print(f'{nome}, {Fore.LIGHTYELLOW_EX}Voce tinha que ter se alistado a {tempoAlist} anos !!!')

