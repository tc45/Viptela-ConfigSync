import requests
from vmanage.api.authentication import Authentication
from vmanage.api.http_methods import HttpMethods
from vmanage.data.parse_methods import ParseMethods


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

    def get_all_tloc_info(self):
        url = f'{self.base_url}dataservice/device/tlocs'
        response = HttpMethods(self.session, url).request('GET', timeout=60)
        result = ParseMethods.parse_data(response)
        return response
