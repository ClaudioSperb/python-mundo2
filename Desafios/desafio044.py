from colorama import Fore
from time import sleep


valorProduto = float(input('Digite o valor do produto:R$ '))
aVista = valorProduto - (valorProduto * (10 / 100))
aVistaCartao = valorProduto - (valorProduto * (5 / 100))
tresVezesCartao = valorProduto + (valorProduto * (20 / 100))

pagamento = int(input(f'Escolha a forma de pagamento digitando o numero correspondente: \n{Fore.LIGHTGREEN_EX}[0] - Pagamento a vista{Fore.RESET}, {Fore.LIGHTCYAN_EX}[1] - A vista no Cartão{Fore.RESET}, {Fore.LIGHTRED_EX}[2] - 3x no Cartão{Fore.RESET}, {Fore.LIGHTYELLOW_EX}[3] - em até 2x Valor normal{Fore.RESET}: '))
print('')
sleep(1.5)
if pagamento == 0:
    print(f'O valor do produto a Vista fica {Fore.LIGHTGREEN_EX}R${aVista:.2f}{Fore.RESET}. Você ganhou 10% de desconto !')
elif pagamento == 1:
    print(f'O valor do produto a vista no cartão fica {Fore.LIGHTCYAN_EX}R${aVistaCartao:.2f}{Fore.RESET}. Você ganhou 5% de desconto !')
elif pagamento == 2:
    print(f'O valor em 3x no cartão fica {Fore.LIGHTRED_EX}R${tresVezesCartao:.2f}{Fore.RESET}. Voce teve acréscimo de 20% de Juros !')
else:
    print(f'O valor em 2x no carão fica {Fore.LIGHTYELLOW_EX}R${valorProduto:.2f}{Fore.RESET}. Você pagou o valor normal !')
