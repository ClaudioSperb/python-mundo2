#PRATICANDO FUNÇÕES
def saudacao(msg):
   return f'Ola {msg}, seja bem vindo!'

def maior_menor(num):
    if num >= 18:
        return f'Você tem {num} anos. É maior de idade!'
    else:
        return f'Voce tem {num} anos. É menor de idade!'

#Programa Principal
nome = str(input('Digite seu nome: '))
print(saudacao(nome))

num = int(input(f'Digite sua idade {nome}: '))
print(maior_menor(num))
