from lang.actions import *
from lang.guy import AL

from textblob import TextBlob

TRAINING_DATA = {
    'my_cards': {
        'action': my_cards,
        'training_data': [
            'card mine',
            'my card',
            'all cards',
            'show card',
            'show card mine',
            'card I working',
            'card',
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
            'I am',
            'hello',
            'hi',
            'hola',
            'greetings',
            'I am',
            'talk to me'
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


