"""

Main I/O interfaces

"""

from colorama import init, Back, Fore, Style
from artifacts import Artifact


def ioinit():
    init(autoreset=True)


def banner(txt):
    print(Fore.RED + Back.GREEN + txt)


def al_speak(txt):
    print(Style.DIM + Fore.BLUE + 'AL>> ', end='')
    print(Fore.CYAN + txt)


def display(text, *args, **kargs):
    print(Fore.RED + text, *args, **kargs)


def display_result(result, *args, **kargs):
    if isinstance(result, str):
        al_speak(result)
    elif isinstance(result, Artifact):
        print(result.describe())
    elif isinstance(result, list):
        for r in result:
            display_result(r)
    else:
        display_result('Does not seem like anything to me...!')
    print()
