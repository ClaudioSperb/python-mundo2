from colorama import Fore
from time import sleep
valorProduto = float(input('Digite o valor do produto: '))
aVista = valorProduto - (valorProduto * (10 / 100))
aVistaCartao = valorProduto - (valorProduto * (5 / 100))
tresVezesCartao = valorProduto - (valorProduto * (20 / 100))
print(aVista)