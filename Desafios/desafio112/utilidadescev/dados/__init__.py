from colorama import Fore


def leia_dinheiro(msg):
    valido = False
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'{Fore.RED}[ERRO] >> {Fore.YELLOW}"{entrada.upper()}"{Fore.RESET} {Fore.LIGHTRED_EX}é um preço INVÁLIDO{Fore.RESET}')
        else:
            valido = True
            return float(entrada)