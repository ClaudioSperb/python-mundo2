from colorama import Fore
from time import sleep
print(f'{50 * '='}')
print(f'{15 * '='} CAIXA ELETRÔNICO {17 * '='}')
opc = 0
saldo = float(1500)
while opc != 4:
    print(f'''
        Seja Bem-Vindo
        
        Esolha a opção desejada:
        {Fore.GREEN}[1] - DEPOSITAR{Fore.RESET}
        {Fore.YELLOW}[2] - SACAR{Fore.RESET}
        {Fore.CYAN}[3] - SALDO NA TELA{Fore.RESET}
        {Fore.LIGHTMAGENTA_EX}[4] - SAIR{Fore.RESET}
      
      ''')
    opc = int(input('Digite a opção desejada: '))
    if opc == 1:
        sleep(1)
        print(f'SALDO ATUAL -> R${saldo:.2f}')
        deposito = float(input('Qual valor a ser depositado: R$ '))
        saldo += deposito
        print('Depositando...')
        sleep(1)
        print(f'Tudo certo, seu saldo atualizado é {Fore.LIGHTGREEN_EX}{saldo:.2f}{Fore.RESET}')
    elif opc == 2:
        sleep(1)
        saque = float(input('Digite o valor do saque desejado: R$ '))
        saldo -= saque
        print('Saque em Andamento....')
        sleep(1)
        print(f'pode Retirar o valor no local indicado')
        sleep(1)
        print(f'SALDO ATUALIZADO - R${saldo:.2f}')
        print(f'{20 * '='}')
        
        if saldo < 0:
          print('ATENÇÃO ! Você entrou no Cheque Especial')
          sleep(1)
          print(f'Seu saldo atual é {Fore.RED}R${saldo:.2f}{Fore.RESET}')
          
    elif opc == 3:
        print('AGUARDE ....')
        sleep(1)
        print(f'SALDO - R${saldo:.2f}')
    elif opc == 4:
      print('ESTAMOS ENCERRANDO ...')
      sleep(1)
      print('Tudo certo. Pode retirar seu cartão. ')
      print('PROGRAMA ENCERRADO')
    else:
      print('OPÇÃO INVALIDA.')
      sleep(1)
      print('COLOQUE A OPÇÃO DESEJADA >>> ')
      