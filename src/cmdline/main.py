"""

Command line client


"""

from lang import prepare, parser
from cmdline.io import *
import readline


def main():
    prepare()
    ioinit()
    banner('Welcome! I am AL, your Projectplace assistant')
    while True:
        display('>> ', end='')
        data = input()
        if data == 'exit' or data == 'quit':
            break
        display_result(parser.parse(data))
    banner('bye')


