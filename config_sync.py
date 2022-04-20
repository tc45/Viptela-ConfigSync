from viptela import ViptelaClient
import argparse
import logging
import yaml
import helpers


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c", help="Path to the configuration file", default="viptela.cfg")
    parser.add_argument("--debug", "-d", help="Display debug logs", action="store_true")
    return parser.parse_args()


def init_logger(log_level=logging.INFO):
    logger = logging.getLogger(__file__)
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    if log_level == 10:
        # create file handler which logs even debug messages
        fh = logging.FileHandler('log_file.txt')
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG)
        logger.addHandler(fh)
    return logger


class ConfigSync:

    def __init__(self, config, log):
        self.log = log
        self.config_file = config
        self.log.info('Initializing ConfigSync Class.')
        self.config = self._parse_config(config)
        self.viptela = self._init_viptela_client(self.config)
        self.log.debug('Finished initializing the configSync class.')

    def _parse_config(self, config_file):
        self.log.info('Parsing the configuration file.')
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        self.log.debug(f'The following parameters were received: {config}')
        return config

    def _init_viptela_client(self, config):
        self.log.info('Initializing ViptelaClient class.')
        host = config.get('viptela_host')
        username = config.get('viptela_username')
        password = config.get('viptela_password')
        port = config.get('viptela_port')
        self.log.debug(f'Username is {username} and password is {password}')
        viptela = ViptelaClient(host, username=username, password=password, port=port, log=self.log)
        self.log.info('Login to Viptela.')
        viptela.login_sdk()
        return viptela

    def logout_viptela_client(self):
        response = self.viptela.logout_sdk()
        print(response)

    def cs_get_all_device_info(self):
        if type == "":
            self.log.info(f"Type must be set for get_all_device_info function to return data.")
            return []
        vedges = self.viptela.get_devices_list('vedges')
        controllers = self.viptela.get_devices_list('controllers')
        return vedges, controllers

    def cs_get_all_template_info(self):
        return self.viptela.get_template_info()

    def cs_get_config_info(self, devices):
        return self.viptela.get_config_info(devices)

    def cs_save_log_file(self):
        helpers.save_to_text('log_file.txt', log)


if __name__ == "__main__":
    args = parse_arguments()

    if args.debug:
        log = init_logger(logging.DEBUG)
    else:
        log = init_logger()

    # Instantiate ConfigSync which will launch connection to Viptela, setup logging, and
    # load configuration from config file.
    cs = ConfigSync(config=args.config, log=log)
    # Get Device info for vedges and controllers
    vedge_list, controller_list = cs.cs_get_all_device_info()
    vedge_table = helpers.print_device_table(vedge_list)
    controller_table = helpers.print_device_table(controller_list)
    # Get template info and print using table parser
    device_templates = cs.cs_get_all_template_info()
    helpers.print_template_table(device_templates)

    # Get Configs for devices
    vedge_configs = cs.cs_get_config_info(vedge_table)
    controller_configs = cs.cs_get_config_info(controller_table)

    # Save Configs for devices to disk
    for device in vedge_configs:
        cs.log.debug(f'Writing file {device["device_name"]} to disk.')
        helpers.save_to_text(device['device_name'], device['config'])
    for device in controller_configs:
        cs.log.debug(f'Writing file {device["device_name"]} to disk.')
        helpers.save_to_text(device['device_name'], device['config'])



