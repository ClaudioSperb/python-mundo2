from colorama import Fore

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
print(f'Os número digitados foram {num1} e {num2}.')
if num1 > num2:
    print(f'O numero {Fore.LIGHTBLUE_EX}{num1}{Fore.RESET} é maior que {Fore.LIGHTWHITE_EX}{num2}{Fore.RESET}.')
elif num2 > num1:
    print(f'O numero {Fore.LIGHTWHITE_EX}{num2}{Fore.RESET} é maior que {Fore.LIGHTBLUE_EX}{num1}{Fore.RESET}.')
elif num1 == num2:
    print(f'Os números digitados tem o {Fore.LIGHTYELLOW_EX}mesmo valor{Fore.RESET} !!! ')