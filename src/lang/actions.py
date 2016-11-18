"""

All command actions

"""

from lang.jokes import all_jokes
import random
from artifacts.user import my_cards, my_assignments, my_comembers, my_groups

rand = random.seed()


def my_card(*args):
    return my_cards()


def greet(*args):
    return 'Hi there!'


def joke(*args):
    i = random.randint(0, len(all_jokes) - 1)
    return all_jokes[i]


def blank(*args):
    return 'That does not look like anything to me...'


def boards(action_type):
    def show_boards(*args):
        return ['Showing al boards']

    def create_board(*args):
        return ['Creating a board']

    def rename_board(*args):
        return ['Renaming board']

