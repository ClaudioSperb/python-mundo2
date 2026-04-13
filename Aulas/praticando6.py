from colorama import Fore
with open("Aulas/vendasloja.txt", "r") as arquivo:
    texto = arquivo.read()
#    print(texto)
lista_texto = texto.split('\n')
lista_texto = lista_texto[1:]
#print(lista_texto)
#PARA CADA LINHA NO MEU ARQUIVO, EU QUERO SOMAR O VALOR QUE ESTIVER DEPOIS DO PONTO E VIRGULA
faturamento = 0

for linha in lista_texto:
    posicao_pv = linha.find(';')
    valor = linha[posicao_pv + 1 : ]
    valor_conv = float(valor)
    faturamento += valor_conv
print(f'o Valor do faturamento total da empresa é de {Fore.GREEN}R${faturamento:.2f}{Fore.RESET} Reais')