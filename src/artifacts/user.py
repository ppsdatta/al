"""


"""

from globals import SESSION
from artifacts import get_resource, get_stuffs


SLAM_RESOURCE = 'api/v1/user/{0}/slam'
PROFILE_RESOURCE = 'api/v1/user/{0}/profile'
MY_CARDS_RESOURCE = 'api/v1/user/{0}/cards'
MY_ASSIGNMENTS_RESOURCE = 'api/v1/user/{0}/assignments'
COWORKERS_RESOURCE = 'api/v2/user/{0}/coworkers'
BOARDS_RESOURCE = 'api/v1/user/{0}/boards'


def get_slam():
    return get_resource(SLAM_RESOURCE)


def get_profile():
    return get_resource(PROFILE_RESOURCE)


def greet_message():
    message = ''

    # here goes user info getting part (first name etc.)
    profile = get_profile()
    profile_message = ''
    if profile[0]:
        user_profile = profile[1].json()
        SESSION['user_profile'] = user_profile

        profile_message = 'Hi, {}!'.format(user_profile['first_name']) + '\n'
        message += profile_message

    # here we get slam status
    slam_status = get_slam()
    slam_message = ''
    if slam_status[0]:
        status = slam_status[1].json()['status']
        if status == 'SLAMMED':
            slam_message = 'Oh, you seem to be under pressure...!'
        elif status == 'NO_STATUS':
            slam_message = 'Looks like you have not updated your workload status.'
        else:
            slam_message = 'Looks like you\'re comfortable with current workload, great!'

        message += slam_message + '\n'

    return message


def my_cards():
    return get_stuffs(MY_CARDS_RESOURCE, 'card')


def my_assignments():
    return get_stuffs(MY_ASSIGNMENTS_RESOURCE, 'assignment')


def my_comembers():
    return get_stuffs(COWORKERS_RESOURCE, 'member', json_key='members')


def my_groups():
    return get_stuffs(COWORKERS_RESOURCE, 'group', json_key='groups')


def my_boards():
    return get_stuffs(BOARDS_RESOURCE, 'board')


def who():
    return 'You are {}, your email is {}'.format(SESSION['user_profile']['sort_name'], SESSION['user_profile']['email'])

