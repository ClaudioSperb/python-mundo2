from PyInstaller.depend.imphookapi import PreSafeImportModuleAPI
from colorama import Fore
from time import sleep

#FUNÇÃO QUE PERSONALIZA O TITULO
def titulo(msg):
    tam = len(msg)
    print('=-' * tam)
    print(msg.center(tam * 2))
    print('=-' * tam)
titulo('\033[0;30;44mCALCULE A AREA DO SEU TERRENO\033[0m')

def area(a, b):
    area_terreno = a * b
    print(f'Voce tem as seguintes medida => {a} m de Comprimento X {b} m de Largura')
    return f'A área total do seu terreno é {area_terreno} m²'

#PROGRAMA PRINCIPAL
while True:
    comprimento = float(input('Comprimento do Terreno: '))
    largura = float(input('Largura do Terreno: '))
    print(area(comprimento, largura))

    res = str(input('Quer calcular a área de mais terrenos? [S / N] ')).upper()[0]
    if res == 'N':
        print('ENCERRANDO')
        sleep(0.5)
        break

print('VOLTE SEMPRE')