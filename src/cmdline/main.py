"""

Command line client


"""
import readline
from lang import prepare, parser
from cmdline.io import *
from auth import ALSession
from artifacts.user import greet_message

def login():
    uname = normal_input('user name: ')
    password = password_input('password: ')
    uid = ALSession(uname, password).authenticate()

    if uid is None or uid is False:
        display('... something went wrong, please re-login.')
        login()
    else:
        display(greet_message())


def main():
    prepare()
    ioinit()
    banner('Welcome! I am AL, your Projectplace assistant')
    display('[may the command line be with you...]')

    login()

    while True:
        display('>> ', end='')
        data = input()
        if data == 'exit' or data == 'quit':
            break
        display_result(parser.parse(data))
    banner('bye')


