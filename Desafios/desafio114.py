import urllib
import urllib.request
import urllib.error
from colorama import Fore

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print(f'{Fore.RED}O site não está acessível no momento.{Fore.RESET}')
else:
    print(f'{Fore.GREEN}Consegui acessar o site com sucesso!{Fore.RESET}')
    print(site.read())