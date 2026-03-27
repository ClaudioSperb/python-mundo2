from time import sleep
from colorama import init, Fore

nomeCliente = str(input('Digite o nome do cliente: ')).strip().upper()
valorSalario = float(input('Digite o salário atualizado do comprador: '))
valorCasa = float(input('Digite o valor da casa: '))
tempoPrestação = int(input('Digite quantas parecelas desejadas: '))
anosParcela = tempoPrestação / 12
valorPrestação = valorCasa / tempoPrestação
validando = valorSalario * (30 / 100)
salarioValidado = valorSalario - validando
print(f'O valor a ser financiado é de {valorCasa:.2f}.')
print('_-_' * 30)
print(f'A quantidade de parcelas serão de {tempoPrestação} vezes - {anosParcela:.2f} anos')
print('_-_' * 30)
print(f'O valor da parcela é de R${valorPrestação:.2f} reais')
print('Analisando Crédito . . .')
print('_-_' * 30)
sleep(2)
if valorPrestação > salarioValidado:
    print(f'{Fore.LIGHTRED_EX}Crédito NÃO APROVADO{Fore.RESET} Verifique a documentação.')
else:
    print(f'Parabens {nomeCliente} !!! , seu credito foi {Fore.LIGHTGREEN_EX}APROVADO{Fore.RESET}')