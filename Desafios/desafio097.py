from colorama import Fore

def titulo(texto):
    print('-='*30)
    print(f'{texto}'.center(70))
    print('-=' * 30)
titulo(f'{Fore.RED}{'ADAPTANDO TEXTOS'}{Fore.RESET}')

def escreva(palavra):
    tam = len(palavra)
    print('=-'* tam)
    print(f'{palavra}'.center(tam * 2))
    print('=-'* tam)

escreva('CLAUDIO')
escreva('JOSIANE LACERDA')
escreva('BRIANA SEGATTO PAULO')