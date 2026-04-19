from time import sleep

print(f'{"=" * 10} PROGRESSÃO ARITIMÉTICA {"=" * 10}')

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10 #O PROGRAMA COMEÇA QUERENDO MOSTRAR 10 TERMOS

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} => ', end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? [0 para sair]: '))
print(f'Progressão finalizada com {total} de termos mostrados')