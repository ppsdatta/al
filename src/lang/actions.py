"""

All command actions

"""

from lang.jokes import all_jokes
import random
import artifacts.user as uactions

rand = random.seed()


def my_cards(*args):
    return uactions.my_cards()


def my_boards(*args):
    return uactions.my_boards()


def my_assignments(*args):
    return uactions.my_assignments()


def my_coworkers(*args):
    return uactions.my_comembers()


def my_groups(*args):
    return uactions.my_groups()


def who(*args):
    return uactions.who()


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

