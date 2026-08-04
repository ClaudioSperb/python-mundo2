from Desafios.desafio112.utilidadescev import moeda
from Desafios.desafio112.utilidadescev.dados import leia_dinheiro

num = leia_dinheiro('Digite um valor: R$')
moeda.resumo(num, 30, 50)
