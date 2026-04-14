from colorama import Fore
from time import sleep

print(f'{15 * '='} ANALISANDO OS PESOS {15 * '='}')
# --- CONJUNTOS DE DADOS ---
pesos = []
nomes = []
idades = []
# --- CRIANDO O LOOP DE INPUT ---
for c in range(1):
    print(f'{5 * '='} COLETANDO DADOS DA PRIMEIRA PESSOA {5 * '='}')
    nome = str(input('Digite seu Nome: ')).upper()
    idade = int(input('Digite sua Idade: '))
    peso = float(input('Digite seu Peso: '))
    pesos.append(peso)
    nomes.append(nome)
    idades.append(idade)
print(f'Seja bem vindo {nome} !!!')
print(f'Seu peso é de {peso}Kg e sua idade é {idade} anos de idade. ')

for c in range(1):
    print(f'{5 * '='} COLETANDO DADOS DA SEGUNDA PESSOA {5 * '='}')
    nome = str(input('Digite seu Nome: ')).upper()
    idade = int(input('Digite sua Idade: '))
    peso = float(input('Digite seu Peso: '))
    pesos.append(peso)
    nomes.append(nome)
    idades.append(idade)
print(f'Seja bem vindo {nome} !!!')
print(f'Seu peso é de {peso}Kg e sua idade é {idade} anos de idade. ')

for c in range(1):
    print(f'{5 * '='} COLETANDO DADOS DA TERCEIRA PESSOA {5 * '='}')
    nome = str(input('Digite seu Nome: ')).upper()
    idade = int(input('Digite sua Idade: '))
    peso = float(input('Digite seu Peso: '))
    pesos.append(peso)
    nomes.append(nome)
    idades.append(idade)
print(f'Seja bem vindo {nome} !!!')
print(f'Seu peso é de {peso}Kg e sua idade é {idade} anos de idade. ')

print(nomes, idades, pesos)