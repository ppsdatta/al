"""

Command line client


"""
import readline
from lang import prepare, parser
from cmdline.io import *
from auth import ALSession
from artifacts.user import greet_message


GOOGLE_SPEECH_API_DATA = '''
'''


def login():
    uname = normal_input('user name: ')
    password = password_input('password: ')
    uid = ALSession(uname, password).authenticate()

    if uid is None or uid is False:
        display('... something went wrong, please re-login.')
        login()
    else:
        display(greet_message())


def voice_input():
    import speech_recognition as sr
    import re

    display('>> Say something... ')

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    if audio:
        data = None
        try:
            data = r.recognize_google_cloud(audio, credentials_json=GOOGLE_SPEECH_API_DATA)
        except:
            display('I could not recognize that...! :-(')
        if data:
            display('I think you said: {}'.format(data))

            if re.match(r'.*stop.*', data):
                display('Stopping the listener now...')
                return False
            else:
                display_result(parser.parse(str(data)))
                return True
    else:
        display('I did not get that...! :-(')
        return False


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
        elif data == 'listen':
            more = voice_input()
            while more:
                more = voice_input()
        else:
            display_result(parser.parse(data))
    banner('bye')


