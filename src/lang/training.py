from lang.actions import *
from lang.guy import AL

from textblob import TextBlob

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
            'card mine',
            'my card',
            'all card',
            'show my card',
            'show cards mine',
            'card assigned me',
            'card I working on',
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
    blob = TextBlob(raw_data)
    blob.correct()
    data = []
    for s in blob.sentences:
        ws = [w.singularize() for w in s.words]
        ws = ' '.join(ws)
        data.append(ws)
    return data



