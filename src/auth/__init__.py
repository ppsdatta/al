"""



"""

import requests
from globals import SESSION

BASE_URL = 'https://local.rnd.projectplace.com'
AUTH_URL = '/login'


def login(uname='', password=''):
    "Returns a tuple of authenticated?, response and session if login is valid"
    headers = {
        'Origin': BASE_URL,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en,es;q=0.8,fr;q=0.6,nl;q=0.4,de;q=0.2,da;q=0.2,no;q=0.2,sv;q=0.2,en-US;q=0.2',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'https://local.rnd.projectplace.com/login',
        'Connection': 'keep-alive',
    }

    data = {
      'uname': uname,
      'password': password,
      'keepmeloggedin': 'yes',
      'lang': 'english'
    }

    session = requests.Session()
    session.post(BASE_URL + AUTH_URL, headers=headers, cookies=dict(), data=data)
    return session


class ALSession():
    def __init__(self, uname, password, base_url=BASE_URL):
        self.uname = uname
        self.password = password
        self.session = None
        self.loggedin = False
        self.uinfo = self.cookies = None

    def authenticate(self):
        global SESSION

        sess = login(self.uname, self.password)

        if sess and (sess.cookies.get_dict() != {}):
            self.loggedin = True
        else:
            print('login error')
            self.loggedin = False
            return False

        self.session = sess
        self.cookies = sess.cookies
        self.uinfo = dict(uid=self.cookies['uid'])

        SESSION['uinfo'] = self.uinfo
        SESSION['session'] = self

        return self.uinfo


class ALRequester:
    @staticmethod
    def request(resource, params={}, method='GET'):
        global SESSION

        sessiono = SESSION['session']
        if sessiono is None:
            return None

        if not sessiono.loggedin:
            return None

        if method == 'GET':
            response = sessiono.session.get(BASE_URL + '/' + resource, data=params, cookies=sessiono.cookies)
        else:
            response = sessiono.session.post(BASE_URL + '/' + resource, data=params, cookies=sessiono.cookies)

        if response.status_code not in (200, 302):
            return False, response
        else:
            return True, response



