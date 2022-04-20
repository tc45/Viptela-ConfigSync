import requests
from vmanage.api.authentication import Authentication
from vmanage.api.device import Device
from vmanage.data.template_data import TemplateData
from vmanage.api.device_templates import DeviceTemplates
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

    # def _send_request(self, url, method='get', headers=None, body=None, params=None):
    #     self.log.debug('Sending request to Vmanage')
    #     request_method = getattr(requests, method)
    #     if not headers:
    #         headers = self.base_headers
    #
    #     self.log.debug(f'Using URL: {url}')
    #     self.log.debug(f'Using method: {method}')
    #     self.log.debug(f'Using headers: {str(headers)}')
    #     self.log.debug(f'Using body: {str(body)}')
    #     self.log.debug(f'Using query strings: {str(params)}')
    #
    #     response = request_method(url, verify=False, headers=headers, json=body, params=params)
    #     status_code = response.status_code
    #     response_body = response.json()
    #     self.log.debug(f'Got status code: {str(status_code)}')
    #     self.log.debug(f'Got response body: {str(response_body)}')
    #     if status_code != 200:
    #         msg = response_body.get('message', 'Request to Vmanage unsuccessful.')
    #     return response_body

    def login_sdk(self):
        self.log.debug(f'Login to Viptela vManage with Python SDK at host {self.host}.')
        self.session = Authentication(host=self.host, user=self.username, password=self.password,
                                 port=self.port).login()
        self.cookie = self.session.cookies._cookies[self.host]["/"]["JSESSIONID"]
        self.log.debug(f'Viptela provided authentication cookie: {self.session.cookies._cookies[self.host]["/"]["JSESSIONID"]}.')

    # def logout_sdk(self):
    #     self.log.debug(f'Logging out of Viptela vManage with Python SDK at host {self.host}.')
    #
    #     url = f"{self.base_url}logout"
    #     response = HttpMethods(self.session, url).request('GET')
    #     result = ParseMethods.parse_data(response)
    #     return result

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

    def get_template_info(self):
        # Extract and print template data
        template_data = TemplateData(self.session, self.host, port=self.port)
        exported_device_template_list = template_data.export_device_template_list()
        return exported_device_template_list

    def get_config_info(self, devices):
        device_templates = DeviceTemplates(self.session, self.host, port=self.port)
        device_configs = []
        for hostname, uuid in devices:
            device_config = device_templates.get_device_running_config(uuid)
            config = {
                'device_name': hostname,
                'config': device_config
            }
            device_configs.append(config)

        return device_configs
