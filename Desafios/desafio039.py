from datetime import date, datetime
anoAtual = date.today().year
#print(anoAtual)
nome = str(input('Digite seu nome completo: ')).strip().upper()
anoNsacimento = int(input('Digite o ano do seu nascimento: '))
situaçãoAlist = str(input('Você ja se alistou? ')).strip().upper()

if anoAtual - anoNsacimento > 18 and situaçãoAlist == 'SIM':
    print('Voce esta em dia com o serviço obrigatório')

if anoAtual - anoNsacimento == 17:
    print(f'Olá {nome}, você esta perto de se alistar para o serviço Militar.')
elif anoAtual - anoNsacimento == 18:
    print(f'Ola {nome}, você precisa se Alistar esse ano, nao perca essa oportunidade !')
elif anoAtual - anoNsacimento > 19 and situaçãoAlist == 'NAO':
    print(f'Olá {nome}, verifique junto a Junta Militar, pois seu prazo ja passou.')