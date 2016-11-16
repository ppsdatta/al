"""

All command actions

"""

from lang.jokes import all_jokes
import random
from artifacts import Card


def my_card(*args):
    return ['showing your cards',
            Card('1223', 'Card 1', 'http://www.service.projectplace.com/card/1223'),
            Card('1224', 'Card 2', 'http://www.service.projectplace.com/card/1224')]


def greet(*args):
    return 'Hi there!'


def joke(*args):
    i = random.randint(0, len(all_jokes) - 1)
    return all_jokes[i]


def blank(*args):
    r = random.randint(1, 10)
    if r <= 5:
        return 'yep...'
    else:
        return 'well...'
