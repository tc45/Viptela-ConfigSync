import requests
from vmanage.api.authentication import Authentication
from vmanage.api.device import Device
from vmanage.api.monitor_network import MonitorNetwork


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

    def get_devices_list(self, type):
        '''
        Get devices uses the Viptela Device API to fetch the list of devices
        either vedges or controllers and returns them in a list of dictionaries.

        :param type: Either 'vedges' or 'controllers'
        :return:
            result (list): Device list
        '''

        # Instantiate new device object to use the Device library
        device = Device(self.session, self.host, port=self.port)
        # Request list of all devices by type specified and store in variable
        device_list = device.get_device_list(type)
        return device_list


    def get_route_table(self, system_ip):
        '''
        Get route table retrieves the routes from selected vedge for later manipulation.
        :param type: DeviceID: DeviceIP address
        :return:
            result (list): route_list
        '''

        # Instantiate new device object to use the Device library
        monitor = MonitorNetwork(self.session, self.host, port=self.port)
        # Request list of all devices by type specified and store in variable
        route_list = monitor.get_ip_route_table(system_ip)
        return route_list
