from colorama import Fore
from time import sleep

print(f'{15 * '='} ANALISANDO OS PESOS {15 * '='}')
# --- CONJUNTOS DE DADOS ---
pesos = []
nomes = []
idades = []
# --- CRIANDO O LOOP DE INPUT --
for pessoa in range(0, 3):
    print(f'{5 * '='}{Fore.CYAN}COLETANDO OS DADOS DA {pessoa + 1}ª PESSOA{Fore.RESET} {5 * '='}')
    
    for dados in range(1):
        nome = str(input('Digite seu nome: ')).upper()
        idade = int(input('Digite sua idade: '))
        peso = float(input('Digite seu peso: '))
        
        nomes.append(nome)
        idades.append(idade)
        pesos.append(peso)
    print(f'{10 * '=-'}')
    print(f'Seja bem vindo {Fore.LIGHTGREEN_EX}{nome}{Fore.RESET}')
    print(f'Seu peso é de {Fore.LIGHTGREEN_EX}{peso}{Fore.RESET} Kg e sua idade é de {Fore.LIGHTGREEN_EX}{idade}{Fore.RESET} anos')
    
# --- PEGANDO OS DADOS E ANALISANDO ---

print(f'{20 * '='}')
print('ANALISANDO ....')
sleep(1)
print(f'{20 * '='}')
maior_peso = max(pesos)
menor_peso = min(pesos)
indice_maior = pesos.index(maior_peso)
indice_menor = pesos.index(menor_peso)
print(f'O maior peso é {maior_peso} referente a {nomes[indice_maior]}')
print(f'O menor peso é {menor_peso} referente a {nomes[indice_menor]}')

sleep(0.8)

maior_idade = max(idades)
menor_idade = min(idades)
indiceIdade_maior = idades.index(maior_idade)
indiceIdade_menor = idades.index(menor_idade)
print(f'A maior idade é {maior_idade} referente a {nomes[indiceIdade_maior]}')
print(f'A menor idade é {menor_idade} referente a {nomes[indiceIdade_menor]}')