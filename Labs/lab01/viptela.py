import requests
from vmanage.api.authentication import Authentication
from vmanage.api.device import Device


class ViptelaClient:

    def __init__(self, host, port=443, username='admin', password='admin', log=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.log = log
        if not log:
            raise Exception('The logger should not be None.')

        self.cookie = None
        self.session = None
        self.base_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        self.base_url = f'https://{self.host}:{self.port}/'

        requests.packages.urllib3.disable_warnings()

        self.log.debug('ViptelaClient class initialization finished.')

    def login_sdk(self):
        self.log.debug(f'Login to Viptela vManage with Python SDK at host {self.host}.')
        self.session = Authentication(host=self.host, user=self.username, password=self.password,
                                 port=self.port).login()
        self.cookie = self.session.cookies._cookies[self.host]["/"]["JSESSIONID"]
        self.log.debug(f'Viptela provided authentication cookie: {self.session.cookies._cookies[self.host]["/"]["JSESSIONID"]}.')
