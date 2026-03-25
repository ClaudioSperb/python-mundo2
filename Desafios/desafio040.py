from time import sleep
from colorama import Fore

nomeAluno = str(input('Digite o nome do Aluno: ')).upper().strip()
primeiraNota = float(input('Digite a nota da primeira avaliação: '))
segundaNota = float(input('Digite a nota da segunda avaliação: '))
mediaNota = (primeiraNota + segundaNota) / 2
print(f'Ola {nomeAluno}, estamos validando suas notas.')
sleep(2)
print('...................')
sleep(1.5)

if mediaNota < 5.0:
    print(f'Ola {nomeAluno}, sua média foi de {mediaNota:.1f} e voce foi {Fore.LIGHTRED_EX}REPROVADO !!!{Fore.RESET}')
elif mediaNota < 7.0:
    print(f'Ola {nomeAluno}, sua média foi de {mediaNota:.1f} e voce está de {Fore.LIGHTYELLOW_EX}RECUPERAÇÃO !!!{Fore.RESET}')
elif mediaNota >= 7.0:
    print(f'Ola {nomeAluno}, sua média foi de {mediaNota:.1f} e você está {Fore.LIGHTGREEN_EX}APROVADO{Fore.RESET}, parabens e continue assim !!! ')