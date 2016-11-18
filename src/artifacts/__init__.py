"""



"""

from colorama import Fore, Back, Style
from globals import SESSION
from auth import ALRequester
from textblob.blob import Word


class Artifact:
    def __init__(self):
        self.title = ''
        self.data_dict = dict()

    @staticmethod
    def shorten(txt, limit=20):
        if len(txt) <= limit:
            return txt
        else:
            return txt[:(limit - 3)] + '...'

    def describe(self):
        display_str = ''
        display_str += Back.LIGHTBLUE_EX + Fore.WHITE + self.__class__.__name__.upper() + ' ~ ' + str(self.title) + Back.RESET + '\n'
        for k in sorted(self.data_dict.keys()):
            display_str += '\t\t' + Fore.RED + k.upper() + ': ' + Fore.BLUE + str(self.data_dict[k]) + '\n'
        return display_str


class Card(Artifact):
    def __init__(self, json):
        super().__init__()
        self.title = json['title']
        self.data_dict['id'] = json['id']
        self.data_dict['description'] = self.shorten(json['description'])
        self.data_dict['direct_url'] = json['direct_url']


class Assignment(Artifact):
    def __init__(self, json):
        super().__init__()
        self.title = json['name']
        self.data_dict = dict(due_date=json['due_date'],
                              due_time=json['due_time'],
                              project_name=json['project_name'],
                              work_type=json['type'])


class Member(Artifact):
    def __init__(self, memjson):
        super().__init__()
        self.title = memjson['name']
        self.data_dict = dict(email=memjson['email'],
                              member_type=memjson['type'])


class Group(Artifact):
    def __init__(self, gjson):
        super().__init__()
        self.title = gjson['name']
        self.data_dict = dict(description=gjson['description'],
                              members=' '.join([m['name'] for m in gjson['members']]))


class Board(Artifact):
    pass


KLASS_MAP = {
    'card': Card,
    'assignment': Assignment,
    'member': Member,
    'group': Group
}


def get_resource(resource):
    sess = SESSION['session']
    uid = SESSION['uid']
    if sess is None:
        return ''
    return ALRequester.request(resource.format(uid))


def get_stuffs(resource, name, json_key=None):
    klass = KLASS_MAP[name]
    results = get_resource(resource)
    if results[0]:
        rs = results[1].json()
        if not (json_key is None):
            rs = rs[json_key]

        if isinstance(rs, list):
            return [Word(name).pluralize()] + [klass(aJson) for aJson in rs]
        else:
            return [name, klass(rs)]
    else:
        return 'No result for ' + Word(name).pluralize()



