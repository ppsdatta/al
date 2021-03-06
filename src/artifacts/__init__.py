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
        self.max_pad = 40

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
            display_str += '\t' + Back.WHITE + Fore.RED + k.upper() + Back.RESET + (' ' * (self.max_pad - len(k))) + \
                           '\t' + Fore.BLUE + str(self.data_dict[k]) + '\n'
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
    def __init__(self, bjson):
        super().__init__()
        self.title = bjson['name']
        self.data_dict = dict(project_id=bjson['project_id'],
                              email=bjson['email'],
                              cards_done=bjson['done_count'],
                              archived=bjson['is_archived'],
                              project=bjson['project']['name'])


class Search(Artifact):
    def __init__(self, sjson):
        super().__init__()

        def get_matched_by_string(highlight):
            s = ''
            for k in highlight.keys():
                s += '{0} => {1}'.format(k, ', '.join(highlight[k]))
            return s

        def get_artifact_details_string(details):
            if not isinstance(details, dict):
                return str(details)

            s = ''
            for k in details.keys():
                if k in ('id', 'name', 'project', 'due_date'):
                    s += '{0}{1}{2} => {3}{4}{5} '.format(Back.LIGHTWHITE_EX, k, Back.RESET,
                                                          Back.LIGHTWHITE_EX, get_artifact_details_string(details[k]),
                                                          Back.RESET)
            return '[' + s.rstrip() + ']'

        self.title = sjson['artifact_details']['name']
        self.data_dict = dict(artifact_type=sjson['artifact_type'],
                              url=sjson['html_url'],
                              matched_by=get_matched_by_string(sjson['highlight']),
                              artifact_details=get_artifact_details_string(sjson['artifact_details']))


KLASS_MAP = {
    'card': Card,
    'assignment': Assignment,
    'member': Member,
    'group': Group,
    'board': Board,
    'search': Search
}


def get_resource(resource):
    sess = SESSION['session']
    uid = SESSION['uid']
    if sess is None:
        return ''
    return ALRequester.request(resource.format(uid))


def search_request(resource, query):
    sess = SESSION['session']
    if sess is None:
        return ''
    return ALRequester.request(resource.format(query))



def get_stuffs(resource, name, json_key=None):
    klass = KLASS_MAP[name]
    results = get_resource(resource)
    return process_result(results, name, klass, json_key)


def get_search_stuffs(resource, query, json_key=None):
    klass = KLASS_MAP['search']
    results = search_request(resource, query)
    return process_result(results, 'search', klass, json_key)


def process_result(results, name, klass, json_key=None):
    if results[0]:
        rs = results[1].json()
        if not (json_key is None):
            rs = rs[json_key]

        if isinstance(rs, list):
            return ['Showing ' + Word(name).pluralize()] + [klass(aJson) for aJson in rs]
        else:
            return ['Showing ' + name, klass(rs)]
    else:
        return 'No result for ' + Word(name).pluralize()

