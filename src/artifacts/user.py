"""


"""

from globals import SESSION
from auth import ALRequester


SLAM_RESOURCE = 'api/v1/user/{0}/slam'
PROFILE_RESOURCE = 'api/v1/user/{0}/profile'


def get_resource(resource):
    sess = SESSION['session']
    uid = SESSION['uid']
    if sess is None:
        return ''
    return ALRequester.request(resource.format(uid))


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



