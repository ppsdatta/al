"""


"""

from globals import SESSION
from auth import ALRequester

SLAM_RESOURCE = 'api/v1/user/{0}/slam'


def get_slam():
    sess = SESSION['session']
    uid = SESSION['uid']
    if sess is None:
        return ''
    return ALRequester.request(SLAM_RESOURCE.format(uid))


def greet_message():
    message = ''

    # here goes user info getting part (first name etc.)

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



