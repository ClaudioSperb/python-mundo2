from Desafios.desafio109 import moeda

num = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, False)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, False)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num, 10, False)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(num, 13, False)}')
