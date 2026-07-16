from datetime import date
from colorama import Fore

def titulo(palavra):
    tam = len(palavra)
    print('=-'* tam)
    print(f'{palavra}'.center(tam * 2))
    print('=-'* tam)
titulo('SISTEMAS DE VOTO')

ano_atual = date.today().year
def voto(status):
    validando_ano = ano_atual - ano_nascimento
    if validando_ano < 16:
        return print(f'Você tem {validando_ano} anos >>> {Fore.RED}NEGADO!!!{Fore.RESET} Você ainda não tem idade para votar')
    elif validando_ano >= 18 and validando_ano < 60:
        return print(f'Você tem {validando_ano} anos >>> {Fore.GREEN}VOTO OBRIGATÓRIO{Fore.RESET}')
    elif validando_ano >= 60 or validando_ano >= 16 or validando_ano <= 17:
        return print(f'Você tem {validando_ano} anos >>> O voto é {Fore.YELLOW}OPCIONAL!{Fore.RESET}')
    else:
        print('Ano Inválido')
        
        
while True:    
    ano_nascimento = int(input('Qual ano do seu nascimento: '))
    voto(ano_nascimento)
    res = str(input('Quer continuar [S / N ]: ')).upper()[0]
    
    if res == 'N':
        print('=== FIM DO PROGRAMA ===')
        break
    print('-=' * 30)
