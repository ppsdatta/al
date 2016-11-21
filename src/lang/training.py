from lang.actions import *
from lang.guy import AL

from textblob import TextBlob

TRAINING_DATA = {
    'greetings': {
        'action': greet,
        'training_data': [
            'hello',
            'hi',
            'yo',
            'good day',
            'good morning',
            'good evening',
            'good night',
            'hallo',
            'hullo',
            'howdy'
        ]
    },
    'my_cards': {
        'action': my_cards,
        'training_data': [
            'card mine',
            'my card',
            'all cards',
            'show card',
            'show card mine',
            'card I working',
            'card'
        ],
    },
    'my_boards': {
        'action': my_boards,
        'training_data': [
            'board mine',
            'my board',
            'all board',
            'show board',
            'show board mine',
            'board I working',
            'board',
            'boards'
        ],
    },
    'my_assignments': {
        'action': my_assignments,
        'training_data': [
            'assignment mine',
            'my assignment',
            'all assignment',
            'show assignment',
            'show assignment mine',
            'things I work',
            'assignment',
            'assignments',
            'work',
            'working',
            'show work',
            'what i working'
        ],
    },
    'my_coworkers': {
        'action': my_coworkers,
        'training_data': [
            'my co-worker',
            'my co-worker',
            'my coworker',
            'people',
            'member',
            'people I know',
            'fellow',
            'members',
            'persons',
            'all members',
            'working with'
        ],
    },
    'my_groups': {
        'action': my_groups,
        'training_data': [
            'my groups',
            'group',
            'show my group',
            'group information',
            'group detail',
            'group',
            'people in groups',
            'group persons',
            'group members'
        ],
    },
    'who': {
        'action': who,
        'training_data': [
            'who',
            'who am i',
            'i am who',
            'myself',
            'tell me about me',
            'say my name',
            'show my info',
            'about me',
            'me',
            'myself',
            'I am'
        ]
    },
    'search': {
        'action': search,
        'training_data': [
            'search for',
            'find',
            'find for',
            'search',
            'find for me',
            'can you search',
            'please find',
            'please search'
        ]
    }
}

REGEX_GRAMMAR = {
    'blank': [
        r''
    ],
    'greetings': [
        r'^(hello|hi|howdy|good|yo|hallo|hullo'
    ],
    'my_cards': [
        r'.*show.*(me)?.*my.*cards.*'
    ],
    'joke': [
        r'.*(tell|say).*(me)?.*joke.*',
        r'.*feeling.*(sad|down).*',
        r'.*make.*happy.*'
    ]
}


def train():
    ali = AL().get()
    ali.train(TRAINING_DATA)


def clear_data(raw_data):
    blob = TextBlob(raw_data)
    blob.correct()
    data = []
    for s in blob.sentences:
        ws = [w.singularize() for w in s.words]
        ws = ' '.join(ws)
        data.append(ws)
    return data


