cadastro_geral = []

def cadastro(nome, idade, lista_destino):
    pessoa = dict(nome=nome, idade=idade)

    # Adiciona a pessoa diretamente na lista que passamos
    lista_destino.append(pessoa)

#Programa Principal
while True:
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))

    # Chama a função DENTRO do loop a cada pessoa digitada
    cadastro(nome, idade, lista_destino=cadastro_geral)

    res = str(input('Quer continuar [S/N]: ')).strip().upper()
    if res == 'N':
        print('Finalizando Cadastro...')
        break

# Exibe o resultado final
print("📋 Lista final cadastrada:")
print(cadastro_geral)