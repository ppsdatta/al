"""



"""

from colorama import Fore, Back, Style


class Artifact:
    @staticmethod
    def shorten(txt, limit=20):
        if len(txt) <= limit:
            return txt
        else:
            return txt[:(limit - 3)] + '...'

    def describe(self):
        return 'Some artifact'


class Card(Artifact):
    def __init__(self, id, description, url):
        self.id = id
        self.desc = self.shorten(description)
        self.url = url

    def describe(self):
        return Back.WHITE + Fore.RED + 'ID: ' + self.id + Back.RESET + '\t\t' + \
               Back.WHITE + Fore.RED + self.desc + Back.RESET + '\t\t' + \
               Back.WHITE + Fore.RED + self.url

