from lang.actions import *
from lang.guy import AL

TRAINING_DATA = {
    'blank': {
        'action': blank,
        'training_data': [
            'great',
            'ummm...',
            'ok',
            'alright',
            'really',
            'yes',
            'no'
        ]
    },
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
        'action': my_card,
        'training_data': [
            'cards mine',
            'my cards',
            'all cards',
            'show my cards',
            'show cards mine',
            'cards assigned me',
            'cards I working on',
            'my work',
            'what I working',
            'I work card'
        ],
    },
    'joke': {
        'action': joke,
        'training_data': [
            'tell me joke',
            'tell joke',
            'feelind sad',
            'feeling busy',
            'make me happy',
            'time pass',
            'tell me something',
            'joke',
            'another joke'
        ]
    }
}


def train():
    ali = AL().get()
    ali.train(TRAINING_DATA)


def clear_data(raw_data):
    return [raw_data]


