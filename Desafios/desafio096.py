from colorama import Fore

def titulo(texto):
    print('-='*30)
    print(f'{texto}'.center(70))
    print('-=' * 30)
titulo(f'{Fore.RED}{'AREA DO TERRENO (m²)'}{Fore.RESET}')

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área do terreno {largura:.1f} x {comprimento} é {a}m²')
#PROGRAMA PRINCIPAL

l = float(input('Qual a largura do terreno (m): '))
c = float(input('Qual o comprimento do terreno (m): '))

print(60 * '=')
area(l, c)

titulo(F'{Fore.GREEN}{'FIM DO PROGRAMA'}{Fore.RESET}')
