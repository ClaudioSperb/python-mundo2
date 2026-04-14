from colorama import Fore
from time import sleep

print(f'{15 * '='} ANALISANDO OS PESOS {15 * '='}')
# --- CONJUNTOS DE DADOS ---
pesos = []
nomes = []
idades = []
# --- CRIANDO O LOOP DE INPUT --
for pessoa in range(0, 3):
    print(f'{5 * '='}{Fore.CYAN}COLETANDO OS DADOS DA {pessoa}ª PESSOA{Fore.RESET} {5 * '='}')
    
    for dados in range(1):
        nome = str(input('Digite seu nome: '))
        idade = int(input('Digite sua idade: '))
        peso = float(input('Digite seu peso: '))
        
        nomes.append(nome)
        idades.append(idade)
        pesos.append(peso)
    print(f'{10 * '=-'}')
    print(f'Seja bem vindo {Fore.LIGHTGREEN_EX}{nome}{Fore.RESET}')
    print(f'Seu peso é de {Fore.LIGHTGREEN_EX}{peso}{Fore.RESET} Kg e sua idade é de {Fore.LIGHTGREEN_EX}{idade}{Fore.RESET} anos')
    
# --- PEGANDO OS DADOS E ANALISANDO ---
