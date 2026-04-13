#PRATICANDO COM FOR
from colorama import Fore
lista_produtos = ["faca", "garfo", "panela", "frigideira", "flavorstone"]
lista_precos = [10, 10, 200, 50, 300]

# for item in lista_produtos:
#     print(item.upper())
# print(f'{30 * '=-'}')

# for item in lista_precos:
#     imposto = item * ( 10 / 100) + item
#     print(f'O item R${Fore.LIGHTBLUE_EX}{item:.2f}{Fore.RESET} adicinando seu imposto de 10% fica {Fore.LIGHTGREEN_EX}{imposto:.2f}{Fore.RESET}')
#     print(f'{15 * '='}')
    
for item in range(len(lista_precos)):
    imposto = 0.10
    produto_imposto = lista_precos[item] * (1 + imposto)
    print(f'O valor do item - {Fore.CYAN}{lista_produtos[item].capitalize()}{Fore.RESET} é {Fore.BLUE}R${lista_precos[item]:.2f}{Fore.RESET}')
    print(f'{20 * '='}')
    print(f'O valor do item - {Fore.LIGHTGREEN_EX}{lista_produtos[item].capitalize()}{Fore.RESET} fica {Fore.LIGHTRED_EX}R${produto_imposto:.2f}{Fore.RESET} com o imposto de 10 % aplicado.')
    print(f'{20 * '='}')
print('')
print('FIM DO PROGRAMA')
print('')